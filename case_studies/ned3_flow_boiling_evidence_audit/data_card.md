# Data card for NED3 flow-boiling evidence-audit studio

## Identity and rights

- Dataset name/version: BubbleID-Flow Multimodal Flow-Boiling Dataset; release reviewed 2026-10-17.
- Provider and stable identifiers: NED3 Laboratory; [Hugging Face dataset card](https://huggingface.co/datasets/UARK-NED3/BubbleID-Flow); [Zenodo DOI](https://doi.org/10.5281/zenodo.22235802).
- Evidence class: measured, annotated, and derived.
- License: CC BY 4.0 according to the release record.
- Access boundary: no payload is copied here; retain source attribution and release version.

## Engineering context and evaluation

- Fluid/channel: FC-72 in a 2.5 mm by 5.0 mm heated rectangular passage; the documented target is two-dimensional vapor area fraction in a fixed near-wall ROI.
- Optical record: 3,977 BMP images and 130 manually annotated images in the source release.
- Split limitation: the reported 104/26 reconstruction split samples a sorted source sequence and is not an independent experiment-held-out split.
- Required audit: separate image-level reconstruction from condition-level generalization; identify the independent experimental unit before reporting performance.

## Known limitations

- The archive does not provide spatial calibration sufficient for calibrated bubble size, local optical-thermal registration, or volumetric void fraction.
- Optical, thermal, and AE systems do not have verified common-trigger synchronization.
- Folder labels containing onset/CHF terminology are retained source labels, not validated transition labels.
