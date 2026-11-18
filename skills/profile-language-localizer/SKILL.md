---
name: profile-language-localizer
description: >-
  the user wants to adapt a LinkedIn profile for another language, region, market, or professional culture
---

# Profile Language Localizer

**Specialist:** Profile Optimizer  
**Category:** Profile and reputation

## When to use this skill

Use this workflow when: the user wants to adapt a LinkedIn profile for another language, region, market, or professional culture Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect source profile text, target language and region, target audience, role level, terms to preserve, and whether a localized or bilingual profile is intended.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Identify terms that need translation versus local equivalents
2. Preserve role seniority, qualifications, dates, and factual meaning
3. Adapt idioms, spelling, and industry terminology for the target market
4. Provide a glossary for ambiguous titles and terms and flag wording needing a native review

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Localized headline and About section
- Localized experience and skills wording
- Terminology decisions
- Human review flags

## Example prompt

> Localize my English LinkedIn About section for professional roles in Germany, keeping the facts and seniority unchanged.

## Edge cases and failure handling

- Job titles and qualifications may not map one-to-one across countries
- For regulated professions, require local credential verification
- Do not infer visa or work authorization.

## Quality and safety checks

- [ ] No new qualification or fluency claim is introduced
- [ ] Localization reads naturally for the named audience
- [ ] Uncertain equivalences are flagged.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
