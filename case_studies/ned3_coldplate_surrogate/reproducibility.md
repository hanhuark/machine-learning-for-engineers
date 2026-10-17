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
