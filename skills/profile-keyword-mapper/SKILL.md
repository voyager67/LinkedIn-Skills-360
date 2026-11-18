---
name: profile-keyword-mapper
description: >-
  the user wants to identify and naturally map role, skill, or industry keywords into their LinkedIn profile using a target job or audience
---

# Profile Keyword Mapper

**Specialist:** Profile Optimizer  
**Category:** Profile

## When to use this skill

Use this workflow when: the user wants to identify and naturally map role, skill, or industry keywords into their LinkedIn profile using a target job or audience Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Ask for one or more target job descriptions, the current profile text, confirmed skills, preferred role level, and any terms the user must not claim.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Extract repeated role language, tools, domain terms, qualifications, and outcome verbs from the supplied job descriptions.
2. Group terms into must-have, useful, context-specific, and unsupported categories.
3. Map supported terms to existing profile evidence and identify proof gaps.
4. Recommend where each supported term belongs: headline, About, experience, projects, or skills.
5. Draft natural wording and a gap list; never add unsupported skills just because they appear in a job description.

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Keyword groups with source context
- Evidence mapping table
- Suggested profile placement
- Unsupported terms to learn or evidence
- Draft wording

## Example prompt

> Compare these three product analyst job descriptions with my profile. Find overlapping skills I can truthfully feature and gaps I should address.

## Edge cases and failure handling

- If postings conflict, show differences rather than treating all keywords as universal.
- Do not imply keyword frequency reveals LinkedIn's ranking algorithm.
- If no job descriptions are provided, ask for a target role and label the initial list as provisional.

## Quality and safety checks

- [ ] Every recommended keyword maps to real evidence or is marked as a gap.
- [ ] No keyword stuffing or misleading skill claims.
- [ ] Recommendations distinguish job-description language from verified platform ranking factors.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
