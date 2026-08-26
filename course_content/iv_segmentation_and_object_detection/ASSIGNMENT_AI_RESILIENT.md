# Current assignment: visual measurement for an engineering decision

This specification supplements the legacy Homework 4 PDF/DOCX. Use it after the instructor confirms data rights, a reproducible environment, and a private evaluation set or condition.

## Engineering question

Can a segmentation or object-detection model provide a reliable visual measurement for a stated engineering decision under changed imaging and operating conditions?

Choose one defined task:

- **Segmentation:** estimate a spatial region or quantity, such as vapor region/fraction, from images and masks.
- **Object detection:** locate and classify an object relevant to inspection, sorting, or experimental measurement.

Do not combine the two tasks merely to train more models. State which output is required, why its error matters, and how it becomes an engineering quantity or action.

## Required workflow

1. Document image/video provenance, frame rate if applicable, resolution, field of view, labels, annotator/process, class definitions, preprocessing, and all data rights.
2. Split by independent source before augmentation: video/run, object, surface, operator/session, or operating condition. No related frames or augmented versions may cross train/validation/test boundaries.
3. Establish a simple reference method. Examples include thresholding or morphology for a segmentation task, or a non-neural detector/inspection rule for a detection task.
4. Train one justified model and record the model version, seed, image size, augmentation, compute environment, and decision threshold.
5. Report task-appropriate held-out metrics: IoU/Dice and measurement error for segmentation; precision, recall, mAP, localization error, and class errors for detection. Accuracy alone is insufficient.
6. Test at least two realistic shifts, such as illumination, blur, orientation, scale, background, surface/geometry, or operating condition. Report the test design and performance change.
7. Complete a visual failure audit containing at least ten incorrect, low-confidence, or boundary cases. Identify plausible causes without claiming a physical mechanism that the data cannot support.
8. For a measurement task, compare the derived quantity with a manual or independent reference on a reserved sample and report units/uncertainty. For an inspection task, define an abstention or human-review rule and analyze its consequence.

## Required reasoning and AI audit

- Explain why the chosen independent split matches the anticipated deployment setting.
- Identify one annotation-quality limitation and one consequence of a false positive and false negative.
- Use the [AI-use record](../../teaching_resources/AI_USE_TEMPLATE.md) if generative AI is permitted. Verify one AI-proposed change on held-out data and a shifted condition.
- During an individual check, be prepared to inspect an unfamiliar output, change a threshold, or explain why a visually plausible mask/detection is not necessarily a valid engineering measurement.

## Submission

```text
lastname_firstname_visual_measurement/
  README.md
  environment.yml or requirements.txt
  train.py or train.ipynb
  AI_USE.md
  results/
    metrics.json
    figures/
    failure_audit.md
    measurement_or_deployment_note.md
```

Grade with the [shared rubric](../../teaching_resources/ENGINEERING_ML_RUBRIC.md). Keep student labels, private data, answer keys, and instructor-held deployment conditions outside the public repository.
