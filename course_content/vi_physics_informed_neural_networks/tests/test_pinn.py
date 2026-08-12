import pytest

torch = pytest.importorskip("torch")

from src.heat_equation import HeatEquationConfig
from src.pinn import HeatPINN, pde_residual, sample_training_points


def test_sampling_shapes_and_ranges():
    config = HeatEquationConfig()
    domain, left, right, initial, initial_temperature = sample_training_points(config, 11, 7, 5, 1)
    assert domain.shape == (11, 2)
    assert left.shape == right.shape == (7, 2)
    assert initial.shape == (5, 2)
    assert initial_temperature.shape == (5, 1)
    assert torch.all(domain[:, 0] >= 0) and torch.all(domain[:, 0] <= config.length_m)
    assert torch.all(domain[:, 1] >= 0) and torch.all(domain[:, 1] <= config.final_time_s)


def test_pde_residual_shape_and_finiteness():
    config = HeatEquationConfig()
    model = HeatPINN(config, hidden_width=8, hidden_layers=2)
    domain, *_ = sample_training_points(config, 13, 2, 2, 2)
    residual = pde_residual(model, domain, config.alpha_m2_s)
    assert residual.shape == (13, 1)
    assert torch.isfinite(residual).all()
