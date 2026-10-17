"""Transparent data-contract and linear-baseline helpers for the cold-plate studio.

The public source release stores one CFD realization per simulation and a
separate JSON DOE record. These helpers intentionally use only NumPy so the
first student comparison is inspectable before introducing a neural surrogate.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

import numpy as np


def _numeric_sequence(value: Any) -> bool:
    """Return whether a value is a non-string sequence of finite numeric values."""
    if isinstance(value, (str, bytes)) or not isinstance(value, Sequence):
        return False
    try:
        array = np.asarray(value, dtype=float)
    except (TypeError, ValueError):
        return False
    return array.ndim == 1 and array.size > 0 and np.isfinite(array).all()


def _collect_doe_series(value: Any, prefix: tuple[str, ...] = ()) -> list[tuple[str, np.ndarray]]:
    """Flatten nested DOE fields into deterministically ordered numeric series."""
    if _numeric_sequence(value):
        return [(".".join(prefix), np.asarray(value, dtype=float))]
    if not isinstance(value, Mapping):
        return []

    series: list[tuple[str, np.ndarray]] = []
    for key in sorted(value):
        series.extend(_collect_doe_series(value[key], prefix + (str(key),)))
    return series


def build_design_matrix(model_setup: Mapping[str, Any], simulation_ids: Sequence[int]) -> tuple[list[str], np.ndarray]:
    """Return DOE inputs for one-based simulation IDs in the requested order.

    The source JSON is expected to contain ``doe_configuration``. All retained
    numeric leaf series must have the same length. This function does not infer
    units; callers must document them from the canonical source record.
    """
    configuration = model_setup.get("doe_configuration")
    if not isinstance(configuration, Mapping):
        raise ValueError("model_setup.json lacks a mapping named 'doe_configuration'")

    series = _collect_doe_series(configuration)
    if not series:
        raise ValueError("doe_configuration contains no numeric input series")

    lengths = {values.size for _, values in series}
    if len(lengths) != 1:
        raise ValueError("DOE input series do not share one simulation count")
    simulation_count = lengths.pop()
    indices = np.asarray(simulation_ids, dtype=int) - 1
    if indices.ndim != 1 or indices.size == 0:
        raise ValueError("simulation_ids must be a non-empty one-dimensional sequence")
    if indices.min() < 0 or indices.max() >= simulation_count:
        raise ValueError(f"simulation IDs must lie between 1 and {simulation_count}")

    names = [name for name, _ in series]
    matrix = np.column_stack([values[indices] for _, values in series])
    return names, matrix


def fit_linear_baseline(features: np.ndarray, target: np.ndarray) -> np.ndarray:
    """Fit an ordinary least-squares baseline with an intercept column."""
    x = np.asarray(features, dtype=float)
    y = np.asarray(target, dtype=float).reshape(-1)
    if x.ndim != 2 or x.shape[0] != y.size:
        raise ValueError("features must be two-dimensional with one target per row")
    if not np.isfinite(x).all() or not np.isfinite(y).all():
        raise ValueError("linear baseline inputs must be finite")
    augmented = np.column_stack([np.ones(x.shape[0]), x])
    return np.linalg.lstsq(augmented, y, rcond=None)[0]


def evaluate_regression(
    coefficients: np.ndarray, features: np.ndarray, target: np.ndarray
) -> tuple[np.ndarray, dict[str, float]]:
    """Predict and calculate transparent held-out scalar regression metrics."""
    x = np.asarray(features, dtype=float)
    y = np.asarray(target, dtype=float).reshape(-1)
    coefficients = np.asarray(coefficients, dtype=float).reshape(-1)
    if x.ndim != 2 or x.shape[1] + 1 != coefficients.size or x.shape[0] != y.size:
        raise ValueError("coefficient, feature, and target dimensions are inconsistent")
    predicted = np.column_stack([np.ones(x.shape[0]), x]) @ coefficients
    error = predicted - y
    return predicted, {
        "rmse": float(np.sqrt(np.mean(error**2))),
        "mae": float(np.mean(np.abs(error))),
        "max_abs_error": float(np.max(np.abs(error))),
    }
