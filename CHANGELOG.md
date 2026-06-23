# Changelog

All notable changes to ARCHON are documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/); versioning follows [VERSIONING.md](VERSIONING.md).

## [1.1.0] - 2026-06-23

### Added
- `skills/00_Core/reference/principal-engineer-thinking.md` — the Principal Engineer Thinking pre-flight checklist: eight questions (is this complexity justified, can it be simpler, what breaks first, operational costs, trade-offs, can the team maintain this, what happens after 10x growth, what should NOT be built yet) plus the compressed default-preference order (Simplicity, Maintainability, Reliability, Cost Efficiency, Battle-tested solutions, Clear migration paths), reconciled against the existing 10-part Engineering Decision Principles order.
- Linked the new checklist from `skills/00_Core/SKILL.md`'s Decision Rule and Reference Files, and from `agents/archon.md`'s "How You Work" as a new step run before domain routing.

### Changed
- `SKILL_REGISTRY.md` and `MODULE_INDEX.md` reference-file counts updated from 57 to 58.

## [1.0.0] - 2026-06-23

### Added
- Initial public release of ARCHON as a Claude Code / Cowork plugin.
- Single `archon` agent persona spanning seniority levels L1 (Foundations) through L5 (CTO & Business).
- 20 skill domains (`skills/00_Core` through `skills/99_Decision_Engine`) covering 56 architecture topics, each with a `SKILL.md` entry point and detailed `reference/` documents.
- 8 slash commands: `/archon`, `/archon-cto`, `/archon-principal`, `/archon-robotics`, `/archon-ai`, `/archon-review`, `/archon-plan`, `/archon-reflect`.
- Registry layer: `AGENT_REGISTRY.md`, `SKILL_REGISTRY.md`, `COMMAND_REGISTRY.md`, `MODULE_INDEX.md`.
- Governance docs: `ARCHITECTURE_DECISIONS.md`, `VERSIONING.md`, `ROADMAP.md`, `PRE_RELEASE_CHECKLIST.md`.
- User docs: `docs/INSTALL.md`, `docs/QUICKSTART.md`, `docs/FAQ.md`, `docs/EXAMPLES.md`, `docs/SHOWCASE.md`, `docs/BRAND_VOICE.md`.
- Worked examples (`examples/`), a structure validator and consistency tests (`tests/`), and a decision-memory persistence guide (`memory/README.md`).
- MIT License.
