"""Screen generated design candidates against explicit engineering constraints."""

from collections.abc import Iterable


def feasible_candidates(
    candidates: Iterable[dict[str, float | str]], maximum_mass_kg: float, maximum_temperature_K: float
) -> list[dict[str, float | str]]:
    """Keep only candidates whose reported properties meet both stated constraints."""
    return [
        candidate
        for candidate in candidates
        if float(candidate["mass_kg"]) <= maximum_mass_kg
        and float(candidate["peak_temperature_K"]) <= maximum_temperature_K
    ]


if __name__ == "__main__":
    candidates = [
        {"name": "candidate A", "mass_kg": 0.80, "peak_temperature_K": 340.0},
        {"name": "candidate B", "mass_kg": 1.20, "peak_temperature_K": 330.0},
    ]
    print(feasible_candidates(candidates, maximum_mass_kg=1.0, maximum_temperature_K=350.0))
    print("A constraint screen is not validation: verify candidate properties independently before use.")
