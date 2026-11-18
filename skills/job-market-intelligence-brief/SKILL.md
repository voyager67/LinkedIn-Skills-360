---
name: job-market-intelligence-brief
description: >-
  the user wants a sourced view of hiring demand, role trends, skill requirements, or target-employer activity
---

# Job Market Intelligence Brief

**Specialist:** Job Hunter  
**Category:** Job search and career operations

## When to use this skill

Use this workflow when: the user wants a sourced view of hiring demand, role trends, skill requirements, or target-employer activity Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect target occupation, geography, seniority, timeframe, industry, and the decision the research will inform.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Define a bounded research question and time window
2. Gather current public postings and primary labour-market sources where available
3. Separate observed sample patterns from market-wide conclusions
4. Summarize recurring skills, role levels, employers, and data limitations with dates and source links

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Executive summary
- Sample scope and date window
- Observed demand themes and evidence
- Caveats, source list, and implications

## Example prompt

> Research current entry-level data analyst hiring themes in Mumbai and summarize the skills appearing across recent postings.

## Edge cases and failure handling

- Public job-posting samples are not a complete labour-market census
- Postings can be stale or duplicated
- Do not infer salary or demand from isolated examples.

## Quality and safety checks

- [ ] Sample size and retrieval dates are stated
- [ ] Facts and interpretation are separate
- [ ] No market-wide claim exceeds the evidence.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
