"""Leakage-aware forecasting tutorial using a simulated lumped thermal system.

Run from this directory:
    python thermal_rc_forecasting.py

The fixture is simulated teaching data, not a digital twin or experimental
validation result. Temperatures are in degC, power is in W, thermal resistance
is in K/W, thermal capacitance is in J/K, and time is in s.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path

import numpy as np
import pandas as pd


@dataclass(frozen=True)
class ThermalRCConfig:
    """Parameters for C dT/dt = P - (T - T_ambient) / R."""

    dt_s: float = 0.1
    duration_s: float = 60.0
    thermal_resistance_K_per_W: float = 0.50
    thermal_capacitance_J_per_K: float = 20.0
    ambient_temperature_C: float = 25.0

    @property
    def sample_count(self) -> int:
        return int(round(self.duration_s / self.dt_s)) + 1


def simulate_thermal_run(config: ThermalRCConfig, power_W: np.ndarray, run_id: str) -> pd.DataFrame:
    """Integrate the lumped thermal balance with a forward-Euler update."""
    power_W = np.asarray(power_W, dtype=float)
    if power_W.shape != (config.sample_count,):
        raise ValueError("power_W length must equal the configured sample count")
    if config.dt_s <= 0 or config.thermal_resistance_K_per_W <= 0 or config.thermal_capacitance_J_per_K <= 0:
        raise ValueError("time step, thermal resistance, and thermal capacitance must be positive")

    time_s = np.arange(config.sample_count, dtype=float) * config.dt_s
    temperature_C = np.full(config.sample_count, config.ambient_temperature_C, dtype=float)
    for index in range(config.sample_count - 1):
        cooling_W = (temperature_C[index] - config.ambient_temperature_C) / config.thermal_resistance_K_per_W
        temperature_C[index + 1] = temperature_C[index] + config.dt_s / config.thermal_capacitance_J_per_K * (
            power_W[index] - cooling_W
        )

    return pd.DataFrame(
        {
            "run_id": run_id,
            "time_s": time_s,
            "power_W": power_W,
            "temperature_C": temperature_C,
            "ambient_temperature_C": config.ambient_temperature_C,
            "thermal_resistance_K_per_W": config.thermal_resistance_K_per_W,
            "thermal_capacitance_J_per_K": config.thermal_capacitance_J_per_K,
        }
    )


def make_power_profile(config: ThermalRCConfig, phase_rad: float) -> np.ndarray:
    """Create a known, bounded heat-load command for a teaching fixture."""
    time_s = np.arange(config.sample_count, dtype=float) * config.dt_s
    steps = np.where((time_s % 20.0) < 10.0, 18.0, 42.0)
    modulation = 5.0 * np.sin(2.0 * np.pi * time_s / 15.0 + phase_rad)
    return steps + modulation


def chronological_run_split(runs: list[pd.DataFrame]) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Assign whole runs to train, validation, and condition-held-out test sets."""
    if len(runs) != 3:
        raise ValueError("provide exactly three time-ordered runs: train, validation, test")
    return tuple(frame.copy() for frame in runs)  # type: ignore[return-value]


def make_supervised_windows(
    runs: list[pd.DataFrame], history_steps: int, horizon_steps: int
) -> pd.DataFrame:
    """Make within-run windows only; no window can span an independent run boundary."""
    if history_steps < 1 or horizon_steps < 1:
        raise ValueError("history_steps and horizon_steps must be positive")
    records: list[dict[str, object]] = []
    for run in runs:
        run_id = str(run["run_id"].iloc[0])
        for end_index in range(history_steps - 1, len(run) - horizon_steps):
            history = run.iloc[end_index - history_steps + 1 : end_index + 1]
            target = run.iloc[end_index + 1 : end_index + horizon_steps + 1]
            records.append(
                {
                    "run_id": run_id,
                    "last_time_s": float(history["time_s"].iloc[-1]),
                    "last_temperature_C": float(history["temperature_C"].iloc[-1]),
                    "last_power_W": float(history["power_W"].iloc[-1]),
                    "target_temperature_C": float(target["temperature_C"].iloc[-1]),
                }
            )
    return pd.DataFrame.from_records(records)


