---
name: job-alert-search-setup-planner
description: >-
  the user wants a repeatable LinkedIn Jobs saved-search and alert strategy
---

# Job Alert and Saved Search Planner

**Specialist:** Job Hunter  
**Category:** Job search and career operations

## When to use this skill

Use this workflow when: the user wants a repeatable LinkedIn Jobs saved-search and alert strategy Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Ask for role families, locations, remote/hybrid preference, experience level, schedule, frequency tolerance, and what alerts are already active.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Split materially different targets into separate searches
2. Specify keywords, filters, alert cadence, and naming conventions
3. Explain how to manually save searches and verify alert settings in the current UI
4. Set a review cadence to retire noisy alerts and update target terms

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Saved-search plan
- Search names and filters
- Alert cadence recommendation
- Review and cleanup checklist

## Example prompt

> Create separate saved-search plans for frontend internships and junior full-stack roles in Mumbai.

## Edge cases and failure handling

- Feature labels and alert limits may change
- Avoid excessive alerts or duplicate searches
- A saved search does not prove a job is still open.

## Quality and safety checks

- [ ] Each alert maps to a distinct target
- [ ] Cadence is manageable
- [ ] Users verify dates and availability before applying.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
