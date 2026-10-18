# VII. Time-Series Forecasting and Prognostics

> **Status: ready to assign for the simulated thermal-RC core.** The legacy PCA–LSTM/boiling materials are preserved as a reference extension and must be refreshed before graded use.

**Five-minute demo:** Run [`thermal_rc_forecasting.py`](tutorials/thermal_rc_forecasting.py). It simulates a lumped thermal system, holds out an entire shifted condition, and compares persistence with a training-only linear autoregressive-with-exogenous-input (ARX) baseline.

**Current assignment:** Complete the [AI-resilient thermal-forecasting assignment](ASSIGNMENT_AI_RESILIENT.md) and consult the [simulated-data card](data_card_thermal_rc.md). The fixture is illustrative simulation, not experimental evidence or a validated digital twin.

**Detailed foundations:** Read [forecasting and prognostics foundations](FOUNDATIONS.md) for the time base, sequence-window equation, baseline metric, split design, and failure checks.

## Engineering question

Given the history of a physically meaningful observable and known inputs, what can be forecast at a stated horizon—and does that forecast remain useful when the operating condition changes?

The current fixture predicts temperature $T$ in degrees Celsius from a known heat-load command $P$ in watts. It uses the simulated balance $C\,dT/dt=P-(T-T_a)/R$, sampled every 0.1 s. The held-out run changes thermal resistance and ambient temperature, so good performance on adjacent samples alone cannot be mistaken for transfer across conditions.

## Why this is a separate module

Forecasting and prognostics are not merely another neural-network architecture. They introduce time ordering, forecast horizon, autocorrelation, regime change, drift, alarm consequences, and leakage risks that are different from the image and tabular modules. The current materials address forecasting only; maintenance/prognostics content is a planned extension.

## Current materials

The [tutorials](tutorials/) folder contains the runnable [thermal-RC forecasting script](tutorials/thermal_rc_forecasting.py), plus historical Python, notebook, MATLAB, and vapor-fraction files. The latter are reference materials, not validated current solutions.

## Current assessment requirements

1. Use the supplied train, validation, and condition-held-out test runs; do not pool or randomly split their windows.
2. Fit any scaling/normalization using training data only.
3. Compare persistence and the simple ARX baseline before trying a higher-capacity model.
4. Report held-out horizon-dependent MAE/RMSE and forecast plots—not training loss as evidence of performance.
5. Diagnose the shifted resistance/ambient test condition and state what the simulation cannot establish about a physical device.
6. Require students to state the observable, units, sampling interval, input window, forecast horizon, and intended decision use.

## Assessment expectation

Students should submit a split plan, baseline forecast, model comparison, held-out forecast plot, error-versus-horizon analysis, and a short defense. A strong result on adjacent windows from one time record is not evidence of cross-condition generalization.

The [time-series refresh protocol](REFRESH_PROTOCOL.md) still applies to the legacy boiling extension and any replacement measured-data case.
