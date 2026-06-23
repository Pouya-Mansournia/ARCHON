# Technical Debt Management

## Goal

Technical debt is a legitimate, often correct trade-off (shipping faster now in exchange for cleanup work later) — the failure mode isn't taking on debt, it's taking it on invisibly and never revisiting it. (See the `engineering:tech-debt` skill for the tactical audit/prioritization workflow; this file covers the underlying philosophy.)

## Categorizing Debt

| Category | Example | Typical urgency |
|---|---|---|
| Deliberate, tracked debt | "We're hardcoding this config to ship the MVP faster, will generalize after we validate demand" | Low until the triggering condition (validated demand) occurs — then it should be addressed |
| Deliberate, untracked debt | The same shortcut taken with no record of it anywhere | Hidden risk — it will be rediscovered at an inconvenient time, often by someone who didn't make the original trade-off and lacks the context |
| Accidental debt (from learning) | An early design choice that made sense with the team's understanding at the time, now understood to be suboptimal | Variable — reassess against current priorities, not against the embarrassment of having been wrong earlier |
| Bit rot / decay | Code that was fine but has degraded in fit as the surrounding system evolved (an unmaintained dependency, an integration pattern the rest of the codebase has moved away from) | Variable — often surfaces as friction in unrelated work and is best caught by noticing that friction pattern |

## The Core Discipline: Make Debt Visible

The single highest-leverage practice in debt management is simply recording it at the moment it's incurred — a ticket, a `TODO` with context and a ticket reference, a note in the relevant design doc. Untracked debt is the kind that compounds invisibly and gets rediscovered as a crisis rather than addressed on a sane schedule.

## Prioritizing Debt Against Feature Work

Debt competes with every other backlog item for the same finite engineering capacity, so it needs the same kind of impact/cost reasoning as a feature: what's the actual cost of carrying this debt longer (slower future work in this area, increased bug risk, onboarding friction for new team members) versus the cost of paying it down now (engineering time that could go to user-facing work)? Debt that's actively slowing down current feature work or causing recurring incidents should be prioritized highly; debt in a rarely-touched, stable area can reasonably wait indefinitely.

## Allocating Dedicated Capacity

Many effective teams reserve a standing percentage of engineering capacity (commonly cited ranges are 10-20%) for debt paydown and maintenance work, rather than relying on debt being prioritized ad hoc against feature pressure every single sprint — ad hoc prioritization systematically loses to features with a visible launch date and a stakeholder asking about them.

## Common Mistakes

- Taking on debt with no record of it, guaranteeing it gets rediscovered at an inconvenient time with none of the original context.
- Treating all debt as equally urgent, leading either to debt paydown crowding out feature work or features perpetually crowding out debt paydown.
- No dedicated capacity for maintenance work, so debt paydown only happens during rare lulls or after a debt-caused incident forces the issue.
- Conflating "code I'd write differently today" with "debt actively causing harm" — not all retrospective dissatisfaction with past decisions is debt that needs paying down.

## Decision Rule for This Domain

Record debt the moment it's taken on, with enough context for someone else to understand the trade-off later. Prioritize paydown based on actual current cost (velocity drag, incident risk), not just age or discomfort. Reserve some standing capacity for debt work so it doesn't perpetually lose to feature pressure.
