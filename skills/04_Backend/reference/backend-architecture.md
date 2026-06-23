# Backend Architecture — Full Reference

## Goal

Backend language/framework choice should be driven primarily by team expertise and workload shape, with ecosystem maturity and operational characteristics as the tiebreakers — not by general popularity.

## Concurrency Models — Why They Matter for the Decision

| Model | Languages/Runtimes | Characteristics |
|---|---|---|
| Single-threaded event loop | Node.js | Excellent for I/O-bound concurrency (many simultaneous waiting connections); a single CPU-bound request blocks the entire event loop — CPU-heavy work must be offloaded to worker threads/processes |
| Multi-threaded with GIL | Python (CPython) | True parallelism limited by the Global Interpreter Lock for CPU-bound code; I/O-bound async code (FastAPI + `asyncio`) scales well; CPU-bound work needs multiprocessing or a native extension |
| Goroutines (lightweight green threads) | Go | Excellent, simple concurrency model for high-throughput network services; scales to very high concurrent connection counts with low overhead |
| OS threads / thread pools | Java, C#, Rust (when used with threads) | True parallelism, more overhead per unit of concurrency than goroutines, but mature, well-understood tooling |
| Async/await with a runtime | Rust (Tokio), C# (async), modern Python | High-performance async I/O when the language/runtime supports it well |

**Decision rule:** For a typical CRUD/API backend (the overwhelming majority of products), the concurrency model rarely becomes the binding constraint before other factors (database design, caching, N+1 queries) do. Don't over-index on concurrency-model arguments for workloads that are mostly waiting on a database anyway.

## API Layer Design Considerations (Cross-Language)

- Input validation at the API boundary (using the framework's validation layer — Pydantic for FastAPI, class-validator for NestJS, or equivalent) should be non-negotiable, regardless of language choice — this is the first line of defense against malformed and malicious input.
- Consistent error response shape across the whole API (a documented error envelope: code, message, optionally a trace ID) makes client integration dramatically easier than ad-hoc error formats that vary by endpoint.
- Versioning strategy (URL path versioning `/v1/...`, header-based versioning, or none if the API is fully internal and deployed atomically with its only consumer) should be decided before the first external consumer exists — retrofitting versioning onto an unversioned public API is painful.

## Framework Maturity & Ecosystem Considerations

- NestJS (Node) brings Angular-like structure/conventions to backend Node development — useful for larger teams wanting enforced structure; adds ceremony smaller teams may not need (Express/Fastify are lighter defaults).
- FastAPI (Python) has become the strong default for new Python APIs needing async support and automatic OpenAPI schema generation; Django remains strong when the built-in admin panel, ORM, and "batteries included" conventions are genuinely valuable (e.g., internal tools, content-heavy sites).
- Spring Boot (Java/Kotlin) remains the de facto enterprise default where JVM expertise already exists — extensive ecosystem for nearly any integration need, at the cost of more configuration ceremony than lighter frameworks.

## Background Jobs & Workers

Regardless of primary backend language, CPU-bound or long-running work should be offloaded to background workers rather than handled inline in a request-response cycle — see `skills/06_API/reference/messaging-event-driven.md` for queue/worker architecture. This decouples the API's latency profile from the actual processing time of heavy tasks.

## Decision Rule for This Domain

When recommending a backend language/framework, lead with the team's existing skill composition as the dominant factor unless the workload has a specific, named technical characteristic that makes a different choice clearly better — and say so explicitly, so the user understands why the recommendation isn't simply "whatever is most popular."

## Common Mistakes

- Choosing a language for a team that doesn't know it, betting on "we'll learn it," without budgeting for the real ramp-up cost.
- Putting CPU-bound work directly in a single-threaded Node.js request handler, blocking the event loop for all other requests.
- No input validation layer, leaving the API exposed to malformed/malicious payloads.
- No API versioning strategy before the first external consumer integrates, making future breaking changes far more painful than necessary.
