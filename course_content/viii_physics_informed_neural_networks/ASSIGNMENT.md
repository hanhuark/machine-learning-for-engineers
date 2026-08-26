# Homework 6 - Physics-Informed Neural Networks for Transient Heat Conduction

## Purpose

Develop, verify, and critique a physics-informed neural network for a one-dimensional transient heat-conduction problem. Then estimate an unknown thermal diffusivity from sparse synthetic temperature observations.

The assignment evaluates physical formulation, numerical verification, inverse-problem reasoning, and individual understanding. A working notebook or low training loss alone is not sufficient evidence of correctness.

## AI-use classification

This is an **AI-assisted and AI-audited assignment**. Generative AI may be used for syntax, debugging, code review, and proposing experiments. You remain responsible for every equation, assumption, line of submitted code, and result.

Submit `AI_USE.md` containing:

1. tools and models used;
2. tasks for which they were used;
3. two representative prompts or task descriptions;
4. one recommendation you accepted and how you verified it;
5. one recommendation you rejected or corrected and why;
6. a statement that you can explain and modify all submitted work.

Do not submit private account information or an entire chat history.

## Physical model

Use the heat equation, boundary conditions, initial condition, symbols, and baseline parameters defined in `README.md`. State all assumptions and units in your report.

## Part A - Analytical and finite-difference baselines (15 points)

1. Derive the Fourier number `Fo = alpha*t/L^2` and calculate its value at the final time.
2. Plot the analytical temperature profile at a minimum of five times.
3. Implement or complete the explicit finite-difference solver.
4. Derive and enforce its stability condition.
5. Perform one spatial/time-step refinement comparison and report the change in error.

## Part B - Forward PINN (25 points)

1. Draw or describe the PINN computational graph from `(x,t)` to `T_theta`, derivatives, residual, and loss.
2. Implement the PDE residual with automatic differentiation.
3. Clearly distinguish interior, boundary, and initial-condition points.
4. Train a forward PINN with a fixed random seed.
5. Record architecture, activation, optimizer, learning rate, training iterations, point counts, and loss weights.
6. Plot each loss component separately rather than only total loss.

## Part C - Independent verification (20 points)

Evaluate the trained network on `reference_temperature_field.csv`, which must not be used for forward-PINN training.

Report:

- predicted and analytical temperature fields;
- absolute-error field;
- PDE-residual field;
- profiles at selected times;
- relative L2 error;
- maximum absolute temperature error;
- maximum initial-condition and boundary-condition errors;
- comparison with the finite-difference baseline;
- training and inference times.

Explain why a small PDE residual does not necessarily imply a small solution error.

## Part D - Inverse thermal diffusivity (20 points)

Treat thermal diffusivity as a positive trainable parameter and use the sparse observations in `inverse_temperature_noise_0p50K.csv`.

1. State the true value only after completing the blinded or instructor-provided evaluation, if applicable.
2. Estimate `alpha` from at least five independent random initializations.
3. Report the mean, standard deviation, and range of the estimates.
4. Repeat using the clean and `1.00 K` noise datasets.
5. Discuss how sensor location, time coverage, noise, and the initial guess affect identifiability.
6. Report relative diffusivity error when the reference value is available.

Do not define dimensionless time using the unknown diffusivity in a way that removes `alpha` from the inverse formulation.

## Part E - Failure audit and AI audit (15 points)

Perform at least three controlled failure experiments:

- remove most initial-condition points;
- imbalance the PDE and condition loss weights;
- use poorly scaled inputs;
- use an unsuitable activation function for second derivatives;
- concentrate collocation points in only part of the domain;
- introduce an incorrect sign or coefficient in the PDE residual.

For each experiment, state a prediction before running it, report the observed effect, and diagnose the mechanism.

Ask an AI coding tool to propose one improvement. Test that recommendation against independent-grid error, boundary/initial errors, and computational cost. Do not claim improvement based only on training loss.

## Part F - Individual verification (5 points)

During a short individual check, you may be asked to:

- explain one derivative or loss term;
- identify units and scaling;
- diagnose a supplied failure plot;
- modify a boundary condition or parameter;
- predict the effect before running the modified code.

## Required submission

```text
lastname_firstname_pinn/
  report.pdf
  forward_pinn.py or forward_pinn.ipynb
  inverse_pinn.py or inverse_pinn.ipynb
  AI_USE.md
  environment.yml or requirements.txt
  results/
    metrics.json
    figures/
```

The submitted code must run from top to bottom or from a documented command. Do not submit generated environments, caches, or large model checkpoints.

## Grading

| Component | Points |
| --- | ---: |
| Physical formulation and conventional baselines | 15 |
| Forward PINN implementation | 25 |
| Independent verification | 20 |
| Inverse diffusivity estimation | 20 |
| Failure and AI audits | 15 |
| Individual verification | 5 |
| **Total** | **100** |

## Claim and integrity requirements

- Label all provided temperature observations as synthetic.
- Distinguish solver convergence, numerical verification, model validation, and use validity.
- Do not call the PINN experimentally validated.
- Preserve the instructor-held evaluation data until its authorized release.
- Cite external code, text, figures, and datasets, including AI-assisted contributions as required by course policy.
