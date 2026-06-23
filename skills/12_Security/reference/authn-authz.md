# Authentication & Authorization

## Goal

Authentication (who are you) and authorization (what can you do) are distinct concerns that should be designed and reasoned about separately, even though they're often implemented in adjacent code paths — conflating them is a common source of access-control bugs.

## Authentication Options

| Approach | Use when | Avoid when |
|---|---|---|
| Managed auth provider (Auth0, Clerk, AWS Cognito, Firebase Auth, Supabase Auth) | Default choice for almost every product — offloads password storage, MFA, social login, session management to a vetted provider | A specific regulatory/data-residency constraint genuinely prohibits a third-party auth provider |
| Self-hosted with a vetted library (e.g., a mature framework's built-in auth) | Strong reason to self-host (data residency, cost at extreme scale, specific compliance posture) while still avoiding hand-rolled crypto/session logic | Used as a default without a specific justifying reason — the operational and security burden of correctly handling password storage, session fixation, and token rotation is easy to underestimate |
| Hand-rolled authentication | Effectively never the right choice for a product team | Any production system — this is the clearest "never roll your own" case in this entire knowledge base |

## OAuth 2.0 / OIDC Essentials

OAuth 2.0 handles delegated authorization (granting a third party limited access without sharing credentials); OpenID Connect (OIDC) builds identity/authentication on top of OAuth 2.0. For most product authentication needs (login, social sign-in, SSO), OIDC via a managed provider is the right mental model and the right implementation path — understand the Authorization Code flow (with PKCE for public clients) as the default flow for web and mobile apps; avoid the Implicit flow (deprecated due to token-exposure risks).

## Session Management

| Approach | Trade-off |
|---|---|
| Server-side sessions (session ID in a cookie, state stored server-side) | Easy to revoke immediately; requires session storage (often Redis) shared across instances |
| Stateless tokens (JWT) | No server-side storage needed, scales easily across instances; harder to revoke before expiry (mitigate with short expiry + refresh tokens, or a revocation list for the rare cases needing immediate invalidation) |

**Decision rule:** Server-side sessions are simpler to reason about and revoke; default to them unless there's a specific need for stateless scaling (e.g., a public API used by many independent clients) that justifies JWT's added revocation complexity.

## Authorization Models

| Model | How it works | Use when |
|---|---|---|
| RBAC (Role-Based Access Control) | Users assigned roles; roles grant permissions | Most products — a manageable, well-understood default |
| ABAC (Attribute-Based Access Control) | Access decisions based on attributes of the user, resource, and context (e.g., "owner of this record," "same organization") | Fine-grained, context-dependent access rules that RBAC's fixed roles can't express cleanly (e.g., multi-tenant systems where a user's access depends on resource ownership, not just their role) |
| ReBAC (Relationship-Based Access Control) | Access derived from relationships in a graph (e.g., "can edit if a collaborator on this document") | Collaboration-heavy products with rich, evolving sharing/permission relationships (the model behind Google Docs-style sharing) |

**Decision rule:** Start with RBAC. Add ABAC-style resource-ownership checks (the most common real-world need: "is this user the owner/member of the org that owns this resource") as soon as the product has multi-tenant or per-resource ownership semantics — this is needed by almost every real SaaS product, not just an edge case.

## Centralizing Authorization Logic

Scatter-implemented authorization checks (an `if user.role == 'admin'` sprinkled inconsistently across the codebase) are a recurring source of access-control vulnerabilities — a single missed check is a security hole. Centralize authorization logic behind a single policy layer/middleware so every access path goes through the same, auditable rule set.

## Common Mistakes

- Hand-rolling password hashing or session token generation instead of using a vetted library/managed provider.
- Conflating authentication (who you are) with authorization (what you can do), leading to checks that verify identity but skip permission checks, or vice versa.
- Inconsistent, scattered authorization checks across the codebase rather than a centralized policy layer.
- Using JWTs for session management without a clear revocation strategy, leaving compromised tokens valid until natural expiry.

## Decision Rule for This Domain

Use a managed auth provider by default. Use server-side sessions unless a specific stateless-scaling need justifies JWTs. Start authorization with RBAC, add resource-ownership/ABAC-style checks as soon as multi-tenancy exists, and centralize all authorization logic behind one policy layer.
