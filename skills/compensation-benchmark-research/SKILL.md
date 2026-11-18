---
name: compensation-benchmark-research
description: >-
  the user wants to research salary ranges for a role, location, seniority, or industry before negotiation
---

# Compensation Benchmark Research

**Specialist:** Job Hunter  
**Category:** Job search and career operations

## When to use this skill

Use this workflow when: the user wants to research salary ranges for a role, location, seniority, or industry before negotiation Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Ask for role level, geography, industry, company stage/size, total-compensation components, experience, and offer date.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Find multiple current and credible compensation sources
2. Normalize currency, annual/monthly units, base/bonus/equity, and sample population
3. Compare like-for-like roles and note outliers
4. Produce a range with confidence and negotiation questions rather than a false precise market rate

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Comparable-role table with sources/dates
- Indicative range and confidence
- Base/variable/equity breakdown
- Negotiation implications and unknowns

## Example prompt

> Benchmark a junior product analyst offer in Bengaluru using current public sources; separate base pay from variable components.

## Edge cases and failure handling

- Salary aggregators can be self-reported or stale
- India CTC and take-home are not equivalent
- Do not infer another person's compensation from their profile.

## Quality and safety checks

- [ ] At least two independent sources where possible
- [ ] Currency and compensation components are normalized
- [ ] Range limitations and dates are visible.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
