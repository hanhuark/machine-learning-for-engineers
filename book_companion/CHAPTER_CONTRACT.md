# Chapter companion contract

Use this contract when turning a course module or application studio into a
book-companion chapter. A chapter should link to canonical material elsewhere
in the repository whenever possible; it should not fork tutorials merely to
change their book location.

## Required public assets

1. **Chapter guide:** purpose, prerequisites, engineering questions, learning
   objectives, and links to the canonical tutorial and exercise.
2. **Engineering data contract:** source, evidence class, variables and units,
   access/license boundary, preprocessing, independent sampling unit, and split
   logic.
3. **Baseline and evaluation:** a simple credible reference method, a held-out
   or otherwise independent evaluation rule, metrics with units, and a stated
   validity range.
4. **Failure and transfer task:** at least one failure mode, an explanation of
   why it matters physically, and a changed-condition task that tests transfer
   rather than recall.
5. **Reproducibility record:** environment/dependency guidance, seed or
   deterministic split when applicable, commands, expected outputs, and a
   statement of what was actually verified.
6. **Assessment boundary:** public exercises may be supplied, but instructor
   answer keys, private tests, student records, and individual-check prompts
   remain outside the repository.

## Standard chapter sequence

Use the following sequence unless the method demands another ordering:

1. State the engineering decision and system boundary.
2. Define variables, units, assumptions, and evidence class.
3. Establish a physics, empirical, numerical, or human-reference baseline.
4. Build and evaluate the ML method without contaminating held-out evidence.
5. Inspect residuals, uncertainty, physical plausibility, and failure cases.
6. State the valid-use boundary and the next evidence needed for stronger use.

## Updating fast-moving material

Model names, libraries, hosted tools, and agent products change faster than a
book manuscript. Keep the book explanation centered on durable decisions:
data rights, task specification, verification, traceability, and engineering
accountability. Put product-specific setup and maintained comparison tables in
the repository, version them, and date their review.
