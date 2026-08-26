# Case study: the mechanical-engineering-research skill

The public [mechanical-engineering-research skill](https://github.com/hanhuark/mechanical-engineering-research-skill) is a useful case study because it does not merely ask an AI agent to sound like an engineer. It packages domain-rigor instructions and references intended to make agents check assumptions, validity ranges, uncertainty, CFD credibility, data leakage, and claim strength in thermal-fluid work.

## What students should study

1. **Workflow scope.** Identify the task families it addresses: correlation use, CFD review, experiment planning, data analysis, research coding, and AI/ML credibility.
2. **Rigor gates.** Find examples of checks that a generic coding assistant might omit: Reynolds/Prandtl/geometry validity ranges, mesh independence, boundary conditions, property models, uncertainty, and engineering tradeoffs.
3. **Packaging.** Observe that the repository includes a skill, plugin metadata for more than one harness, workflow prompts, public-safe examples, tests, and validation guidance.
4. **Evidence limits.** The skill can make a review more structured; it cannot create missing experimental data, establish a correlation outside its range, or turn a simulated result into a validated physical claim.

## Suggested classroom exercise

Give students the following deliberately overconfident claim:

> A coarse-mesh CFD study proves a microchannel heat sink is optimal because its average Nusselt number is 40% higher than a baseline. The model uses constant water properties and does not report pressure drop, pumping power, grid independence, or experimental validation.

Students should first review the claim without an agent. Then, using either an approved installation, an instructor-supplied output, or the repository’s public example, they compare the two reviews. They must identify:

- which physical and numerical checks changed the conclusion;
- what evidence is absent;
- which conclusion can be supported now; and
- what next computation or experiment would reduce the uncertainty.

## Guardrail for this course

Use public examples only. Do not install the skill into a workspace containing unpublished lab material or use it to upload confidential data. The learning outcome is the student’s ability to construct and assess the rigor gate, not merely invoke a named workflow.
