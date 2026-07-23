# Changelog

All notable changes to ARCHON are documented in this file.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/); versioning follows [VERSIONING.md](VERSIONING.md).

## [1.6.0] - 2026-07-23

### Added
- `docs/images/archon_demo.gif` — a ~21-second terminal demo (typing `/archon-principal` with a real stack-decision question, then revealing the Output Standard answer), generated programmatically (Python/Pillow) from the same worked example already used in Quick Start and `examples/architecture-decision-modular-monolith-vs-microservices.md`. Registered in `MODULE_INDEX.md`.
- New README "See It In Action" section directly under the hero: the demo GIF plus a text rendition of the same prompt/answer, so the value proposition and a complete working example are both visible within the first screen.

### Changed
- `README.md` — first-impression pass, addressing user-reported gaps against ARCHON's own `/archon-repo-audit` checklist:
  - Rewrote the opening paragraph to lead with outcome ("stop guessing your stack, get a defensible decision") instead of a project description.
  - Moved "Why ARCHON OS?", "Features", and "Who Is It For" (credibility/proof signals) up to sit right after the new demo section — before "Philosophy," the Five Levels table, and the Core Modules deep-dive, and well before "Quick Start" — so a first-time visitor hits proof before installation instructions.
  - Trimmed the duplicate long worked example previously in "Quick Start" (now shown once, in "See It In Action") to reduce repetition.
  - No invented features, metrics, or claims — the "See It In Action" and moved sections all reuse content already true of the repository.
- `MODULE_INDEX.md` — added `docs/images/archon_demo.gif` row.
- Version bumped to `1.6.0` (`.claude-plugin/plugin.json`, `README.md` badge, `VERSIONING.md`).

## [1.5.0] - 2026-07-23

### Added
- `commands/archon-repo-audit.md` enriched with content from a second, overlapping user-supplied repository-optimization prompt: a "Quick Win Example" template (`Input → Execution → Generated Output → Expected Result`), a Mermaid diagram type table (Architecture/Component, Sequence, Request/Data Flow, User Flow, Deployment) mapped to when each applies, and an explicit License Decision Rule table (MIT for broad-adoption libraries, Apache-2.0 for patent exposure, GPL only for clearly-intended strong copyleft).

### Changed
- `commands/archon-repo-audit.md` Output section now lists Mermaid diagram recommendations and references the license decision rule explicitly.

## [1.4.0] - 2026-07-23

### Added
- ADR-005 in `ARCHITECTURE_DECISIONS.md` — optional, read-only GitHub MCP access (`mcp__github__*`) for the `archon` agent, justified by `/archon-review`, `/archon-reflect`, and `/archon-repo-audit` all needing to ground output in a real PR/issue/repo rather than a paraphrase of one. No write scopes; the agent degrades gracefully and says so when no GitHub MCP connection is available.
- `agents/archon.md` — new "GitHub MCP Access (Optional, Read-Only)" section; `/archon-review`, `/archon-reflect`, and `/archon-repo-audit` mode descriptions updated to note when they use it.

### Changed
- `agents/archon.md` — `tools:` frontmatter extended to `Read, Grep, Glob, WebSearch, mcp__github__*`; `description:` frontmatter now lists `/archon-repo-audit`.
- `AGENT_REGISTRY.md` — Tools row updated to include optional GitHub MCP access, referencing ADR-005.
- `README.md` — reworded the "Zero required external integrations" Features bullet to "No required external integrations ... optional, read-only GitHub MCP access when connected"; Roadmap moved the GitHub integration item from "Later" to "Now (v1.4)"; version badge bumped to 1.4.0.
- `VERSIONING.md` — Current Version updated to `1.4.0`.
- `.claude-plugin/plugin.json` — version bumped to `1.4.0`.

## [1.3.0] - 2026-07-23

### Added
- `commands/archon-repo-audit.md` — new `/archon-repo-audit` command: a repository-optimization mode that audits any repo (README, docs, architecture, GitHub optimization, license, CI/CD, developer experience, AI/SEO readability) through a four-phase Audit → Benchmark → Score → Improvement Plan pipeline, grounded strictly in what the repository actually contains and never rewriting working code unnecessarily.

### Changed
- `COMMAND_REGISTRY.md` — added `/archon-repo-audit` row and file entry (9 commands total).
- `README.md` — updated command count to 9, added `/archon-repo-audit` to the Features bullet, Commands table, Example Questions, and Roadmap; bumped version badge to 1.3.0.
- `VERSIONING.md` — Current Version updated to `1.3.0` (9 commands).
- `.claude-plugin/plugin.json` — version bumped to `1.3.0`.

## [1.2.0] - 2026-06-23

### Added
- `docs/images/archon_os.png` — README hero image (decision-convergence diagram), registered in `MODULE_INDEX.md`.
- A "Code of Conduct" section in `CONTRIBUTING.md`.
- A "Keep the README version badge in sync" hard constraint in `VERSIONING.md`.

### Changed
- `README.md` rewritten as a premium, badge-led project page: hero section, Philosophy, Who Is It For, Why ARCHON OS?, Architecture Overview, a simplified 13-item "Big Picture" module summary alongside the authoritative 21-module map, Features, a worked Quick Start example, Example Questions, a checklist Roadmap, and a Documentation index — while keeping every cross-reference and structural claim (21 modules, 58 reference files, 57 topics, 8 commands) accurate to the real repository. Project identity stays `ARCHON` (`ARCHON OS` used as the README-level tagline only); no rename of the plugin, package, or repository.

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
