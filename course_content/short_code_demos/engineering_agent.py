"""Verify a simple agent-assisted calculation with independent physical checks."""


def conduction_heat_rate(
    length_m: float,
    conductivity_W_mK: float,
    area_m2: float,
    hot_temperature_K: float,
    cold_temperature_K: float,
) -> float:
    """Return one-dimensional steady plane-wall heat rate [W]."""
    resistance_K_W = length_m / (conductivity_W_mK * area_m2)
    return (hot_temperature_K - cold_temperature_K) / resistance_K_W


def conduction_acceptance_checks(length_m: float, conductivity_W_mK: float, area_m2: float) -> dict[str, bool]:
    """Return limiting-case checks for the declared plane-wall model."""
    base = conduction_heat_rate(length_m, conductivity_W_mK, area_m2, 310.0, 300.0)
    return {
        "zero_temperature_difference_gives_zero_heat_rate": conduction_heat_rate(
            length_m, conductivity_W_mK, area_m2, 300.0, 300.0
        ) == 0.0,
        "longer_wall_reduces_heat_rate": conduction_heat_rate(
            2 * length_m, conductivity_W_mK, area_m2, 310.0, 300.0
        ) < base,
        "larger_area_increases_heat_rate": conduction_heat_rate(
            length_m, conductivity_W_mK, 2 * area_m2, 310.0, 300.0
        ) > base,
    }


if __name__ == "__main__":
    heat_rate = conduction_heat_rate(0.01, 200.0, 0.02, 310.0, 300.0)
    print(f"heat rate: {heat_rate:.0f} W")
    print(conduction_acceptance_checks(0.01, 200.0, 0.02))
    print("This verifies only the stated idealized conduction model, not a complete thermal assembly.")
