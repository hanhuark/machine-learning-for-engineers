# Instructor notes: cold-plate surrogate studio

## Before release

- Provide the pinned 141-file subset and its manifest through an approved local
  course location. Do not redistribute the full archive from this repository.
- Confirm that students can run the two baseline scripts in the supported
  environment and that their local data path is outside the Git repository.
- Keep any alternative test IDs, instructor perturbations, grading notes, and
  answer keys outside the public repository. Rotate the individual prompt by
  term or learner when practical.

## Assessment design

The public files deliberately disclose the fixed teaching split and baseline.
Grade the stated data contract, the held-out workflow, failure reasoning, and
the individual defense—not a lower error obtained with a larger model. The
individual check can use a previously unseen operating condition and should ask
for a prediction before the student runs code.

Accept equivalent scripts or notebooks if they preserve the split, record
versions, and do not use undocumented pressure-drop units. Students may use
approved AI tools, but an AI-use record and individual check are required.
Avoid AI-detection claims as evidence of learning.

## Accessibility and compute

The subset is approximately 0.091 GiB and the supplied NumPy baselines run on
a standard CPU in under one second after data access. Offer a pre-downloaded
course copy for learners with limited network access. Do not require ANSYS,
GPU access, an API key, or a commercial AI subscription.

## Safety of claims

This dataset contains steady CFD outputs, not measurements. The source release
does not record the `pdrop_*` unit. Do not convert this activity into a
pressure-drop, transient-control, or hardware-design exercise without a
separate data/physics review.
