# Current assignment: structure discovery in boiling images

This specification supplements the legacy Homework 3 PDF/DOCX. Use it after the instructor confirms data access and provides a private evaluation or interpretation prompt.

## Engineering question

What low-dimensional image structure is present in a boiling-image collection, and when does that structure support a defensible physical interpretation rather than a visually appealing plot?

PCA/SVD and clustering are exploratory tools. A cluster is not automatically a boiling regime, a causal mechanism, or a validated operational state.

## Required workflow

1. Document image source, resolution, preprocessing, operating conditions available in metadata, and the independent sampling unit (for example, video, run, surface, or operating condition).
2. Reserve at least one independent run or condition before choosing representation settings. Fit normalization and PCA/SVD on training images only, then apply the fitted transformation to the reserved images.
3. Establish a simple reference: raw-image distance, mean-image reconstruction, or a no-clustering/one-cluster baseline, as appropriate.
4. Plot explained variance and reconstruction error as functions of retained components. Show reconstructions for representative images selected before inspecting the result.
5. Choose a clustering method and justify the feature space, number of components, distance/scale convention, and number of clusters. Do not select the number of clusters solely because the visualization looks separated.
6. Test stability under at least two plausible choices: bootstrap/resampled images, altered component count, seed, or held-out run. Report what changes.
7. Produce a visual audit with representative members, ambiguous samples, and at least five examples that challenge the proposed interpretation.
8. State a bounded engineering interpretation and one measurement or label that would be needed to validate it.

## Required reasoning and AI audit

- Explain one way adjacent video frames or augmentation could create leakage or artificially stable clusters.
- Distinguish variance captured by PCA from engineering importance.
- Use the [AI-use record](../../teaching_resources/AI_USE_TEMPLATE.md) if generative AI is permitted. Independently reproduce every claimed equation, code change, and interpretation.
- During an individual check, be prepared to interpret an unseen reconstruction, explain a changed cluster assignment, or predict the effect of retaining fewer components.

## Submission

```text
lastname_firstname_structure_discovery/
  README.md
  environment.yml or requirements.txt
  analysis.py or analysis.ipynb
  AI_USE.md
  results/
    reconstruction_metrics.csv
    stability_summary.md
    figures/
    visual_audit.md
```

Grade with the [shared rubric](../../teaching_resources/ENGINEERING_ML_RUBRIC.md). Keep instructor-held data, labels, and interpretation prompts outside the public repository.
