---
name: security-architecture
description: Security architecture — authentication and authorization, data protection and encryption, and threat modeling/application security — with "secure by default" decision rules tied back to the Under-Engineering Detector.
---

# 12 — Security Architecture (L4)

**Level:** L4 — Principal Engineering.

## Goal

Apply security as a default property of the system, not a feature bolted on before a compliance audit — most real-world breaches exploit basic gaps (missing auth checks, unencrypted sensitive data, unpatched dependencies) rather than exotic attacks, so the highest-leverage security work is disciplined coverage of the fundamentals.

## Security-by-Default Checklist (Maps to the Under-Engineering Detector)

`skills/00_Core/reference/over-under-engineering.md` already flags "no real auth" as a classic under-engineering trigger. This domain expands that into a fuller default-secure baseline every production system should have regardless of stage:

| Area | Default expectation |
|---|---|
| Authentication | Managed auth provider or well-vetted library — never hand-rolled password storage/session handling |
| Authorization | Explicit, centrally-defined access rules — not scattered ad-hoc checks across the codebase |
| Data in transit | TLS everywhere, no exceptions for "internal" traffic that turns out to cross a trust boundary |
| Data at rest | Encryption for sensitive data at minimum; full-disk/volume encryption as a baseline |
| Secrets management | A secrets manager (not hardcoded values, not committed `.env` files) |
| Dependency hygiene | Automated vulnerability scanning on dependencies, with a real process for acting on findings |
| Input validation | Validate and sanitize all external input — the root cause of most injection-class vulnerabilities |

## Decision Rule

Default to managed/standard solutions (managed auth, established encryption libraries, a real secrets manager) over custom security implementations in virtually all cases — security is one of the few domains where "don't roll your own" is close to an absolute rule, not just a strong default. Reserve custom security engineering for genuinely novel requirements a standard solution can't satisfy, and have that work reviewed by someone with real security expertise.

## Reference Files

- `reference/authn-authz.md` — authentication and authorization patterns in depth (OAuth/OIDC, RBAC/ABAC, session management).
- `reference/data-protection-encryption.md` — encryption at rest/in transit, key management, and data classification.
- `reference/threat-modeling-appsec.md` — threat modeling process, OWASP Top 10 coverage, and application security practices.
- `reference/compliance-governance.md` — GDPR/HIPAA/SOC 2/PCI-DSS technical requirements and staged compliance posture.
