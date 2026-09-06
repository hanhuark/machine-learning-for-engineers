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
