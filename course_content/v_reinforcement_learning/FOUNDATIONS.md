# Foundations: reinforcement learning for bounded engineering control

This guide introduces the mechanics and limits of tabular Q-learning. It is a teaching model for a bounded simulation, not permission to deploy an unverified learned controller on hardware.

## 1. Formulate the control problem

At decision step $k$, the controller observes a state $s_k$, selects an action $a_k$, receives reward $r_{k+1}$, and transitions to $s_{k+1}$. For a mobile robot, a state might include position $[x,y]$ in m, heading in rad, range-to-obstacle in m, and speed in m/s. An action might be a bounded turning or wheel-speed command. The timestep $\Delta t$ must be stated.

The discounted return is

$$
G_k = \sum_{j=0}^{\infty}\gamma^j r_{k+j+1},
\qquad 0\leq\gamma<1.
$$

Reward is not a physical law. It is a designer-specified objective. For a classroom navigation simulation, one transparent form is

$$
r_{k+1} =
w_p\Delta d_{\mathrm{goal}}
-w_c I_{\mathrm{collision}}
-w_u\lVert u_k\rVert^2
-w_t,
$$

where distance progress has units of m, $I_{\mathrm{collision}}$ is an indicator, $u_k$ is a bounded control command, and the weights convert competing terms into a documented utility. The chosen weights and constraint treatment determine learned behavior.

## 2. Q-learning update

For a discrete state-action table, Q-learning updates one value after each transition:

$$
Q(s_k,a_k)
\leftarrow
Q(s_k,a_k)+\eta
\left[r_{k+1}+\gamma\max_a Q(s_{k+1},a)-Q(s_k,a_k)\right],
$$

where $\eta$ is the learning rate. The bracketed quantity is the temporal-difference error. Exploration, such as $\epsilon$-greedy action selection, is needed to discover actions but can also produce unsafe simulated trajectories. Do not explore on physical hardware without a separate safety design.

## 3. Worked representative case

Run the one-update example:

<pre><code>python ../short_code_demos/reinforcement_learning.py</code></pre>

The script uses an explicit collision penalty and prints one updated Q value. Change only the penalty, then explain how the target in the update changes. This demonstrates reward sensitivity; it does **not** train a useful policy.

## 4. A defensible teaching comparison

Evaluate a learned policy against a simple policy that a student can explain, such as stop-before-obstacle, wall following, proportional steering, or a shortest-safe-path planner. For each evaluation episode, report success rate, collision count, travel time in s, energy proxy if defined, and the operating conditions. Hold out obstacle layouts or disturbances not seen during training.

## Failure checks

- **Reward hacking:** The agent earns reward without accomplishing the engineering objective.
- **Constraint masking:** A large average reward hides a small number of unacceptable collisions.
- **State aliasing:** The chosen state omits a variable needed to distinguish safe from unsafe situations.
- **Simulator gap:** The policy depends on ideal sensing, actuation, friction, latency, or geometry absent in hardware.
- **Evaluation leakage:** The same layouts, random seeds, or initial states appear during training and testing.
- **Unbounded action:** The policy commands values outside stated actuator, rate, or workspace limits.

## Transfer task

Define a two-action cooling, charging, or routing simulation. State the state variables and units, action bounds, timestep, a non-RL baseline, the reward terms, one hard safety constraint, and a perturbed test condition. Explain why a high training reward alone would be insufficient.
