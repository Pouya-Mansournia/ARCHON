# Over-Engineering & Under-Engineering Detector

Run this checklist against every draft recommendation before finalizing it. Most bad architecture decisions fall into one of these two failure modes — and a single design can contain both simultaneously (e.g., a team that built Kubernetes for a tiny MVP, yet has no backups).

## Over-Engineering Triggers

Flag the design if any of these are true without a specific, named justification:

| Trigger | Why it's usually wrong | What "justified" looks like |
|---|---|---|
| Microservices before product-market fit | Splits a team that needs to move fast across boundaries it doesn't yet understand; massively increases operational surface area for unproven value | A team of 30+ engineers, multiple independently-deployable domains with stable APIs between them, and clear evidence that the monolith is the bottleneck |
| Kubernetes for a tiny MVP | K8s adds a full layer of operational complexity (cluster lifecycle, networking, RBAC, upgrades) most early products don't need | Already running enough services that a PaaS (Render, Fly.io, ECS Fargate) genuinely can't express the topology, or a hard requirement for multi-cloud portability |
| Kafka for small background jobs | Kafka requires real operational investment (partitioning strategy, consumer group management, retention tuning) that a simple queue doesn't | Genuine need for event replay, multiple independent consumers of the same event stream, or sustained throughput in the tens of thousands of events/sec |
| Multi-cloud without regulatory need | Multiplies operational complexity and erases most cloud-native managed-service benefits, for marginal vendor-lock-in protection most companies never actually exercise | A specific regulatory, contractual, or customer-mandated requirement, or genuine, demonstrated negotiating leverage need |
| Custom auth when managed auth suffices | Auth is a security-critical, easy-to-get-subtly-wrong domain; reinventing it adds risk for no differentiation | A genuinely unusual auth requirement that no managed provider supports (rare) |
| Distributed databases without global-scale need | Distributed SQL/NoSQL systems trade simplicity and strong consistency guarantees for horizontal scale most products never need | Demonstrated single-node ceiling being hit, or a hard multi-region active-active requirement |
| Event sourcing without audit/replay need | Event sourcing makes simple CRUD operations dramatically more complex to reason about and query | A genuine regulatory audit trail requirement, or a real need to replay/rebuild state from history |
| Building a platform before building a product | Generalizing for hypothetical future use cases before validating the first one wastes the most valuable early-stage resource: time-to-learning | Multiple validated, concrete use cases already in hand that share clear common abstractions |

## Under-Engineering Triggers

Flag the design if any of these are missing without a specific, named reason it's acceptable for now:

| Trigger | Why it's usually a problem | Acceptable exception |
|---|---|---|
| No backups | Data loss is often unrecoverable and is the single most common cause of company-ending incidents for small companies | Genuinely ephemeral/regenerable data only |
| No real authentication | Any system with real user data needs access control from day one | Pure internal prototype never exposed beyond localhost |
| No monitoring/alerting | Without it, failures are discovered by users, not by the team | Pre-launch prototype with zero real users |
| No rate limiting | Leaves the system open to abuse, runaway costs, and accidental self-inflicted DoS | Fully internal tool with a small, trusted, fixed user set |
| Weak or missing data model | "We'll figure out the schema as we go" routinely produces unmaintainable data over time | Genuine, time-boxed throwaway spike explicitly marked as such |
| No error handling | Silent failures are far more expensive to debug later than the time saved by skipping them now | Never acceptable in anything touching real users or money |
| No real deployment process | "SSH in and git pull" doesn't scale past one engineer and has no rollback story | A true single-developer side project with no users depending on uptime |
| Unclear ownership boundaries | When nobody owns a system, nobody fixes it until it's an incident | Acceptable only inside a single-person team where ownership is implicit |

## How to Use This in a Recommendation

1. Run the design against both tables.
2. For every trigger hit, either remove the offending complexity/gap, or write one sentence naming the specific justification from the "acceptable exception" column.
3. If a design has zero hits on both tables, say so explicitly — it's a meaningful, positive statement about the design's calibration, not a non-event.
