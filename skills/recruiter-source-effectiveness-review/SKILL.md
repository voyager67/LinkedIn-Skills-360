---
name: recruiter-source-effectiveness-review
description: >-
  a recruiter wants to compare sourcing channel usefulness using anonymized aggregate pipeline data
---

# Recruiter Source Effectiveness Review

**Specialist:** Recruiter Operations Partner  
**Category:** Recruiting and talent operations

## When to use this skill

Use this workflow when: a recruiter wants to compare sourcing channel usefulness using anonymized aggregate pipeline data Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect source definitions, anonymized volume by stage, role family, time period, effort/cost data, and duplicate attribution rules.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Normalize source attribution and cohort windows
2. Compare qualified progression, time and effort, not only raw applicant volume
3. Identify confounders such as role mix, brand campaigns and referral bias
4. Recommend controlled channel tests with clear stop criteria

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Source metric table
- Data-quality caveats
- Channel hypotheses
- Test plan

## Example prompt

> Compare LinkedIn, referrals and campus outreach as channels using this anonymized quarterly funnel.

## Edge cases and failure handling

- Do not infer individual candidate merit from source
- Attribution is often multi-touch and incomplete
- Avoid treating small volume as statistically decisive.

## Quality and safety checks

- [ ] Metric definitions and denominators are explicit
- [ ] Confounders are noted
- [ ] Recommendations are testable.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
