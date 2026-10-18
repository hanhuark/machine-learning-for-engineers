# Physical demonstration protocol

Use this protocol when a course activity connects ML/AI to a sensor, actuator, robot, thermal system, DAQ system, or other physical asset. A functioning demonstration is evidence of integration; it is not, by itself, evidence that a model is valid or that each student understands it.

## Before implementation

1. State the system boundary, physical objective, variables, units, coordinate frame, time base, and operating range.
2. Identify hazards, safe operating limits, emergency stop/override, supervision requirements, and prohibited actions.
3. Define a non-AI or non-learning baseline controller, procedure, or decision rule.
4. Define the expected sensor/DAQ schema, calibration state, latency, synchronization rule, and missing-data behavior.
5. Specify which evidence may be generated with AI tools and which checks must be independently performed.

## Demonstration evidence

The public learner submission should include:

- the task specification and safety envelope;
- a baseline result and a proposed-model result under the same test protocol;
- a log of inputs, outputs, time base, and any intervention;
- at least one perturbed, held-out, or failure condition;
- a physical interpretation of success and failure; and
- an individual explanation or modification check.

## Minimum comparison table

| Condition | Baseline outcome | AI/ML outcome | Constraint violations | Interpretation |
| --- | --- | --- | --- | --- |
| Nominal |  |  |  |  |
| Perturbed sensor/operating condition |  |  |  |  |
| Known failure boundary |  |  |  |  |

## Claims to avoid

- “The system worked once, therefore the method is robust.”
- “The agent obtained high reward, therefore it is safe.”
- “The sensor output is accurate because the model prediction looks plausible.”
- “The model was deployed” when only a notebook demonstration was completed.

Use this protocol with the [engineering evidence checklist](../docs/engineering-evidence-checklist.md) and the [capstone assessment guidance](../capstone_and_assessment/).
