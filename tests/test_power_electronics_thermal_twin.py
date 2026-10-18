"""Behavior checks for the simulated power-electronics thermal-twin baseline."""

from pathlib import Path
import sys
import unittest

import numpy as np


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
TUTORIAL_DIRECTORY = REPOSITORY_ROOT / "case_studies" / "power_electronics_thermal_digital_twin" / "tutorials"
sys.path.insert(0, str(TUTORIAL_DIRECTORY))

from thermal_twin_baseline import (  # noqa: E402
    fit_lumped_thermal_parameters,
    forecast_lumped_temperature,
)

THERMAL_TUTORIAL_DIRECTORY = REPOSITORY_ROOT / "course_content" / "vii_time_series_forecasting" / "tutorials"
sys.path.insert(0, str(THERMAL_TUTORIAL_DIRECTORY))
from thermal_rc_forecasting import ThermalRCConfig, make_power_profile, simulate_thermal_run  # noqa: E402


class ThermalTwinBaselineTests(unittest.TestCase):
    def test_identification_recovers_simulated_lumped_parameters(self):
        config = ThermalRCConfig(thermal_resistance_K_per_W=0.6, thermal_capacitance_J_per_K=18.0)
        run = simulate_thermal_run(config, make_power_profile(config, phase_rad=0.4), run_id="calibration")

        parameters = fit_lumped_thermal_parameters(run)

        self.assertAlmostEqual(parameters.thermal_resistance_K_per_W, config.thermal_resistance_K_per_W, places=8)
        self.assertAlmostEqual(parameters.thermal_capacitance_J_per_K, config.thermal_capacitance_J_per_K, places=8)

    def test_forecast_respects_zero_power_cooling_limit(self):
        config = ThermalRCConfig(duration_s=10.0, thermal_resistance_K_per_W=0.5, thermal_capacitance_J_per_K=20.0)
        run = simulate_thermal_run(config, np.full(config.sample_count, 30.0), run_id="calibration")
        parameters = fit_lumped_thermal_parameters(run)
        start_temperature_C = 70.0

        predicted = forecast_lumped_temperature(
            initial_temperature_C=start_temperature_C,
            future_power_W=np.zeros(20),
            ambient_temperature_C=25.0,
            dt_s=config.dt_s,
            parameters=parameters,
        )

        self.assertLess(predicted[-1], start_temperature_C)
        self.assertGreater(predicted[-1], 25.0)

    def test_forecast_rejects_a_time_step_that_creates_nonphysical_cooling_oscillation(self):
        from thermal_twin_baseline import LumpedThermalParameters

        with self.assertRaises(ValueError):
            forecast_lumped_temperature(
                initial_temperature_C=70.0,
                future_power_W=np.zeros(2),
                ambient_temperature_C=25.0,
                dt_s=10.0,
                parameters=LumpedThermalParameters(thermal_resistance_K_per_W=0.5, thermal_capacitance_J_per_K=20.0),
            )


if __name__ == "__main__":
    unittest.main()
