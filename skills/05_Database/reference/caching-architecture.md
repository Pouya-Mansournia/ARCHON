# Caching Architecture

## Goal

Caching is one of the highest-leverage performance tools available — and one of the easiest to get subtly wrong (stale data, cache stampedes, invalidation bugs that are notoriously hard to debug). Treat cache design with the same rigor as database design, not as a quick bolt-on.

## Cache Layers

| Layer | What it caches | Example |
|---|---|---|
| Browser/client cache | Static assets, API responses with cache headers | `Cache-Control`, `ETag` |
| CDN / edge cache | Static assets, sometimes full HTML pages, sometimes API responses | CloudFront, Cloudflare, Fastly |
| Application-level cache | Computed results, database query results, session data | Redis, Memcached |
| Database-level cache | Query plan cache, buffer cache | Built into the database engine itself |

Each layer has a different invalidation difficulty and a different blast radius when wrong — design invalidation strategy per layer explicitly, don't assume one strategy covers all of them.

## Caching Strategies — Decision Table

| Strategy | How it works | Best for | Risk |
|---|---|---|---|
| Cache-aside (lazy loading) | App checks cache first; on miss, reads from DB and populates cache | Most general-purpose read-heavy workloads — simplest, most common default | Cache stampede on a popular key's expiry under high concurrency (mitigate with request coalescing/locking) |
| Write-through | Every write updates the cache and the DB synchronously | Data that must never be stale on read, but reads are frequent enough to justify the write overhead | Slightly higher write latency; cache and DB must be kept in lockstep |
| Write-behind (write-back) | Writes go to the cache first, asynchronously flushed to the DB | Very high write throughput where some durability risk is acceptable | Risk of data loss if the cache fails before flushing to durable storage |
| Read-through | Cache itself is responsible for loading from the DB on a miss (often via a caching library/proxy) | Similar to cache-aside, with the loading logic centralized in the cache layer rather than the application | Less common in typical application code; more common in dedicated caching infrastructure |

**Decision rule:** Cache-aside is the right default for the overwhelming majority of application caching needs. Reach for write-through/write-behind only when there's a specific, measured need that cache-aside doesn't satisfy.

## Invalidation — The Genuinely Hard Part

"There are only two hard things in computer science: cache invalidation and naming things" exists as a cliché because it's true. Concrete strategies:

- **TTL-based expiry** — simplest, accept some staleness window by design. Right for data where slightly-stale is acceptable (e.g., a product listing that updates every few minutes is fine cached for 60 seconds).
- **Explicit invalidation on write** — when a record changes, explicitly delete/update its cache entry. More precise, more code to maintain and more places it can be missed (a write path that forgets to invalidate is a recurring, hard-to-spot bug class).
- **Versioned/keyed cache entries** — include a version or last-modified timestamp in the cache key itself, so a new write naturally produces a cache miss without needing explicit deletion. Reduces invalidation-bug risk at the cost of slightly more key-management complexity.

## Cache Stampede Protection

When a popular cache key expires, many concurrent requests can simultaneously miss and hammer the database at once. Mitigations: request coalescing (only one request actually queries the DB, others wait for that result), staggered/jittered TTLs (avoid many keys expiring at the exact same moment), or a background refresh that updates the cache before expiry rather than on-demand after.

## What NOT to Cache

- Data that changes on every read anyway (no benefit).
- Highly personalized, low-reuse data where the cache hit rate would be too low to justify the complexity (e.g., a one-off computed result nobody else will request).
- Anything where staleness has serious consequences (e.g., real-time account balance in a financial system) without an extremely tight, deliberately-chosen TTL and explicit invalidation discipline.

## Decision Rule for This Domain

Add caching when there's a measured read-latency or database-load problem, not preemptively "because it'll be faster." Once added, the invalidation strategy is the actual design decision — picking a caching technology (Redis vs. Memcached, almost always Redis given its richer feature set) is the easy part.

## Common Mistakes

- Caching without a clear invalidation strategy, leading to stale-data bugs that are hard to reproduce and debug.
- No cache stampede protection on high-traffic keys, causing thundering-herd database load spikes on expiry.
- Caching data that changes too frequently for the cache to provide real benefit, adding complexity for negligible hit rate.
