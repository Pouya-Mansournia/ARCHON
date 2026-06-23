# Architecture Patterns — Full Reference

## Goal

Every pattern in this file is a tool that trades simplicity for a specific capability. The skill is matching the tool to a real, current need — and recognizing that "we might need this eventually" is not the same as "we need this now."

## Monolith vs. Modular Monolith vs. Microservices

**Monolith:** Single deployable unit, single codebase, typically single database. Fastest to build, easiest to reason about as a whole, easiest to refactor across boundaries (a single PR can safely change a function signature and all its callers). Downside: as the team grows, everyone working in the same codebase can create merge contention and deploy coordination overhead, and the whole system scales as one unit even if only one part needs more capacity.

**Modular Monolith:** A monolith with enforced internal module boundaries — each module owns its own data access and exposes a deliberate internal API to other modules (no reaching directly into another module's database tables). This is the recommended default starting point for nearly every new product: you get the monolith's simplicity now, and a clean extraction path later because the boundaries are already real, just not yet physically separated by a network call.

**Microservices:** Independently deployable, independently scalable services, each typically owning its own datastore. Solves real problems at real scale: independent team deploy cadence, independent scaling per component, fault isolation (one service crashing doesn't take down the whole system). Costs real complexity: distributed transactions become hard (see eventual consistency patterns below), network calls replace function calls (introducing latency and partial-failure modes that didn't exist before), and operational surface area multiplies (more services to monitor, deploy, secure, and version).

**Migration path:** Modular monolith → identify a module with genuinely independent scaling needs or team ownership pressure → extract it behind the same internal API it already exposed → it becomes a microservice with minimal application-logic rewrite, because the boundary was already clean.

## Event-Driven Architecture

Producers publish events; consumers subscribe and react, without producers needing to know who's listening. This decouples systems that need to react to the same business event (e.g., "order placed" → inventory service, email service, analytics service, fraud-detection service, all reacting independently).

**Trade-off:** Harder to trace a single business process end-to-end (the logic is spread across multiple independent consumers reacting asynchronously) compared to a single synchronous call chain. Mitigate with distributed tracing (see `skills/13_Reliability/reference/observability-monitoring.md`) and clear event schemas/contracts.

## CQRS (Command Query Responsibility Segregation)

Separates the model used for writes (commands) from the model used for reads (queries) — they can have entirely different shapes, even live in different datastores. Useful when read patterns are numerous, complex, and meaningfully different from how data is naturally written (e.g., a write model that's normalized/transactional, with a denormalized read model optimized for a specific dashboard query).

**Decision rule:** Most CRUD applications don't need CQRS — the write and read models are naturally similar enough that maintaining two synchronized models adds complexity without commensurate benefit. Reach for it when you have a demonstrated, specific read-pattern complexity problem that a single model can't serve well.

## Event Sourcing

The system of record becomes an append-only log of events (e.g., "OrderCreated", "ItemAdded", "OrderShipped") rather than current-state rows; current state is derived by replaying events (often with periodic snapshots for performance). Strong fit when you need a true audit trail of every state change (regulated industries) or need to rebuild/replay state for analysis or recovery.

**Real cost:** Querying "current state" requires either replaying events or maintaining projections (read models) kept in sync — this is meaningfully more complex than querying a normal table, and schema evolution of event types over time is a genuinely hard problem (old events in the log were created under an old schema and must remain interpretable).

**Decision rule:** Don't adopt event sourcing for typical CRUD audit needs — a simple, well-designed audit log table (who changed what, when, old/new values) solves the audit-trail need for the vast majority of products without event sourcing's query complexity. Reach for true event sourcing when replay/rebuild is a first-class functional requirement, not just "nice to have traceability."

## Domain-Driven Design (DDD)

A set of practices (bounded contexts, aggregates, ubiquitous language, domain events) for managing complexity in systems with rich, complex business logic. Strong fit for domains like insurance underwriting, complex pricing/promotion engines, logistics routing — anywhere the business rules themselves are the hard part, not just the data access.

**Decision rule:** Apply DDD's concepts where the domain logic is genuinely complex; don't apply its full ceremony (explicit bounded context maps, aggregate root enforcement) to simple CRUD domains where it adds process overhead without corresponding clarity benefit. DDD's *thinking* (model the domain in the language domain experts use, draw deliberate boundaries) is valuable broadly; its *full tooling* is not always worth adopting wholesale.

## Clean / Hexagonal Architecture

Structures code so business logic (the "domain core") has no dependency on frameworks, databases, or external services — those are plugged in via interfaces/ports, making the core logic independently testable and the infrastructure swappable. Valuable for long-lived systems where you genuinely expect infrastructure to change (e.g., swapping databases, supporting multiple delivery mechanisms for the same logic) or where test coverage of complex business logic is a priority.

**Decision rule:** The discipline (don't let business logic directly depend on a specific ORM or framework class) is good practice broadly. The full formal layering (explicit ports/adapters, dependency inversion containers) is worth the ceremony for systems expected to live and evolve for years — overkill for a short-lived prototype.

## Choosing Between Patterns — A Worked Example

A 6-person startup building a B2B SaaS product: start as a modular monolith (clear modules: auth, billing, core-product-domain), synchronous REST internally, a simple audit-log table (not event sourcing), and apply DDD-style thinking only to the genuinely complex parts of the domain (e.g., a pricing engine) without adopting the full DDD ceremony everywhere. Revisit microservices/event-driven/CQRS only when a specific module demonstrably needs independent scaling or a specific read pattern demonstrably needs a separate model — not before.

## Common Mistakes

- Adopting microservices before there's a team-coordination or scaling problem that actually requires it.
- Adopting event sourcing or CQRS for simple CRUD needs that a normal table and a basic audit log already solve.
- Treating DDD as all-or-nothing — applying its full ceremony uniformly across both complex and trivial parts of a domain.
- Skipping clear module boundaries even in a monolith, making a future extraction (or even just safe parallel development) far harder than it needed to be.
