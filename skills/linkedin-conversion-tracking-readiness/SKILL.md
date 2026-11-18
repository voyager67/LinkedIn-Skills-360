---
name: linkedin-conversion-tracking-readiness
description: >-
  the user wants to plan or review readiness for LinkedIn conversion measurement and attribution
---

# LinkedIn Conversion Tracking Readiness Review

**Specialist:** LinkedIn Ads Strategist  
**Category:** Marketing and learning

## When to use this skill

Use this workflow when: the user wants to plan or review readiness for LinkedIn conversion measurement and attribution Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect campaign objective, conversion action, website/app flow, analytics stack, consent mechanism, event definitions, attribution needs and authorized technical owners.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Define the business conversion and exact event boundary
2. Map the user journey and required event data
3. Identify consent, data minimization and governance questions
4. Document technical dependencies for the analytics owner
5. List validation steps and reporting limitations before activation

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Conversion measurement specification
- Event and parameter map
- Consent/privacy questions
- Technical validation checklist

## Example prompt

> Create a measurement plan for a LinkedIn ad that sends visitors to a product demo request form.

## Edge cases and failure handling

- Do not provide code that transmits personal data without review
- Conversions API and tags require authorized technical setup
- Attribution is not proof of incrementality.

## Quality and safety checks

- [ ] Events correspond to real business actions
- [ ] Only necessary data is planned
- [ ] Technical and privacy owners are named.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
