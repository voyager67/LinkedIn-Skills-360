---
name: job-search-strategist
description: >-
  the user asks for a structured job search plan, role targeting strategy, search queries, or weekly job-search routine
---

# Job Search Strategist

**Specialist:** Job Hunter  
**Category:** Search and applications

## When to use this skill

Use this workflow when: the user asks for a structured job search plan, role targeting strategy, search queries, or weekly job-search routine Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect target roles, seniority, geography or remote preference, industries, work authorization constraints if relevant, skills, experience, preferred compensation if comfortable, and weekly time budget.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Translate the user's goals into a primary target role and one or two adjacent role families.
2. Define role criteria: must-haves, preferences, deal-breakers, and acceptable trade-offs.
3. Build search strings from title variants, skill combinations, location, and level.
4. Set a sustainable weekly workflow for discovery, fit review, tailored applications, networking, and reflection.
5. Define tracking fields and a review cadence; adapt the plan using observed results rather than unsupported job-market claims.

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Target role map
- Search query set
- Role filters and decision rules
- Weekly action plan
- Tracking and review metrics

## Example prompt

> Build a four-week search plan for junior backend developer roles in Mumbai and remote India. I can spend six hours each week and have two Python projects.

## Edge cases and failure handling

- For a student or fresher, include internships, apprenticeships, graduate roles, and project-based proof.
- If location/work authorization is unclear, do not assume eligibility.
- If the market appears slow, treat anecdotes as signals and recommend checking current postings.

## Quality and safety checks

- [ ] Plan is feasible within the stated time budget.
- [ ] Search terms reflect the user's actual experience level.
- [ ] No guaranteed number of applications or interviews is promised.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
