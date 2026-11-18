---
name: follow-up-planner
description: >-
  the user wants to plan a follow-up after an application, networking conversation, referral request, recruiter exchange, or interview
---

# Networking and Application Follow-up Planner

**Specialist:** Outreach Writer  
**Category:** Networking

## When to use this skill

Use this workflow when: the user wants to plan a follow-up after an application, networking conversation, referral request, recruiter exchange, or interview Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect last contact date, context, any promised response date, message history, next stage, and the user's intended outcome. Distinguish a stated deadline from a suggested reminder.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Review the interaction and identify whether a response or action was explicitly promised.
2. Decide whether a follow-up is useful, premature, or unnecessary.
3. Choose a respectful interval based on context and stated timelines; explain the choice.
4. Draft a short message that references the prior interaction and adds useful context without guilt or pressure.
5. Set a stop condition and update the user's private tracker only with confirmed information.

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Follow-up recommendation and rationale
- Suggested date or window
- Draft message
- Stop condition and tracker update

## Example prompt

> I interviewed last Thursday and the recruiter said they hoped to update me this week. Draft a polite follow-up for after the promised window, not before it.

## Edge cases and failure handling

- If a promised date has not passed, recommend waiting unless there is a genuine deadline.
- If the user has already followed up repeatedly without response, recommend stopping.
- Do not manufacture urgency, competing offers, or deadlines.

## Quality and safety checks

- [ ] Timing respects prior commitments.
- [ ] Message is concise and non-coercive.
- [ ] Reminder dates are labelled as suggestions unless confirmed.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
