# Architecture Decisions — ARCHON (the plugin itself)

This log records the meta-decisions made while designing ARCHON as a Claude Code / Cowork plugin. These are decisions about ARCHON's own structure, not the architecture advice ARCHON gives to its users — that advice is produced live, per the templates in `skills/99_Decision_Engine/`.

---

## ADR-001: Single Agent with Internal Seniority Levels, Not a C-Suite Roster

**Status:** Accepted
**Date:** 2026-06-23

**Context:** The source playbook (`Universal_Agentic_OS_Factory_v3`) describes a full C-suite agent roster (CEO, CPO, CTO, CIO, COO, CFO, CRO, CMO, CHRO, CBO). ARCHON's source knowledge base (UPEA-OS) is scoped entirely to engineering/technical architecture decision-making, not general business operations.

**Decision:** Ship ARCHON as one cohesive Principal-Engineer / CTO persona with five internal seniority levels (L1 Foundations → L5 CTO & Business), rather than ten separate C-suite agents or a hybrid subset.

**Why:** The user's actual need is a single trustworthy technical decision-maker, callable from one place, that scales its altitude (from "how does Nginx routing work" to "should we go multi-region") based on the question — not a simulated executive team. A single agent avoids routing ambiguity ("which of 10 agents do I call?") and keeps the plugin's surface area small and maintainable.

**Why not the C-suite roster:** Building 10 agent personas for a single-operator use case adds maintenance burden (10x persona drift risk) without adding decision quality — UPEA-OS's content doesn't actually contain CFO/CMO/CHRO-level material, so those agents would either be empty shells or require fabricating content outside the source material's actual expertise.

**Trade-offs:** A single agent cannot "argue with itself" the way a CTO-vs-CFO roleplay could. Mitigated by giving ARCHON an explicit `/archon-review` critic mode and `/archon-reflect` mode that deliberately stress-test its own prior recommendation from an adversarial angle.

**Confidence:** High — this was explicitly confirmed by the user as the chosen scope.

---

## ADR-002: Brand-OS Downgraded From Mandatory Agent to a Lightweight Doc

**Status:** Accepted
**Date:** 2026-06-23

**Context:** The playbook marks Brand-OS (including a dedicated CBO-Agent) as "Mandatory." ARCHON rejected the multi-agent roster in ADR-001, which makes a dedicated CBO-Agent inconsistent with the chosen scope.

**Decision:** Implement Brand-OS as `docs/BRAND_VOICE.md` — a short, concrete voice/tone/output-style guide that ARCHON's agent definition explicitly references — instead of a standalone agent.

**Why:** The playbook's actual intent behind Brand-OS is consistency of voice and output format across all surfaces. That outcome is fully achievable with a referenced style doc; it does not require a simulated brand executive for a single-agent, single-operator product.

**Trade-offs:** Less ceremony than the playbook's literal instruction. Acceptable because the underlying goal (consistent voice) is preserved.

**Confidence:** Medium — this is a reasonable interpretation of "mandatory," not a literal implementation. Revisit if ARCHON is ever extended to a multi-agent setup (see `ROADMAP.md`).

---

## ADR-003: Skill Directory Naming Follows the User's Domain Taxonomy, Not Generic Kebab-Case

**Status:** Accepted
**Date:** 2026-06-23

**Context:** Claude Code skills conventionally use kebab-case directory names (`architecture/`, `write-spec/`). The user explicitly sketched a numbered domain taxonomy (`00_Core/, 01_Product/, 02_Frontend/, ..., 99_Decision_Engine/`) as the desired structure, taken directly from the end of his own UPEA-OS prompt history.

**Decision:** Keep the user's `NN_Domain_Name` directory convention for the 20 top-level skill folders. Each folder is one Claude skill (one `SKILL.md` entry point), with the `name:` frontmatter field set to a kebab-case slug derived from the folder for tool-routing compatibility, while the folder name itself stays in the user's numbered style for human navigation and GitHub readability.

**Why:** This is the structure the user explicitly asked for, taken verbatim from his own prior work — preserving it respects both his intent and the effort already invested in that taxonomy. Numbered prefixes also make the L1-L5 progression and domain grouping visually obvious in a file browser/GitHub tree, which plain kebab-case names would not.

