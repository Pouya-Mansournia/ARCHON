# Multi-Region Architecture

## Goal

Multi-region is one of the most expensive architectural commitments a system can take on — data replication complexity, consistency trade-offs, deployment complexity, and cost all multiply. Apply it only when a specific, real requirement demands it, and choose the lightest pattern that satisfies that requirement.

## When Multi-Region Is Actually Justified

| Driver | What it actually requires |
|---|---|
| Data residency / regulatory compliance (e.g., GDPR requiring EU data to stay in the EU) | Data for in-scope users physically stored/processed in the required region — often satisfiable with regional data partitioning, not full multi-region active-active |
| Demonstrated latency problem for a specific user geography | Often satisfiable by a CDN/edge cache for read-heavy content before justifying full regional application deployment |
| Disaster recovery beyond single-region backup/restore | A genuine RTO/RPO requirement tighter than "restore from backup in another region within N hours" — see `skills/05_Database/reference/storage-architecture.md` for RTO/RPO definitions |
| Global user base with real latency-sensitive interactivity (e.g., real-time multiplayer, live collaboration) | True multi-region active deployment, the most complex and expensive driver to satisfy |

**Decision rule:** Before building multi-region, ask which specific driver above applies. "We might go global someday" is not a driver — it's a hypothesis that should be validated by actual user geography data first.

## Multi-Region Patterns

| Pattern | How it works | Complexity | Use when |
|---|---|---|---|
| Single-region + cross-region backup | Primary region serves all traffic; backups replicated to a second region for disaster recovery only | Low | The default for most products — covers DR without ongoing multi-region complexity |
| Active-passive (warm standby) | Secondary region kept in sync (via replication) but not serving live traffic; promoted on primary failure | Moderate | A real DR/uptime requirement beyond what backup-restore provides, without needing active multi-region latency benefits |
| Active-active | Multiple regions simultaneously serving live traffic, with data replicated/partitioned across them | High | Genuine global latency requirements or extreme availability requirements — the most operationally demanding pattern, with real data-consistency trade-offs (see below) |

## Data Consistency in Active-Active

Active-active forces an explicit choice on the CAP-theorem spectrum for any data that can be written in more than one region: either accept eventual consistency with conflict resolution (last-write-wins, CRDTs, or application-level merge logic) or restrict writes for a given record to a single "home" region (avoiding multi-region write conflicts at the cost of not being fully active-active for writes). Most systems that claim "active-active" in practice use the latter — active-active for reads, single-home-region for writes per record/tenant.

## The Staged Path

1. Single region, properly architected with good backups and a tested restore process (the foundation almost everyone needs and most of what "DR" really means in practice).
2. Add a CDN/edge cache for static and cacheable content to solve most latency complaints without touching the application architecture.
3. Add active-passive cross-region failover only once a specific availability SLA requires it.
4. Reach for active-active only with a validated, specific global-latency or extreme-availability requirement — and budget for the real engineering cost of data-conflict handling.

## Common Mistakes

- Building active-active multi-region for a product with no validated global user base, driven by aspiration rather than data.
- Underestimating the data-consistency engineering cost of active-active and discovering conflict-resolution bugs in production.
- Treating "we have a backup in another region" as equivalent to a tested DR plan — a backup that's never been restored is not a disaster recovery plan.

## Decision Rule for This Domain

Default to single-region with cross-region backups and a CDN for static content. Escalate to active-passive or active-active only against a named, specific driver from the table above, and document that driver explicitly (it belongs in the ADR — see the `/archon-principal` Output Standard's "Why this choice" field).
