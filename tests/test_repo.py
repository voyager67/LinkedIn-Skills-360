"""Structural and security-regression tests for LinkedIn Skills 360."""
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
        required = [
            "## When to use this skill", "## Inputs to collect", "## Workflow",
            "## Output format", "## Example prompt", "## Edge cases and failure handling",
            "## Quality and safety checks", "## Completion rule",
        ]
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
        self.assertEqual({case["skill"] for case in cases}, skill_names)
        self.assertEqual(len(cases), len(skill_names))

    def test_all_skills_are_in_markdown_index(self):
        index = (ROOT / "skills/README.md").read_text(encoding="utf-8")
        for path in (ROOT / "skills").glob("*/SKILL.md"):
            self.assertIn(chr(96) + path.parent.name + chr(96), index)

    def test_website_catalogues_match_source_files(self):
        skill_names = {p.parent.name for p in (ROOT / "skills").glob("*/SKILL.md")}
        skills = json.loads((ROOT / "site/skills/catalog.json").read_text(encoding="utf-8"))
        self.assertEqual({item["slug"] for item in skills}, skill_names)
        self.assertEqual(len(skills), 141)
        for item in skills:
            self.assertTrue((ROOT / "skills" / item["slug"] / "SKILL.md").is_file())

        agent_names = {p.stem for p in (ROOT / "agents").glob("*.md")}
        agents = json.loads((ROOT / "site/agents/catalog.json").read_text(encoding="utf-8"))
        self.assertEqual({item["slug"] for item in agents}, agent_names)
        self.assertEqual(len(agents), 19)
        descriptions = [item["description"] for item in agents]
        self.assertEqual(len(descriptions), len(set(descriptions)))
        self.assertTrue(all(d and d != "A portable specialist role prompt for a bounded professional workflow." for d in descriptions))

    def test_pages_workflow_is_scoped_and_actions_are_pinned(self):
        pages = (ROOT / ".github/workflows/pages.yml").read_text(encoding="utf-8")
        self.assertIn("source: ./site", pages)
        self.assertIn("path: ./_site", pages)
        self.assertIn("actions/jekyll-build-pages@", pages)
        self.assertNotRegex(pages, r"(?m)^\s*path:\s*[\"']?\.[\"']?\s*$")
        self.assertFalse((ROOT / ".github/workflows/static.yml").exists())
        validate = (ROOT / ".github/workflows/validate.yml").read_text(encoding="utf-8")
        for workflow in (pages, validate):
            actions = re.findall(r"(?m)^\s*uses:\s*([^\s]+)", workflow)
            self.assertTrue(actions)
            for action in actions:
                self.assertRegex(action, r"@[0-9a-f]{40}(?:\s+# .+)?$")
        self.assertIn("cancel-in-progress: false", pages)
        self.assertNotIn("actions: read", pages)

    def test_jekyll_site_has_shared_layouts_and_project_baseurl(self):
        config = (ROOT / "site/_config.yml").read_text(encoding="utf-8")
        self.assertIn('baseurl: "/LinkedIn-Skills-360"', config)
        self.assertIn("strict_front_matter: true", config)
        self.assertTrue((ROOT / "site/_layouts/default.html").is_file())
        self.assertTrue((ROOT / "site/_includes/header.html").is_file())
        self.assertTrue((ROOT / "site/_includes/footer.html").is_file())
        for page in ["index.html", "skills/index.html", "agents/index.html",
                     "use-cases/index.html", "docs/index.html", "404.html"]:
            content = (ROOT / "site" / page).read_text(encoding="utf-8")
            self.assertTrue(content.startswith("---\n"), page)
            self.assertIn("layout: default", content, page)
        self.assertTrue((ROOT / "site/sitemap.xml").is_file())
        self.assertTrue((ROOT / "site/robots.txt").is_file())

    def test_issue_template_has_real_security_contact(self):
        text = (ROOT / ".github/ISSUE_TEMPLATE/config.yml").read_text(encoding="utf-8")
        self.assertNotIn("<YOUR_GITHUB_OWNER>", text)
        self.assertIn("https://github.com/voyager67/LinkedIn-Skills-360/blob/main/SECURITY.md", text)

    def test_owner_only_housekeeping_files_are_not_shipped(self):
        for name in ["FILE_TREE.txt", "GITHUB_METADATA.md", "SOCIAL_PREVIEW.md", "PAGES.md"]:
            self.assertFalse((ROOT / name).exists(), name)
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertNotIn("PAGES.md", readme)
        self.assertNotIn("GITHUB_METADATA.md", readme)


if __name__ == "__main__":
    unittest.main()
