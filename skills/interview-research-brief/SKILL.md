---
name: interview-research-brief
description: >-
  the user wants to prepare for an interview using a job description, company context, role expectations, or likely interview themes
---

# Interview Preparation Research Brief

**Specialist:** Interview Coach  
**Category:** Interview and offers

## When to use this skill

Use this workflow when: the user wants to prepare for an interview using a job description, company context, role expectations, or likely interview themes Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect job description, company name, interview stage, role level, interviewer details only if publicly and appropriately provided, and the user's resume or relevant examples.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Extract competencies and responsibilities from the job description.
2. Research current company facts only from reliable public sources when browsing is available; record source dates and separate fact from inference.
3. Map likely interview themes to the role requirements without claiming access to the actual interview questions.
4. Identify stories, technical topics, questions for the interviewer, and potential gaps.
5. Create a focused preparation plan for the user's available time.

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Role and company context
- Competency map
- Likely question themes, clearly labelled as hypotheses
- Candidate evidence to prepare
- Questions to ask
- Timed preparation plan
- Sources and retrieval dates

## Example prompt

> Prepare a research brief for a first-round backend engineer interview using this job description and public company information. Separate verified facts from your interview-topic hypotheses.

## Edge cases and failure handling

- If current research is unavailable, label company details as user-supplied or needing verification.
- Do not claim to know confidential interview questions or private interviewer information.
- If the job posting is vague, show uncertainty and recommend asking the recruiter for format details.

## Quality and safety checks

- [ ] Current facts have sources and dates.
- [ ] Hypotheses are not presented as insider knowledge.
- [ ] Preparation is tailored to role requirements and candidate evidence.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
