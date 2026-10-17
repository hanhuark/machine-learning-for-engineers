"""Transparent data-contract and linear-baseline helpers for the cold-plate studio.

The public source release stores one CFD realization per simulation and a
separate JSON DOE record. These helpers intentionally use only NumPy so the
first student comparison is inspectable before introducing a neural surrogate.
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any

import numpy as np


CHIP_AREA_M2 = 0.0016
"""Chip area used by the source deposit's published analysis code, in m²."""

_ENERGY_BALANCE_FIELDS = (
    "chip1.thermal.heat_flux",
    "chip2.thermal.heat_flux",
    "inlet1.momentum.mass_flow_rate",
    "inlet1.thermal.total_temperature",
    "inlet2.momentum.mass_flow_rate",
    "inlet2.thermal.total_temperature",
)


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


def build_energy_balance_inputs(
    feature_names: Sequence[str], features: np.ndarray, *, chip_area_m2: float = CHIP_AREA_M2
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Convert the documented six DOE inputs into an energy-balance state.

    ``chip_area_m2`` converts the two heat-flux boundary conditions to total
    heat rate.  The source deposit uses 0.0016 m² in its released analysis
    code.  The calculation treats both circuits as one mixed outlet control
    volume, which is appropriate only for the release's single outlet scalar.
    """
    x = np.asarray(features, dtype=float)
    if x.ndim != 2 or x.shape[1] != len(feature_names):
        raise ValueError("features must be a two-dimensional matrix matching feature_names")
    if not np.isfinite(x).all() or not np.isfinite(chip_area_m2) or chip_area_m2 <= 0:
        raise ValueError("features and chip_area_m2 must be finite; chip_area_m2 must be positive")
    index = {name: position for position, name in enumerate(feature_names)}
    missing = [name for name in _ENERGY_BALANCE_FIELDS if name not in index]
    if missing:
        raise ValueError(f"required energy-balance input(s) missing: {', '.join(missing)}")

    q1 = x[:, index["chip1.thermal.heat_flux"]] * chip_area_m2
    q2 = x[:, index["chip2.thermal.heat_flux"]] * chip_area_m2
    m1 = x[:, index["inlet1.momentum.mass_flow_rate"]]
    m2 = x[:, index["inlet2.momentum.mass_flow_rate"]]
    t1 = x[:, index["inlet1.thermal.total_temperature"]]
    t2 = x[:, index["inlet2.thermal.total_temperature"]]
    mass_flow = m1 + m2
    if np.any(m1 <= 0) or np.any(m2 <= 0):
        raise ValueError("each inlet mass-flow rate must be positive")
    total_power = q1 + q2
    if np.any(total_power < 0):
        raise ValueError("total applied heat rate must be non-negative")
    mixed_inlet_temperature = (m1 * t1 + m2 * t2) / mass_flow
    return total_power, mass_flow, mixed_inlet_temperature


def fit_effective_heat_capacity(
    total_power_w: np.ndarray,
    mass_flow_kg_s: np.ndarray,
    mixed_inlet_temperature_k: np.ndarray,
    outlet_temperature_k: np.ndarray,
) -> float:
    """Fit one effective constant heat capacity from training CFD data.

    The fitted relationship is ``T_out = T_in,mix + Q/(m_dot * c_eff)``.
    It is an interpretable lumped-energy baseline, not a measured fluid
    property or a replacement for the CFD model.
    """
    power = np.asarray(total_power_w, dtype=float).reshape(-1)
    mass_flow = np.asarray(mass_flow_kg_s, dtype=float).reshape(-1)
    inlet = np.asarray(mixed_inlet_temperature_k, dtype=float).reshape(-1)
    outlet = np.asarray(outlet_temperature_k, dtype=float).reshape(-1)
    if not (power.size and power.size == mass_flow.size == inlet.size == outlet.size):
        raise ValueError("energy-balance arrays must be non-empty and share one length")
    if not all(np.isfinite(values).all() for values in (power, mass_flow, inlet, outlet)):
        raise ValueError("energy-balance arrays must be finite")
    if np.any(power < 0) or np.any(mass_flow <= 0):
        raise ValueError("total power must be non-negative and mass flow must be positive")
    heat_loading = power / mass_flow
    denominator = float(heat_loading @ heat_loading)
    if denominator <= 0:
        raise ValueError("at least one training point must have positive heat loading")
    inverse_heat_capacity = float(heat_loading @ (outlet - inlet) / denominator)
    if inverse_heat_capacity <= 0:
        raise ValueError("fitted effective heat capacity is not physically positive")
    return 1.0 / inverse_heat_capacity


def predict_outlet_energy_balance(
    total_power_w: np.ndarray,
    mass_flow_kg_s: np.ndarray,
    mixed_inlet_temperature_k: np.ndarray,
    effective_heat_capacity_j_kg_k: float,
) -> np.ndarray:
    """Predict a scalar mixed-outlet temperature from a lumped energy balance."""
    power = np.asarray(total_power_w, dtype=float)
    mass_flow = np.asarray(mass_flow_kg_s, dtype=float)
    inlet = np.asarray(mixed_inlet_temperature_k, dtype=float)
    heat_capacity = float(effective_heat_capacity_j_kg_k)
    if not (power.shape == mass_flow.shape == inlet.shape):
        raise ValueError("power, mass_flow, and inlet_temperature must share one shape")
    if not all(np.isfinite(values).all() for values in (power, mass_flow, inlet)):
        raise ValueError("energy-balance inputs must be finite")
    if np.any(power < 0) or np.any(mass_flow <= 0) or not np.isfinite(heat_capacity) or heat_capacity <= 0:
        raise ValueError("power must be non-negative; mass flow and heat capacity must be positive")
    return inlet + power / (mass_flow * heat_capacity)
