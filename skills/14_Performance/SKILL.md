---
name: performance-engineering
description: Performance engineering — profiling and load testing methodology, and scaling patterns (vertical/horizontal, caching, async offload) — with a decision rule of measure before optimizing.
---

# 14 — Performance Engineering (L3/L4)

**Level:** L3/L4 — Infrastructure & Principal Engineering.

## Goal

Performance work should be driven by measurement against a real, user-impacting bottleneck — not by intuition about what "feels slow" or by reflexively reaching for the most powerful scaling technique available. The Engineering Decision Principles place Performance below Simplicity, Maintainability, Reliability, Development Speed, Cost Efficiency, and Security in priority order for good reason: premature performance optimization routinely costs more in complexity than it returns in speed.

## The Measurement-First Rule

Never optimize without a profile or load test pinpointing the actual bottleneck first. "I think the database is slow" is a hypothesis, not a diagnosis — confirm it with actual query timing data before redesigning the data layer. This single rule prevents the majority of wasted performance-engineering effort.

## Performance Work by Stage

| Stage | What's warranted |
|---|---|
| Pre-PMF / MVP | Avoid obviously bad patterns (N+1 queries, no indexing on common lookups) but don't invest in load testing or scaling infrastructure for traffic that doesn't exist yet |
| Growth | Profile and load test critical user journeys, address measured bottlenecks, introduce caching where data justifies it |
| Scale | Continuous performance monitoring tied to SLOs, capacity planning ahead of demand, deeper architectural scaling work where genuinely warranted |

## Reference Files

- `reference/performance-profiling-load-testing.md` — profiling methodology, load testing tools and practices, and how to interpret results.
- `reference/scaling-patterns.md` — vertical vs. horizontal scaling, caching's role, async offload, and database scaling patterns.
- `reference/analytics-data-platform.md` — OLTP vs. OLAP, the decoupling pattern, ETL vs. ELT, and batch vs. streaming analytics.
