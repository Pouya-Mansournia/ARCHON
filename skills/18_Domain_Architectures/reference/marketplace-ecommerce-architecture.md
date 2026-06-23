# Reference Architecture: Marketplace & E-Commerce

## Goal

Marketplace and e-commerce products share a distinguishing architectural challenge that most SaaS products don't face: they coordinate at least two distinct user populations (buyers and sellers, or customers and the storefront operator) around inventory, search/discovery, and money movement, with correctness requirements (don't oversell inventory, don't lose a payment) that are unusually strict for a typical web product.

## Representative Stack

| Layer | Choice | Why |
|---|---|---|
| Catalog & search | PostgreSQL for the catalog system of record + a dedicated search engine (Elasticsearch/Meilisearch) once catalog size/query complexity justifies it | Faceted search, relevance ranking, and typo-tolerant search are core to discovery UX and exceed what SQL-native search handles well at any real catalog size (see `skills/05_Database/reference/search-architecture.md`) |
| Inventory | Strongly consistent transactional writes against PostgreSQL, with explicit locking/optimistic-concurrency handling for stock decrements | Overselling inventory is a correctness bug with direct business and customer-trust consequences — this is one of the few places where consistency must clearly win over availability/latency trade-offs |
| Payments | A payments provider (Stripe or equivalent) via their hosted/managed flow — never custom card-handling | PCI-DSS scope reduction and the "never roll your own" security default both point firmly at a managed provider (see `skills/12_Security/reference/data-protection-encryption.md`) |
| Order/checkout flow | Synchronous for the critical path (payment authorization), asynchronous (queue-based) for everything that can happen after payment succeeds (confirmation emails, fulfillment triggers, analytics events) | Keeps the user-facing checkout latency low while ensuring downstream side effects are reliably processed via the outbox pattern (see `skills/06_API/reference/messaging-event-driven.md`) |
| Search/discovery caching | CDN/edge caching for product listing pages, cache-aside for frequently-viewed product detail data | High read-to-write ratio on catalog browsing makes this one of the highest-leverage caching opportunities in the whole system |
| Multi-sided notifications | Event-driven architecture notifying both buyer and seller sides of relevant state changes (order placed, shipped, refunded) | Two distinct user populations need independently-tailored notifications off the same underlying event stream |

## The Hard Problem: Consistency at the Inventory/Payment Boundary

The single highest-stakes correctness requirement in this category is ensuring a successful payment and a successful inventory reservation happen together, reliably, even under concurrent requests or partial failures. The standard pattern: reserve inventory optimistically at checkout start (with a time-boxed hold), confirm the reservation atomically with payment success (often via the outbox pattern to reliably trigger downstream effects), and release the hold automatically if payment doesn't complete within the window. Treat this flow with the same rigor as a financial system's transaction handling — it effectively is one.

## Search & Discovery as a Differentiator

For marketplaces specifically, search/discovery quality is often a direct driver of conversion and a real competitive differentiator (helping buyers find the right item among many sellers' listings) — this typically justifies a dedicated search engine earlier in the product's life than a typical SaaS product would need one, since search relevance directly impacts revenue rather than being a secondary feature.

## What Changes as the Product Scales

- **Catalog size growth** → search engine becomes necessary (if not already adopted), sharding/partitioning considerations for the catalog database.
- **Transaction volume growth** → payment/order processing may need dedicated scaling attention (read replicas for order history queries, queue throughput for fulfillment events) ahead of the rest of the system.
- **Seller/operational tooling growth** → a seller-facing dashboard and operations becomes its own significant surface area, often justifying its own team and potentially its own service boundary once large enough.

## Common Mistakes

- Treating inventory decrements as a simple, unguarded database update, leading to overselling under concurrent checkout load.
- Hand-building payment card handling instead of using a managed provider's hosted flow, taking on unnecessary PCI compliance scope and security risk.
- Underinvesting in search/discovery quality despite it being a direct revenue driver for marketplace conversion.
- No time-boxed inventory hold during checkout, leaving abandoned checkouts to lock up inventory indefinitely.

## Decision Rule for This Domain

Treat the inventory-payment consistency boundary as the architecture's most safety-critical path, deserving transactional rigor. Use a managed payments provider without exception. Invest in dedicated search/discovery infrastructure earlier than a typical SaaS product would, given its direct link to marketplace conversion.
