# Scaling Patterns

## Goal

Scaling is a response to a measured constraint, not a default posture — apply the lightest scaling technique that resolves the actual measured bottleneck, in the order that keeps the system simplest for as long as possible.

## Vertical vs. Horizontal Scaling

| Approach | How it works | Use when | Limits |
|---|---|---|---|
| Vertical scaling | Increase resources (CPU/RAM) on existing instances | Simplest first lever, especially for stateful components (databases) where horizontal scaling is harder | Has a hard ceiling (the largest available instance size), and a single point of failure remains |
| Horizontal scaling | Add more instances behind a load balancer | Stateless components (application servers, API layers) — scales further than vertical scaling and improves redundancy | Requires the component to actually be stateless (or have externalized state — sessions in Redis, not in-memory) |

**Decision rule:** Scale vertically first for simplicity when there's headroom available — it requires no architectural change. Move to horizontal scaling once vertical scaling's ceiling is in sight or redundancy (not just capacity) is the goal.

## The Scaling Toolkit, in Order of Likely First Application

1. **Fix the actual bottleneck** identified via profiling (a missing index, an N+1 query, an inefficient algorithm) — this is "scaling" in the sense that it's almost always cheaper than infrastructure scaling and should come first.
2. **Caching** (see `skills/05_Database/reference/caching-architecture.md`) — often the highest-leverage lever for read-heavy workloads once the underlying queries are already efficient.
3. **Async offload** — move non-latency-critical work off the synchronous request path into a background job/queue (see `skills/06_API/reference/messaging-event-driven.md`), so the user-facing request returns fast and heavy processing happens out of band.
4. **Horizontal scaling of stateless layers** — add more application server instances behind a load balancer, the standard lever once caching and async offload have been applied.
5. **Database read replicas** — offload read traffic from the primary database once read load (not write load) is the bottleneck.
6. **Database scaling (vertical, then sharding/partitioning)** — see `skills/05_Database/reference/database-data-architecture.md` for the sharding threshold discussion; this is among the most expensive and hardest-to-reverse scaling steps, so it should come after the cheaper levers above have been exhausted.
7. **Architectural decomposition** (extracting a genuinely independent-scaling component into its own service) — the most expensive lever, reserved for a demonstrated, specific scaling mismatch between components (see `skills/07_Architecture/SKILL.md`'s microservices decision rule).

## CDN and Edge Caching

For read-heavy, broadly-shared content (static assets, public pages, cacheable API responses), pushing the cache to the edge (CDN) reduces both latency and origin load simultaneously — often the single best cost/effort ratio in the entire scaling toolkit, and worth applying early regardless of stage (see `skills/08_Cloud/reference/edge-multi-cloud.md`).

## Autoscaling

Configure autoscaling (for horizontally-scaled stateless layers) based on the metric that actually predicts user-facing degradation for that component (often request latency or queue depth, not just raw CPU utilization) — scaling triggers tied to the wrong metric either scale too late (after users are already affected) or too eagerly (wasting cost on noise).

## Common Mistakes

- Reaching for horizontal scaling or a new caching layer before fixing an underlying inefficient query or algorithm that profiling would have caught.
- Scaling the database vertically indefinitely without considering read replicas for read-heavy load, when that's a cheaper and more architecturally sound next step.
- Autoscaling on raw CPU utilization for a workload where the real user-facing constraint is something else (queue depth, memory, an external dependency's rate limit).
- Reaching for sharding or service decomposition long before simpler levers (caching, read replicas, async offload) have been tried and measured.

## Decision Rule for This Domain

Apply the scaling toolkit in order of cost and reversibility — fix bottlenecks, then cache, then offload async, then scale horizontally, then scale the database, and only decompose architecturally as a last, well-justified resort. Tie autoscaling triggers to metrics that genuinely predict user-facing degradation.
