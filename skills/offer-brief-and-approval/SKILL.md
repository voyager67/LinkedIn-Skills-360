---
name: offer-brief-and-approval
description: >-
  a recruiter wants to prepare an offer recommendation or approval brief using confirmed role and compensation terms
---

# Recruitment Offer Brief and Approval Pack

**Specialist:** Recruiter Operations Partner  
**Category:** Recruiting and talent operations

## When to use this skill

Use this workflow when: a recruiter wants to prepare an offer recommendation or approval brief using confirmed role and compensation terms Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect approved compensation bands, candidate expectations, role level, benefits, location, start date, dependencies, and internal approval process.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Validate consistency with approved role and band
2. Separate base, variable, equity, benefits and one-time items
3. List approvals and unresolved terms
4. Prepare a candidate-facing offer summary only after authorized approval

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Internal offer brief
- Compensation component table
- Approval checklist
- Candidate offer discussion notes

## Example prompt

> Prepare an offer approval brief for a software engineer using these approved compensation components.

## Edge cases and failure handling

- Do not fabricate budget authority or approval
- Equity valuation and variable pay require caveats
- Do not share internal salary data externally without authorization.

## Quality and safety checks

- [ ] Every term matches source documentation
- [ ] Approvals are explicit
- [ ] Internal and candidate-facing versions are separated.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
