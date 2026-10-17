# Course data registry

This directory records the external datasets selected for future engineering
application studios. It intentionally contains **no copied experimental,
simulation, student, confidential, or restricted payloads**.

Use [dataset_manifest.csv](dataset_manifest.csv) to identify the canonical
source, license, evidence class, access boundary, and proposed teaching role
for each case. The manifest is a curation record, not a redistribution grant:
a public landing page or download does not itself authorize copying a source
file into this repository or into a course package.

## Status labels

- **candidate-verified**: the source and its stated access/license information
  have been checked, but this repository does not yet provide a runnable
  teaching package.
- **release-reconciliation-required**: public hosting and local release
  records need reconciliation before an instructor relies on the source.
- **rights-audit-required**: the intended source includes raw, derived,
  annotated, or model material whose release status must be reviewed before a
  public course subset is created.
- **ready-to-learn**: reserved for a case with a documented command, expected
  runtime, data card, and a clean-environment verification result.
- **ready-to-assign**: reserved for a ready-to-learn case with a current
  assignment, protected individual evidence, and instructor validation.

## Public-course boundary

Keep large source archives in their canonical data repositories. A future
teaching release may provide a download script, an authorized small subset, or
a synthetic alternative, but must retain dataset version, citation, checksum,
units, split rule, and transformation lineage. Do not upload unpublished
research data, protected health information, sponsor-restricted material,
student work, instructor-held tests, or third-party records without explicit
redistribution permission.

The [case studies](../case_studies/) directory contains the instructional
framing for the records below. The [data-card template](../teaching_resources/DATA_CARD_TEMPLATE.md)
and [reproducibility checklist](../teaching_resources/REPRODUCIBILITY_CHECKLIST.md)
remain the common release standard.
