# Quality bar

A useful skill is more than a long prompt. It should be focused, testable, honest about what it knows, and safe to use with real career data.

## Required skill contract

Each `SKILL.md` must contain frontmatter (`name`, `description`) and clear sections for triggers, inputs, workflow, output, example, edge cases, quality checks, and completion. Descriptions must identify when the skill should activate and avoid vague “help with career” triggers.

## Evidence rules

- Never invent employers, titles, dates, certifications, projects, skills, metrics, salary ranges, candidate qualifications, or performance results.
- Use `{{placeholder}}` for missing details and state what evidence would fill the gap.
- Separate user-provided facts, externally sourced facts, assumptions, and recommendations.
- Cite time-sensitive company or market research with source name, URL, retrieval date, and what the source supports.
- Explain any score's rubric and limitations. Do not call an internal fit rubric an ATS score or an objective prediction.

## Writing rules

Prefer specific, plain language over generic superlatives. Preserve the user's authentic voice. Avoid keyword stuffing, fake urgency, manipulative outreach, false claims of familiarity, and unsupported “guarantees”.

## Recruiting rules

Use the same job-related criteria for candidates applying to the same role. Define observable evidence and scoring anchors before reviewing applicants. Accommodate equivalent experience and avoid proxies for protected characteristics. Do not rank or reject candidates automatically; humans must review evidence and context.

## Validation

The repository validator checks structure and metadata. Human review and carefully designed evaluation cases are still needed to assess usefulness, factuality, bias, and real-world outcomes. Do not state that passing structural tests proves these broader qualities.
