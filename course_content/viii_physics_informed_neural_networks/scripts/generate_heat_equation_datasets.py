"""Generate deterministic synthetic datasets for the PINN teaching module."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

import numpy as np
import pandas as pd

MODULE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MODULE_ROOT))

from src.heat_equation import HeatEquationConfig, analytical_temperature  # noqa: E402


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    config = HeatEquationConfig()
    data_dir = MODULE_ROOT / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    x_values = np.linspace(0.0, config.length_m, 101)
    time_values = np.linspace(0.0, config.final_time_s, 51)
    time_grid, x_grid = np.meshgrid(time_values, x_values, indexing="ij")
    reference = pd.DataFrame(
        {
            "x_m": x_grid.ravel(),
            "t_s": time_grid.ravel(),
            "T_excess_K": analytical_temperature(x_grid, time_grid, config).ravel(),
            "alpha_m2_s": config.alpha_m2_s,
            "source": "synthetic_analytical",
        }
    )
    reference_path = data_dir / "reference_temperature_field.csv"
    reference.to_csv(reference_path, index=False, float_format="%.10g")

    sensor_locations = config.length_m * np.array([0.2, 0.4, 0.6, 0.8])
    observation_times = np.linspace(10.0, config.final_time_s, 20)
    sensor_ids = np.repeat(["S01", "S02", "S03", "S04"], observation_times.size)
    x_observed = np.repeat(sensor_locations, observation_times.size)
    t_observed = np.tile(observation_times, sensor_locations.size)
    exact = analytical_temperature(x_observed, t_observed, config)
    rng = np.random.default_rng(54403)

    output_paths = [reference_path]
    for noise_std_K, label in ((0.0, "clean"), (0.5, "noise_0p50K"), (1.0, "noise_1p00K")):
        noise = np.zeros_like(exact) if noise_std_K == 0 else rng.normal(0.0, noise_std_K, exact.size)
        observations = pd.DataFrame(
            {
                "sensor_id": sensor_ids,
                "x_m": x_observed,
                "t_s": t_observed,
                "T_excess_K": exact + noise,
                "T_uncertainty_K": noise_std_K,
                "source": "synthetic_analytical_with_gaussian_noise" if noise_std_K else "synthetic_analytical",
            }
        )
        path = data_dir / f"inverse_temperature_{label}.csv"
        observations.to_csv(path, index=False, float_format="%.10g")
        output_paths.append(path)

    metadata = {
        "schema_version": "1.0",
        "evidence_class": "synthetic",
        "generator": "scripts/generate_heat_equation_datasets.py",
        "random_seed": 54403,
        "governing_equation": "dT/dt = alpha*d2T/dx2",
        "temperature_definition": "excess temperature above fixed boundary temperature",
        "parameters": {
            "length_m": config.length_m,
            "initial_amplitude_K": config.initial_amplitude_K,
            "alpha_m2_s": config.alpha_m2_s,
            "final_time_s": config.final_time_s,
        },
        "boundary_conditions": "T(0,t)=T(L,t)=0 K excess temperature",
        "initial_condition": "T(x,0)=T0*sin(pi*x/L)",
        "observation_design": {
            "sensor_x_over_L": [0.2, 0.4, 0.6, 0.8],
            "times_s": observation_times.tolist(),
            "noise_model": "independent zero-mean Gaussian, fixed seeded realization",
        },
        "files": {},
        "limitations": [
            "No experimental measurements are included.",
            "Synthetic observations use the same model assumed by the PINN.",
            "The noise model omits bias, drift, temporal correlation, and boundary uncertainty.",
        ],
    }
    for path in output_paths:
        metadata["files"][path.name] = {"sha256": sha256(path), "rows": sum(1 for _ in path.open()) - 1}
    (data_dir / "dataset_metadata.json").write_text(
        json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
    )

    print(f"Generated {len(output_paths)} datasets in {data_dir}")


if __name__ == "__main__":
    main()
