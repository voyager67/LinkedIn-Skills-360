---
name: job-fit-analyzer
description: >-
  the user wants to compare a job description with their resume or experience and decide whether an application is worth prioritizing
---

# Job Fit Analyzer

**Specialist:** Job Hunter  
**Category:** Search and applications

## When to use this skill

Use this workflow when: the user wants to compare a job description with their resume or experience and decide whether an application is worth prioritizing Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Request the full job description, resume or relevant experience, target location, work authorization constraints where relevant, and user priorities. Redact direct identifiers if unnecessary.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Extract responsibilities, required qualifications, preferred qualifications, seniority, and logistics from the posting.
2. Map each requirement to explicit evidence in the user's materials.
3. Classify each requirement as demonstrated, adjacent/transferable, missing, unclear, or potentially disqualifying.
4. Apply a transparent user-defined rubric only if requested; show weighting and uncertainty.
5. Recommend apply, investigate, or deprioritize, with gap-closing questions and tailored evidence to foreground.

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Role summary and hard constraints
- Requirement-to-evidence matrix
- Strengths, gaps, and unknowns
- Optional transparent fit rubric
- Apply / investigate / deprioritize recommendation

## Example prompt

> Compare my resume to this junior ML engineer posting. Tell me which requirements I can demonstrate, which are gaps, and whether I should apply despite lacking a production ML internship.

## Edge cases and failure handling

- Do not interpret an unknown requirement as a failure without checking whether it is mandatory.
- Do not call the result an ATS score or predict employer decisions.
- If the job description is incomplete or generic, state the limits of the comparison.

## Quality and safety checks

- [ ] Each match is tied to an evidence excerpt.
- [ ] Missing and unknown are not conflated.
- [ ] Recommendation reflects the user's stated priorities and hard constraints.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
