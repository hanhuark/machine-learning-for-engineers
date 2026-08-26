# Legacy PCA–LSTM / sequence-forecasting materials

These files were moved from the prior Topic 5 option set without changing their scientific content. They provide an implementation reference for vapor-fraction forecasting from boiling-image sequences.

They are **not** the current validated tutorial. In particular, the legacy Python workflow creates overlapping sequence windows near its split boundary and uses training history for part of its architecture-length comparison. Follow the [module refresh requirements](../README.md#required-refresh-before-assessment-use) before assigning or interpreting its results.

Contents:

- `vapor_fraction_Boiling-81_110W.txt`: legacy vapor-fraction time series;
- `tutorial_iv_seq2seq_regression_python.py` and notebook: historical implementation;
- `tutorial_iv_seq2seq_regression_matlab.mlx`: historical MATLAB implementation; and
- `tutorial_iv_seq2seq_regression_python_report.pdf`: historical exported report.
