---
name: job-posting-risk-review
description: >-
  the user wants to assess whether a LinkedIn job post looks suspicious, misleading, or incomplete
---

# Job Posting Risk Review

**Specialist:** Job Hunter  
**Category:** Job search and career operations

## When to use this skill

Use this workflow when: the user wants to assess whether a LinkedIn job post looks suspicious, misleading, or incomplete Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect the full posting, company URL or name, recruiter identity/context, application link/domain, contact requests, and any communication received.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Extract employer, role, location, employment type, pay, responsibilities, and application route
2. Flag inconsistencies such as upfront fees, requests for sensitive documents early, mismatched domains, vague duties, or implausible claims
3. Check public employer evidence if browsing is available, recording source dates
4. Classify signals as verified, concerning, or unknown and define safe verification steps

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Posting summary
- Evidence table and red flags
- Unknowns and safe verification actions
- Cautious risk assessment, not a definitive fraud verdict

## Example prompt

> Review this job posting and recruiter message for scam indicators before I share my details.

## Edge cases and failure handling

- A risk signal is not proof of fraud
- Fake profiles and spoofed domains can look convincing
- Do not upload passport, bank, tax, or identity credentials during the review.

## Quality and safety checks

- [ ] Each warning is linked to observed evidence
- [ ] Uncertainty is made visible
- [ ] Advice never asks the user to pay a recruiter.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
