# Decision Trees for Common Multi-Domain Questions

## Goal

Give a concrete routing path through the 20 domain skills for the questions that come up most often and naturally span multiple domains, so the synthesis in `skills/18_Domain_Architectures/` and the routing logic in `skills/99_Decision_Engine/SKILL.md` have worked examples to follow.

## Tree 1 — "How should we architect a new product?"

1. Start in `skills/02_Product/` — what category of product is this (SaaS, marketplace, AI product, IoT, robotics, internal tool)? What's the actual problem and who's the user? Don't proceed to technical architecture before this is answered.
2. Check `skills/18_Domain_Architectures/` for a reference architecture matching the product category.
3. Walk the layers in order: data architecture (`05_Database`) → API/communication (`06_API`) → structural pattern (`07_Architecture`, default modular monolith) → cloud/deployment (`08_Cloud`, `09_DevOps`) → security baseline (`12_Security`) → observability baseline (`13_Reliability`).
4. Apply `skills/00_Core/reference/over-under-engineering.md` to every layer's choice before finalizing.
5. If the product has an AI, IoT, or robotics component, layer in `skills/10_AI/` or `skills/11_Robotics/` and re-examine the cloud-edge-device placement question from `skills/18_Domain_Architectures/reference/ai-iot-robotics-product-architecture.md`.

## Tree 2 — "Our system needs to scale, what do we do?"

1. Demand evidence first — `skills/14_Performance/reference/performance-profiling-load-testing.md`'s measurement-first rule. No profiling/load-test data means this tree shouldn't proceed past this step yet.
2. Identify the actual limiting resource (database, a specific service, network, a third-party dependency).
3. Apply the scaling toolkit in order from `skills/14_Performance/reference/scaling-patterns.md`: fix the bottleneck → cache (`05_Database/reference/caching-architecture.md`) → async offload (`06_API/reference/messaging-event-driven.md`) → horizontal scale stateless layers → database read replicas/scaling (`05_Database/`) → architectural decomposition (`07_Architecture/`), only as a last resort.
4. If multi-region is being discussed, route through `skills/08_Cloud/reference/multi-region-architecture.md`'s justification checklist before going further.

## Tree 3 — "We need a security review."

1. Start with the security-by-default checklist in `skills/12_Security/SKILL.md`.
2. Run a lightweight threat-modeling pass (`skills/12_Security/reference/threat-modeling-appsec.md`, STRIDE categories).
3. Check authentication/authorization design against `skills/12_Security/reference/authn-authz.md`.
4. Check data handling against `skills/12_Security/reference/data-protection-encryption.md`.
5. If the system includes AI features, additionally check `skills/10_AI/reference/ai-product-safety.md` for prompt-injection and guardrail coverage.
6. Produce findings in the `skills/19_Review_Outputs/reference/review-output-standards.md` format.

## Tree 4 — "Should we migrate to/adopt [some new technology]?"

1. Treat this as a build-vs-buy-adjacent question first — route through `skills/17_Cost_Business/reference/build-vs-buy-tco.md`'s framework even when "buy" isn't literally the alternative; the same TCO discipline applies to "adopt new tech vs. keep current approach."
2. Check whether the motivating problem is real and current, or hypothetical — `skills/00_Core/reference/over-under-engineering.md`.
3. Identify which specific domain skill governs the technology in question and check its decision matrix for whether this case is a genuine fit.
4. If proceeding, write an ADR (`skills/19_Review_Outputs/reference/adr-decision-log-templates.md`) capturing the alternatives considered and trade-offs accepted, and check `skills/16_Team_Leadership/reference/hiring-engineering-talent.md` for whether the team has or can build the needed expertise.

## Decision Rule for This Domain

Use these trees as starting routes, not rigid scripts — the actual judgment still happens at each domain skill's decision rule, applying the Engineering Decision Principles priority order when domains pull in different directions. The value of a tree is making sure no relevant domain gets skipped, not replacing judgment with a flowchart.
