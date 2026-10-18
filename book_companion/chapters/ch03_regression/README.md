# Chapter 3 Regression and Surrogate Modeling

> **Companion state: reference implementation.** This route supports the
> proposed regression chapter with a transparent physical-data example and a
> reproducible simulation-based surrogate case. It is not a replacement for
> the final book chapter or evidence of hardware validation.

## Engineering questions

1. When can a model estimate a continuous engineering response accurately enough
   for a stated screening decision?
2. Does a flexible ML model improve on a simple, interpretable baseline?
3. What evidence limits a regression model to interpolation, a particular
   geometry, or a simulated rather than measured system?

## Companion routes

| Route | Evidence class | Core comparison | What it teaches |
| --- | --- | --- | --- |
| [Regression module](../../../course_content/i_regression/) | Educational tabular example | Interpretable regression models and feature availability | Train/validation/test roles, residuals, forecasting versus explanation. |
| [Cold-plate surrogate studio](../../../case_studies/ned3_coldplate_surrogate/) | Steady simulated CFD | Mixed-outlet energy balance versus ordinary least squares | Units, control-volume assumptions, surrogate validity, and held-out CFD evaluation. |
| Pool-boiling heat-flux route | Measured experimental data | To be released as a versioned companion route | Nonlinear response, uncertainty, and a physical operating-range boundary. |

## Required learning evidence

Use the [chapter contract](../../CHAPTER_CONTRACT.md) with either executable
route. A completed exercise must include:

1. an input/target table with units, source, and availability at the decision
   time;
2. a declared independent split and a statement of what data remain held out;
3. an interpretable baseline before a flexible model;
4. RMSE and MAE in the target's physical units, residual inspection, and a
   largest-error discussion;
5. one physical-plausibility or valid-range check; and
6. a statement separating implementation, verification, CFD validation, and
   hardware validation.

## Method-selection guidance

Start with the engineering decision and data regime rather than a preferred
algorithm. Linear or low-order models are useful when interpretability and
simple trends matter. Tree ensembles are useful tabular baselines but should
not be trusted for unconstrained extrapolation. Neural networks require a
split-aware training/validation procedure and an explicit reason that their
added flexibility is useful. Gaussian-process models are useful for modest
datasets when model-based predictive uncertainty is relevant, but their kernel
assumptions and computational scaling must be reported.

## Transfer and failure tasks

- Change a split to represent a different operating condition or time period;
  explain why a random split might overstate generalization.
- Test a model on an out-of-range input without reporting the resulting number
  as a reliable prediction.
- Compare a low-error result with a conservation, monotonicity, limiting-case,
  or engineering-tolerance check.
- Record one AI-assisted suggestion, the independent evidence used to evaluate
  it, and whether it was accepted or rejected.

## Next implementation work

The next Chapter 3 artifact is a versioned pool-boiling route with a data card,
rights review, environment file, deterministic split, baseline correlation or
physical bound, uncertainty discussion, and a runnable figure-generation
script. Do not copy experimental data into this repository until its release
and redistribution boundary are confirmed.
