#!/usr/bin/env python3
"""Validate the LinkedIn Skills repository without third-party dependencies."""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = 141
EXPECTED_AGENTS = 19  # orchestrator + 18 specialist prompts
EXPECTED_EXAMPLES = 18
REQUIRED_ROOT = ["README.md", "LICENSE", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md", "SECURITY.md", "AGENTS.md", "INSTALL.md", "GITHUB_METADATA.md"]
REQUIRED_SECTIONS = [
    "## When to use this skill", "## Inputs to collect", "## Workflow",
    "## Output format", "## Example prompt", "## Edge cases and failure handling",
    "## Quality and safety checks", "## Completion rule",
]

def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)

def validate_local_links() -> int:
    checked = 0
    pattern = re.compile(r"\]\(([^)]+)\)")
    for md in ROOT.rglob("*.md"):
        if any(part in {".git", "node_modules"} for part in md.parts):
            continue
        body = md.read_text(encoding="utf-8")
        for raw in pattern.findall(body):
            target = raw.strip().split()[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            dest = (md.parent / target).resolve()
            try:
                dest.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"link escapes repository: {md.relative_to(ROOT)} -> {raw}")
            if not dest.exists():
                fail(f"broken local Markdown link: {md.relative_to(ROOT)} -> {raw}")
            checked += 1
    return checked

def main() -> int:
    for name in REQUIRED_ROOT:
        if not (ROOT / name).is_file():
            fail(f"missing required root file: {name}")

    skill_files = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if len(skill_files) != EXPECTED_SKILLS:
        fail(f"expected {EXPECTED_SKILLS} skill files, found {len(skill_files)}")
    names = set()
    for path in skill_files:
        body = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()
        if not body.startswith("---\n"):
            fail(f"missing YAML frontmatter: {rel}")
        parts = body.split("---", 2)
        if len(parts) < 3:
            fail(f"malformed frontmatter: {rel}")
        fm = parts[1]
        name_match = re.search(r"^name:\s*([a-z0-9-]+)\s*$", fm, re.M)
        desc_match = re.search(r"^description:\s*>-\s*\n\s+(.+)$", fm, re.M)
        if not name_match or not desc_match:
            fail(f"frontmatter requires name and folded description: {rel}")
        name = name_match.group(1)
        description = desc_match.group(1).strip()
        if not 1 <= len(name) <= 64:
            fail(f"skill name must be 1-64 characters: {rel}")
        if name != path.parent.name:
            fail(f"name/folder mismatch: {rel}")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
            fail(f"invalid skill name: {name}")
        if len(description) > 1024:
            fail(f"skill description exceeds 1024 characters: {rel}")
        if name in names:
            fail(f"duplicate skill name: {name}")
        names.add(name)
        for section in REQUIRED_SECTIONS:
            if section not in body:
                fail(f"missing section {section}: {rel}")
        if len(body.splitlines()) > 500:
            fail(f"skill exceeds 500 lines: {rel}")

    agents = sorted((ROOT / "agents").glob("*.md"))
    if len(agents) != EXPECTED_AGENTS:
        fail(f"expected {EXPECTED_AGENTS} agent prompt files, found {len(agents)}")
    if not (ROOT / "agents/orchestrator.md").is_file():
        fail("missing orchestrator")
    examples = [p for p in (ROOT / "examples").glob("*.md") if p.name != "README.md"]
    if len(examples) != EXPECTED_EXAMPLES:
        fail(f"expected {EXPECTED_EXAMPLES} example prompts, found {len(examples)}")

    cases_path = ROOT / "evals/cases.json"
    cases = json.loads(cases_path.read_text(encoding="utf-8"))["cases"]
    case_names = [case.get("skill") for case in cases]
    if set(case_names) != names or len(case_names) != len(set(case_names)):
        fail("evaluation cases must map one-to-one to all skill names")

    index = (ROOT / "skills/README.md").read_text(encoding="utf-8")
    missing = [name for name in sorted(names) if f"`{name}`" not in index]
    if missing:
        fail(f"skills missing from catalogue: {', '.join(missing)}")

    metadata = (ROOT / "GITHUB_METADATA.md").read_text(encoding="utf-8")
    desc = re.search(r"## Description \(under 350 characters\)\s+(.+?)\s+## Topics", metadata, re.S)
    if not desc or len(desc.group(1).strip()) >= 350:
        fail("GitHub description is missing or is not under 350 characters")
    topic_block = re.search(r"## Topics \(20\)\s+(.+?)\s+## Social preview", metadata, re.S)
    topics = re.findall(r"`([^`]+)`", topic_block.group(1)) if topic_block else []
    if len(topics) != 20 or len(set(topics)) != 20:
        fail(f"expected 20 unique GitHub topics, found {len(topics)}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for phrase in ["141 focused skills", "18 specialist agents", "18 example prompts", "model-agnostic"]:
        if phrase.lower() not in readme.lower():
            fail(f"README is missing inventory statement: {phrase}")

    links_checked = validate_local_links()
    # Scan for live credential patterns and PEM key material; policy words in docs are not secrets.
    secret_patterns = [
        re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
        re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
        re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    ]
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix not in {".md", ".py", ".json", ".csv", ".yml", ".yaml", ".txt"}:
            continue
        content = path.read_text(encoding="utf-8", errors="ignore")
        if any(pattern.search(content) for pattern in secret_patterns):
            fail(f"possible credential/private-key pattern in {path.relative_to(ROOT)}")

    print(f"PASS: {len(skill_files)} skills, {len(agents)} agent prompts, {len(examples)} examples, {len(cases)} evaluation cases, {links_checked} local Markdown links")
    return 0

if __name__ == "__main__":
    sys.exit(main())
