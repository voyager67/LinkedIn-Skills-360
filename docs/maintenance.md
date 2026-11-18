# Maintenance guide

## Before changing a skill

- Read the complete existing skill and any linked template/reference.
- Identify its trigger, intended user, required inputs and output contract.
- Check for overlap with the existing index; merge or cross-link when a new folder would only duplicate a neighbour.
- Verify any time-sensitive LinkedIn product details against current official material.

## When adding a skill

1. Create `skills/<lowercase-kebab-name>/SKILL.md`.
2. Add YAML frontmatter with matching `name` and a trigger-specific `description`.
3. Include inputs, ordered steps, output format, example prompt, edge cases, quality checks and a clear completion rule.
4. Keep the skill narrow; move long references to `docs/` or `templates/`.
5. Add a matching evaluation case and at least one example or use-case link where useful.
6. Update the coverage map if it materially changes domain coverage.
7. Run validator and tests. Regenerate the index/tree/archive after structural changes.

## When changing agent routing

- Update `agents/orchestrator.md`, `docs/agent-protocol.md` and architecture diagrams together.
- Keep each specialist's mission, skill routes, inputs, workflow, output contract and boundaries aligned.
- Do not add a specialist for a single skill unless it represents a stable responsibility.
- Never claim parallel execution on a host that does not support it.

## Release and version policy

This repository is maintained as a single coherent public state. Do not create version tags or GitHub releases unless the maintainer explicitly changes this policy. Use descriptive commits and the repository's current default branch.

## Review checklist

- Is this a distinct useful workflow, not skill-count inflation?
- Are all current platform claims sourced and dated?
- Are facts, assumptions and estimates clearly separated?
- Is data minimization applied?
- Are high-impact and hiring decisions left to accountable humans?
- Do examples avoid private data and fabricated results?
- Do tests, catalogue, README counts and archive contents match the actual files?
