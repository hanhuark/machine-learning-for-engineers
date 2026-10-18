"""Fit a line and evaluate it only on held-out engineering measurements."""

import numpy as np


def fit_line(feature: np.ndarray, target: np.ndarray) -> tuple[float, float]:
    """Return least-squares slope and intercept for a one-feature model."""
    design = np.column_stack((feature, np.ones_like(feature)))
    slope, intercept = np.linalg.lstsq(design, target, rcond=None)[0]
    return float(slope), float(intercept)


def mean_absolute_error(observed: np.ndarray, predicted: np.ndarray) -> float:
    """Return MAE in the same unit as the engineering target."""
    return float(np.mean(np.abs(observed - predicted)))


if __name__ == "__main__":
    # Illustrative calibration data: pressure drop [kPa] versus flow rate [L/min].
    flow_train = np.array([1.0, 2.0, 3.0, 4.0])
    drop_train = np.array([2.1, 4.0, 6.2, 8.1])
    flow_test = np.array([1.5, 3.5])
    drop_test = np.array([3.0, 7.1])

    slope, intercept = fit_line(flow_train, drop_train)
    predicted = slope * flow_test + intercept
    print(f"pressure-drop model: delta_p = {slope:.2f} * flow + {intercept:.2f} kPa")
    print(f"held-out MAE: {mean_absolute_error(drop_test, predicted):.3f} kPa")
    print("Change the held-out operating point; do not report only training error.")
