#!/usr/bin/env python3
"""
ARCHON structure validator.

Checks the things that have historically gone wrong while building this
repository, so they fail loudly in CI instead of shipping silently:

  1. .claude-plugin/plugin.json is present and valid JSON.
  2. Every skills/*/SKILL.md has frontmatter with `name` and `description`.
  3. Every commands/*.md has frontmatter with `name` and `description`.
  4. agents/archon.md has frontmatter with `name` and `description`.
  5. Every in-repo markdown cross-reference (`skills/...md`, `agents/...md`,
     `commands/...md`) points at a file that actually exists.
  6. No non-Latin-script characters (Persian, Arabic, CJK, Cyrillic, Hangul)
     appear anywhere in the repository's markdown or JSON content.

Run from the repository root:

    python3 tests/validate_structure.py

Exits 0 with no output on success, exits 1 and prints every failure found
on failure (it does not stop at the first one).
"""

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
FAILURES: list[str] = []


def fail(message: str) -> None:
    FAILURES.append(message)


def check_plugin_manifest() -> None:
    manifest = REPO_ROOT / ".claude-plugin" / "plugin.json"
    if not manifest.exists():
        fail(f"Missing plugin manifest: {manifest.relative_to(REPO_ROOT)}")
        return
    try:
        json.loads(manifest.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"Invalid JSON in {manifest.relative_to(REPO_ROOT)}: {exc}")


FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def parse_frontmatter(text: str) -> dict:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    return fields


def check_frontmatter(path: Path, required: tuple[str, ...] = ("name", "description")) -> None:
    text = path.read_text(encoding="utf-8")
    fields = parse_frontmatter(text)
    rel = path.relative_to(REPO_ROOT)
    if not fields:
        fail(f"{rel}: missing YAML frontmatter block (expected --- ... --- at top of file)")
        return
    for key in required:
        if key not in fields or not fields[key]:
            fail(f"{rel}: frontmatter missing required field '{key}'")


def check_all_frontmatter() -> None:
    for skill_md in sorted((REPO_ROOT / "skills").glob("*/SKILL.md")):
        check_frontmatter(skill_md)

    commands_dir = REPO_ROOT / "commands"
    if commands_dir.is_dir():
        for cmd_md in sorted(commands_dir.glob("*.md")):
            check_frontmatter(cmd_md, required=("name", "description"))

    agent_md = REPO_ROOT / "agents" / "archon.md"
    if agent_md.exists():
        check_frontmatter(agent_md, required=("name", "description"))
    else:
        fail("Missing agents/archon.md")


CROSS_REF_RE = re.compile(r"`((?:skills|agents|commands)/[A-Za-z0-9_./-]+\.md)`")

ROOT_DOC_NAMES = (
    "README", "LICENSE", "VERSIONING", "CHANGELOG", "ROADMAP", "CONTRIBUTING",
    "ARCHITECTURE_DECISIONS", "PRE_RELEASE_CHECKLIST",
    "AGENT_REGISTRY", "COMMAND_REGISTRY", "SKILL_REGISTRY", "MODULE_INDEX",
)
ROOT_DOC_RE = re.compile(
    r"`([A-Za-z0-9_./-]*?(" + "|".join(ROOT_DOC_NAMES) + r")\.md)`"
)


def check_root_doc_references() -> None:
    """Catch references to root governance docs that drifted to a wrong
    path (e.g. a stale `registry/SKILL_REGISTRY.md` prefix from an earlier
    planned layout that was never actually used). These files all live at
    the repository root, so any directory-prefixed reference to one of
    them is a bug -- unless that exact prefixed path also happens to be a
    real, separate file (e.g. `tests/README.md` and `memory/README.md`
    are legitimate files in their own right, not misrouted references to
    the root `README.md`)."""
    for md_file in REPO_ROOT.rglob("*.md"):
        if ".git" in md_file.parts:
            continue
        text = md_file.read_text(encoding="utf-8")
        for full_path, stem in ROOT_DOC_RE.findall(text):
            if full_path == f"{stem}.md":
                continue
            if (REPO_ROOT / full_path).exists():
                continue
            fail(
                f"{md_file.relative_to(REPO_ROOT)}: reference to `{full_path}` "
                f"should point at root-level `{stem}.md` (no directory prefix)"
            )


def check_cross_references() -> None:
    md_files = list(REPO_ROOT.rglob("*.md"))
    for md_file in md_files:
        if ".git" in md_file.parts:
            continue
        text = md_file.read_text(encoding="utf-8")
        for ref in CROSS_REF_RE.findall(text):
            target = REPO_ROOT / ref
            if not target.exists():
                fail(f"{md_file.relative_to(REPO_ROOT)}: dangling reference to `{ref}`")


NON_LATIN_RE = re.compile(
    "[؀-ۿ一-鿿぀-ヿЀ-ӿ가-힯]"
)


def check_english_only() -> None:
    for path in REPO_ROOT.rglob("*"):
        if path.is_dir() or ".git" in path.parts:
            continue
        if path.suffix not in (".md", ".json"):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        match = NON_LATIN_RE.search(text)
        if match:
            line_no = text[: match.start()].count("\n") + 1
            fail(
                f"{path.relative_to(REPO_ROOT)}:{line_no}: non-Latin-script character "
                f"found ('{match.group()}') — repository content must be English-only"
            )


def main() -> int:
    check_plugin_manifest()
    check_all_frontmatter()
    check_cross_references()
    check_root_doc_references()
    check_english_only()

    if FAILURES:
        print(f"FAILED: {len(FAILURES)} issue(s) found\n")
        for item in FAILURES:
            print(f"  - {item}")
        return 1

    print("OK: all structure checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
