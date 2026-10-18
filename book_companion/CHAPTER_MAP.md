# Chapter map and implementation roadmap

The planned book has fourteen chapters in four parts. This map connects each
chapter to the canonical repository material and prevents the book companion
from becoming a second, inconsistent curriculum.

| Part and chapter | Canonical repository material | Current companion state | Next release criterion |
| --- | --- | --- | --- |
| I.1 Machine Learning in Mechanical Engineering | [Course gateway](../docs/), [AI-literacy framework](../teaching_resources/ENGINEERING_AI_LITERACY_FRAMEWORK.md), [case studies](../case_studies/) | Mapped | Create an engineering-problem taxonomy and a method-selection decision guide. |
| I.2 Engineering Data Preparation and Model Evaluation | [Data-card template](../teaching_resources/DATA_CARD_TEMPLATE.md), [reproducibility checklist](../teaching_resources/REPRODUCIBILITY_CHECKLIST.md), [assessment policy](../teaching_resources/ASSESSMENT_AND_AI_POLICY.md) | Mapped | Add a shared data/split/uncertainty tutorial with worked experimental and CFD examples. |
| I.3 Regression and Surrogate Modeling | [Regression module](../course_content/i_regression/), [cold-plate studio](../case_studies/ned3_coldplate_surrogate/) | Reference implementation | Maintain the detailed [chapter route](chapters/ch03_regression/), then add a versioned pool-boiling route. |
| I.4 Training Generalization and Failure Modes | [Quiz readiness guide](../teaching_resources/QUIZ_READINESS_GUIDE.md), [engineering ML rubric](../teaching_resources/ENGINEERING_ML_RUBRIC.md) | In development | Publish a cross-method hyperparameter, calibration, leakage, extrapolation, and failure-audit tutorial. |
| II.5 Classification for Engineering Diagnostics | [Classification module](../course_content/ii_classification/) | Mapped | Pin a small rights-cleared diagnostic dataset and group-held-out evaluation route. |
| II.6 Computer Vision for Mechanical Systems | [Classification module](../course_content/ii_classification/), [BoilingBench CV candidate](../case_studies/ned3_boilingbench_cv/) | In development | Resolve the public release record and provide a reproducible transfer-learning case. |
| II.7 Segmentation and Object Detection | [Segmentation module](../course_content/iv_segmentation_and_object_detection/), [flow-boiling evidence audit](../case_studies/ned3_flow_boiling_evidence_audit/) | Mapped | Add condition-held-out measurement error and annotation-quality exercises. |
| II.8 Dimensionality Reduction and Clustering | [PCA and clustering module](../course_content/iii_dimensionality_reduction_and_clustering/) | Mapped | Refresh legacy paths and add cluster-stability and physical-interpretation checks. |
| III.9 Time Series and Sequence Modeling | [Time-series module](../course_content/vii_time_series_forecasting/), [multimodal candidate](../case_studies/ned3_boiling_multimodal_signals/) | Validation refresh required | Release a rights-cleared sequence subset with chronological splits, naive baseline, drift, and missing-data tests. |
| III.10 Physics-Aware and Hybrid Machine Learning | [PINN module](../course_content/viii_physics_informed_neural_networks/), cold-plate studio | Mapped | Add dimensional analysis, constrained features, residual learning, uncertainty, and PINN-to-numerical-baseline comparisons. |
| III.11 Reinforcement Learning and Data-Driven Control | [RL module](../course_content/v_reinforcement_learning/) | Conceptual/special-topic option | Release a bounded simulation or hardware demonstration with safety constraints and a baseline controller. |
| III.12 Reproducible and AI-Assisted Engineering Workflows | [AI agent harness module](../course_content/ix_ai_agent_harnesses/), [course integrity check](../tools/check_course_integrity.py) | Mapped | Add maintained tool comparison, local/open route, experiment tracking, model/data cards, and a digital-twin deployment case. |
| IV.13 Engineering Case Studies | [Application studios](../case_studies/), [course-data registry](../course_data/) | In development | Build a balanced gallery spanning thermal fluids, manufacturing, materials/design, energy/condition monitoring, and robotics/control. |
| IV.14 Capstone Project Guide | [Shared rubric](../teaching_resources/ENGINEERING_ML_RUBRIC.md), [assessment policy](../teaching_resources/ASSESSMENT_AND_AI_POLICY.md), [project examples](../project_examples/) | In development | Publish a reusable capstone proposal, checkpoint, peer-review, and individual-defense kit. |

## Cross-cutting additions requested by reviewers

The following are threaded across chapters instead of becoming disconnected
survey chapters:

- explainability and engineering interpretation, including feature importance,
  partial-dependence reasoning, and limits of post-hoc explanations;
- uncertainty, calibration, risk-sensitive decisions, and error tolerance in
  physical units;
- feature engineering from signals, images, metadata, and dimensional analysis;
- small-data, transfer-learning, and domain-shift decisions;
- digital twins, deployment boundaries, and system monitoring;
- AI-assisted workflows, accountability, and verification;
- case coverage beyond thermal fluids, without implying unconfirmed partners or
  public-data availability.

The book companion should prioritize a small number of deep, reproducible cases
over a large collection of lightly documented examples.
