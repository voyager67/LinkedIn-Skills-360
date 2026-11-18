---
name: boolean-job-search-builder
description: >-
  the user wants targeted search strings for LinkedIn jobs, people, companies, or external job boards
---

# Boolean Job Search Builder

**Specialist:** Job Hunter  
**Category:** Job search and career operations

## When to use this skill

Use this workflow when: the user wants targeted search strings for LinkedIn jobs, people, companies, or external job boards Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect target role titles, synonyms, seniority, must-have terms, exclusions, location, and the exact search surface being used.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Build a core query with quoted phrases and uppercase Boolean operators where supported
2. Create narrow and broad variants and explain each clause
3. Check syntax and operator support for the named LinkedIn search surface before use
4. Provide a manual refinement loop based on result quality

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Search objective and surface
- Core Boolean string
- Broad/narrow variants
- Operator explanation and refinement steps

## Example prompt

> Build Boolean searches for entry-level cybersecurity analyst roles in Mumbai and remote India, excluding sales jobs.

## Edge cases and failure handling

- LinkedIn product search and Recruiter/Sales Navigator can differ in supported syntax
- Asterisk wildcards and unsupported operators must not be assumed
- Do not scrape results.

## Quality and safety checks

- [ ] Search strings are syntactically plausible for the named surface
- [ ] Exclusions do not accidentally remove relevant synonyms
- [ ] No result volume or recall guarantee.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
