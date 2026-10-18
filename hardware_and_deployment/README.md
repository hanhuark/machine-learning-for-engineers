# Hardware and deployment pathways

Engineering AI becomes consequential when it touches measurements, simulations,
actuators, products, or plant decisions. This pathway connects the repository's
models and agent workflows to those settings without treating a successful demo
as evidence of safe deployment.

## Staged pathway

| Stage | Example | Required evidence before advancing |
| --- | --- | --- |
| Offline analysis | CFD surrogate or recorded sensor dataset | Data card, units, baseline, held-out evaluation, and failure audit |
| Replay and shadow mode | Historical/replayed signals or robot telemetry | Time-base alignment, latency estimate, missed/faulted-data behavior, and human review |
| Bounded demonstration | Classroom robot, sensor/DAQ fixture, or digital-twin interface | Safety boundary, operating procedure, stop condition, baseline controller/analysis, and instructor supervision |
| Deployment study | Product, plant, or research-system workflow | Calibration, uncertainty, cybersecurity, privacy/rights, monitoring, rollback, and owner approval |

## Priority directions

- **Multimodal sensing:** synchronize images/video with thermal, acoustic,
  vibration, electrical, or process signals; document clocks, sampling rates,
  missingness, and sensor uncertainty.
- **Simulation and digital twins:** distinguish a visualization, a surrogate,
  and a calibrated predictive digital twin; state the evidence required for
  each claim.
- **Embodied AI:** compare learned policies with a baseline controller; assess
  safety constraints and sim-to-real differences before task performance.
- **Industrial assurance:** include latency, data interfaces, fault handling,
  human override, monitoring, and rollback as engineering requirements.

The [cold-plate surrogate studio](../case_studies/ned3_coldplate_surrogate/)
is the current simulation-based starting point. Hardware-connected releases
require separate equipment, safety, access, and data-governance approval.
