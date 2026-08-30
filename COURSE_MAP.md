# Course map

## Recommended progression

The modules are ordered by engineering task and evidence burden, not by a catalog of model families. The foundational sequence is a recommendation, not a prerequisite chain for reuse. Introduce the [engineering AI-literacy framework](teaching_resources/ENGINEERING_AI_LITERACY_FRAMEWORK.md) and AI-agent harness boundary during the first week, then assess them after students have completed at least one programming-based assignment.

| Week(s) | Module | Prerequisites | Engineering emphasis | Check for understanding |
| --- | --- | --- | --- | --- |
| 1 | Foundations + AI-literacy and IX orientation | Python, arrays, plotting, basic probability | Units, data tables, train/validation/test purpose, AI capabilities/limits, data/tool boundary | Short supervised code-reading and metric quiz plus a policy/AI-literacy check |
| 2-3 | I. Regression | Foundations | Feature availability, forecast vs. explanation, residuals | Defend one feature exclusion and one baseline |
| 4-5 | II. Classification | I | Image pipeline, group splits, threshold decisions | Diagnose a misclassification and confidence threshold |
| 6 | III. PCA and clustering | I-II | Representations, reconstruction, cluster stability | Explain a principal component using representative images |
| 7-9 | IV. Segmentation/object detection | II | Label quality, transfer learning, visual validation | Inspect and explain failed predictions |
| 10-12 | Advanced-track selection: VII. Time-series forecasting **after refresh**, VIII. PINNs, or V. RL as a conceptual/special-topic option | Foundations plus relevant prior module | Dynamic forecasting, governing equations, or constrained sequential decisions | Present hypothesis, baseline, and limitation |
| 13 | IX. AI agent harnesses lab | One prior programming-based engineering assignment | Tool boundaries, skills, MCP, plugins, verification | Defend a constrained workflow and reject an unsupported agent output |
| 14 | Capstone/project integration | At least two prior modules | Engineering decision, held-out evidence, communication | Explain a result, limitation, and next validation step |

The advanced-track modules are alternatives in a typical one-semester offering. Module IX can also be used as a one- to two-week lab alongside a later project. Module VI is under development, Module VII requires a validation refresh before it is used as graded material, and Module V requires an engineering environment before it is a full applied-control release. See [CURRICULUM_ARCHITECTURE.md](CURRICULUM_ARCHITECTURE.md) for module-level decisions and the planned industrial-AI roadmap.

## Minimum competency standard

By the end of the course, a student should be able to independently:

1. Define the engineering objective, inputs, label/target, units, and relevant constraints.
2. Choose an independent sampling/splitting unit and identify plausible leakage.
3. Establish a simple baseline before claiming a complex model is useful.
4. Evaluate performance on meaningful held-out conditions and inspect failures.
5. State whether results demonstrate implementation, verification, validation, or only a screening-level result.
6. Specify an AI-assisted task with relevant variables, units, constraints, evidence needs, and data boundaries.
7. Use generative AI responsibly, verify its claims, and explain submitted work.

## Assessment checkpoints

Use multiple sources of evidence rather than treating a take-home notebook as proof of individual competence:

- short supervised foundational checks before a module;
- staged submissions: question/split plan, baseline, technical artifact, validation/failure audit;
- AI-use record for permitted AI-assisted work;
- short individual code defense or live modification after major assignments;
- an authentic final project with a designated held-out evaluation protocol.

The shared [assessment policy](teaching_resources/ASSESSMENT_AND_AI_POLICY.md) and [rubric](teaching_resources/ENGINEERING_ML_RUBRIC.md) specify the reusable framework.
