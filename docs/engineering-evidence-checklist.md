---
layout: default
title: Engineering Evidence Checklist
---

# Engineering evidence checklist

Use this checklist before claiming that an AI/ML result supports an engineering decision. It is intentionally method-agnostic: the same questions apply to regression, vision, PINNs, forecasting, reinforcement learning, generative models, and agent-assisted workflows.

## 1. Frame the engineering question

- What decision will the result inform?
- What is the system boundary, operating range, and intended user?
- What is the target variable or action, including units and time basis?
- What would a harmful false positive, false negative, or wrong numerical estimate mean?

## 2. Describe the evidence

- Where did the data, simulation, measurement, or labels originate?
- What is the independent sampling unit: device, run, experiment, part, production lot, site, patient, or time interval?
- What preprocessing occurred, and what information was unavailable at prediction time?
- What rights, privacy, sponsor, or export-control limits apply?

## 3. Establish a baseline

- What simple physical, empirical, rule-based, or conventional method should the AI method beat?
- Is the baseline evaluated on the same held-out evidence?
- Is the chosen metric meaningful for the engineering decision?

## 4. Test independent evidence

- Does the split prevent leakage across the meaningful unit?
- Are hyperparameters, normalization, and thresholds selected without seeing test results?
- Is there a condition-held-out, time-held-out, or out-of-regime test?
- Are errors reported by operating condition, horizon, class, region, or other relevant subgroup?

## 5. Audit physical credibility and failure

- Does the output respect dimensional, conservation, geometric, safety, or feasibility constraints where applicable?
- Which examples fail visibly or materially?
- Could label error, sensor drift, model-form error, or distribution shift explain the apparent performance?
- When should the model abstain or defer to a human/physical test?

## 6. Document AI-assisted work

- What AI tool, model, skill, prompt, data access, or external tool connection was used?
- What was the permitted scope, and what evidence was independently checked?
- Can the learner explain, alter, and rerun the relevant workflow?
- Does the final report distinguish measured, simulated, inferred, and generated material?

## Minimum claim format

> For **[system and operating range]**, the model predicts **[target and units]** using **[inputs/evidence]**. Against **[baseline]** on **[held-out rule]**, it achieved **[metric]**. The result is limited by **[failure boundary]** and is intended only to support **[decision]**.

Use the shared [engineering-ML rubric](../teaching_resources/ENGINEERING_ML_RUBRIC.md) when grading this evidence.
