# Foundations: physics-informed neural networks for transient heat conduction

This guide explains the physical baseline that a PINN must satisfy. The module uses synthetic data and a controlled one-dimensional problem; it is not evidence of performance on a real material system.

## 1. State the thermal model and its limits

The dependent variable is excess temperature $T(x,t)$ in K above a fixed boundary temperature. For a homogeneous one-dimensional rod with constant thermal diffusivity $\alpha$ in m²/s, no heat generation, and fixed end temperatures,

$$
\frac{\partial T}{\partial t}
=\alpha\frac{\partial^2T}{\partial x^2}.
$$

The dimensionless diffusion time is the Fourier number:

$$
\mathrm{Fo}=\frac{\alpha t}{L^2}.
$$

It compares elapsed time to the diffusion timescale. With $L=0.10$ m, $\alpha=1.0\times10^{-5}$ m²/s, and $t=200$ s, $\mathrm{Fo}=0.2$. This value is dimensionless.

## 2. Analytical and numerical baselines come first

For the module's sine initial condition, the analytical solution is

$$
T(x,t)=T_0
\exp\left(-\frac{\pi^2\alpha t}{L^2}\right)
\sin\left(\frac{\pi x}{L}\right).
$$

An explicit finite-difference baseline also has a known stability requirement:

$$
\frac{\alpha\Delta t}{\Delta x^2}\leq\frac{1}{2}.
$$

For example, if $\Delta x=0.002$ m and $\alpha=1.0\times10^{-5}$ m²/s, an explicit timestep must not exceed $0.2$ s. This is a numerical-stability condition, not a statement that the spatial grid is sufficiently accurate.

## 3. What the PINN adds

A neural approximation $T_{\theta}(x,t)$ is differentiated automatically to form a residual:

$$
r_{\theta}=
\frac{\partial T_{\theta}}{\partial t}
-\alpha\frac{\partial^2T_{\theta}}{\partial x^2}.
$$

The training objective combines residual, initial-condition, boundary-condition, and optional observation losses. Its components can decrease at different rates. A small composite loss is not independent proof that the temperature field or inferred diffusivity is correct.

## 4. Worked representative case

Run the analytical baseline:

<pre><code>python ../short_code_demos/heat_equation.py</code></pre>

The script reports $\mathrm{Fo}=0.2$ at 200 s and checks the initial and boundary conditions. Then run the full module tutorial and compare its PINN output with the analytical field on a grid that was not used as training/collocation points.

## 5. Inverse problem boundary

In the inverse exercise, sparse synthetic observations estimate $\alpha$. Because the observations are generated from the same governing equation that constrains the PINN, the exercise tests implementation and noise sensitivity—not model-form adequacy. For a real experiment, boundary conditions, material heterogeneity, sensor dynamics, and heat losses can be uncertain and correlated.

## Failure checks

- **Residual-only success:** The PDE residual is small while initial, boundary, or held-out temperature error is unacceptable.
- **Loss imbalance:** One loss term dominates, leaving another physical constraint unsatisfied.
- **Scaling error:** Inputs or losses differ greatly in magnitude and produce misleading optimization progress.
- **Grid leakage:** The same analytical grid is used to tune the model and report final accuracy.
- **Numerical baseline error:** The finite-difference timestep violates its stability condition or the spatial grid is not checked for convergence.
- **Model-form error:** A real specimen violates the one-dimensional, constant-property, or fixed-boundary assumptions.

## Transfer task

Change one assumption—internal heat generation, a convective boundary, spatially varying conductivity, or uncertain initial temperature. State which governing equation, boundary condition, data source, and validation baseline must change before a PINN result could be interpreted.
