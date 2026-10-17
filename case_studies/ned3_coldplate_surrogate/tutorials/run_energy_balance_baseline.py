"""Fit and assess a lumped energy-balance baseline for the CFD outlet scalar.

The model is deliberately constrained to
``T_out = T_in,mix + Q_total / (m_dot_total * c_eff)``.  ``c_eff`` is fitted
from the training CFD cases, so it is an effective parameter for this released
simulation configuration rather than an independently measured property.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from coldplate_baseline import (
    CHIP_AREA_M2,
    build_design_matrix,
    build_energy_balance_inputs,
    evaluate_regression,
    fit_effective_heat_capacity,
    predict_outlet_energy_balance,
)
from download_subset import DEFAULT_TEST_IDS, DEFAULT_TRAIN_IDS
from run_linear_baseline import load_scalar_target


DEFAULT_TARGET = "outlet_tavg|temperature"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument("--target", default=DEFAULT_TARGET)
    parser.add_argument("--chip-area-m2", type=float, default=CHIP_AREA_M2)
    parser.add_argument("--output", type=Path, default=Path("coldplate_energy_balance_metrics.json"))
    arguments = parser.parse_args()
    if arguments.target != DEFAULT_TARGET:
        parser.error(
            "this constrained baseline only supports outlet_tavg|temperature; "
            "chip temperatures require a separately stated thermal-resistance model"
        )

    model_setup = json.loads((arguments.data_root / "1_Dataset" / "model_setup.json").read_text(encoding="utf-8"))
    feature_names, train_x = build_design_matrix(model_setup, DEFAULT_TRAIN_IDS)
    _, test_x = build_design_matrix(model_setup, DEFAULT_TEST_IDS)
    train_y = load_scalar_target(arguments.data_root, DEFAULT_TRAIN_IDS, arguments.target)
    test_y = load_scalar_target(arguments.data_root, DEFAULT_TEST_IDS, arguments.target)
    train_state = build_energy_balance_inputs(feature_names, train_x, chip_area_m2=arguments.chip_area_m2)
    test_state = build_energy_balance_inputs(feature_names, test_x, chip_area_m2=arguments.chip_area_m2)
    heat_capacity = fit_effective_heat_capacity(*train_state, train_y)
    predicted = predict_outlet_energy_balance(*test_state, heat_capacity)
    _, metrics = evaluate_regression(
        coefficients=[0.0, 1.0], features=predicted.reshape(-1, 1), target=test_y
    )
    output = {
        "evidence_class": "simulated CFD teaching subset",
        "target": arguments.target,
        "equation": "T_out = T_in,mix + Q_total / (m_dot_total * c_eff)",
        "chip_area_m2": arguments.chip_area_m2,
        "fitted_effective_heat_capacity_j_kg_k": heat_capacity,
        "metrics": metrics,
        "interpretation": (
            "c_eff is fitted from the training CFD cases. It is an effective parameter "
            "for this one released configuration, not a measured fluid property."
        ),
        "warning": (
            "This is a held-out instructional comparison on simulated steady CFD data, "
            "not CFD validation, hardware validation, or an extrapolation claim."
        ),
    }
    arguments.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
