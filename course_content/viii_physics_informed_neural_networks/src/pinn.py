"""Small PyTorch PINN implementation intended for inspection and modification."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import time

import numpy as np
import pandas as pd
import torch
from torch import nn

from .heat_equation import HeatEquationConfig


def set_seed(seed: int) -> None:
    np.random.seed(seed)
    torch.manual_seed(seed)


class HeatPINN(nn.Module):
    """Fully connected network with scaled `x` and `t` inputs."""

    def __init__(
        self,
        config: HeatEquationConfig,
        hidden_width: int = 32,
        hidden_layers: int = 3,
    ) -> None:
        super().__init__()
        self.config = config
        layers: list[nn.Module] = []
        widths = [2] + [hidden_width] * hidden_layers + [1]
        for input_width, output_width in zip(widths[:-2], widths[1:-1]):
            layers.extend([nn.Linear(input_width, output_width), nn.Tanh()])
        layers.append(nn.Linear(widths[-2], widths[-1]))
        self.network = nn.Sequential(*layers)

    def forward(self, xt: torch.Tensor) -> torch.Tensor:
        scaled = torch.cat(
            (
                2.0 * xt[:, 0:1] / self.config.length_m - 1.0,
                2.0 * xt[:, 1:2] / self.config.final_time_s - 1.0,
            ),
            dim=1,
        )
        return self.config.initial_amplitude_K * self.network(scaled)


def pde_residual(
    model: nn.Module,
    xt: torch.Tensor,
    alpha_m2_s: torch.Tensor | float,
) -> torch.Tensor:
    """Return dimensional residual `T_t - alpha*T_xx` in K/s."""

    xt_grad = xt.detach().clone().requires_grad_(True)
    temperature = model(xt_grad)
    first = torch.autograd.grad(
        temperature,
        xt_grad,
        grad_outputs=torch.ones_like(temperature),
        create_graph=True,
    )[0]
    temperature_t = first[:, 1:2]
    temperature_x = first[:, 0:1]
    temperature_xx = torch.autograd.grad(
        temperature_x,
        xt_grad,
        grad_outputs=torch.ones_like(temperature_x),
        create_graph=True,
    )[0][:, 0:1]
    return temperature_t - alpha_m2_s * temperature_xx


def sample_training_points(
    config: HeatEquationConfig,
    n_domain: int,
    n_boundary: int,
    n_initial: int,
    seed: int,
) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
    rng = np.random.default_rng(seed)
    domain = np.column_stack(
        (
            rng.uniform(0.0, config.length_m, n_domain),
            rng.uniform(0.0, config.final_time_s, n_domain),
        )
    )
    boundary_time = rng.uniform(0.0, config.final_time_s, n_boundary)
    left = np.column_stack((np.zeros(n_boundary), boundary_time))
    right = np.column_stack((np.full(n_boundary, config.length_m), boundary_time))
    initial_x = rng.uniform(0.0, config.length_m, n_initial)
    initial = np.column_stack((initial_x, np.zeros(n_initial)))
    initial_temperature = config.initial_amplitude_K * np.sin(
        np.pi * initial_x / config.length_m
    )
    return tuple(
        torch.tensor(value, dtype=torch.float32)
        for value in (domain, left, right, initial, initial_temperature[:, None])
    )


@dataclass
class TrainingResult:
    model: HeatPINN
    history: pd.DataFrame
    elapsed_s: float
    alpha_estimate_m2_s: float | None = None


def train_forward(
    config: HeatEquationConfig,
    iterations: int = 5000,
    n_domain: int = 2000,
    n_boundary: int = 100,
    n_initial: int = 100,
    learning_rate: float = 1.0e-3,
    seed: int = 54403,
    report_every: int = 100,
) -> TrainingResult:
    """Train a forward PINN with fixed, reproducible collocation points."""

    set_seed(seed)
    model = HeatPINN(config)
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    domain, left, right, initial, initial_temperature = sample_training_points(
        config, n_domain, n_boundary, n_initial, seed
    )
    history: list[dict[str, float]] = []
    start = time.perf_counter()
    for iteration in range(iterations + 1):
        optimizer.zero_grad()
        residual = pde_residual(model, domain, config.alpha_m2_s)
        loss_pde = torch.mean((residual * config.final_time_s / config.initial_amplitude_K) ** 2)
        loss_bc = (
            torch.mean((model(left) / config.initial_amplitude_K) ** 2)
            + torch.mean((model(right) / config.initial_amplitude_K) ** 2)
        )
        loss_ic = torch.mean(
            ((model(initial) - initial_temperature) / config.initial_amplitude_K) ** 2
        )
        loss = loss_pde + loss_bc + loss_ic
        loss.backward()
        optimizer.step()
        if iteration % report_every == 0 or iteration == iterations:
            history.append(
                {
                    "iteration": iteration,
                    "loss_total": float(loss.detach()),
                    "loss_pde": float(loss_pde.detach()),
                    "loss_bc": float(loss_bc.detach()),
                    "loss_ic": float(loss_ic.detach()),
                }
            )
    return TrainingResult(model, pd.DataFrame(history), time.perf_counter() - start)


def train_inverse(
    observations_csv: str | Path,
    config: HeatEquationConfig,
    iterations: int = 5000,
    n_domain: int = 2000,
    n_boundary: int = 100,
    n_initial: int = 100,
    initial_alpha_m2_s: float = 5.0e-6,
    learning_rate: float = 1.0e-3,
    seed: int = 54403,
    report_every: int = 100,
) -> TrainingResult:
    """Estimate a positive thermal diffusivity using sparse observations."""

    if initial_alpha_m2_s <= 0:
        raise ValueError("initial_alpha_m2_s must be positive")
    set_seed(seed)
    model = HeatPINN(config)
    log_alpha = nn.Parameter(torch.tensor(np.log(initial_alpha_m2_s), dtype=torch.float32))
    optimizer = torch.optim.Adam([*model.parameters(), log_alpha], lr=learning_rate)
    domain, left, right, initial, initial_temperature = sample_training_points(
        config, n_domain, n_boundary, n_initial, seed
    )
    observations = pd.read_csv(observations_csv)
    required = {"x_m", "t_s", "T_excess_K"}
    if not required.issubset(observations.columns):
        raise ValueError(f"Observation file must contain {sorted(required)}")
    observed_xt = torch.tensor(
        observations[["x_m", "t_s"]].to_numpy(), dtype=torch.float32
    )
    observed_temperature = torch.tensor(
        observations[["T_excess_K"]].to_numpy(), dtype=torch.float32
    )

    history: list[dict[str, float]] = []
    start = time.perf_counter()
    for iteration in range(iterations + 1):
        optimizer.zero_grad()
        alpha = torch.exp(log_alpha)
        residual = pde_residual(model, domain, alpha)
        loss_pde = torch.mean((residual * config.final_time_s / config.initial_amplitude_K) ** 2)
        loss_bc = (
            torch.mean((model(left) / config.initial_amplitude_K) ** 2)
            + torch.mean((model(right) / config.initial_amplitude_K) ** 2)
        )
        loss_ic = torch.mean(
            ((model(initial) - initial_temperature) / config.initial_amplitude_K) ** 2
        )
        loss_data = torch.mean(
            ((model(observed_xt) - observed_temperature) / config.initial_amplitude_K) ** 2
        )
        loss = loss_pde + loss_bc + loss_ic + loss_data
        loss.backward()
        optimizer.step()
        if iteration % report_every == 0 or iteration == iterations:
            history.append(
                {
                    "iteration": iteration,
                    "loss_total": float(loss.detach()),
                    "loss_pde": float(loss_pde.detach()),
                    "loss_bc": float(loss_bc.detach()),
                    "loss_ic": float(loss_ic.detach()),
                    "loss_data": float(loss_data.detach()),
                    "alpha_m2_s": float(alpha.detach()),
                }
            )
    estimate = float(torch.exp(log_alpha).detach())
    return TrainingResult(
        model,
        pd.DataFrame(history),
        time.perf_counter() - start,
        alpha_estimate_m2_s=estimate,
    )


def predict(model: nn.Module, x_m: np.ndarray, time_s: np.ndarray) -> np.ndarray:
    """Predict excess temperature at paired coordinate arrays."""

    xt = torch.tensor(np.column_stack((x_m, time_s)), dtype=torch.float32)
    model.eval()
    with torch.no_grad():
        return model(xt).cpu().numpy().ravel()
