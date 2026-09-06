# Case-study template

Copy this directory to a descriptive, lower-case case name before adding a proposed or released engineering studio.

## Required files

- `README.md`: engineering question, audience, prerequisites, expected time, system boundary, variables/units, validity range, and learning outcomes.
- `data_card.md`: use the repository [data-card template](../../teaching_resources/DATA_CARD_TEMPLATE.md).
- `tutorial.ipynb` or a reproducible Python script: a runnable learning route with a documented command and expected runtime.
- `assignment.md`: staged evidence, baseline, split rule, held-out evaluation, failure audit, and individual check.
- `instructor_notes.md`: private/local adaptation needs, data restrictions, accessibility, and equipment/software requirements. Keep answer keys and instructor-held tests outside this public repository.
- `reproducibility.md`: environment, version, seed, output locations, and verification command.

## Required framing block

Place this near the top of each case README:

| Item | Complete before release |
| --- | --- |
| Engineering decision | What action, screening, or measurement does the learner support? |
| System boundary | What components, time interval, regime, and exclusions apply? |
| Inputs and target | Define symbols, units, coordinate/time basis, and availability at decision time. |
| Evidence class | Measured, simulated, synthetic, or derived; do not blur these categories. |
| Baseline | What simplest credible physics, empirical, rule-based, or human-reference method is compared? |
| Evaluation | What is the independent unit and held-out condition? What metric and uncertainty matter? |
| Failure boundary | Where should the model not be trusted, and what should a learner do instead? |

## Status language

Use **proposed** until a discipline contributor and data/rights owner approve the public case. Use **ready to learn** only after the tutorial and verification command work in a clean environment. Use **ready to assign** only after the assignment meets the repository's current assessment requirements.
