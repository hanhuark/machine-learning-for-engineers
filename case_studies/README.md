# Engineering application studios

This directory is the expansion mechanism for the curriculum. It does **not** create separate machine-learning courses by discipline. Instead, it pairs a shared engineering-ML core with compact, discipline-led application studios that preserve common expectations for variables, units, provenance, baselines, held-out evaluation, and failure analysis.

The five initial studio directions align with the University of Arkansas College of Engineering Priority Research Growth Areas supplied to the course team:

1. Materials, Semiconductors & Power Electronics
2. Food Systems & Nutrition
3. Metabolic Health
4. Supply Chain and Contested Logistics
5. Lithium & Critical Minerals

The directions below are **proposed**. They do not indicate an official College program, a confirmed partnership, or availability of a dataset. A studio becomes publishable or assignable only after its contributor confirms the engineering question, data rights, baseline, split logic, and limitations.

## Start a studio

Copy the materials in [_case_template](_case_template/) and complete every applicable section before publishing. The [priority-studio roadmap](PRIORITY_STUDIO_ROADMAP.md) explains the initial targets and what remains needed.

## NED3 data-backed studio candidates

The following records connect the shared ML core to NED3 resources without
copying raw research payloads into this repository. Each row states its own
release status; do not treat a proposed studio as ready simply because another
studio has completed its release checks.

| Candidate | Shared methods | Current boundary |
| --- | --- | --- |
| [Cold plate surrogate](ned3_coldplate_surrogate/) | Regression, PCA/POD, surrogate modeling | **Ready to assign:** public simulated source, pinned checksummed subset, runnable baselines, and an instructor-held individual check. |
| [BoilingBench CV](ned3_boilingbench_cv/) | Vision, segmentation, domain shift | Public/local release records need reconciliation before a course download is released. |
| [Multimodal boiling signals](ned3_boiling_multimodal_signals/) | Features, time series, multimodal reasoning | Track-specific rights audit and a lightweight feature table are required. |
| [Flow-boiling evidence audit](ned3_flow_boiling_evidence_audit/) | Segmentation critique, time-base audit, AI verification | Public source; designed first as an evidence-quality exercise, not a general benchmark. |
| [Power-electronics thermal digital-twin studio](power_electronics_thermal_digital_twin/) | Time series, regression, monitoring, hybrid modeling | **Design stage:** a simulated thermal-RC core is available through Module VII; a device-data release needs collaborator and rights review. |

See the [course-data registry](../course_data/) for canonical source links,
licenses, access boundaries, and status labels.

## Shared core, different context

| Shared method | Example studio use |
| --- | --- |
| Regression | Predict an engineering response from measurable features; compare against a mechanism-informed baseline. |
| Classification/vision | Inspect product, material, organism, or infrastructure conditions using defined labels and a condition-held-out split. |
| Representation learning | Identify structure, operating regimes, or anomaly candidates without confusing clusters with physical mechanisms. |
| Time series | Forecast or detect changes while respecting chronology, drift, missing data, and decision costs. |
| PINNs/surrogates | Combine governing equations with measurements only when analytical or numerical comparison is available. |
| RL/embodied AI | Make bounded sequential decisions under explicit safety, actuator, and transfer constraints. |

## Public-release boundary

Do not put restricted industrial data, protected health information, student work, unpublished research, proprietary code, answer keys, or instructor-held tests here. Public cases should use rights-cleared measured data, a documented simulation, or transparently synthetic data. See the [data-card template](../teaching_resources/DATA_CARD_TEMPLATE.md) and [reproducibility checklist](../teaching_resources/REPRODUCIBILITY_CHECKLIST.md).
