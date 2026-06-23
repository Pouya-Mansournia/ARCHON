# CI/CD & GitOps

## Goal

Continuous integration and continuous delivery is one of the few infrastructure investments with almost no downside — even a one-person team benefits from automated test/build/deploy over manual steps. The decision space here is about pipeline sophistication and deployment strategy, not whether to have a pipeline at all.

## CI/CD Pipeline Stages

| Stage | Purpose |
|---|---|
| Lint / static analysis | Catch style and obvious correctness issues before tests even run |
| Unit tests | Fast feedback on logic correctness in isolation (see `skills/15_Engineering_Practices/` for testing strategy depth) |
| Build | Produce the deployable artifact (container image, compiled bundle) |
| Integration / end-to-end tests | Verify the system works across component boundaries — slower, run less frequently than unit tests |
| Security scanning | Dependency vulnerability scanning, container image scanning, secret-leak detection |
| Deploy | Push the built artifact to the target environment |

## CI/CD Platform Options

| Platform | Good fit for |
|---|---|
| GitHub Actions | Default choice for most teams already on GitHub — tight integration, large marketplace of pre-built actions |
| GitLab CI | Teams on GitLab, strong built-in CI/CD without needing third-party integration |
| CircleCI | Teams wanting a CI-focused tool independent of the git host, mature caching/parallelism features |
| Jenkins | Legacy/enterprise environments with existing Jenkins investment; generally not the right new default given its operational overhead vs. modern SaaS CI |

**Decision rule:** Use the CI/CD tooling built into the team's existing git host (GitHub Actions for GitHub, GitLab CI for GitLab) unless there's a specific reason not to — this minimizes integration overhead and keeps pipeline config alongside the code it builds.

## Deployment Strategies

| Strategy | How it works | Risk profile |
|---|---|---|
| Recreate | Stop old version, start new version | Downtime during deploy — acceptable only for non-critical/internal tools |
| Rolling update | Gradually replace old instances with new ones | Brief mixed-version window; the default for most managed container services |
| Blue-green | Deploy new version fully alongside old, then switch traffic atomically | Fast rollback (switch back), but requires double the infrastructure during the switch |
| Canary | Route a small percentage of traffic to the new version, expand gradually | Lowest blast radius for catching issues early, but more complex to set up and monitor |

**Decision rule:** Rolling updates are the right default for most teams. Reach for blue-green or canary once deployment risk (high-traffic production system, regulatory/financial stakes) justifies the added pipeline complexity.

## GitOps

GitOps treats the Git repository as the single source of truth for both application code and infrastructure/deployment state — a tool (ArgoCD, Flux) continuously reconciles the live environment to match what's declared in Git, rather than CI directly pushing changes imperatively.

**When it's worth adopting:** Teams running Kubernetes at a scale where declarative, auditable, automatically-reconciled deployment state earns its setup cost. **When it's premature:** Teams not yet running Kubernetes, or small enough that a straightforward CI pipeline that deploys directly is simpler to reason about end to end.

## Common Mistakes

- No automated tests in the pipeline — "CI" that only builds and deploys without verifying correctness first, turning the pipeline into a fast way to ship bugs.
- No rollback plan — treating every deploy as one-way, with no quick path back to the last known-good version when something breaks (see `skills/13_Reliability/` and `engineering:deploy-checklist` for rollback-trigger planning).
- Adopting GitOps tooling before adopting Kubernetes, solving a reconciliation problem that doesn't exist yet.
- Secrets committed directly into pipeline config instead of using the CI platform's secret-management feature.

## Decision Rule for This Domain

Every product past the earliest prototype needs an automated CI/CD pipeline with at minimum lint + tests + build + deploy. Use rolling updates by default; escalate deployment strategy sophistication and GitOps only against demonstrated risk/scale. Pair every pipeline with an explicit rollback plan — see `engineering:deploy-checklist`.
