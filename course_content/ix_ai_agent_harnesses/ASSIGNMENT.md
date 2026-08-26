# Assignment: Harness-assisted engineering verification

## Purpose

Design and audit a narrowly scoped AI-agent workflow for an engineering calculation. Your grade reflects your engineering specification, verification, and defense—not how quickly an agent produces code.

## Part A — harness design record (individual)

Complete the [harness specification template](HARNESS_SPECIFICATION_TEMPLATE.md) for the assigned public-safe conduction fixture or an instructor-approved equivalent. State:

1. the physical question, governing equation, variables, units, assumptions, and excluded physics;
2. allowed files, tools, network status, write permissions, and prohibited actions;
3. the chosen environment: approved commercial harness, approved local/open-source harness, or instructor-provided trace;
4. the model/harness version or the supplied-trace identifier, date, and all AI assistance used;
5. at least three acceptance tests, including one limiting-case or dimensional check;
6. two foreseeable failures and the controls that prevent or reveal them.

## Part B — audit and verification (individual)

Using the approved boundary, ask the agent to review the fixture. Submit:

- the unedited prompt and an AI-use record;
- a short tool/file-access trace or the supplied transcript annotations;
- the agent’s proposed diagnosis and any proposed diff;
- your independent hand calculation and test results;
- one accepted output and one rejected, corrected, or caveated output;
- a 400–600 word engineering memo that states what the agent did, what you verified, what remains unvalidated, and why.

## Individual defense

Be prepared for a 5–8 minute individual defense. You may be asked to:

- derive the conduction equation and explain its units;
- modify one input or boundary condition and predict the direction of change before running code;
- identify a tool permission that should be removed;
- explain why a passing software test does not establish experimental validation;
- diagnose an inserted mistake in an AI-generated explanation or calculation.

## Grading

| Criterion | Weight |
| --- | ---: |
| Physical formulation, units, assumptions, and acceptance tests | 30% |
| Harness boundary, data/permission controls, and AI-use trace | 20% |
| Independent verification and correct evidence classification | 25% |
| Failure analysis and quality of rejected/caveated output | 15% |
| Individual defense | 10% |

## Rules

- Use only public-safe course files. Do not provide credentials, student information, unpublished research, restricted datasets, sponsor material, laboratory-control access, or personal cloud content to an agent.
- Do not enable unrestricted file writes, network access, or external connectors for this assignment.
- An agent may assist only after you have written the physical contract in Part A.
- A clean-looking notebook, a passing test, or an agent-generated report alone receives no credit for verification.
- Follow the course [AI-use policy](../../teaching_resources/ASSESSMENT_AND_AI_POLICY.md) and submit the [AI-use record](../../teaching_resources/AI_USE_TEMPLATE.md).
