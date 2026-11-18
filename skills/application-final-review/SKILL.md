---
name: application-final-review
description: >-
  the user wants a pre-submit check of their resume, cover letter, profile links, or application form
---

# Application Final Review

**Specialist:** Job Hunter  
**Category:** Job search and career operations

## When to use this skill

Use this workflow when: the user wants a pre-submit check of their resume, cover letter, profile links, or application form Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Request the job description, final documents, application answers, target company, deadline, and any constraints such as file format or word limit.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Verify role/company names, dates, contact details, links, and document consistency
2. Check required qualifications and application questions for truthful representation
3. Inspect file naming, format, and readability checklist
4. Produce a final issue list sorted into blocking, important, and optional

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Submission checklist
- Blocking corrections
- Consistency and evidence checks
- Final user approval reminder

## Example prompt

> Review my application pack for this product analyst role before I submit it.

## Edge cases and failure handling

- Do not claim an upload or submission occurred
- Do not retain unnecessary sensitive identifiers in examples or repo templates.

## Quality and safety checks

- [ ] No unverified fact is silently edited
- [ ] All required materials are checked
- [ ] Submission remains the user's action.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
