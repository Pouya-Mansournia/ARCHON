---
name: archon-decision-engine
description: The master decision engine — how ARCHON routes a question to the right domain skill(s), resolves conflicts between competing principles, and calibrates confidence. This is the capstone skill tying together all 20 domain skill modules (00-19).
---

# 99 — Decision Engine (L1-L5, Cross-Cutting)

**Level:** All levels — this is the routing and arbitration layer above every domain skill.

## Goal

With 20 domain skill modules (00_Core through 19_Review_Outputs) each containing their own decision rules, ARCHON needs a consistent process for (1) figuring out which domain(s) a given question actually belongs to, (2) resolving it when two domains' decision rules seem to pull in different directions, and (3) being honest about how confident the resulting recommendation actually is. This skill is that process — read it whenever a question doesn't cleanly map to a single domain skill, or when domain rules conflict.

## Step 1 — Route the Question

Most questions map to one or two domains fairly directly (a database choice → `skills/05_Database/`; a deployment topology question → `skills/09_DevOps/`). When a question spans many domains (e.g., "how should we architect our new product"), decompose it into its constituent decisions first — product/business framing (`skills/02_Product/`), data architecture, API design, cloud/deployment, security — and address each with its own domain skill before synthesizing, rather than trying to answer the whole question from general intuition. See `skills/18_Domain_Architectures/` for worked examples of this synthesis for common product categories.

## Step 2 — Apply the Universal Filters First

Before diving into domain-specific rules, run every recommendation through the two universal filters defined in `skills/00_Core/`:

1. **The Over/Under-Engineering Detector** (`skills/00_Core/reference/over-under-engineering.md`) — is the candidate solution solving a real, current problem, or a hypothetical future one (over-engineering)? Does it cover the genuine baseline requirements (auth, backups, monitoring) every production system needs (under-engineering)?
2. **The Engineering Decision Principles priority order** (`skills/00_Core/reference/core-principles.md` and `agents/archon.md`) — Simplicity → Maintainability → Reliability → Development Speed → Cost Efficiency → Security → Scalability → Performance → Future Flexibility → Technical Elegance.

## Step 3 — Resolving Conflicts Between Domain Rules

When two domain skills' decision rules appear to conflict (e.g., `skills/07_Architecture/` says default to a modular monolith, but a specific component's needs from `skills/14_Performance/` seem to argue for extracting a service), resolve using the priority order above, applied to the *specific* trade-off at hand — not by mechanically picking whichever domain skill was consulted first. Document the resolution as an ADR (`skills/19_Review_Outputs/reference/adr-decision-log-templates.md`) when the conflict and its resolution are significant enough to outlive the conversation.

## Step 4 — Calibrate Confidence Honestly

Not every recommendation deserves the same confidence level. See `reference/output-standard-and-confidence.md` for the full confidence-calibration framework — the short version: high confidence requires both a well-understood problem and strong consensus among the relevant domain decision rules; low confidence should be stated explicitly whenever the question involves unusual constraints, conflicting principles with no clean resolution, or a domain at the edge of this knowledge base's coverage.

## Reference Files

- `reference/decision-trees.md` — routing decision trees for common multi-domain questions (new product architecture, scaling an existing system, security review, technology migration).
- `reference/output-standard-and-confidence.md` — the full 10-part Output Standard definition and the confidence-calibration framework.
