"""Run a transparent scalar-temperature baseline on a downloaded teaching subset."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np

from coldplate_baseline import build_design_matrix, evaluate_regression, fit_linear_baseline
from download_subset import DEFAULT_TEST_IDS, DEFAULT_TRAIN_IDS


DEFAULT_TARGET = "chip1_tmax|temperature"


def load_scalar_target(data_root: Path, simulation_ids: tuple[int, ...], key: str) -> np.ndarray:
    """Load one scalar target per CFD simulation and reject non-scalar fields."""
    values: list[float] = []
    for identifier in simulation_ids:
        source = data_root / "1_Dataset" / f"sim_{identifier:04d}.npz"
        with np.load(source) as archive:
            if key not in archive:
                raise KeyError(f"{key!r} is not present in {source.name}")
            value = np.asarray(archive[key], dtype=float).reshape(-1)
        if value.size != 1:
            raise ValueError(f"{key!r} in {source.name} is not scalar; choose a scalar target")
        values.append(float(value[0]))
    return np.asarray(values)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument("--target", default=DEFAULT_TARGET)
    parser.add_argument("--output", type=Path, default=Path("coldplate_linear_baseline_metrics.json"))
    arguments = parser.parse_args()

    model_setup = json.loads((arguments.data_root / "1_Dataset" / "model_setup.json").read_text(encoding="utf-8"))
    feature_names, train_x = build_design_matrix(model_setup, DEFAULT_TRAIN_IDS)
    _, test_x = build_design_matrix(model_setup, DEFAULT_TEST_IDS)
    train_y = load_scalar_target(arguments.data_root, DEFAULT_TRAIN_IDS, arguments.target)
    test_y = load_scalar_target(arguments.data_root, DEFAULT_TEST_IDS, arguments.target)

    coefficients = fit_linear_baseline(train_x, train_y)
    _, metrics = evaluate_regression(coefficients, test_x, test_y)
    output = {
        "evidence_class": "simulated CFD teaching subset",
        "target": arguments.target,
        "feature_names": feature_names,
        "metrics": metrics,
        "warning": (
            "This linear baseline is an instructional comparison, not a CFD "
            "validation result or an extrapolation claim."
        ),
    }
    arguments.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
