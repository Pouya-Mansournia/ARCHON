# Code Review Practices

## Goal

Code review exists to catch defects, spread knowledge, and maintain a consistent standard across a codebase that outlives any single contributor — not to gatekeep or perform rigor theater. A review process that's too slow gets bypassed under deadline pressure; one that's too shallow doesn't catch what it exists to catch. Calibrate for both speed and depth.

## What Good Review Actually Checks

| Dimension | What to look for |
|---|---|
| Correctness | Does the change do what it claims, including edge cases and error paths |
| Security | Input validation, authorization checks, secrets handling (see `skills/12_Security/`) |
| Maintainability | Will the next person (possibly the reviewer, in six months) understand this without the author present to explain it |
| Test coverage | Are the meaningful behaviors covered, not just line coverage as a vanity metric |
| Scope | Is the change appropriately sized and focused, or does it bundle unrelated concerns making review and rollback harder |

## Review Speed vs. Depth

- **Keep PRs small** — a 2,000-line PR gets a shallow rubber-stamp review because no reviewer can hold that much context; a 200-line PR gets genuine scrutiny. Author discipline on PR size is a bigger lever on review quality than any review-process tooling.
- **Set a response-time norm** (e.g., review within one business day) so authors aren't blocked indefinitely — a review process with no speed expectation quietly becomes a process people route around.
- **Distinguish blocking from non-blocking feedback** explicitly (a "nit:" prefix convention or equivalent) so authors know what must be addressed before merge vs. what's a suggestion for later.

## What Review Should Not Be

- A style debate that a linter/formatter should have settled automatically — automate formatting/style enforcement so human review time goes to things automation can't catch.
- A gate where the reviewer rewrites the approach entirely after the author has already built it — substantial design disagreements belong earlier, before significant implementation effort (a design doc, an early draft PR, or a quick conversation).
- A bottleneck where only one senior person can approve anything — this doesn't scale and creates a single point of failure; spread review capability and authority across the team deliberately.

## Common Mistakes

- Allowing PR size to grow unchecked, leading to shallow reviews that miss real issues.
- No automated linting/formatting, burning human review attention on style nits that tooling should catch for free.
- Treating review as adversarial gatekeeping rather than collaborative quality improvement, which erodes psychological safety and slows everyone down.
- Bottlenecking all approvals through one person, creating both a scaling problem and a single point of failure.

## Decision Rule for This Domain

Automate what can be automated (style, formatting, basic static analysis) so human review time concentrates on correctness, security, and maintainability. Keep PRs small enough for genuine scrutiny, set a clear response-time norm, and distribute review authority across the team rather than centralizing it in one person.
