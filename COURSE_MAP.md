# Course map

## Recommended progression

The modules are ordered to build from supervised learning and data hygiene to higher-dimensional, dynamic, and physics-informed problems. The sequence is a recommendation, not a prerequisite chain for reuse.

| Week(s) | Module | Prerequisites | Engineering emphasis | Check for understanding |
| --- | --- | --- | --- | --- |
| 1 | Foundations | Python, arrays, plotting, basic probability | Units, data tables, train/validation/test purpose | Short supervised code-reading and metric quiz |
| 2-3 | I. Regression | Foundations | Feature availability, forecast vs. explanation, residuals | Defend one feature exclusion and one baseline |
| 4-5 | II. Classification | I | Image pipeline, group splits, threshold decisions | Diagnose a misclassification and confidence threshold |
| 6-7 | III. PCA and clustering | I-II | Representations, reconstruction, cluster stability | Explain a principal component using representative images |
| 8-10 | IV. Segmentation/object detection | II | Label quality, transfer learning, visual validation | Inspect and explain failed predictions |
| 11-12 | Advanced-track selection: V. Reinforcement learning, VI. Generative models, or VII. Time-series forecasting | Foundations plus relevant prior module | Sequential decisions, synthetic data, or dynamic forecasting | Present hypothesis, baseline, and limitation |
| 13-14 | VIII. PINNs | Calculus, differential equations, neural networks | Governing equations, inverse problems, model-form error | Modify a boundary condition and predict its effect |

The advanced-track modules are alternatives in a typical one-semester offering. Module VI is under development, and Module VII requires a validation refresh before it is used as graded material.

## Minimum competency standard

By the end of the course, a student should be able to independently:

1. Define the engineering objective, inputs, label/target, units, and relevant constraints.
2. Choose an independent sampling/splitting unit and identify plausible leakage.
3. Establish a simple baseline before claiming a complex model is useful.
4. Evaluate performance on meaningful held-out conditions and inspect failures.
5. State whether results demonstrate implementation, verification, validation, or only a screening-level result.
6. Use generative AI responsibly, verify its claims, and explain submitted work.

## Assessment checkpoints

Use multiple sources of evidence rather than treating a take-home notebook as proof of individual competence:

- short supervised foundational checks before a module;
- staged submissions: question/split plan, baseline, technical artifact, validation/failure audit;
- AI-use record for permitted AI-assisted work;
- short individual code defense or live modification after major assignments;
- an authentic final project with a designated held-out evaluation protocol.

The shared [assessment policy](teaching_resources/ASSESSMENT_AND_AI_POLICY.md) and [rubric](teaching_resources/ENGINEERING_ML_RUBRIC.md) specify the reusable framework.
