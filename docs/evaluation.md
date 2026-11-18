# Evaluation and verification

## What the repository tests

The project distinguishes two different kinds of validation:

1. **Repository checks** verify file structure, skill metadata, required sections, links, catalogue coverage, agent/example counts and evaluation-case coverage.
2. **Model-output evaluation** requires running prompts against a specific model/host, reviewing the resulting outputs against a rubric and reporting the model, date, settings, sample size and failure cases. The current repository does not claim those benchmark runs have been completed.

## Local checks

```bash
python scripts/validate_repo.py
python -m unittest discover -s tests -v
```

Python 3.10+ and the standard library are sufficient. No model SDK, LinkedIn credentials or API key is required for structural checks.

## Evaluation case format

`evals/cases.json` has one illustrative case per skill. A case contains:

- Skill identifier and example input.
- Expected output sections derived from the skill contract.
- Negative constraints such as no fabricated facts, no claimed external action and no unnecessary personal data.
- A note that the case is illustrative, not a measured result.

These are acceptance prompts, not a scientific benchmark or an evaluation of a specific model. They help maintain coverage when a skill changes.

## Recommended model evaluation protocol

For a future measured evaluation, record:

1. Model/provider and exact model identifier.
2. Host, date, system/user prompt context, temperature and relevant settings.
3. Skill version by commit SHA, not an unverified release tag.
4. Number and type of cases, including positive, edge and adversarial/untrusted-input cases.
5. Rubric scores for factual support, task completion, output format, privacy, safety and usability.
6. Human reviewer agreement and disagreements.
7. Failed cases, limitations and reproducible instructions.

Do not report a percentage improvement from a handful of cherry-picked examples. Separate structural test success from model performance and real-world outcomes.

## Domain-specific checks

- Career/profile: factuality, attribution, target-role fit, accessible language and no fabricated achievements.
- Job search: correct search surface, current posting verification, eligibility unknowns and role evidence mapping.
- Content: original value, source/permission checks, voice, claim provenance and no fake engagement.
- Sales: ICP rationale, relevance, opt-out/stop condition and no misleading relationship claims.
- Recruiting: job-related criteria, consistent process, evidence vs inference, candidate privacy, and human decision authority.

## Reporting a failure

Use the bug report template with the skill name, redacted input, expected behaviour, observed issue, host/model context if applicable, and a minimal reproduction. Do not attach private resumes, candidate records, credentials or client data to a public issue.
