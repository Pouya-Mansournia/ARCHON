# Quickstart

A five-minute tour of ARCHON, assuming it's already installed (see `docs/INSTALL.md`).

## 1. Ask a General Question

Start with the default mode — it routes to whichever domain skill(s) the question actually needs:

```
/archon Should we use a message queue or just call the service directly?
```

ARCHON will answer using the full Output Standard (What to use / Why / Why not alternatives / Trade-offs / Risks / Cost impact / Scalability impact / Security impact / Confidence level / Migration path) — not just an opinion. See `skills/99_Decision_Engine/reference/output-standard-and-confidence.md` for what each part means.

## 2. Get a Concrete Architecture Decision

For a decision you want documented in ADR form:

```
/archon-principal We need to choose between a modular monolith and microservices for our 6-person engineering team building a logistics platform.
```

This mode biases toward L4 Principal Engineering depth and structures its answer to drop directly into an ADR (`skills/19_Review_Outputs/reference/adr-decision-log-templates.md`).

## 3. Critique an Existing Design

```
/archon-review Here's our current architecture: [paste description or PR]. What's wrong with it?
```

Review mode actively hunts for over/under-engineering, single points of failure, and missing security controls, and returns a structured critique (Summary / Findings / Risk Ranking / What's Working Well) rather than a free-form opinion.

## 4. Domain-Specific Modes

- `/archon-cto` — business-facing technical strategy, cost, team, build-vs-buy.
- `/archon-robotics` — robotics/embedded/real-time systems.
- `/archon-ai` — AI/ML/LLM product and architecture questions.
- `/archon-plan` — phased MVP → Growth → Scale planning.
- `/archon-reflect` — revisit a past decision (Unchanged / Refined / Reversed).

See `COMMAND_REGISTRY.md` for the full list and when to use each.

## 5. Where to Go Next

- `docs/EXAMPLES.md` — full worked transcripts for several command modes.
- `docs/FAQ.md` — common questions about how ARCHON is structured and why.
- `SKILL_REGISTRY.md` — the full index of domain knowledge ARCHON draws on.
- `ARCHITECTURE_DECISIONS.md` — why ARCHON itself is built the way it is.
