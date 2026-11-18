# Skill authoring guide

## Required folder contract

```text
skills/<skill-name>/
└── SKILL.md
```

Every `SKILL.md` starts with YAML frontmatter:

```yaml
---
name: example-skill
description: >-
  Explain what this workflow does and when the model should activate it.
---
```

Use `name` exactly as the folder name. The open Agent Skills convention uses lowercase kebab-case names; keep names concise and descriptions specific. Check the current [Agent Skills specification](https://agentskills.io/) before making format-level changes.

## Required sections

- `## When to use this skill`
- `## Inputs to collect`
- `## Workflow`
- `## Output format`
- `## Example prompt`
- `## Edge cases and failure handling`
- `## Quality and safety checks`
- `## Completion rule`

## Design rules

- One skill should solve one recognizable task. Split it only when triggers, inputs or outputs materially differ.
- State triggers as natural-language user intents. Avoid keyword-only descriptions.
- Ask only for information that changes correctness or the risk profile. Otherwise state assumptions and proceed.
- Make steps operational. “Optimize the profile” is not a step; mapping evidence to a target role and drafting copy is.
- Define the output shape so another agent or human can use it.
- Include edge cases that change the process, not generic disclaimers alone.
- Make factuality, privacy and human approval explicit in the checks.
- Prefer links to supporting templates and docs over copying long reference material into every skill.
- Keep `SKILL.md` focused and below 500 lines where practical; large references belong outside the activated skill.

## Quality bar

A reviewer should be able to answer: Who should use this? What context is needed? What exact steps should the model follow? What should it return? What could go wrong? What must it never claim or do?
