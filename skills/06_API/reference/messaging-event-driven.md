# Messaging & Event-Driven Architecture

## Goal

Choose a messaging backbone that matches the actual delivery-guarantee, throughput, and consumer-pattern needs — and understand the operational commitment each choice implies before adopting it.

## Delivery Guarantees — The Core Vocabulary

| Guarantee | Meaning | Trade-off |
|---|---|---|
| At-most-once | Message delivered zero or one times | Simplest, but messages can be silently lost — rarely acceptable for anything important |
| At-least-once | Message delivered one or more times | Standard default for most queue systems; requires idempotent consumers to handle duplicate delivery safely |
| Exactly-once | Message delivered exactly one time | Genuinely hard to guarantee end-to-end across distributed systems; usually achieved as "effectively-once" via at-least-once delivery + idempotent processing, rather than a true system-level guarantee |

**Decision rule:** Design consumers to be idempotent (safe to process the same message twice) by default, rather than chasing true exactly-once delivery — this is simpler to reason about and more robust in practice.

## Queue/Broker Decision Table (Expanded)

| Technology | Throughput | Routing complexity | Replay capability | Operational burden | Best for |
|---|---|---|---|---|---|
| RabbitMQ | Moderate-high | Rich (exchanges: direct, topic, fanout) | Limited (messages consumed and removed) | Moderate | General task queues, complex routing needs |
| Kafka | Very high | Topic/partition-based | Strong (configurable retention, full replay) | High (partitioning strategy, consumer group management, broker ops) | Event streaming, audit logs, multiple independent consumers needing replay |
| NATS / NATS JetStream | High, very low latency | Subject-based pub/sub | JetStream adds persistence/replay | Low-moderate | Cloud-native microservices, IoT, latency-sensitive pub/sub |
| Redis Streams / BullMQ | Moderate | Simple | Limited | Low (if Redis already present) | Simple background jobs when Redis is already in the stack |
| AWS SQS / GCP Pub/Sub / Azure Service Bus | High | Moderate | Varies (Pub/Sub supports replay; SQS standard does not) | Very low (fully managed) | Teams wanting to avoid operating broker infrastructure at all |

**Decision rule:** Default to a managed cloud queue (SQS, Pub/Sub, Service Bus) when already on that cloud provider and there's no specific reason to self-host — removes an entire operational burden category. Reach for Kafka specifically when you need event replay or multiple independent consumer groups reading the same stream at high throughput; this is a deliberate, named capability, not a default.

## Event-Driven Architecture Patterns

- **Task queue pattern** — a producer enqueues a unit of work, a worker pool consumes and processes it. The most common, simplest async pattern. Use for: sending emails, generating reports, processing uploads, any "do this later, off the request path" need.
- **Pub/sub / fan-out pattern** — one event triggers multiple independent consumers reacting to it (e.g., "order placed" triggers inventory update, email confirmation, analytics event, fraud check — independently). Decouples producers from needing to know about every consumer.
- **Event sourcing** — the system of record is an append-only log of events, with current state derived by replaying them. Powerful for audit/replay needs, substantially more complex to query and reason about for typical CRUD needs. See `skills/07_Architecture/reference/architecture-patterns.md` for the full event sourcing/CQRS treatment — this is a pattern to reach for deliberately, not by default.
- **Outbox pattern** — when a service needs to update its own database and publish an event atomically, write the event to an "outbox" table in the same transaction as the data change, then a separate process reliably publishes from the outbox. Solves the dual-write consistency problem (where a DB write succeeds but the corresponding message publish fails, or vice versa) without needing distributed transactions.

## Dead Letter Queues & Failure Handling

Every queue-based system needs an explicit answer to "what happens when processing a message fails repeatedly?" — route to a dead-letter queue after N retries, alert on DLQ growth, and have a defined process (automatic or manual) for inspecting and reprocessing or discarding dead-lettered messages. A queue with no DLQ strategy either retries forever (potentially blocking the queue) or silently drops failed messages.

## Decision Rule for This Domain

Before adopting any messaging technology, name explicitly: the delivery guarantee needed, the expected throughput, whether replay is needed, and who will operate the broker. If the honest answer to "who will operate Kafka" is "nobody on this team has run it before," that's a Hiring Reality / Operational Reality flag (see `skills/00_Core/reference/core-principles.md`) worth weighing against a managed alternative.

## Common Mistakes

- Choosing Kafka by default without a genuine replay or high-throughput multi-consumer need, then struggling with its operational complexity.
- Non-idempotent consumers that double-process messages on retry (e.g., double-charging a customer, double-sending an email).
- No dead-letter queue strategy, leading to either infinite retry loops or silent message loss.
- Using the outbox pattern's absence as an excuse for dual-write bugs (DB updated, event never published, or vice versa) that silently desynchronize systems.
