# Principal Engineer Thinking

## Goal

The 8 Core Principles (`core-principles.md`) and the Over/Under-Engineering Detector define *what* good engineering judgment looks like. This file is the *pre-flight checklist* you run on every draft recommendation before it goes out the door — the eight questions a good Principal Engineer asks reflexively, in a design review, in a Slack thread, or in their own head before hitting send on an RFC comment. It exists to catch a specific failure mode this knowledge base is built to prevent: an answer that is technically correct on every individual point but was never actually pressure-tested as a whole.

If you cannot answer one of these eight questions in a sentence, that is a signal — not that the question is unfair, but that the recommendation underneath it isn't finished yet.

## The Pre-Flight Checklist

Run all eight against the recommendation you are about to give, not in the abstract. Each one is paired with what it actually catches.

| Question | What it catches |
|---|---|
| Is this complexity justified? | Architecture or tooling added because of a real, current constraint, vs. added because it's interesting, resume-friendly, or "best practice" with no specific problem attached. |
| Can it be simpler? | A simpler design that meets the same requirement was dismissed without being seriously considered, usually because the complex one was decided on first and justified backward. |
| What breaks first? | No identified failure mode means the design hasn't actually been load-tested in your head yet. Every system has a first thing that breaks under load, bad input, or partial failure — name it. |
| What are the operational costs? | The on-call burden, the new skill the team needs, the additional service to patch and monitor at 2 a.m. — costs that don't show up in a cloud bill but show up in attrition and incident counts. |
| What are the trade-offs? | Every option chosen something away from something else. If you can't name what was given up, you've described a feature, not a decision. |
| Can the team maintain this? — see `hiring-reality` in `core-principles.md` | A design that assumes a team the company doesn't have, hasn't hired, or can't afford — the most common source of "it worked great until the person who built it left." |
| What happens after 10x growth? | Distinguishes "this scales" (verified, or at least reasoned about) from "this should probably scale" (hoped). Also flags premature scaling work for a system nowhere near 10x today. |
| What should NOT be built yet? | The single most skipped question in technical writing. A recommendation without an explicit not-yet list quietly implies "build all of it now" — which is usually the over-engineering trigger in disguise. |

## Optimize for Engineering Reality, Never for Hype

A recommendation justified by "it's what [well-known company] uses" or "it's the modern way to do this" has skipped the checklist above, not completed it. Company-at-a-different-scale and technology-because-it's-current are both real inputs, but they are evidence, not conclusions — they still have to clear "is this complexity justified for *this* team, at *this* scale, *today*."

This is the same stance as `core-principles.md`'s Simplicity First and MVP Before Scale principles, applied as a habit of mind rather than a one-time rule: default to the boring, well-understood, operationally cheap choice, and require a specific, current reason — not a hypothetical future one — to spend complexity budget on anything else.

## Default Preference Order

When the checklist surfaces a genuine trade-off, default to:

1. Simplicity
2. Maintainability
3. Reliability
4. Cost efficiency
5. Battle-tested solutions
6. Clear migration paths

This is the field-checklist version of the full Engineering Decision Principles priority order (`core-principles.md`; `agents/archon.md`; Simplicity → Maintainability → Reliability → Development Speed → Cost Efficiency → Security → Scalability → Performance → Future Flexibility → Technical Elegance). The two lists do not conflict: this shorter list is what to reach for first when reasoning quickly about a design; the full ten-part order is the tie-breaker once Security, Scalability, Performance, and Future Flexibility also need to be weighed explicitly. "Battle-tested solutions" and "clear migration paths" are not separate principles competing with the original ten — they are restatements of Reliability (proven in production beats novel) and of the Output Standard's mandatory tenth field (every recommendation needs an exit path), surfaced here because they are exactly the kind of thing the checklist above is meant to force into view.

## Worked Example

**Question:** "Should we adopt a service mesh (Istio) across our 12-service backend?"

Running the checklist against a yes-by-default answer:

- *Is this complexity justified?* Only if there's a real, current need for mTLS between services, fine-grained traffic shifting, or multi-cluster routing — not because microservices and meshes are usually mentioned together.
- *Can it be simpler?* Yes, almost always at 12 services: a thin shared library for retries/timeouts, plus your cloud load balancer for routing, covers most of what a mesh provides at a fraction of the operational cost.
- *What breaks first?* The mesh's own control plane (Istio's `istiod`) becomes a new single point of failure and upgrade dependency for all 12 services simultaneously — you've added a new thing that, when it breaks, breaks everything at once.
- *What are the operational costs?* A sidecar proxy per pod (real CPU/memory tax at this scale), a new control plane to patch and version, and a steep learning curve the team has to absorb before they can debug a production incident through it.
- *What are the trade-offs?* Uniform traffic policy and security posture, in exchange for a new layer of indirection in every network call and a much harder debugging path when something is slow.
- *Can the team maintain this?* Only if someone owns mesh operations specifically — meshes are notorious for being installed by one person who later leaves, after which nobody touches the configuration out of fear.
- *What happens after 10x growth (120 services)?* This is where a mesh's value proposition gets real — consistent mTLS, traffic shaping, and observability across a service count too large to manage with ad hoc per-service config. At 12 services, you are years away from needing that.
- *What should NOT be built yet?* The mesh itself, for now. Revisit when service count, multi-team ownership, or a specific compliance requirement (e.g., mandatory mTLS everywhere) makes the operational cost worth it.

**Resulting recommendation:** No, not yet — use a shared client library for retries/circuit-breaking and your existing load balancer for routing today; document the specific triggers (service count, a concrete mTLS requirement, multi-cluster topology) that would flip this decision, so it's a deliberate re-evaluation later, not a default neglected forever.

## Decision Rule

Run this checklist *before* `skills/00_Core/reference/over-under-engineering.md`'s trigger tables and before producing the Output Standard — it is the fast, holistic gut-check; the trigger tables are the detailed, pattern-matched follow-up; the Output Standard is the final structured write-up. If the checklist surfaces a question you can't answer in a sentence, that is the question to research next, not a reason to soften or hedge the eventual recommendation.
