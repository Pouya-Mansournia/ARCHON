# Example: `/archon-review` — Checkout Flow Critique

**Prompt:**

```
/archon-review Here's our checkout flow: the frontend calls our API directly with the cart contents and a price total computed client-side; the API charges the card via Stripe for that total, then writes the order to Postgres. What's wrong with this?
```

**Response:**

### Summary

The checkout flow has one critical, immediately exploitable vulnerability (trusting a client-supplied price) and two secondary gaps (no idempotency on payment capture, no explicit inventory-consistency handling). The Stripe integration choice itself is sound — the issues are all in how the surrounding flow trusts client input and handles failure/retry cases.

### Findings

**1. Client-supplied price is trusted for payment** — Category: Security — Severity: Critical
The API charges whatever total the frontend sends, rather than recomputing the price server-side from the cart contents and current catalog prices. This is directly exploitable: any user can modify the request to charge $0.01 for any cart. Recommendation: recompute the total server-side from trusted catalog data immediately before charging; never accept a price from the client as authoritative. See `skills/12_Security/reference/threat-modeling-appsec.md` on validating all external input.

**2. No idempotency key on the Stripe charge** — Category: Reliability — Severity: High
A network retry (client-side timeout-and-retry, or a transient failure between charge and order-write) without an idempotency key risks double-charging the customer. Recommendation: generate an idempotency key per checkout attempt and pass it to Stripe's charge call, so retries are safely deduplicated.

**3. No explicit inventory-consistency handling** — Category: Correctness — Severity: Medium
Nothing in the described flow addresses concurrent purchase of the last unit of an item (overselling). Recommendation: reserve inventory atomically before charging, or accept the charge and handle oversell as an explicit refund-and-notify path — pick one deliberately rather than leaving it unhandled. See `skills/18_Domain_Architectures/reference/marketplace-ecommerce-architecture.md`.

**4. Payment and order-write aren't described as a single consistent operation** — Category: Reliability — Severity: Medium
If the charge succeeds but the order write fails (crash, DB error), the customer is charged with no order on record. Recommendation: write the order in a "pending" state before charging, then confirm it on charge success — or use a saga/outbox pattern if this flow grows more steps — so there's always a recoverable record tying the charge to an order.

### Risk Ranking

1. Client-trusted pricing (Critical — actively exploitable, direct financial loss)
2. Missing idempotency (High — will cause real double-charges under normal network conditions, not just attack scenarios)
3. Payment/order-write consistency gap (Medium — recoverable but creates support burden and reconciliation risk)
4. Inventory consistency (Medium — depends on actual contention; low risk for low-volume SKUs, real risk for popular/limited items)

### What's Working Well

Routing payment through Stripe rather than handling card data directly is the right call — it keeps PCI scope minimal (see `skills/12_Security/reference/compliance-governance.md`). Writing the order to Postgres as the source of truth, rather than relying on Stripe's records as the system of record, is also sound.

---

*This response demonstrates the structured review format defined in `skills/19_Review_Outputs/reference/review-output-standards.md`, applied via `/archon-review` mode.*
