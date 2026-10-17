# Data card for NED3 cold plate surrogate studio

## Identity and rights

- Dataset name/version: Cold Plate CFD 2000 simulations; Hugging Face revision `58911fc77390a70a6c71da0612e02b4976976283` verified 2026-10-17.
- Provider and stable URL/DOI: NED3 Laboratory; [Hugging Face dataset card](https://huggingface.co/datasets/UARK-NED3/ColdPlate-CFD-2000sims); [Dryad DOI](https://doi.org/10.5061/dryad.k0p2ngfp5).
- Evidence class: simulated.
- License: CC0 1.0 according to the source card; retain the source citation.
- Access boundary: download from the canonical source; no archive copy is included here.

## Engineering context

- System: steady liquid-cooled dual-chip pin-fin cold plate modeled with coupled flow and energy equations in CFD.
- Independent unit: one CFD simulation / DOE condition.
- Validity: limited to the released geometry, boundary-condition space, model assumptions, and steady regime.
- Prohibited interpretation: experimental validation, transient prediction, pressure-drop prediction with an unstated unit, or geometry extrapolation.

## Schema and evaluation

- Inputs: six source-defined boundary conditions. The tutorial uses the source
  workflow's SI interpretation—heat flux (W/m²), mass flow (kg/s), and inlet
  temperature (K)—and the released source code's chip area (0.0016 m²). The
  original Fluent case is not redistributed, so verify this convention against
  the source record before changing the analysis or assigning it.
- Targets: temperature fields in K and selected scalar temperature reports. The `pdrop_*` export names require separate unit recovery.
- Split rule: preserve a fixed simulation-level split; never fit scalers/POD modes using held-out simulations.
- Baselines: a mixed-outlet energy balance with training-fitted effective heat
  capacity, then linear regression, then POD-NN. The fitted effective heat
  capacity is not a measured property.
- Metrics: temperature RMSE/MAE and maximum absolute error on held-out simulations, reported with the physical operating range.

## Known limitations

- The public release does not record a pressure unit for the `pdrop_*` channels.
- A surrogate's speed and interpolation accuracy do not establish CFD-model or hardware validity.
- The published environment is not fully version-pinned; the course package must pin its own environment before it is labeled ready to learn.
