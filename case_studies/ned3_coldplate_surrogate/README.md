# NED3 cold plate surrogate studio

> **Status: ready to assign.** The pinned teaching route, current assignment,
> and instructor-held individual-verification design were reviewed locally on
> 2026-10-17. It remains a simulated-CFD learning case, not hardware
> validation.

## Engineering decision

Screen liquid-cooling boundary conditions for a dual-chip pin-fin cold plate
before running a costly steady CFD solve. The learning objective is not to
replace CFD validation. It is to compare a reduced-order ML surrogate with a
declared physical and numerical baseline, and to identify when the surrogate
should not be trusted.

| Item | Current scope |
| --- | --- |
| System boundary | A simulated liquid-cooled dual-chip pin-fin cold plate under the source deposit's steady, incompressible CFD assumptions. |
| Evidence class | Simulated CFD fields and scalar reports; not measured hardware data. |
| Inputs | Two chip heat-flux boundary conditions (W/m²), two inlet mass-flow rates (kg/s), and two inlet total temperatures (K), as documented by the source release. |
| Candidate outputs | Chip mean/maximum temperature, outlet temperature, and the central yz-plane temperature field. |
| Baseline | A fitted, lumped mixed-outlet energy balance plus a simple linear-regression baseline before POD-NN. |
| Held-out unit | Independent CFD simulation, with a documented DOE-based split. |
| Failure boundary | Do not infer transient behavior, experimental accuracy, geometry changes, or unrecorded pressure-drop units from this release. |

## Why this belongs in the course

This studio anchors the Materials, Semiconductors & Power Electronics direction
while reusing the shared ML core. It can support regression in Module I,
PCA/POD in Module III, a constrained inverse-design discussion in Module VI,
and a comparison with physics-aware approaches in Module VIII.

## Audience, prerequisites, and expected effort

The case is designed for learners who have completed the regression module and
can run a documented Python command. It requires basic heat-transfer concepts:
heat rate, mass flow rate, energy balance, and temperature units. Budget about
4–6 hours after the instructor has provisioned the checksummed subset.

## Source and limitations

Use the canonical [ColdPlate CFD dataset card](https://huggingface.co/datasets/UARK-NED3/ColdPlate-CFD-2000sims)
and the linked Dryad record. The reviewed Hugging Face revision is
`58911fc77390a70a6c71da0612e02b4976976283` (verified 2026-10-17). The
release documents 2,000 steady simulations,
but a classroom lesson should download only an authorized, checksummed subset.
The source card notes that the `pdrop_*` key names are inherited export labels
and that their pressure unit is not recorded; they must not be used as a
unit-qualified target without recovering that information.

See the local [data card](data_card.md), [reproducibility record](reproducibility.md),
and the [course-data registry](../../course_data/).

## Release steps before use

1. Define a fixed, small subset and record its file hashes.
2. Publish a download script that retrieves only that subset from the canonical
   release; do not commit simulation payloads here.
3. Keep the energy-balance baseline as a comparator before a POD-NN route; do
   not treat its fitted effective heat capacity as a measured material property.
4. Add a failure audit requiring students to explain a physically implausible
   or out-of-domain prediction.

The current student-facing [assignment](assignment.md) and
[instructor notes](instructor_notes.md) specify the bounded assessment route.
