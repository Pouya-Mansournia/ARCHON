# Communication Architecture — Full Reference

## Goal

Match the communication protocol to the actual interaction shape: request/response, streaming, pub/sub, or device telemetry each have a clearly best-suited protocol family.

## REST — Design Conventions

- Resource-oriented URLs (`/orders/123/items`, not `/getOrderItems?id=123`), HTTP verbs mapped correctly (GET = read/idempotent, POST = create, PUT = full replace, PATCH = partial update, DELETE = remove).
- Consistent pagination (cursor-based for large/changing datasets, offset-based acceptable for small/stable ones), consistent filtering/sorting query parameter conventions, consistent error envelope (see `skills/04_Backend/reference/backend-architecture.md`).
- Idempotency keys for any non-idempotent operation that might be retried (payments, order creation) — without this, network retries can cause duplicate side effects.
- Versioning decided before the first external consumer (see `skills/04_Backend/reference/backend-architecture.md`).

## GraphQL — When It Actually Pays Off

GraphQL solves a real problem: multiple clients (web, iOS, Android) each needing different shapes/depths of the same underlying data, without either over-fetching (REST returning more than needed) or under-fetching (requiring many round trips). It introduces real new problems: N+1 query risk in resolvers (mitigate with DataLoader-style batching), harder HTTP-level caching (a single endpoint serving many different queries doesn't cache as simply as REST's per-resource URLs), and a steeper learning curve for the team.

**Decision rule:** Adopt GraphQL when you have genuinely diverse client query needs across multiple consumers — not for a single web app talking to its own backend, where REST's simplicity wins.

## gRPC — Internal Service Communication

Protobuf-defined contracts give strong typing and codegen across languages, plus efficient binary serialization and HTTP/2 multiplexing — strong fit for internal service-to-service calls in a microservices/service-mesh environment (see `skills/07_Architecture/reference/service-mesh.md`). Browser support requires a gRPC-Web proxy layer, so it's a poor fit for direct browser-facing APIs.

## WebSocket & Real-Time Communication

For genuinely bidirectional, low-latency, persistent-connection needs (chat, live collaborative editing, live dashboards, multiplayer features): WebSocket is the standard. Server-Sent Events (SSE) are a simpler alternative when communication only needs to flow server-to-client (e.g., streaming LLM token output, live notifications) — SSE avoids WebSocket's added connection-management complexity when bidirectional isn't actually needed.

**Operational note:** WebSocket connections are stateful and don't fit cleanly behind simple stateless load balancing — connection affinity or a dedicated real-time infrastructure layer (e.g., a managed service like Pusher/Ably, or a self-managed solution with sticky sessions/a pub-sub backplane like Redis) is needed once you scale beyond a single server instance.

## Webhooks — Async Notification to External Systems

Design for the receiver's reality: retries with exponential backoff, signature verification (HMAC) so receivers can trust the payload's authenticity, and idempotency on the receiving end (the same event may be delivered more than once — receivers should de-duplicate by event ID). Provide a way for consumers to replay missed events (a webhook event log they can query) rather than relying solely on push delivery succeeding every time.

## Sync vs. Async — The Core Decision Framework

Ask: **does the caller need the result immediately to proceed, or can it be notified/polled later?**
- If immediate result is required → synchronous (REST/gRPC request-response).
- If the work is long-running, can tolerate delay, or needs to be retried/rate-limited independently of the request path → asynchronous (queue + worker, see `reference/messaging-event-driven.md`).

**Common mistake:** Doing genuinely long-running work (sending bulk emails, generating a large report, processing a video) synchronously inside an HTTP request handler, causing timeouts and poor user experience, when a queue + background worker + status polling/webhook notification would be both faster-feeling and more resilient.

## Decision Rule for This Domain

Pick the protocol per interaction, not per system — a single product commonly uses REST for its public API, gRPC internally between services, and WebSocket for one specific real-time feature. Don't force one protocol to serve every interaction shape just for architectural uniformity.
