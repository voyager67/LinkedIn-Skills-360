---
name: career-switch-narrative
description: >-
  the user wants to explain a career change, translate transferable skills, or reposition their experience for a different industry or role
---

# Career Switch Narrative Builder

**Specialist:** Career Transition Advisor  
**Category:** Career-stage variants

## When to use this skill

Use this workflow when: the user wants to explain a career change, translate transferable skills, or reposition their experience for a different industry or role Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect current and target roles, reason for transition if the user wishes to share it, prior responsibilities, transferable evidence, training, projects, and role requirements.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Identify overlap between the target role's requirements and the user's demonstrated capabilities.
2. Separate transferable strengths from skills that require new evidence.
3. Build a concise transition story: prior foundation, insight or motivation, deliberate preparation, and target contribution.
4. Adapt the story for headline, About, resume summary, interviews, and outreach.
5. Create a staged proof plan that reduces the biggest credibility gaps.

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Transferable skill map
- Transition narrative
- Targeted profile/resume wording
- Skill and evidence gaps
- 30/60/90-day proof plan

## Example prompt

> Help me move from customer support into business analysis. Map my problem-solving, documentation, and stakeholder work to analyst requirements, and identify what I still need to learn.

## Edge cases and failure handling

- The user does not need to disclose personal reasons for switching.
- Do not claim direct experience in the target role when only adjacent experience exists.
- If the switch is not yet validated, propose small experiments before a full repositioning.

## Quality and safety checks

- [ ] Transferability is linked to concrete examples.
- [ ] Target-role gaps are acknowledged rather than hidden.
- [ ] The narrative remains truthful and forward-looking.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
