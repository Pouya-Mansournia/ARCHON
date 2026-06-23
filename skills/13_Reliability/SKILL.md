---
name: reliability-sre
description: Site reliability engineering — observability and monitoring, incident management and chaos engineering, and SLOs/SLAs/error budgets — with decision rules for how much reliability investment a given system's stage actually warrants.
---

# 13 — Reliability & SRE (L4)

**Level:** L4 — Principal Engineering.

## Goal

Invest in reliability practices proportional to what the system's actual uptime/correctness requirements demand — a pre-PMF MVP and a payments system serving millions of transactions warrant very different levels of observability, on-call rigor, and chaos engineering investment, and applying the wrong level in either direction is a real cost (under-investment risks real incidents; over-investment burns engineering time the product doesn't yet need spent that way).

## Reliability Investment by Stage

| Stage | What's warranted |
|---|---|
| Pre-PMF / early MVP | Basic monitoring (uptime, error rate), simple alerting, manual incident response — heavy SRE tooling investment here is premature |
| Growth, real users depending on the product | Structured observability (logs/metrics/traces), defined on-call rotation, a real incident response process, basic SLOs for critical paths |
| Scale, mission-critical reliability expectations | Full observability stack, error budgets driving release decisions, chaos engineering, multi-layered redundancy, mature postmortem culture |

## Core Reliability Practices

| Practice | Purpose |
|---|---|
| Observability (logs, metrics, traces) | Understand system behavior and diagnose issues — see `reference/observability-monitoring.md` |
| Incident response process | Respond to and resolve issues quickly and learn from them — see `reference/incident-management-chaos.md` (and the `engineering:incident-response` skill for live incident workflow) |
| SLOs/SLAs/error budgets | Quantify and govern acceptable reliability targets — see `reference/slo-sla-error-budgets.md` |
| Chaos engineering | Proactively validate resilience assumptions before real failures test them | 

## Decision Rule

Build the observability and incident-response foundation early (it's cheap relative to its value and painful to retrofit during a live incident with no visibility), but defer error-budget-driven release governance and chaos engineering until there's a real reliability target worth defending and enough production traffic for the practice to yield meaningful signal.

## Reference Files

- `reference/observability-monitoring.md` — logs, metrics, traces, and the three pillars of observability in practice.
- `reference/incident-management-chaos.md` — incident response process, severity classification, and chaos engineering practices.
- `reference/slo-sla-error-budgets.md` — defining and governing SLOs, SLAs, and error budgets.
