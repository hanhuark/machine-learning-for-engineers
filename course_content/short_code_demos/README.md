# Short code demonstrations

These demonstrations are intentionally small enough to read in one sitting. They are not turnkey homework solutions and do not replace the module tutorials, data cards, assignments, or independent validation. Each script uses only Python and NumPy, runs in seconds, and ends with a question a learner should be able to answer without an AI assistant.

Install the one shared dependency from the repository root:

```powershell
python -m pip install numpy
```

| Method or workflow | Demo | Engineering check to explain |
| --- | --- | --- |
| Regression | [`regression.py`](regression.py) | Is held-out MAE small enough in the target's physical unit? |
| Classification | [`classification.py`](classification.py) | What failure type changes when the decision threshold changes? |
| PCA | [`pca.py`](pca.py) | How much information is retained, and what does reconstruction lose? |
| Segmentation | [`segmentation.py`](segmentation.py) | Why can pixel accuracy be misleading for a small object? |
| Reinforcement learning | [`reinforcement_learning.py`](reinforcement_learning.py) | How does the reward encode collision or other constraint consequences? |
| Time series | [`time_series.py`](time_series.py) | Why must the holdout remain later in time than training data? |
| PINN baseline | [`heat_equation.py`](heat_equation.py) | Do the analytical solution's boundary and initial conditions hold? |
| Agent-harness verification | [`engineering_agent.py`](engineering_agent.py) | Does the calculation satisfy limiting cases before it is trusted? |
| Generative/inverse design | [`generative_design_screen.py`](generative_design_screen.py) | Which generated candidates violate explicit constraints? |

Run one example, for example:

```powershell
python course_content/short_code_demos/regression.py
```

## Mathematical notation

The modules use GitHub's TeX notation: inline expressions use `$...$`; displayed equations use `$$...$$` on separate lines. The companion GitHub Pages site loads MathJax so these same expressions render in the browser. See the [math and code authoring guide](../../docs/MATH_AND_CODE_GUIDE.md) before adding new material.

## Responsible use

The numbers are **illustrative** except where a module explicitly identifies a public data source. Learners must state the variables, units, assumptions, split rule, and independent check before interpreting output as an engineering finding.
