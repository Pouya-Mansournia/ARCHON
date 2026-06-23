# Pre-Release Checklist

Run through this before tagging any new ARCHON version.

## Structure

- [ ] `.claude-plugin/plugin.json` version matches the top entry in `CHANGELOG.md`.
- [ ] Every `skills/<NN_Domain>/SKILL.md` has valid YAML frontmatter (`name`, `description`).
- [ ] Every file referenced from a `SKILL.md` pointer list actually exists under that domain's `reference/` folder.
- [ ] No skill folder is empty (must contain at least `SKILL.md`).
- [ ] No top-level `modules/` folder exists (content lives under `skills/`).
- [ ] `docs/SHOWCASE.md` exists and was not deleted.

## Registries

- [ ] `SKILL_REGISTRY.md` lists all 20 skill domains with correct paths.
- [ ] `COMMAND_REGISTRY.md` lists all commands under `commands/`.
- [ ] `MODULE_INDEX.md` lists every `reference/*.md` file across all domains.
- [ ] `AGENT_REGISTRY.md` accurately describes the single `archon` agent and its L1-L5 routing.

## Commands & Agent

- [ ] Every file in `commands/` has valid frontmatter and a non-empty `## Usage` section.
- [ ] `agents/archon.md` frontmatter (`name`, `description`) is present and the persona body references the correct skill paths.

## Docs

- [ ] `README.md` Commands table and Skills table match the registries exactly.
- [ ] `docs/INSTALL.md`, `docs/QUICKSTART.md`, `docs/FAQ.md`, `docs/EXAMPLES.md` all exist and are internally consistent (no stale command/skill names).
- [ ] All internal markdown links resolve (no 404s against the actual file tree).

## Content Quality

- [ ] Spot-check 3 random reference files against the 10-part Output Standard.
- [ ] Confirm zero non-English content anywhere in the repository.
- [ ] Confirm `LICENSE` is present and matches `VERSIONING.md` / `plugin.json` (MIT).

## Git / GitHub

- [ ] Working tree clean, all new files committed.
- [ ] Commit message describes the release scope.
- [ ] Tag created matching the version (e.g., `v1.0.0`) if this is a tagged release.
