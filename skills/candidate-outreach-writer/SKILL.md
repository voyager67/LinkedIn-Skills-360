---
name: candidate-outreach-writer
description: >-
  the user wants a respectful, personalized candidate message for an open role or talent conversation
---

# Candidate Outreach Writer

**Specialist:** Recruiter Assistant  
**Category:** Recruiting

## When to use this skill

Use this workflow when: the user wants a respectful, personalized candidate message for an open role or talent conversation Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect approved job description, recipient's relevant professional context from authorized sources, why the person may match, message channel, and sender identity. Do not use scraped or sensitive personal data.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Confirm that the role is real, approved, and accurately described.
2. Identify one job-related reason the recipient may find the opportunity relevant.
3. Draft a concise message with transparent sender identity, role context, and an easy way to decline.
4. Avoid pressure, false personalization, misleading compensation claims, or unsupported claims about fit.
5. Prepare one courteous follow-up and a clear stop condition; the recruiter sends manually through an authorized channel.

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Personalization basis
- First outreach draft
- Optional follow-up
- Facts requiring verification
- Stop condition

## Example prompt

> Write a first message to a software engineer whose public open-source work overlaps with this role. Be transparent about why I reached out and don't imply we have met.

## Edge cases and failure handling

- If personalization is weak, use a transparent general message rather than pretending to know the candidate.
- Do not mention sensitive characteristics or inferred personal circumstances.
- If the candidate declines or does not respond after the planned follow-up, stop contacting them.

## Quality and safety checks

- [ ] Opportunity details are accurate.
- [ ] Personalization is job-related and sourced.
- [ ] Message is optional, respectful, and manually reviewed.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
