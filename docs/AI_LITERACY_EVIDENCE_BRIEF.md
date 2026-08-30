---
layout: default
title: AI Literacy in Engineering Education
---

# AI literacy in engineering education

## Scope

This brief synthesizes public guidance, institutional implementations, and engineering-education literature that inform the curriculum. It distinguishes three evidence classes:

- **Institutional guidance:** current implementation choices and policies, not universal evidence of learning impact.
- **Scholarly literature:** peer-reviewed or clearly labeled preprint evidence that requires attention to design, population, and outcome measures.
- **This repository:** a reusable curriculum artifact and implementation case, not evidence that a single course causes learning gains across institutions.

Internal planning documents, student records, instructor-held assessment data, and confidential discussions are not part of this public brief.

## Why AI literacy is urgent in higher education

Generative and other AI tools can produce plausible text, code, images, and analyses quickly. That changes both professional practice and the evidentiary value of many traditional take-home assessments. Stanford advises instructors to begin with the actual learning outcome rather than an abstract debate about AI, while the University of Michigan asks instructors to decide whether AI should be used, how it should be documented, whether outcomes need revision, and whether assessment should change. [Stanford](https://teachingcommons.stanford.edu/news/pedagogic-strategies-adapting-generative-ai-chatbots) and [Michigan](https://genai.umich.edu/resources/faculty) frame these as course-design questions.

Urgency does not justify a generic or surveillance-oriented response. Current guidance consistently emphasizes human agency, transparent expectations, responsible use, and assessment evidence beyond generated output. UNESCO's student framework organizes AI learning around a human-centered mindset, AI ethics, techniques/applications, and system design at understand, apply, and create levels. [UNESCO](https://www.unesco.org/en/articles/ai-competency-framework-students?hub=66973)

For engineering, the urgent issue is not merely whether a student can prompt a chatbot. Graduates need to decide when AI is relevant, understand data and model limitations, protect sensitive information, verify outputs against independent evidence, and accept responsibility for decisions affecting safety, reliability, cost, and environmental impact.

## State of practice

### Competency frameworks and progression

Stanford's framework distinguishes functional, ethical, rhetorical, and pedagogical AI literacy, with objectives that progress from awareness to application and creation. Its guide combines instructional modules, practice, assessment activities, and instructor workshop materials. [Stanford Teaching Commons](https://teachingcommons.stanford.edu/teaching-guides/artificial-intelligence-teaching-guide/understanding-ai-literacy)

The University of Florida operationalizes a campus-wide model that separates knowing/understanding AI, using/applying AI, evaluating/creating AI, and AI ethics. Its model pairs broad literacy with optional deeper credentials and discipline-specific applications. [UF AI Across the Curriculum](https://www.ai.ufl.edu/teaching/ai-across-the-curriculum/) The University of Illinois recommends a three-part progression across majors: early modules on effective, reflective, and responsible AI; domain-specific tools in existing courses; and reinforcement in senior projects. [Illinois Campus AI Curriculum Task Force](https://provost.illinois.edu/about/committees/campus-ai-curriculum-task-force/)

### Faculty support, policy, and assessment

Mature institutional approaches provide more than a policy statement. Stanford supplies modular guidance and workshop kits; Michigan provides tool, prompt-literacy, training, policy, and assignment-redesign resources; and MIT recommends a clear, prominent, understandable AI-use policy with a rationale for every class. [Stanford guide](https://teachingcommons.stanford.edu/teaching-guides/artificial-intelligence-teaching-guide), [Michigan training](https://genai.umich.edu/resources/training), and [MIT faculty guidance](https://facultygovernance.mit.edu/ai-use-policy-and-resources-instructors-august-25-2026) illustrate this pattern.

For engineering specifically, Cornell's College of Engineering recommends linking AI decisions to the intended learning outcomes and acknowledges both pedagogical opportunities and the risk that AI becomes a crutch for foundational skills. [Cornell Engineering guidance](https://mtei.engineering.cornell.edu/teaching-resources/guidance-genai/)

### Engineering curriculum pathways

National workshop recommendations describe AI pathways as combinations of courses, combined courses, and embedded modules rather than a single required course structure. They identify mathematical foundations, core computing, machine learning, human-centered AI/ethics, generative AI, AI systems, and professional skills as foundational knowledge areas, while recognizing that institutional pathways vary. [NSF LEVEL UP AI curriculum pathways](https://cra.org/wp-content/uploads/2026/07/Designing-AI-Curriculum-Pathways-NSF-LEVEL-UP-AI-Workshop-Recommendations.pdf)

Recent engineering-education scholarship includes a systematic review of AI applications in engineering education and a review-plus-pilot introductory module for UK engineering students. These sources establish an active implementation literature but do not remove the need for more rigorous evidence on transfer, disciplinary judgment, and durable learning. [Liu et al. (2025)](https://doi.org/10.1109/access.2025.3532595) and [Hao et al. (2025)](https://doi.org/10.1109/TE.2025.3536105)

## Remaining issues

1. **Generic literacy versus engineering judgment.** Many frameworks apply across disciplines, but engineering tasks require variables, units, system boundaries, physical limits, uncertainty, safety consequences, and design constraints.
2. **Tool fluency versus evidence.** Prompt quality and tool access do not establish that a result is correct, generalizable, or suitable for an engineering decision.
3. **Policy versus learning design.** A syllabus rule is necessary but cannot replace explicit practice, feedback, assessment, and faculty development.
4. **Assessment validity.** AI-capable take-home work needs complementary evidence, such as staged artifacts, held-out cases, oral explanation, code modification, or in-class foundational checks. AI detection alone is not a valid indicator of learning.
5. **Data governance and equity.** Students need clear boundaries for confidential, sponsor-restricted, personal, proprietary, or otherwise sensitive data, along with equitable access or alternative pathways.
6. **Transfer across disciplines.** A shared foundation should reduce duplicated introductory content, but it must be tested through disciplinary cases rather than assuming that abstract knowledge transfers automatically.
7. **Public, reusable teaching infrastructure.** Instructors need adaptable tutorials, datasets, rubrics, data cards, AI-use records, and examples of failure analysis, not only high-level recommendations.

## Response of this curriculum

*Machine Learning for Engineers* uses a shared engineering-AI core with discipline-adaptable cases. Its design is captured in the [engineering AI-literacy framework](../teaching_resources/ENGINEERING_AI_LITERACY_FRAMEWORK.md): task and tool reasoning; interaction/specification; data and provenance; responsible use; verification/communication; and workflow governance.

The curriculum operationalizes these outcomes through:

- project-based modules that connect models to physical questions, units, baselines, and decisions;
- data cards and reproducibility checklists;
- AI-free, AI-assisted, and AI-audited assessment modes;
- failure analysis, held-out evaluation, and individual explanation; and
- a bounded AI-agent-harness module covering skills, MCP/tools, permissions, logs, and independent verification.

This approach is a template to adapt, not a substitute for local instructional design. It should be evaluated through multi-disciplinary implementation evidence, including common rubrics, transfer tasks, faculty adaptation records, and carefully governed student data.

## Implications for the planned education paper

The paper can make a distinct contribution by examining how a college-level AI-literacy framework connects to a shared engineering-AI/ML core and discipline-embedded application studios. The research question should not be whether one course can replace all disciplinary AI learning. A more defensible question is:

> Which common AI competencies can be taught and assessed through a shared engineering core, which require disciplinary embedding, and what evidence demonstrates students can transfer responsible engineering judgment to an unfamiliar application?

The existing curriculum and repository can serve as one implementation case. A stronger study would add co-designed cases across engineering disciplines, an explicit outcome crosswalk, common assessment criteria, independent or transfer evaluations, faculty implementation data, and appropriate human-subjects oversight before using student work as research data.

## Sources for continued review

- [Stanford Teaching Commons AI teaching guide](https://teachingcommons.stanford.edu/teaching-guides/artificial-intelligence-teaching-guide)
- [University of Michigan GenAI guidance for faculty](https://genai.umich.edu/resources/faculty)
- [University of Florida AI Across the Curriculum](https://www.ai.ufl.edu/teaching/ai-across-the-curriculum/)
- [University of Illinois Campus AI Curriculum Task Force](https://provost.illinois.edu/about/committees/campus-ai-curriculum-task-force/)
- [Cornell Engineering guidance on GenAI](https://mtei.engineering.cornell.edu/teaching-resources/guidance-genai/)
- [UNESCO AI Competency Framework for Students](https://www.unesco.org/en/articles/ai-competency-framework-students?hub=66973)
- [NSF LEVEL UP AI recommendations](https://cra.org/wp-content/uploads/2026/07/Designing-AI-Curriculum-Pathways-NSF-LEVEL-UP-AI-Workshop-Recommendations.pdf)
- [Liu et al., *The Application of Artificial Intelligence in Engineering Education: A Systematic Review*](https://doi.org/10.1109/access.2025.3532595)
- [Hao et al., *Integrating AI in Engineering Education*](https://doi.org/10.1109/TE.2025.3536105)
