---
name: application-question-response-coach
description: >-
  the user wants to answer application form questions about motivation, experience, eligibility, or skills
---

# Job Application Question Coach

**Specialist:** Job Hunter  
**Category:** Job search and career operations

## When to use this skill

Use this workflow when: the user wants to answer application form questions about motivation, experience, eligibility, or skills Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect the exact question, job description, resume/evidence, truthful eligibility details, word or character limit, and any required disclosure.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Classify what the question is testing
2. Map answer claims to evidence in the user's materials
3. Draft a direct response within the stated limit
4. Flag legal or eligibility questions that require the user to answer personally and accurately

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Question intent
- Evidence map
- Copy-ready answer within limit
- Unresolved facts or disclosures

## Example prompt

> Answer “Why do you want to work here?” using my project background and this job description, within 150 words.

## Edge cases and failure handling

- Do not guess work authorization, disability, criminal-history, or demographic disclosures
- If a question has legal significance, do not advise concealment or fabrication.

## Quality and safety checks

- [ ] All biographical facts are verified by the user
- [ ] Length is checked
- [ ] The answer addresses the actual question.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
