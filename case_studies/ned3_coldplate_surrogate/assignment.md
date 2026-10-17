# Current assignment: cold-plate outlet screening with physics and data

## Engineering question

For a liquid-cooled dual-chip cold plate, screen steady CFD boundary conditions
to estimate the **single released outlet-temperature scalar** before deciding
whether a more expensive CFD solve is warranted. The task is a simulated-CFD
exercise; it does not validate a physical device.

## AI-use boundary

This is an **AI-assisted and AI-audited** assignment. You may use an approved
AI coding tool for syntax, debugging, or code review. You remain responsible
for every calculation, assumption, and conclusion. Submit an `AI_USE.md` based
on the [shared template](../../teaching_resources/AI_USE_TEMPLATE.md), including
one recommendation you tested and one you rejected or corrected.

## Required workflow

1. Use the instructor-provided, checksummed subset. Record the source revision
   and manifest hash; do not train on files outside the assigned split.
2. Make a compact data contract that names the six inputs, target, units used
   by the tutorial, system boundary, and evidence class. Explain why
   `pdrop_*` is excluded.
3. Fit the constrained mixed-outlet model
   `T_out = T_in,mix + Q_total / (m_dot_total * c_eff)` using only the 80
   training simulations. State how `T_in,mix`, `Q_total`, and `m_dot_total`
   are calculated and why `c_eff` is an effective fitted parameter rather than
   a measured coolant property.
4. Fit the six-input ordinary-least-squares model to the **same outlet target**
   using the same 80 training simulations. Do not use test simulations to tune
   either model. Use the 20 validation simulations only for a declared choice,
   such as whether to retain a proposed preprocessing change.
5. Evaluate both models once on the fixed 40-simulation held-out test split.
   Report RMSE, MAE, maximum absolute error, and the test target range in K.
   Include a predicted-versus-CFD plot and identify the largest-error case for
   each model.
6. Conduct two failure or boundary checks. One must alter an input condition so
   that the energy-balance assumptions are violated or unavailable (for
   example, non-positive mass flow); explain why the model should reject it.
   The other must address an unsupported claim (for example, transient
   behavior, geometry transfer, pressure-drop units, or experimental accuracy).
7. Write a concise engineering recommendation: when is the constrained model
   adequate for this release, when would you run CFD, and what evidence would
   be needed before using a similar model for hardware design?

## Individual evidence of understanding

After submission, complete a brief individual check using an instructor-held
perturbation. Before executing code, predict the effect of one changed heat
load, inlet temperature, or mass-flow condition on `T_out`. Then explain the
result, one metric, and one limitation of the model you submitted. The check
assesses your understanding rather than authorship of the initial code.

## Submission

```text
lastname_firstname_coldplate/
  README.md
  analysis.py or analysis.ipynb
  environment.yml or requirements.txt
  AI_USE.md
  results/
    metrics.json
    figures/
```

Do not submit raw CFD archives, cached environments, or model checkpoints.
Grade with the [shared engineering-ML rubric](../../teaching_resources/ENGINEERING_ML_RUBRIC.md).

## Claim boundary

Your report must call the observations **simulated steady CFD results**. Do not
claim experimental validation, transient performance, circuit-resolved outlet
behavior, pressure-drop units, geometry transfer, or deployment readiness from
this assignment.
