---
name: archon-principal
description: Ask ARCHON for a deep Principal Engineer-level architecture trade-off analysis, formatted as an Architecture Decision Record (ADR).
argument-hint: "<architecture decision or system to design>"
---

# /archon-principal

Bias ARCHON's answer toward L4 (Principal Engineering): deep trade-off analysis between named alternatives, formatted as an ADR.

## Usage

```
/archon-principal $ARGUMENTS
```

## Output — ADR Format

```markdown
# ADR-[number]: [Title]

**Status:** Proposed | Accepted | Deprecated | Superseded
**Date:** [Date]
**Deciders:** [Who needs to sign off]

## Context
[Situation and forces at play]

## Decision
[The proposed change]

## Options Considered

### Option A: [Name]
| Dimension | Assessment |
|---|---|
| Complexity | |
| Cost | |
| Scalability | |
| Team familiarity | |
| Operational burden | |

**Pros:** ...
**Cons:** ...

### Option B: [Name]
[Same format]

## Trade-off Analysis
[Explicit reasoning, referencing the Engineering Decision Principles priority order]

## Risks & Mitigations

## Migration Path

## Confidence
High | Medium | Low — [why]
```

Draws primarily from `skills/07_Architecture/`, `skills/99_Decision_Engine/reference/output-standard-and-confidence.md`, and whichever domain skill(s) the decision touches.

## Example

```
/archon-principal Should our order-processing service use event sourcing + CQRS, or a simpler CRUD model with an audit log table?
```
