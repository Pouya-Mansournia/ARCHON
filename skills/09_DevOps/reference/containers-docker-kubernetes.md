# Containers, Docker & Kubernetes

## Goal

Containerization solves a real, near-universal problem (environment consistency between dev/staging/prod, reproducible deployments). Kubernetes solves a much narrower set of orchestration problems at a real operational cost. Treat these as two separate decisions, not one bundled choice.

## Why Containerize (Almost) Everything

- **Environment parity** — "works on my machine" failures drop sharply when dev, CI, and production all run the same container image.
- **Reproducible builds** — a Docker image is a versioned, immutable artifact; rollback is "deploy the previous image tag," not "hope the server state matches what it was before."
- **Portability** — moving between providers or between a managed container service and (eventually) Kubernetes is far easier starting from a containerized app than from a bare-metal/VM deployment.

## Dockerfile Practices

- Use multi-stage builds to keep final images small (build dependencies don't need to ship in the runtime image).
- Pin base image versions explicitly (`node:20.11-slim`, not `node:latest`) — floating tags break reproducibility silently when the underlying image updates.
- Run as a non-root user inside the container — a basic security hardening step that's easy to skip and shouldn't be.
- Use `.dockerignore` aggressively (node_modules, .git, local env files) to keep build context small and avoid leaking secrets into images.

## Managed Container Services (the Right Default for Most Teams)

| Service | Provider | Good fit for |
|---|---|---|
| ECS/Fargate | AWS | Teams in AWS wanting container orchestration without managing the underlying cluster |
| Cloud Run | GCP | Simple, scale-to-zero-capable container hosting, very low ops overhead, good for APIs and background workers |
| App Service / Container Apps | Azure | Azure-committed teams wanting managed container hosting |

These give most of containerization's benefit (consistency, portability, reproducible deploys) with a small fraction of Kubernetes's operational surface area (no cluster upgrades, no node management, no networking-stack ownership).

## Kubernetes — Core Concepts (For When It's Actually Adopted)

| Concept | What it is |
|---|---|
| Pod | Smallest deployable unit — one or more tightly-coupled containers |
| Deployment | Manages a set of replica Pods, handles rolling updates |
| Service | Stable network endpoint routing to a set of Pods |
| Ingress | Manages external HTTP(S) access into the cluster, routing rules |
| ConfigMap / Secret | Externalized configuration and sensitive values, decoupled from the image |
| Horizontal Pod Autoscaler | Automatically scales replica count based on load metrics |
| Namespace | Logical isolation boundary within a cluster (e.g., per-environment or per-team) |

## When Kubernetes Earns Its Complexity

A genuinely complex multi-service system with real, differentiated scaling needs per service; a platform/SRE team with the bandwidth and expertise to own cluster upgrades, security patching, and networking; or a specific need Kubernetes uniquely satisfies (custom operators, complex stateful workload orchestration, multi-tenant cluster isolation requirements). Absent these, the managed-container-service tier above delivers most of the benefit at a fraction of the ongoing operational cost.

## Common Mistakes

- Adopting Kubernetes for a single-service MVP because "we'll need to scale eventually" — by the time real orchestration needs emerge, the team will understand its own scaling bottlenecks far better than it does today, and the migration from managed-containers to Kubernetes is mechanical.
- Running a Kubernetes cluster with no one clearly owning upgrades/security patching, leading to a cluster running an unsupported, unpatched version.
- Floating Docker base image tags (`:latest`) causing non-reproducible builds and surprise breakage.
- Running containers as root inside the image, missing a basic and easy security hardening step.

## Decision Rule for This Domain

Containerize almost everything past the earliest prototype. Deploy to a managed container service by default. Escalate to Kubernetes only against a specific, named orchestration need and confirmed operational capacity to run it well — this mirrors the general Over-Engineering Detector pattern in `skills/00_Core/reference/over-under-engineering.md`.
