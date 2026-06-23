# Git & Version Control

## Goal

Version control discipline is a force multiplier or a force divider depending on how a team uses it. Get the branching model, merge strategy, and commit hygiene right early — fixing it later, with history already polluted, is much more expensive.

## Branching Models — Decision Table

| Model | How it works | Best for |
|---|---|---|
| Trunk-Based Development | Everyone commits small, frequent changes directly to `main` (or very short-lived branches merged within a day), gated by feature flags for incomplete work | Teams with strong CI/CD and test coverage, wanting fast integration and minimal merge conflicts — the default recommendation for most modern teams |
| GitHub Flow | `main` is always deployable; feature branches off `main`, PR review, merge back, deploy | Small-to-medium teams, continuous deployment, simple release cadence — a good default for most startups |
| Git Flow | Long-lived `develop` branch, feature branches off `develop`, `release` branches, `hotfix` branches off `main` | Teams shipping versioned releases on a fixed cadence (e.g., desktop software, embedded firmware) where multiple versions must be supported in parallel — overkill for most continuously-deployed web/SaaS products |

**Decision rule:** Default to GitHub Flow or trunk-based development for anything continuously deployed. Reach for Git Flow only when you genuinely need to maintain multiple released versions in parallel (this is common in embedded/robotics/firmware contexts — see `skills/11_Robotics/`).

## Merge vs. Rebase

- **Merge** preserves the true history of when branches diverged and converged, at the cost of merge commits cluttering the log. Safe for shared/public branches — never rewrites history other people have already pulled.
- **Rebase** rewrites a branch's commits onto a new base, producing a linear, cleaner history — but rewrites commit hashes, which is dangerous on any branch others have already based work on. Rule: rebase freely on your own local, not-yet-pushed (or not-yet-shared) branches; never rebase a branch other people are actively building on top of, without explicit coordination.
- Squash-merge (common default on GitHub/GitLab PRs) gives you a clean one-commit-per-feature `main` history while still allowing messy, iterative commits during review — a good default for most teams that want clean history without enforcing perfect commit hygiene during development.

## Commit Hygiene

- Atomic commits: each commit should represent one logical change, and the codebase should build/pass tests at every commit (this matters for `git bisect` to actually work when hunting a regression).
- Commit message convention: a short imperative summary line (`Fix race condition in session refresh`), optionally a blank line then a body explaining *why*, not just *what* (the diff already shows *what*). Conventional Commits (`feat:`, `fix:`, `chore:`, `docs:`) is a reasonable, widely-adopted convention if you want machine-parseable history (e.g., for automated changelog generation).
- Never commit secrets. Use `.gitignore` proactively, and a pre-commit hook (e.g., `gitleaks`, `trufflehog`) as a backstop — once a secret is committed, rotating it is mandatory even after removing it from history, because it's recoverable from anyone's local clone or any fork.

## Monorepo vs. Polyrepo

| | Monorepo | Polyrepo |
|---|---|---|
| Cross-cutting changes | Easy — one atomic commit/PR touches every affected package | Hard — requires coordinated PRs across repos, versioning, and dependency bumps |
| Build tooling | Needs investment (Bazel, Nx, Turborepo, or similar) to avoid building/testing everything on every change | Each repo's build is naturally scoped and simple |
| Ownership clarity | Requires deliberate `CODEOWNERS`/access-control discipline | Natural, repo-level ownership boundaries |
| CI time at scale | Can balloon without incremental/affected-only build tooling | Naturally stays fast per-repo |

**Decision rule:** Most teams under ~50 engineers are well served by a monorepo (or a small number of repos grouped by genuine deployment/ownership boundary) — it removes an entire category of cross-repo dependency-version coordination overhead. Reach for polyrepo specifically when teams genuinely need independent release cadences, different access-control boundaries (e.g., open-source one component, keep another private), or different tech stacks that don't share build tooling well.

## Tags & Releases

- Use annotated tags (`git tag -a v1.2.0 -m "..."`) for releases, not lightweight tags — annotated tags carry metadata (tagger, date, message) and are the convention most release tooling expects.
- Tag immediately after the release commit lands, and never move a tag once published — moving a published tag breaks anyone who already built against it (mirrors the "never downgrade a version" rule in `VERSIONING.md`).

## Common Mistakes

- Force-pushing to a shared branch without coordinating, silently dropping others' commits.
- Giant, multi-purpose PRs that are nearly impossible to review properly — split by concern, even if it means more PRs.
- No branch protection rules on `main` (requiring CI pass + review before merge), leaving the deployable branch one accidental push away from breaking.
- Treating `.gitignore` as an afterthought instead of setting it up before the first commit, leading to accidentally committed build artifacts, `node_modules`, or `.env` files baked permanently into history.
