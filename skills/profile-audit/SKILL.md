---
name: profile-audit
description: >-
  the user asks for a structured review or score of their LinkedIn profile, or wants to know what to fix first
---

# LinkedIn Profile Audit

**Specialist:** Profile Optimizer  
**Category:** Profile

## When to use this skill

Use this workflow when: the user asks for a structured review or score of their LinkedIn profile, or wants to know what to fix first Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Request the headline, About, current and previous role descriptions, target audience or role, featured section, skills, and any profile sections the user wants reviewed. A public URL is not required; pasted text is preferred.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Confirm the profile's primary goal: hiring, clients, peers, recruiting, or thought leadership.
2. Review first-impression clarity, audience fit, proof, specificity, readability, discoverability, and calls to action using the transparent rubric in `docs/profile-rubric.md`.
3. Separate evidence-backed strengths from gaps caused by missing information; do not penalize a user for sections that are not relevant to their goal.
4. Prioritize fixes by impact and effort. Rewrite only the highest-value sections first and preserve the user's voice.
5. Re-score only the parts changed, explain the rubric, and identify what cannot be improved by copy alone (such as missing proof or recommendations).

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Goal and audience
- Section-by-section review with rubric rationale
- Top five prioritized changes
- Copy-ready rewrites
- Missing evidence and profile changes the user must make

## Example prompt

> Audit this profile for entry-level data analyst roles. Identify the three highest-impact improvements and rewrite my headline and About using only the facts I provide.

## Edge cases and failure handling

- If the user provides only a screenshot, assess visible elements and list what cannot be reviewed.
- If the target audience is unclear, state a provisional goal and offer alternate positioning.
- Never infer a numerical score from LinkedIn's algorithm or claim to predict search ranking.

## Quality and safety checks

- [ ] Every score is explained by an explicit rubric.
- [ ] No credential, metric, recommendation, or achievement is invented.
- [ ] Advice is specific to the stated audience and goal.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
