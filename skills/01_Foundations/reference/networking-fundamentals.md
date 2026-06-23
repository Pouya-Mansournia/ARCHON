# Networking Fundamentals

## Goal

Most "the API is slow" or "intermittent connection errors" incidents are networking problems wearing application-layer clothing. A solid mental model of TCP/IP, DNS, and TLS resolves them faster and prevents a category of architecture mistakes (e.g., not understanding why a load balancer health check is failing).

## TCP/IP Basics

- TCP gives you reliable, ordered, connection-oriented delivery at the cost of a handshake (3-way handshake: SYN, SYN-ACK, ACK) and head-of-line blocking. UDP gives you no reliability/ordering guarantees but lower latency and no handshake — used where occasional loss is acceptable or handled at the application layer (real-time media, some game networking, QUIC/HTTP3's transport).
- A TCP connection is identified by the 4-tuple (source IP, source port, destination IP, destination port). Port exhaustion (running out of available ephemeral ports for outbound connections) is a real, recurring production issue under high connection-churn workloads — connection pooling and keep-alive exist specifically to avoid it.
- TCP backlog and `SYN` queue limits matter at high connection rates — a server that looks "slow" under load is sometimes actually dropping/queuing new connections at the kernel level before the application ever sees them.

## DNS

- DNS resolution order: browser/OS cache → resolver cache (often your router or ISP, or a configured resolver like 1.1.1.1/8.8.8.8) → recursive lookup through root → TLD → authoritative nameservers.
- TTL controls cache duration — lowering TTL before a planned cutover (e.g., DNS-based failover or migration) is a standard, necessary step, and forgetting to do it in advance is a common cause of "why didn't the failover work immediately" incidents (clients are still using cached, stale records).
- Common record types: `A`/`AAAA` (IPv4/IPv6 address), `CNAME` (alias to another name), `MX` (mail), `TXT` (verification, SPF/DKIM), `NS` (delegation). `ALIAS`/`ANAME` records (provider-specific, e.g., Route 53/Cloudflare) solve the "CNAME at the zone apex isn't allowed" problem.
- DNS-based load balancing/failover is real but has real limits: client-side caching and ISP-level resolver caching mean failover is never instant — for a hard requirement of sub-second failover, you need a layer below DNS (anycast, or an active load balancer health check), not DNS alone.

## TLS/SSL

- TLS handshake (simplified): client and server agree on a cipher suite, server presents a certificate chain, key exchange happens (commonly ECDHE for forward secrecy), session keys are derived. TLS 1.3 reduced this to effectively one round trip; TLS 1.2 needs two.
- Certificate chain validation: leaf cert → intermediate(s) → root CA, the client must be able to build a path to a trusted root. The most common TLS production incident is an expired certificate or a missing intermediate cert in the chain (works in browsers that cache intermediates, fails in strict clients/curl).
- Let's Encrypt (free, automatable via ACME protocol, 90-day certs meant to be auto-renewed) is the default choice for most workloads. Use a commercial CA only for specific needs (extended validation, certain compliance/contractual requirements, or very long-lived embedded-device certs where ACME's renewal cadence is impractical).
- TLS termination point matters architecturally: terminate at the load balancer/CDN (simpler cert management, but traffic is unencrypted hop-to-hop internally — acceptable inside a private VPC, NOT acceptable for compliance regimes requiring end-to-end encryption) vs. terminate at each service (more cert management overhead, full encryption in transit).

## Load Balancing Concepts

- Layer 4 (TCP/UDP, routes by IP/port, doesn't see HTTP) vs. Layer 7 (HTTP-aware, can route by path/header/cookie, terminate TLS, do content-based routing). L7 is right for almost all web/API traffic; L4 is right for non-HTTP protocols or when you need the absolute lowest latency passthrough.
- Health checks are the mechanism that makes load balancing actually safe — an LB without a correct health check will happily keep routing traffic to a dead instance. The health check endpoint should verify real dependency health (can it reach its database?), not just "process is running," but should NOT be so strict that a transient blip takes the instance out of rotation and triggers cascading failure.
- Load balancing algorithms: round-robin (simple, even distribution, ignores instance load), least-connections (better under uneven request cost), consistent hashing (needed when you want session affinity / cache locality without sticky sessions).

## Firewalls & Network Segmentation

- Security groups (AWS)/NSGs (Azure)/firewall rules (GCP) implement stateful, instance/subnet-level filtering — this is your first line of network-level least-privilege: only open the ports that need to be open, only between the specific sources that need access.
- Private subnets (no direct route to the internet) for databases and internal services, public subnets only for load balancers/bastion hosts/NAT gateways, is the standard, correct default topology — don't put a database in a public subnet "because it was easier to set up."
- A NAT gateway gives private-subnet resources outbound internet access (for package updates, third-party API calls) without exposing them to inbound traffic — standard, necessary cost line item, not optional in most cloud VPC designs.

## Common Ports Reference

| Port | Protocol/Use |
|---|---|
| 22 | SSH |
| 80 / 443 | HTTP / HTTPS |
| 53 | DNS |
| 5432 | PostgreSQL |
| 3306 | MySQL |
| 6379 | Redis |
| 27017 | MongoDB |
| 5672 | RabbitMQ (AMQP) |
| 9092 | Kafka |

## Decision Rule

When debugging "intermittent connectivity" or "slow" issues, check in this order before assuming an application bug: DNS resolution time → TCP connection establishment time → TLS handshake time → time-to-first-byte → application processing time. Each layer is independently measurable (via `curl -w`, or distributed tracing spans) — don't guess which layer is slow when you can measure it directly.
