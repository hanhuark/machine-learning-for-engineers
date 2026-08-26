---
layout: default
title: Machine Learning for Engineers
---

# Machine Learning for Engineers

## Project-based AI for physical systems

An open curriculum for students and instructors who want to do more than run a model: define a physical question, build a defensible baseline, test on meaningful held-out conditions, inspect failure cases, and explain what the result means for an engineering decision.

> **Originating implementation:** MEEG 54403: Machine Learning for Mechanical Engineers at the University of Arkansas. The course is ongoing, and this repository is designed for adaptation by other engineering programs.

## Choose your path

| I am a… | Start here |
| --- | --- |
| Student learning a method | Read the [course map](../COURSE_MAP.md), then select a module and complete its tutorial before attempting the assignment. |
| Instructor adopting one module | Use the [adoption guide](../ADOPTION_GUIDE.md) and the [instructor guide](../INSTRUCTOR_GUIDE.md). |
| Instructor designing AI-resilient assessment | Start with the [assessment and AI policy](../teaching_resources/ASSESSMENT_AND_AI_POLICY.md) and shared [engineering-ML rubric](../teaching_resources/ENGINEERING_ML_RUBRIC.md). |
| Contributor | Read the [contributing guide](../CONTRIBUTING.md), especially the data-rights and student-information boundaries. |

Confirmed course implementations and adaptations are listed in [IMPLEMENTATIONS.md](../IMPLEMENTATIONS.md).

## What makes this different

- **Engineering question first.** Every module connects algorithms to a measurable physical system, variables, units, assumptions, and a decision.
- **Verification before claims.** Students compare against analytical, numerical, or simple empirical baselines and distinguish implementation from validation.
- **Failure analysis is required.** Leakage, domain shift, model-form error, label quality, uncertainty, and visibly wrong predictions are part of the work.
- **AI is a tool, not evidence of learning.** Students may use generative AI only under documented conditions and must verify, explain, and modify their work independently.
- **Reusable by design.** Python is the primary reproducible pathway; modules may be adopted independently with clear provenance and licensing expectations.

## Explore the six modules

1. [Regression](../course_content/i_regression/): continuous engineering outcomes, baselines, residuals, and split design.
2. [Classification](../course_content/ii_classification/): image classification, grouped splits, and deployment constraints.
3. [Dimensionality reduction and clustering](../course_content/iii_dimensionality_reduction_and_clustering/): structure discovery in boiling images.
4. [Segmentation and object detection](../course_content/iv_segmentation_and_object_detection/): visual labels, transfer learning, and error audits.
5. [Reinforcement learning](../course_content/v_reinforcement_learning/): bounded sequential decisions and policy evaluation.
6. [Generative models](../course_content/vi_generative_models/): engineering synthetic data and credibility checks (**under development**).
7. [Time-series forecasting](../course_content/vii_time_series_forecasting/): boiling dynamics and sequence-to-sequence forecasting (**validation refresh required**).
8. [Physics-informed neural networks](../course_content/viii_physics_informed_neural_networks/): transient heat conduction, inverse problems, and model-form error.

## Evidence and reuse

The repository includes [student project examples](../project_examples/), a reusable [data-card template](../teaching_resources/DATA_CARD_TEMPLATE.md), and a [reproducibility checklist](../teaching_resources/REPRODUCIBILITY_CHECKLIST.md). Related educational publications and project outcomes are listed in the [main README](../README.md#related-publications-and-project-outcomes).

Please cite the curriculum using its [citation metadata](../CITATION.cff), preserve attribution and the BSD 3-Clause license, and do not upload student records, private assessment material, or restricted data.
