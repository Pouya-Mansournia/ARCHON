# Product Engineering — MVP Scoping & Product-Market-Fit-Aware Architecture

## Goal

The right architecture pace and rigor depends heavily on whether a product has found product-market fit (PMF). Building for post-PMF scale before reaching PMF is one of the most common and costly architecture mistakes; under-investing after PMF is the inverse mistake.

## Pre-PMF: Optimize for Learning Speed

Before PMF, the most valuable resource is speed of learning whether the product solves a real problem for real users. Architecture decisions should minimize time-to-feedback, even at the cost of technical debt that would be unacceptable post-PMF.

**Acceptable pre-PMF shortcuts (with explicit follow-up plan):**
- A monolith, even a messy one, beats any service split.
- Manual processes for low-frequency operations (e.g., manually triggering a report rather than building a scheduling system) are fine if they happen rarely enough.
- Using a single, simple database (Postgres) for everything, including things that "should" eventually be a queue or a cache — premature introduction of additional infrastructure slows iteration without adding learning value.
- Skipping comprehensive automated test coverage for parts of the product still being actively reshaped by user feedback (though core business logic — payments, auth — should still be tested).

**Non-negotiable even pre-PMF:** basic security (auth, no plaintext secrets), backups, and enough error handling/monitoring to know when something is actually broken. These aren't "scale" investments — they're correctness investments, and skipping them risks losing the exact users you're trying to learn from.

## Finding PMF: The Inflection Point

Signals that a product has found genuine PMF (not exhaustive, look for multiple converging signals, not just one): organic/word-of-mouth growth without proportional spend increase, strong retention curves that flatten rather than decay to zero, users expressing strong reactions to losing access, usage growing faster than the team is actively pushing it.

## Post-PMF: Shift Investment Toward Reliability and Scale Readiness

Once PMF signals are real, the cost calculus flips: an outage or a security incident now costs real, demonstrated business value (churned customers, damaged trust), not just embarrassment. This is the point to:
- Pay down the specific technical debt that's now actually blocking velocity or reliability (not all debt — see `skills/15_Engineering_Practices/reference/technical-debt-management.md`).
- Invest in proper observability, on-call processes, and incident response (see `skills/13_Reliability/`).
- Revisit the multi-tenancy, data model, and service boundary decisions made pre-PMF against now-real usage patterns, and plan deliberate migrations where they no longer fit (not as a rewrite, as a sequence of safe, incremental changes).

## Scoping an MVP Correctly

An MVP should be the smallest thing that lets you test the core hypothesis with real users — not the smallest thing that's technically impressive, and not a feature-complete v1 with corners cut everywhere.

**Common MVP scoping mistakes:**
- Building configurability/customization "because customers will want different things," before a single customer has confirmed they want the base case.
- Building for multiple platforms (web + iOS + Android) simultaneously before validating on one.
- Building an admin panel/internal tooling polish before validating the core user-facing hypothesis.
- Treating the MVP as disposable in a way that makes the *real* product impossible to evolve from it cleanly (e.g., hardcoding assumptions so deeply that the eventual rebuild is a full rewrite rather than an evolution).

## Required Output for This Domain

State explicitly which stage (pre-PMF, finding PMF, post-PMF, scaling, mature) the recommendation assumes, and flag any place where the "right" answer differs meaningfully depending on that stage — this is one of the most common places a recommendation can be technically correct but contextually wrong.
