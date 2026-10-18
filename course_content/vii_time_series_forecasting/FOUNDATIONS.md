# Foundations: time-series forecasting and prognostics

Forecasting uses the order of observations as information. This guide explains the baseline forecasting problem; it does not validate the legacy sequence-to-sequence tutorial for graded use.

## 1. Define the signal and clock

Let $y_k$ be a physical observable sampled at time $t_k$, with sampling interval $\Delta t=t_{k+1}-t_k$. In the legacy boiling record, vapor fraction is dimensionless and the nominal sampling frequency is 3,000 Hz, so $\Delta t\approx0.33$ ms. State whether timestamps are measured or assumed, whether samples are equally spaced, and how missing frames are handled.

Using a history window of $w$ samples, a direct multi-step forecasting task is

$$
\hat{\mathbf{y}}_{k+1:k+h}
= f_{\theta}\left(
y_{k-w+1:k},\,
\mathbf{u}_{k-w+1:k}
\right),
$$

where $h$ is the forecast horizon in samples and $\mathbf{u}$ is an optional vector of known inputs or operating conditions. A forecast horizon must be converted to time: $h\Delta t$.

## 2. Start with an honest baseline

The persistence baseline assumes the next value remains equal to the last observed value:

$$
\hat{y}_{k+\ell}^{\mathrm{pers}} = y_k,
\qquad \ell=1,\ldots,h.
$$

On held-out values, report error in the same unit as the target:

$$
\mathrm{MAE}(h) =
\frac{1}{n_h}\sum_{i=1}^{n_h}
\left|y_{i,h}-\hat{y}_{i,h}\right|.
$$

For vapor fraction, MAE is dimensionless. A model must beat a relevant baseline at the stated horizon and condition before its added complexity is useful.

## 3. Worked representative case

Run the chronological-split example:

<pre><code>python ../short_code_demos/time_series.py</code></pre>

The code holds out the last three values and forecasts each with the final training value. This protects time ordering; it does not validate a real deployment. Change the horizon, then explain why error normally needs to be reported separately by forecast lead time.

## 4. Split design

Use a chronological training block, a later validation block, and a final test block. When data include several experiments, hold out entire runs or operating conditions whenever possible. Fit normalization, feature selection, and hyperparameter choices using training/validation information only. A random split of overlapping windows leaks future-adjacent information into training.

## 5. Forecasting versus prognostics

Forecasting estimates a future signal. Prognostics additionally supports a maintenance or risk decision, such as remaining useful life, anomaly alarm, or intervention timing. A prognostics claim needs an outcome definition, decision threshold, lead-time requirement, cost of false alarms/missed alarms, and evidence across equipment or conditions.

## Failure checks

- **Future leakage:** A shuffled split or scaler uses information from the final test period.
- **Overlap leakage:** Nearly identical windows from the same time region appear in training and testing.
- **Horizon mismatch:** A one-step model is reported as evidence for a long-horizon decision.
- **Regime change:** Heat flux, flow condition, sensor placement, or process state shifts from the training regime.
- **Autocorrelation illusion:** A persistence baseline looks strong because the signal changes slowly.
- **Unit/time-base error:** A learner confuses samples, ms, s, or a nondimensional signal with a dimensional one.

## Transfer task

Choose a sensor signal from thermal management, manufacturing, food processing, logistics, or energy systems. Specify the observable and unit, $\Delta t$, window length, forecast horizon in both samples and time, the persistence baseline, a split rule, and one shifted test condition.
