---
name: skills-gap-and-learning-plan
description: >-
  the user wants to compare their current skills with a target LinkedIn role or job description and plan learning
---

# Skills Gap and Learning Plan

**Specialist:** Job Hunter  
**Category:** Job search and career operations

## When to use this skill

Use this workflow when: the user wants to compare their current skills with a target LinkedIn role or job description and plan learning Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect target posting(s), self-assessed skill evidence, projects, available time, budget constraints, and preferred learning style.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Extract required and preferred competencies from the role
2. Classify each skill as demonstrated, adjacent, beginner, or unknown using evidence
3. Prioritize gaps by job relevance and learning effort
4. Design practice tasks that produce portfolio evidence and set reassessment criteria

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Skill gap matrix
- Priority learning sequence
- Practice projects and evidence outputs
- Reassessment checklist

## Example prompt

> Compare my current Python, SQL and Excel skills to these analyst jobs and create a 6-week learning plan.

## Edge cases and failure handling

- Do not equate course completion with proficiency
- Do not label skills as absent without checking evidence
- Avoid endorsing a paid provider without comparison.

## Quality and safety checks

- [ ] Each proficiency label has an evidence rationale
- [ ] Plan fits time constraints
- [ ] Outcomes are demonstrable.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
