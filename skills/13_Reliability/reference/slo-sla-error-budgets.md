# SLOs, SLAs & Error Budgets

## Goal

Reliability targets should be explicit, measured, and tied to actual user/business impact — "we want to be as reliable as possible" is not an actionable target; "99.9% of API requests succeed within 300ms, measured monthly" is.

## Definitions

| Term | Definition |
|---|---|
| SLI (Service Level Indicator) | A specific, measured metric of system behavior (e.g., request success rate, latency percentile) |
| SLO (Service Level Objective) | An internal target for an SLI (e.g., "99.9% of requests succeed") |
| SLA (Service Level Agreement) | An external, often contractual commitment to a service level, typically with consequences (credits, penalties) for missing it |
| Error budget | The allowed amount of unreliability implied by an SLO (e.g., a 99.9% SLO allows roughly 43 minutes of full downtime per month) |

SLOs should generally be set somewhat stricter than any external SLA, so there's a buffer to detect and respond to degradation before it breaches a contractual commitment.

## Choosing SLOs That Matter

- **Tie SLOs to user-facing outcomes**, not internal implementation details — "checkout completes successfully" is a better SLO target than "database CPU stays below 80%."
- **Don't over-set precision** — 99.99% ("four nines") implies under an hour of downtime per year and demands a level of engineering investment (redundancy, automated failover, rigorous testing) that's only worth it for systems where that level of reliability has real, measurable business value. Most products are well served by 99.9% or even 99.5% targets.
- **Set SLOs per critical user journey**, not just one number for the whole system — a checkout flow and a "view profile settings" page don't warrant the same reliability bar.

## Error Budgets as a Governance Tool

Once an SLO is defined, the error budget it implies can drive concrete decisions: if the error budget for the period is already spent, prioritize reliability work and slow down on risky feature releases; if there's ample budget remaining, that's a signal there's room to take on calculated risk (a faster release cadence, a more ambitious infrastructure change) without violating the reliability commitment. This turns "reliability vs. velocity" from a recurring subjective argument into a data-driven, pre-agreed policy.

## Practical Staging

| Stage | SLO practice |
|---|---|
| Pre-PMF | Informal reliability awareness; formal SLOs are premature — the product itself may still be the wrong one |
| Early growth | Define SLOs for the 1-3 most critical user journeys; track but don't yet gate releases on them |
| Mature/scale | Formal SLOs across critical paths, with error budgets actively informing release/risk decisions, often paired with external SLAs for enterprise customers |

## Common Mistakes

- Setting an SLO target (e.g., 99.99%) without evaluating whether the business value of that reliability level justifies its engineering cost.
- Defining SLOs around internal infrastructure metrics rather than the user-facing outcomes that actually matter.
- Treating an SLO as a one-time-set-and-forget number rather than revisiting it as the product, user expectations, and architecture evolve.
- Offering an external SLA stricter than or equal to the internal SLO, leaving no buffer to detect and fix degradation before breaching the contractual commitment.

## Decision Rule for This Domain

Define SLOs per critical user journey, tied to user-facing outcomes, set realistically against actual business value rather than aspirational perfection. Use the resulting error budget as an explicit, pre-agreed input to release and risk decisions rather than litigating reliability-vs-velocity trade-offs case by case.
