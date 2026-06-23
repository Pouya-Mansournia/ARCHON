---
name: frontend-architecture
description: Frontend and mobile architecture decisions — web frameworks (React, Next.js, Vue, Svelte, Angular), mobile approaches (native Swift/Kotlin vs React Native/Flutter), and the decision rules for choosing between them based on team, product, and performance needs.
---

# 03 — Frontend Architecture (L2)

**Level:** L2 — Software Engineering.

## Goal

Pick the frontend/mobile stack that matches the team's skill set, the product's performance/interactivity needs, and the platform reach required — not the framework that's currently trending.

## Web Framework Decision Matrix

| Framework | Best for | Avoid when |
|---|---|---|
| Plain HTML/CSS/JS | Marketing pages, minimal interactivity | Any non-trivial app state or interactivity |
| React (CSR) | Highly interactive SPAs, large ecosystem need, large hiring pool | SEO-critical content without SSR added on top |
| Next.js (React + SSR/SSG) | Default modern choice for most product web apps — SEO, performance, and interactivity all matter | Extremely simple static sites where the framework overhead isn't earning its keep |
| Vue / Nuxt | Teams preferring a gentler learning curve and more opinionated structure than React | Need for the largest possible hiring pool / ecosystem (React's is larger) |
| Svelte / SvelteKit | Performance-sensitive apps wanting less runtime overhead and less boilerplate | Need for the deepest third-party component ecosystem |
| Angular | Large enterprise teams wanting a full, opinionated, batteries-included framework with strong conventions | Small teams/startups wanting to move fast with minimal framework ceremony |

## Mobile Decision Matrix

| Approach | Best for | Avoid when |
|---|---|---|
| Native (Swift/iOS, Kotlin/Android) | Performance-critical apps, deep platform API usage (AR, advanced camera, background processing), or a team with native expertise already | Small team needing to ship both platforms fast with limited mobile-specific hiring |
| React Native | Teams with existing React/JS expertise wanting shared logic across platforms, most consumer app categories | Apps with heavy custom native UI/animation needs or very tight performance budgets |
| Flutter | Teams wanting one codebase with high UI consistency across platforms and willing to invest in Dart | Need to maximize reuse of existing JS/web team skills |

## Decision Rule

Default to Next.js for web and React Native (if the team already knows React) or Flutter (if starting fresh with no existing stack bias) for cross-platform mobile, unless a specific, named requirement (SEO depth, native performance ceiling, existing team expertise) points elsewhere. Never choose a frontend framework primarily because it's new — frontend framework churn has a real, recurring cost in retraining and ecosystem instability.

## Reference Files

- `reference/frontend-architecture.md` — full framework comparison, state management, rendering strategy (CSR/SSR/SSG/ISR) decision rules.
- `reference/mobile-architecture.md` — native vs. cross-platform deep dive, offline-first mobile patterns, app store release process considerations.
