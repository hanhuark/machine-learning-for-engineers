# First 30 minutes: a thermal prediction model

**Time:** 25–40 minutes

**Level:** New to machine learning; basic algebra is enough

**Compute:** Any current Python installation or a browser session in Google Colab
**Evidence class:** Illustrative synthetic data; this is not a measured cold-plate data set.

## Engineering question

Can an input electrical power \(P\) predict a representative device temperature \(T\) well enough to support a bounded operating decision?

The included script uses an illustrative thermal system with:

| Symbol | Meaning | Unit |
| --- | --- | --- |
| \(P\) | electrical power applied to a device | W |
| \(T_{amb}\) | ambient temperature | degC |
| \(T\) | representative device temperature | degC |
| \(R_{th}\) | effective thermal resistance | K/W |

The first baseline is the linear thermal-resistance relation \(T=T_{amb}+R_{th}P\). A quadratic regression is then fitted as a more flexible data-driven candidate. The exercise intentionally tests the highest-power operating points, so it also illustrates why extrapolation needs caution.

## Run it

### Browser route

1. Open [Google Colab](https://colab.research.google.com/).
2. Create a new Python notebook.
3. Copy the contents of [`first_model.py`](first_model.py) into one cell and run it.

### Local route

```bash
python -m pip install -r requirements.txt
python first_model.py
```

The script prints held-out MAE values and saves `first_model_results.png` in the current directory.

## What to look for

1. Which model has the lower held-out mean absolute error (MAE), in degC?
2. Is the improvement large enough to matter for an allowable-temperature decision? The script does **not** answer that; the engineering requirement must be supplied.
3. Why does a held-out high-power region test something different from a random train/test split?
4. Would either model be credible at 250 W? Explain why the present data do or do not support that claim.

## Try one change

Change `TEST_START_POWER_W` from `100.0` to `80.0`, rerun the script, and explain how the evaluation question changes. Do not compare MAE values from different test ranges as if they measure identical difficulty.

## Common misconception

“The more flexible model has lower error, so it is the better engineering model.” Not necessarily. A model can fit this illustrative range while behaving implausibly outside it. In a real thermal system, geometry, airflow, material properties, boundary conditions, sensor placement, and operating regime affect the valid relationship.

## Where to go next

Continue to [Module I: Regression](../../course_content/i_regression/) for regression methods, residual analysis, data availability, and current assessment requirements.
