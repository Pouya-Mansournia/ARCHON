# FinOps & Cloud Cost Optimization

## Goal

Cloud cost should be treated as a first-class engineering metric, monitored and owned the same way latency and error rate are — by the time an unexpectedly large bill becomes the trigger for cost attention, waste has typically been accumulating silently for months.

## Cost Visibility — The Prerequisite for Everything Else

You can't optimize what you can't see. Tag/label every resource by team, environment, and feature/project from the start, so cost can be attributed to the part of the system or organization actually responsible for it — untagged, unattributed cloud spend is the single biggest blocker to any real cost optimization effort, because no one can tell what's safe to change.

## Common Cloud Waste Patterns

| Pattern | Why it happens | Fix |
|---|---|---|
| Oversized instances | Provisioned for a peak load estimate that never materialized, or just defaulted to a comfortable size and never revisited | Right-size based on actual observed utilization metrics, not original estimates |
| Idle/orphaned resources | Test environments, old experiments, or decommissioned features whose infrastructure was never torn down | Regular audits, automated expiry/cleanup policies for non-production resources |
| Unoptimized storage tiers | Data sitting in expensive "hot" storage tiers long after access patterns no longer justify it | Lifecycle policies that automatically transition data to cheaper tiers (see `skills/05_Database/reference/storage-architecture.md`) |
| No reserved/committed-use discounts | Paying full on-demand rates for steady, predictable baseline usage | Reserved instances/savings plans/committed-use discounts for predictable baseline load, on-demand only for variable/burst capacity |
| Data egress costs | Cross-region or cross-cloud data transfer charged per byte, often discovered only after the fact | Architect to minimize unnecessary cross-region/cross-cloud transfer; factor egress into any multi-region/multi-cloud decision (see `skills/08_Cloud/`) |
| Inefficient queries/code driving excess compute | A performance problem manifesting as a cost problem | Performance optimization (see `skills/14_Performance/`) often is cost optimization once you account for pay-as-you-go compute pricing |

## FinOps as a Practice, Not a One-Time Project

FinOps treats cost as an ongoing, cross-functional discipline (engineering, finance, and leadership collaborating with shared visibility) rather than a periodic cost-cutting exercise. The core loop: **inform** (give engineers real-time visibility into the cost impact of their decisions) → **optimize** (right-size, eliminate waste, choose efficient architectures) → **operate** (continuously monitor and govern, catching drift before it becomes a crisis).

## Cost as an Architectural Input, Not Just an Audit Target

Bring cost into the decision at design time, not just as a retrospective audit: the choice between a managed service and self-hosting, between a serverless and always-on compute model, between storing raw vs. compressed/aggregated data, all have direct cost implications that belong in the same trade-off analysis as performance and reliability (this is exactly the "Cost impact" field in the `/archon-principal` Output Standard).

## Common Mistakes

- No resource tagging, making it impossible to attribute cost to the team or feature responsible, which blocks any real optimization effort.
- Treating cost optimization as a one-time clean-up project rather than an ongoing operational discipline.
- Paying full on-demand rates for predictable, steady-state baseline load that reserved/committed-use pricing would discount significantly.
- Discovering cross-region/cross-cloud egress costs only after architecture decisions involving data transfer have already been made.

## Decision Rule for This Domain

Tag everything from day one. Treat cost visibility as a continuous, owned metric rather than a periodic audit. Bring cost into architecture decisions at design time as a named trade-off dimension, not as a post-hoc optimization pass.
