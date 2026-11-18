---
name: sales-navigator-query-planner
description: >-
  the user wants to design a Sales Navigator lead or account search with relevant filters
---

# Sales Navigator Search Planner

**Specialist:** Sales Development Strategist  
**Category:** Sales, partnerships and business development

## When to use this skill

Use this workflow when: the user wants to design a Sales Navigator lead or account search with relevant filters Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect ideal customer profile, target industries, company size, geography, buyer roles/seniority, exclusion rules, and exact Sales Navigator access level.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Translate the ICP into lead and account filters
2. Separate hard filters from optional refinements
3. Build Boolean keyword variants only where the current surface supports them
4. Define a manual sample-review loop to test relevance before saving a search

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- ICP filter matrix
- Lead and account query plan
- Boolean variants and limitations
- Relevance sampling checklist

## Example prompt

> Build a Sales Navigator search plan for operations leaders at mid-market logistics companies in India.

## Edge cases and failure handling

- Sales Navigator plan and filter availability vary
- Do not scrape, export prohibited data, or evade search limits
- Do not assume filter semantics are universal across products.

## Quality and safety checks

- [ ] Every filter is tied to ICP rationale
- [ ] Search syntax is checked against current official guidance
- [ ] Sample review precedes scale.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
