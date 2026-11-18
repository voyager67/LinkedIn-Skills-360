---
name: account-intelligence-brief
description: >-
  the user wants to prepare a public-source account brief before a B2B conversation
---

# Account Intelligence Brief

**Specialist:** Sales Development Strategist  
**Category:** Sales, partnerships and business development

## When to use this skill

Use this workflow when: the user wants to prepare a public-source account brief before a B2B conversation Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Ask for company, target team or role, business hypothesis, geography, product context, and sources already reviewed.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Research official company materials and reputable public sources
2. Map business priorities, public initiatives and likely stakeholder roles
3. Separate sourced facts from commercial hypotheses
4. Prepare useful discovery questions and a reason to contact now

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Account snapshot
- Verified facts with dates/URLs
- Hypotheses and confidence
- Stakeholder map and discovery questions

## Example prompt

> Prepare an account brief for a first conversation with an Indian retail technology company.

## Edge cases and failure handling

- Do not infer confidential buying intent, internal budgets or personal details
- Public information can be outdated
- Use only sources permitted for the purpose.

## Quality and safety checks

- [ ] Material claims are source-backed
- [ ] Hypotheses are clearly labelled
- [ ] No invented relationship or deal stage.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
