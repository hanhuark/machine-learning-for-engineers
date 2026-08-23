# Current assignment: regression, forecasting, and evidence

This version supplements the legacy Homework 1 PDF/DOCX. Use it for future offerings after the instructor supplies dates, submission logistics, and a private evaluation set.

## Engineering question

Build and assess models for Razorback football win margin while distinguishing two different tasks:

1. **Pregame forecast:** use only features known before kickoff.
2. **Postgame explanation:** use game statistics to explain the observed margin, but do not call this a forecast.

Your report must include a feature-availability table. For every candidate feature, state when it is available and whether it is permissible for each task.

## Required workflow

1. Inspect the data, units/definitions, missing values, and seasons represented.
2. Create a chronological train/validation/test split. Do not randomly mix future games into the training period for a forecasting claim.
3. Establish a simple baseline before complex models.
4. Train at least two model families, including one interpretable baseline. Document hyperparameters, seed, and compute time.
5. Report MAE and one additional justified regression metric on the held-out set; include uncertainty or bootstrap intervals if feasible.
6. Plot predictions, residuals, and the three largest-error cases. Explain likely causes without claiming causality from correlation alone.
7. Complete an instructor-held evaluation after submitting the initial pipeline.

## Required reasoning and AI audit

- Identify at least three leakage-prone features or transformations.
- Defend one included feature and one excluded feature.
- Explain whether the goal is prediction, explanation, or both.
- Use the [AI-use record](../../teaching_resources/AI_USE_TEMPLATE.md) if generative AI is permitted.
- Test one AI-proposed improvement against held-out error and computational cost; do not credit it based only on training loss.

## Submission

```text
lastname_firstname_regression/
  README.md
  environment.yml or requirements.txt
  analysis.py or analysis.ipynb
  AI_USE.md
  results/
    metrics.json
    figures/
```

Grade with the [shared rubric](../../teaching_resources/ENGINEERING_ML_RUBRIC.md). A short individual check may ask you to classify a feature as pregame/postgame, explain a residual, or modify the split.
