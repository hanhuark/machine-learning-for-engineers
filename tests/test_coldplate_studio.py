"""Tests for the cold-plate teaching subset and transparent baseline helpers."""

from pathlib import Path
import sys
import tempfile
import unittest

import numpy as np


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
TUTORIAL_DIRECTORY = REPOSITORY_ROOT / "case_studies" / "ned3_coldplate_surrogate" / "tutorials"
sys.path.insert(0, str(TUTORIAL_DIRECTORY))

from coldplate_baseline import (  # noqa: E402
    build_design_matrix,
    build_energy_balance_inputs,
    evaluate_regression,
    fit_effective_heat_capacity,
    fit_linear_baseline,
    predict_outlet_energy_balance,
)
from download_subset import DEFAULT_TEST_IDS, DEFAULT_TRAIN_IDS, DEFAULT_VALIDATION_IDS, subset_plan  # noqa: E402


class ColdPlateBaselineTests(unittest.TestCase):
    def test_subset_plan_preserves_a_pinned_revision_and_disjoint_splits(self):
        plan = subset_plan("0123456789abcdef")

        self.assertEqual(plan["source_revision"], "0123456789abcdef")
        splits = plan["splits"]
        all_ids = splits["train"] + splits["validation"] + splits["test"]
        self.assertEqual(len(all_ids), len(set(all_ids)))
        self.assertEqual(splits["train"], list(DEFAULT_TRAIN_IDS))
        self.assertEqual(splits["validation"], list(DEFAULT_VALIDATION_IDS))
        self.assertEqual(splits["test"], list(DEFAULT_TEST_IDS))

    def test_subset_plan_rejects_a_model_path_that_leaves_the_source_tree(self):
        with self.assertRaises(ValueError):
            subset_plan("0123456789abcdef", "../outside.json")

    def test_design_matrix_preserves_requested_simulation_order(self):
        setup = {
            "doe_configuration": {
                "inlet": {"mass_flow_rate": [1.0, 2.0, 3.0]},
                "chip": {"heat_flux": [10.0, 20.0, 30.0]},
            }
        }

        names, matrix = build_design_matrix(setup, [3, 1])

        self.assertEqual(names, ["chip.heat_flux", "inlet.mass_flow_rate"])
        np.testing.assert_allclose(matrix, [[30.0, 3.0], [10.0, 1.0]])

    def test_linear_baseline_recovers_a_linear_scalar_target(self):
        train_x = np.array([[0.0], [1.0], [2.0], [3.0]])
        train_y = 2.0 + 3.0 * train_x[:, 0]
        test_x = np.array([[4.0], [5.0]])
        test_y = 2.0 + 3.0 * test_x[:, 0]

        coefficients = fit_linear_baseline(train_x, train_y)
        predicted, metrics = evaluate_regression(coefficients, test_x, test_y)

        np.testing.assert_allclose(predicted, test_y)
        self.assertAlmostEqual(metrics["rmse"], 0.0)
        self.assertAlmostEqual(metrics["mae"], 0.0)

    def test_energy_balance_recovers_a_constant_effective_heat_capacity(self):
        names = [
            "chip1.thermal.heat_flux",
            "chip2.thermal.heat_flux",
            "inlet1.momentum.mass_flow_rate",
            "inlet1.thermal.total_temperature",
            "inlet2.momentum.mass_flow_rate",
            "inlet2.thermal.total_temperature",
        ]
        features = np.array(
            [
                [100.0, 200.0, 2.0, 300.0, 3.0, 320.0],
                [200.0, 100.0, 4.0, 310.0, 1.0, 300.0],
                [150.0, 150.0, 1.0, 290.0, 4.0, 330.0],
            ]
        )
        power, mass_flow, mixed_inlet = build_energy_balance_inputs(
            names, features, chip_area_m2=2.0
        )
        expected_outlet = mixed_inlet + power / (mass_flow * 10.0)

        heat_capacity = fit_effective_heat_capacity(
            power, mass_flow, mixed_inlet, expected_outlet
        )
        predicted = predict_outlet_energy_balance(
            power, mass_flow, mixed_inlet, heat_capacity
        )

        self.assertAlmostEqual(heat_capacity, 10.0)
        np.testing.assert_allclose(predicted, expected_outlet)


if __name__ == "__main__":
    unittest.main()
