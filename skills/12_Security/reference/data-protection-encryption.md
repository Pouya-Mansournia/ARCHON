# Data Protection & Encryption

## Goal

Protect data proportionally to its sensitivity — not every field needs the same handling, but every system needs an explicit, deliberate answer for how sensitive data is classified, encrypted, and accessed, rather than a uniform default of "the database has a password, that's our security."

## Data Classification

| Class | Examples | Baseline handling |
|---|---|---|
| Public | Marketing content, public listings | No special protection needed |
| Internal | Business metrics, internal documentation | Access-controlled, not encrypted beyond standard infrastructure encryption |
| Sensitive (PII) | Names, emails, addresses, phone numbers | Encrypted at rest, access-logged, minimized retention |
| Highly sensitive | Payment data, health records, government IDs, credentials | Encrypted at rest and in transit, strict access controls, often subject to specific regulatory regimes (PCI-DSS, HIPAA), minimized storage footprint (e.g., tokenize payment data rather than storing raw card numbers) |

Classify data explicitly during data modeling (see `skills/05_Database/reference/database-data-architecture.md`), not as an afterthought once a breach or audit forces the question.

## Encryption in Transit

TLS for all network communication, with no "internal traffic doesn't need it" exceptions — internal network boundaries are not as trustworthy as they're often assumed to be (lateral movement after any single compromised host is a standard attack pattern), and modern infrastructure (load balancers, service meshes) makes TLS-everywhere a solved, low-cost default rather than a meaningful engineering burden.

## Encryption at Rest

| Layer | What it covers |
|---|---|
| Full-disk / volume encryption | Baseline protection if physical storage media is lost/stolen/improperly decommissioned — essentially free with modern cloud storage, should be the default everywhere |
| Database-level encryption | Encrypts data within the database engine itself (transparent data encryption), protecting against direct storage access bypassing the application |
| Field-level / application-level encryption | Specific highly sensitive fields encrypted before ever reaching the database, so even a full database compromise doesn't expose them in plaintext — reserved for the highest-sensitivity fields given the added complexity (key management, queryability trade-offs) |

## Key Management

Never store encryption keys alongside the data they protect, and never hardcode them in application code or commit them to version control. Use a managed key management service (AWS KMS, GCP Cloud KMS, Azure Key Vault, HashiCorp Vault) for key generation, rotation, and access control. Rotate keys on a defined schedule and immediately upon any suspected compromise.

## Secrets Management

| Anti-pattern | Correct approach |
|---|---|
| Hardcoded API keys/credentials in source code | Secrets manager (AWS Secrets Manager, GCP Secret Manager, HashiCorp Vault, or at minimum the CI/CD platform's encrypted secrets feature) |
| Committed `.env` files with real credentials | `.env.example` with placeholder values committed; real `.env` gitignored, real values injected at deploy time |
| Shared, long-lived static credentials across environments | Per-environment credentials, rotated regularly, with short-lived credentials (e.g., temporary IAM role credentials) preferred where supported |

## Data Minimization & Retention

Collect and retain only the data actually needed for the product to function, and define explicit retention/deletion policies rather than keeping everything indefinitely "in case it's useful later." This reduces breach blast radius and is often a direct regulatory requirement (GDPR's data minimization principle, the "right to be forgotten").

## Common Mistakes

- No explicit data classification, treating all data with the same (often insufficient) level of protection.
- Hardcoded secrets in source code or committed environment files, a top-ten recurring real-world breach vector.
- TLS only for "external" traffic, leaving internal service-to-service communication unencrypted on the assumption the internal network is inherently trustworthy.
- Storing encryption keys in the same place as the data they protect, defeating the purpose of encryption if that location is ever compromised.
- Indefinite data retention with no deletion policy, increasing both breach impact and regulatory exposure.

## Decision Rule for This Domain

Classify data sensitivity explicitly during design. Encrypt in transit everywhere, encrypt at rest for sensitive data at minimum, and use a real secrets manager and key management service — never hand-managed secrets or self-managed keys colocated with the data.
