# Testing Strategy

## Goal

A testing strategy should give the team confidence to ship changes quickly without manually re-verifying everything — too little testing makes every change risky; too much (or the wrong kind) testing slows the team down without proportionally increasing real confidence. (See the `engineering:testing-strategy` skill for tactical, per-feature test planning; this file covers the overall philosophy and shape of a healthy test suite.)

## The Test Pyramid

| Layer | What it tests | Speed | Proportion of suite |
|---|---|---|---|
| Unit tests | Individual functions/components in isolation | Fast (milliseconds) | The majority — cheap, fast, precise about what broke |
| Integration tests | Multiple components working together (e.g., API endpoint + database) | Moderate | A meaningful minority — catches issues unit tests structurally can't see |
| End-to-end tests | Full user journeys through the real system | Slow | A small number, covering only the most critical paths |

A healthy suite is shaped like a pyramid (many fast unit tests, fewer integration tests, very few E2E tests) rather than an inverted pyramid (a handful of unit tests propped up by a large, slow, flaky E2E suite) — the inverted shape is a common and costly anti-pattern that makes the whole suite slow and brittle.

## Coverage Philosophy

Line/branch coverage percentage is a weak proxy for actual confidence — a test that executes a line without meaningfully asserting on its behavior inflates coverage without adding real protection. Prioritize testing behaviors that matter (business logic, edge cases, error handling, anything that has broken before) over chasing a coverage number. That said, a coverage floor (e.g., "no PR decreases coverage") is a reasonable guardrail against silent erosion, even if the target percentage itself shouldn't be treated as the goal.

## What to Test at Each Layer

- **Unit tests**: business logic, edge cases (empty input, boundary values, error conditions), anything with non-trivial branching.
- **Integration tests**: the seams between components — does the API layer correctly persist to the database, does a queue consumer correctly process a message, does an external API client handle a realistic error response.
- **E2E tests**: the handful of user journeys where a regression would be most damaging (signup, checkout, core workflow) — kept few because they're slow and more prone to environmental flakiness.

## Flaky Tests

A flaky test (one that intermittently fails without a real underlying bug) is worse than no test at all — it trains the team to ignore failures, which then hides real regressions in the noise. Treat flaky test triage as a priority, not a backlog item that lingers indefinitely; either fix the root cause (often a timing assumption or shared state issue) or remove the test.

## Testing AI and Robotics Components

AI features need evaluation-set-based testing in addition to conventional unit/integration tests (see `skills/10_AI/reference/ai-product-safety.md`) — deterministic assertions don't capture quality for non-deterministic outputs. Robotics control logic needs simulation-based and hardware-in-the-loop testing before real-world deployment (see `skills/11_Robotics/`) — a unit test on a control algorithm in isolation doesn't validate real-time/physical behavior.

## Common Mistakes

- Chasing a coverage percentage target rather than testing behaviors that actually matter.
- An inverted test pyramid — heavy reliance on slow, flaky E2E tests instead of fast, precise unit tests.
- Letting known-flaky tests linger, training the team to ignore CI failures generally.
- Treating conventional unit-test practices as sufficient for AI or robotics components without the domain-specific testing layers those areas require.

## Decision Rule for This Domain

Build a pyramid-shaped suite: many fast unit tests, a meaningful integration layer, very few E2E tests covering only the most critical journeys. Treat coverage as a guardrail, not a target. Fix or remove flaky tests immediately rather than letting them erode trust in CI.
