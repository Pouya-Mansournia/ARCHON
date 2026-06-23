---
name: devops-cicd
description: Containers, Docker, Kubernetes, CI/CD pipelines, and GitOps — stage-aware decision rules for when each layer of deployment/orchestration sophistication is earned vs. premature.
---

# 09 — DevOps, Containers & CI/CD (L3)

**Level:** L3 — Infrastructure & Cloud.

## Goal

Build a deployment pipeline and runtime orchestration layer that matches the team's actual operational maturity and the system's actual scale — Kubernetes for a single-service MVP is the single most common over-engineering trigger in this entire knowledge base, named explicitly in `skills/00_Core/reference/over-under-engineering.md`.

## Containers & Orchestration Decision Matrix

| Approach | Use when | Avoid when |
|---|---|---|
| No containers (managed PaaS: Render, Railway, Fly.io, Heroku-style) | Earliest stage, small team, want to minimize ops entirely | Need fine-grained infra control or have specific compliance/networking requirements the PaaS can't satisfy |
| Docker + managed container service (ECS/Fargate, Cloud Run, App Service) | Most products past the earliest prototype stage — containerized for portability and reproducibility, without taking on full Kubernetes operational burden | Team needs Kubernetes-specific features (custom schedulers, complex multi-service networking, operators) |
| Kubernetes (self-managed or managed: EKS/GKE/AKS) | Genuinely complex multi-service systems with real scaling/orchestration needs, or a platform team dedicated to operating it | Single service or small number of services, small team, no dedicated platform/SRE capacity — see the over-engineering trigger |

## Decision Rule

Default to Docker + a managed container service (Fargate, Cloud Run, or equivalent) for the overwhelming majority of products. Adopt Kubernetes only with a demonstrated need: a genuinely complex multi-service topology, a real requirement for custom orchestration logic, or a team large enough to dedicate real platform-engineering capacity to operating it well. Kubernetes operated badly (no one really owns it, no one fully understands the cluster) is worse than no Kubernetes at all.

## CI/CD — Always Justified, Unlike Kubernetes

Unlike container orchestration sophistication, a CI/CD pipeline (automated build, test, and deploy) is close to a universal requirement — even the smallest team benefits from not deploying via manual SSH/SCP. The question is pipeline sophistication (see `reference/cicd-gitops.md`), not whether to have one at all.

## Reference Files

- `reference/containers-docker-kubernetes.md` — full container/orchestration deep dive, including Kubernetes core concepts for when it is adopted.
- `reference/cicd-gitops.md` — CI/CD pipeline design, deployment strategies, and GitOps practices.
