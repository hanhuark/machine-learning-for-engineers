# Foundations: AI agent harnesses as bounded engineering workflows

An engineering agent workflow is defined by its physical contract and verification gates, not by the name of a model or agent product.

## 1. Write the physical contract first

For a plane wall under the stated idealization, the conductive resistance and heat rate are

$$
R_{\mathrm{cond}}=\frac{L}{kA},
\qquad
\dot Q=\frac{T_{\mathrm{hot}}-T_{\mathrm{cold}}}{R_{\mathrm{cond}}}.
$$

Use $L$ in m, $k$ in W/(m K), $A$ in m², $R_{\mathrm{cond}}$ in K/W, and $\dot Q$ in W. Temperature differences may be expressed in K or °C. The equations assume steady, one-dimensional conduction with constant isotropic conductivity, no heat generation, and no contact resistance.

An agent must receive this contract before it sees the code. Otherwise a correct-looking implementation can answer a different problem.

## 2. Define the harness boundary

A minimal harness has five components:

1. **Task specification:** objective, variables, units, assumptions, acceptance tests, and exclusions.
2. **Context:** only public-safe fixture files and stated reference material.
3. **Tools and permissions:** read-only by default; no credentials, cloud storage, email, or unsupervised web access.
4. **Trace:** prompts, responses, files read, tool calls, and proposed changes.
5. **Verification gate:** a student checks units, limits, a hand calculation, code diff, and test result before making a claim.

The same pattern applies to commercial, local, and open-source harnesses. Local deployment changes the data path and operational burden; it does not remove the need for verification.

## 3. Worked representative case

Run the independent calculation:

<pre><code>python ../short_code_demos/engineering_agent.py</code></pre>

With $L=0.010$ m, $k=200$ W/(m K), $A=0.020$ m², and a 10 K temperature difference, the model gives $R_{\mathrm{cond}}=0.0025$ K/W and $\dot Q=4000$ W. The high heat rate may be inappropriate for a real assembly because spreading, convection, geometry, and contact resistance are excluded. Arithmetic correctness does not validate the assembly model.

## 4. Acceptance tests before agent execution

For this fixture, require the following:

$$
\dot Q=0\quad\text{when}\quad T_{\mathrm{hot}}=T_{\mathrm{cold}},
$$

and, with the other values fixed, resistance increases with $L$ and decreases with $k$ and $A$. These are limiting-case tests. They are independent of the agent's confidence, prose quality, or whether a generated unit test passes.

## Failure checks

- **Scope escape:** The agent reads, writes, or sends material beyond the approved fixture.
- **Unit error:** A formula mixes mm and m, or misstates K/W as W/K.
- **Hidden assumption:** The result omits the boundary condition or treats the idealized wall as a complete assembly.
- **Trace gap:** A result cannot be tied to the prompt, sources, tools, and file changes that produced it.
- **Test theater:** Tests confirm only a happy path and would not fail for a seeded defect.
- **Authority confusion:** An agent suggestion is reported as a validated engineering conclusion.

## Transfer task

Design a read-only agent task for a fluid, thermal, manufacturing, or energy calculation. Specify the physical contract, approved files/tools, prohibited actions, two acceptance tests, one independent baseline, and the evidence a student must present in a short defense.
