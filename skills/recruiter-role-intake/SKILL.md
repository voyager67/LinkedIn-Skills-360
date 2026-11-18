---
name: recruiter-role-intake
description: >-
  a recruiter or hiring manager wants to convert a hiring request into a clear, approved role brief
---

# Recruiter Role Intake

**Specialist:** Recruiter Operations Partner  
**Category:** Recruiting and talent operations

## When to use this skill

Use this workflow when: a recruiter or hiring manager wants to convert a hiring request into a clear, approved role brief Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect business reason, outcomes expected, responsibilities, team context, location/work model, compensation range, level, timeline, constraints, and decision owners.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Clarify why the role exists and what successful work looks like
2. Separate essential outcomes from preferences and proxies
3. Resolve scope, reporting, level, compensation and process gaps
4. Produce a kickoff brief and decision log for hiring-manager approval

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Role intake brief
- Essential and preferred criteria
- Open decisions and owners
- Hiring-process assumptions

## Example prompt

> Run a role-intake workshop for a junior backend engineer role; flag missing compensation and on-call expectations.

## Edge cases and failure handling

- Do not invent salary, level, or legal requirements
- Challenge unnecessary credential filters
- Keep business-sensitive details access-controlled.

## Quality and safety checks

- [ ] Criteria connect to actual work
- [ ] Essential criteria are limited and explainable
- [ ] Unresolved decisions remain visible.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
