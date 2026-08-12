# Tutorial guide

`tutorial_vi_heat_equation_pinn.py` is an executable, inspectable tutorial organized into four sections:

1. analytical and explicit finite-difference baselines;
2. forward PINN construction and training;
3. independent-grid error evaluation;
4. inverse estimation of thermal diffusivity.

Use `--mode quick` only to verify that the software pipeline executes. Its 100 training iterations are intentionally insufficient for a scientific accuracy claim. Use `--mode full`, inspect convergence and independent errors, and repeat with multiple seeds before interpreting model performance.

Suggested student modifications:

- plot all loss components on logarithmic axes;
- change the number and placement of collocation points;
- remove input scaling and compare convergence;
- replace `tanh` and explain why piecewise-linear activations are problematic for a PDE requiring a second derivative;
- vary the initial diffusivity estimate;
- repeat inverse training with clean and higher-noise observations;
- implement hard boundary constraints and compare them with soft penalty enforcement.
