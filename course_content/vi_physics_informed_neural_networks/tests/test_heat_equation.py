import numpy as np
import pytest

from src.heat_equation import (
    HeatEquationConfig,
    analytical_temperature,
    explicit_finite_difference,
    relative_l2,
)


def test_analytical_solution_satisfies_initial_condition():
    config = HeatEquationConfig()
    x = np.linspace(0.0, config.length_m, 101)
    expected = config.initial_amplitude_K * np.sin(np.pi * x / config.length_m)
    np.testing.assert_allclose(analytical_temperature(x, 0.0, config), expected, atol=1e-12)


def test_analytical_solution_satisfies_boundaries():
    config = HeatEquationConfig()
    time = np.linspace(0.0, config.final_time_s, 21)
    np.testing.assert_allclose(analytical_temperature(0.0, time, config), 0.0, atol=1e-12)
    np.testing.assert_allclose(analytical_temperature(config.length_m, time, config), 0.0, atol=1e-12)


def test_fourier_number_is_dimensionless_baseline_value():
    config = HeatEquationConfig()
    assert config.fourier_number(config.final_time_s) == pytest.approx(0.2)


def test_finite_difference_matches_analytical_solution():
    config = HeatEquationConfig()
    x, time, temperature = explicit_finite_difference(config, nx=51, dt_s=0.10)
    reference = analytical_temperature(x, time[-1], config)
    assert relative_l2(temperature[-1], reference) < 5e-4


def test_finite_difference_rejects_unstable_step():
    with pytest.raises(ValueError, match="Unstable explicit scheme"):
        explicit_finite_difference(HeatEquationConfig(), nx=51, dt_s=3.0)
