---
name: api-communication-architecture
description: API and communication architecture — REST, GraphQL, gRPC, WebSocket, MQTT, webhooks, and messaging/queue systems (RabbitMQ, Kafka, NATS, Celery) with sync vs async decision rules.
---

# 06 — API & Communication Architecture (L2)

**Level:** L2 — Software Engineering.

## Goal

Choose the right communication protocol per interaction (request/response vs. streaming vs. event-driven) and the right messaging backbone when async processing is genuinely needed — protocol and messaging-technology choice should follow from the actual interaction pattern, not from default habit.

## Protocol Decision Matrix

| Protocol | Best for | Avoid when |
|---|---|---|
| REST | Default choice for most public/external APIs — simple, cacheable, universally understood | Client needs to fetch deeply nested/varied data shapes efficiently in one round trip |
| GraphQL | Clients with varied, evolving data needs (especially mobile/multiple frontend clients sharing one API) | Simple CRUD APIs where REST's simplicity is sufficient — GraphQL adds real server-side complexity (resolver design, N+1 query risk, caching difficulty) |
| gRPC | Internal service-to-service communication needing high performance and strong typing (via Protobuf) | Public APIs needing broad client compatibility (browser support is limited without a proxy) |
| WebSocket | Real-time, bidirectional, persistent-connection needs (chat, live collaboration, live dashboards) | Simple request/response interactions — adds connection-management complexity for no benefit |
| MQTT | IoT/constrained-device messaging — lightweight, designed for unreliable networks | General web/app backend communication — it's purpose-built for device telemetry, not a general API protocol |
| Webhooks | Notifying external systems of events asynchronously | Needing a guaranteed, ordered delivery or sub-second latency without the receiver investing in robust retry handling |

## Messaging / Queue Decision Matrix

| Technology | Best for |
|---|---|
| RabbitMQ | General-purpose task queues, complex routing (exchanges/topics), moderate throughput — strong default for most background-job needs |
| Kafka | High-throughput event streaming, event replay, multiple independent consumers of the same stream, log-based architectures |
| NATS | Lightweight, very low-latency pub/sub and request/reply, especially in cloud-native/microservices and IoT contexts |
| Redis Queue / BullMQ | Simple background job queues when Redis is already in the stack and throughput needs are modest |
| Celery (Python) | Python-ecosystem task queue, mature, well-integrated with Django/FastAPI |

## Decision Rule

Default to synchronous REST for client-facing APIs and a simple queue (RabbitMQ, or Redis-based if Redis is already present) for background jobs. Reach for GraphQL only with a genuine multi-client/varied-query-shape need. Reach for Kafka only with a genuine event-replay or high-throughput multi-consumer need — see `skills/00_Core/reference/over-under-engineering.md`'s "Kafka for small background jobs" trigger.

## Reference Files

- `reference/communication-architecture.md` — full protocol comparison, API design conventions, sync vs. async decision framework.
- `reference/messaging-event-driven.md` — queue/broker deep dive, delivery guarantees, event-driven architecture patterns.
