"""Fit and test an inspectable thermal-state baseline for the studio.

The script uses only the simulated thermal-RC fixture from Module VII.  The
fitted parameters are effective values for this numerical exercise, not
measured device properties and not evidence of a calibrated digital twin.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import sys

import numpy as np
import pandas as pd


REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
THERMAL_TUTORIAL_DIRECTORY = REPOSITORY_ROOT / "course_content" / "vii_time_series_forecasting" / "tutorials"
sys.path.insert(0, str(THERMAL_TUTORIAL_DIRECTORY))

from thermal_rc_forecasting import (  # noqa: E402
    ThermalRCConfig,
    make_power_profile,
    mean_absolute_error,
    simulate_thermal_run,
)


@dataclass(frozen=True)
class LumpedThermalParameters:
    """Effective parameters for C dT/dt = P - (T - T_a) / R."""

    thermal_resistance_K_per_W: float
    thermal_capacitance_J_per_K: float


def fit_lumped_thermal_parameters(calibration_run: pd.DataFrame) -> LumpedThermalParameters:
    """Identify effective R and C from a single simulated calibration trajectory.

    Forward Euler gives (T[k+1]-T[k])/dt = a P[k] - b(T[k]-T_a), where
    a=1/C and b=1/(R C).  Both fitted coefficients must be positive for this
    passive first-order thermal model.
    """
    required_columns = {"time_s", "power_W", "temperature_C", "ambient_temperature_C"}
    missing_columns = required_columns.difference(calibration_run.columns)
    if missing_columns:
        raise ValueError(f"calibration run is missing columns: {sorted(missing_columns)}")
    if len(calibration_run) < 3:
        raise ValueError("calibration run needs at least three samples")

    time_s = calibration_run["time_s"].to_numpy(dtype=float)
    time_steps_s = np.diff(time_s)
    if np.any(time_steps_s <= 0) or not np.allclose(time_steps_s, time_steps_s[0]):
        raise ValueError("calibration run requires a strictly increasing, uniform time base")
    temperature_C = calibration_run["temperature_C"].to_numpy(dtype=float)
    power_W = calibration_run["power_W"].to_numpy(dtype=float)
    ambient_temperature_C = calibration_run["ambient_temperature_C"].to_numpy(dtype=float)
    derivative_K_per_s = np.diff(temperature_C) / time_steps_s[0]
    regressors = np.column_stack((power_W[:-1], -(temperature_C[:-1] - ambient_temperature_C[:-1])))
    inverse_capacitance, inverse_resistance_capacitance = np.linalg.lstsq(
        regressors, derivative_K_per_s, rcond=None
    )[0]
    if inverse_capacitance <= 0 or inverse_resistance_capacitance <= 0:
        raise ValueError("calibration did not identify a passive positive-R, positive-C thermal model")
    thermal_capacitance_J_per_K = 1.0 / inverse_capacitance
    thermal_resistance_K_per_W = inverse_capacitance / inverse_resistance_capacitance
    return LumpedThermalParameters(thermal_resistance_K_per_W, thermal_capacitance_J_per_K)


def forecast_lumped_temperature(
    initial_temperature_C: float,
    future_power_W: np.ndarray,
    ambient_temperature_C: float,
    dt_s: float,
    parameters: LumpedThermalParameters,
) -> np.ndarray:
    """Forecast a known-power trajectory using the identified Euler model."""
    if dt_s <= 0:
        raise ValueError("dt_s must be positive")
    if parameters.thermal_resistance_K_per_W <= 0 or parameters.thermal_capacitance_J_per_K <= 0:
        raise ValueError("thermal resistance and capacitance must be positive")
    thermal_time_constant_s = (
        parameters.thermal_resistance_K_per_W * parameters.thermal_capacitance_J_per_K
    )
    if dt_s >= thermal_time_constant_s:
        raise ValueError(
            "dt_s must be shorter than the thermal time constant for a non-oscillatory Euler cooling update"
        )
    future_power_W = np.asarray(future_power_W, dtype=float)
    predicted_temperature_C = np.empty(future_power_W.size, dtype=float)
    temperature_C = float(initial_temperature_C)
    for index, power_W in enumerate(future_power_W):
        cooling_W = (temperature_C - ambient_temperature_C) / parameters.thermal_resistance_K_per_W
        temperature_C += dt_s / parameters.thermal_capacitance_J_per_K * (power_W - cooling_W)
        predicted_temperature_C[index] = temperature_C
    return predicted_temperature_C


def main() -> None:
    calibration_config = ThermalRCConfig(thermal_resistance_K_per_W=0.50, thermal_capacitance_J_per_K=20.0)
    test_config = ThermalRCConfig(
        thermal_resistance_K_per_W=0.65,
        thermal_capacitance_J_per_K=20.0,
        ambient_temperature_C=30.0,
    )
    calibration = simulate_thermal_run(
        calibration_config, make_power_profile(calibration_config, phase_rad=0.0), "calibration_nominal"
    )
    test = simulate_thermal_run(test_config, make_power_profile(test_config, phase_rad=1.6), "test_shifted_condition")
    fitted = fit_lumped_thermal_parameters(calibration)
    horizon_steps = 100
    prediction = forecast_lumped_temperature(
        initial_temperature_C=float(test["temperature_C"].iloc[0]),
        future_power_W=test["power_W"].to_numpy()[:horizon_steps],
        ambient_temperature_C=float(test["ambient_temperature_C"].iloc[0]),
        dt_s=test_config.dt_s,
        parameters=fitted,
    )
    truth = test["temperature_C"].to_numpy()[1 : horizon_steps + 1]
    print("Evidence class: simulated teaching fixture")
    print("Model: identified first-order thermal balance; no device calibration claim")
    print(f"Fitted effective R: {fitted.thermal_resistance_K_per_W:.3f} K/W")
    print(f"Fitted effective C: {fitted.thermal_capacitance_J_per_K:.3f} J/K")
    print(f"Held-out shifted-condition MAE: {mean_absolute_error(truth, prediction):.3f} degC")
    print("The test changes R and ambient temperature; the error is a transfer diagnostic, not a reliability metric.")


if __name__ == "__main__":
    main()
