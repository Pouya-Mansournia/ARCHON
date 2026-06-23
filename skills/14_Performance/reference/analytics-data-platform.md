# Analytics & Data Platform Architecture

## Goal

Analytical workloads (dashboards, ad-hoc business queries, ML feature pipelines, historical reporting) have fundamentally different access patterns than transactional workloads — wide scans over large historical ranges instead of narrow, indexed point lookups. Running both on the same system past a certain scale degrades both: analytics queries starve transactional latency, and the transactional schema is rarely shaped the way analytical queries want the data.

## OLTP vs. OLAP

| | OLTP (transactional) | OLAP (analytical) |
|---|---|---|
| Access pattern | Many small reads/writes, row-oriented, latency-sensitive | Few large scans, column-oriented, throughput-sensitive |
| Schema shape | Normalized, optimized to avoid write anomalies | Denormalized/star-schema, optimized for scan and aggregation speed |
| Storage format | Row-store (Postgres, MySQL) | Columnar (Parquet, ORC; queried by BigQuery, Snowflake, Athena, ClickHouse) |
| Typical question | "What's this user's current balance?" | "What was average order value by region, by month, for the last two years?" |

## The Decoupling Pattern

The standard architecture decouples the two: the transactional database remains the source of truth for live application state, while analytical data is exported (via change-data-capture, scheduled batch export, or event streaming) into object storage in an open columnar format (Parquet is the practical default) and queried there with tools built for scan-heavy workloads (Athena, BigQuery, Snowflake, Spark, or a self-hosted engine like ClickHouse/DuckDB at smaller scale). This protects transactional latency from analytical query load and lets the analytical layer use a schema shape and storage format suited to its own access pattern.

## ETL vs. ELT

| Approach | Pattern | Best for |
|---|---|---|
| ETL (Transform before Load) | Transform data in a dedicated pipeline before it lands in the analytical store | Legacy pattern; still relevant when the destination can't cheaply do large-scale transforms itself |
| ELT (Transform after Load) | Load raw/lightly-processed data first, transform inside the analytical warehouse using its own compute (commonly via dbt) | The modern default — cloud warehouses are cheap and fast at large-scale transforms, and keeping raw data around supports re-deriving new transforms later without re-extracting from source |

## Batch vs. Streaming Analytics

| | When it's the right call |
|---|---|
| Batch (hourly/daily jobs) | The overwhelming majority of analytics and reporting needs — dashboards, business reporting, and most ML feature pipelines don't need sub-minute freshness |
| Streaming (Kafka/Kinesis + a stream processor) | Only when a specific, named use case needs near-real-time freshness (live fraud scoring, real-time operational dashboards) — this is meaningfully more operationally complex than batch and should be justified by a concrete latency requirement, not adopted by default |

## Common Mistakes

- Running heavy analytical/reporting queries directly against the production transactional database, degrading application latency for everyone.
- Building a streaming pipeline for a reporting need that would have been perfectly served by a nightly batch job.
- Choosing ETL-then-load by default in 2025+ stacks, when ELT-with-a-cloud-warehouse is usually simpler and more flexible for typical analytics needs.
- Letting the data lake become a "data swamp" — raw exports with no schema discipline, ownership, or documentation, making the data unusable for anyone but its original author.

## Decision Rule for This Domain

Decouple analytical workloads from the transactional database as soon as analytical queries measurably affect application performance, using a columnar export and a query engine matched to the team's scale (start with the cloud provider's managed serverless query service before standing up a dedicated cluster). Default to batch processing and ELT; require a specific, named latency requirement before adopting streaming infrastructure.
