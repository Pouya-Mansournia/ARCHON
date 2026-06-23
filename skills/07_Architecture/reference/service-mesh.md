# Service Mesh

## Goal

Decide whether a service mesh (Istio, Linkerd, Consul Connect) is solving a problem you actually have, or adding a substantial new operational layer to a microservices environment that doesn't yet need it.

## What a Service Mesh Actually Provides

- **mTLS between services automatically**, without each service implementing TLS itself — strong security default once you have many services.
- **Traffic management**: fine-grained routing (canary releases, traffic splitting, retries, circuit breaking) configured declaratively rather than in application code.
- **Observability**: automatic, consistent metrics/tracing for service-to-service calls (latency, error rate, request volume) without instrumenting every service individually.
- **Policy enforcement**: consistent rate limiting, access control between services, independent of each service's own implementation.

## When It Earns Its Complexity

A service mesh is genuinely valuable when you have: a meaningful number of independently-deployed microservices (commonly cited threshold is somewhere in the dozens, not a handful), multiple teams each owning different services who need consistent cross-cutting policy without coordinating changes to every service's code, and a real need for the specific capabilities above (canary deployments, mTLS at scale, consistent cross-service observability).

## When It's Over-Engineering

- A handful of services (single digits) — the sidecar proxy overhead (every service gets a co-located proxy, typically Envoy) and the operational learning curve (mesh control plane, CRDs, debugging "why did my request 503 inside the mesh") usually outweigh the benefit at this scale.
- A monolith or modular monolith — there's no service-to-service traffic for the mesh to manage.
- A team with no prior service-mesh operational experience taking this on "because it's best practice" without a specific capability gap it closes today.

## Simpler Alternatives That Solve Part of the Same Problem

- mTLS between services: can often be handled at the load balancer/API gateway layer, or via cloud-provider-native private networking, without a full mesh.
- Retries/circuit breaking: can be implemented in a shared client library (e.g., a common HTTP client wrapper) used by all services, without mesh-level infrastructure.
- Consistent observability: can be achieved via a shared instrumentation library/SDK (OpenTelemetry) without the mesh layer.

**Decision rule:** Reach for these simpler alternatives first. Adopt a full service mesh only once you've outgrown what a shared client library and cloud-native networking can reasonably provide, and you have the dedicated platform engineering capacity to operate it well.

## Decision Rule for This Domain

Treat "should we adopt a service mesh" as a question with a default answer of "not yet" for most organizations, reversed only by specific evidence: real multi-team microservices scale, a genuine cross-cutting traffic-management or mTLS-at-scale need, and a team with (or actively building) the operational capacity to run it. This mirrors the Kubernetes-for-a-tiny-MVP over-engineering trigger in `skills/00_Core/reference/over-under-engineering.md` — a service mesh is the same pattern one layer up the stack.

## Common Mistakes

- Adopting a service mesh for a handful of services with no specific capability gap it's closing.
- Underestimating the learning curve and debugging difficulty a mesh control plane adds to incident response.
- Adopting a mesh without first trying simpler alternatives (shared client libraries, cloud-native networking) that solve a meaningful subset of the same problems.
