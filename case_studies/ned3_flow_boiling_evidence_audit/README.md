# NED3 flow-boiling evidence-audit studio

> **Status: candidate-verified; proposed advanced teaching package.** This is
> initially an evidence-quality exercise, not a general segmentation benchmark.

## Engineering decision

Audit whether a vision model for a fixed near-wall flow-boiling region can
support a stated measurement claim, and determine which additional data would
be needed before using it for independent operating conditions.

| Item | Current scope |
| --- | --- |
| System boundary | Camera-plane union-mask vapor area fraction in a fixed near-wall ROI of a subcooled FC-72 flow-boiling channel. |
| Evidence class | Measured high-speed images, manual annotations, thermal records, AE records, and derived model outputs. |
| Baseline | Human annotation and a simple segmentation audit before a fine-tuned model. |
| Evaluation | The released reconstruction split is same-sequence; it is not independent experiment-held-out generalization. |
| Failure boundary | Do not report projected ROI area as volumetric void fraction or claim verified optical-acoustic synchronization. |

## Teaching use

The studio supports visual-model critique in Module IV, time-base and
multimodal evidence reasoning in Module VII, and AI-agent output verification
in Module IX. Students should examine the release records, identify what a
held-out condition would mean physically, and propose a more credible split.

Use the canonical [BubbleID-Flow dataset card](https://huggingface.co/datasets/UARK-NED3/BubbleID-Flow)
and the linked Zenodo record. The source release includes explicit limitations
on spatial calibration, cross-modality synchronization, and generalization.

See [data_card.md](data_card.md) and the [course-data registry](../../course_data/).
