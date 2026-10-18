"""Plan or download a pinned small teaching subset of the ColdPlate CFD release.

Downloading is opt-in. A course release must record a reviewed immutable
revision, preserve the generated manifest, and remain outside this repository.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
from typing import Iterable


REPOSITORY_ID = "UARK-NED3/ColdPlate-CFD-2000sims"
DEFAULT_MODEL_SETUP_PATH = "1_Dataset/model_setup.json"
DEFAULT_TRAIN_IDS = tuple(range(1, 81))
DEFAULT_VALIDATION_IDS = tuple(range(81, 101))
DEFAULT_TEST_IDS = tuple(range(1601, 1641))


def subset_plan(
    revision: str, model_setup_path: str = DEFAULT_MODEL_SETUP_PATH
) -> dict[str, object]:
    """Return the deterministic teaching-replication subset without downloading."""
    source_path = PurePosixPath(model_setup_path)
    if (
        not model_setup_path
        or "\\" in model_setup_path
        or source_path.is_absolute()
        or ".." in source_path.parts
        or str(source_path) in {".", ""}
    ):
        raise ValueError("model_setup_path must be a non-empty repository-relative source path")
    splits = {
        "train": list(DEFAULT_TRAIN_IDS),
        "validation": list(DEFAULT_VALIDATION_IDS),
        "test": list(DEFAULT_TEST_IDS),
    }
    simulation_ids = [identifier for split in splits.values() for identifier in split]
    source_files = [source_path.as_posix()] + [f"1_Dataset/sim_{identifier:04d}.npz" for identifier in simulation_ids]
    return {
        "source_repository": REPOSITORY_ID,
        "source_revision": revision,
        "evidence_class": "simulated CFD",
        "model_setup_path": source_path.as_posix(),
        "splits": splits,
        "source_files": source_files,
        "warning": (
            "This split reproduces a bounded teaching comparison. It is not an "
            "independent extrapolation, geometry-transfer, or experimental-validation test."
        ),
    }


def sha256(path: Path) -> str:
    """Return a SHA-256 digest without loading a potentially large file at once."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def write_manifest(destination: Path, plan: dict[str, object]) -> Path:
    """Write file hashes for the downloaded teaching subset."""
    files: list[dict[str, str]] = []
    for relative_name in plan["source_files"]:
        path = destination / str(relative_name)
        if not path.is_file():
            raise FileNotFoundError(f"Expected downloaded source file is missing: {path}")
        files.append({"path": str(relative_name), "sha256": sha256(path)})
    payload = dict(plan)
    payload["files"] = files
    manifest_path = destination / "teaching_subset_manifest.json"
    manifest_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return manifest_path


def download(destination: Path, plan: dict[str, object]) -> Path:
    """Download only planned source files using Hugging Face Hub."""
    try:
        from huggingface_hub import snapshot_download
    except ImportError as error:  # pragma: no cover - environment-specific dependency gate
        raise RuntimeError("Install huggingface_hub before using --download") from error

    destination.mkdir(parents=True, exist_ok=True)
    snapshot_download(
        repo_id=REPOSITORY_ID,
        repo_type="dataset",
        revision=str(plan["source_revision"]),
        allow_patterns=[str(path) for path in plan["source_files"]],
        local_dir=destination,
    )
    return write_manifest(destination, plan)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--revision", required=True, help="Immutable Hugging Face commit hash or reviewed tag")
    parser.add_argument("--destination", type=Path, default=Path("coldplate_teaching_subset"))
    parser.add_argument("--model-setup-path", default=DEFAULT_MODEL_SETUP_PATH)
    parser.add_argument("--download", action="store_true", help="Retrieve files; otherwise print the planned subset")
    arguments = parser.parse_args()

    plan = subset_plan(arguments.revision, arguments.model_setup_path)
    if arguments.download:
        manifest = download(arguments.destination, plan)
        print(f"Downloaded {len(plan['source_files'])} files and wrote {manifest}")
    else:
        print(json.dumps(plan, indent=2))


if __name__ == "__main__":
    main()
