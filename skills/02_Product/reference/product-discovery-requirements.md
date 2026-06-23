# Product, Business & Requirements Discovery

## Goal

Architecture decisions made before understanding the product are guesses wearing engineering clothes. This is the mandatory discovery layer before any non-trivial recommendation.

## The 16 Discovery Questions, In Depth

1. **What problem does this product solve, and for whom?** — Forces clarity on the actual user pain, not just the feature list. A vague answer here ("it's a productivity app") usually means the architecture conversation is premature.
2. **Who are the actual users?** — Consumer (cost-sensitive, latency-sensitive, high volume, low individual value) vs. B2B (fewer users, higher individual value, higher reliability/compliance expectations) vs. internal (lower external-facing reliability bar, but correctness still matters) vs. developer-facing (API design and documentation quality become core product surface).
3. **What's the current stage?** — Idea/pre-launch (optimize for speed of learning, not scale), MVP/early traction (optimize for iteration speed and just-enough reliability), scaling (optimize for the specific bottleneck that's actually been hit), mature (optimize for reliability, cost efficiency, and safe change velocity).
4. **Team size and skill composition?** — Directly bounds what's operable (see Hiring Reality principle, `skills/00_Core/reference/core-principles.md`).
5. **Expected scale in 6-12 months?** — Not "what's the theoretical ceiling" — what's the realistic, evidence-based near-term number. Over-asking this question in the wrong direction ("what if we go viral") is how over-engineering starts.
6. **Budget/cost sensitivity?** — A well-funded enterprise SaaS and a bootstrapped solo founder should get materially different infrastructure recommendations for the identical technical problem.
7. **Timeline pressure?** — Shapes how much "good enough for now, revisit later" is the right call vs. genuinely wrong.
8. **Compliance/regulatory requirements?** — GDPR (EU user data), HIPAA (US health data), SOC2 (B2B trust/sales requirement, not a law), PCI-DSS (handling card data directly) each impose specific, non-negotiable technical requirements — see `skills/12_Security/reference/compliance-governance.md`.
9. **Data sensitivity level?** — PII, financial, health data each raise the security and compliance bar substantially above a typical low-sensitivity SaaS product.
10. **Geographic distribution of users?** — Drives data residency requirements, latency budget, and whether multi-region is a real near-term need or premature (see `skills/08_Cloud/reference/multi-region-architecture.md`).
11. **Required uptime/reliability bar?** — A 99.9% target and a 99.99% target imply meaningfully different architecture investment (see `skills/13_Reliability/reference/slo-sla-error-budgets.md`).
12. **Existing systems/infrastructure to integrate with?** — Greenfield and "must integrate with this 15-year-old SOAP API" are different problems wearing the same feature request.
13. **Monetization model?** — Usage-based billing requires metering infrastructure as a first-class concern from day one, not an afterthought; seat-based billing has different requirements than transaction-based billing.
14. **What's explicitly NOT in scope?** — As important as what's in scope; prevents silent scope creep into the architecture itself.
15. **Competitive landscape and differentiation?** — Sometimes the right technical answer depends on what "table stakes" your category demands (e.g., real-time collaboration is table-stakes for some categories, differentiating in others).
16. **What does success look like in 90 days?** — Forces the team to define the actual near-term target the architecture needs to serve, not a vague long-term vision.

## How to Run Discovery Efficiently

Don't ask all 16 questions every time. Identify which 3-5 would actually change the recommendation given what's already known, ask those, and state explicit assumptions for the rest. Revisit assumptions if they turn out wrong (see `/archon-reflect`).

## Product Category Deep Dive

### Website / Marketing Site
Static-first (Next.js/Astro/Hugo + CDN) is almost always correct. Backend need is usually limited to a contact form handler and maybe a CMS integration. Resist the urge to build a custom backend for what a static site generator + headless CMS solves in a day.

### SaaS (B2B)
Multi-tenancy model decision (shared schema with tenant_id, schema-per-tenant, or database-per-tenant) is the single highest-leverage early decision — see `skills/18_Domain_Architectures/reference/saas-b2b-architecture.md`. RBAC, audit logging, and SSO support become sales requirements earlier than most teams expect (often at the first enterprise deal, not at scale).

### Marketplace
Two-sided architecture: supply side and demand side often have meaningfully different data models and growth dynamics. Trust/reputation systems (reviews, verification) and payment + payout architecture (splitting payments, handling refunds/disputes across two parties) are core, not peripheral, technical requirements from the first transaction.

### E-Commerce
Inventory consistency under concurrent purchase attempts is the classic hard problem (overselling). Payment processing should almost always go through a PCI-compliant processor (Stripe, Adyen) rather than handling card data directly — see `skills/12_Security/reference/compliance-governance.md`. Search/catalog performance becomes a real bottleneck earlier than expected as SKU count grows.

### AI Product
Inference cost per request is a first-class architecture input from day one — it directly determines unit economics. Latency budget (interactive chat vs. async batch processing) determines model size/hosting trade-offs. An evaluation pipeline (how do you know outputs are good?) needs to exist before scaling traffic, not after.

### IoT Product
Devices must assume intermittent/no connectivity (offline-first design) — see `skills/18_Domain_Architectures/reference/ai-iot-robotics-product-architecture.md`. Fleet provisioning and OTA update strategy need to be designed before the first device ships, because retrofitting them onto deployed hardware is dramatically harder than retrofitting software.

### Robotics Product
Real-time and safety constraints are non-negotiable architecture inputs, not features to add later — see `skills/11_Robotics/reference/robotics-architecture-ros.md`. Simulation-first development (testing in simulation before physical hardware) is standard practice for de-risking iteration cost.

### Internal Tool
Lower external-facing reliability bar is usually acceptable (a 30-minute internal tool outage is rarely a company-ending event the way a customer-facing outage is), but data correctness still matters fully — an internal tool that corrupts data is just as costly as a customer-facing one that does. Optimize primarily for build speed and maintainability given the team will likely be smaller and the tool lower-priority for ongoing investment.

## Required Output for This Domain

A short **Product Context Summary** (3-6 lines covering stage, team size, scale, constraints) should precede any architecture recommendation that depends on it — stated explicitly so the user can correct any wrong assumption immediately.
