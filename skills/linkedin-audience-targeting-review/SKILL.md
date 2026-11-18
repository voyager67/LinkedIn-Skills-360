---
name: linkedin-audience-targeting-review
description: >-
  the user wants to review LinkedIn campaign audience targeting for relevance, exclusions, privacy and fairness
---

# LinkedIn Ads Audience Targeting Review

**Specialist:** LinkedIn Ads Strategist  
**Category:** Marketing and learning

## When to use this skill

Use this workflow when: the user wants to review LinkedIn campaign audience targeting for relevance, exclusions, privacy and fairness Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Ask for campaign objective, intended buyer or candidate audience, proposed filters, geography, audience size estimates, exclusions, and policy constraints.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Translate the audience into job-relevant or business-relevant characteristics
2. Review each filter for necessity, relevance and potential proxy effects
3. Remove sensitive or inappropriate targeting criteria
4. Check audience size, overlap, exclusions and current platform rules
5. Return a human review checklist before launch

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Audience definition
- Filter-by-filter rationale
- Risk and exclusion review
- Manual pre-launch checklist

## Example prompt

> Review this proposed LinkedIn Ads audience for a B2B software campaign. Flag irrelevant or sensitive targeting and suggest safer filters.

## Edge cases and failure handling

- Do not infer protected traits from names, photos or profile clues
- Ad policy and local law may restrict targeting
- Platform audience estimates are not guaranteed delivery.

## Quality and safety checks

- [ ] Every filter has a business rationale
- [ ] Sensitive targeting is excluded
- [ ] Audience fit and limitations are explicit.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
