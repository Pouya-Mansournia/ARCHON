# Search Architecture

## Goal

Decide whether your application's "search" feature needs a dedicated search engine or whether your existing relational database already handles it — a surprising number of "we need Elasticsearch" requests are actually solved by a well-indexed SQL query.

## When SQL-Native Search Is Enough

- PostgreSQL's full-text search (`tsvector`/`tsquery` with a GIN index) handles single-language text search with stemming, ranking, and reasonable performance for small-to-medium corpora (commonly comfortable into the low millions of rows, depending on hardware and query complexity).
- Simple `LIKE`/`ILIKE` with a trigram index (`pg_trgm` extension) works fine for fuzzy substring matching at moderate scale.
- **Decision rule:** If search is a secondary feature (e.g., "find a customer by name" in an internal admin tool) rather than a core product experience, start with Postgres full-text search. Don't introduce a dedicated search engine until you've measured that it's actually insufficient.

## When You Need a Dedicated Search Engine

| Need | Why SQL falls short |
|---|---|
| Relevance ranking across many fields with complex boosting | SQL full-text search ranking is comparatively crude |
| Faceted filtering (filter + count by multiple dimensions simultaneously) | Computationally expensive to do efficiently in SQL at scale |
| Typo tolerance / fuzzy matching at scale | Purpose-built search engines have far more sophisticated fuzzy-matching algorithms |
| Search-as-you-type with sub-100ms latency at high query volume | Dedicated search engines are built and indexed specifically for this access pattern |
| Multi-language search with language-specific analyzers | Search engines ship mature analyzer plugins; rolling this in SQL is a significant undertaking |

## Search Engine Decision Table

| Engine | Best for |
|---|---|
| Elasticsearch / OpenSearch | Most mature, largest ecosystem, strong for complex relevance tuning and analytics-adjacent use cases (log search, e-commerce search) |
| Meilisearch / Typesense | Simpler to operate, excellent out-of-the-box relevance and typo-tolerance for product/content search without heavy tuning — good default when you don't need Elasticsearch's full feature depth |
| Algolia | Fully managed, excellent developer experience and latency, but ongoing cost scales with usage — a strong build-vs-buy candidate (see `skills/17_Cost_Business/reference/build-vs-buy-tco.md`) when the team doesn't want to operate a search cluster at all |

## Keeping a Search Index in Sync

Search engines are typically a denormalized read-replica of your source-of-truth database, not the source of truth itself. Sync strategies:
- **Dual writes** (write to DB and search index in the same code path) — simplest, but risks the index silently drifting out of sync if one write succeeds and the other fails.
- **Change-data-capture (CDC) pipeline** (e.g., Debezium reading the DB's write-ahead log, or a queue-based outbox pattern) — more robust, decouples the write path from indexing latency, recommended once search correctness genuinely matters to the business.
- **Periodic full reindex** as a safety net regardless of which live-sync approach is used — catches drift before it becomes a customer-visible problem.

## Decision Rule for This Domain

Treat "do we need a dedicated search engine" as its own explicit decision, separate from "what search engine should we use." The first answer is "not yet" for a large share of products — don't skip straight to comparing Elasticsearch vs. Meilisearch before confirming the need is real.

## Common Mistakes

- Introducing Elasticsearch for a feature that a GIN-indexed `tsvector` column would have handled.
- No sync strategy between the source-of-truth database and the search index, leading to silent drift over time.
- Treating the search index as a system of record and losing data because it wasn't backed by a durable, recoverable source.
