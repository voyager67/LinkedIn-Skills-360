---
name: talent-boolean-search-builder
description: >-
  a recruiter wants search strings for public professional search tools or approved sourcing databases
---

# Talent Boolean Search Builder

**Specialist:** Recruiter Operations Partner  
**Category:** Recruiting and talent operations

## When to use this skill

Use this workflow when: a recruiter wants search strings for public professional search tools or approved sourcing databases Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect role, must-have skills, synonyms, titles, location, seniority, adjacent backgrounds, exclusions, and the search tool being used.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Break the job profile into title, skill and domain synonym groups
2. Build a broad recall query and focused precision variants
3. Explain Boolean clauses and tool-specific limitations
4. Define manual sampling and query tuning based on relevant/irrelevant results

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Search concept map
- Boolean query variants
- Inclusion/exclusion logic
- Search validation checklist

## Example prompt

> Build search strings for platform engineers with Kubernetes and Terraform experience, including adjacent job titles.

## Edge cases and failure handling

- Search syntax differs among LinkedIn Recruiter, Sales Navigator, and external tools
- Do not scrape profiles or bypass search limits
- Avoid exclusions that encode demographic proxies.

## Quality and safety checks

- [ ] Query maps to approved role criteria
- [ ] No protected-trait terms
- [ ] Manual sample review is included.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
