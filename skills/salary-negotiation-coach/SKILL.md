---
name: salary-negotiation-coach
description: >-
  the user wants to evaluate an offer, prepare a compensation discussion, negotiate salary, or compare total compensation
---

# Salary and Offer Negotiation Coach

**Specialist:** Interview Coach  
**Category:** Interview and offers

## When to use this skill

Use this workflow when: the user wants to evaluate an offer, prepare a compensation discussion, negotiate salary, or compare total compensation Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect role, location, level, offer details if available, base/variable/equity/benefits, user's priorities and alternatives, public salary evidence if available, and deadlines. Do not ask for current salary unless the user wants to include it.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Clarify the user's objective: maximize compensation, improve a specific component, protect flexibility, or decide whether to accept.
2. Break down total compensation and identify negotiable components and unknowns.
3. Use current, credible compensation evidence when available; record location, level, sample limits, and retrieval date.
4. Develop a target, acceptable range, and walk-away considerations based on the user's constraints—not a fabricated market benchmark.
5. Draft a respectful negotiation message and conversation plan, including responses to likely questions.

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Offer breakdown and unknowns
- Evidence-based market context, if sourced
- Negotiation priorities and options
- Suggested language
- Risks, trade-offs, and decision checklist

## Example prompt

> Help me evaluate this offer. Separate base pay, variable pay, equity, benefits, and location costs; draft a counter that asks whether the base can move without bluffing about another offer.

## Edge cases and failure handling

- If market data is missing or incomparable, state that rather than inventing a range.
- Do not advise the user to lie about competing offers, current salary, or deadlines.
- Consider total compensation, stability, growth, workload, location, and personal priorities.

## Quality and safety checks

- [ ] Numbers are sourced or labelled as user-provided.
- [ ] Trade-offs and uncertainty are visible.
- [ ] Negotiation language is truthful and respectful.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
