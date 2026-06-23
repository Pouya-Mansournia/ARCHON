# Business Architecture Patterns

## Goal

Business model decisions impose specific, often non-obvious technical requirements. Getting these wrong early is expensive to retrofit because they tend to be woven through the data model, not isolated to one service.

## Billing & Monetization Models

| Model | Technical implications |
|---|---|
| Subscription (seat-based) | Need a billing provider integration (Stripe Billing, Chargebee), seat counting logic synced with auth/org membership, proration handling for mid-cycle seat changes |
| Usage-based / metered | Need a metering pipeline that's accurate and auditable (usage events → aggregation → invoice), idempotent event ingestion (double-counting on retry is a real, recurring bug class), and a clear definition of the billable unit decided early — changing it later is a customer-facing, contractual change |
| Transaction-based (take a cut) | Need payment + payout splitting (Stripe Connect or equivalent), careful handling of refunds/chargebacks affecting both parties, reconciliation reporting |
| Freemium | Need usage limit enforcement that's reliable under concurrency (two simultaneous requests shouldn't both succeed past a hard limit due to a race condition) and a clear upgrade path technically (not just a pricing page) |
| Ad-supported | Need to design for very high request volume at very low cost-per-request from day one — this fundamentally shapes infrastructure choices toward cost-optimized, high-throughput patterns |

**Decision rule:** Decide the billable unit and metering granularity before building the core data model — retrofitting usage tracking onto a system that wasn't designed to record it accurately is a common, expensive mistake.

## Multi-Tenancy as a Business-Driven Decision

The choice of multi-tenancy model (see `skills/18_Domain_Architectures/reference/saas-b2b-architecture.md`) is as much a business decision as a technical one:
- Enterprise customers needing data residency guarantees or wanting "their own database" for compliance/contractual reasons push toward database-per-tenant.
- Cost-sensitive, high-volume, low-ACV (annual contract value) customers push toward shared-schema multi-tenancy for unit economics.

## Trust & Reputation Systems (Marketplaces, Platforms)

- Reviews/ratings need abuse-resistance from day one (fake reviews, review bombing) — this is a security and product-integrity concern simultaneously.
- Verification (identity, business legitimacy) requirements scale with transaction value and risk — a low-value goods marketplace needs less verification rigor than a high-value services marketplace or a financial platform.

## Compliance as a Sales Requirement, Not Just a Legal One

SOC2 Type II, in particular, is frequently not a legal requirement but a sales requirement — many enterprise buyers will not sign a contract without it. This means the technical controls SOC2 requires (access logging, change management, vendor risk management) often need to be designed in well before the company is contractually forced to by an actual regulation. See `skills/12_Security/reference/compliance-governance.md`.

## Build vs. Buy Through a Business Lens

Every build-vs-buy decision (see `skills/17_Cost_Business/reference/build-vs-buy-tco.md`) should be evaluated against: does building this differentiate us competitively, or is it undifferentiated heavy lifting that a vendor already solves well? Time spent building undifferentiated infrastructure is time not spent on the product's actual differentiation.

## Required Output for This Domain

When a business model detail (billing model, tenancy expectations, compliance sales requirements) materially shapes the technical design, name it explicitly as a driving constraint in the recommendation — don't bury a business-driven requirement inside what looks like a purely technical choice.
