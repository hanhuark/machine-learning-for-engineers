# Power-electronics thermal digital-twin studio

> **Status: design stage.** This studio provides a literature-grounded teaching specification and uses the simulated thermal-RC core in Module VII. It does **not** distribute device waveforms, assert validation on a physical converter, or make a public reliability claim.

## Engineering decision

Estimate a power-semiconductor thermal state, such as junction temperature $T_j$, from a stated measurement set and operating history, then decide whether the estimate is adequate for a bounded monitoring action. This is an engineering inference problem, not an image of an "AI twin."

The initial learning route is the [Module VII thermal-RC fixture](../../course_content/vii_time_series_forecasting/): a known heat-load input $P$ drives a lumped temperature state $T$ through

$$
C\frac{dT}{dt}=P-\frac{T-T_a}{R}.
$$

It is deliberately simple and simulated. A later device-specific case may use electrical waveforms, temperature-sensitive electrical parameters, heat-sink/coolant measurements, or controlled thermal measurements only after the source, calibration, safety envelope, and redistribution rights are documented.

## What students should learn

1. Separate a temperature estimate from a digital-twin claim. An offline fitted predictor is not automatically a synchronized, decision-relevant twin.
2. Retain physical quantities and units: electrical input/loss in W, temperature in $^\circ$C or K, resistance in K/W, capacitance in J/K, and time in s.
3. Compare a transparent thermal-resistance/RC or threshold baseline against a learned estimator.
4. Hold out a meaningful condition: device, power cycle, ambient/coolant condition, switching regime, aging state, or test campaign—not adjacent overlapping windows.
5. Report the error and the safety consequence of error. A low average MAE can still be unsuitable near a thermal limit or during a fast transient.

## Evidence ladder for this studio

This is a proposed teaching taxonomy, not a universal standard.

| Level | Minimum evidence | Claim that is justified |
| --- | --- | --- |
| 0. Transparent simulation | Stated equation, parameters, numerical checks | A learner can inspect a model and forecasting workflow. |
| 1. Calibrated estimator | Traceable measurements, calibration, held-out device/condition | A model estimates a defined measured target in its stated envelope. |
| 2. Monitored digital shadow | Time-aligned incoming data, latency and failure handling | A virtual representation is updated from the physical system for monitoring. |
| 3. Decision-capable digital twin | Validated state estimate, uncertainty/limits, bounded action and verification | The coupled representation supports a defined monitoring or control decision. |

Students must state the highest level supported by their evidence rather than selecting the word "twin" for a visually compelling dashboard.

## Current exercise

Use the [AI-resilient forecasting assignment](../../course_content/vii_time_series_forecasting/ASSIGNMENT_AI_RESILIENT.md), then reframe its simulated state as a converter thermal-management analogue. The required physical limits are: (i) with $P=0$ and $T>T_a$, the temperature must decay toward $T_a$; and (ii) at constant $P$, the ideal steady-state rise is $T-T_a=PR$.

The [data card](data_card.md) gives the release boundary. The [literature map](LITERATURE_MAP.md) provides reading and the engineering logic behind the studio. For a physics-based comparison, run the [lumped-thermal baseline](tutorials/) and complete the [studio extension](ASSIGNMENT_EXTENSION.md).

## What is required before a hardware/data release

- a faculty technical co-lead and a specific decision, such as over-temperature warning or parameter drift monitoring;
- a rights-cleared dataset or reproducible simulation, with device topology, sensor locations, calibration, time synchronization, operating envelope, and units;
- a safe operating plan and an explicit rule that students cannot alter live converter hardware without supervision;
- a baseline such as a thermal impedance/RC observer, calibrated temperature-sensitive parameter, or established threshold;
- an independent device/condition/time split and a safety-relevant error analysis; and
- an instructor-held transfer test that changes a condition or fault hypothesis.

## Sources and boundaries

The [annotated literature map](LITERATURE_MAP.md) links reviews and primary examples. It distinguishes review-level conclusions from individual demonstrations. The studio does not reproduce figures, tables, code, or data from those works.
