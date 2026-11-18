---
name: linkedin-campaign-performance-diagnostic
description: >-
  the user wants to interpret Campaign Manager results and decide what to test or change
---

# LinkedIn Campaign Performance Diagnostic

**Specialist:** LinkedIn Ads Strategist  
**Category:** Marketing and learning

## When to use this skill

Use this workflow when: the user wants to interpret Campaign Manager results and decide what to test or change Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect date range, objective, spend, impressions, clicks, conversions, leads, qualified leads, attribution settings, audience/creative breakdowns, and campaign changes.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Confirm the metric definitions, attribution window and reporting period
2. Calculate relevant rates and costs with explicit denominators
3. Separate delivery, engagement, conversion and lead quality
4. Compare like-for-like segments and annotate budget or creative changes
5. Recommend prioritized tests while distinguishing correlation from cause

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Data and metric dictionary
- Performance summary with calculations
- Funnel and lead-quality interpretation
- Hypotheses and next experiment

## Example prompt

> Analyze this LinkedIn campaign export. Calculate CTR and cost per qualified lead, note the attribution limitations, and suggest the next experiment.

## Edge cases and failure handling

- Small samples and attribution models can mislead
- Do not infer incremental lift without a valid experiment
- Paid and organic metrics must not be conflated.

## Quality and safety checks

- [ ] All calculations can be reproduced
- [ ] Denominators and windows are stated
- [ ] Causal claims are avoided unless experimentally supported.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
