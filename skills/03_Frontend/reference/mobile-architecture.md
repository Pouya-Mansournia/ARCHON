# Mobile Architecture

## Goal

Choose native vs. cross-platform mobile development based on real performance/platform-API requirements and real team composition — not default assumption. Mobile architecture mistakes are expensive to reverse because app store release cycles and user-installed-base inertia slow any correction.

## Native vs. Cross-Platform — Full Decision Table

| Dimension | Native (Swift/Kotlin) | React Native | Flutter |
|---|---|---|---|
| Performance ceiling | Highest — direct platform API access | Good for most apps; can hit limits on heavy animation/graphics | Good, often better than RN for animation-heavy UI (own rendering engine) |
| Code sharing across platforms | None — fully separate codebases | High (most business logic and UI shared) | High (UI and logic shared via Dart) |
| Team skill reuse | Requires dedicated iOS + Android expertise | Reuses existing React/JS team skills | Requires learning Dart, but UI paradigm is approachable |
| Access to brand-new platform APIs | Immediate | Often requires waiting for a community bridge/module, or writing a native module yourself | Similar — may require platform channel code for very new APIs |
| Hiring pool | Large for each platform individually, but need two specialties | Large (JS/React ecosystem) | Smaller than React but growing, strong Google backing |
| App size / cold start | Smallest, fastest | Larger than native, generally acceptable | Larger than native, generally acceptable |

**Decision rule:**
- Choose **native** when the app is fundamentally built around deep platform-specific capability (advanced camera/AR/ML processing, heavy background processing, platform-specific design language being a core differentiator) or when performance is the core product differentiator (e.g., a high-end game).
- Choose **React Native** when the team already has strong React/web expertise and wants maximum code/skill reuse — this is the most common correct default for product startups building a standard consumer or B2B mobile app.
- Choose **Flutter** when starting fresh with no existing team bias toward JS, and wanting the most visual/behavioral consistency across platforms with a single codebase.

## Offline-First Mobile Patterns

Mobile apps must assume intermittent connectivity as the normal case, not the exception:
- Local-first data storage (SQLite, Realm, or platform-native persistence) with a sync layer to the backend, rather than assuming every action can make a live network call.
- Optimistic UI updates (show the action as succeeded immediately, reconcile with the server in the background, handle conflicts/rollback gracefully) dramatically improve perceived performance on unreliable networks.
- Conflict resolution strategy must be decided explicitly (last-write-wins, server-authoritative merge, or user-prompted resolution) — "we'll figure it out" is not a strategy and produces silent data loss in practice.

## App Store Release Process Considerations

- Release cadence is constrained by app store review times (variable, sometimes same-day, sometimes multi-day) — this affects how teams think about hotfixes; a server-side feature flag or remote-config system to disable broken features without a new app store release is a standard, valuable safety net.
- Staged rollouts (releasing to a percentage of users first) are supported by both major app stores and should be the default release pattern for any non-trivial update, to limit blast radius of a bad release.
- Backward compatibility: users update on their own schedule, not yours — backend APIs must support at least N-1 (commonly N-2) app versions simultaneously, or you will break users who haven't updated yet.

## Push Notifications & Background Processing

- Push notification infrastructure (APNs for iOS, FCM for Android) is best accessed through a unified service (e.g., Firebase Cloud Messaging, OneSignal) rather than building separate platform-specific pipelines, unless there's a specific scale/cost reason not to.
- Background processing capability differs meaningfully between iOS (tightly restricted) and Android (historically more permissive, increasingly restricted in recent versions) — design background-dependent features (location tracking, sync) assuming the OS can suspend or kill background work at any time, and design for graceful resumption.

## Required Output for This Domain

State explicitly which platform(s) are in scope (iOS only, Android only, both) and the team's existing mobile/JS skill composition — this single piece of context most often determines the right answer here.
