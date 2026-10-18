# Time-series forecasting refresh protocol

> **Validation-refresh protocol.** Complete and document these checks before promoting this module to “Ready to assign.”

## Data audit

1. Identify the observable, units, sampling rate, timestamp source, run/device/condition identifier, and known regime changes.
2. Confirm that historical values are available at the intended forecast time; remove features that leak future information.
3. Record missing-data handling, filtering, scaling, and whether scaling parameters are fitted on training evidence only.
4. Establish a rights-cleared local or public data route, including a small fixture suitable for reproducibility tests.

## Benchmark route

Implement and preserve these comparators before any LSTM/GRU/sequence-to-sequence model:

| Comparator | Why it is needed |
| --- | --- |
| Persistence | Establishes whether a model beats “the next value equals the most recent value.” |
| Seasonal/periodic or moving-average rule, if physically appropriate | Tests whether regular dynamics explain the apparent benefit. |
| Simple autoregressive or linear model | Establishes whether a complex network adds predictive value. |

## Split and evaluation route

- Use chronological, non-overlapping train/validation/test blocks.
- Where possible, hold out an entire boiling run, device, heat-flux condition, or operating condition.
- Select hyperparameters without using final test evidence.
- Report MAE/RMSE by forecast horizon, not just one aggregate loss.
- Display forecasts with uncertainty or spread where justified, plus at least one failure case.
- Connect forecast error to a stated decision: monitoring, warning, control, or experiment planning.

## Promotion gate

The module may move to **Ready to assign** only when the data route, baseline scripts, seeded training path, expected runtime, held-out evaluation, instructor notes, and current assignment are verified together. A working legacy notebook alone does not meet this gate.
