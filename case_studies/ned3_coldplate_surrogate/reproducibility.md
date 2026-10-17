# Cold-plate studio reproducibility record

## Verified route

- Verification date: 2026-10-17.
- Source repository: `UARK-NED3/ColdPlate-CFD-2000sims`.
- Source revision: `58911fc77390a70a6c71da0612e02b4976976283`.
- Evidence class: simulated steady CFD.
- Host: Windows local environment.
- Python environment: isolated virtual environment with Python 3.12, NumPy
  2.5.4, and `huggingface_hub` 2.2.0.
- Retrieved files: 141 source files: 140 `.npz` simulations plus
  `1_Dataset/model_setup.json`.
- Local size after download: 0.091 GiB.

## Commands

```bash
python download_subset.py --revision 58911fc77390a70a6c71da0612e02b4976976283 --download --destination D:\MEEG-54403_course_data\coldplate_subset
python run_linear_baseline.py --data-root D:\MEEG-54403_course_data\coldplate_subset --output D:\MEEG-54403_course_data\coldplate_subset\coldplate_linear_baseline_metrics.json
python run_energy_balance_baseline.py --data-root D:\MEEG-54403_course_data\coldplate_subset --output D:\MEEG-54403_course_data\coldplate_subset\coldplate_energy_balance_metrics.json
```

The downloader writes `teaching_subset_manifest.json`, which records the source
revision, planned splits, and SHA-256 digest for every retrieved source file.
Keep that manifest with local course data; it is not committed here.

## Baseline result

For the fixed 80-train / 20-validation / 40-test teaching-replication split,
the NumPy ordinary-least-squares baseline predicted
`chip1_tmax|temperature` with:

| Metric | Value |
| --- | ---: |
| RMSE | 1.5579 K |
| MAE | 1.2468 K |
| Maximum absolute error | 3.8481 K |

The model uses six declared CFD boundary-condition inputs. This result only
checks that the released source, tutorial contract, and fixed simulated-CFD
split run coherently. It does not establish experimental validity, geometry
transfer, transient performance, uncertainty calibration, or safe design use.

## Constrained outlet energy-balance result

Using the same fixed teaching split, the tutorial fitted the training-set
effective parameter in

```text
T_out = T_in,mix + Q_total / (m_dot_total * c_eff)
```

where `Q_total` is calculated from the two heat-flux inputs and the 0.0016 m²
chip area used by the release's source code. The result for
`outlet_tavg|temperature` was:

| Quantity | Value |
| --- | ---: |
| Fitted `c_eff` | 4188.8946 J/(kg·K) |
| RMSE | 0.0724 K |
| MAE | 0.0532 K |
| Maximum absolute error | 0.2139 K |

The small residual is evidence that this constrained relation closely matches
this simulated, steady-state source configuration and fixed split. It is not
evidence that `c_eff` is a measured coolant property, that the model resolves
each circuit separately, or that the relation transfers to a different
geometry, fluid, operating range, or hardware system.

For the same outlet target and held-out split, the six-input ordinary
least-squares baseline gave RMSE = 1.8754 K, MAE = 1.4476 K, and maximum
absolute error = 5.6232 K. This comparison is instructional: it illustrates
how a physically structured relationship can be a more useful baseline than a
generic linear fit for one response under the documented source assumptions.
