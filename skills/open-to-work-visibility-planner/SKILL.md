---
name: open-to-work-visibility-planner
description: >-
  the user wants to decide how to communicate job-seeking status and review LinkedIn Open to Work visibility options
---

# Open to Work Visibility Planner

**Specialist:** Profile Optimizer  
**Category:** Profile and reputation

## When to use this skill

Use this workflow when: the user wants to decide how to communicate job-seeking status and review LinkedIn Open to Work visibility options Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect target roles, preferred locations, employment type, urgency, confidentiality constraints, and concerns about current employer visibility.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Clarify the trade-off between discoverability and discretion
2. Prepare accurate role/location preferences and a concise explanation for recruiters
3. List current LinkedIn visibility choices for the user to verify in account settings
4. Draft an alternative quiet-search plan if public signalling is unsuitable

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Visibility decision matrix
- Role and location preference checklist
- Optional recruiter-facing note
- Quiet-search alternative

## Example prompt

> Help me decide whether to use Open to Work while I am still employed and searching confidentially.

## Edge cases and failure handling

- Availability and labels in LinkedIn settings can change by account and region
- Do not promise that an employer cannot discover a setting.

## Quality and safety checks

- [ ] The privacy trade-off is explicit
- [ ] No certainty is claimed about visibility guarantees
- [ ] The user makes and confirms the setting change.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
