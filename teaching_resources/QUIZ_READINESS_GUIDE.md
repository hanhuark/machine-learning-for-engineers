# Quiz readiness guide: reasoning about ML for engineering

Short quizzes in this curriculum assess whether you can interpret an ML workflow as an engineering activity. They are not intended to reward memorizing vocabulary, code syntax, or a particular AI-tool response.

## What to be ready to do

For a brief engineering scenario, you should be able to:

1. identify the engineering objective, inputs, target, units, decision time, and important constraint;
2. state a simple analytical, empirical, rule-based, or persistence baseline and explain why it is relevant;
3. choose an independent train/validation/test split and identify a plausible source of leakage;
4. interpret an error metric, residual, confusion-matrix result, reconstruction, or visual failure in relation to the engineering decision;
5. distinguish a runnable demonstration from verification, validation, generalization, or deployment readiness;
6. identify when a model output violates a physical boundary, data boundary, or tool-permission boundary.

## How to study effectively

Do not begin by trying to memorize definitions. For each lecture, repository README, and tutorial, make a one-page engineering record:

| Prompt | Your record should contain |
| --- | --- |
| What physical or operational decision is being supported? | System boundary, operating condition, constraint, and decision owner. |
| What are the variables? | Inputs, target/label, units, time basis, and what is known at the time of the decision. |
| What is the simplest credible comparison? | Analytical relation, rule, conventional controller, persistence forecast, or transparent reference model. |
| What makes the evaluation independent? | Experiment, video, batch, geometry, operating campaign, time block, or other sampling unit. |
| What could fail? | Leakage, domain shift, invalid units, poor labels, sensor drift, physical implausibility, or a safety-relevant error. |
| What evidence would justify the claim? | Held-out result, error audit, independent reference, condition check, or individual explanation. |

Then rerun the tutorial yourself. Change one stated condition, predict the effect before execution, and explain the result in engineering terms. A quiz may ask you to reason through the same pattern with different numbers, geometry, operating condition, or decision consequence.

## Module-specific reasoning patterns

| Topic | Be able to reason about | Study route |
| --- | --- | --- |
| Foundations and regression | feature availability, temperature/pressure/flow units, baseline versus flexible fit, residual trends, extrapolation | [First 30 minutes](../learning_paths/00_first_30_minutes/), [Module I](../course_content/i_regression/) |
| Classification | class consequence, precision/recall, thresholds, grouped image splits, false-negative and false-positive implications | [Module II](../course_content/ii_classification/) |
| PCA and clustering | scaling, variance versus decision value, reconstruction, cluster stability, physical interpretation limits | [Module III](../course_content/iii_dimensionality_reduction_and_clustering/) |
| Segmentation and detection | what a pixel mask, object box, or class label can measure; calibration; held-out condition and visual error audit | [Module IV](../course_content/iv_segmentation_and_object_detection/) |
| Reinforcement learning | state/action/reward, safety constraints, conventional-policy baseline, simulation-to-physical transfer | [Module V](../course_content/v_reinforcement_learning/) |
| Time-series forecasting | prediction horizon, time-respecting split, window overlap, persistence baseline, drift | [Module VII](../course_content/vii_time_series_forecasting/) — use for graded quizzes only after the stated validation refresh |
| Generative and inverse design | conditioning, feasibility, manufacturing/physics constraints, independent candidate evaluation | [Module VI](../course_content/vi_generative_models/) — use for graded quizzes only when the module is released |
| PINNs | governing equation, units, boundary/initial conditions, residual versus solution error, reference-solution verification | [Module VIII](../course_content/viii_physics_informed_neural_networks/) |
| AI agent harnesses | task boundary, skills versus MCP tools, permissions, logs, independent verification, individual accountability | [Module IX](../course_content/ix_ai_agent_harnesses/) |

## Examples of the reasoning level

You should be able to decide whether a temperature measured *after* a test may be used to predict a pre-test power setting; explain why random frames from one video can be a weak test; identify why high accuracy can hide missed rare faults; or reject an agent-produced result that passes a software test but violates units. You are not expected to reproduce an entire notebook from memory.

## Assessment boundary

The exact active quiz questions, answer choices, numerical values, and answer keys are instructor-held. This preserves the quiz as one source of individual evidence. The course uses quizzes alongside tutorials, assignments, error audits, and individual explanation; no single artifact is treated as complete evidence of engineering competence.

For allowed AI use in other course activities, see the [assessment and generative-AI policy](ASSESSMENT_AND_AI_POLICY.md). A supervised quiz's permitted resources and tools will be stated by the instructor for that quiz.
