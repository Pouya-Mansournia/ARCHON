# Roadmap

## Now (v1.0)
- Ship the full L1-L5 knowledge base across 20 skill domains / 56 topics.
- Ship the single ARCHON agent persona and 8 core commands.
- Ship registries, governance docs, and onboarding docs.

## Next (v1.1 - v1.x)
- Add worked "Architecture Review" transcripts for 3-5 real-world stack combinations (e.g., AI SaaS on AWS, robotics fleet platform, fintech ledger system).
- Expand `tests/` with executable consistency checks (link validation, frontmatter schema validation) runnable via a small Node/Python script.
- Add a `/archon-cost` shortcut command for fast FinOps-only reviews.
- Add language-specific style addenda (e.g., Rust-specific backend guidance, Swift-specific mobile guidance) as additional reference files rather than new skills.

## Later (v2.0+)
- Optional companion "Brand-OS" lightweight skill if ARCHON is white-labeled for a team or company (currently intentionally scoped out — see `ARCHITECTURE_DECISIONS.md` ADR-002).
- Optional integration hooks for project trackers / knowledge bases (read-only context pull), following the same `CONNECTORS.md` convention used by other Claude plugins — only if a real connector need emerges. ARCHON v1.0 is intentionally standalone (knowledge-only, no required integrations).
- Community-contributed reference modules for additional domain verticals (healthtech, gaming infra, telecom) via `CONTRIBUTING.md`.

## Explicitly Not Planned
- Splitting ARCHON into a multi-agent C-suite roster (CEO/CPO/CTO/CIO/COO/CFO/CRO/CMO/CHRO/CBO). This was evaluated and deliberately rejected — see `ARCHITECTURE_DECISIONS.md` ADR-001. ARCHON stays a single cohesive persona with internal seniority levels.
