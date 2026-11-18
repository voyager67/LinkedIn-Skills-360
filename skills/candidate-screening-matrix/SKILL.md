---
name: candidate-screening-matrix
description: >-
  the user wants to build or apply a structured, job-related candidate screening matrix for human review
---

# Candidate Screening Matrix

**Specialist:** Recruiter Assistant  
**Category:** Recruiting

## When to use this skill

Use this workflow when: the user wants to build or apply a structured, job-related candidate screening matrix for human review Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect the approved job description, criteria fixed before review, must-have versus preferred classification, evidence sources, scoring anchors, and any applicable accommodation or jurisdictional constraints. Use anonymized candidate IDs where practical.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Convert essential job requirements into observable, job-related criteria.
2. Define consistent scoring anchors with examples before reviewing candidate materials.
3. Create a matrix that records evidence excerpts, unknowns, and reviewer notes separately from scores.
4. Review each candidate against the same criteria; do not infer missing evidence as lack of ability without a fair opportunity to clarify.
5. Summarize patterns and questions for human reviewers; do not automatically rank, reject, or advance people.

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Role criteria and scoring anchors
- Candidate evidence matrix
- Evidence source and unknowns
- Reviewer questions
- Human review summary and limitations

## Example prompt

> Create a structured screening matrix for this customer support analyst role. Use the same five criteria for every applicant and distinguish missing information from a demonstrated gap.

## Edge cases and failure handling

- Do not use age, sex, race, disability, religion, family status, or other protected traits in evaluation.
- Do not infer personality, culture fit, or commitment from names, photos, gaps, accents, or school prestige.
- If criteria change mid-review, pause and apply a documented, fair process to all candidates.

## Quality and safety checks

- [ ] Criteria are defined before candidate review.
- [ ] Each score is tied to job-relevant evidence.
- [ ] No automated ranking or employment decision is produced.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
