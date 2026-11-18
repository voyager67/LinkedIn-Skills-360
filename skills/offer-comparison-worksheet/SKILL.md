---
name: offer-comparison-worksheet
description: >-
  the user wants to compare two or more job offers across compensation, role, growth, location, risk, and values
---

# Offer Comparison Worksheet

**Specialist:** Job Hunter  
**Category:** Job search and career operations

## When to use this skill

Use this workflow when: the user wants to compare two or more job offers across compensation, role, growth, location, risk, and values Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect offer letters or verified terms, role scope, total compensation breakdowns, location, working model, benefits, deadlines, and personal priorities.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Normalize pay periods, currencies, variable pay, equity, benefits and vesting
2. Compare role scope, manager/team, growth, stability, commute, flexibility and constraints
3. Weight criteria chosen by the user rather than imposing universal values
4. List unresolved terms and prepare clarifying questions

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Side-by-side offer matrix
- User-weighted comparison
- Risks and unknowns
- Clarification questions and decision notes

## Example prompt

> Compare these two offers using my priorities: learning, manager quality, fixed pay, and location.

## Edge cases and failure handling

- Equity and variable pay are uncertain and not cash-equivalent
- Do not give tax/legal advice
- Do not treat public company estimates as guaranteed offer terms.

## Quality and safety checks

- [ ] Every term is sourced to the offer or labelled unknown
- [ ] User priorities determine weights
- [ ] Trade-offs are transparent.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
