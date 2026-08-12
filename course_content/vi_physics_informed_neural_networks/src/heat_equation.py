"""Analytical and finite-difference baselines for one-dimensional heat conduction."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class HeatEquationConfig:
    """Dimensional parameters for the teaching problem.

    Temperature is an excess temperature relative to the fixed boundaries.
    """

    length_m: float = 0.10
    alpha_m2_s: float = 1.0e-5
    initial_amplitude_K: float = 50.0
    final_time_s: float = 200.0

    def __post_init__(self) -> None:
        if self.length_m <= 0:
            raise ValueError("length_m must be positive")
        if self.alpha_m2_s <= 0:
            raise ValueError("alpha_m2_s must be positive")
        if self.final_time_s <= 0:
            raise ValueError("final_time_s must be positive")

    def fourier_number(self, time_s: float | np.ndarray) -> float | np.ndarray:
        """Return Fo = alpha*t/L^2."""

        return self.alpha_m2_s * np.asarray(time_s) / self.length_m**2


def analytical_temperature(
    x_m: np.ndarray | float,
    time_s: np.ndarray | float,
    config: HeatEquationConfig = HeatEquationConfig(),
    alpha_m2_s: float | None = None,
) -> np.ndarray:
    """Return the exact excess-temperature solution in kelvin."""

    alpha = config.alpha_m2_s if alpha_m2_s is None else alpha_m2_s
    if alpha <= 0:
        raise ValueError("alpha_m2_s must be positive")
    x = np.asarray(x_m, dtype=float)
    t = np.asarray(time_s, dtype=float)
    if np.any(x < 0) or np.any(x > config.length_m):
        raise ValueError("x_m must lie within [0, length_m]")
    if np.any(t < 0):
        raise ValueError("time_s cannot be negative")
    decay = np.exp(-(np.pi**2) * alpha * t / config.length_m**2)
    shape = np.sin(np.pi * x / config.length_m)
    return config.initial_amplitude_K * decay * shape


def explicit_finite_difference(
    config: HeatEquationConfig = HeatEquationConfig(),
    nx: int = 51,
    dt_s: float = 0.10,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Solve the problem using a stable FTCS finite-difference method.

    Returns `(x_m, time_s, temperature_K)` with temperature shape `(nt, nx)`.
    The final step is shortened when needed to land exactly on `final_time_s`.
    """

    if nx < 3:
        raise ValueError("nx must be at least 3")
    if dt_s <= 0:
        raise ValueError("dt_s must be positive")

    x = np.linspace(0.0, config.length_m, nx)
    dx = x[1] - x[0]
    stability = config.alpha_m2_s * dt_s / dx**2
    if stability > 0.5:
        raise ValueError(
            f"Unstable explicit scheme: alpha*dt/dx^2 = {stability:.3f} > 0.5"
        )

    times = np.arange(0.0, config.final_time_s, dt_s)
    if times.size == 0 or not np.isclose(times[-1], config.final_time_s):
        times = np.append(times, config.final_time_s)

    temperature = np.zeros((times.size, nx), dtype=float)
    temperature[0] = analytical_temperature(x, 0.0, config)

    for n in range(times.size - 1):
        step = times[n + 1] - times[n]
        ratio = config.alpha_m2_s * step / dx**2
        temperature[n + 1, 1:-1] = temperature[n, 1:-1] + ratio * (
            temperature[n, 2:]
            - 2.0 * temperature[n, 1:-1]
            + temperature[n, :-2]
        )
        temperature[n + 1, (0, -1)] = 0.0

    return x, times, temperature


def relative_l2(prediction: np.ndarray, reference: np.ndarray) -> float:
    """Return ||prediction-reference||_2 / ||reference||_2."""

    prediction = np.asarray(prediction, dtype=float)
    reference = np.asarray(reference, dtype=float)
    if prediction.shape != reference.shape:
        raise ValueError("prediction and reference must have the same shape")
    denominator = np.linalg.norm(reference.ravel())
    if denominator == 0:
        raise ValueError("reference norm is zero")
    return float(np.linalg.norm((prediction - reference).ravel()) / denominator)
