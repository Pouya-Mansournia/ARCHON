# Threat Modeling & Application Security

## Goal

Threat modeling is the practice of systematically asking "how could this system be attacked" before it ships, rather than discovering the answer via an actual incident — it doesn't need to be heavyweight to be valuable; even a lightweight pass catches a meaningful share of real-world vulnerabilities.

## A Lightweight Threat Modeling Process

1. **Identify what you're protecting** — the system's trust boundaries, sensitive data, and critical operations.
2. **Identify who/what could attack it** — external attackers, malicious or compromised users, and (often overlooked) insider risk.
3. **Enumerate how each component could be attacked** — the STRIDE categories below give a structured checklist.
4. **Rank by likelihood and impact** — same risk-ranking approach used in `/archon-review`'s critic-mode process.
5. **Decide and document mitigations** — for each significant threat, an explicit mitigation or an explicit, justified acceptance of the residual risk.

## STRIDE Categories

| Category | Threat | Example mitigation |
|---|---|---|
| Spoofing | Pretending to be someone/something else | Strong authentication, mutual TLS for service-to-service |
| Tampering | Unauthorized modification of data | Integrity checks, signed payloads, authorization controls |
| Repudiation | Denying having performed an action | Audit logging, non-repudiable records |
| Information disclosure | Exposing data to unauthorized parties | Encryption, access controls, data minimization |
| Denial of service | Making the system unavailable | Rate limiting, autoscaling, resource quotas |
| Elevation of privilege | Gaining unauthorized capability | Least-privilege design, centralized authorization, input validation |

## OWASP Top 10 — Application-Layer Baseline

| Risk | Core mitigation |
|---|---|
| Broken access control | Centralized, consistently-applied authorization checks (see `reference/authn-authz.md`) |
| Cryptographic failures | Proper encryption at rest/in transit, vetted libraries, sound key management (see `reference/data-protection-encryption.md`) |
| Injection (SQL, command, etc.) | Parameterized queries/prepared statements, never string-concatenated dynamic queries, input validation |
| Insecure design | Threat modeling during design, not just code review after the fact |
| Security misconfiguration | Hardened defaults, no unnecessary exposed services/ports, regular configuration audits |
| Vulnerable/outdated components | Automated dependency scanning, a real patching process, not "we'll update eventually" |
| Identification/authentication failures | Managed auth, MFA where appropriate, secure session management |
| Software/data integrity failures | Verified dependency sources, signed artifacts/releases, integrity checks on critical updates |
| Logging/monitoring failures | Security-relevant event logging, alerting on anomalous patterns (see `skills/13_Reliability/`) |
| Server-side request forgery (SSRF) | Validate/restrict outbound requests triggered by user input, especially for any feature that fetches a user-supplied URL |

## Input Validation — The Common Thread

The majority of injection-class vulnerabilities (SQL injection, command injection, XSS, SSRF) trace back to the same root cause: untrusted input treated as trusted. Validate and sanitize all external input at the boundary, use parameterized queries/prepared statements for any database interaction, encode output appropriately for its context (HTML-escape for HTML output, etc.), and apply the same untrusted-input discipline to LLM prompts (see `skills/10_AI/reference/ai-product-safety.md`).

## Dependency & Supply Chain Security

Run automated vulnerability scanning (Dependabot, Snyk, or equivalent) as part of CI, and have an actual process for triaging and acting on findings — a scanner that flags vulnerabilities no one looks at provides no real protection. Pin dependency versions and review what a new dependency actually does before adding it, particularly for anything with broad runtime access.

## Common Mistakes

- Skipping threat modeling entirely until a security review (often externally mandated) forces the question, rather than building it into the design process.
- String-concatenated SQL queries instead of parameterized queries — still one of the most common real-world vulnerability classes despite being well understood for decades.
- Running a dependency vulnerability scanner but never triaging or acting on its findings.
- No SSRF protection on any feature that fetches a user-supplied URL (webhooks, link previews, file imports).

## Decision Rule for This Domain

Run a lightweight threat-modeling pass (STRIDE categories, ranked by likelihood/impact) during design for any system handling sensitive data or critical operations. Treat input validation and parameterized queries as non-negotiable defaults, and maintain an active (not just configured) dependency vulnerability scanning process.
