# FAQ

## Why is ARCHON a single agent instead of a full C-suite roster (CEO/CPO/CTO/CIO/COO/CFO/...)?

Because the actual need is a single, consistent engineering decision-making voice, not a simulated executive team. A roster of separate agents fragments context and forces the user to figure out which "executive" to ask — a single agent with internal L1-L5 seniority levels gives the same range of perspective (junior-engineer fundamentals through CTO-level business trade-offs) without that fragmentation. See ADR-001 in `ARCHITECTURE_DECISIONS.md` for the full reasoning.

## What do the L1-L5 levels actually mean?

They're internal seniority lenses the single `archon` agent applies depending on the question, not separate personas: L1 Foundations (junior-engineer fundamentals), L2 Software Engineering (day-to-day implementation decisions), L3 Infrastructure & Cloud, L4 Principal Engineering (architecture trade-off depth), L5 CTO & Business (cost, team, strategy). A question about choosing a Linux distro gets an L1-flavored answer; a question about org design gets an L5-flavored answer — same agent, different depth and framing.

## Why does every recommendation come back in the same 10-part format?

Consistency is what makes ARCHON's output usable as a durable record rather than a one-off chat answer — see `skills/99_Decision_Engine/reference/output-standard-and-confidence.md`. A recommendation that doesn't state its trade-offs, risks, and confidence level is an opinion; one that does is closer to an engineering decision document. The 10 parts are: What to use, Why this choice, Why not the alternatives, Trade-offs, Risks, Cost impact, Scalability impact, Security impact, Confidence level, Migration path.

## What's the "Over/Under-Engineering Detector"?

A universal filter applied to every recommendation, defined in `skills/00_Core/reference/over-under-engineering.md`. Over-engineering means solving a hypothetical future problem instead of the real, current one (Kubernetes for an MVP with no traffic, multi-cloud with no regulatory driver). Under-engineering means skipping a genuine baseline requirement every production system needs (no real auth, no backups, no monitoring). Both failure modes get checked on every answer, not just one.

## How does ARCHON decide how confident it is?

Per `skills/99_Decision_Engine/reference/output-standard-and-confidence.md`: high confidence requires both a well-understood problem and strong consensus among the relevant domain decision rules. Low confidence is stated explicitly whenever a question involves unusual constraints, conflicting principles with no clean resolution, or sits at the edge of this knowledge base's coverage. ARCHON is designed to say "Medium confidence, here's why" rather than projecting false certainty.

## Can I add my own domain knowledge?

Yes — new domain modules follow the existing `skills/<NN_Domain>/SKILL.md` + `reference/*.md` pattern. See `CONTRIBUTING.md` and `SKILL_REGISTRY.md` for the structure to follow, and remember to update both registries plus `MODULE_INDEX.md` so cross-references stay resolvable.

## Does ARCHON replace human architecture review?

No. ARCHON is a decision-support tool that applies a consistent framework and a broad (but finite) knowledge base. It's most useful for getting a fast, structured first pass at a trade-off — including the parts people forget to ask about (cost, security, migration path) — not as a substitute for review by someone with direct context on your system, team, and constraints.

## Why MIT license?

To make ARCHON as freely reusable and forkable as possible, including for commercial use, with minimal friction. See `LICENSE`.
