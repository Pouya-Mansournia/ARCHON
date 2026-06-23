---
name: cloud-infrastructure
description: Cloud provider selection (AWS, Azure, GCP, and alternatives), multi-region architecture, edge computing, and multi-cloud strategy — with stage-aware decision rules for when each level of infrastructure sophistication is justified.
---

# 08 — Cloud, Infrastructure & Multi-Region (L3)

**Level:** L3 — Infrastructure & Cloud.

## Goal

Choose a cloud provider and infrastructure topology that matches actual scale, actual compliance/geographic needs, and actual team capacity — multi-region and multi-cloud are two of the most commonly over-applied infrastructure decisions in the industry.

## Cloud Provider Decision Matrix

| Provider | Best for |
|---|---|
| AWS | Broadest service catalog, largest talent pool, default safe choice for most general-purpose workloads |
| GCP | Strong data/analytics/ML tooling (BigQuery, Vertex AI), strong Kubernetes (GKE, where K8s originated), good fit for data-heavy or ML-heavy products |
| Azure | Strong fit for enterprises already invested in Microsoft ecosystem (AD, .NET, Office 365 integration) |
| Cloudflare (Workers/Pages/R2) | Edge-first, simple apps wanting global low latency with minimal infra ops |
| Vercel / Netlify | Frontend-focused teams wanting zero-ops deployment for Next.js/static/Jamstack apps |
| Hetzner / DigitalOcean | Cost-sensitive teams with straightforward infra needs, less need for the hyperscaler service catalog depth |
| Oracle Cloud (OCI) | Specific enterprise/legacy Oracle-ecosystem ties, or notably cheap egress/compute for certain workloads |

**Decision rule:** Default to AWS unless a specific factor points elsewhere (ML/data-heavy → GCP; deep Microsoft ecosystem → Azure; simple app wanting minimal ops and global edge → Cloudflare/Vercel; pure cost sensitivity with simple needs → Hetzner/DigitalOcean). Switching cloud providers later is expensive — but so is over-engineering for hypothetical multi-cloud portability from day one (see `reference/edge-multi-cloud.md`).

## Multi-Region — When It's Real vs. Premature

Multi-region is justified by: a specific data-residency/compliance requirement, a demonstrated latency problem for a specific user geography, or a genuine disaster-recovery requirement beyond what single-region + good backups provides. It is not justified by "we might have global users someday."

## Reference Files

- `reference/cloud-providers-infrastructure.md` — full provider comparison, core service categories (compute, networking, managed databases), and infrastructure-as-code practices.
- `reference/multi-region-architecture.md` — multi-region patterns (active-passive, active-active), data residency, and the staged path to get there.
- `reference/edge-multi-cloud.md` — edge computing use cases and multi-cloud strategy, including when it's genuinely warranted vs. an over-engineering trigger.
