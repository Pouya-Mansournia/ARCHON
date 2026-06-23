# Performance Profiling & Load Testing

## Goal

Profiling tells you where time/resources actually go inside a single execution; load testing tells you how the system behaves under realistic or stress-level concurrent demand. Both are evidence-gathering tools that should precede any non-trivial optimization effort.

## Profiling

| Type | What it reveals | Tooling examples |
|---|---|---|
| CPU profiling | Which functions/code paths consume the most CPU time | Language-native profilers (py-spy, pprof, Node's `--prof`, Java Flight Recorder) |
| Memory profiling | Allocation patterns, leaks, excessive garbage collection pressure | Heap snapshots, language-specific memory profilers |
| Database query profiling | Slow queries, missing indexes, N+1 query patterns | `EXPLAIN ANALYZE` (Postgres), slow query logs, ORM query logging |
| Distributed tracing | Where time goes across a multi-service request path | OpenTelemetry traces (see `skills/13_Reliability/reference/observability-monitoring.md`) |

**Decision rule:** Start with the layer most likely to be the bottleneck given the symptom — for most typical web/API products, database query patterns (missing indexes, N+1 queries) are the single most common real-world performance bottleneck and the first place to look before reaching for application-code micro-optimization.

## Load Testing

| Test type | Purpose |
|---|---|
| Load test | Verify the system handles expected normal/peak traffic within acceptable latency |
| Stress test | Find the actual breaking point — how far beyond expected load before the system degrades or fails |
| Soak test | Run sustained load over an extended period to catch issues that only emerge over time (memory leaks, connection pool exhaustion, log disk filling up) |
| Spike test | Verify behavior under a sudden, sharp traffic increase (a flash-sale or viral-moment scenario) |

| Tool | Good fit for |
|---|---|
| k6 | Modern, scriptable load testing, good CI integration |
| Locust | Python-based, good for teams wanting to write test scenarios in Python |
| JMeter | Mature, GUI-capable, broad protocol support, heavier-weight |
| Gatling | High-performance, Scala-based, strong reporting |

## Designing a Useful Load Test

- **Model realistic traffic patterns**, not just raw request volume — real user behavior (browsing, then checkout) differs from a flat barrage of identical requests, and the difference matters for cache hit rates, connection pooling behavior, and database load patterns.
- **Test the critical user journeys**, not an arbitrary endpoint — the goal is confidence in the paths that actually matter to the business and the user.
- **Run load tests in an environment that resembles production** closely enough for results to be meaningful — load testing a vastly under-provisioned staging environment produces numbers that don't transfer.

## Interpreting Results

Look at latency percentiles (p50/p95/p99), not just throughput or average latency — a system can show acceptable average latency while a meaningful share of requests experience unacceptable tail latency. Identify the actual limiting resource (CPU, memory, database connections, a downstream dependency) rather than assuming where the bottleneck is.

## Common Mistakes

- Optimizing code based on intuition ("this loop looks slow") without profiling data confirming it's actually the bottleneck.
- Load testing with unrealistic traffic patterns that don't resemble real user behavior, producing misleading confidence.
- Looking only at average latency and missing a real tail-latency problem.
- Load testing in an environment too different from production for the results to be actionable.

## Decision Rule for This Domain

Profile or load test before optimizing — every time. Start with database query patterns for typical web/API bottlenecks. Design load tests around realistic traffic patterns on critical user journeys, and judge results by percentile latency and identified limiting resource, not aggregate throughput alone.
