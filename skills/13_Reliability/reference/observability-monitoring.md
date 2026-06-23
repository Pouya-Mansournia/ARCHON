# Observability & Monitoring

## Goal

Observability answers "what is actually happening inside this system right now" — without it, every production issue starts with guesswork instead of evidence. Build it as a first-class system component, not an afterthought added once an incident makes its absence painfully obvious.

## The Three Pillars

| Pillar | What it captures | Best for |
|---|---|---|
| Logs | Discrete, timestamped events with context | Detailed debugging of specific events, audit trails |
| Metrics | Numeric measurements over time (counters, gauges, histograms) | Trend analysis, alerting thresholds, dashboards |
| Traces | The path of a single request across services/components | Diagnosing latency and failures in distributed/multi-service systems |

A mature observability setup uses all three together — metrics tell you something's wrong and roughly where, traces show you the path the failing request took, and logs give you the specific detail of what happened at each step.

## Monitoring Stack Options

| Tool | Category | Good fit for |
|---|---|---|
| Prometheus + Grafana | Metrics + dashboards | Self-hosted/Kubernetes-native environments, strong open-source default |
| Datadog | Full observability platform (logs, metrics, traces, APM) | Teams wanting an integrated managed platform without assembling open-source pieces |
| Grafana Loki | Logs | Pairing with Prometheus/Grafana for a cohesive open-source stack |
| OpenTelemetry | Instrumentation standard (vendor-neutral) | Instrumenting code once and being able to send data to multiple backends without vendor lock-in — increasingly the right default for new instrumentation |
| Sentry | Error tracking | Application-level error/exception tracking with rich context, complements metrics/logs rather than replacing them |

**Decision rule:** Instrument with OpenTelemetry from the start regardless of which backend is chosen — it decouples instrumentation from vendor choice, avoiding a painful re-instrumentation project if the backend changes later.

## What to Monitor — The RED and USE Methods

| Method | Focus | Metrics |
|---|---|---|
| RED (Rate, Errors, Duration) | Request-driven services | Requests per second, error rate, request duration (latency percentiles) |
| USE (Utilization, Saturation, Errors) | Resources (CPU, memory, disk, queues) | How busy a resource is, how much queued work it has, error counts |

Track latency as percentiles (p50, p95, p99), never just averages — an average can look healthy while a meaningful fraction of users experience a badly degraded p99 experience.

## Alerting Principles

- **Alert on symptoms users would notice (error rate, latency), not just on causes** (CPU usage) — a CPU spike that doesn't affect user-facing behavior shouldn't page anyone at 3am.
- **Every alert should be actionable** — if there's nothing a human can do in response, it shouldn't be a page; it can be a dashboard signal instead.
- **Avoid alert fatigue** — too many low-value alerts trains the on-call rotation to ignore pages, which defeats the purpose of alerting at all.

## Common Mistakes

- Logging extensively but with no structured metrics or alerting, so problems are only discovered by manually digging through logs after a user complaint.
- Alerting on every metric anomaly regardless of user impact, causing alert fatigue and trained-in ignoring of pages.
- Tracking only average latency, masking a real tail-latency problem affecting a meaningful share of users.
- Instrumenting directly against a specific vendor's SDK with no abstraction, making a future observability-backend migration a full re-instrumentation project.

## Decision Rule for This Domain

Instrument with OpenTelemetry across logs, metrics, and traces from early on — the cost is low and retrofitting it during an active incident with zero visibility is far worse. Alert on user-facing symptoms with clear actionability, and track latency by percentile, not average.
