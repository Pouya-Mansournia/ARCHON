# Showcase

A few scenarios illustrating the kind of value ARCHON is built to provide — structured, trade-off-explicit engineering judgment instead of a quick opinion.

## Scenario 1: Stopping an Over-Engineering Decision Before It Ships

**Situation:** A 3-person team building their first product proposes a Kubernetes cluster across 3 environments "to do things properly from day one."

**Without ARCHON:** The team ships it. Three months later, two of the three engineers spend a disproportionate share of their time on cluster operations instead of product work, and the third environment was never actually used.

**With ARCHON (`/archon-review` or `/archon`):** The Over-Engineering Detector (`skills/00_Core/reference/over-under-engineering.md`) flags Kubernetes-for-an-MVP as a named, common trigger and the response recommends a managed container platform (Cloud Run, App Service, or ECS Fargate) instead — with the explicit migration path back to Kubernetes once there's a concrete, named operational need (multiple services needing independent scaling, a real multi-region requirement) rather than a hypothetical one. The team ships faster and spends its scarce engineering time on the product.

## Scenario 2: Catching an Under-Engineering Gap Before an Incident

**Situation:** A team asks for help speeding up their deployment process. Nothing in the question mentions security.

**Without ARCHON:** The question gets answered narrowly — deployment speed improves, but the system still has no automated dependency vulnerability scanning, a gap nobody asked about.

**With ARCHON:** The Security-by-Default checklist in `skills/12_Security/SKILL.md` runs as a standing baseline check regardless of what was explicitly asked, and the response surfaces the missing dependency-scanning gap alongside the deployment-speed answer — because under-engineering gaps (missing auth, no backups, no monitoring, no dependency scanning) are checked by default, not only when directly asked about.

## Scenario 3: Turning a Disagreement Into a Documented Decision

**Situation:** Two engineers disagree about whether to extract a service from the monolith.

**Without ARCHON:** The disagreement gets resolved verbally in a meeting, the reasoning isn't written down, and six months later nobody remembers why the decision went the way it did when a new engineer asks to revisit it.

**With ARCHON (`/archon-principal`):** The response applies the Engineering Decision Principles priority order to the specific trade-off, produces output in the full 10-part Output Standard, and is structured to drop directly into an ADR (`skills/19_Review_Outputs/reference/adr-decision-log-templates.md`) — so the decision, its alternatives, and its trade-offs are preserved as a durable record, and `/archon-reflect` can revisit it later with full context instead of re-litigating from scratch.

## Scenario 4: A Robotics Team Avoiding a Safety Architecture Mistake

**Situation:** A robotics startup wants their obstacle-avoidance logic to run as one more node alongside everything else in their ROS 2 graph, gated by the same QoS settings as their telemetry topics.

**With ARCHON (`/archon-robotics`):** `skills/11_Robotics/reference/robotics-architecture-ros.md` flags that QoS misconfiguration on safety-critical topics is a named common mistake, and `skills/11_Robotics/SKILL.md`'s architecture layering table makes the case for an architecturally independent safety supervisor with override authority — not a peer node that can fail silently alongside everything else. This is the kind of domain-specific safety judgment a general-purpose coding assistant without robotics-specific knowledge would likely miss.
