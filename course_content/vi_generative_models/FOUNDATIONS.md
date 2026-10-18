# Foundations: generative models and inverse engineering design

This guide teaches the questions that must be answered before a generative result can become an engineering candidate. It does not make this under-development module ready for graded assignment.

## 1. Separate three different tasks

- **Reconstruction:** infer a cleaner, lower-dimensional, or missing-data representation of a measured input.
- **Generation:** sample a new candidate from a learned distribution.
- **Inverse design:** search for an input or geometry that meets stated performance targets and constraints.

A visually plausible image, signal, or geometry is not automatically a physically credible one. Preserve provenance: measured, simulated, reconstructed, or synthetic.

## 2. A generative objective is not a feasibility guarantee

An autoencoder maps an input $x$ to a latent variable $z$ and reconstructs it as $\hat{x}$. A basic reconstruction objective is

$$
\mathcal{L}_{\mathrm{rec}} =
\frac{1}{n}\sum_{i=1}^{n}
\left\lVert x_i-\hat{x}_i\right\rVert^2.
$$

For a conditional generator, the intended distribution can be written

$$
x_{\mathrm{candidate}} \sim p_{\theta}(x\mid c),
$$

where $c$ records target conditions or properties. Neither expression proves that a candidate is manufacturable, stable, safe, or useful under conditions not represented in the data.

Inverse design must include explicit constraints:

$$
\min_{d}\; J(d)
\quad\text{subject to}\quad
g_j(d)\leq 0,\quad j=1,\ldots,m,
$$

where $d$ is the candidate design, $J$ is a stated objective, and each $g_j$ is a checkable limit such as mass, peak temperature, pressure drop, cost, stress, or a manufacturability rule.

## 3. Worked representative case

Run the constraint screen:

<pre><code>python ../short_code_demos/generative_design_screen.py</code></pre>

The script filters reported candidates using maximum mass in kg and maximum temperature in K. It intentionally does not generate candidates. Its lesson is that a model proposal remains a *candidate* until the reported properties and constraint checks are independently verified.

## 4. Evidence ladder for generated engineering content

1. **Plausible:** the output looks similar to training examples.
2. **Distributionally checked:** a held-out distributional or reconstruction metric is reported.
3. **Task-useful:** a held-out downstream task improves relative to a non-generative baseline.
4. **Physically screened:** stated conservation, units, bounds, and feasibility constraints are checked.
5. **Validated:** independent experimental or high-fidelity evidence supports the intended use.

Do not skip levels. A high visual-quality score belongs at the first level, not the last.

## Failure checks

- **Memorization:** generated samples reproduce training examples or sensitive source content.
- **Mode collapse or low diversity:** the generator produces a narrow subset of plausible cases.
- **Artifact amplification:** generated features reflect imaging, simulation, or preprocessing artifacts rather than physics.
- **Constraint violation:** a candidate passes a learned score but violates mass, temperature, stress, geometry, or manufacturability limits.
- **Out-of-distribution target:** the requested condition lies outside training coverage.
- **Synthetic-data confusion:** generated labels or images are mixed with measurements without clear labeling and a sensitivity analysis.

## Transfer task

Choose a public-safe image, waveform, or geometry case. State whether the goal is reconstruction, generation, or inverse design; name one non-generative baseline; define one held-out metric; and write two constraints with units that every candidate must satisfy.
