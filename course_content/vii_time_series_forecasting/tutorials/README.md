# Tutorials and legacy PCA–LSTM / sequence-forecasting materials

## Current runnable tutorial

[`thermal_rc_forecasting.py`](thermal_rc_forecasting.py) generates a fully simulated, rights-clear teaching fixture for a lumped thermal system. It preserves units and time base, keeps whole runs separate, holds out a shifted thermal resistance/ambient condition, and reports persistence and training-only ARX baselines. Run:

<pre><code>python thermal_rc_forecasting.py</code></pre>

The generated CSV is local output only. It is illustrative simulation, not an experimental data release or a validated digital twin.

## Legacy materials

These files were moved from the prior Topic 5 option set without changing their scientific content. They provide an implementation reference for vapor-fraction forecasting from boiling-image sequences.

They are **not** the current validated tutorial. In particular, the legacy Python workflow creates overlapping sequence windows near its split boundary and uses training history for part of its architecture-length comparison. Follow the [refresh protocol](../REFRESH_PROTOCOL.md) before assigning or interpreting its results.

Contents:

- `vapor_fraction_Boiling-81_110W.txt`: legacy vapor-fraction time series;
- `tutorial_iv_seq2seq_regression_python.py` and notebook: historical implementation;
- `tutorial_iv_seq2seq_regression_matlab.mlx`: historical MATLAB implementation; and
- `tutorial_iv_seq2seq_regression_python_report.pdf`: historical exported report.
