# NED3 BoilingBench CV studio

> **Status: release reconciliation required; proposed teaching package.** Do
> not build a public course subset until the public card, archive payload, and
> source-image release records identify the same canonical version.

## Engineering decision

Estimate two-dimensional bubble morphology from high-speed boiling images and
decide whether an image model remains credible after the fluid, surface,
optical arrangement, regime, or source sequence changes.

| Item | Current scope |
| --- | --- |
| System boundary | Two-dimensional camera-plane bubble masks in the documented image domains. |
| Evidence class | Measured images, human annotations, and derived morphometry. |
| Baseline | Rule-based thresholding or a documented non-neural image baseline. |
| Evaluation | Grouped split by source video/power condition and reporting by regime. |
| Failure boundary | A water-versus-HFE score is a compound domain shift, not evidence of a fluid-only causal effect. |

## Learning route

The eventual studio should begin with image metadata and simple bubble-count or
vapor-area questions before instance segmentation. Students should inspect
failed masks, compare pooled and regime-specific metrics, and explain why
random frame splits leak correlated acquisition sequences.

The public [BoilingBench-CV dataset card](https://huggingface.co/datasets/UARK-NED3/BoilingBench-CV)
lists a CC BY 4.0 card and grouped benchmark metadata. The inspected local
release record uses an internal version label and states that its archive was
being prepared. Reconcile those records, including the source-image payload,
before a classroom download script or assignment is released.

See [data_card.md](data_card.md) and the [course-data registry](../../course_data/).
