# Data card: power-electronics thermal digital-twin studio

## Current release

No measured converter or semiconductor dataset is distributed in this folder. The only current runnable data route is the **simulated** lumped thermal-RC fixture in [Module VII](../../course_content/vii_time_series_forecasting/data_card_thermal_rc.md). It is rights-clear because it is generated from the disclosed equation and parameters.

## Intended measured-data schema

Any future release must define, at minimum:

| Field group | Examples | Required metadata |
| --- | --- | --- |
| Device and topology | Device family, module/package, converter topology | Device identifier, configuration, safe operating envelope, ownership/release permission |
| Electrical state | $V_{DS}$/$V_{CE}$, $V_{GS}$, $I_D$/$I_C$, switching command | Units, bandwidth, probe model, calibration, sampling clock, synchronization |
| Thermal state | Reference $T_j$, case/heat-sink/coolant temperatures | Sensor/estimation method, location, calibration, uncertainty, response time |
| Operating context | DC-link voltage, switching frequency, load, coolant/ambient state | Units, ranges, control mode, test sequence |
| Target and decision | Temperature estimate, fault label, thermal margin | Ground-truth construction, label provenance, decision threshold/consequence |

## Split and evaluation

The independent unit must be chosen before modeling. Prefer a holdout by device, campaign, thermal condition, power-cycle profile, or aging state. Do not randomly split overlapping waveform segments or allow a scaler/preprocessor to learn from the held-out condition. Report MAE/RMSE in temperature units, worst-case/near-limit error, latency, and failure modes.

## Privacy, safety, and intellectual-property boundary

Do not upload industrial traces, device serial numbers, unpublished measurements, student project data, unreleased source code, or safety-critical controller settings. A collaborator must approve technical accuracy and public release separately; possession on a lab drive is not permission to redistribute.
