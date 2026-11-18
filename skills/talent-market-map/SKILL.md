---
name: talent-market-map
description: >-
  a recruiter wants to map public talent pools, adjacent industries, role titles, and geographic supply for an approved search
---

# Talent Market Mapping Brief

**Specialist:** Recruiter Operations Partner  
**Category:** Recruiting and talent operations

## When to use this skill

Use this workflow when: a recruiter wants to map public talent pools, adjacent industries, role titles, and geographic supply for an approved search Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect approved role profile, geography, seniority, adjacent sectors, relevant skills, search access, and the intended use of the map.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Define the target population and time window
2. Identify public role/title and company clusters using permitted sources
3. Separate observed profiles or postings from market-level inference
4. Summarize supply constraints, adjacent talent pools and sourcing hypotheses

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Market map scope and method
- Role/title and sector clusters
- Talent-pool hypotheses
- Source/sample limitations and next steps

## Example prompt

> Prepare a talent market map for senior data platform engineers in India, using permitted public research only.

## Edge cases and failure handling

- A LinkedIn search sample is not the full labour market
- Do not estimate demographic composition from profile names or photos
- Do not store personal profiles in a bulk dataset.

## Quality and safety checks

- [ ] Scope and sampling method are explicit
- [ ] Findings are appropriately qualified
- [ ] No sensitive inference.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
