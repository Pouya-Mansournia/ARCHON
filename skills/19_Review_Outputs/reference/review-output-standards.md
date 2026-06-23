# Review Output Standards

## Goal

`/archon-review` mode exists to critique an existing system, proposal, or decision with the same rigor `/archon-principal` mode applies to making a new one. This file defines the structured critique format so review output is consistent, actionable, and not just a list of vague concerns.

## The Review Output Structure

```
## Summary
One or two sentences: overall assessment and the single highest-priority finding.

## Findings
For each finding:
- **What**: the specific issue (cite the file/component/decision)
- **Category**: Over-engineering | Under-engineering | Security | Reliability |
  Performance | Cost | Maintainability | Team/Process
- **Severity**: Critical | High | Medium | Low
- **Why it matters**: concrete consequence if left unaddressed
- **Recommendation**: the specific change, with trade-offs if relevant

## Risk Ranking
Findings ordered by (likelihood × impact), highest first — not by
the order they were noticed.

## What's Working Well
Explicitly name what shouldn't change — a review that only lists
problems implies everything else is also suspect, which is rarely true
and undermines trust in the critique.
```

## Severity Calibration

| Severity | Definition |
|---|---|
| Critical | Active risk of data loss, security breach, or outage; should block release/merge |
| High | Significant risk or cost if unaddressed within a reasonably short window |
| Medium | Real issue worth fixing, not urgent |
| Low | Minor improvement, optional |

Calibrate severity against actual likelihood and impact (the same risk-ranking logic used throughout `skills/00_Core/`), not against how easy or interesting the fix is — an easy fix for a low-impact issue should not outrank a hard fix for a critical one in the findings order.

## Connecting Review Findings to the Rest of the Knowledge Base

Every finding should, where applicable, reference the specific domain skill and decision rule it relates to (e.g., "this is the Kafka-for-small-background-jobs over-engineering trigger from `skills/00_Core/reference/over-under-engineering.md`") — this makes the critique traceable to a documented standard rather than reading as a personal opinion, and gives the recipient a reference to study if they want to understand the reasoning more deeply.

## Composing with the Principal-Engineer Output Standard

When a review finding leads to a concrete recommendation for a different approach, that recommendation should follow the same 10-part Output Standard `/archon-principal` mode uses (What to use, Why this choice, Why not alternatives, Trade-offs, Risks, Cost impact, Scalability impact, Security impact, Confidence level, Migration path) — a review's recommendations are still architecture recommendations and deserve the same rigor as a from-scratch one.

## Common Mistakes

- Listing findings in the order they were noticed rather than ranked by actual risk, burying the most important issue in the middle of a long list.
- Severity inflation — marking everything "Critical" dilutes the signal and trains recipients to discount the rating.
- A purely negative review with no acknowledgment of what's working, which reads as adversarial and makes the findings harder to act on calmly.
- Vague findings ("this seems risky") without a specific, concrete recommendation attached.

## Decision Rule for This Domain

Structure every review around ranked, severity-calibrated findings with concrete recommendations, explicitly connected to the relevant domain skill's decision rule. Always include what's working well. Treat any recommended alternative with the same Output Standard rigor as a fresh `/archon-principal` recommendation.
