# Tests

ARCHON is a documentation-and-knowledge-base plugin, not a runtime application — there's no application logic to unit-test. What can and does break is structural: a `SKILL.md` missing required frontmatter, a cross-reference pointing at a file that was renamed or never created, or stray non-English content slipping into a reference file. `validate_structure.py` exists to catch exactly those failure modes automatically, because they were each found and fixed by hand at least once while building this repository.

## Running

```bash
python3 tests/validate_structure.py
```

No dependencies beyond the Python 3 standard library. Exits `0` with `OK: all structure checks passed.` on success; exits `1` and lists every failure found (not just the first) otherwise.

## What It Checks

1. `.claude-plugin/plugin.json` exists and is valid JSON.
2. Every `skills/*/SKILL.md`, every `commands/*.md`, and `agents/archon.md` have YAML frontmatter with a non-empty `name` and `description`.
3. Every backtick-quoted markdown path reference rooted at the `skills/`, `agents/`, or `commands/` directories, anywhere in the repository's markdown, actually points at a file that exists.
4. No Persian, Arabic, CJK, Cyrillic, or Hangul characters appear anywhere in the repository's markdown or JSON content (this repository is English-only per `CONTRIBUTING.md`).

## Running in CI

This script is wired into `.github/workflows/validate.yml`, which runs it on every push and pull request against `main`. A broken cross-reference or missing frontmatter field fails the build rather than shipping silently.

## Extending

If you add a new structural convention this repository should hold to (e.g., requiring every `reference/*.md` file to end with a "Decision Rule for This Domain" section), add a corresponding `check_*` function to `validate_structure.py` rather than relying on manual review to catch regressions.
