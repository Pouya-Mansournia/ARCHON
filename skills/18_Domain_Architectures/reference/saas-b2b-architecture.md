# Reference Architecture: B2B SaaS

## Goal

Show a concrete, justified reference architecture for a typical multi-tenant B2B SaaS product at early-to-growth stage, illustrating how the modular-monolith-first, managed-services-by-default principles from across this knowledge base compose into one coherent system.

## Representative Stack

| Layer | Choice | Why |
|---|---|---|
| Frontend | Server-rendered or hybrid React framework (e.g., Next.js) | Fast iteration, good default SEO/performance characteristics for marketing pages alongside the authenticated app (see `skills/03_Frontend/`) |
| Backend | Modular monolith, one well-structured codebase with clear domain modules | Matches small-to-mid team size; defers microservices until a specific scaling/team-coordination need emerges (see `skills/07_Architecture/`) |
| Primary datastore | PostgreSQL, multi-tenant via a `tenant_id`/`organization_id` column on shared tables | The default datastore choice; row-level multi-tenancy is the simplest model that scales to a large number of small-to-mid-size tenants (see `skills/05_Database/` and `skills/02_Product/reference/business-architecture-patterns.md`) |
| Caching | Redis | Session storage, rate-limit counters, and cache-aside for expensive read paths once measured |
| Auth | Managed auth provider with SSO/SAML support added once enterprise customers require it | B2B SaaS customers increasingly expect SSO; build on a provider that supports it rather than hand-rolling (see `skills/12_Security/reference/authn-authz.md`) |
| Background jobs | A queue (RabbitMQ or Redis-based) for async work — report generation, email sends, webhook delivery | Keeps the request path fast; async offload is the first scaling lever, not a service split (see `skills/14_Performance/reference/scaling-patterns.md`) |
| Deployment | Containerized, deployed to a managed container service (Fargate/Cloud Run) behind CI/CD | Avoids Kubernetes until genuine orchestration complexity exists (see `skills/09_DevOps/`) |
| Observability | OpenTelemetry instrumentation, a managed platform (Datadog) or Prometheus/Grafana | Tier-appropriate for early-to-growth stage (see `skills/13_Reliability/`) |

## Multi-Tenancy as the Defining Architectural Decision

For B2B SaaS specifically, the multi-tenancy model is the single decision with the widest blast radius across the rest of the system — it touches data modeling, security (tenant data isolation), query patterns (every query needs a tenant filter), and pricing/billing logic. Row-level multi-tenancy (shared tables, tenant ID column, enforced via application logic or database row-level security) is the right default; reserve schema-per-tenant or database-per-tenant for specific large-enterprise customers with their own compliance/isolation requirements, applied selectively rather than as the system-wide default.

## What Changes as the Product Scales

- **Read load growth** → add read replicas and caching before considering any service split.
- **A specific component with genuinely independent scaling needs** (e.g., a reporting/analytics engine running expensive queries that would otherwise contend with the transactional workload) → extract that specific component, not a general microservices migration.
- **Enterprise customer requirements** (SSO, audit logs, data residency, dedicated infrastructure) → these often arrive as a bundle once the product starts closing larger deals, and should be anticipated in the data model (tenant isolation, audit logging hooks) even before they're contractually required.

## Common Mistakes

- Building multi-tenancy as an afterthought (a single shared database with no tenant isolation discipline), discovered as a security gap only once a customer asks how their data is isolated.
- Splitting into microservices in anticipation of scale that hasn't arrived, well before the team or the system has outgrown a modular monolith.
- No plan for enterprise-tier requirements (SSO, audit logs) until a large prospective customer asks for them in a sales cycle, forcing a rushed retrofit.

## Decision Rule for This Domain

Start as a modular monolith with row-level multi-tenancy on PostgreSQL, managed auth, async offload for background work, and tier-appropriate observability. Treat the multi-tenancy isolation model as the architecture decision deserving the most upfront care, since it's the hardest to retrofit later.
