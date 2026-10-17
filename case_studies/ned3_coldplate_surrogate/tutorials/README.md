# Cold-plate tutorial route

This route is executable after an instructor pins a reviewed source revision
and downloads the teaching subset outside the repository. It uses an
interpretable energy-balance baseline and a transparent linear baseline before
any POD-NN surrogate.

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

## Run two complementary baselines

```bash
python run_linear_baseline.py --data-root C:\data\coldplate_subset
python run_energy_balance_baseline.py --data-root C:\data\coldplate_subset
```

The linear tutorial writes held-out RMSE, MAE, and maximum absolute error for
`chip1_tmax|temperature`. The energy-balance tutorial fits the single equation
`T_out = T_in,mix + Q_total / (m_dot_total * c_eff)` to training CFD cases and
evaluates `outlet_tavg|temperature` on held-out CFD cases. It converts each
heat-flux boundary condition to power using the 0.0016 m² chip area recorded in
the source release's analysis code. Temperatures are in K, mass flow is in
kg/s, heat flux is in W/m², and `c_eff` is in J/(kg·K). `c_eff` is a fitted
effective parameter for this simulated configuration; it is not a measured
coolant property. The calculation treats the release's one outlet scalar as a
mixed outlet and cannot resolve circuit-specific behavior.

For an apples-to-apples model comparison, run the linear baseline on the same
outlet target:

```bash
python run_linear_baseline.py --data-root C:\data\coldplate_subset --target outlet_tavg|temperature
```

Neither script uses `pdrop_*`, because the source deposit does not record the
pressure unit.

## Verified run

On 2026-10-17, the pinned subset download and both baselines ran in a clean
Windows virtual environment using NumPy 2.5.4 and `huggingface_hub` 2.2.0. The
141 source files occupied 0.091 GiB after download. On the 40-simulation
held-out split, the linear baseline for `chip1_tmax|temperature` had RMSE =
1.56 K, MAE = 1.25 K, and maximum absolute error = 3.85 K. The constrained
outlet energy balance had RMSE = 0.072 K, MAE = 0.053 K, and maximum absolute
error = 0.214 K; its fitted `c_eff` was 4188.9 J/(kg·K). A six-input ordinary
least-squares model on the same outlet target had RMSE = 1.875 K, MAE = 1.448
K, and maximum absolute error = 5.623 K. These are reproducibility smoke tests
for the specified simulated-CFD split, not independent CFD-validation,
hardware-validation, or extrapolation results.

On that host, the baseline calculation completed in under one second; download
time depends on network throughput and Hugging Face access limits.

## Before calling this ready to learn

1. Run the route from a clean environment against a pinned source revision.
2. Check that `model_setup.json` is located at the documented source path; use
   `--model-setup-path` in the downloader only if the canonical card records a
   different path.
3. Record runtime, operating-range summary, source revision, and all hashes.
4. For each prediction, inspect that all mass flows remain positive, all heat
   loads remain non-negative, and the output is an outlet scalar. Flag a model
   that violates these conditions instead of reporting its accuracy alone.
5. Compare the energy-balance residual against the linear-model residual on the
   same outlet target before introducing POD-NN; explain what physics the
   simpler equation omits.
