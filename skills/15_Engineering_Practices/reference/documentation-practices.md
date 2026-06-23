# Documentation Practices

## Goal

Most documentation efforts fail not because no one writes anything, but because what gets written isn't the documentation that's actually needed, or it's written once and never updated as the system changes underneath it. (See the `engineering:documentation` skill for tactical writing workflows; this file covers what should exist and why.)

## What Documentation Actually Needs to Exist

| Type | Purpose | Where it lives |
|---|---|---|
| Architecture decision records (ADRs) | Capture why a significant decision was made, including rejected alternatives | Versioned alongside the code, e.g., `ARCHITECTURE_DECISIONS.md` or a `docs/adr/` folder |
| README / onboarding docs | Get a new contributor from zero to a working local environment and a mental model of the system | Repository root |
| API documentation | Let consumers (internal or external) use an API correctly without reading its implementation | Generated from code/schema where possible (OpenAPI, GraphQL schema introspection) to avoid drift |
| Runbooks | Step-by-step operational procedures for known scenarios (deploy, rollback, common incident types) | Accessible during an incident, not buried in a wiki no one can find under pressure |
| System/architecture overview | A current mental model of how major components fit together | Kept intentionally high-level so it's less likely to drift out of date |

## Why Documentation Drifts and Dies

Documentation that requires a separate, manual update step from the code/system it describes will drift — there's no architectural force keeping it accurate. The most durable documentation either lives close to what it describes (inline comments for non-obvious logic, ADRs committed alongside the relevant code) or is generated directly from a source of truth (API docs from a schema) rather than hand-maintained in parallel.

## ADRs as the Highest-Leverage Documentation Type

An ADR capturing why a decision was made — including the alternatives considered and rejected, and the trade-offs accepted — has a much longer useful life than a description of how a system currently works (which will become outdated as the system evolves). The "why" tends to remain relevant context long after the specific "how" has changed, and it's the question new team members and future-you ask most often when revisiting an old decision ("why didn't we just use X").

## Documentation as Part of "Done"

Treat documentation updates as part of the definition of done for a change that affects how something is built, deployed, or operated — not a separate task that gets deprioritized once the "real" work ships. A PR that changes a deployment process without updating the relevant runbook has left the work genuinely unfinished.

## Calibrating Documentation Depth

Not everything needs the same documentation investment. A small internal tool with three users doesn't need the same documentation rigor as a public API with external developers depending on it — calibrate depth to the audience size, the cost of someone getting it wrong, and how long the system is expected to live.

## Common Mistakes

- Writing detailed "how it works" documentation that drifts out of sync within months, with no mechanism keeping it current.
- No ADRs at all, so years later no one remembers why a significant architectural choice was made or what alternatives were considered.
- Burying operational runbooks in a hard-to-find wiki, making them useless precisely when they're needed most (during an incident, under time pressure).
- Treating documentation as separate, deprioritizable work rather than part of completing the change itself.

## Decision Rule for This Domain

Prioritize ADRs (the "why") over exhaustive "how it works" documentation (which drifts). Generate what can be generated from source (API docs from schemas). Keep runbooks accessible under pressure. Calibrate documentation depth to audience size and consequence of error, not a uniform standard for every change.
