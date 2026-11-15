"""Check top-level AOSSIE skill metadata."""

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
NON_SKILL_DIRS = {"InteractiveSimulation", "public", "scripts", "tests"}
NAME_PATTERN = re.compile(r"aossie(?:-[a-z0-9]+)+\Z")


def discover_skill_dirs(root: Path) -> list[Path]:
    return sorted(
        (
            path
            for path in root.iterdir()
            if path.is_dir()
            and not path.name.startswith(".")
            and path.name not in NON_SKILL_DIRS
        ),
        key=lambda path: path.name,
    )


def validate_skill(skill_dir: Path) -> list[str]:
    skill_file = skill_dir / "SKILL.md"
    label = f"{skill_dir.name}/SKILL.md"
    if not skill_file.is_file():
        return [f"{label}: missing SKILL.md file"]
    try:
        lines = skill_file.read_text(encoding="utf-8-sig").splitlines()
    except (OSError, UnicodeError) as error:
        return [f"{label}: could not read file: {error}"]

    if not lines or lines[0].strip() != "---":
        return [f"{label}: YAML frontmatter must start with --- on the first line"]
    end = next(
        (i for i, line in enumerate(lines[1:], 1) if line.strip() == "---"), None
    )
    if end is None:
        return [f"{label}: YAML frontmatter is missing its closing --- delimiter"]
    try:
        metadata = yaml.safe_load("\n".join(lines[1:end]))
    except yaml.YAMLError as error:
        return [f"{label}: invalid YAML frontmatter: {error}"]
    if not isinstance(metadata, dict):
        return [f"{label}: YAML frontmatter must be a mapping"]

    errors = []
    for field in ("name", "description"):
        value = metadata.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{label}: '{field}' must be a non-empty string")
    name = metadata.get("name")
    if isinstance(name, str) and name.strip() and not NAME_PATTERN.fullmatch(name):
        errors.append(
            f"{label}: 'name' must use lowercase kebab-case and start with 'aossie-'"
        )
    return errors


def validate_repository(root: Path) -> list[str]:
    skills = discover_skill_dirs(root)
    if not skills:
        return [f"{root}: no skill directories found"]
    return [error for skill in skills for error in validate_skill(skill)]


def main() -> int:
    errors = validate_repository(ROOT)
    if errors:
        print("Skill frontmatter validation failed:", file=sys.stderr)
        print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
        return 1
    print(
        f"Validated SKILL.md frontmatter in {len(discover_skill_dirs(ROOT))} skill directories."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
