---
name: portfolio-project-story
description: >-
  the user wants to explain a portfolio project, open-source contribution, case study, hackathon, or side project for LinkedIn or applications
---

# Portfolio and Project Storyteller

**Specialist:** Career Transition Advisor  
**Category:** Career-stage variants

## When to use this skill

Use this workflow when: the user wants to explain a portfolio project, open-source contribution, case study, hackathon, or side project for LinkedIn or applications Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect project goal, user problem, scope, team composition, user's contribution, technical choices, trade-offs, links, results, limitations, and what can be shared publicly.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Clarify the problem and intended user or audience.
2. Separate the user's work from teammates' work and external dependencies.
3. Explain architecture or process, key decisions, and constraints in accessible language.
4. Describe results only with actual evidence; include limitations and lessons.
5. Create versions for LinkedIn, resume, portfolio README, and interview discussion as needed.

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Project one-line summary
- Problem and approach
- Individual contribution
- Evidence and outcomes
- Trade-offs and limitations
- Platform-specific versions

## Example prompt

> Turn my open-source CLI project into a LinkedIn project entry and a resume bullet. Keep the fact that it is a prototype visible and don't invent downloads or users.

## Edge cases and failure handling

- For collaborative projects, do not claim team features as sole personal work.
- If metrics are unavailable, highlight shipped artifacts, tests, demo, or design decisions.
- Check licenses, secrets, and confidential data before making repository links public.

## Quality and safety checks

- [ ] Individual contribution is explicit.
- [ ] Outcomes and project maturity are accurately labelled.
- [ ] Technical claims and links can be verified.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
