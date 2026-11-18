---
name: skills-inventory-curator
description: >-
  the user wants to organize, prioritize, validate, or choose LinkedIn skills and endorsements for a target role
---

# Skills Inventory Curator

**Specialist:** Profile Optimizer  
**Category:** Profile

## When to use this skill

Use this workflow when: the user wants to organize, prioritize, validate, or choose LinkedIn skills and endorsements for a target role Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect target roles, current skills list, projects or work evidence, tools used, proficiency descriptions, and skills the user is actively learning.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Build an inventory of technical, domain, transferable, and communication skills.
2. For each skill, record supporting evidence and recency.
3. Prioritize skills by relevance to the target role and strength of evidence rather than popularity alone.
4. Separate demonstrated skills from exposure, coursework, and active learning.
5. Recommend a concise profile list and a plan to strengthen weakly evidenced skills.

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Categorized skills inventory
- Evidence and confidence column
- Priority list for target role
- Skills to remove, verify, or develop
- Suggested proof-building actions

## Example prompt

> Help me choose the most relevant LinkedIn skills for an entry-level cloud engineer profile. I have coursework, one AWS lab project, and basic Linux experience.

## Edge cases and failure handling

- Do not describe a beginner as advanced without evidence.
- If the user has no formal work history, project and coursework evidence remains valid when labeled accurately.
- Do not recommend endorsements from people who have not observed the skill.

## Quality and safety checks

- [ ] Proficiency labels match evidence.
- [ ] Skills are relevant and not duplicated under synonyms.
- [ ] Learning goals are not presented as demonstrated ability.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
