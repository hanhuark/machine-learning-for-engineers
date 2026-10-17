# Data card for NED3 multimodal boiling-signals studio

## Identity and rights

- Dataset family: BoilingBench-Multimodal Lite candidate tracks.
- Provider: NED3 Laboratory and source-record contributors.
- Evidence class: measured sensor/video signals, plus derived thermal and signal products.
- Access boundary: rights audit required for each chosen raw, processed, annotated, and model artifact.
- Course release rule: publish only a documented feature-table subset or a download script after the audit; never assume tool-code licenses apply to data.

## Engineering context and evaluation

- Record sensor, sampling rate, physical units, time reference, synchronization basis, target status, processing version, and quality flag for every lesson row.
- Split by independent run or physical condition before creating windows; adjacent windows, duplicate processed copies, and cached waveform segments must not cross partitions.
- Compare persistence/mean and transparent feature-based baselines with any recurrent or multimodal model.
- Report error by held-out run/condition and explain uncertainty, calibration limitations, and domain shift.

## Prohibited claims

- Do not call processed thermal reconstructions direct measurements.
- Do not infer causal sensor coupling from archived clock offsets alone.
- Do not use a random-window score as evidence of cross-run or cross-facility generalization.
