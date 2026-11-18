---
name: hiring-debrief
description: >-
  the user wants to structure a hiring debrief, synthesize interview feedback, or identify evidence and unresolved questions across a panel
---

# Hiring Debrief Facilitator

**Specialist:** Recruiter Assistant  
**Category:** Recruiting

## When to use this skill

Use this workflow when: the user wants to structure a hiring debrief, synthesize interview feedback, or identify evidence and unresolved questions across a panel Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect approved role criteria, anonymized candidate ID, structured scorecards, interviewer evidence notes, and any outstanding reference or work-sample evidence. Exclude protected or unnecessary personal information.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Restate the role criteria and evidence standard agreed before interviews.
2. Summarize each competency using observed evidence, not vague impressions.
3. Highlight agreement, disagreement, missing evidence, and possible interviewer bias or inconsistent questioning.
4. Generate neutral follow-up questions or additional assessment options when evidence is insufficient.
5. Produce a decision-support summary for accountable human decision-makers; do not issue an automatic hire/reject result.

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Criteria-based evidence summary
- Areas of agreement and disagreement
- Missing or conflicting evidence
- Follow-up assessment questions
- Human decision notes

## Example prompt

> Summarize these anonymized panel notes against the agreed role criteria. Flag unsupported impressions and do not make the hire/no-hire decision for us.

## Edge cases and failure handling

- If notes contain protected or irrelevant personal information, exclude it and flag the process issue.
- If evidence is contradictory, represent both accounts and request clarification.
- Never transform subjective “culture fit” into a score.

## Quality and safety checks

- [ ] Summary is anchored to agreed criteria.
- [ ] No protected-trait inference or automatic decision.
- [ ] Dissent and uncertainty remain visible.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
