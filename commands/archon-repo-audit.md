---
name: archon-repo-audit
description: Have ARCHON audit any repository — its own included — and turn it into a production-grade, world-class open-source project. Covers README, docs, architecture, GitHub optimization, license, CI/CD, developer experience, and AI/SEO readability, grounded strictly in what the repo actually contains.
argument-hint: "<repo path, or paste the README/folder structure to audit>"
---

# /archon-repo-audit

Repository-optimization mode. ARCHON puts on five hats at once — Staff Engineer, Maintainer, Technical Writer, Product Marketer, and Documentation Architect — and runs the repo through a fixed four-phase pipeline. Never invents features; every recommendation is grounded in the actual codebase, and working code is never rewritten unnecessarily (`skills/00_Core/reference/over-under-engineering.md`).

## Usage

```
/archon-repo-audit $ARGUMENTS
```

## What Happens

ARCHON loads `skills/15_Engineering_Practices/reference/documentation-practices.md` and `skills/19_Review_Outputs/reference/review-output-standards.md`, then runs:

1. **Audit** — repository purpose, tech stack, folder structure, README, architecture docs, examples, assets (including a check for a demo GIF/screenshots and a "Quick Win" example), GitHub config, community files, license, CI/CD, versioning, security, testing, developer experience, contributor experience, branding, SEO/GEO, AI readability. Output: strengths, weaknesses, risks, missing items, a prioritized roadmap (High/Medium/Low ROI).
2. **Benchmark** — compares against excellent open-source projects in the same category on first impression, onboarding, documentation, UX, architecture docs, examples, and community health.
3. **Score** — 0-10 per category (First Impression, README, Documentation, Developer Experience, Contributor Experience, Architecture, Examples, Visual Design, GitHub Optimization, Community Standards, SEO, GEO, AI Readability, Repository Health).
4. **Improvement Plan** — only the changes that maximize impact; preserves existing functionality; generates missing files (README, ARCHITECTURE.md, LICENSE, community health files, GitHub topics, CI/CD recommendations) only when genuinely beneficial, never speculatively.

### Quick Win Example

If the README doesn't let a developer understand the project in under 30 seconds, ARCHON recommends adding one complete worked example near the top, in this shape:

```
Input → Execution → Generated Output → Expected Result
```

Concrete and runnable, not abstract — a copy-pasteable command or snippet plus the actual output it produces, not a description of what it would do.

### Mermaid Diagrams (Only Where They Clarify)

When architecture documentation is missing or unclear, ARCHON recommends the specific diagram type that fits the gap — not diagrams for their own sake:

| Diagram Type | Use It For |
|---|---|
| Architecture / Component | How major components fit together |
| Sequence | A specific multi-step interaction (auth flow, request lifecycle) |
| Request/Data Flow | How a request or piece of data moves through the system |
| User Flow | The path a user takes through the product |
| Deployment | How the system maps onto infrastructure/environments |

Generate a diagram only when it replaces a paragraph that's genuinely harder to follow in prose — per the same over-engineering discipline as everything else ARCHON recommends.

### License Decision Rule

| Situation | Default Recommendation |
|---|---|
| Library or framework meant for broad adoption | MIT — simplest, fewest adoption barriers |
| Patent exposure is a real concern (larger codebase, corporate contributors) | Apache-2.0 — adds explicit patent grant/protection |
| Maintainer explicitly wants downstream modifications to stay open | GPL — only when strong copyleft is clearly the intent, since it's also the biggest adoption barrier |

Always explain the reasoning, never just name a license.

## Output

- Repository Health Report (strengths / weaknesses / risks / missing items)
- Updated README structure recommendation (hero, value prop within 5 seconds, before/after, a Quick Win worked example, quick start, comparison table, etc.)
- Missing documentation list (only what's actually beneficial — `ARCHITECTURE.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, and similar, per `skills/15_Engineering_Practices/reference/documentation-practices.md`)
- Mermaid diagram recommendations, only the specific type(s) that close an actual gap (see table above)
- License recommendation (if missing), with reasoning against the decision rule above
- GitHub optimization: title, description, 15-20 topics, issue/PR templates
- CI/CD recommendations (lint, tests, release automation, Dependabot, CodeQL) — only where appropriate
- Scorecard: current score vs. potential score per category after applying recommendations

## Example

```
/archon-repo-audit Audit this repo: a Python CLI tool, 40 stars, no README badges, no CONTRIBUTING.md, no LICENSE, tests exist but aren't documented, last release was 8 months ago.
```

## Tips

- This mode is read-and-recommend, not read-and-rewrite: it proposes what to add or change and why, ranked by ROI, rather than silently regenerating files.
- For a single already-scoped architecture decision instead of a whole-repo pass, use `/archon-principal`. For an adversarial critique of a design or PR, use `/archon-review`.
