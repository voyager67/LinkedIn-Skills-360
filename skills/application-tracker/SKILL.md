---
name: application-tracker
description: >-
  the user wants to create, update, summarize, or plan follow-ups for a job application pipeline
---

# Job Application Tracker

**Specialist:** Job Hunter  
**Category:** Search and applications

## When to use this skill

Use this workflow when: the user wants to create, update, summarize, or plan follow-ups for a job application pipeline Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect job/company, source URL, role, location, date found, application date, current stage, next action, deadline, contact, and notes. Use initials or IDs for contacts where practical.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Create a row for each distinct opportunity and normalize stage names.
2. Capture dates and next actions; distinguish actual deadlines from personal reminders.
3. Identify stale, duplicate, incomplete, and time-sensitive records.
4. Suggest the next action for each active application based on stage and last contact.
5. Summarize pipeline health without assuming that an unreported response means rejection.

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Tracker schema or updated rows
- Stage summary
- Next-action list with dates
- Missing fields and stale-record flags
- Optional CSV-compatible table

## Example prompt

> Create a CSV-friendly application tracker for these five roles. Add stages, next actions, and a follow-up date only where a real contact or deadline supports it.

## Edge cases and failure handling

- Do not invent a response, status, contact name, or deadline.
- If the user provides conflicting dates, flag the conflict instead of choosing silently.
- Keep candidate and recruiter contact details private; do not publish tracker data.

## Quality and safety checks

- [ ] Each record has a unique role/company identifier.
- [ ] Dates and stage changes are traceable to user input.
- [ ] Follow-up reminders are respectful and not excessive.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
