"""Verify the analytical baseline used before training a heat-equation PINN."""

from math import exp, pi, sin


def fourier_number(alpha_m2_s: float, time_s: float, length_m: float) -> float:
    """Return the dimensionless diffusion time alpha*t/L^2."""
    return alpha_m2_s * time_s / length_m**2


def temperature_excess(x_m: float, time_s: float, length_m: float, amplitude_K: float, alpha_m2_s: float) -> float:
    """Return the analytical excess-temperature solution for the stated rod problem."""
    return amplitude_K * exp(-(pi**2) * fourier_number(alpha_m2_s, time_s, length_m)) * sin(pi * x_m / length_m)


if __name__ == "__main__":
    L, T0, alpha = 0.10, 50.0, 1.0e-5
    print(f"Fo at 200 s: {fourier_number(alpha, 200.0, L):.3f} [-]")
    print(f"midpoint excess temperature at 20 s: {temperature_excess(L / 2, 20.0, L, T0, alpha):.2f} K")
    print("Check the initial and boundary conditions before treating a PINN result as credible.")
