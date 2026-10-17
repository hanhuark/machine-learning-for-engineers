# Cold-plate tutorial route

This route is executable after an instructor pins a reviewed source revision
and downloads the teaching subset outside the repository. It uses a transparent
linear scalar-temperature baseline before any POD-NN surrogate.

## Setup

```bash
python -m pip install numpy huggingface_hub
```

## Plan before downloading

Obtain an immutable revision from the canonical [dataset card](https://huggingface.co/datasets/UARK-NED3/ColdPlate-CFD-2000sims).
Do not substitute a moving branch name for the reviewed revision.

```bash
python download_subset.py --revision REVIEWED_COMMIT_HASH
```

The command prints the planned 140-file subset: 80 training simulations, 20
validation simulations, 40 test simulations, and the DOE configuration. This
is a bounded teaching-replication split, not an extrapolation or hardware
validation test.

## Download and record hashes

```bash
python download_subset.py --revision REVIEWED_COMMIT_HASH --download --destination C:\data\coldplate_subset
```

The script writes `teaching_subset_manifest.json` with source revision and
SHA-256 values. Keep it with the local lesson data; do not commit it if it
contains a local path.

## Run the first baseline

```bash
python run_linear_baseline.py --data-root C:\data\coldplate_subset
```

The tutorial writes held-out RMSE, MAE, and maximum absolute error for
`chip1_tmax|temperature`. Interpret all temperatures in K. The script does not
use `pdrop_*` because the source deposit does not record its pressure unit.

## Before calling this ready to learn

1. Run the route from a clean environment against a pinned source revision.
2. Check that `model_setup.json` is located at the documented source path; use
   `--model-setup-path` in the downloader only if the canonical card records a
   different path.
3. Record runtime, operating-range summary, source revision, and all hashes.
4. Add an energy-balance or thermal-resistance calculation and a failure case
   before introducing POD-NN.
