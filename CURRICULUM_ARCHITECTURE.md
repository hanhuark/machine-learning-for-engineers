# Curriculum architecture, readiness review, and roadmap

## Review basis

This review evaluates the current modules as teaching materials for engineering applications. A module is considered ready for graded use only when its assignment states the engineering question, data/split requirements, baseline, evaluation, failure analysis, reproducibility expectations, and individual verification. A runnable notebook or polished model output alone is not sufficient.

## Decisions on the current modules

| Module | Decision | Current instructional status | Required evidence |
| --- | --- | --- | --- |
| I. Regression | Keep first; strengthen through the current assignment | Usable with instructor verification of external tutorial/data access | Time-aware split, baseline, residuals, feature-availability audit |
| II. Classification | Keep separate from segmentation | Usable with instructor verification of external tutorial/data access | Grouped split, robustness tests, deployment/abstention rule |
| III. Dimensionality reduction and clustering | Keep the pairing; add a current assignment | Current assignment added; legacy tutorial still needs local-path refresh | Train-only representation, reconstruction, stability, physical interpretation |
| IV. Segmentation and object detection | Keep separate from image classification | Current assignment added; local reproducible tutorial/data package remains a priority | Spatial/grouped split, mask/box metrics, visual error audit, measurement uncertainty |
| V. Reinforcement learning | Keep separate; do not merge with sequence modeling | Conceptual foundation only until a constrained engineering environment is released | Baseline controller, constraint audit, perturbed evaluation |
| VI. Generative models and inverse engineering design | Broaden the framing; do not assign yet | Under development | Data rights, non-generative baseline, held-out task metric, synthetic-data failure audit |
| VII. Time-series forecasting and prognostics | Retain as a distinct dynamics module | Validation refresh required before grading | Chronological/grouped split, persistence baseline, error by horizon, shifted-condition test |
| VIII. PINNs | Keep after supervised/core ML | Current controlled teaching module | Analytical and numerical baselines, inverse uncertainty, model-form failure analysis |
| IX. AI agent harnesses | Treat as a cross-cutting thread plus later lab | Current design/verification module | Access boundary, AI-use trace, independent check, individual defense |

## Recommended progression

The foundational order does **not** change: it moves from simple supervised prediction to increasingly structured image/physical-system questions. The change is to make the agent-harness material visible in Week 1 and assess it later, rather than treating it as a disconnected final topic.

| Phase | Modules | Purpose |
| --- | --- | --- |
| Orientation | Foundations + short IX orientation | Units, data provenance, splits, baseline-first reasoning, AI-use boundary |
| Core prediction | I. Regression; II. Classification | Targets, metrics, leakage, uncertainty, deployment consequences |
| Representation and measurement | III. Dimensionality reduction and clustering; IV. Segmentation and object detection | Structure discovery, labels, spatial outputs, visual measurement and failure audit |
| Advanced selection | VII. Time series **after refresh**; VIII. PINNs; V. RL as a conceptual/special-topic option | Dynamic systems, governing equations, and constrained decision-making |
| Capstone extensions | VI. Generative/inverse design **after release**; IX harness lab; final project | Design/augmentation credibility, controlled agent workflows, engineering decisions |

Do not make every advanced module compulsory in a one-semester offering. A defensible default is I–IV, VIII, and the IX orientation/lab, with one validated advanced option selected for the available time.

## Near-term curriculum roadmap

These are planned additions, not current graded modules.

1. **Multimodal AI for engineering sensing.** Fuse image/video, thermal, acoustic, vibration, and process data; require synchronization bounds, ablation, cross-condition tests, and a physical measurement target.
2. **Industrial time series, prognostics, and anomaly detection.** Extend VII from forecasting to maintenance-oriented decisions, false-alarm costs, missing data, drift, and condition-held-out evaluation.
3. **Digital twins, surrogates, and active learning.** Connect simulation, experiments, uncertainty, design-space coverage, and model updating; avoid calling a visualization a digital twin without calibrated predictive evidence.
4. **Embodied AI and sim-to-real engineering.** Begin with simulation and public-safe fixtures before hardware; assess perception, state estimation, safety constraints, and transfer gap rather than only task completion.
5. **Edge deployment and AI assurance.** Cover latency, data interfaces, fault handling, cybersecurity, human override, monitoring, and rollback for plants and products.

## Common non-negotiable requirements

Every current or future module should require an explicit engineering objective, variables and units, data provenance, an independent sampling/splitting unit, a simple baseline, meaningful held-out evaluation, failure analysis, evidence-bounded claims, and an individual check. The shared [assessment policy](teaching_resources/ASSESSMENT_AND_AI_POLICY.md) and [rubric](teaching_resources/ENGINEERING_ML_RUBRIC.md) are the common implementation mechanism.
