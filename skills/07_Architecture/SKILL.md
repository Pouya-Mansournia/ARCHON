---
name: architecture-patterns
description: System architecture patterns — monolith, modular monolith, microservices, event-driven, CQRS, event sourcing, domain-driven design, clean/hexagonal architecture, and service mesh — with explicit stage-aware decision rules for when each pattern earns its complexity.
---

# 07 — Architecture Patterns (L4)

**Level:** L4 — Principal Engineering.

## Goal

Match the structural pattern to the team's actual size, the system's actual complexity, and the actual scaling/ownership pressures present today — architecture patterns are tools for solving specific problems (team coordination at scale, independent deployability, complex domain logic clarity), not badges of engineering maturity.

## Pattern Decision Matrix

| Pattern | Solves | Adopt when | Avoid when |
|---|---|---|---|
| Monolith | Simplicity, fast iteration, easy reasoning about the whole system | Small team, early stage, unclear domain boundaries | Team has grown large enough that independent deploy cadence is now the bottleneck |
| Modular Monolith | Monolith's simplicity + clear internal boundaries that ease a future split | Almost always the right starting point for new products | Never really wrong as a starting point — only outgrown, not avoided |
| Microservices | Independent deployability, independent scaling, team autonomy at scale | Demonstrated team-coordination bottleneck, genuinely independent scaling needs across components | Pre-PMF, small team, unclear domain boundaries — the classic over-engineering trigger |
| Event-Driven Architecture | Decoupling producers from consumers, reacting to business events across boundaries | Multiple independent systems need to react to the same business events | Simple request/response needs being forced into events for no decoupling benefit |
| CQRS | Read and write models with very different shape/scale needs | Read patterns are numerous/complex and genuinely different from the write model | Most CRUD apps, where read and write models are naturally similar |
| Event Sourcing | Full audit/replay of state changes | Regulatory audit trail or genuine replay/rebuild-state need | Used by default for typical CRUD — adds real query complexity for no corresponding benefit |
| Domain-Driven Design | Managing complex business logic clarity across a large domain | Genuinely complex business domain with rich rules (e.g., a logistics/pricing/insurance engine) | Simple CRUD domains where DDD's ceremony (aggregates, bounded contexts, ubiquitous language) outweighs its clarity benefit |
| Clean / Hexagonal Architecture | Decoupling business logic from frameworks/infrastructure for testability and swap-ability | Long-lived systems where infrastructure (DB, framework) is likely to change, or testability is a priority | Short-lived prototypes where the abstraction overhead isn't earning its keep |

## Decision Rule

Start every new product as a **modular monolith**. Define clear internal module boundaries (by domain, not by technical layer) from day one — this is nearly free and makes a future extraction mechanical rather than a rewrite. Only extract a true microservice when there's a demonstrated, specific need: a team that needs to deploy independently of others, or a component with genuinely different scaling characteristics from the rest of the system (e.g., a video transcoding service vs. the main API).

## Reference Files

- `reference/architecture-patterns.md` — full pattern deep dive with concrete examples and migration paths between patterns.
- `reference/service-mesh.md` — when a service mesh (Istio, Linkerd) earns its operational complexity, and what it solves that a simpler approach doesn't.
