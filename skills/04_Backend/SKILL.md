---
name: backend-architecture
description: Backend language and framework selection — Node.js/TypeScript, Python, Go, Java, C#/.NET, Rust, PHP — with decision rules based on team skills, performance needs, and ecosystem fit.
---

# 04 — Backend Architecture (L2)

**Level:** L2 — Software Engineering.

## Goal

Pick a backend language/framework combination that matches the team's existing skills, the workload's actual performance profile, and the ecosystem maturity needed — not the language that's most discussed online this year.

## Decision Matrix

| Language/Framework | Best for | Avoid when |
|---|---|---|
| Node.js / TypeScript (Express, Fastify, NestJS) | Teams already strong in JS/TS wanting one language across frontend and backend; I/O-bound workloads (most typical web/API backends) | CPU-bound, heavy computational workloads (use a worker in a different language/runtime for that specific job instead) |
| Python (FastAPI, Django) | Data/ML-heavy products needing the Python ecosystem (numpy, pandas, ML frameworks); teams prioritizing developer velocity and readability | Extremely high-throughput, low-latency requirements where Python's runtime overhead becomes the bottleneck |
| Go | High-concurrency network services, infrastructure/platform tooling, teams wanting strong performance with a small, simple language | Teams needing rich, mature web-framework batteries-included conventions (Go's ecosystem is more do-it-yourself) |
| Java / Kotlin (Spring Boot) | Large enterprise systems, teams with strong JVM expertise, need for mature, battle-tested ecosystem and tooling at scale | Small teams/startups where Spring Boot's ceremony and JVM resource footprint outweigh its benefits |
| C# / .NET | Teams already in the Microsoft ecosystem, enterprise systems, strong tooling and performance balance | No existing .NET expertise and no specific ecosystem requirement pulling toward it |
| Rust | Systems programming, extreme performance/safety requirements, embedded or latency-critical services | Most typical product/web backends — the productivity cost rarely pays for itself outside specific high-stakes performance/safety contexts |
| PHP (Laravel) | Fast CRUD-heavy web apps, teams with existing PHP expertise, large legacy PHP codebases | Greenfield projects with no existing PHP bias — there are usually now-easier defaults |

## Decision Rule

Default to the language/framework the team already has the deepest expertise in, unless the workload has a specific, named characteristic (CPU-bound at scale, extreme latency budget, ML/data ecosystem dependency) that points elsewhere. Language choice is rarely the highest-leverage decision in a system's success — architecture, data model, and operational discipline matter more in the vast majority of products. Don't let language selection consume disproportionate decision-making time relative to its actual impact.

## Reference Files

- `reference/backend-architecture.md` — full language/framework comparison, async/concurrency models, and API layer design considerations.
