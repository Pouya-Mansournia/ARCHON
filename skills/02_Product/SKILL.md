---
name: product-business
description: Product, business, and requirements discovery — the 16 questions that must be answered before any architecture decision, product category patterns, and product engineering (MVP/PMF) discipline. Load this before any system design begins; architecture without product context is guessing.
---

# 02 — Product, Business & Requirements Discovery (L2)

**Level:** L2 — Software Engineering, with direct ties to L5 business context.

## Goal

No architecture decision is correct or incorrect in a vacuum — it's correct or incorrect relative to the product's actual users, scale, stage, and constraints. This domain is the discovery layer that every other domain's decisions should be conditioned on.

## The 16 Required Discovery Questions

Before any non-trivial architecture recommendation, get answers (or explicit "unknown, here's our best assumption") to:

1. What problem does this product solve, and for whom?
2. Who are the actual users (consumer, business, internal, developer)?
3. What's the current stage (idea, MVP, early traction, scaling, mature)?
4. What's the team size and skill composition?
5. What's the expected user/request scale in the next 6-12 months?
6. What's the budget/cost sensitivity?
7. What's the timeline pressure (weeks, months, no hard deadline)?
8. Are there compliance/regulatory requirements (GDPR, HIPAA, SOC2, PCI-DSS)?
9. What's the data sensitivity level (PII, financial, health, none)?
10. What's the expected geographic distribution of users?
11. What's the required uptime/reliability bar?
12. What existing systems/infrastructure must this integrate with?
13. What's the monetization model (if any), and does it impose technical requirements (metering, billing)?
14. What's explicitly NOT in scope for this version?
15. Who are the competitors, and what's the differentiation?
16. What does success look like in 90 days, and how is it measured?

## Product Categories & Their Default Architecture Gravity

| Category | Typical gravity |
|---|---|
| Website / Marketing Site | Static-first, CDN, minimal backend |
| SaaS (B2B) | Multi-tenant data model, RBAC, billing integration, audit logs early |
| Marketplace | Two-sided data model, trust/reputation systems, payment + payout architecture |
| E-Commerce | Inventory consistency, payment processing, search/catalog performance |
| AI Product | Model/inference cost as a first-class architecture input, latency budget, evaluation pipeline |
| IoT Product | Offline-first device behavior, fleet provisioning, OTA updates |
| Robotics Product | Real-time + safety constraints, edge/cloud split, simulation-first development |
| Internal Tool | Lower reliability bar usually acceptable, but data correctness still matters; optimize for build speed |

Full treatment: `reference/product-discovery-requirements.md`, `reference/business-architecture-patterns.md`, `reference/product-engineering-mvp-pmf.md`.

## Decision Rule

If a user asks an architecture question without providing this context, ask for the smallest subset of the 16 questions that would actually change the recommendation — don't interrogate with all 16 if 3 of them already make the answer clear.

## Reference Files

- `reference/product-discovery-requirements.md` — full discovery framework and category-specific question sets.
- `reference/business-architecture-patterns.md` — how business model shapes technical requirements (billing, multi-tenancy, marketplace trust).
- `reference/product-engineering-mvp-pmf.md` — MVP scoping discipline, product-market-fit-aware architecture pacing.
