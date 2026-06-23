# Database & Data Architecture — Full Reference

## Goal

The data model and datastore choice underlie almost every other architecture decision's difficulty later — get this layer right early, because migrating data models under live traffic is one of the most expensive classes of engineering work.

## Relational (SQL) Deep Dive

PostgreSQL is the strong default: ACID transactions, mature query planner, rich indexing (B-tree, GIN, GiST, BRIN), native `jsonb` for semi-structured data, extensions (`pgvector` for embeddings, `PostGIS` for geospatial, `TimescaleDB` for time-series) that let one database cover multiple needs longer than teams expect.

**Indexing rules:**
- Index every foreign key and every column used in a `WHERE`, `JOIN`, or `ORDER BY` on tables with meaningful row counts.
- Composite indexes should match query patterns (leftmost-prefix rule) — an index on `(tenant_id, created_at)` serves queries filtering by `tenant_id` alone or by both, but not by `created_at` alone.
- Watch for index bloat and unused indexes on write-heavy tables — every index adds write overhead; periodically audit with `pg_stat_user_indexes`.

**Replication:**
- Streaming replication (one primary, one or more read replicas) is the standard pattern for read scaling and high availability. Replicas introduce replication lag — design the application to tolerate slightly stale reads where acceptable, and route anything requiring up-to-date data (e.g., "read your own write" right after an update) to the primary.
- Logical replication enables selective table replication and zero-downtime major version upgrades — useful at scale, unnecessary complexity for small deployments.

**When to shard:** Only after a single primary genuinely can't handle the write volume (commonly tens of thousands of writes/sec sustained, varies by hardware and row size) or data size exceeds what's comfortably manageable on one instance for backup/maintenance windows. Sharding adds substantial complexity (cross-shard queries, rebalancing, distributed transactions) — confirm vertical scaling and read replicas are truly exhausted first.

## Document / NoSQL Deep Dive

MongoDB (or similar document stores) suit workloads where each record's shape varies meaningfully and queries are mostly per-document rather than cross-document joins. Real trade-off: weaker default consistency guarantees and join support than relational databases — multi-document transactions exist in MongoDB but are more expensive and less idiomatic than relational joins.

**When it's the right call:** Content management systems with highly variable content-block structures, catalogs with wildly different attribute sets per product category, event/log storage where each event type has a different shape.

**When it's the wrong call (common mistake):** Using MongoDB as the default datastore for a typical relational application (users, orders, line items, payments) where the data is naturally relational and the team ends up manually re-implementing joins and referential integrity in application code — this is strictly worse than just using Postgres.

## Key-Value Deep Dive

Redis is the standard choice: in-memory speed, rich data structures (strings, hashes, sets, sorted sets, streams), pub/sub, and optional persistence (RDB snapshots, AOF log) for durability when needed. Used for caching, session storage, rate-limiting counters, leaderboards (sorted sets), and lightweight pub/sub messaging.

**Durability caveat:** Redis is not a substitute for a real system-of-record database unless deliberately configured and operated for durability (AOF with appropriate fsync policy, replication, backups) — by default, treat data in Redis as ephemeral/reconstructable.

## Time-Series Deep Dive

TimescaleDB (a Postgres extension — keeps you in the Postgres ecosystem) or InfluxDB for high-volume, time-ordered data (metrics, IoT sensor readings, financial ticks). Key capability: automatic time-based partitioning and retention/downsampling policies that would be painful to hand-build on a general-purpose relational database at scale.

**Decision rule:** Reach for a dedicated time-series store once ingestion volume or retention/downsampling needs exceed what a well-indexed Postgres table comfortably handles — don't introduce it for low-volume metrics that a regular table handles fine.

## Vector Database Deep Dive

For AI/RAG features needing embedding similarity search: `pgvector` (Postgres extension) is the right default when you already run Postgres and don't yet have a clear need for a dedicated vector database's specialized indexing (HNSW at very large scale) or multi-tenancy features. Pinecone/Weaviate/Qdrant become worth the added operational surface area at larger embedding-corpus scale or when their specific features (hybrid search, advanced filtering at scale) are genuinely needed. See `skills/10_AI/reference/llm-integration-rag.md`.

## Object Storage Deep Dive

S3 (or GCS/Azure Blob) for anything file-shaped: user uploads, generated reports, backups, data lake raw storage. Never store large binary blobs directly in a relational database — it bloats backups, slows queries, and is dramatically more expensive per GB than object storage. Store a reference (URL/key) in the database, the actual bytes in object storage.

## Data Modeling Principles

- Normalize by default for transactional (OLTP) data — denormalize deliberately and selectively for specific, measured read-performance needs, not preemptively.
- Use UUIDs or ULIDs for primary keys when records might be created in distributed/offline contexts (mobile apps, multi-region writes) where sequential integer IDs would collide; otherwise sequential integers/bigints are simpler and more index-efficient.
- Soft deletes (a `deleted_at` timestamp) vs. hard deletes: soft deletes preserve audit trail and allow recovery, at the cost of needing to remember to filter deleted rows everywhere — decide explicitly and enforce consistently (e.g., via a default scope), don't mix patterns ad hoc across a codebase.

## Decision Rule for This Domain

Start from "what's the access pattern" (transactional CRUD, full-text search, time-ordered telemetry, similarity search, file storage), not from "what database is popular" — each access pattern has a clearly best-suited category, and the comparison matrix above should resolve most decisions quickly.

## Common Mistakes

- Using MongoDB by default for naturally relational data, then hand-rolling joins and referential integrity in application code.
- Storing large files directly in the database instead of object storage.
- No indexing strategy, leading to full table scans that get slower as data grows until the application appears to "mysteriously" degrade.
- Sharding prematurely, before vertical scaling and read replicas have actually been exhausted.
