# IX. AI Agent Harnesses for Engineering Workflows

## Why this module exists

An AI model is not an engineering workflow. An **agent harness** is the surrounding system that gives a model instructions, context, tools, permissions, and a way to record and verify work. This module teaches students to design and audit that surrounding system for a bounded engineering task.

The goal is not to train students to hand an assignment to an agent. The goal is to help them decide what an agent may access or change, test its output against physics and data, and remain accountable for the resulting engineering claim.

## Learning objectives

After this module, a student should be able to:

1. Describe the role of instructions, workspace context, tools, permissions, logs, and verification in an AI-agent harness.
2. Compare a commercial hosted harness and a local/open-source deployment for a particular engineering task, including confidentiality, cost, capability, reproducibility, and operational burden.
3. Write a constrained task specification that states the physical objective, units, inputs, allowed files/tools, prohibited actions, and acceptance tests.
4. Distinguish a reusable **skill** (workflow instructions and resources), an **MCP server** (a protocol-based provider of tools/context), and a **plugin** (a distributable bundle that can include skills and connectors).
5. Independently verify an AI-assisted calculation or code change against an analytical result, a baseline, and a stated engineering limit.
6. Diagnose a failed or unsafe agent workflow: invalid assumptions, a false citation, improper data access, an unchecked tool call, or a result that passes a superficial test but violates physics.

## Core concepts

| Concept | Engineering interpretation | Required question |
| --- | --- | --- |
| Model | Produces candidate reasoning, code, or text | What evidence would make its output credible? |
| Harness | Controls the model's context, tools, permissions, and execution loop | What is it permitted to read, write, run, or send? |
| Skill | Reusable instructions, references, and optional helper scripts for a defined workflow | What domain checks must be followed every time? |
| MCP server | A standard interface through which an agent can obtain context or call tools | What data, units, provenance, and side effects does each tool expose? |
| Plugin | A distributable package that can bundle one or more skills and connectors | What capabilities become available after installation? |
| Verification gate | Independent test before a result becomes an engineering conclusion | Does the output satisfy conservation, units, limits, and held-out evidence? |

## Commercial and local examples

The module uses examples to make the architecture concrete; it does not endorse a vendor or require a paid account.

- **Commercial harnesses:** Codex and Claude Code are examples of coding-agent environments with project context, tool connections, and configurable behavior. Students may use an instructor-approved account only for public-safe, bounded class fixtures.
- **Local/open-source harnesses:** a local model runtime, an agent client, a controlled workspace, and explicitly exposed tools can provide a local deployment. Ollama is one example of a runtime that documents tool calling. A local model does not automatically make a workflow private, reproducible, accurate, or safe; the data path, logs, model version, hardware, and tool permissions still matter.
- **No-install path:** students without a supported commercial account or capable local hardware complete the same design, review, and verification work from an instructor-provided transcript/log. Access to a particular model must not determine the grade.

## A safe engineering harness pattern

```text
Physical question and acceptance tests
        ↓
Task specification: inputs, units, scope, constraints
        ↓
Read-only public-safe fixture + limited tools
        ↓
Agent proposes analysis or change; all tool calls are logged
        ↓
Student review: assumptions, provenance, units, diff, tests
        ↓
Independent analytical/baseline check and individual defense
        ↓
Evidence-bounded engineering conclusion
```

Start with read-only access. Allow writes only inside a disposable course fixture or a student-owned branch after review. Do not connect this module to student records, unpublished data, sponsor-restricted data, institutional credentials, laboratory controls, email, cloud storage, or unsupervised web actions.

## Course materials

- [Harness design tutorial](TUTORIAL.md): an instructor-led walk-through of a safe agent workflow.
- [Assignment: harness-assisted engineering verification](ASSIGNMENT.md): a two-part design, audit, and defense exercise.
- [Case study: mechanical-engineering-research skill](CASE_STUDY_ME_RESEARCH_SKILL.md): a public example of domain-rigor instructions.
- [Harness specification template](HARNESS_SPECIFICATION_TEMPLATE.md): the required design record.
- [Instructor implementation notes](INSTRUCTOR_NOTES.md): access, privacy, and assessment controls.
- [References and current product documentation](REFERENCES.md).

## Recommended placement

Use this as a one- to two-week advanced module after students have completed at least one programming-based ML assignment. It can also be introduced earlier as a short orientation, then revisited before the final project. It is not a prerequisite for the other ML modules.

## Assessment principle

A successful agent run is **not** evidence of learning. Credit is based on the student’s task boundary, independent verification, failure diagnosis, AI-use record, and short individual defense. Use the repository-wide [assessment policy](../../teaching_resources/ASSESSMENT_AND_AI_POLICY.md) and [engineering ML rubric](../../teaching_resources/ENGINEERING_ML_RUBRIC.md) alongside this module.
