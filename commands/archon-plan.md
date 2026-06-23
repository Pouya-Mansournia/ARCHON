---
name: archon-plan
description: Have ARCHON convert an accepted architecture decision into a phased execution plan (MVP to Scale to Enterprise), explicit about what NOT to build yet.
argument-hint: "<decision or system to turn into an execution plan>"
---

# /archon-plan

Planner mode. Converts a decision (yours, or one ARCHON already gave you) into a sequenced, stage-aware build plan.

## Usage

```
/archon-plan $ARGUMENTS
```

## What Happens

ARCHON produces a phased plan with three horizons:

1. **MVP / Now** — the minimum that proves the core hypothesis. Explicit "good enough" choices that are fine to revisit later.
2. **Growth / Next** — what to add once you have real usage and real constraints (not before).
3. **Scale / Later** — what to add only once you've actually hit the limits of the Growth-stage setup, with the specific signal that tells you it's time (e.g., "move off a single Postgres primary once you're sustained above ~5K writes/sec or replication lag becomes a product problem").

Each phase explicitly lists **what we are NOT building yet, and why** — this is treated as a first-class output, not an afterthought, per `skills/99_Decision_Engine/`.

## Example

```
/archon-plan We've decided to start as a modular monolith on a single Postgres instance. Give me the phased plan from MVP through eventual scale-out.
```

## Tips

- This mode assumes a decision has already been made (by you or by `/archon` / `/archon-principal`). If you haven't decided yet, start with `/archon` instead.