def fit_one_step_linear_model(training_run: pd.DataFrame) -> np.ndarray:
    """Fit T[k+1] = beta_0 + beta_T T[k] + beta_P P[k] using training evidence only."""
    inputs = np.column_stack(
        [
            np.ones(len(training_run) - 1),
            training_run["temperature_C"].to_numpy()[:-1],
            training_run["power_W"].to_numpy()[:-1],
        ]
    )
    targets = training_run["temperature_C"].to_numpy()[1:]
    return np.linalg.lstsq(inputs, targets, rcond=None)[0]


def recursive_linear_forecast(initial_temperature_C: float, future_power_W: np.ndarray, coefficients: np.ndarray) -> np.ndarray:
    """Forecast recursively when future heat-load commands are known inputs."""
    future_power_W = np.asarray(future_power_W, dtype=float)
    if coefficients.shape != (3,):
        raise ValueError("coefficients must contain intercept, temperature, and power terms")
    predicted = np.empty(future_power_W.size, dtype=float)
    temperature_C = float(initial_temperature_C)
    for index, power_W in enumerate(future_power_W):
        temperature_C = coefficients[0] + coefficients[1] * temperature_C + coefficients[2] * power_W
        predicted[index] = temperature_C
    return predicted


def mean_absolute_error(truth: np.ndarray, prediction: np.ndarray) -> float:
    """Return MAE in the same unit as the temperature target: degC."""
    return float(np.mean(np.abs(np.asarray(truth) - np.asarray(prediction))))


def evaluate_forecast_run(run: pd.DataFrame, coefficients: np.ndarray, horizon_steps: int) -> tuple[float, float]:
    """Return persistence and recursive ARX MAE for one independent run."""
    if horizon_steps >= len(run):
        raise ValueError("forecast horizon must be shorter than the available run")
    truth = run["temperature_C"].to_numpy()[1 : horizon_steps + 1]
    persistence = np.full(horizon_steps, run["temperature_C"].iloc[0], dtype=float)
    linear = recursive_linear_forecast(
        run["temperature_C"].iloc[0], run["power_W"].to_numpy()[:horizon_steps], coefficients
    )
    return mean_absolute_error(truth, persistence), mean_absolute_error(truth, linear)


def main() -> None:
    base = ThermalRCConfig()
    train_config = base
    validation_config = replace(base, thermal_resistance_K_per_W=0.55)
    test_config = replace(base, thermal_resistance_K_per_W=0.65, ambient_temperature_C=30.0)
    train, validation, test = chronological_run_split(
        [
            simulate_thermal_run(train_config, make_power_profile(train_config, 0.0), "train_nominal"),
            simulate_thermal_run(validation_config, make_power_profile(validation_config, 0.8), "validation_shifted_R"),
            simulate_thermal_run(test_config, make_power_profile(test_config, 1.6), "test_shifted_R_and_ambient"),
        ]
    )
    coefficients = fit_one_step_linear_model(train)
    horizon_steps = 100
    validation_persistence_mae, validation_arx_mae = evaluate_forecast_run(validation, coefficients, horizon_steps)
    test_persistence_mae, test_arx_mae = evaluate_forecast_run(test, coefficients, horizon_steps)
    print("Evidence class: simulated teaching fixture")
    print("Independent split: full validation run with shifted R_th; full test run with shifted R_th and ambient temperature")
    print(f"Forecast horizon: {horizon_steps} samples = {horizon_steps * base.dt_s:.1f} s")
    print(f"Validation persistence MAE: {validation_persistence_mae:.3f} degC")
    print(f"Validation training-only linear ARX MAE: {validation_arx_mae:.3f} degC")
    print(f"Test persistence MAE: {test_persistence_mae:.3f} degC")
    print(f"Test training-only linear ARX MAE: {test_arx_mae:.3f} degC")
    print("Do not interpret the linear model as validated for an unmodeled physical system.")

    output_directory = Path(__file__).resolve().parent / "generated"
    output_directory.mkdir(exist_ok=True)
    pd.concat([train, validation, test], ignore_index=True).to_csv(output_directory / "thermal_rc_runs.csv", index=False)


if __name__ == "__main__":
    main()
