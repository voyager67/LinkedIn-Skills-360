---
name: recruiter-capacity-prioritization
description: >-
  a recruiting lead wants to prioritize open requisitions against capacity and business urgency
---

# Recruiter Capacity and Requisition Prioritizer

**Specialist:** Recruiter Operations Partner  
**Category:** Recruiting and talent operations

## When to use this skill

Use this workflow when: a recruiting lead wants to prioritize open requisitions against capacity and business urgency Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect open roles, approved priority, aging, hiring complexity, recruiter capacity, target dates, stakeholder responsiveness and dependencies.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Normalize role priority and business impact
2. Estimate workload by complexity and current stage, not raw vacancy count alone
3. Identify blocking dependencies and overloaded owners
4. Propose a transparent prioritization and escalation plan

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Requisition priority matrix
- Capacity and dependency view
- Risks and trade-offs
- Escalation recommendations

## Example prompt

> Help prioritize these eight open roles across two recruiters with different sourcing workloads.

## Edge cases and failure handling

- Do not invent business urgency
- Capacity estimates are directional and should be confirmed
- Avoid using speed targets to lower evaluation quality.

## Quality and safety checks

- [ ] Priority criteria are transparent
- [ ] Workload assumptions are stated
- [ ] Trade-offs are reviewed with stakeholders.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
