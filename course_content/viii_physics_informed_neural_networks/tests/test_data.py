import json
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]


def test_reference_dataset_schema_and_size():
    frame = pd.read_csv(ROOT / "data" / "reference_temperature_field.csv")
    assert list(frame.columns) == ["x_m", "t_s", "T_excess_K", "alpha_m2_s", "source"]
    assert len(frame) == 101 * 51
    assert frame["source"].eq("synthetic_analytical").all()


def test_inverse_datasets_are_sparse_and_declared_synthetic():
    for path in sorted((ROOT / "data").glob("inverse_temperature_*.csv")):
        frame = pd.read_csv(path)
        assert len(frame) == 80
        assert {"sensor_id", "x_m", "t_s", "T_excess_K", "T_uncertainty_K", "source"}.issubset(frame.columns)
        assert frame["source"].str.startswith("synthetic").all()


def test_metadata_declares_evidence_class_and_units():
    metadata = json.loads((ROOT / "data" / "dataset_metadata.json").read_text(encoding="utf-8"))
    assert metadata["evidence_class"] == "synthetic"
    assert metadata["parameters"]["alpha_m2_s"] > 0
    assert len(metadata["files"]) == 4
