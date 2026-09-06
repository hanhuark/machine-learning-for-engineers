# Priority Research Growth Area studio roadmap

## Purpose

The curriculum will expand through a common engineering-ML core and discipline-led studios. This is a proposed roadmap, not an official College of Engineering curriculum or a record of confirmed collaborations.

## Proposed initial studios

| Priority Research Growth Area | Example engineering decision | Suitable modules | Minimum credible baseline | Required resource before release |
| --- | --- | --- | --- | --- |
| Materials, Semiconductors & Power Electronics | Predict thermal state, fault class, or reliability risk from waveform, temperature, and operating features. | I, II, VII, VIII | Thermal-resistance/first-principles estimate, threshold rule, or established diagnostic indicator. | Faculty co-lead; rights-cleared data or simulation; variables/units; safe operating envelope. |
| Food Systems & Nutrition | Classify or quantify a visible/process condition for food production, quality, or agricultural sensing. | II, IV, VII | Human/threshold inspection protocol or simple image-feature classifier. | Faculty co-lead; annotation protocol; redistribution permission; representative held-out farm/lot/condition split. |
| Metabolic Health | Estimate a bounded physiological or imaging-derived endpoint while communicating uncertainty and privacy limits. | I, II, III, VIII | Clinical/physical reference calculation or simple interpretable model. | Biomedical/health collaborator; de-identified public or synthetic data; ethics/privacy review; clinically meaningful metric. |
| Supply Chain and Contested Logistics | Forecast disruption-sensitive demand or identify an operational anomaly under constrained decisions. | I, III, V, VII | Persistence forecast, rule-based alert, or transparent optimization heuristic. | Industrial engineering/logistics co-lead; public/synthetic scenario data; explicit decision objective and consequence model. |
| Lithium & Critical Minerals | Predict separation/recovery performance or prioritize experiments under process constraints. | I, III, VI, VIII | Mass-balance, equilibrium/correlation, or response-surface baseline. | Chemical engineering co-lead; rights-cleared experiment/simulation data; process conditions, units, and validity range. |

## Studio acceptance criteria

A case is ready to learn only when it supplies:

1. a concrete decision, system boundary, variables, units, and validity range;
2. a data card with source, rights, independent unit, schema, and limitations;
3. a documented simple baseline;
4. a split rule that prevents leakage across the meaningful unit, such as device, production lot, patient, site, experiment, or time period;
5. held-out evaluation and at least one known failure mode;
6. a reproducible Python route and expected runtime; and
7. a transfer or individual-defense prompt that tests engineering reasoning rather than code authorship.

## Collaboration intake

For each prospective studio contributor, request:

- the decision the learner should support, not merely a data file;
- a shareable or reproducible synthetic/simulation alternative if raw data cannot be released;
- variable definitions, units, sensor/process context, and known confounders;
- a credible baseline a student can implement and inspect;
- a recommended held-out condition and likely failure mode; and
- review of technical accuracy before public release.

## Expansion beyond the five priorities

Additional mechanical, civil, environmental, aerospace, and manufacturing studios remain welcome if they satisfy the same acceptance criteria. They should extend the shared core rather than duplicate it.
