# Engineering AI literacy framework

## Purpose and boundary

This framework helps instructors infuse AI literacy into an engineering machine-learning course without reducing it to prompt writing, tool demonstrations, or an academic-integrity warning. It is a public teaching framework, not institutional policy. Adapt it to local privacy, accessibility, academic-integrity, and data-governance requirements.

AI literacy concerns how a learner understands, uses, evaluates, and takes responsibility for AI systems. **Engineering AI literacy** adds the ability to connect those activities to a physical system, a decision, a data source, constraints, uncertainty, and independent evidence. A fluent, executable, or visually plausible AI output is not by itself engineering evidence.

## Learning outcomes

By the end of the course, students should be able to:

| Outcome | Student can | Evidence of learning |
| --- | --- | --- |
| 1. Task and tool reasoning | Define the engineering decision, then justify whether a conventional analysis, an ML model, a generative tool, an agent workflow, or no AI is appropriate. | Problem statement, baseline, and method-selection rationale. |
| 2. Interaction and specification | Give an AI system context, variables, units, assumptions, constraints, desired evidence, and acceptance criteria; revise an inadequate request after inspecting the response. | Annotated prompt or harness specification and a revision rationale. |
| 3. Data and provenance | Identify the source, ownership, units, labels, preprocessing, split unit, uncertainty, and permitted data path for AI-assisted work. | Data card and AI-use record. |
| 4. Responsible use | Identify privacy, confidentiality, bias, safety, intellectual-property, accessibility, environmental, and accountability concerns relevant to the task. | Risk/mitigation note linked to the engineering decision. |
| 5. Verification and communication | Test an AI-assisted claim against a baseline, held-out condition, analytical/numerical solution, physical limit, or independent source; state the remaining limitation. | Validation and failure audit plus an individual explanation. |
| 6. Workflow governance | Define a bounded agent workflow, including instructions, tools, permissions, logs, and a human verification point. | Harness specification, reproducible trace, and defense. |

## Progression

Use the outcomes at progressively higher levels rather than treating literacy as a single completed lesson.

| Level | Expected performance | Suitable course location |
| --- | --- | --- |
| Recognize | Identify common AI capabilities, limits, data risks, and assignment boundaries. | Week 1 orientation and AI-free foundation check. |
| Apply with guidance | Use an approved tool for a bounded task and document the interaction, data path, and a simple check. | Regression through segmentation modules. |
| Independently justify and verify | Choose or reject an AI approach, establish an engineering baseline, inspect failure cases, and defend the conclusion. | Advanced modules, agent-harness lab, and final project. |

## Course integration map

| Course component | AI-literacy emphasis | Suggested evidence |
| --- | --- | --- |
| Foundations | Capabilities/limits, data path, assignment mode, units, baseline thinking | Short code-reading and metric check; policy acknowledgement. |
| Regression and classification | Task selection, feature availability, leakage, threshold choices | Explain one rejected feature or invalid split; compare with a simple baseline. |
| Clustering and visual measurement | Representation, label/data quality, interpretability, visible failure cases | Annotate a misleading cluster or failed prediction. |
| Reinforcement learning and generative models | Objective/reward specification, constraint violations, synthetic-data/design credibility | Identify reward hacking, infeasible design, or unsupported generative claim. |
| Forecasting and PINNs | Temporal leakage, domain shift, governing-equation assumptions, independent numerical checks | Evaluate on a realistic held-out condition; compare PINN and analytical/numerical evidence. |
| AI agent harnesses | Instructions, skills, MCP/tools, permissions, logs, confidentiality, reproducibility | Constrained harness specification, output rejection, and individual defense. |
| Capstone | Integration of all outcomes | AI-assisted engineering decision dossier. |

## Assignment modes

Every assessment should state one of the following modes before students begin work.

1. **AI-free foundation check.** Students independently demonstrate essential concepts, code reading, or calculations.
2. **AI-assisted technical work.** AI may help only within stated boundaries; students submit an AI-use record and verify the work.
3. **AI-audited work.** Students must use AI, identify at least one limitation or failure, and evaluate the result against independent evidence.

Use the [assessment and generative-AI policy](ASSESSMENT_AND_AI_POLICY.md) and [AI-use record template](AI_USE_TEMPLATE.md) to operationalize these modes.

## Minimum evidence standard

For a consequential AI-assisted engineering claim, collect:

- the engineering question, system boundary, inputs, target, units, and decision context;
- data provenance, permissions, preprocessing, and split plan;
- an appropriate baseline or independent reference;
- the AI interaction or workflow record at the level needed for audit;
- quantitative and qualitative failure analysis; and
- a short individual explanation, defense, or live modification.

Do not require students to disclose credentials, private account information, confidential research, student records, restricted data, or complete private conversation histories.

## Instructor implementation sequence

1. Select two or three outcomes that fit the course rather than adding all outcomes at once.
2. State the assignment mode and data/tool boundary in the syllabus and each assignment.
3. Add one low-stakes AI-audited activity before allowing AI-assisted project work.
4. Use a common AI-use record and rubric language across modules.
5. Retain instructor-held evaluation fixtures, grading keys, and private data outside the public repository.
6. Review student evidence and revise the activity; do not treat tool access, polished code, or self-report as proof of competence.

## Design influences and further reading

- [Stanford Teaching Commons, *Understanding AI Literacy*](https://teachingcommons.stanford.edu/teaching-guides/artificial-intelligence-teaching-guide/understanding-ai-literacy): functional, ethical, rhetorical, and pedagogical AI-literacy domains with progressive objectives.
- [University of Florida, *AI Across the Curriculum*](https://www.ai.ufl.edu/teaching/ai-across-the-curriculum/): institution-wide progression from literacy to competence and expertise across disciplines.
- [University of Illinois, Campus AI Curriculum Task Force](https://provost.illinois.edu/about/committees/campus-ai-curriculum-task-force/): early, discipline-embedded, and capstone reinforcement of reflective and responsible AI use.
- [University of Michigan, course and assignment redesign guidance](https://genai.umich.edu/resources/faculty/redesigning-assessments): align AI use and assessment design with course outcomes.
- [UNESCO, *AI Competency Framework for Students*](https://www.unesco.org/en/articles/ai-competency-framework-students): human-centered, ethical, technical, and system-design dimensions with understand, apply, and create progression.
