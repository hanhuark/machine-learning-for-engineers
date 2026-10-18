# Engineering AI platform roadmap

## Purpose

This repository develops engineering capability rather than a catalog of AI
products. Learners should be able to formulate a physical question, establish
what evidence is needed, build an appropriate model or agent workflow, verify
its output, and connect the result to an experiment, simulation, sensor,
robot, plant, or product decision.

The existing machine-learning course is the first implementation. The
[book companion](book_companion/) is a downstream view of material that has
been tested and stabilized; it does not determine the platform architecture.

## Capability architecture

| Capability | Repository home | Learner outcome |
| --- | --- | --- |
| Engineering evidence | [Engineering core](engineering_core/) | Define variables, units, data rights, baselines, split logic, uncertainty, and valid-use limits. |
| Modeling methods | [Course content](course_content/) | Select, train, evaluate, and critique ML/AI methods for a stated engineering question. |
| Agentic engineering workflows | [Engineering workflows](engineering_workflows/) and [Module IX](course_content/ix_ai_agent_harnesses/) | Bound skills, tools, MCP connections, permissions, logs, and verification before trusting agent output. |
| Physical integration and deployment | [Hardware and deployment](hardware_and_deployment/) | Connect models to simulations, sensors, DAQ, robotics, monitoring, and human decision points. |
| Discipline-led application | [Engineering application studios](case_studies/) | Apply shared evidence standards to a real engineering context without duplicating introductory ML courses by discipline. |
| Capstone and assessment | [Capstone and assessment](capstone_and_assessment/) | Demonstrate understanding through staged evidence, a failure audit, and an individual defense or physical demonstration. |

## Delivery sequence

### Release 1: shared engineering workflow

Create a common foundation for data/evidence contracts, baseline selection,
held-out evaluation, uncertainty and interpretation, and AI-assisted-work
records. Apply it first to the current regression, vision, PINN, and cold-plate
materials rather than adding new model families.

**Release evidence:** public templates, a worked physical-data example, an
instructor-held assessment pattern, and passing repository-integrity checks.

### Release 2: bounded agentic engineering

Expand the existing agent-harness module into a maintained workflow track:
commercial and local harnesses, reusable skills, MCP/tool schemas,
least-privilege permissions, tool-output verification, and evaluation.
Product names and setup instructions remain versioned repository material; the
durable learning outcomes are specification, provenance, safety, and evidence.

**Release evidence:** public-safe fixtures, a skill/harness specification,
independent acceptance tests, a no-install review route, and individual defense
prompts held outside the public repository.

### Release 3: physical integration

Develop reusable patterns for simulation-to-surrogate workflows, sensor/DAQ
data, multimodal measurement, digital-twin claims, and embodied control. Begin
with public-safe simulations or recorded data. Introduce hardware only after
safety, access, calibration, and instructor-support requirements are defined.

**Release evidence:** system boundary, signal/time-base schema, baseline,
operating range, failure mode, and demonstration protocol.

### Release 4: discipline-led studios

Develop a small number of deep cases for the College of Engineering Priority
Research Growth Areas. A studio is released only after a contributor confirms
the engineering question, data rights, variables/units, baseline, split rule,
and limitation statement.

**Release evidence:** contributor review, data card, runnable route, staged
assignment, and instructor-held individual evaluation.

## Initial studio portfolio

| Priority area | Candidate teaching problem | Status boundary |
| --- | --- | --- |
| Materials, Semiconductors and Power Electronics | Cold-plate CFD surrogate, electronics thermal management, additive manufacturing inspection | Cold-plate route is ready to assign; other cases require contributor and data review. |
| Food Systems and Nutrition | Vision or sensing for quality, poultry, or process monitoring | Needs a collaborator-approved public or course-controlled dataset. |
| Metabolic Health | Non-diagnostic sensing/data workflow and uncertainty-aware decision support | Requires strict privacy, ethics, and data-governance review before release. |
| Supply Chain and Contested Logistics | Forecasting, anomaly detection, routing, or resource allocation under uncertainty | Needs an operationally meaningful public/synthetic fixture and a defined decision cost. |
| Lithium and Critical Minerals | Process, materials, or imaging data with physical constraints | Needs a contributor-approved, rights-cleared case and baseline. |

## Non-negotiable evidence standard

No tutorial, agent run, benchmark score, simulation visualization, or physical
demo alone establishes an engineering claim. Every released activity must state
the decision, system boundary, variables and units, data/evidence class,
baseline, independent evaluation rule, failure boundary, and individual
evidence of understanding.
