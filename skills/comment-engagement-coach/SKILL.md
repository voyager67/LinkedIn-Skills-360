---
name: comment-engagement-coach
description: >-
  the user wants to write a substantive LinkedIn comment or reply to a post they have read
---

# Thoughtful Comment and Engagement Coach

**Specialist:** Content Strategist  
**Category:** Brand and content

## When to use this skill

Use this workflow when: the user wants to write a substantive LinkedIn comment or reply to a post they have read Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect the post text or a user summary, the user's genuine reaction or experience, intended relationship, and desired length. Avoid requesting account credentials or automated access.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Identify the post's main claim and the kind of contribution that would add value.
2. Ask what the user genuinely agrees with, questions, or can add from experience.
3. Draft a specific response that advances the conversation rather than repeating praise.
4. Check whether any personal example or statistic is accurate and appropriate to share.
5. Offer a concise version and remind the user to review and submit manually.

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Post's central point
- Comment angle
- Draft comment
- Optional shorter version
- Fact and privacy checks

## Example prompt

> Write a thoughtful comment on this post about open-source maintenance. I agree with the point about issue quality and want to add one lesson from my student project.

## Edge cases and failure handling

- If the user has no genuine view or useful contribution, suggest not commenting.
- Do not simulate personal experience the user did not have.
- Avoid repetitive mass comments and engagement bait.

## Quality and safety checks

- [ ] Comment adds a distinct idea or question.
- [ ] No false familiarity or fabricated experience.
- [ ] The user controls whether and where to comment.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
