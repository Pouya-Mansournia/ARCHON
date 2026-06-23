---
name: archon-review
description: Have ARCHON run an adversarial architecture review on an existing design, codebase description, or a previous recommendation — hunting for over-engineering, under-engineering, single points of failure, and unjustified complexity.
argument-hint: "<system, design doc, or prior recommendation to review>"
---

# /archon-review

Adversarial review (critic) mode. ARCHON stops proposing and starts attacking — its own prior recommendation included.

## Usage

```
/archon-review $ARGUMENTS
```

## What Happens

ARCHON loads `skills/19_Review_Outputs/reference/review-output-standards.md` and `skills/00_Core/reference/over-under-engineering.md`, then runs the design through:

1. **Over-Engineering Detector** — microservices before PMF, Kubernetes for a tiny MVP, Kafka for small background jobs, multi-cloud without regulatory need, custom auth when managed auth suffices, distributed databases without global-scale need, event sourcing without an audit/replay need.
2. **Under-Engineering Detector** — missing backups, missing security controls, no monitoring, no authentication, no rate limiting, missing data model rigor, missing error handling, no real deployment process, unclear ownership boundaries.
3. **Failure Mode Analysis** — single points of failure, blast radius of each component failing, cascading failure paths.
4. **Bottleneck Analysis** — where the design will hit a wall first as load grows, and at roughly what scale.
5. **Risk Ranking** — every identified issue ranked by (likelihood × blast radius), not just listed.

## Output

A risk table (Issue | Category [Over-engineered / Under-engineered / Failure mode / Bottleneck] | Likelihood | Blast Radius | Recommendation) followed by a short prioritized action list (Fix now / Fix before scale / Accept and monitor).

## Example

```
/archon-review Here's our current setup: single EC2 instance running Rails monolith + Postgres + Sidekiq + Redis, no read replica, deploys via SSH + git pull, no staging environment.
```
