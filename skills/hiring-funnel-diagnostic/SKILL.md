---
name: hiring-funnel-diagnostic
description: >-
  a talent leader wants to diagnose hiring funnel data across role, stage, source, or time period
---

# Hiring Funnel Diagnostic

**Specialist:** Recruiter Operations Partner  
**Category:** Recruiting and talent operations

## When to use this skill

Use this workflow when: a talent leader wants to diagnose hiring funnel data across role, stage, source, or time period Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect anonymized counts, role family, stages, source definitions, date window, stage-entry rules and business context.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Check counts, stage definitions and duplicate records
2. Calculate conversions and aging with explicit denominators
3. Compare only comparable cohorts and note sample limitations
4. Propose process experiments and a measurement plan

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Data-quality review
- Funnel conversion and aging table
- Bottleneck hypotheses
- Experiment and owner list

## Example prompt

> Diagnose these anonymized hiring funnel numbers for our graduate software roles.

## Edge cases and failure handling

- Do not infer candidate quality from source alone
- Avoid rankings of individuals or demographic inferences
- Do not call correlations causal.

## Quality and safety checks

- [ ] Calculations are reproducible
- [ ] Cohorts and windows are explicit
- [ ] Recommendations focus on process fairness and speed.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
