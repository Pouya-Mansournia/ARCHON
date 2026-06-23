# Example: `/archon-principal` — Modular Monolith vs. Microservices

**Prompt:**

```
/archon-principal We're a 6-person engineering team building a logistics/dispatch platform. We're debating modular monolith vs. microservices before we write the first line of backend code. What should we do?
```

**Response:**

### What to Use

A modular monolith — one deployable backend, internally organized into clearly bounded modules (dispatch, fleet, billing, notifications) with enforced boundaries between them (separate packages/namespaces, no reaching into another module's internals, communication through defined interfaces).

### Why This Choice

At 6 engineers, the operational overhead of microservices (independent deployments, service discovery, distributed tracing, network-call failure handling between every module boundary) costs more in velocity than it returns in isolation benefits. A modular monolith gets you most of microservices' organizational benefit — clear module boundaries, the ability to reason about one module at a time — without paying for distributed-systems complexity you don't yet need. See `skills/07_Architecture/reference/architecture-patterns.md`.

### Why Not the Alternatives

**Microservices now:** Would require the team to build and operate service discovery, inter-service auth, distributed tracing, and independent CI/CD pipelines for each service — real engineering effort that doesn't differentiate the dispatch product, at a team size where most modules will still be touched by the same 1-2 engineers regardless of deployment boundary. The over-engineering trigger here is "premature distributed systems complexity" per `skills/00_Core/reference/over-under-engineering.md`.

**A single undifferentiated codebase with no internal module boundaries:** Would be even faster to start, but creates the specific failure mode modular monoliths exist to prevent — module boundaries erode, and a future extraction (if ever needed) becomes far harder because nothing was ever cleanly separated.

### Trade-Offs

Gaining: faster iteration speed, one deployment pipeline, one place to look for any given bug, lower operational burden for a small team. Giving up: the ability to scale individual modules' compute independently, and the forcing function microservices provide against module boundaries eroding (a modular monolith's boundaries are enforced by discipline and tooling, not the harder physical boundary of separate deployments).

### Risks

The primary risk is boundary erosion — without the hard separation microservices impose, it's easy for module boundaries to blur under deadline pressure. Mitigate with lint rules or architecture-test tooling that fails CI if one module imports another module's internals directly.

### Cost Impact

Meaningfully lower than microservices at this stage: one set of infrastructure to run and monitor, not N. This is the more cost-efficient choice for a 6-person team's actual current load.

### Scalability Impact

Sufficient for a long runway — most products never need to scale past what a well-built modular monolith can handle, and you can scale it vertically and with read replicas/caching well before module extraction becomes necessary. If a specific module (e.g., real-time dispatch matching) later develops genuinely distinct scaling needs, it's a strong extraction candidate at that point — not before.

### Security Impact

Neutral-to-positive at this stage: fewer network boundaries between modules means fewer places requiring inter-service authentication to get right, which is one less class of security control your small team needs to build and maintain correctly right now.

### Confidence Level

**High.** This is a well-understood problem (team size vs. architecture complexity) with strong consensus in the relevant decision rules (`skills/07_Architecture/`, `skills/00_Core/reference/over-under-engineering.md`) and no unusual constraints in the prompt that would push toward an exception.

### Migration Path

Enforce module boundaries from day one (separate packages, explicit interfaces, no cross-module database access) so that if a specific module later needs independent scaling or a different release cadence, it can be extracted into its own service with a well-defined boundary already in place — extraction becomes a mechanical refactor, not an archaeology project.

---

*This response demonstrates the full 10-part Output Standard defined in `skills/99_Decision_Engine/reference/output-standard-and-confidence.md`, applied via `/archon-principal` mode.*
