# Data card for NED3 BoilingBench CV studio

## Identity and rights

- Dataset name/version: BoilingBench-CV; public card accessed 2026-10-17 and local release record `0.1.0-internal` reviewed 2026-10-17.
- Provider: NED3 Laboratory and documented source-record contributors.
- Evidence class: measured images plus human annotations and derived benchmark metadata.
- Reported license: CC BY 4.0 on the public card; release reconciliation remains required.
- Access boundary: no image, annotation, model, or source-video payload is included in this repository.

## Engineering context and evaluation

- Target: two-dimensional bubble instance masks and per-frame morphometry.
- Domain factors: fluid, surface, regime, image geometry, optical arrangement, facility, and source sequence may co-vary.
- Split rule: group frames by source video/power condition; use supplied grouped partitions when the canonical payload is confirmed.
- Baselines: thresholding or another documented non-neural image method before transfer learning.
- Metrics: mask/instance metrics plus per-regime visual error audit; do not report only a pooled score.

## Prohibited claims

- Do not call the image-plane metric a volumetric void fraction.
- Do not interpret water-to-HFE transfer as a fluid-only causal effect.
- Do not use random near-duplicate frame splits as independent generalization evidence.
