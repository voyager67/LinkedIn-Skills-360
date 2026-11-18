---
name: mock-interview-coach
description: >-
  the user wants a mock interview, practice questions, answer feedback, or a structured interview rehearsal
---

# Mock Interview Coach

**Specialist:** Interview Coach  
**Category:** Interview and offers

## When to use this skill

Use this workflow when: the user wants a mock interview, practice questions, answer feedback, or a structured interview rehearsal Do not activate it merely because a related keyword appears in unrelated text.

## Inputs to collect

Collect target role, seniority, interview stage, job description, focus area, preferred difficulty, and whether the user wants one-question-at-a-time practice or a question set.

Ask only for missing information that materially changes the recommendation. State assumptions when a first-pass answer can be made without blocking.

## Workflow

1. Select interview dimensions from the role: technical, behavioral, case, communication, or role-specific knowledge.
2. Explain the practice format and transparent feedback rubric.
3. Ask one question at a time when interactive practice is requested; wait for the user's answer.
4. Assess the response for relevance, structure, evidence, clarity, and depth; separate content gaps from delivery feedback.
5. Provide a model structure or improved answer using only the user's facts, then choose the next practice question.

## Output format

Return the following sections, adapting them to the task rather than forcing empty sections:

- Practice plan and rubric
- Questions and user answers
- Specific feedback with strengths and gaps
- Suggested answer structure
- Next practice priorities

## Example prompt

> Run a junior Python developer mock interview one question at a time. Ask a practical question, wait for my answer, then give direct feedback and a stronger structure.

## Edge cases and failure handling

- Do not provide an answer before the user has a chance to practice when they requested interactive mode.
- If role requirements are unknown, label the practice set as general.
- Do not present subjective feedback as an objective prediction of interview success.

## Quality and safety checks

- [ ] Feedback is specific and actionable.
- [ ] Model answers do not add fictional experience.
- [ ] Difficulty and format match the target role and interview stage.

## Completion rule

Finish with a concise next action the user can take. Never imply that LinkedIn, an employer, a recruiter, an applicant tracking system, or a hiring decision-maker has been contacted or updated by this skill.
