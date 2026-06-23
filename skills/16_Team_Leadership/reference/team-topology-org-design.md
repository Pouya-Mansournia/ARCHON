# Team Topology & Organizational Design

## Goal

Conway's Law isn't a curiosity, it's a design constraint: the software architecture and the team structure that builds it will converge toward mirroring each other whether or not that's planned. Design team topology deliberately, the same way system architecture is designed deliberately — an accidental org structure produces an accidental, fragmented architecture.

## The Four Fundamental Team Types (Team Topologies Model)

| Team type | Purpose | Example |
|---|---|---|
| Stream-aligned | Owns a continuous flow of work tied to a business domain/value stream, end to end | A team owning the checkout experience, front to back |
| Platform | Provides internal services/tooling that stream-aligned teams consume, reducing their cognitive load | An internal developer platform team providing deployment/observability tooling as a self-service product |
| Enabling | Helps stream-aligned teams adopt new capabilities, then steps back rather than embedding permanently | A team helping other teams adopt a new architecture pattern or testing practice |
| Complicated-subsystem | Owns a component requiring deep specialist knowledge that shouldn't be duplicated across every stream-aligned team | A team owning a sensor-fusion/perception subsystem requiring specialized robotics expertise |

Most of an organization's teams should be stream-aligned — platform, enabling, and complicated-subsystem teams exist specifically to reduce the cognitive load stream-aligned teams would otherwise carry, not as an end in themselves.

## Team Size and Cognitive Load

A team can only effectively own as much system complexity as its cognitive load allows — the classic "two-pizza team" framing (roughly 5-9 people) isn't an arbitrary number, it reflects the practical limit of how much a group can hold in shared context while still communicating efficiently. When a team's owned scope exceeds what it can reason about coherently, that's the actual signal to split the team and the system boundary together — not headcount growth for its own sake.

## Designing Team Boundaries to Match Architecture Boundaries

Team boundaries and service/module boundaries should be drawn together, not independently — a microservice owned by three different teams undermines the independent-deployability benefit microservices are meant to provide (see `skills/07_Architecture/SKILL.md`), and a team spanning multiple unrelated services carries unnecessary cognitive load and coordination overhead. The modular monolith's internal module boundaries (recommended as the default starting architecture) should ideally already track the team boundaries the org expects to grow into.

## Staged Org Design

| Stage | Typical structure |
|---|---|
| Early (1-10 engineers) | One team, full-stack, minimal formal structure — premature specialization here is itself a form of over-engineering |
| Growth (10-50 engineers) | A small number of stream-aligned teams emerging around clear product/domain boundaries, possibly the first platform team forming as shared infrastructure needs grow |
| Scale (50+ engineers) | Multiple stream-aligned teams, a real platform organization, possibly enabling and complicated-subsystem teams for specialized domains (ML, robotics, security) |

## Common Mistakes

- Splitting teams by technical layer (a "frontend team" and a "backend team") rather than by business/product domain, which forces cross-team coordination for nearly every feature.
- Growing team structure organically with no deliberate connection to architecture boundaries, producing both coordination overhead and an accidental, fragmented system architecture.
- Creating a platform team before there's a genuine internal-tooling need it solves, adding organizational overhead the company's stage doesn't yet justify.
- Letting a single team's owned scope grow past what it can hold in shared context, without splitting the team and the system boundary together.

## Decision Rule for This Domain

Default to stream-aligned teams organized around product/domain boundaries, not technical layers. Introduce platform, enabling, or complicated-subsystem teams only against a demonstrated need those team types specifically address. Design team boundaries and architecture/module boundaries together, not independently.
