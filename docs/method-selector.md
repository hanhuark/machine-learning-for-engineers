---
layout: default
title: Engineering AI Method Selector
---

# Engineering AI method selector

Choose a method only after stating the engineering question, evidence available, and decision consequence. This page is a routing aid, not a model-recommendation engine.

| If the engineering task is… | Start with… | Then verify… | Current route |
| --- | --- | --- | --- |
| Estimate a continuous quantity | Regression and a physically meaningful baseline | Units, residuals, operating-range coverage, and held-out error | [Module I](../course_content/i_regression/) |
| Sort images, signals, or records into categories | Classification and a transparent threshold/rule baseline | Group/site/device split, class imbalance, false-alarm cost, and confusing cases | [Module II](../course_content/ii_classification/) |
| Find structure without a supplied label | PCA/SVD or clustering | Train-only representation, reconstruction, stability, and physical interpretation | [Module III](../course_content/iii_dimensionality_reduction_and_clustering/) |
| Locate or measure regions/objects in imagery | Segmentation or object detection | Spatial labels, condition-held-out performance, visual errors, and measurement uncertainty | [Module IV](../course_content/iv_segmentation_and_object_detection/) |
| Choose actions over time | A baseline controller before reinforcement learning | State/action units, safety constraints, reward design, perturbations, and sim-to-real gap | [Module V](../course_content/v_reinforcement_learning/) |
| Create synthetic samples or propose candidates | Constraint screen and non-generative comparison | Provenance, novelty/memorization, task utility, physical feasibility, and fabrication limits | [Module VI](../course_content/vi_generative_models/) |
| Forecast a dynamic signal or detect degradation | Persistence/AR baseline before a sequence model | Chronological split, horizon-dependent error, drift, missingness, and decision cost | [Module VII](../course_content/vii_time_series_forecasting/) |
| Combine governing equations with data | Analytical/numerical solution before a PINN | Boundary/initial conditions, residuals, inverse uncertainty, and model-form error | [Module VIII](../course_content/viii_physics_informed_neural_networks/) |
| Delegate a bounded workflow to an AI agent | Written workflow/specification before tool access | Permissions, provenance, tool-output checks, acceptance tests, and human responsibility | [Module IX](../course_content/ix_ai_agent_harnesses/) |

If the problem does not have a defensible target, baseline, data/right-to-use statement, or validation route, do not select a more complex model. Reframe the engineering question first.

For discipline-specific examples, use the [application-studio roadmap](../case_studies/PRIORITY_STUDIO_ROADMAP.md).
