# Assignment: forecast a shifted thermal condition

## Engineering question

Can a model trained on one lumped thermal condition forecast temperature during a different thermal resistance and ambient condition? Your goal is not to produce the most elaborate neural network. It is to make a defensible forecast claim with units, a baseline, and a clear boundary on what the simulation demonstrates.

## Materials and allowed tools

Run [`tutorials/thermal_rc_forecasting.py`](tutorials/thermal_rc_forecasting.py). You may use an AI assistant for coding, debugging, or explanation if you keep a short tool-use record. You remain responsible for every physical statement, split, calculation, and conclusion.

## Required work

1. State the energy-balance equation, the meaning and units of $T$, $P$, $R$, $C$, and $T_a$, the sampling interval, and the forecast horizon in both samples and seconds.
2. Run the fixture without changing its split. Report test-run MAE in $^\circ$C for persistence and for the training-only linear ARX baseline. Include a plot or table that identifies the held-out run.
3. Change **one** declared simulation condition (for example, test ambient temperature, thermal resistance, or the forecast horizon). Predict before running whether the two baselines will improve or degrade, then report the result and explain the mechanism from the governing balance.
4. Propose one higher-capacity forecasting model. Specify its input window, known future inputs, output horizon, tuning evidence, and the exact condition you would hold out. Do not report a neural-network result without the same comparison and split discipline.
5. Give two limitations that prevent this exercise from validating a physical converter, cold plate, or semiconductor digital twin.

## Deliverables

Submit a two-page technical note or equivalent annotated notebook, the minimally changed code, and an AI-use record of at most 150 words. Do not submit a raw chat transcript as a substitute for the explanation.

## Individual understanding check

Be prepared to explain why random splitting of overlapping time windows can leak information and to predict the temperature response when $P$ is set to zero while $T>T_a$. The instructor may change one parameter or horizon during a short oral or in-class check.

## Assessment criteria

| Criterion | Evidence |
| --- | --- |
| Physical interpretation | Correct system boundary, variables, units, and limiting-case reasoning |
| Evaluation validity | Whole-run split, training-only fitting, stated horizon, and relevant baselines |
| Analysis | Correct MAE units, interpretable comparison, and mechanism-based failure explanation |
| AI-enabled integrity | Clear record of assistance and demonstrated individual understanding |
