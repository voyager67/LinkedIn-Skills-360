---
name: public-profile-privacy-audit
description: >-
  the user wants to review personal information, visibility, contact details, or discoverability risks on a LinkedIn profile
---

# Public Profile Privacy Audit

**Specialist:** Profile Optimizer  
**Category:** Profile and reputation

## When to use this skill

Use this workflow when: the user wants to review personal information, visibility, contact details, or discoverability risks on a LinkedIn profile Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect the profile fields the user is comfortable sharing, intended audience, threat concerns, public-facing contact preferences, and any information that must remain private.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Inventory exposed identifiers and contact paths
2. Classify information as necessary, optional, or sensitive for the stated goal
3. Recommend least-disclosure edits and audience/visibility settings for the user to check manually
4. Create a before/after checklist without requesting account credentials

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Exposure inventory
- Risk-ranked recommendations
- Manual settings checklist
- Information not needed for the stated goal

## Example prompt

> Review this profile text for privacy oversharing while keeping it useful to recruiters.

## Edge cases and failure handling

- The model cannot inspect live settings without a user-provided view
- Do not request passwords, verification codes, identity documents, or private third-party data.

## Quality and safety checks

- [ ] Only information actually supplied is assessed
- [ ] Recommendations preserve legitimate contact routes
- [ ] No claim is made that settings were changed.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
