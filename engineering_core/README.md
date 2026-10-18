# Engineering core

This foundation is shared by every method and application studio. It teaches
students to decide what must be true before an ML model, generative model, or
agent result can support an engineering conclusion.

## Core workflow

1. Define the engineering decision, system boundary, and consequence of error.
2. Name inputs, target, units, availability at decision time, and constraints.
3. Classify the evidence as measured, simulated, derived, or synthetic; record
   data ownership, permitted use, and preprocessing.
4. Choose an independent sampling or splitting unit that prevents leakage.
5. Establish the simplest credible analytical, numerical, empirical, or
   human-reference baseline.
6. Evaluate on meaningful held-out conditions; inspect residuals, uncertainty,
   physical plausibility, and failure cases.
7. State what has been implemented, verified, validated, or remains untested.

## Reusable resources

- [Data-card template](../teaching_resources/DATA_CARD_TEMPLATE.md)
- [Reproducibility checklist](../teaching_resources/REPRODUCIBILITY_CHECKLIST.md)
- [Engineering ML rubric](../teaching_resources/ENGINEERING_ML_RUBRIC.md)
- [AI-use record template](../teaching_resources/AI_USE_TEMPLATE.md)
- [Engineering AI-literacy framework](../teaching_resources/ENGINEERING_AI_LITERACY_FRAMEWORK.md)
- [Cold-plate studio](../case_studies/ned3_coldplate_surrogate/), a worked
  simulated-CFD evidence route

## Planned foundation releases

| Topic | Required artifact | First use |
| --- | --- | --- |
| Data and split design | Worked examples of random, grouped, chronological, and condition-held-out splits | Regression, vision, and time series |
| Model selection | Decision guide linking data regime and engineering decision to a baseline and candidate method | Regression and case studios |
| Uncertainty and interpretation | Calibration, tolerance, uncertainty-source, and explanation audit | Regression, PINNs, and deployment cases |
| Failure analysis | Reusable failure-audit worksheet | Every graded module |

This directory will link to canonical materials rather than duplicate method
tutorials in `course_content/`.
