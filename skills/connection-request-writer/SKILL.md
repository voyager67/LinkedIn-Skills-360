---
name: connection-request-writer
description: >-
  the user wants a personalized LinkedIn connection note or short introduction to a person they have a legitimate reason to contact
---

# LinkedIn Connection Request Writer

**Specialist:** Outreach Writer  
**Category:** Networking

## When to use this skill

Use this workflow when: the user wants a personalized LinkedIn connection note or short introduction to a person they have a legitimate reason to contact Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect recipient's relevant public context or user's reason for connecting, shared context if true, desired outcome, and character limit. Do not require a recipient's full name.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Identify a real point of relevance from user-provided or verified public context.
2. State who the user is in a few words, if useful.
3. Write a concise, low-pressure connection note with one clear reason to connect.
4. Remove generic flattery, false familiarity, and immediate asks that are disproportionate to the relationship.
5. Offer one or two tone variants and remind the user to check platform limits before sending.

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Recommended connection note
- Alternate version
- Personalization detail used
- Fact to verify before sending

## Example prompt

> Draft a short connection note to an alumnus working in data engineering. I found their talk on data pipelines useful and would like to connect, not immediately ask for a referral.

## Edge cases and failure handling

- If there is no authentic personalization, write a transparent general note rather than inventing a shared interest.
- If platform character limits change, ask the user to confirm in the UI.
- Do not generate bulk variations for mass invitations.

## Quality and safety checks

- [ ] Any shared background or interest is true.
- [ ] The note is concise and respectful.
- [ ] The user reviews and sends it manually.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
