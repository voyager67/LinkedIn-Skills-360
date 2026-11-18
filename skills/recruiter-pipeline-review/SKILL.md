---
name: recruiter-pipeline-review
description: >-
  a recruiter wants to review a hiring pipeline, identify bottlenecks, or prepare a status update
---

# Recruiter Pipeline Review

**Specialist:** Recruiter Operations Partner  
**Category:** Recruiting and talent operations

## When to use this skill

Use this workflow when: a recruiter wants to review a hiring pipeline, identify bottlenecks, or prepare a status update Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect anonymized stage counts, time window, role, stage definitions, aging, source categories, and agreed funnel targets.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Validate stage definitions and denominator consistency
2. Review conversion, aging, throughput and candidate drop-off by stage
3. Separate data issues from process hypotheses
4. Recommend workflow experiments and specific owners

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Funnel snapshot and definitions
- Bottleneck hypotheses
- Candidate-experience risks
- Action register and data gaps

## Example prompt

> Analyze this anonymized recruiting pipeline and identify where candidates are waiting too long.

## Edge cases and failure handling

- Small samples and changing role mix distort comparisons
- Do not compare recruiters without context
- Do not use metrics to make automated candidate decisions.

## Quality and safety checks

- [ ] Every rate has a denominator and period
- [ ] Hypotheses are not stated as causes
- [ ] Actions focus on process, not profiling.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
