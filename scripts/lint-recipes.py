#!/usr/bin/env python3
"""Validate recipe frontmatter so broken PRs fail fast.

Checks every file under content/recipes/<section>/*.md (excluding _index.md):
  - has YAML frontmatter
  - required fields are present and non-empty
  - authors[] entries each have a profile at content/authors/<slug>/_index.md
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
RECIPES_DIR = ROOT / "content" / "recipes"
AUTHORS_DIR = ROOT / "content" / "authors"

REQUIRED_FIELDS = [
    "title",
    "authors",
    "cuisines",
    "servings",
    "prep_time",
    "cook_time",
    "ingredient_keys",
    "ingredients",
]


def split_frontmatter(text: str):
    if not text.startswith("---"):
        return None, text
    try:
        _, fm, body = text.split("---", 2)
    except ValueError:
        return None, text
    return yaml.safe_load(fm), body


def lint_recipe(path: Path) -> list[str]:
    errors: list[str] = []
    fm, _ = split_frontmatter(path.read_text(encoding="utf-8"))
    if fm is None:
        return [f"{path}: missing YAML frontmatter"]
    for field in REQUIRED_FIELDS:
        value = fm.get(field)
        if value is None or value == "" or value == []:
            errors.append(f"{path}: missing or empty required field '{field}'")
    authors = fm.get("authors") or []
    if not isinstance(authors, list):
        errors.append(f"{path}: 'authors' must be a list")
        authors = []
    for a in authors:
        if not isinstance(a, str) or not a.strip():
            errors.append(f"{path}: author entry must be a non-empty string, got {a!r}")
            continue
        profile = AUTHORS_DIR / a / "_index.md"
        if not profile.exists():
            errors.append(
                f"{path}: author '{a}' has no profile at {profile.relative_to(ROOT)}"
            )
    for field in ("ingredients", "ingredient_keys"):
        values = fm.get(field) or []
        if not isinstance(values, list):
            errors.append(f"{path}: '{field}' must be a list")
        elif any(not isinstance(v, str) or not v.strip() for v in values):
            errors.append(f"{path}: every entry in '{field}' must be a non-empty string")
    keys = fm.get("ingredient_keys") or []
    for k in keys:
        if isinstance(k, str) and k != k.lower():
            errors.append(f"{path}: ingredient_keys entry {k!r} must be lowercase")
    return errors


def main() -> int:
    if not RECIPES_DIR.exists():
        print(f"No recipes directory at {RECIPES_DIR}", file=sys.stderr)
        return 0
    all_errors: list[str] = []
    count = 0
    for path in sorted(RECIPES_DIR.rglob("*.md")):
        if path.name == "_index.md":
            continue
        count += 1
        all_errors.extend(lint_recipe(path))
    if all_errors:
        for e in all_errors:
            print(e, file=sys.stderr)
        print(f"\n{len(all_errors)} error(s) across {count} recipe(s).", file=sys.stderr)
        return 1
    print(f"OK — {count} recipe(s) validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
