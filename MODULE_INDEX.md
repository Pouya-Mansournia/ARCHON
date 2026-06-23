# Module Index

The complete map of this repository: every file, what it's for, and how the pieces fit together. Use `AGENT_REGISTRY.md`, `COMMAND_REGISTRY.md`, and `SKILL_REGISTRY.md` for the detailed indexes of their respective categories — this file is the top-level orientation map tying all of them together.

## Plugin Manifest

| Path | Purpose |
|---|---|
| `.claude-plugin/plugin.json` | The Claude Code plugin manifest — name, version, and entry points that make this repository loadable as a plugin. |

## Agent (1 file)

| Path | Purpose |
|---|---|
| `agents/archon.md` | The single ARCHON agent definition — Principal Engineer/CTO persona spanning L1-L5. See `AGENT_REGISTRY.md`. |

## Commands (9 files)

| Path | Purpose |
|---|---|
| `commands/archon.md` | `/archon` — default general advisory mode. |
| `commands/archon-cto.md` | `/archon-cto` — business-facing technical strategy. |
| `commands/archon-principal.md` | `/archon-principal` — architecture decision / ADR-style output. |
| `commands/archon-robotics.md` | `/archon-robotics` — robotics/embedded/real-time systems. |
| `commands/archon-ai.md` | `/archon-ai` — AI/ML/LLM product and architecture. |
| `commands/archon-review.md` | `/archon-review` — critique an existing design. |
| `commands/archon-plan.md` | `/archon-plan` — phased MVP/Growth/Scale planning. |
| `commands/archon-reflect.md` | `/archon-reflect` — revisit a past decision. |

See `COMMAND_REGISTRY.md` for the full detail on each.

## Skills (21 `SKILL.md` + 58 `reference/*.md` = 79 files)

Twenty domain modules (`00_Core` through `19_Review_Outputs`) plus the cross-cutting `99_Decision_Engine` routing layer. Full index, levels, and summaries: `SKILL_REGISTRY.md`.

| Range | Domains |
|---|---|
| `00` | Core Principles & Decision Engine (foundation layer) |
| `01-04` | Foundations, Product/Business, Frontend, Backend |
| `05-09` | Database, API, Architecture Patterns, Cloud, DevOps |
| `10-14` | AI/ML, Robotics, Security, Reliability, Performance |
| `15-19` | Engineering Practices, Team Leadership, Cost/Business, Domain Architectures, Review/Output Standards |
| `99` | Decision Engine (routing, conflict resolution, confidence calibration) |

## Documentation (7 files)

| Path | Purpose |
|---|---|
| `docs/INSTALL.md` | How to install ARCHON as a Claude Code plugin. |
| `docs/QUICKSTART.md` | A five-minute guided first session. |
| `docs/FAQ.md` | Common questions about ARCHON's design and behavior. |
| `docs/EXAMPLES.md` | Quick-reference example prompts per command mode. |
| `docs/SHOWCASE.md` | Narrative scenarios illustrating ARCHON's value. |
| `docs/BRAND_VOICE.md` | Writing/tone guidelines for contributing new content. |
| `docs/images/archon_os.png` | README hero image — the decision-convergence diagram referenced at the top of `README.md`. |

## Examples (3 files)

| Path | Purpose |
|---|---|
| `examples/architecture-decision-modular-monolith-vs-microservices.md` | Full `/archon-principal` transcript demonstrating the 10-part Output Standard. |
| `examples/security-review-checkout-flow.md` | Full `/archon-review` transcript demonstrating the structured review format. |
| `examples/robotics-ros2-vs-embedded.md` | Full `/archon-robotics` transcript demonstrating domain-specific reasoning. |

## Tests (2 files)

| Path | Purpose |
|---|---|
| `tests/validate_structure.py` | Validates plugin manifest JSON, required frontmatter, cross-reference integrity, and English-only content. |
| `tests/README.md` | How to run the validator and what it checks. |

## CI (1 file)

| Path | Purpose |
|---|---|
| `.github/workflows/validate.yml` | Runs `tests/validate_structure.py` on every push and pull request against `main`. |

## Memory (1 file)

| Path | Purpose |
|---|---|
| `memory/README.md` | The recommended pattern for persisting ARCHON-assisted decisions across sessions via ADRs, since ARCHON itself is stateless between invocations. |

## Root Governance & Reference Files (12 files)

| Path | Purpose |
|---|---|
| `README.md` | Project overview and entry point. |
| `LICENSE` | MIT License. |
| `.gitignore` | Standard ignore rules. |
| `VERSIONING.md` | How ARCHON's versioning works. |
| `CHANGELOG.md` | Version history. |
| `ROADMAP.md` | Planned future work. |
| `ARCHITECTURE_DECISIONS.md` | ADR-001 through ADR-004 — why ARCHON itself is built the way it is. |
| `CONTRIBUTING.md` | How to contribute new skills, commands, or content. |
| `PRE_RELEASE_CHECKLIST.md` | Checklist run before tagging a release. |
| `AGENT_REGISTRY.md` | Index of the single ARCHON agent. |
| `COMMAND_REGISTRY.md` | Index of all 8 slash commands. |
| `SKILL_REGISTRY.md` | Index of all 21 skill modules and 58 reference files. |
| `MODULE_INDEX.md` | This file — the complete repository map. |

## How These Pieces Compose at Runtime

1. A user invokes a slash command (`commands/*.md`), which frames the interaction mode and invokes the `archon` agent (`agents/archon.md`).
2. The agent reasons using `skills/00_Core/` as its baseline operating principles, and `skills/99_Decision_Engine/` to route the question to the right domain module(s) among `01_Foundations` through `19_Review_Outputs`.
3. Each relevant domain's `SKILL.md` and `reference/*.md` files supply the specific decision rules, comparison tables, and common-mistake checks for that domain.
4. The response is structured per `skills/99_Decision_Engine/reference/output-standard-and-confidence.md` (or the relevant review/ADR format from `skills/19_Review_Outputs/`), with an explicit confidence level.

## Keeping This Index Accurate

Every time a skill, command, or agent file is added, renamed, or removed, update `SKILL_REGISTRY.md` / `COMMAND_REGISTRY.md` / `AGENT_REGISTRY.md` as appropriate, update this file's counts and tables, and run `python3 tests/validate_structure.py` before committing — it will catch dangling cross-references introduced by a rename, which is the single most common way this repository's documentation has drifted out of sync with itself during its own construction.
