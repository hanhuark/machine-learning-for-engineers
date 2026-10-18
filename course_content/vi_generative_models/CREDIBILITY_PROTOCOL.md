# Generative and inverse-design credibility protocol

> **Release protocol, not a current assignment.** This protocol defines the evidence required before a generative-model or inverse-design tutorial can become an assessed activity.

## 1. Define the claimed role

Choose one role and state it precisely:

- reconstruct a degraded measurement;
- augment a training set;
- generate a physically constrained field or signal;
- propose a candidate design; or
- infer design variables from a target response.

Do not call a visually plausible image, field, or geometry an engineering design until its constraint checks and downstream task performance are evaluated.

## 2. Establish evidence and comparator

| Requirement | Minimum evidence |
| --- | --- |
| Data provenance | Rights, source, variables/units, acquisition conditions, independent split unit |
| Non-generative comparator | Interpolation, augmentation-free model, response surface, physics/correlation, or conventional optimization route |
| Held-out protocol | Entire run/device/condition/design family excluded from training and tuning |
| Engineering metric | Downstream prediction/measurement utility, constraint residual, feasibility rate, or experimental/simulation response |
| Failure audit | Memorization, mode collapse, artifacts, distribution shift, constraint violation, and false novelty |
| Disclosure | Every generated artifact labeled synthetic, reconstructed, or proposed—not measured |

## 3. Candidate feasibility screen

Before a candidate is ranked or fabricated, screen it for the constraints that apply to the case: geometry, mass/volume, material bounds, conservation, manufacturing, safety, cost, and operating range. A screen is not a substitute for an experiment or high-fidelity simulation; it establishes only the stated feasibility conditions.

## 4. Minimum learner evidence

The learner should produce a provenance statement, baseline comparison, held-out result, constraint screen, two failure examples, and a bounded engineering conclusion. The instructor should retain an unseen transfer or modification prompt for individual verification.
