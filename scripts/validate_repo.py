#!/usr/bin/env python3
"""Validate inventory, catalogues, deployment boundaries, links and repository hygiene."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = 141
EXPECTED_AGENTS = 19
EXPECTED_EXAMPLES = 18
REQUIRED_ROOT = [
    "README.md", "LICENSE", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md",
    "SECURITY.md", "AGENTS.md", "INSTALL.md",
]
OWNER_ONLY_FILES = {"FILE_TREE.txt", "GITHUB_METADATA.md", "SOCIAL_PREVIEW.md", "PAGES.md"}
REQUIRED_SECTIONS = [
    "## When to use this skill", "## Inputs to collect", "## Workflow",
    "## Output format", "## Example prompt", "## Edge cases and failure handling",
    "## Quality and safety checks", "## Completion rule",
]
TEXT_SUFFIXES = {
    ".md", ".py", ".json", ".csv", ".yml", ".yaml", ".txt",
    ".html", ".js", ".css", ".svg",
}


def fail(message: str) -> None:
    print("FAIL: " + message)
    raise SystemExit(1)


def validate_markdown_links() -> int:
    count = 0
    pattern = re.compile(r"\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        if any(part in {".git", "node_modules", "__pycache__"} for part in path.parts):
            continue
        body = path.read_text(encoding="utf-8")
        for raw in pattern.findall(body):
            target = raw.strip().split()[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            destination = (path.parent / target).resolve()
            try:
                destination.relative_to(ROOT.resolve())
            except ValueError:
                fail("Markdown link escapes repository: " + str(path.relative_to(ROOT)) + " -> " + raw)
            if not destination.exists():
                fail("broken Markdown link: " + str(path.relative_to(ROOT)) + " -> " + raw)
            count += 1
    return count


def validate_catalogues(skill_names: set[str], agent_names: set[str]) -> tuple[int, int]:
    skills = json.loads((ROOT / "site/skills/catalog.json").read_text(encoding="utf-8"))
    agents = json.loads((ROOT / "site/agents/catalog.json").read_text(encoding="utf-8"))

    skill_slugs = [item.get("slug") for item in skills]
    if len(skills) != len(skill_names) or set(skill_slugs) != skill_names or len(skill_slugs) != len(set(skill_slugs)):
        fail("website skill catalogue must map one-to-one to every SKILL.md")
    for item in skills:
        slug = item["slug"]
        if item.get("path") != "../skills/" + slug + "/SKILL.md":
            fail("incorrect website skill path: " + slug)
        if not (ROOT / "skills" / slug / "SKILL.md").is_file():
            fail("website catalogue points to missing skill: " + slug)
        if not item.get("description") or not item.get("github", "").startswith("https://github.com/"):
            fail("incomplete website skill entry: " + slug)

    agent_slugs = [item.get("slug") for item in agents]
    if len(agents) != len(agent_names) or set(agent_slugs) != agent_names or len(agent_slugs) != len(set(agent_slugs)):
        fail("website agent catalogue must map one-to-one to every agent prompt")
    descriptions = []
    for item in agents:
        slug = item["slug"]
        if not (ROOT / "agents" / (slug + ".md")).is_file():
            fail("website agent catalogue points to missing prompt: " + slug)
        description = item.get("description", "").strip()
        if not description or description == "A portable specialist role prompt for a bounded professional workflow.":
            fail("agent entry needs a distinct mission summary: " + slug)
        if not item.get("github", "").startswith("https://github.com/"):
            fail("missing agent source URL: " + slug)
        descriptions.append(description)
    if len(set(descriptions)) != len(descriptions):
        fail("agent catalogue descriptions are not distinct")
    return len(skills), len(agents)


def validate_workflows() -> None:
    if (ROOT / ".github/workflows/static.yml").exists():
        fail("remove legacy static.yml; it uploads the repository root")
    pages_path = ROOT / ".github/workflows/pages.yml"
    validate_path = ROOT / ".github/workflows/validate.yml"
    if not pages_path.is_file() or not validate_path.is_file():
        fail("required Pages and validation workflows are missing")

    pages = pages_path.read_text(encoding="utf-8")
    if not re.search(r"^\s+source:\s*\./site\s*$", pages, re.M):
        fail("Jekyll build must use site/ as its source")
    if not re.search(r"^\s+path:\s*\./_site\s*$", pages, re.M):
        fail("Pages workflow must upload only the generated _site/ directory")
    if "actions/jekyll-build-pages@" not in pages:
        fail("Pages workflow must build the website with the official Jekyll action")
    if "cancel-in-progress: false" not in pages:
        fail("Pages deploy should not cancel an in-progress publish")

    for path in (pages_path, validate_path):
        body = path.read_text(encoding="utf-8")
        actions = re.findall(r"^\s*uses:\s*([^\s]+)", body, re.M)
        if not actions:
            fail("no actions found in " + str(path.relative_to(ROOT)))
        for action in actions:
            if "@" not in action or not re.fullmatch(r"[0-9a-f]{40}", action.rsplit("@", 1)[1]):
                fail("GitHub Action is not pinned to a full commit SHA: " + action)

    issue_config = ROOT / ".github/ISSUE_TEMPLATE/config.yml"
    body = issue_config.read_text(encoding="utf-8")
    if "<YOUR_GITHUB_OWNER>" in body or "linkedin-skills/blob/main" in body:
        fail("issue template contains a placeholder or stale security URL")
    expected = "https://github.com/voyager67/LinkedIn-Skills-360/blob/main/SECURITY.md"
    if expected not in body:
        fail("issue template security link must point to this repository")


def scan_text_for_secrets() -> int:
    patterns = [
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
        re.compile(r"\bgithub_pat_[A-Za-z0-9_]{30,}\b"),
        re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    ]
    scanned = 0
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if any(part in {".git", "__pycache__", "node_modules"} for part in path.parts):
            continue
        content = path.read_text(encoding="utf-8", errors="ignore")
        scanned += 1
        for pattern in patterns:
            if pattern.search(content):
                fail("possible credential/private-key pattern in " + str(path.relative_to(ROOT)))
    return scanned


def main() -> int:
    for name in REQUIRED_ROOT:
        if not (ROOT / name).is_file():
            fail("missing required root file: " + name)
    for name in OWNER_ONLY_FILES:
        if (ROOT / name).exists():
            fail("owner-only/generated housekeeping file is still present: " + name)

    skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if len(skill_files) != EXPECTED_SKILLS:
        fail("expected " + str(EXPECTED_SKILLS) + " skills; found " + str(len(skill_files)))
    skill_names: set[str] = set()
    for path in skill_files:
        body = path.read_text(encoding="utf-8")
        if not body.startswith("---\n") or len(body.split("---", 2)) < 3:
            fail("missing or malformed YAML frontmatter: " + str(path.relative_to(ROOT)))
        frontmatter = body.split("---", 2)[1]
        name_match = re.search(r"^name:\s*([a-z0-9-]+)\s*$", frontmatter, re.M)
        description_match = re.search(r"^description:\s*>-\s*\n\s+(.+)$", frontmatter, re.M)
        if not name_match or not description_match:
            fail("frontmatter needs name and folded description: " + str(path.relative_to(ROOT)))
        name = name_match.group(1)
        description = description_match.group(1).strip()
        if name != path.parent.name or not 1 <= len(name) <= 64:
            fail("skill name/folder mismatch: " + str(path.relative_to(ROOT)))
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            fail("invalid skill name: " + name)
        if len(description) > 1024:
            fail("skill description exceeds 1024 characters: " + name)
        if name in skill_names:
            fail("duplicate skill name: " + name)
        skill_names.add(name)
        for section in REQUIRED_SECTIONS:
            if section not in body:
                fail("missing section " + section + " in " + name)
        if len(body.splitlines()) > 500:
            fail("skill exceeds 500 lines: " + name)

    agent_files = sorted((ROOT / "agents").glob("*.md"))
    if len(agent_files) != EXPECTED_AGENTS:
        fail("expected " + str(EXPECTED_AGENTS) + " agent prompts; found " + str(len(agent_files)))
    agent_names = {path.stem for path in agent_files}
    if "orchestrator" not in agent_names:
        fail("missing orchestrator")

    example_files = [p for p in (ROOT / "examples").glob("*.md") if p.name != "README.md"]
    if len(example_files) != EXPECTED_EXAMPLES:
        fail("expected " + str(EXPECTED_EXAMPLES) + " examples; found " + str(len(example_files)))

    cases = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))["cases"]
    case_names = [case.get("skill") for case in cases]
    if set(case_names) != skill_names or len(case_names) != len(set(case_names)):
        fail("evaluation cases must map one-to-one to all skills")

    index = (ROOT / "skills/README.md").read_text(encoding="utf-8")
    missing = [name for name in skill_names if chr(96) + name + chr(96) not in index]
    if missing:
        fail("skills missing from Markdown index: " + ", ".join(sorted(missing)))

    site_skills, site_agents = validate_catalogues(skill_names, agent_names)
    validate_workflows()
    readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    for phrase in ("141 focused skills", "18 specialist agents", "18 example prompts", "model-agnostic"):
        if phrase not in readme:
            fail("README missing inventory statement: " + phrase)

    links = validate_markdown_links()
    scanned = scan_text_for_secrets()
    print(
        "PASS: " + str(len(skill_files)) + " skills, " + str(len(agent_files)) +
        " agents, " + str(len(example_files)) + " examples, " + str(len(cases)) +
        " evaluation cases, " + str(site_skills) + " website skills, " +
        str(site_agents) + " website agents, " + str(links) +
        " local Markdown links, " + str(scanned) + " text files secret-scanned"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
