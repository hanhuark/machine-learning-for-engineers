# V. Reinforcement Learning for Engineering Control

## Status and intended use

This module introduces reinforcement learning (RL) as a framework for sequential decision-making. It is a focused learning module, not a claim that RL is appropriate for every engineering-control problem. The current material uses tabular Q-learning in a simple environment to establish the agent, state, action, reward, transition, and policy concepts before students work with an engineering-oriented environment.

## Engineering question

How should a controller choose actions over time when each action changes a system state and the engineering objective depends on cumulative reward, energy use, constraint violations, or terminal performance?

For an engineering adaptation, students must define the physical state variables and units, actuator/action bounds, timestep, reward terms, safety constraints, and a non-RL controller or policy baseline.

## Learning outcomes

Students should be able to:

1. formulate a state, action, transition, and reward for a bounded engineering-control problem;
2. implement and inspect tabular Q-learning on a transparent baseline environment;
3. explain the effect of learning rate, discount factor, and exploration schedule;
4. compare the learned policy to a non-RL baseline using cumulative reward *and* engineering constraints; and
5. identify unsafe, poorly specified, or non-transferable reward designs.

## Current tutorial

The introductory Q-learning walkthrough and animation remain available below. It is a conceptual prerequisite, not an engineering validation case. The detailed historical walk-through is retained in [the legacy Topic 5 materials](../../teaching_resources/legacy_assignments/TOPIC_5_ADVANCED_OPTIONS_LEGACY.md#option-1-reinforcement-learning).

![Q-learning walk](static/rlwalkgif.gif)

## Assessment expectation

A current assignment should require a short formulation note, a baseline controller/policy, a held-out or perturbed evaluation condition, a reward and constraint audit, and an individual defense. Do not grade a generated policy solely on reward from the training environment.

The previous multi-option Topic 5 assignment is retained for historical reference in [legacy assignments](../../teaching_resources/legacy_assignments/README.md); its generative-model and sequence-forecasting options are no longer part of this module.

## Development needed for a full engineering-control release

Before treating this as a full applied RL module, add a reproducible engineering environment with explicit units and constraints, deterministic baseline policies, seeded training/evaluation, and a failure case such as reward hacking or an out-of-regime disturbance.
