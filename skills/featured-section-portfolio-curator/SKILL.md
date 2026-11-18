---
name: featured-section-portfolio-curator
description: >-
  the user wants to choose, order, or write descriptions for Featured-section links, projects, articles, or portfolio assets
---

# Featured Section and Portfolio Curator

**Specialist:** Profile Optimizer  
**Category:** Profile and reputation

## When to use this skill

Use this workflow when: the user wants to choose, order, or write descriptions for Featured-section links, projects, articles, or portfolio assets Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Ask for target audience, available public assets, proof quality, ownership/permission, link destination, and the action a profile visitor should take.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Rank assets by relevance, credibility, freshness, and accessibility
2. Check that each asset is public and the user has permission to share it
3. Write concise titles and descriptions with context and the user's contribution
4. Propose an order that supports the profile goal and identify missing proof assets

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Recommended asset order
- Copy-ready titles and descriptions
- Permission/accessibility checks
- Missing portfolio asset suggestions

## Example prompt

> Choose the best three Featured items for my internship profile from these project links and explain the order.

## Edge cases and failure handling

- Do not expose client data or unpublished work
- If an asset is team-owned, clarify the user's role and permission before recommending it.

## Quality and safety checks

- [ ] Each asset has a clear audience purpose
- [ ] Links are verified by the user before publishing
- [ ] Claims about authorship and outcomes are accurate.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
