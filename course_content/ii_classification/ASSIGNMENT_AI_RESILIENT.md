# Current assignment: nuts-and-bolts classification as a deployed vision system

This version supplements the legacy Homework 2 PDF/DOCX. Use it for future offerings after the instructor supplies dates, robot access, and a private deployment set.

## Engineering question

Develop and evaluate a vision model for sorting nuts and bolts. The central question is not only whether a CNN trains, but whether its decisions remain reliable when lighting, orientation, scale, surface finish, blur, or background differ from the training images.

## Required workflow

1. Document image provenance, grayscale conversion, resizing to `(300, 300, 1)`, class definitions, and augmentation policy.
2. Split by source image/object/session before augmentation. Augmented versions of one source image must not be split across train, validation, and test sets.
3. Establish a non-neural baseline or a deliberately simple reference model.
4. Train a CNN compatible with the sorting-robot interface. Record framework version, seed, architecture, training time, and threshold.
5. Report confusion matrix, accuracy, precision, recall, F1, ROC/AUC, and class-specific errors on a reserved test set.
6. Evaluate controlled robustness changes: at minimum brightness, rotation, blur, and partial occlusion. Report the test design and results.
7. Inspect and annotate at least ten failure or low-confidence cases.
8. Define an abstention/inspection rule for low-confidence predictions and test it on the instructor-held deployment images.

## Deployment and reasoning evidence

- Measure actual sorting success rate if the robot is used; report the number of trials and a binomial confidence interval.
- Explain the engineering consequence of a false nut-versus-bolt prediction.
- During a short individual check, predict a likely failure mode, inspect an unfamiliar image, or modify the decision threshold.
- Use the [AI-use record](../../teaching_resources/AI_USE_TEMPLATE.md) if generative AI is permitted. Verify one AI-generated suggestion with an independent test, not only training accuracy.

## Submission

```text
lastname_firstname_classification/
  README.md
  environment.yml or requirements.txt
  train.py or train.ipynb
  AI_USE.md
  results/
    metrics.json
    figures/
    failure_audit.md
```

Grade with the [shared rubric](../../teaching_resources/ENGINEERING_ML_RUBRIC.md). Keep held-out deployment images and model-answer material outside the public repository.
