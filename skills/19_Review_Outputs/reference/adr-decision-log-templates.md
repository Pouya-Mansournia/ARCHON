# ADR & Decision Log Templates

## Goal

An Architecture Decision Record (ADR) is the highest-leverage documentation artifact in this entire knowledge base (see `skills/15_Engineering_Practices/reference/documentation-practices.md`) — it captures not just what was decided, but why, including what was rejected and what trade-offs were knowingly accepted. This file defines the standard template ARCHON uses internally (see `ARCHITECTURE_DECISIONS.md` at the repository root for live examples) and recommends for any project.

## The ADR Template

```
# ADR-NNN: <Short, specific title>

## Status
Proposed | Accepted | Superseded by ADR-NNN | Deprecated

## Context
What problem or decision point is this addressing? What constraints
(team size, timeline, compliance, existing system) shape the decision?

## Decision
What was decided, stated plainly and specifically.

## Alternatives Considered
- Alternative A — why it was rejected
- Alternative B — why it was rejected

## Trade-Offs Accepted
What are we knowingly giving up by choosing this option?

## Consequences
What does this decision make easier? What does it make harder later?
What follow-up work or future decisions does it set up?
```

## Why Each Section Matters

- **Status** — makes it immediately clear whether a decision is still active, which prevents someone from acting on an outdated ADR without realizing it's been superseded.
- **Context** — without this, the decision looks arbitrary in hindsight; the constraints that made it reasonable at the time are exactly what future readers need to evaluate whether those constraints still hold.
- **Alternatives Considered** — this is the section most often skipped, and the one with the highest long-term value — it pre-answers "why didn't we just use X" before anyone has to ask it again.
- **Trade-Offs Accepted** — forces explicit acknowledgment of the downside, which both improves the decision quality at the time (no trade-off-blind decisions) and sets honest expectations for later.
- **Consequences** — connects this decision to what it implies for future decisions, turning a single ADR into a thread that can be followed forward through the project's history.

## When to Write One

Write an ADR for any decision that's expensive to reverse, affects multiple parts of the system, or would otherwise be re-litigated from scratch by a future team member encountering the same question. Don't write one for decisions that are easily reversible or genuinely low-stakes — ADR overhead should track decision significance (see ADR-004 in this repository's own `ARCHITECTURE_DECISIONS.md` for a worked example of this calibration).

## Decision Logs vs. ADRs

A decision log is a lighter-weight, append-only running record (often just a dated list of shorter entries) useful for tracking many smaller decisions over time without the full ADR ceremony for each one. Use ADRs for the significant, hard-to-reverse decisions; use a decision log for the higher-volume stream of smaller calls that still benefit from being recorded somewhere, even briefly.

## Common Mistakes

- Writing ADRs only after a decision is questioned, rather than at the time it's made — by then, the original context and rejected alternatives are harder to reconstruct accurately.
- Skipping the "Alternatives Considered" section, losing the specific value an ADR provides over a simple decision announcement.
- Writing an ADR for every minor, easily-reversible decision, creating documentation overhead that discourages the practice for the decisions that actually warrant it.
- Never updating an ADR's Status field when a later decision supersedes it, leaving stale guidance that looks current.

## Decision Rule for This Domain

Write an ADR at decision time (not retroactively) for any choice that's expensive to reverse or affects multiple parts of the system. Always include rejected alternatives and accepted trade-offs explicitly. Use a lighter decision log for smaller, more frequent decisions.
