# Tutorial: Design and audit a bounded engineering agent workflow

## Scenario

A teammate asks an AI agent to review a Python calculation for one-dimensional steady conduction through a plane wall. The intended model is

\[
R_{cond} = \frac{L}{kA}, \qquad \dot{Q} = \frac{T_{hot}-T_{cold}}{R_{cond}}.
\]

The task is useful because it has a simple independent answer, explicit SI units, and clear limiting cases. It is not a claim about a complete thermal system.

## Step 1: establish the physical contract before using an agent

Write the following yourself.

| Item | Required statement |
| --- | --- |
| Objective | Check whether the code correctly evaluates plane-wall conduction resistance and heat rate. |
| Variables and units | `L` [m], `k` [W/(m K)], `A` [m²], `T_hot` and `T_cold` [°C or K difference], `R_cond` [K/W], `Q_dot` [W]. |
| Assumptions | Steady state, one-dimensional conduction, constant isotropic conductivity, no contact resistance, no heat generation. |
| Acceptance tests | Dimensional consistency; hand calculation; \(R\) increases with \(L\), decreases with \(k\) and \(A\); \(\dot Q=0\) when temperatures are equal. |
| Exclusions | No material-property lookup, external web search, repository writes outside the fixture, or changes to test expectations. |

If an AI agent produces an answer without this contract, it has not established an engineering result.

## Step 2: define the harness boundary

Configure or describe a harness with these limits:

- it may read only the assigned fixture directory and public course reference files;
- it may run the supplied test command and a short local calculation;
- it may propose a patch, but it may not apply it until the student reviews the diff;
- it may not use browser, cloud-drive, email, shell commands outside the fixture, credentials, or network services;
- every prompt, response, tool call, model/harness identifier, and changed file must be recorded in the AI-use record.

The same boundary applies whether the model is accessed through Codex, Claude Code, or a local agent client.

## Step 3: use a precise task request

An acceptable request has a physical objective and a verification plan, for example:

> Review the assigned plane-wall conduction fixture. First state the governing equation, variable units, and assumptions. Identify any defect without editing files. Then propose the smallest patch and list tests that would distinguish the corrected result from the defect. Do not access files or tools outside the fixture. Do not claim validation beyond the stated model.

Do not ask the agent to “finish the homework” or accept a patch only because a test passes.

## Step 4: inspect the agent trace

Check each of the following.

1. Did it use \(L/(kA)\), not an expression with incompatible units?
2. Did it preserve the stated boundary and forbid unsupported physical claims?
3. Did it identify all files it read and all proposed changes?
4. Did it cite a source only when the source was actually available and relevant?
5. Did it run tests that could fail for the seeded defect, rather than only a happy-path calculation?

Treat a confident unsupported answer as a failure case, not a partial success.

## Step 5: independently verify

Use the instructor-provided values or choose public-safe values. For example, with \(L=0.010\) m, \(k=200\) W/(m K), and \(A=0.020\) m²,

\[
R_{cond}=0.0025\ \mathrm{K/W}.
\]

For a 10 K temperature difference, \(\dot Q=4000\) W under the stated idealized model. Explain why this result may be physically unrealistic for a particular assembly even though the arithmetic is correct: convection, spreading, contact resistance, geometry, and property variation are excluded.

## Step 6: record the conclusion

Use the [harness specification template](HARNESS_SPECIFICATION_TEMPLATE.md). Your conclusion must distinguish:

- **implemented:** the code was changed or reviewed;
- **verified:** it passed the stated analytical and numerical checks;
- **not validated:** it has not been demonstrated to predict a real assembly outside the assumed plane-wall model.
