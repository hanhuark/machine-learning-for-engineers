# Reinforcement-learning embodied demonstration brief

> **Design brief, not a current assignment.** Use this only after an instructor selects a safe platform and validates the simulation, hardware, and assessment route.

## Candidate task

Move a small ground robot or equivalent safe mobile platform from a start zone to a goal zone without contacting obstacles. The same task must first run in a bounded simulator. A line-following, wall-following, or waypoint controller provides the baseline; a tabular or lightweight learned policy is the comparison.

## Required formulation

| Element | Example specification | Must be fixed before students begin |
| --- | --- | --- |
| State | Robot pose estimate, obstacle distance, heading error, and goal distance | Units, sensor source, update rate, missing-data behavior |
| Action | Discrete steering/velocity commands | Actuator bounds and stop rule |
| Reward | Goal progress minus collision, energy, time, and boundary penalties | Relative weights and rationale |
| Episode | Start pose through goal, timeout, boundary exit, or collision | Reset procedure and maximum duration |
| Baseline | Rule-based controller | Tuned without using learner test results |
| Held-out condition | Changed obstacle arrangement, starting pose, lighting, sensor noise, or surface condition | Predeclared evaluation protocol |

## Evidence sequence

1. **Simulation sanity check:** show state/action logs and compare a baseline controller with an untrained policy.
2. **Training audit:** plot return, collision count, and constraint violations separately; reward alone is insufficient.
3. **Simulation holdout:** evaluate seeds and layouts not used for tuning.
4. **Hardware checkout:** test sensing, actuation, emergency stop, and baseline policy before learned deployment.
5. **Physical demonstration:** conduct repeated trials under the stated protocol.
6. **Individual defense:** change a reward weight, safety threshold, or state feature; predict and explain the observed consequence.

## Required metrics

- goal completion rate;
- collision/boundary-violation rate;
- time to goal and path length;
- energy proxy or control effort where measurable;
- performance difference between nominal and held-out conditions; and
- reason for every termination.

## Safety and integrity boundary

The instructor retains authority over platform selection, speed limits, obstacle construction, supervision, and emergency stop. Students may use approved AI tools for code assistance only if they document the tool use and can explain or modify the deployed policy.

Use the shared [physical demonstration protocol](../../hardware_and_deployment/PHYSICAL_DEMONSTRATION_PROTOCOL.md) before release.
