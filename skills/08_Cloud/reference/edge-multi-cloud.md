# Edge Computing & Multi-Cloud Strategy

## Goal

Edge computing and multi-cloud are both legitimate tools for specific problems — and both are frequently adopted for the wrong reasons (hype, theoretical vendor-lock-in fear, resume-driven architecture). Apply the same evidence-based bar used everywhere else in this knowledge base.

## Edge Computing — When It's Real

| Use case | Why edge helps |
|---|---|
| Static asset delivery | CDN edge caching reduces latency globally — this is the most common and almost always justified edge use case |
| Edge functions for personalization/auth checks | Running lightweight logic (redirects, A/B test bucketing, auth token checks) at the edge avoids a round trip to a origin server for simple decisions |
| IoT/device-adjacent processing | Reducing latency and bandwidth for sensor data by processing near the device before sending aggregated results upstream (see `skills/11_Robotics/` for the robotics-specific edge-compute treatment) |
| Real-time gaming/collaboration | Edge points-of-presence reduce latency for geographically distributed real-time interactions |

**Decision rule:** Static asset/CDN edge caching is close to a default best practice for any product with a real user base — low cost, low complexity, real latency benefit. Edge *functions* (compute at the edge, not just caching) earn their complexity only with a specific latency-sensitive logic need; don't move business logic to the edge by default.

## Multi-Cloud — The Over-Engineering Trigger Revisited

This is explicitly named in `skills/00_Core/reference/over-under-engineering.md` as a common over-engineering trigger: "multi-cloud without regulatory need." The reasoning:

- **The theoretical benefit** (avoiding vendor lock-in, negotiating leverage, resilience against a single provider's outage) is real but rarely outweighs the cost for most companies.
- **The actual cost** is substantial: engineering time spent on abstraction layers that work across providers (often settling for the lowest common denominator of each provider's features), duplicated operational tooling/expertise, and split team attention.
- **The case where it's genuinely justified**: a specific regulatory/contractual requirement (e.g., a customer contract mandating provider diversity), a demonstrated single-provider outage that caused unacceptable business impact and a board-level mandate to mitigate it, or a company at a scale where provider-negotiation leverage measurably matters (this is a late-stage, large-company concern, not an early/mid-stage one).

## A Lighter-Weight Alternative to Full Multi-Cloud

Most of the *real* risk multi-cloud is meant to mitigate (a single provider's regional outage) is better addressed by multi-region within a single provider, which is far cheaper than running infrastructure across two entirely different providers. Reserve true multi-cloud for the specific regulatory/contractual driver, not as general-purpose risk mitigation.

## Common Mistakes

- Building a cloud-agnostic abstraction layer "just in case," paying an ongoing tax in engineering complexity and feature limitation for a switch that may never happen.
- Treating multi-cloud as a resilience strategy when single-provider multi-region (much cheaper) would address the same realistic failure modes.
- Pushing business logic to edge functions for the sake of using the technology, when a regular origin-server request would have been simpler to reason about and debug.

## Decision Rule for This Domain

Use CDN/edge caching for static content as a near-default. Reserve edge functions for genuine latency-sensitive logic. Do not adopt multi-cloud without a named regulatory, contractual, or board-mandated driver — review `skills/00_Core/reference/over-under-engineering.md` before recommending it.
