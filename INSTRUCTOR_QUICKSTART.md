# Instructor Quickstart: course in a box

This page is the operational entry point for instructors adapting the curriculum. It provides public teaching materials, not a substitute for local accessibility, academic-integrity, privacy, safety, or records-retention requirements. Keep answer keys, active quiz items, student work, grading records, and instructor-held evaluation fixtures in a private course area.

## Choose an adoption pathway

| Pathway | Best for | Public materials to use | Local work required |
| --- | --- | --- | --- |
| **A. Adopt one module** | An existing ME, thermal-fluids, manufacturing, or data-science course | One module README, tutorial, current assignment, data card, and rubric | Confirm local software/data access; create a private held-out or transfer check. |
| **B. Teach a 14-week ML-for-engineers course** | Upper-level undergraduate or graduate technical elective | The [14-week map](#pathway-b-14-week-course), shared assessment system, and one advanced track | Choose dates, local examples, quiz items, and capstone constraints. |
| **C. Use project/capstone integration** | Design, laboratory, or capstone course with an engineering artifact | [Application studios](case_studies/), method selector, evidence checklist, project rubric | Provide the engineering system, safety boundary, data rights, and a demonstration/defense format. |

## Before the term: complete these six decisions

1. **Select current materials.** Check [module status](MODULE_STATUS.md). Assign only items marked ready, and state the module version/commit in the syllabus or LMS.
2. **Set the computing route.** Confirm Python environment, student hardware, accessibility accommodations, and any approved cloud/HPC use. Python is the reproducible default; do not assume MATLAB access.
3. **Set the data boundary.** For each assignment, identify the source, license, units, independent sampling unit, and what students may upload to AI tools. Use the [data-card template](teaching_resources/DATA_CARD_TEMPLATE.md).
4. **Declare the AI mode.** Mark each activity AI-free, AI-assisted, or AI-audited using the [assessment policy](teaching_resources/ASSESSMENT_AND_AI_POLICY.md). Give students the [AI-use record](teaching_resources/AI_USE_TEMPLATE.md) for AI-assisted work.
5. **Create a private instructor area.** Store keys, current quiz questions, rubrics with scoring notes, student records, and instructor-held/late-release evaluation cases outside this repository.
6. **Run the learner route.** Execute each tutorial in a clean environment and record the command, expected run time, known limitation, and fallback route before publishing the assignment.

## Pathway A: adopt one module

Use this sequence for each module:

1. Give the lecture from the module README: engineering question, variables/units, baseline, method, and failure modes.
2. Run the short code demo or tutorial live; change one input or condition and ask students to predict the direction of the result first.
3. Release the current assignment—not the completed tutorial—as AI-assisted technical work unless you designate otherwise.
4. Require a staged submission: problem/split plan, baseline, technical artifact, held-out evaluation, and failure/limitation audit.
5. Conduct a 3–5 minute individual defense or an instructor-held modification after submission.
6. Grade with the [shared engineering-ML rubric](teaching_resources/ENGINEERING_ML_RUBRIC.md), adapted only where the module needs a more specific criterion.

### A lecture pattern that transfers across modules

| Segment | Student task | Instructor evidence of understanding |
| --- | --- | --- |
| Physical problem | Name system boundary, target, inputs, and units | Cold-call or low-stakes response identifies a missing variable/constraint. |
| Baseline | Derive or run the simplest defensible comparison | Student predicts a limiting case or failure of the baseline. |
| ML method | Connect the representation/model to the engineering question | Student explains why a feature, label, or architecture is appropriate. |
| Evaluation | Identify independent unit and held-out condition | Student diagnoses leakage or a misleading metric. |
| Transfer | Change geometry, regime, device, time block, or operating condition | Student states what result would or would not generalize. |

## Pathway B: 14-week course

This is a recommended course shell, not a mandated syllabus. It assumes one 14-week term and three lecture-equivalent contact hours per week. Weeks 10–12 use **one** advanced track; they are not intended to cover all advanced modules superficially.

| Week | Teaching focus | Student deliverable | Instructor-held evidence |
| --- | --- | --- | --- |
| 1 | Foundations, AI literacy, variables/units, splits and metrics | First-30-minutes self-check; policy acknowledgement | Short supervised code/metric reading check |
| 2–3 | [I. Regression](course_content/i_regression/) | Assignment: baseline and held-out residual analysis | Explain one excluded feature and one baseline |
| 4–5 | [II. Classification](course_content/ii_classification/) | Assignment: grouped split and threshold/failure analysis | Diagnose a misclassification or threshold decision |
| 6 | [III. PCA and clustering](course_content/iii_dimensionality_reduction_and_clustering/) | Structure/reconstruction interpretation | Explain a component or cluster against representative cases |
| 7–9 | [IV. Segmentation/object detection](course_content/iv_segmentation_and_object_detection/) | Visual measurement assignment and error audit | Inspect one failed prediction and identify likely cause |
| 10–12 | **Choose one:** [VII. thermal time series](course_content/vii_time_series_forecasting/), [VIII. PINNs](course_content/viii_physics_informed_neural_networks/), or a bounded [power-electronics thermal studio](case_studies/power_electronics_thermal_digital_twin/) | Advanced assignment with baseline, held-out condition, and limitation | Defend a model claim and identify evidence level |
| 13 | [IX. AI agent harnesses](course_content/ix_ai_agent_harnesses/) | Constrained harness specification and verification audit | Reject or repair an unsupported agent output |
| 14 | Engineering project integration | Project presentation, evidence packet, and transfer test | Explain decision, limitation, and next validation step |

**Module VII note:** its simulated thermal-RC core is ready to assign. The historical boiling PCA–LSTM materials remain a non-current extension pending data-rights and leakage/reproducibility refresh.

### Suggested grading distribution

| Evidence | Suggested share | What it establishes |
| --- | ---: | --- |
| Supervised quizzes and code-reading checks | 15–20% | Individual foundations and interpretation |
| Staged module assignments | 40–50% | Engineering workflow, baseline, and evidence quality |
| Individual defense/live modification | 10–15% | Ability to explain and modify submitted work |
| Project, presentation, and peer review | 20–30% | Transfer to an authentic engineering decision |

Do not use AI-detection output as the sole or primary evidence of learning. Assess understanding through explanations, changed conditions, transfer prompts, and bounded demonstrations.

## Pathway C: project or capstone integration

Use the [method selector](docs/method-selector.md) before selecting a model. Each project should begin with a one-page evidence plan containing:

- engineering decision, system boundary, target, inputs, units, and constraints;
- data source and redistribution/privacy boundary;
- simple physical, rule-based, or statistical baseline;
- independent split or external evaluation condition;
- success metric, error consequence, and likely failure mode; and
- planned demonstration, hardware/software artifact, or individual defense.

The public [application studios](case_studies/) provide examples, but a study is not ready for student distribution merely because it appears in the repository. Confirm contributor approval and data rights first.

## LMS/Blackboard preparation

Use the [LMS preparation checklist](teaching_resources/LMS_PREPARATION_CHECKLIST.md) when creating course shells. The repository supplies source materials and templates; it does not publish Blackboard packages, live quiz banks, keys, grades, or student records.

## End-of-term evaluation and improvement

Review each module against these questions:

1. Could students state the physical question, variables, units, baseline, and independent test?
2. Which misconceptions, tutorial failures, accessibility barriers, and AI-use problems recurred?
3. Did assignments demonstrate transfer beyond tutorial imitation?
4. Did the assessment route work equitably and within the stated tools/data boundary?
5. What needs a documented fix before the next offering?

Preserve the adopted commit/tag, course-specific syllabus, private assessment records, and a brief change log. Public improvements can be proposed through [CONTRIBUTING.md](CONTRIBUTING.md) without exposing student or restricted material.
