# Contributing

Thanks for helping improve LinkedIn Skills. Contributions should make a workflow more accurate, usable, inclusive, or easier to maintain.

## Before opening an issue

Search existing issues and explain the user problem, audience, expected behavior, and relevant evidence. Do not include private resumes, candidate records, screenshots containing personal data, or credentials.

## Adding or changing a skill

1. Read [the skill-authoring guide](docs/skill-authoring.md), the [quality bar](docs/quality-bar.md), and [privacy and safety rules](docs/privacy-and-safety.md).
2. Keep one skill focused on one workflow. Use lowercase kebab-case directory names.
3. Include valid YAML frontmatter with `name` and a concise, trigger-specific `description`.
4. Document triggers, required inputs, workflow steps, output format, a realistic example, edge cases, and explicit quality/safety checks.
5. Prefer user-provided evidence. Use placeholders for missing metrics; never make them up.
6. Add or update an evaluation case in `evals/cases.json` and an example when it materially helps.
7. Run the validator and unit tests.

## Agent and adapter changes

Agent prompts must define role, boundaries, inputs, output contract, and hand-off behavior. Adapters should explain how to load Markdown skills into a host; do not claim guaranteed compatibility without testing the host version. The core content must remain usable without a specific model provider.

## Pull request checklist

- [ ] The change solves a specific user problem.
- [ ] New claims are supported or clearly marked as assumptions.
- [ ] No private or sensitive data is included.
- [ ] No scraping, unauthorized automation, or automated hiring decisions are introduced.
- [ ] Examples and edge cases are updated.
- [ ] `python scripts/validate_repo.py` passes.
- [ ] `python -m unittest discover -s tests -v` passes.
- [ ] Documentation describes important trade-offs and limitations.

Be respectful, specific, and open to review. See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
