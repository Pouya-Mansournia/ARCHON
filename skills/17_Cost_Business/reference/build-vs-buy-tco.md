# Build vs. Buy & Total Cost of Ownership

## Goal

"Build vs. buy" is one of the most consequential and most frequently mis-decided trade-offs a technical organization makes — engineers systematically underestimate the ongoing cost of what they build (maintenance, on-call burden, opportunity cost) and overestimate the limitations of what they could buy instead.

## The Real Comparison: Total Cost of Ownership, Not Sticker Price

| Cost dimension | Build | Buy |
|---|---|---|
| Upfront engineering time | High — full design and implementation cost | Low to moderate — integration effort only |
| Ongoing maintenance | Borne entirely by the team, indefinitely, including security patching and dependency upgrades | Borne by the vendor; the team's cost is staying current with the vendor's API/contract changes |
| Feature evolution | Full flexibility, but every new capability is more engineering time | Bounded by what the vendor offers (or their roadmap, via influence/requests) |
| Opportunity cost | Engineering time spent here isn't spent on differentiating product work | Engineering time freed up for differentiating work |
| Direct cost | Often "free" in the sense of no line-item invoice, but real in engineering hours | A visible, budgeted line-item cost (subscription/usage fees) |

The most common mistake in this analysis is comparing buy's visible subscription cost against build's invisible (but very real) engineering-hours cost and concluding build is "free" — it almost never is once true TCO is accounted for.

## When Building Is the Right Call

- The capability is a genuine, durable competitive differentiator core to the product's value proposition — not a generic, solved problem.
- No vendor solution fits the actual requirement well enough, and the gap is significant (not just a minor feature nice-to-have).
- The team has (or can build) the specific expertise needed, and maintaining it long-term is a cost the business is genuinely willing to bear.
- A specific compliance, data-residency, or strategic-control requirement that available vendor options can't satisfy.

## When Buying Is the Right Call

- The capability is a solved, generic problem (authentication, payments, email delivery, observability tooling) — see the repeated "managed/standard solution by default" pattern across `skills/04_Backend/`, `skills/12_Security/`, and `skills/08_Cloud/`.
- Speed to market matters more than the marginal customization a build would allow.
- The ongoing maintenance burden of building would meaningfully distract from the team's actual differentiating work.

## A Practical Decision Framework

1. Is this capability core to what makes the product differentiated and valuable to customers? If no, default to buy.
2. If yes — does a vendor solution exist that's "good enough," even if not perfect? If yes, buy and revisit later if the gap becomes a real competitive liability.
3. Only build when the capability is both core to differentiation and not adequately served by any available vendor option — and even then, calculate the realistic multi-year TCO (including the ongoing maintenance and opportunity cost) before committing, not just the initial build estimate.

## Vendor Lock-In — A Real but Often Overweighted Risk

Lock-in risk is real and worth factoring in, but it's frequently overweighted relative to its actual probability and cost, leading teams to build internal abstraction layers or even build instead of buy purely to avoid a hypothetical future migration that may never become necessary (this mirrors the multi-cloud over-engineering trigger in `skills/08_Cloud/reference/edge-multi-cloud.md`). Weigh realistic switching cost against the certain, ongoing cost of avoiding lock-in preemptively.

## Common Mistakes

- Comparing a vendor's visible subscription price against a build's invisible-but-real engineering-hour cost and concluding build is cheaper.
- Building a generic, solved-problem capability (auth, payments, basic observability) because "we can do it better," underestimating the ongoing maintenance burden.
- Over-engineering an abstraction layer to avoid hypothetical vendor lock-in at a cost that exceeds the realistic risk being mitigated.
- Treating the build decision as final and never revisiting it as the product matures and the calculus changes (a capability that was reasonably bought early might be worth building later once it becomes a genuine differentiator).

## Decision Rule for This Domain

Default to buy for generic, solved problems. Reserve building for genuine, durable competitive differentiators where no adequate vendor option exists. Evaluate the decision on realistic multi-year total cost of ownership (including maintenance and opportunity cost), not just upfront cost or sticker price comparison.
