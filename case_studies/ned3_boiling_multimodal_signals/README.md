# NED3 multimodal boiling-signals studio

> **Status: rights audit required; proposed teaching package.** The course must
> use a small, track-specific, rights-cleared subset rather than copying a
> multimodal source archive.

## Engineering decision

Estimate a clearly defined thermal quantity or identify a documented operating
state using sensor signals while distinguishing raw measurements from values
derived through thermal reconstruction and signal processing.

| Item | Current scope |
| --- | --- |
| System boundary | Documented pool-boiling or immersion-cooling track and its stated sensor/time-base conditions. |
| Evidence class | Measured sensor/video signals plus derived heat-transfer and signal features. |
| Baseline | Persistence/mean prediction and a linear or feature-based model before sequence networks. |
| Evaluation | Hold out complete runs, heat-load paths, surfaces, fluids, or pressure conditions as applicable. |
| Failure boundary | A derived heat-flux label is not automatically calibrated ground truth; clock alignment does not prove common-trigger synchronization. |

## Intended learning use

This studio is the primary future case for feature engineering, leakage-safe
time series, and multimodal reasoning in Modules I, III, and VII. The initial
public lesson should use a compact, documented feature table with run-level
identifiers—not raw waveforms, videos, annotations, or checkpoints.

[BoilingLab](https://github.com/UARK-NED3/BoilingLab) provides the relevant
processing context. Before release, audit each selected track's raw/derived
status, license, source record, calibration evidence, synchronization basis,
and data-reduction assumptions.

See [data_card.md](data_card.md) and the [course-data registry](../../course_data/).
