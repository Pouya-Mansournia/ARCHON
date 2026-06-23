---
name: database-data-architecture
description: Database and data architecture — relational vs NoSQL vs key-value vs time-series vs search vs vector vs object storage, caching architecture, search architecture, and storage architecture decision rules.
---

# 05 — Database & Data Architecture (L2/L3)

**Level:** L2 Software Engineering core, extending into L3 Infrastructure for storage/caching at scale.

## Goal

Choose the right datastore(s) for each access pattern — most non-trivial systems use more than one — and avoid both "everything in Postgres forever, including search and full-text and time-series" and "premature polyglot persistence with five datastores for a system serving a hundred users."

## Datastore Category Decision Matrix

| Category | Default Choice | Use For | Avoid When |
|---|---|---|---|
| Relational / SQL | PostgreSQL | Default for almost everything — strong consistency, mature tooling, flexible querying | Schema is genuinely unknown/highly variable per-record at write time |
| Document / NoSQL | MongoDB | Highly variable/nested document shapes, rapid schema iteration | Need for strong cross-document transactional consistency |
| Key-Value / Cache | Redis | Caching, session storage, rate-limit counters, leaderboards, pub/sub | Need for it to be the system of record (it's not durable enough by default for that role) |
| Time-Series | TimescaleDB / InfluxDB | Metrics, sensor data, IoT telemetry, financial tick data | General-purpose application data with no time-ordered query pattern |
| Search | Elasticsearch / OpenSearch / Meilisearch | Full-text search, faceted filtering, relevance ranking | Simple exact-match lookups that an indexed SQL query already handles well |
| Vector DB | pgvector (in Postgres) / Pinecone / Weaviate | Embedding similarity search for AI/RAG features | No AI/semantic-search feature actually exists yet |
| Object Storage | S3 / GCS / Azure Blob | Files, images, backups, data lake raw storage | Structured, queryable data that belongs in a real database |

## PostgreSQL vs. MongoDB — The Most Common Real Decision

Default to PostgreSQL unless there's a specific, named reason for a document store: genuinely unpredictable/sparse schema per record, or a workload that's overwhelmingly document-shaped with little need for cross-record joins. Postgres's `jsonb` column type already covers most "I want some schema flexibility" needs without giving up relational integrity and tooling for the rest of the data.

## Decision Rule

Most products need exactly one primary relational datastore (Postgres) plus a cache (Redis) once there's real read traffic to offload. Add a search engine, time-series store, or vector DB only when there's a specific, demonstrated feature need (full-text search at scale, sensor/metrics ingestion, AI semantic search) — not preemptively.

## Reference Files

- `reference/database-data-architecture.md` — full datastore comparison, indexing, replication, and data modeling guidance.
- `reference/caching-architecture.md` — caching layers, invalidation strategies, cache-aside vs write-through.
- `reference/search-architecture.md` — full-text search architecture, when SQL `LIKE`/`tsvector` suffices vs. needing a dedicated search engine.
- `reference/storage-architecture.md` — object storage, data lakes, backup/retention architecture.
