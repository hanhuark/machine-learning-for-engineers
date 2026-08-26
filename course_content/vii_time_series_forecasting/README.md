# VII. Time-Series Forecasting and Prognostics of Boiling Dynamics

> **Status: validation refresh in progress.** The legacy PCA–LSTM/sequence-to-sequence materials are preserved below, but the tutorial must be refreshed before use as a current graded assignment.

## Engineering question

Given the history of a physically meaningful observable, such as vapor fraction, what can be forecast at a stated horizon—and does that forecast remain useful when the operating condition changes?

The supplied legacy data record contains vapor fraction (dimensionless) as a function of time (ms) from boiling-image sequences sampled at 3,000 Hz (nominal timestep 0.33 ms). The learner's task is a direct multi-step forecast, with sequence-to-sequence RNN/GRU/LSTM architectures as candidate methods.

## Why this is a separate module

Forecasting and prognostics are not merely another neural-network architecture. They introduce time ordering, forecast horizon, autocorrelation, regime change, drift, alarm consequences, and leakage risks that are different from the image and tabular modules. The current materials address forecasting only; maintenance/prognostics content is a planned extension.

## Current materials

The [tutorials](tutorials/) folder contains the historical Python, notebook, MATLAB, and vapor-fraction materials. They are reference materials, not validated current solutions.

## Required refresh before assessment use

1. Use chronological, non-overlapping train/validation/test blocks. Where possible, hold out complete boiling runs or operating conditions.
2. Fit any scaling/normalization using training data only.
3. Compare persistence and simple autoregressive baselines with RNN/GRU/LSTM models.
4. Report held-out horizon-dependent MAE/RMSE and forecast plots—not training loss as evidence of performance.
5. Test at least one shifted condition, such as another heat flux or run, and diagnose failure.
6. Require students to state the observable, units, sampling interval, input window, forecast horizon, and intended decision use.

## Assessment expectation

Students should submit a split plan, baseline forecast, model comparison, held-out forecast plot, error-versus-horizon analysis, and a short defense. A strong result on adjacent windows from one time record is not evidence of cross-condition generalization.
