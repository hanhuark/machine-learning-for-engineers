# Cold-plate tutorial route

This route is executable after an instructor pins a reviewed source revision
and downloads the teaching subset outside the repository. It uses a transparent
linear scalar-temperature baseline before any POD-NN surrogate.

## Setup

```bash
python -m pip install numpy huggingface_hub
```

## Plan before downloading

The verified revision for this draft route is
`58911fc77390a70a6c71da0612e02b4976976283`. Confirm the canonical
[dataset card](https://huggingface.co/datasets/UARK-NED3/ColdPlate-CFD-2000sims)
before using a later revision; do not substitute a moving branch name.

```bash
python download_subset.py --revision 58911fc77390a70a6c71da0612e02b4976976283
```

The command prints the planned 141-file subset: 80 training simulations, 20
validation simulations, 40 test simulations, and the DOE configuration. This
is a bounded teaching-replication split, not an extrapolation or hardware
validation test.

## Download and record hashes

```bash
python download_subset.py --revision 58911fc77390a70a6c71da0612e02b4976976283 --download --destination C:\data\coldplate_subset
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

## Verified run

On 2026-10-17, the pinned subset download and baseline ran in a clean Windows
virtual environment using NumPy 2.5.4 and `huggingface_hub` 2.2.0. The 141
source files occupied 0.091 GiB after download. The 40-simulation held-out
linear-baseline result for `chip1_tmax|temperature` was RMSE = 1.56 K, MAE =
1.25 K, and maximum absolute error = 3.85 K. This is a reproducibility smoke
test for the specified simulated-CFD split, not an independent CFD-validation,
hardware-validation, or extrapolation result.

On that host, the baseline calculation completed in under one second; download
time depends on network throughput and Hugging Face access limits.

## Before calling this ready to learn

1. Run the route from a clean environment against a pinned source revision.
2. Check that `model_setup.json` is located at the documented source path; use
   `--model-setup-path` in the downloader only if the canonical card records a
   different path.
3. Record runtime, operating-range summary, source revision, and all hashes.
4. Add an energy-balance or thermal-resistance calculation and a failure case
   before introducing POD-NN.
