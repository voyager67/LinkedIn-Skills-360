"""Structural regression tests for the LinkedIn Skills repository."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

class RepositoryTests(unittest.TestCase):
    def test_skill_count_frontmatter_and_required_sections(self):
        files = sorted((ROOT / "skills").glob("*/SKILL.md"))
        self.assertEqual(len(files), 141)
        names = []
        required = ["## When to use this skill", "## Inputs to collect", "## Workflow", "## Output format", "## Example prompt", "## Edge cases and failure handling", "## Quality and safety checks", "## Completion rule"]
        for path in files:
            content = path.read_text(encoding="utf-8")
            self.assertTrue(content.startswith("---\n"), path)
            name = re.search(r"^name:\s*([a-z0-9-]+)\s*$", content, re.M)
            desc = re.search(r"^description:\s*>-\s*\n\s+(.+)$", content, re.M)
            self.assertIsNotNone(name, path)
            self.assertIsNotNone(desc, path)
            self.assertLessEqual(len(name.group(1)), 64)
            self.assertLessEqual(len(desc.group(1)), 1024)
            self.assertEqual(path.parent.name, name.group(1))
            self.assertTrue(all(section in content for section in required), path)
            names.append(name.group(1))
        self.assertEqual(len(names), len(set(names)))

    def test_agent_and_example_inventory(self):
        agents = list((ROOT / "agents").glob("*.md"))
        examples = [p for p in (ROOT / "examples").glob("*.md") if p.name != "README.md"]
        self.assertEqual(len(agents), 19)
        self.assertEqual(len(examples), 18)
        self.assertTrue((ROOT / "agents/orchestrator.md").is_file())
        self.assertTrue((ROOT / "agents/privacy-and-fairness-reviewer.md").is_file())

    def test_eval_cases_cover_all_skills_once(self):
        skill_names = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
        cases = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))["cases"]
        self.assertEqual({c["skill"] for c in cases}, skill_names)
        self.assertEqual(len(cases), len(skill_names))

    def test_github_description_and_topics(self):
        text = (ROOT / "GITHUB_METADATA.md").read_text(encoding="utf-8")
        match = re.search(r"## Description \(under 350 characters\)\s+(.+?)\s+## Topics", text, re.S)
        self.assertIsNotNone(match)
        self.assertLess(len(match.group(1).strip()), 350)
        topics = re.search(r"## Topics \(20\)\s+(.+?)\s+## Social preview", text, re.S)
        self.assertIsNotNone(topics)
        values = re.findall(r"`([^`]+)`", topics.group(1))
        self.assertEqual(len(values), 20)
        self.assertEqual(len(values), len(set(values)))

    def test_all_skills_are_in_index(self):
        index = (ROOT / "skills/README.md").read_text(encoding="utf-8")
        for path in (ROOT / "skills").glob("*/SKILL.md"):
            self.assertIn(f"`{path.parent.name}`", index)

if __name__ == "__main__":
    unittest.main()
