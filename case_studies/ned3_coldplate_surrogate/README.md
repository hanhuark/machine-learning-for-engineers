# NED3 cold plate surrogate studio

> **Status: candidate-verified; proposed teaching package.** The external
> source is public, but this repository does not yet provide an executable
> tutorial or graded assignment.

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
| Inputs | Two chip heat-flux boundary conditions, two inlet mass-flow rates, and two inlet total temperatures. Units must be read from the source `model_setup.json` before analysis. |
| Candidate outputs | Chip mean/maximum temperature, outlet temperature, and the central yz-plane temperature field. |
| Baseline | Energy balance and a simple thermal-resistance or linear-regression baseline before POD-NN. |
| Held-out unit | Independent CFD simulation, with a documented DOE-based split. |
| Failure boundary | Do not infer transient behavior, experimental accuracy, geometry changes, or unrecorded pressure-drop units from this release. |

## Why this belongs in the course

This studio anchors the Materials, Semiconductors & Power Electronics direction
while reusing the shared ML core. It can support regression in Module I,
PCA/POD in Module III, a constrained inverse-design discussion in Module VI,
and a comparison with physics-aware approaches in Module VIII.

## Source and limitations

Use the canonical [ColdPlate CFD dataset card](https://huggingface.co/datasets/UARK-NED3/ColdPlate-CFD-2000sims)
and the linked Dryad record. The release documents 2,000 steady simulations,
but a classroom lesson should download only an authorized, checksummed subset.
The source card notes that the `pdrop_*` key names are inherited export labels
and that their pressure unit is not recorded; they must not be used as a
unit-qualified target without recovering that information.

See the local [data card](data_card.md) and the [course-data registry](../../course_data/).

## Release steps before use

1. Define a fixed, small subset and record its file hashes.
2. Publish a download script that retrieves only that subset from the canonical
   release; do not commit simulation payloads here.
3. Implement an energy-balance/thermal-resistance baseline and a linear model
   before a POD-NN route.
4. Verify all inputs, targets, units, and the held-out split in a clean Python
   environment.
5. Add a failure audit requiring students to explain a physically implausible
   or out-of-domain prediction.
