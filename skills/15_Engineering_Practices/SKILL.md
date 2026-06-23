---
name: engineering-practices
description: Day-to-day engineering practices — code review, testing strategy, technical debt management, and documentation — the practices that compound into either a healthy or unhealthy engineering culture over time.
---

# 15 — Engineering Practices (L4)

**Level:** L4 — Principal Engineering.

## Goal

These are the practices that don't show up in an architecture diagram but determine whether a codebase stays maintainable and a team stays fast as both grow — code review quality, testing discipline, technical debt visibility, and documentation habits compound (positively or negatively) far more than any single technology choice.

## Why These Practices Get Under-Invested

Architecture decisions get attention because they're visible and feel consequential; day-to-day practices get neglected because each individual lapse (a rushed review, a skipped test, an undocumented decision) seems low-stakes in isolation. The compounding cost only becomes visible months later as review quality erodes trust, untested code produces regressions, debt silently accumulates, and tribal knowledge walks out the door with whoever leaves.

## Reference Files

- `reference/code-review-practices.md` — what good code review actually checks for, and how to keep it fast without making it shallow.
- `reference/testing-strategy.md` — test pyramid, coverage philosophy, and what to test at each layer (complements the `engineering:testing-strategy` skill's tactical test-planning workflow).
- `reference/technical-debt-management.md` — categorizing, tracking, and prioritizing technical debt (complements the `engineering:tech-debt` skill's audit workflow).
- `reference/documentation-practices.md` — what documentation actually needs to exist and why most documentation efforts fail.
