"""Behavior checks for the public thermal-RC time-series teaching fixture."""

from pathlib import Path
import sys
import unittest

import numpy as np


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
TUTORIAL_DIRECTORY = REPOSITORY_ROOT / "course_content" / "vii_time_series_forecasting" / "tutorials"
sys.path.insert(0, str(TUTORIAL_DIRECTORY))

from thermal_rc_forecasting import (  # noqa: E402
    ThermalRCConfig,
    chronological_run_split,
    evaluate_forecast_run,
    make_supervised_windows,
    simulate_thermal_run,
)


class ThermalRCFixtureTests(unittest.TestCase):
    def test_zero_heat_load_at_ambient_remains_at_ambient(self):
        config = ThermalRCConfig(dt_s=0.1, duration_s=5.0, ambient_temperature_C=25.0)
        power = np.zeros(config.sample_count)

        run = simulate_thermal_run(config, power, run_id="ambient")

        self.assertTrue(np.allclose(run["temperature_C"], config.ambient_temperature_C))

    def test_windows_do_not_cross_run_boundaries(self):
        config = ThermalRCConfig(duration_s=2.0)
        first = simulate_thermal_run(config, np.full(config.sample_count, 20.0), run_id="run_a")
        second = simulate_thermal_run(config, np.full(config.sample_count, 30.0), run_id="run_b")

        windows = make_supervised_windows([first, second], history_steps=3, horizon_steps=2)

        self.assertTrue((windows["run_id"] == "run_a").any())
        self.assertTrue((windows["run_id"] == "run_b").any())
        self.assertTrue((windows["last_time_s"] >= 0.0).all())
        self.assertEqual(set(windows["run_id"]), {"run_a", "run_b"})

    def test_run_split_holds_out_entire_condition(self):
        config = ThermalRCConfig(duration_s=2.0)
        runs = [
            simulate_thermal_run(config, np.full(config.sample_count, 20.0), run_id="train"),
            simulate_thermal_run(config, np.full(config.sample_count, 25.0), run_id="validation"),
            simulate_thermal_run(config, np.full(config.sample_count, 30.0), run_id="test"),
        ]

        train, validation, test = chronological_run_split(runs)

        self.assertEqual(set(train["run_id"]), {"train"})
        self.assertEqual(set(validation["run_id"]), {"validation"})
        self.assertEqual(set(test["run_id"]), {"test"})

    def test_forecast_evaluation_rejects_a_horizon_outside_the_run(self):
        config = ThermalRCConfig(duration_s=1.0)
        run = simulate_thermal_run(config, np.full(config.sample_count, 20.0), run_id="short")

        with self.assertRaises(ValueError):
            evaluate_forecast_run(run, np.array([0.0, 1.0, 0.0]), horizon_steps=len(run))


if __name__ == "__main__":
    unittest.main()
