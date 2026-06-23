# Frontend Architecture — Full Reference

## Goal

Choose a frontend stack and rendering strategy that matches the product's actual needs (SEO, interactivity, performance budget) and the team's actual skills — and choose a state management approach that matches the application's actual complexity, not its imagined future complexity.

## Rendering Strategy Decision Table

| Strategy | What it means | Best for |
|---|---|---|
| CSR (Client-Side Rendering) | Browser downloads JS bundle, renders everything client-side | Highly interactive, behind-login apps where SEO doesn't matter (dashboards, internal tools) |
| SSR (Server-Side Rendering) | Server renders HTML per-request | SEO-sensitive, dynamic/personalized content (logged-in feeds, search results pages) |
| SSG (Static Site Generation) | HTML pre-built at build time | Content that changes infrequently relative to traffic (marketing pages, blogs, docs) |
| ISR (Incremental Static Regeneration) | Static pages that regenerate on a schedule or on-demand after the initial build | Content that changes occasionally but where SSG's build-time cost doesn't scale (e.g., thousands of product pages) |

**Decision rule:** Default to SSR/SSG (via Next.js, Nuxt, SvelteKit, or Astro) for anything public-facing and SEO-relevant. Default to CSR for behind-login, highly interactive applications where search engines never see the content anyway.

## State Management Decision Table

| Need | Recommended approach |
|---|---|
| Simple local component state | Built-in framework state (`useState`, Vue `ref`, Svelte stores) — don't reach for a library |
| Server data caching/synchronization | A dedicated server-state library (React Query/TanStack Query, SWR) — this solves caching, refetching, and loading/error states far better than rolling it manually |
| Complex, deeply shared client-only state | Lightweight global store (Zustand, Jotai, Pinia) before reaching for something heavier |
| Very large app with complex cross-cutting state and strict need for predictability/time-travel debugging | Redux (or Redux Toolkit) — but confirm the complexity is real, not assumed, before adopting it; it's frequently over-applied to apps that didn't need it |

**Anti-pattern:** Reaching for Redux (or any heavy global state library) on a small-to-medium app "because that's the standard," when `useState` + a server-state library would have been sufficient and simpler. This is a textbook over-engineering trigger (see `skills/00_Core/reference/over-under-engineering.md`).

## TypeScript

Default to TypeScript for any frontend codebase beyond a trivial prototype. The type-safety benefit compounds as the codebase and team grow, and the tooling/ecosystem cost of adopting it has dropped close to zero (virtually every modern framework and library ships first-class TS support). The only real exception is a genuinely tiny, short-lived prototype where setup overhead isn't worth it.

## Performance Budget Discipline

- Bundle size directly affects time-to-interactive, especially on mobile networks — track it (e.g., via `webpack-bundle-analyzer` or framework-native equivalents) and treat unexpected growth as a regression, not a footnote.
- Code-splitting (route-based at minimum, component-based for heavy/rare components like rich text editors or chart libraries) should be the default, not an optimization pass done later.
- Image optimization (responsive sizes, modern formats like WebP/AVIF, lazy loading below the fold) is usually the single highest-leverage performance fix on content-heavy sites — check this before reaching for more exotic performance work.

## Component Architecture

- Design-system/component-library discipline (a shared `Button`, `Input`, `Modal` set with consistent props) pays for itself once a product has more than a handful of screens — inconsistent ad-hoc components across a codebase are a recurring source of both UX drift and engineering rework.
- Co-locate logic with the component it serves (custom hooks/composables near their usage) rather than centralizing all logic in a way that makes components hard to reason about independently.

## Decision Rule for This Domain

Don't recommend a frontend rewrite or framework migration based on "this framework is more modern" alone — frontend framework migrations are expensive and disruptive; the bar for justifying one should be a specific, demonstrated limitation of the current stack (a real performance ceiling, a real hiring-pool problem, a real feature the current framework structurally can't support well), not aesthetic preference.

## Common Mistakes

- Over-fetching client-side state management libraries for apps that needed almost none of their complexity.
- Skipping SSR/SSG for public, SEO-relevant pages, then wondering why organic search traffic is weak.
- No performance budget or bundle-size tracking until users start complaining.
- Treating every UI element as a one-off rather than building a small, consistent component library early.
