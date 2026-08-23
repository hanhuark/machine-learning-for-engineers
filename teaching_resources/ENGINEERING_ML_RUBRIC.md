# Shared engineering machine-learning rubric

Adapt weights to the module. A high score requires evidence, not only a working model.

| Dimension | Suggested weight | Evidence expected |
| --- | ---: | --- |
| Problem formulation and engineering context | 15% | Objective, variables, units, assumptions, decision context |
| Data provenance and split validity | 20% | Source, preprocessing, independent unit, leakage analysis |
| Baseline and model design | 15% | Justified baseline, chosen models, reproducible configuration |
| Evaluation and failure analysis | 20% | Meaningful metrics, held-out conditions, uncertainty/sensitivity, visual failures |
| Physical interpretation and limitations | 10% | Mechanism, validity range, what cannot be concluded |
| Reproducibility and communication | 10% | Clear entry point, environment, figures, traceable outputs |
| Individual verification and responsible AI use | 10% | Explanation/modification ability and AI-use audit when applicable |

## Performance anchors

- **Excellent:** independent evidence supports the stated bounded claim; assumptions, units, failure modes, and limitations are explicit.
- **Adequate:** implementation works and the main evaluation is valid, but interpretation, sensitivity, or reproducibility is incomplete.
- **Insufficient:** relies on a training metric, random leakage-prone split, untraceable artifact, or unsupported engineering claim.
