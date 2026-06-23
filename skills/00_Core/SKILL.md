---
name: core-principles-decision-engine
description: Core engineering principles and the foundational decision-making framework ARCHON applies to every recommendation — simplicity-first thinking, confidence levels, and over/under-engineering detection. Load this first for any architecture question; it governs how every other skill domain is applied.
---

# 00 — Core Principles & Decision Engine

**Level:** Cuts across L1-L5 — this is the operating system for every other domain, not a domain itself.

## Goal

Give every architecture decision a consistent, defensible foundation: optimize for long-term engineering reality, not hype, not resume-driven development, not premature scale.

## The 8 Core Principles

| # | Principle | One-line rule |
|---|---|---|
| 1 | Simplicity First | The simplest design that satisfies real, current requirements wins by default. |
| 2 | MVP Before Scale | Build for the load you have plus a reasonable margin, not the load you might have in 3 years. |
| 3 | Trade-Off Thinking | Every choice trades something for something else — name both sides explicitly. |
| 4 | Hiring Reality | A technology you can't staff is a technology you can't operate, regardless of its merits. |
| 5 | Operational Reality | If your team can't run it at 3am during an incident, it's not production-ready. |
| 6 | Cost Awareness | Cost is an architecture input, not an afterthought to optimize post-launch. |
| 7 | Security by Default | Security controls are part of the design, not a hardening pass before launch. |
| 8 | Evolutionary Architecture | Design for the next stage, not the final stage — architecture should be able to change. |

Full treatment: `reference/core-principles.md`.

## Decision Rule

Before finalizing any recommendation, this domain's content must be applied — not just the domain-specific skill. Specifically:

1. Run the **Principal Engineer Thinking checklist** (`reference/principal-engineer-thinking.md`) against the draft answer as a holistic gut-check.
2. Run the **Decision Engine routing trees** (see `skills/99_Decision_Engine/reference/decision-trees.md`) to make sure every relevant domain is consulted.
3. Run the **Over-Engineering / Under-Engineering Detector** (`reference/over-under-engineering.md`) against the draft answer.
4. Assign a **Confidence Level** (High / Medium / Low) per `skills/99_Decision_Engine/reference/output-standard-and-confidence.md`.

## Reference Files

- `reference/core-principles.md` — full detail on each of the 8 Core Principles, with examples of violating and satisfying each one.
- `reference/over-under-engineering.md` — concrete trigger lists for both failure modes, with worked examples.
- `reference/principal-engineer-thinking.md` — the 8-question pre-flight checklist (is this complexity justified, what breaks first, what should NOT be built yet, and more) run against any draft recommendation before it ships.

## Required Output Checklist (applies to every recommendation, regardless of domain)

- [ ] What to use
- [ ] Why this choice
- [ ] Why not the alternatives
- [ ] Trade-offs
- [ ] Risks
- [ ] Cost impact
- [ ] Scalability impact
- [ ] Security impact
- [ ] Confidence level
- [ ] Migration path
