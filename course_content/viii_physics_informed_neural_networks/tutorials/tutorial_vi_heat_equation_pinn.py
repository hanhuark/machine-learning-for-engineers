"""Executable tutorial: forward and inverse PINNs for transient heat conduction.

Run from the module root:
    python tutorials/tutorial_vi_heat_equation_pinn.py --mode quick
    python tutorials/tutorial_vi_heat_equation_pinn.py --mode full
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

MODULE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_ROOT))

from src.heat_equation import (  # noqa: E402
    HeatEquationConfig,
    analytical_temperature,
    explicit_finite_difference,
    relative_l2,
)
from src.pinn import predict, train_forward, train_inverse  # noqa: E402


def plot_profiles(config: HeatEquationConfig, output_dir: Path) -> None:
    x = np.linspace(0.0, config.length_m, 201)
    fig, ax = plt.subplots(figsize=(7, 4.5))
    for time_s in (0.0, 25.0, 50.0, 100.0, 200.0):
        ax.plot(x, analytical_temperature(x, time_s, config), label=f"t = {time_s:g} s")
    ax.set(xlabel="Position, x (m)", ylabel="Excess temperature, T (K)")
    ax.legend()
    ax.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(output_dir / "analytical_profiles.png", dpi=180)
    plt.close(fig)


def evaluate_reference(model, reference: pd.DataFrame) -> tuple[np.ndarray, dict[str, float]]:
    predicted = predict(model, reference["x_m"].to_numpy(), reference["t_s"].to_numpy())
    truth = reference["T_excess_K"].to_numpy()
    metrics = {
        "relative_l2": relative_l2(predicted, truth),
        "mae_K": float(np.mean(np.abs(predicted - truth))),
        "max_abs_error_K": float(np.max(np.abs(predicted - truth))),
    }
    return predicted, metrics


def plot_forward_results(reference: pd.DataFrame, predicted: np.ndarray, output_dir: Path) -> None:
    frame = reference.assign(T_PINN_K=predicted, abs_error_K=np.abs(predicted - reference["T_excess_K"]))
    x_values = np.sort(frame["x_m"].unique())
    t_values = np.sort(frame["t_s"].unique())
    shape = (t_values.size, x_values.size)
    fields = [
        (frame["T_excess_K"].to_numpy().reshape(shape), "Analytical temperature", "T (K)"),
        (frame["T_PINN_K"].to_numpy().reshape(shape), "PINN temperature", "T (K)"),
        (frame["abs_error_K"].to_numpy().reshape(shape), "Absolute error", "|error| (K)"),
    ]
    fig, axes = plt.subplots(1, 3, figsize=(13, 3.8), constrained_layout=True)
    for ax, (field, title, label) in zip(axes, fields):
        image = ax.pcolormesh(x_values, t_values, field, shading="auto")
        ax.set(title=title, xlabel="x (m)", ylabel="t (s)")
        fig.colorbar(image, ax=ax, label=label)
    fig.savefig(output_dir / "forward_field_and_error.png", dpi=180)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("quick", "full"), default="quick")
    args = parser.parse_args()

    config = HeatEquationConfig()
    data_dir = MODULE_ROOT / "data"
    output_dir = MODULE_ROOT / "results"
    output_dir.mkdir(exist_ok=True)
    if not (data_dir / "reference_temperature_field.csv").exists():
        raise FileNotFoundError("Run scripts/generate_heat_equation_datasets.py first")

    # Section 1: analytical and finite-difference baselines.
    plot_profiles(config, output_dir)
    x_fd, t_fd, temperature_fd = explicit_finite_difference(config, nx=51, dt_s=0.10)
    fd_reference = analytical_temperature(x_fd, t_fd[-1], config)
    fd_error = relative_l2(temperature_fd[-1], fd_reference)
    print(f"Final Fourier number: {config.fourier_number(config.final_time_s):.4f}")
    print(f"Finite-difference final-time relative L2 error: {fd_error:.4e}")

    # Sections 2-3: forward PINN and independent verification.
    settings = {
        "quick": {"iterations": 100, "n_domain": 128, "n_boundary": 32, "n_initial": 32, "report_every": 10},
        "full": {"iterations": 5000, "n_domain": 2000, "n_boundary": 100, "n_initial": 100, "report_every": 100},
    }[args.mode]
    forward = train_forward(config, **settings)
    forward.history.to_csv(output_dir / "forward_loss_history.csv", index=False)
    reference = pd.read_csv(data_dir / "reference_temperature_field.csv")
    predicted, forward_metrics = evaluate_reference(forward.model, reference)
    forward_metrics["training_time_s"] = forward.elapsed_s
    plot_forward_results(reference, predicted, output_dir)
    print("Forward PINN metrics:", forward_metrics)

    # Section 4: inverse diffusivity from sparse noisy observations.
    inverse = train_inverse(
        data_dir / "inverse_temperature_noise_0p50K.csv",
        config,
        initial_alpha_m2_s=5.0e-6,
        **settings,
    )
    inverse.history.to_csv(output_dir / "inverse_loss_history.csv", index=False)
    inverse_metrics = {
        "alpha_estimate_m2_s": inverse.alpha_estimate_m2_s,
        "alpha_reference_m2_s": config.alpha_m2_s,
        "alpha_relative_error": abs(inverse.alpha_estimate_m2_s - config.alpha_m2_s) / config.alpha_m2_s,
        "training_time_s": inverse.elapsed_s,
        "mode": args.mode,
        "note": (
            "Quick mode is a software smoke test and is not expected to converge."
            if args.mode == "quick"
            else "Full mode is an instructional baseline; repeat across seeds before interpreting variability."
        ),
    }
    print("Inverse PINN metrics:", inverse_metrics)

    metrics = {
        "evidence_class": "simulated tutorial output",
        "finite_difference_final_relative_l2": fd_error,
        "forward_pinn": forward_metrics,
        "inverse_pinn": inverse_metrics,
    }
    (output_dir / "metrics.json").write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
