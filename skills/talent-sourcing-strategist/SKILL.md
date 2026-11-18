---
name: talent-sourcing-strategist
description: >-
  the user wants an ethical sourcing strategy, target talent profile, search plan, or candidate outreach funnel for a role
---

# Talent Sourcing Strategist

**Specialist:** Recruiter Assistant  
**Category:** Recruiting

## When to use this skill

Use this workflow when: the user wants an ethical sourcing strategy, target talent profile, search plan, or candidate outreach funnel for a role Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect job description, must-have competencies, location, level, acceptable adjacent backgrounds, sourcing channels already authorized, and constraints on data use.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Translate the role into observable competencies and evidence signals.
2. Identify relevant talent pools and adjacent experience paths without using protected-trait proxies.
3. Build search concepts and manual research approaches using authorized sources and platform tools.
4. Define a respectful outreach rationale and a manageable review workflow.
5. Create a sourcing log schema that records role-related evidence and source provenance, not unnecessary personal data.

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Target talent profile
- Competency and evidence signals
- Adjacent talent pools
- Search concepts and channels
- Outreach rationale
- Minimal sourcing log schema

## Example prompt

> Develop a sourcing plan for a junior cybersecurity analyst. Include adjacent backgrounds such as IT support and lab projects, and avoid using university prestige as a proxy for ability.

## Edge cases and failure handling

- Do not scrape LinkedIn, circumvent access controls, or bulk collect contact data.
- If a channel's terms or data permissions are unclear, require human/legal review before use.
- Do not use sensitive characteristics or proxies to narrow the candidate pool.

## Quality and safety checks

- [ ] Search criteria are tied to job requirements.
- [ ] Sourcing uses authorized channels and minimization.
- [ ] The plan broadens access to equivalent evidence rather than narrowing on prestige.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
