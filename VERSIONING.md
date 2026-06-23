# Versioning Policy

ARCHON follows [Semantic Versioning 2.0.0](https://semver.org/): `MAJOR.MINOR.PATCH`.

## Rules

- **MAJOR** — breaking changes to the agent's persona contract, skill directory layout, command names, or output format that existing users/automation depend on.
- **MINOR** — new skills, new commands, new reference documents, or material expansion of an existing skill, with no breaking changes.
- **PATCH** — content corrections, clarity edits, typo fixes, broken-link fixes, registry sync fixes.

## Hard Constraints

1. **Never downgrade a version.** Every release's version number must be strictly greater than the previous one.
2. **Never silently rewrite history.** Use `CHANGELOG.md` to record every version bump, even patch-level ones.
3. **Pre-1.0 vs Post-1.0**: `0.x.y` releases are internal milestones and may still shift structure. `1.0.0` and above are public releases — structural changes to skill paths or command names after `1.0.0` require a MAJOR bump plus a migration note in `CHANGELOG.md`.
4. **Plugin manifest is the source of truth.** The version in `.claude-plugin/plugin.json` must always match the latest entry in `CHANGELOG.md`.
5. **Keep the README version badge in sync.** The version badge at the top of `README.md` must match `.claude-plugin/plugin.json` and `CHANGELOG.md` on every release.

## Current Version

`1.2.0` — full L1-L5 knowledge base (20 skill domains, 57 topics), single ARCHON agent, 8 commands, complete registry and docs set, premium README with hero image and Code of Conduct. See `CHANGELOG.md` for the version history.
