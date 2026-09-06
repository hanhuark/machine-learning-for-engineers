"""A first engineering ML exercise using illustrative synthetic thermal data.

The script compares a linear thermal-resistance baseline with a quadratic
least-squares regression. It is a teaching demonstration, not a calibrated
thermal model or experimental validation.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

AMBIENT_TEMPERATURE_C = 22.0
TEST_START_POWER_W = 100.0
RANDOM_SEED = 7


def make_illustrative_data() -> tuple[np.ndarray, np.ndarray]:
    """Return power [W] and synthetic representative temperature [degC]."""
    power_w = np.arange(10.0, 141.0, 10.0)
    rng = np.random.default_rng(RANDOM_SEED)

    # Illustrative relation: baseline thermal resistance plus mild nonlinearity
    # and measurement-like noise. Coefficients are not for a real device.
    temperature_c = (
        AMBIENT_TEMPERATURE_C
        + 0.28 * power_w
        + 0.0009 * power_w**2
        + rng.normal(loc=0.0, scale=0.8, size=power_w.size)
    )
    return power_w, temperature_c


def mean_absolute_error(observed: np.ndarray, predicted: np.ndarray) -> float:
    """Return mean absolute error in the same units as temperature: degC."""
    return float(np.mean(np.abs(observed - predicted)))


def main() -> None:
    power_w, temperature_c = make_illustrative_data()
    train_mask = power_w < TEST_START_POWER_W
    test_mask = ~train_mask

    train_power_w = power_w[train_mask]
    test_power_w = power_w[test_mask]
    train_temperature_c = temperature_c[train_mask]
    test_temperature_c = temperature_c[test_mask]

    # Baseline: T = intercept + R_th * P. The fitted slope has units K/W.
    linear_coefficients = np.polyfit(train_power_w, train_temperature_c, deg=1)
    # Candidate: a more flexible empirical curve; its coefficients do not
    # establish a physical mechanism.
    quadratic_coefficients = np.polyfit(train_power_w, train_temperature_c, deg=2)

    linear_prediction_c = np.polyval(linear_coefficients, test_power_w)
    quadratic_prediction_c = np.polyval(quadratic_coefficients, test_power_w)
    linear_mae_c = mean_absolute_error(test_temperature_c, linear_prediction_c)
    quadratic_mae_c = mean_absolute_error(test_temperature_c, quadratic_prediction_c)

    print("Illustrative thermal prediction exercise")
    print(f"Training powers: {train_power_w.min():.0f}-{train_power_w.max():.0f} W")
    print(f"Held-out powers: {test_power_w.min():.0f}-{test_power_w.max():.0f} W")
    print(f"Linear baseline held-out MAE: {linear_mae_c:.2f} degC")
    print(f"Quadratic candidate held-out MAE: {quadratic_mae_c:.2f} degC")
    print(f"Fitted linear slope: {linear_coefficients[0]:.3f} K/W")
    print("This result is illustrative only; do not extrapolate beyond the data range.")

    plot_power_w = np.linspace(power_w.min(), power_w.max(), 200)
    figure, axis = plt.subplots(figsize=(8, 5))
    axis.scatter(train_power_w, train_temperature_c, color="#1f77b4", label="training data")
    axis.scatter(test_power_w, test_temperature_c, color="#d62728", label="held-out high-power data")
    axis.plot(
        plot_power_w,
        np.polyval(linear_coefficients, plot_power_w),
        color="#2ca02c",
        label="linear thermal-resistance baseline",
    )
    axis.plot(
        plot_power_w,
        np.polyval(quadratic_coefficients, plot_power_w),
        color="#9467bd",
        label="quadratic regression candidate",
    )
    axis.set_xlabel("Electrical power, P [W]")
    axis.set_ylabel("Representative device temperature, T [degC]")
    axis.set_title("Illustrative thermal prediction: train below, test above")
    axis.grid(alpha=0.25)
    axis.legend()
    figure.tight_layout()
    output_path = Path("first_model_results.png")
    figure.savefig(output_path, dpi=180)
    print(f"Saved plot: {output_path.resolve()}")


if __name__ == "__main__":
    main()
