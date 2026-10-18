# Agentic engineering workflows

AI agents can accelerate coding, data inspection, literature triage, modeling,
and technical communication. They do not remove the need to define a physical
question, protect data, verify tool outputs, or remain accountable for an
engineering conclusion.

This track extends, rather than replaces, [Module IX: AI Agent Harnesses](../course_content/ix_ai_agent_harnesses/).

## Learning progression

| Level | Learner task | Required evidence |
| --- | --- | --- |
| Specify | Write a bounded task with variables, units, allowed inputs/tools, prohibited actions, and acceptance tests | Harness specification |
| Use | Run or inspect a commercial, local, or instructor-provided agent trace on a public-safe fixture | AI-use record and reviewed diff/output |
| Verify | Test the result against physics, code tests, a baseline, held-out data, or an independent source | Verification and failure audit |
| Package | Design a reusable skill or tool interface with permissions, provenance, and versioning | Skill/tool card and evaluation fixture |
| Defend | Explain or modify the workflow under an instructor-held perturbation | Individual defense or live check |

## Skills, tools, and MCP

A **skill** is reusable workflow guidance and supporting resources for a
bounded task. A **tool** performs a specific operation. An **MCP server** can
expose tools or contextual resources to an agent. These categories do not make
a workflow safe by themselves. Every use must specify what the agent may read,
write, execute, or transmit, and how the result will be checked.

The [Genesis Skills catalog](https://github.com/AI-ModCon/genesis-skills) is a
useful public example of portable science-and-engineering agent workflows. Use
it as a reference for skill organization, not as an unreviewed dependency or
as evidence that any installed skill is suitable for a particular course task.

## Engineering boundaries

- Start with public-safe, read-only fixtures.
- Do not expose credentials, student records, unpublished research,
  sponsor-restricted data, laboratory controls, email, cloud drives, or
  unrestricted web actions.
- Require a data/provenance check before a tool call and an independent
  verification gate after it.
- Keep instructor-held evaluation cases and answer keys outside this repository.
- Provide a no-install pathway using an instructor-provided trace so access to
  a paid service or local GPU does not determine the grade.

## Initial releases

1. Skill and harness design guide for engineering tasks.
2. Public fixture showing an agent-proposed model/data change, student review,
   and independent test.
3. Local/open-source comparison route with reproducibility and privacy limits.
4. Agent-assisted digital-twin or sensor-analysis workflow only after its data
   and deployment boundaries are documented.
