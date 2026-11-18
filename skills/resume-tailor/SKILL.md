---
name: resume-tailor
description: >-
  the user wants to tailor a resume to a specific job description or improve its parsing and readability for applicant tracking systems
---

# Resume Tailoring and ATS Readability

**Specialist:** Job Hunter  
**Category:** Search and applications

## When to use this skill

Use this workflow when: the user wants to tailor a resume to a specific job description or improve its parsing and readability for applicant tracking systems Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect the target job description, current resume, target country/industry if relevant, preferred length, and facts that must remain unchanged. Ask the user to remove unnecessary personal identifiers.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Extract core responsibilities, qualifications, tools, and role language from the posting.
2. Map each requirement to truthful evidence in the resume and identify missing proof.
3. Prioritize relevant experience, projects, and skills; rewrite bullets for clarity and direct relevance.
4. Use a simple, readable structure with standard headings and consistent dates; avoid layout tricks that may interfere with parsing.
5. Return a change log and a validation checklist. Explain that ATS products and employer configurations vary.

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Target-role requirement map
- Revised resume content by section
- Keyword coverage supported by evidence
- Change log
- ATS-readability checklist and unresolved gaps

## Example prompt

> Tailor my attached resume for this data analyst internship. Keep all dates and facts unchanged, improve project bullets, and explain any keyword you decide not to include.

## Edge cases and failure handling

- Never add keywords as skills without evidence.
- If the user requests a one-page resume but evidence is dense, explain the trade-off rather than silently deleting important facts.
- Do not promise to pass ATS or claim compatibility with every ATS vendor.

## Quality and safety checks

- [ ] All facts, dates, titles, and metrics are preserved or explicitly queried.
- [ ] No hidden text, keyword stuffing, or deceptive formatting.
- [ ] The final version remains readable to a human reviewer.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
