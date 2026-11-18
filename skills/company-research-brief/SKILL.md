---
name: company-research-brief
description: >-
  the user wants to research an employer, team, product, culture, business model, or public company context before applying or interviewing
---

# Company Research Brief

**Specialist:** Research Analyst  
**Category:** Interview and offers

## When to use this skill

Use this workflow when: the user wants to research an employer, team, product, culture, business model, or public company context before applying or interviewing Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect company name, role or team, geography, purpose of research, known links, and topics the user wants answered. Use public sources only.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Identify authoritative sources: company site, careers page, product documentation, filings, reputable reporting, and public job postings.
2. Collect current facts with publication or retrieval dates and direct source links.
3. Summarize business model, products, customers, strategy, team context, role signals, and recent developments relevant to the question.
4. Separate sourced facts from interpretations and unknowns; note conflicting or stale information.
5. Produce role-specific questions and verification items for the user.

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Executive summary
- Company and product overview
- Current verified signals with links and dates
- Role/team implications
- Open questions and risks
- Interview questions to ask

## Example prompt

> Research this company before my software engineering interview. Use current public sources, prioritize official material, and clearly label your interpretation of the engineering culture as inference.

## Edge cases and failure handling

- If current browsing is unavailable, do not present memory as current fact.
- Do not infer private employee sentiment from isolated anecdotes.
- For public companies, distinguish company disclosures from analyst opinion.

## Quality and safety checks

- [ ] Time-sensitive facts have source links and dates.
- [ ] Facts and interpretation are visually distinguished.
- [ ] No confidential or scraped personal information is used.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
