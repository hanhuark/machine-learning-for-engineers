# Module development standard

Use this standard when proposing a new module or moving an existing module from exploration to formal assessment.

## Required learner-facing components

| Component | Requirement |
| --- | --- |
| Engineering question | State the decision, system boundary, variables, units, operating range, and intended use. |
| Learning outcomes | Use observable actions: formulate, implement, compare, diagnose, justify, or communicate. |
| Foundations | Explain only the mathematics needed for the task; define assumptions and symbols. |
| Short demonstration | Provide one runnable method, one engineering check, and one modification prompt. |
| Full tutorial | Provide data access, environment, deterministic steps, expected outputs, and runtime expectation. |
| Data/evidence card | State source, rights, schema, units, sampling unit, preprocessing, and limitations. |
| Baseline | Provide a simple physical, empirical, rule-based, or conventional comparator. |
| Evaluation | Specify the independent split rule, metric, held-out condition, and error display. |
| Failure audit | Require at least one failure mode, limitation, or out-of-regime test. |
| Assessment | Require engineering reasoning and individual evidence beyond a polished submission. |
| Instructor notes | State setup, compute, safety, access, grading checkpoints, and material to hold privately. |

## Readiness labels

- **Ready to learn:** enough guided material exists for exploration; it is not necessarily suitable for grading.
- **Ready to assign:** all required components exist and the instructor has verified the current environment, data access, and assessment route.
- **Validation refresh required:** useful material exists, but dependencies, data, baselines, or evaluation need reconfirmation.
- **Under development:** the intended scope is public, but learners should not be assigned it as a finished module.

## Minimum acceptance evidence

Before a module is called ready to assign, confirm a learner can identify the target and units, reproduce a baseline, follow a valid split rule, interpret a held-out result, name a failure boundary, and explain their own work without relying on an AI-generated narrative.

See the [engineering evidence checklist](../docs/engineering-evidence-checklist.md) and [shared rubric](ENGINEERING_ML_RUBRIC.md).