**Trade-offs:** Slightly non-idiomatic versus other Claude plugins' folder naming. Mitigated by `SKILL_REGISTRY.md`, which maps every folder to its invocable skill name explicitly, so there is zero ambiguity for tooling or contributors.

**Confidence:** High.

---

## ADR-004: Progressive Disclosure — `SKILL.md` + `reference/*.md` per Domain

**Status:** Accepted
**Date:** 2026-06-23

**Context:** The user's chosen content depth requires authoring comprehensive material across roughly 56 topics. Cramming all 56 topics' full depth into 20 flat `SKILL.md` files would produce files hundreds of lines long, hurting load efficiency and readability.

**Decision:** Each of the 20 skill domains ships a concise `SKILL.md` (frontmatter, scope, decision rules, a comparison table, and a pointer list) plus one `reference/*.md` file per sub-topic containing the full comprehensive treatment.

**Why:** This matches Claude's own skill-authoring guidance (keep `SKILL.md` short, push detail into linked files loaded on demand) and keeps each individual reference file focused and independently linkable/citable.

**Trade-offs:** More files to navigate than a single monolithic doc per domain. Mitigated by `MODULE_INDEX.md`, which lists every reference file with a one-line description.

**Confidence:** High.

---

## ADR-005: Optional, Read-Only GitHub MCP Access — Not a Break From "Knowledge-Only"

**Status:** Accepted
**Date:** 2026-07-23

**Context:** ARCHON shipped at v1.0 as knowledge-only and stateless with zero required external integrations (see README, `ROADMAP.md` "Later" section: "Optional read-only integration hooks for project trackers / knowledge bases, only if a real need emerges"). `/archon-review`, `/archon-reflect`, and the new `/archon-repo-audit` (added same release) all explicitly claim to ground their output in "the actual codebase" or "the actual repository" — but the agent's original toolset (`Read, Grep, Glob, WebSearch`) only sees a locally checked-out working copy, not live PR status, issue history, CI results, or a remote repo the user hasn't cloned.

**Decision:** Grant the `archon` agent read-only access to GitHub via MCP (`mcp__github__*` tools), in addition to its existing `Read, Grep, Glob, WebSearch` tools. This is additive, not a replacement — ARCHON still works fully from local context and user-pasted descriptions if no GitHub MCP connection is configured.

**Why:** The real gap this closes is "ARCHON gives repo/PR/CI advice without being able to look at the repo/PR/CI it's advising on." A live GitHub connection lets `/archon-review` critique an actual PR diff instead of a paraphrase of one, lets `/archon-repo-audit` inspect the actual GitHub configuration (topics, templates, releases, branch protection) instead of guessing from a description, and lets `/archon-reflect` pull the actual history of a decision (linked issues, past PRs) instead of relying on what the user remembers to mention.

**Why not a broader integration surface (Jira, Slack, cloud provider APIs, etc.):** Those would each need their own justification tied to a specific gap in ARCHON's actual command set, which doesn't exist yet. GitHub is the one integration every one of ARCHON's existing repo/PR/review-facing commands already implicitly assumes exists. Scope creep here is exactly the failure mode ADR-001 already rejected once (adding capability the actual need doesn't call for).

**Trade-offs:** Breaks the literal "zero required external integrations" claim as originally worded. Mitigated by keeping the integration (a) read-only — no write scopes requested, ARCHON never opens PRs, pushes commits, or edits issues on the user's behalf — and (b) optional — the agent degrades gracefully and says so explicitly if no GitHub MCP connection is available, rather than blocking. The README/Features claim is reworded from "zero required external integrations" to "no required external integrations; optional read-only GitHub MCP access when connected" to stay accurate rather than silently drop the constraint.

**Confidence:** Medium — the boundary (GitHub only, read-only only) is a deliberate, narrow interpretation of "add MCP" chosen to avoid the scope creep ADR-001 already warned against. Revisit if a second integration is requested; that should get its own ADR rather than being folded in here by precedent.
