# Storage Architecture

## Goal

Pick the right storage tier for each kind of data (hot transactional, file/blob, archival, backup) and design retention/lifecycle policy deliberately — storage cost and data-loss risk both compound silently when this is left to defaults.

## Storage Tiers

| Tier | Use For | Examples |
|---|---|---|
| Hot (transactional) | Actively queried application data | Postgres/MySQL primary storage (SSD-backed) |
| Warm (frequent object access) | User-uploaded files, generated reports actively served | S3 Standard, GCS Standard |
| Cool/Infrequent Access | Data accessed occasionally (older logs, infrequently-downloaded files) | S3 Infrequent Access, GCS Nearline |
| Cold/Archive | Compliance retention, rarely-if-ever accessed | S3 Glacier, GCS Coldline/Archive |

**Decision rule:** Set explicit lifecycle policies (e.g., move to Infrequent Access after 30 days, Archive after 1 year, delete after the legally/contractually required retention period) rather than leaving everything in the most expensive hot tier indefinitely — this is one of the easiest, lowest-risk cost optimizations available (see `skills/17_Cost_Business/reference/finops-cost-optimization.md`).

## Object Storage Design

- Use a clear, consistent key (path) naming convention from day one — retrofitting a key structure across millions of existing objects later is painful. A common, effective pattern: `{tenant_id}/{resource_type}/{resource_id}/{filename}`.
- Never make a bucket containing any sensitive data publicly readable by default — use signed URLs (time-limited, scoped access) for any client-facing file access instead of public bucket policies.
- Enable versioning on buckets containing important data — protects against accidental overwrites/deletes, at a modest storage cost.

## Backup Architecture

- **3-2-1 rule** as a baseline mental model: at least 3 copies of important data, on at least 2 different storage media/systems, with at least 1 copy off-site/in a different failure domain (different region/provider than production).
- Automated, regularly-tested database backups (point-in-time recovery via WAL archiving for Postgres, or managed automated backups via the cloud provider) are non-negotiable for any system holding real user data — see Core Principle #5 (Operational Reality) and #7 (Security by Default) in `skills/00_Core/reference/core-principles.md`.
- **A backup that has never been restored is not a verified backup.** Schedule periodic restore drills — this is the single most commonly skipped, and most consequential, backup practice.
- Define RTO (Recovery Time Objective — how long until service is restored) and RPO (Recovery Point Objective — how much data loss is acceptable, measured in time) explicitly per system; these numbers should drive backup frequency and the disaster-recovery architecture (see `skills/12_Security/reference/compliance-governance.md` and `skills/13_Reliability/reference/incident-management-chaos.md`).

## Data Lake / Analytics Storage

For analytics workloads (see `skills/14_Performance/reference/analytics-data-platform.md`), raw event/data exports commonly land in object storage in an open columnar format (Parquet) rather than directly in a transactional database — this decouples analytical querying (which benefits from columnar formats and tools like Athena/BigQuery/Spark) from transactional database load.

## Decision Rule for This Domain

Storage architecture decisions should explicitly name: which tier each data category lives in, the retention/lifecycle policy, the backup/restore strategy with stated RTO/RPO, and the access-control model (signed URLs vs. public vs. authenticated-proxy). Treat "we'll figure out retention later" as an under-engineering trigger (see `skills/00_Core/reference/over-under-engineering.md`).

## Common Mistakes

- Leaving all data in the most expensive hot storage tier indefinitely with no lifecycle policy.
- Publicly readable buckets containing sensitive user data.
- Backups that exist but have never been test-restored, discovered to be broken only during a real incident.
- No defined RTO/RPO, making it impossible to know whether the current backup strategy is actually adequate.
