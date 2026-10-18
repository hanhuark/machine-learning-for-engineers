# Data card: simulated thermal-RC forecasting fixture

## Purpose and evidence status

This fixture teaches chronological evaluation, known-input forecasting, and transfer limits using a generated lumped thermal system. Every row is **simulated**. It is not experimental data, a release of NED3 data, a device characterization, or validation of a digital twin.

## System boundary and equations

The system has one temperature state $T$ and a prescribed heat-load input $P$:

$$
C\frac{dT}{dt}=P-\frac{T-T_a}{R}.
$$

The script advances the state with a forward-Euler step. The modeled boundary ends at a lumped thermal resistance to a fixed ambient environment; it omits spatial gradients, electrical switching loss physics, sensor noise, controller action, aging, and uncertainty in $R$ and $C$.

## Schema and units

| Field | Meaning | Unit |
| --- | --- | --- |
| `run_id` | Independent simulated operating run | — |
| `time_s` | Sample time | s |
| `power_W` | Prescribed heat load | W |
| `temperature_C` | Lumped temperature state | $^\circ$C |
| `ambient_temperature_C` | Fixed ambient temperature for that run | $^\circ$C |
| `thermal_resistance_K_per_W` | Lumped resistance to ambient | K/W |
| `thermal_capacitance_J_per_K` | Lumped thermal capacitance | J/K |

The default sampling interval is 0.1 s for 60 s. The nominal train run uses $R=0.50$ K/W and $T_a=25^\circ$C. The test run changes to $R=0.65$ K/W and $T_a=30^\circ$C.

## Split and permitted use

Keep full runs separate: nominal run for training, shifted-resistance run for validation, and shifted-resistance-plus-ambient run for the final test. Do not randomly split overlapping windows. Fit scalers, feature choices, and model settings from training/validation evidence only.

Learners may modify the simulation to test hypotheses, but must label all modified results as simulated. They must not claim device, converter, or semiconductor performance from this fixture.

## Known limitations and next evidence

The fixture intentionally makes the governing balance simple enough to inspect. A measured-data extension must identify the device and sensor boundary, calibration, sampling clock, operating envelope, independent unit for the held-out split, data rights, baseline observer/correlation, and uncertainty before it can replace this fixture in a graded case.
