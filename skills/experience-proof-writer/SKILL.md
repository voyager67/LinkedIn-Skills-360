---
name: experience-proof-writer
description: >-
  the user wants to rewrite LinkedIn experience entries, project descriptions, internships, volunteering, or achievement bullets
---

# Experience and Achievement Writer

**Specialist:** Profile Optimizer  
**Category:** Profile

## When to use this skill

Use this workflow when: the user wants to rewrite LinkedIn experience entries, project descriptions, internships, volunteering, or achievement bullets Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect role or project context, dates, responsibilities, actions personally performed, tools used, scope, outcomes, collaborators, and any measured results. Ask which details are confidential.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Separate responsibilities, actions, deliverables, and outcomes.
2. Identify the user's individual contribution versus team outcomes.
3. Convert relevant material into concise action-and-evidence bullets using a situation/action/result pattern where appropriate.
4. Use metrics only when supplied and explain ambiguous attribution; otherwise describe observable deliverables or scope.
5. Create a concise role summary and a longer version where different profile layouts require it.

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Reconstructed role/project summary
- 2–5 evidence-based bullets
- Missing proof questions
- Optional short version for profile display

## Example prompt

> Rewrite my campus hackathon project for LinkedIn Experience. I built the frontend and integrated speech input; the team built the backend. Keep my contribution distinct from the team's work.

## Edge cases and failure handling

- For team projects, label team-level outcomes and the user's contribution separately.
- For confidential work, generalize client and internal system details without making the claim misleading.
- For no professional experience, use coursework, clubs, volunteering, and projects as their real categories.

## Quality and safety checks

- [ ] Attribution is accurate.
- [ ] Numbers and outcomes are sourced or explicitly placeholders.
- [ ] Bullets describe evidence rather than inflated adjectives.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
