"""Build a chronological holdout and a transparent persistence baseline."""

import numpy as np


def chronological_split(series: np.ndarray, test_count: int) -> tuple[np.ndarray, np.ndarray]:
    """Split a time-ordered signal without shuffling future values into training."""
    if not 0 < test_count < len(series):
        raise ValueError("test_count must be between 1 and len(series) - 1")
    return series[:-test_count], series[-test_count:]


def persistence_forecast(last_observation: float, horizon: int) -> np.ndarray:
    """Forecast no change from the final value available before the horizon."""
    if horizon < 1:
        raise ValueError("horizon must be at least one time step")
    return np.full(horizon, last_observation, dtype=float)


if __name__ == "__main__":
    # Illustrative vapor fraction [-], sampled at one stated interval.
    vapor_fraction = np.array([0.10, 0.14, 0.19, 0.25, 0.27, 0.31, 0.36, 0.40])
    train, test = chronological_split(vapor_fraction, test_count=3)
    print("training ends at index", len(train) - 1, "; held-out values:", test)
    print("persistence reference:", persistence_forecast(train[-1], len(test)))
    print("For a real forecast, use only observations available before the forecast horizon.")
