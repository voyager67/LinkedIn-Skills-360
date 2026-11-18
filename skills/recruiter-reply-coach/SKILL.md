---
name: recruiter-reply-coach
description: >-
  the user wants to respond to a recruiter about an opportunity, screening question, interview, compensation, availability, or rejection
---

# Recruiter Reply Coach

**Specialist:** Outreach Writer  
**Category:** Networking

## When to use this skill

Use this workflow when: the user wants to respond to a recruiter about an opportunity, screening question, interview, compensation, availability, or rejection Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect the recruiter message, user's genuine interest, relevant availability, confirmed role preferences, compensation constraints if the user chooses to share them, and desired tone.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Classify the recruiter's request and identify any unanswered questions.
2. Clarify the user's position: interested, exploring, unavailable, or declining.
3. Draft a direct response that answers what is known and marks what needs clarification.
4. For compensation or logistics, avoid committing before the user understands scope and total package.
5. Check for oversharing, invented availability, or accidental commitment; give the user a copy-ready reply.

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Message intent and key points
- Recommended reply
- Questions to clarify
- Optional boundary-setting alternative

## Example prompt

> A recruiter asked for my expected salary and notice period. Help me reply that I want to understand the role scope and budget first; don't invent a current salary or notice period.

## Edge cases and failure handling

- If the recruiter message looks suspicious, recommend verifying the sender and company through official channels.
- If the user does not know an answer, draft a transparent clarification rather than guessing.
- For a rejection, remain courteous and avoid demanding feedback.

## Quality and safety checks

- [ ] Reply reflects the user's actual interest and availability.
- [ ] No personal or compensation facts are invented.
- [ ] The user retains control over commitments and disclosures.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
