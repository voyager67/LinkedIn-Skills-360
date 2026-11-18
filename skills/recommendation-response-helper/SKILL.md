---
name: recommendation-response-helper
description: >-
  the user wants to write or respond to a professional LinkedIn recommendation without exaggerating the relationship
---

# Recommendation Response Helper

**Specialist:** Profile Optimizer  
**Category:** Profile and reputation

## When to use this skill

Use this workflow when: the user wants to write or respond to a professional LinkedIn recommendation without exaggerating the relationship Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Ask for the recommendation text, true relationship, the user's own firsthand experience, desired tone, and whether the reply is public.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Identify the actual point being acknowledged
2. Draft a concise thank-you that reflects the relationship accurately
3. For a recommendation the user is writing, ask for specific observed examples and separate personal contribution from team outcomes
4. Invite correction of any detail that may be misremembered

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Thank-you reply or recommendation draft
- Evidence and attribution check
- Facts to confirm

## Example prompt

> Draft a short reply to this recommendation from a colleague; sound warm but not overly familiar.

## Edge cases and failure handling

- Do not invent shared projects, duration, reporting lines, or impact
- Do not write a recommendation as if the user observed facts they cannot verify.

## Quality and safety checks

- [ ] Every first-person claim is supportable by the user
- [ ] The response does not expose confidential work details
- [ ] Tone fits a public professional exchange.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
