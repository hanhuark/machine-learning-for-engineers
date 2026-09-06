# Module status and learner expectations

This table separates material that is useful to explore from material that is ready to assign. A completed notebook, an attractive figure, or a low training loss is not by itself evidence of engineering learning or validated model performance.

| Module | Start level | Typical time | Compute/access | Current status | Use now |
| --- | --- | ---: | --- | --- | --- |
| [I. Regression](course_content/i_regression/) | Foundations | 1–2 weeks | Browser/local Python; modest CPU | Ready to learn; current assignment available | Use the current AI-resilient specification; verify external tutorial/data access before grading. |
| [II. Classification](course_content/ii_classification/) | I | 1–2 weeks | Browser/local Python; optional GPU for larger CNNs | Ready to learn; current assignment available | Begin with grouped splits and a small data set. |
| [III. Dimensionality reduction and clustering](course_content/iii_dimensionality_reduction_and_clustering/) | I–II | 1 week | Modest CPU | Ready to learn; current assignment available | Refresh legacy local paths before a formal offering. |
| [IV. Segmentation and object detection](course_content/iv_segmentation_and_object_detection/) | II | 2–3 weeks | GPU helpful for training | Ready to learn; current assignment available | Use visual error audits and condition-held-out evaluation. |
| [V. Reinforcement learning](course_content/v_reinforcement_learning/) | Foundations | 1–2 weeks | Simulation; hardware is optional | Conceptual/special-topic option | Do not make it a full applied-control assignment until a bounded engineering environment is released. |
| [VI. Generative models and inverse design](course_content/vi_generative_models/) | I–IV | 1–2 weeks | Varies; GPU may help | In development | Explore concepts only; no current graded assignment. |
| [VII. Time series and prognostics](course_content/vii_time_series_forecasting/) | I plus dynamics | 1–2 weeks | Modest CPU/GPU varies | Validation refresh required | Do not grade until the data, dependencies, splits, and baselines are refreshed. |
| [VIII. PINNs](course_content/viii_physics_informed_neural_networks/) | I plus heat transfer/differential equations | 1–2 weeks | Local Python; GPU optional | Ready controlled teaching module | Use analytical/numerical checks and inverse-problem uncertainty. |
| [IX. AI agent harnesses](course_content/ix_ai_agent_harnesses/) | Foundations plus one programming assignment | 1 week | Approved AI tools; local alternative possible | Ready design/verification module | Introduce boundaries early and assess after students have technical context. |

## Status definitions

- **Ready to learn:** a learner can use the material as a guided resource, subject to the stated setup conditions.
- **Ready to assign:** includes a current assignment with an engineering question, baseline, split rule, evaluation, failure analysis, and individual evidence requirement.
- **Validation refresh required:** retain the concept, but verify the tutorial, data, dependencies, and evaluation protocol before graded use.
- **In development:** do not represent the material as a complete graded module.

For one-semester offerings, a defensible default is Foundations, I–IV, VIII, and a short IX lab. Treat advanced modules as selections rather than an obligation to cover every current AI topic.
