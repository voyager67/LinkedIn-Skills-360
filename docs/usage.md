# Usage guide

## Start with one workflow

1. Search [`../skills/README.md`](../skills/README.md) for the task.
2. Read that skill's `SKILL.md` and any linked support file.
3. Provide only the inputs needed and label supplied evidence.
4. Ask for the specified output format.
5. Verify facts and manually perform any external action.

## Choose the right skill

Use the [coverage map](coverage-map.md) for routes by audience and LinkedIn surface. A common mistake is loading multiple overlapping skills into one prompt. Start with the smallest task and add a second skill only if there is a real dependency.

## Use the orchestrator

Give `agents/orchestrator.md` the user's goal, relevant evidence, constraints and desired output. The orchestrator routes to the smallest useful set of agents and skills. If the AI host cannot delegate, the steps are followed sequentially, not as a fictitious parallel run.

## Research tasks

When browsing is available and current information matters:

- Prioritize official company, LinkedIn, government, university or product documentation.
- Include the URL and publication or retrieval date.
- Separate the source's statement from the model's interpretation.
- Call out stale pages, conflicting reports and sample limitations.
- Never imply access to private LinkedIn data.

## Using trackers and templates

Copy a blank template into a private workspace before entering real personal or candidate information. Do not commit completed tracker rows or candidate matrices to the public repository. Use pseudonymous IDs where possible and follow organizational retention rules.

## For a multi-stage job search

Start with target-role definition and discovery. Review role fit against your evidence before tailoring application material. Keep a local tracker. Prepare interviews from verified company sources and real examples. Compare actual offer terms and your own priorities; do not treat the model's weighting as a decision.

## For recruiting

Align role outcomes and criteria before sourcing. Define structured interview stages and anchors before reviewing candidates. Keep candidate communications accurate and timely. Use aggregate process metrics to improve operations, not to outsource individual hiring decisions to a model.
