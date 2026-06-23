# Incident Management & Chaos Engineering

## Goal

Incidents are inevitable in any non-trivial system — the differentiator between teams isn't whether incidents happen, it's how quickly they're detected, how calmly and effectively they're resolved, and how much the organization actually learns from each one. (See the `engineering:incident-response` skill for the live triage/communication/postmortem workflow itself; this file covers the surrounding architecture and practices.)

## Severity Classification

| Severity | Definition | Example response expectation |
|---|---|---|
| SEV1 / Critical | Complete outage or major data integrity issue affecting most/all users | Immediate, all-hands-on-deck response, continuous status updates |
| SEV2 / High | Significant degradation or a major feature broken for a meaningful subset of users | Urgent response, regular status updates |
| SEV3 / Medium | Minor degradation, workaround available, limited user impact | Addressed within normal working hours/process |
| SEV4 / Low | Cosmetic or negligible-impact issue | Backlog, no urgent response needed |

Define severity levels and their response expectations before an incident happens — deciding severity classification in the middle of an active incident wastes time that should go to resolution.

## Incident Response Process (Architecture-Level View)

1. **Detection** — automated alerting (ideally) or user/internal report.
2. **Triage** — assign severity, assemble the right responders, establish a communication channel.
3. **Mitigation** — stop the bleeding (rollback, feature flag disable, scale up, failover) — mitigation comes before full root-cause diagnosis when user impact is ongoing.
4. **Resolution** — confirm the system is back to a healthy state.
5. **Postmortem** — blameless analysis of what happened, why, and what changes (technical and process) will reduce recurrence likelihood or impact.

## Designing Systems for Fast Mitigation

- **Feature flags** to disable a problematic feature instantly without a full deploy cycle.
- **Fast, reliable rollback** as a first-class deployment capability, not an afterthought (see `skills/09_DevOps/reference/cicd-gitops.md` and `engineering:deploy-checklist`).
- **Circuit breakers** on calls to dependencies, so a failing downstream service degrades gracefully rather than cascading into a full outage.
- **Clear ownership boundaries** so responders know who to page for which component — see the Under-Engineering Detector's "unclear ownership boundaries" trigger in `skills/00_Core/reference/over-under-engineering.md`.

## Chaos Engineering

Chaos engineering deliberately injects failure (killing instances, introducing network latency, simulating dependency outages) into a system — usually starting in a non-production or carefully-scoped production environment — to validate that resilience assumptions (failover works, retries behave correctly, alerts actually fire) hold true before a real failure tests them unexpectedly.

| When it's warranted | When it's premature |
|---|---|
| A system mature enough to have meaningful redundancy/failover mechanisms worth validating, serving real production traffic where reliability genuinely matters | An early-stage system without the redundancy mechanisms chaos testing would be validating in the first place — there's nothing to test yet |

**Decision rule:** Chaos engineering earns its complexity once a system has real redundancy/failover design to validate. Running chaos experiments against a system with no redundancy just confirms what's already known (it has a single point of failure) without the structured practice adding new information.

## Blameless Postmortems

Focus on systemic and process causes, not individual blame — a postmortem culture that punishes the person who happened to be on call when an incident occurred trains people to hide problems rather than surface them. Every postmortem should produce concrete action items with owners, not just a narrative.

## Common Mistakes

- No defined severity levels, leading to wasted time arguing about urgency during an active incident.
- No fast rollback/feature-flag capability, turning mitigation into a slow full redeploy under pressure.
- Postmortems that assign blame to individuals rather than examining systemic/process causes, discouraging honest incident reporting.
- Running chaos engineering experiments before the system has any real redundancy to validate, or running them in production without adequate safeguards/blast-radius control.

## Decision Rule for This Domain

Define severity levels and a response process before they're needed. Build fast mitigation capability (rollback, feature flags, circuit breakers) into the system's design. Run blameless postmortems with concrete action items. Adopt chaos engineering only once there's real redundancy worth validating.
