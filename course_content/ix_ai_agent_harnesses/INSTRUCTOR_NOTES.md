# Instructor notes

## Access equity

Offer three equivalent routes: an approved commercial account, an approved local/open-source configuration, or a supplied trace. Grade the specification and verification record, not tool access, token budget, model choice, or hardware performance.

## Fixture design

Keep the graded fixture private or rotate it by term. Use a public practice fixture and an instructor-held variant with different values, a seeded but plausible defect, and hidden tests. Avoid publishing answer keys or immutable diagnostic prompts in the student repository.

## Permission controls

- Begin read-only and offline whenever possible.
- Confine writes to a disposable course directory or a student branch.
- Do not grant browser, credentials, email, cloud-drive, institution, laboratory, or deployment access.
- Require students to inspect proposed diffs and to record all material AI assistance.
- Do not treat tool logs as surveillance or retain them beyond the instructional need; follow institutional policy.

## Local/open-source pathway

Local deployment should be an opt-in instructor-supported activity, not a requirement. Document the exact model, runtime, hardware/OS, quantization if relevant, prompts, tools, and versions if students compare runs. A local runtime may have tool-calling capability, but the instructor must still control the tool schema, permissions, data rights, and logs.

## Assessment controls

Use a short unassisted derivation or code-reading check before the assignment. After submission, conduct a brief individual defense using a perturbed case. Require students to predict the outcome before executing code and to explain one output they rejected. These checks measure transferable judgment more directly than AI-detection scores.
