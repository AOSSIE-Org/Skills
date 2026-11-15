import tempfile
import unittest
from pathlib import Path

from scripts.validate_skills import discover_skill_dirs, validate_repository


class ValidateSkillsTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    def validate(self, content: str | None, directory: str | None = None) -> list[str]:
        directory = directory or f"example-{len(list(self.root.iterdir()))}"
        skill_dir = self.root / directory
        skill_dir.mkdir()
        if content is not None:
            (skill_dir / "SKILL.md").write_text(content, encoding="utf-8")
        return validate_repository(self.root)

    def test_discovers_skills_and_reports_missing_files(self):
        (self.root / "a-skill").mkdir()
        (self.root / "InteractiveSimulation").mkdir()
        (self.root / "public").mkdir()
        (self.root / "scripts").mkdir()
        (self.root / "tests").mkdir()
        (self.root / ".github").mkdir()

        self.assertEqual([p.name for p in discover_skill_dirs(self.root)], ["a-skill"])
        self.assertIn(
            "a-skill/SKILL.md: missing SKILL.md file", validate_repository(self.root)
        )

    def test_accepts_valid_multiline_description(self):
        content = (
            "---\nname: aossie-example\ndescription: >-\n  Valid description.\n---\n"
        )
        self.assertEqual(self.validate(content), [])

    def test_rejects_bad_frontmatter(self):
        cases = [
            ("# no frontmatter\n", "start with ---"),
            ("---\nname: aossie-example\n", "closing ---"),
            ("---\nname: [bad\n---\n", "invalid YAML"),
        ]
        for content, message in cases:
            with self.subTest(message=message):
                errors = self.validate(content)
                self.assertTrue(any(message in error for error in errors))

    def test_requires_nonempty_fields_and_aossie_kebab_case_name(self):
        cases = [
            ("---\nname: ''\ndescription: null\n---\n", "name"),
            ("---\nname: aossie-ok\ndescription: ''\n---\n", "description"),
            ("---\nname: AOSSIE_bad\ndescription: fine\n---\n", "kebab-case"),
        ]
        for content, message in cases:
            with self.subTest(message=message):
                errors = self.validate(content)
                self.assertTrue(any(message in error for error in errors))


if __name__ == "__main__":
    unittest.main()
