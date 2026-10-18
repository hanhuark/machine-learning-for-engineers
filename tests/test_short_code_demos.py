"""Smoke and invariant tests for the short, student-facing code demonstrations."""

import sys
import unittest
from pathlib import Path

import numpy as np


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY_ROOT))


class ShortCodeDemoTests(unittest.TestCase):
    def test_advanced_modules_have_linked_foundations_with_equations_and_failure_checks(self):
        modules = (
            "iv_segmentation_and_object_detection",
            "v_reinforcement_learning",
            "vi_generative_models",
            "vii_time_series_forecasting",
            "viii_physics_informed_neural_networks",
            "ix_ai_agent_harnesses",
        )
        for module in modules:
            module_root = REPOSITORY_ROOT / "course_content" / module
            readme = (module_root / "README.md").read_text(encoding="utf-8")
            foundations = module_root / "FOUNDATIONS.md"
            self.assertTrue(foundations.is_file(), f"{module} needs a foundations guide")
            self.assertIn("FOUNDATIONS.md", readme, f"{module} README must link its foundations guide")
            content = foundations.read_text(encoding="utf-8")
            self.assertIn("$$", content, f"{module} needs editable display mathematics")
            self.assertIn("## Failure checks", content, f"{module} needs explicit failure checks")

    def test_regression_demo_recovers_a_linear_relation_and_reports_held_out_error(self):
        from course_content.short_code_demos.regression import fit_line, mean_absolute_error

        slope, intercept = fit_line(np.array([0.0, 1.0, 2.0]), np.array([1.0, 3.0, 5.0]))
        prediction = slope * np.array([3.0, 4.0]) + intercept

        self.assertAlmostEqual(slope, 2.0)
        self.assertAlmostEqual(intercept, 1.0)
        self.assertAlmostEqual(mean_absolute_error(np.array([7.0, 9.0]), prediction), 0.0)

    def test_classification_demo_counts_false_negatives_separately_from_accuracy(self):
        from course_content.short_code_demos.classification import binary_metrics

        metrics = binary_metrics(np.array([1, 1, 0, 0]), np.array([0.2, 0.9, 0.8, 0.1]), 0.5)

        self.assertEqual(metrics["true_positive"], 1)
        self.assertEqual(metrics["false_negative"], 1)
        self.assertAlmostEqual(metrics["accuracy"], 0.5)

    def test_pca_demo_returns_orthonormal_components_and_a_reconstruction(self):
        from course_content.short_code_demos.pca import fit_pca

        data = np.array([[0.0, 0.0], [1.0, 1.0], [2.0, 2.0], [3.0, 3.0]])
        result = fit_pca(data, n_components=1)

        self.assertEqual(result["scores"].shape, (4, 1))
        self.assertAlmostEqual(float((result["components"] @ result["components"].T).item()), 1.0)
        self.assertGreater(result["explained_variance_ratio"][0], 0.99)

    def test_segmentation_demo_uses_overlap_metrics(self):
        from course_content.short_code_demos.segmentation import overlap_metrics

        metrics = overlap_metrics(np.array([[1, 1], [0, 0]]), np.array([[1, 0], [0, 0]]))

        self.assertAlmostEqual(metrics["iou"], 0.5)
        self.assertAlmostEqual(metrics["dice"], 2.0 / 3.0)

    def test_q_learning_update_uses_discounted_next_state_value(self):
        from course_content.short_code_demos.reinforcement_learning import q_learning_update

        updated = q_learning_update(old_value=1.0, reward=2.0, next_best_value=4.0, learning_rate=0.5, discount=0.9)

        self.assertAlmostEqual(updated, 3.3)

    def test_time_series_demo_preserves_chronological_holdout(self):
        from course_content.short_code_demos.time_series import chronological_split, persistence_forecast

        series = np.arange(10.0)
        train, test = chronological_split(series, test_count=3)

        self.assertTrue(np.array_equal(train, np.arange(7.0)))
        self.assertTrue(np.array_equal(test, np.arange(7.0, 10.0)))
        self.assertTrue(np.array_equal(persistence_forecast(train[-1], len(test)), np.array([6.0, 6.0, 6.0])))

    def test_heat_equation_demo_satisfies_initial_and_boundary_conditions(self):
        from course_content.short_code_demos.heat_equation import fourier_number, temperature_excess

        self.assertAlmostEqual(temperature_excess(0.05, 0.0, 0.10, 50.0, 1.0e-5), 50.0)
        self.assertAlmostEqual(temperature_excess(0.0, 20.0, 0.10, 50.0, 1.0e-5), 0.0)
        self.assertAlmostEqual(fourier_number(1.0e-5, 200.0, 0.10), 0.2)

    def test_conduction_demo_passes_units_and_limiting_case_checks(self):
        from course_content.short_code_demos.engineering_agent import conduction_acceptance_checks, conduction_heat_rate

        checks = conduction_acceptance_checks(length_m=0.01, conductivity_W_mK=200.0, area_m2=0.02)

        self.assertTrue(all(checks.values()))
        self.assertAlmostEqual(
            conduction_heat_rate(0.01, 200.0, 0.02, 310.0, 300.0),
            4000.0,
        )

    def test_design_screen_rejects_candidates_that_violate_explicit_constraints(self):
        from course_content.short_code_demos.generative_design_screen import feasible_candidates

        candidates = [
            {"name": "A", "mass_kg": 0.8, "peak_temperature_K": 340.0},
            {"name": "B", "mass_kg": 1.2, "peak_temperature_K": 330.0},
        ]

        self.assertEqual(
            feasible_candidates(candidates, maximum_mass_kg=1.0, maximum_temperature_K=350.0),
            [candidates[0]],
        )


if __name__ == "__main__":
    unittest.main()
