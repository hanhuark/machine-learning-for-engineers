# Studio extension: identify and challenge a thermal-state model

## Purpose

Use the simulated thermal-RC fixture to distinguish a physics-based state estimate from a broad digital-twin claim. This extension follows Module VII and is suitable for a short studio activity or an oral-defense prompt.

## Required work

1. Run [`thermal_twin_baseline.py`](tutorials/thermal_twin_baseline.py). Derive why the regression estimates $1/C$ and $1/(RC)$ from the forward-Euler temperature update.
2. Report fitted $R$ (K/W) and $C$ (J/K), the calibration-run boundary, the test-run boundary, and held-out MAE ($^\circ$C).
3. Before changing code, predict what happens if the test ambient temperature or resistance changes further. Run one declared change, report the result, and explain the direction of the error from the energy balance.
4. Compare the parameter-identified model with the Module VII persistence and ARX baselines. State one reason a physically structured baseline could be preferable and one reason it could fail.
5. Classify the result using the [studio evidence ladder](README.md#evidence-ladder-for-this-studio). Justify why it does not reach a calibrated-hardware or decision-capable digital-twin claim.

## Individual check

Be prepared to explain the two limiting cases:

$$
P=0,\;T>T_a \Rightarrow T\ \text{decays toward}\ T_a,
$$

and, under constant power at steady state,

$$
T-T_a=PR.
$$

The instructor may change a resistance, ambient condition, or time step and ask the learner to predict the qualitative effect before rerunning the code.

## What a measured-data upgrade would require

The same model could become a useful device-specific baseline only after measuring or defining a temperature reference, device/system boundary, loss input, sensor calibration, sampling synchronization, operating envelope, independent holdout, and uncertainty. A lower MAE alone is not sufficient.
