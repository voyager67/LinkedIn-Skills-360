---
name: linkedin-learning-path-curator
description: >-
  the user wants to build a learning path using LinkedIn Learning or other course resources for a target skill or role
---

# LinkedIn Learning Path Curator

**Specialist:** Career Growth Coach  
**Category:** Marketing and learning

## When to use this skill

Use this workflow when: the user wants to build a learning path using LinkedIn Learning or other course resources for a target skill or role Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Ask for target skill/role, current proficiency evidence, timeframe, available hours, budget/licence access and preferred learning format.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Translate the target role into learning objectives
2. Select relevant courses or resources only after checking current availability and prerequisites
3. Sequence learning with practice tasks and portfolio evidence
4. Add checkpoint questions and a plan to replace unavailable or outdated content

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Learning objectives
- Ordered learning path
- Practice and evidence tasks
- Access and currency caveats

## Example prompt

> Create a six-week learning path for a beginner preparing for junior data analyst roles using LinkedIn Learning where available.

## Edge cases and failure handling

- Course catalogues and licence entitlements vary by region and account
- Course completion is not proof of job proficiency
- Verify course dates and prerequisites.

## Quality and safety checks

- [ ] Each resource supports a learning objective
- [ ] Practice artifacts accompany course study
- [ ] No job guarantee is implied.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
