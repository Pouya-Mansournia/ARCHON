# Nginx & Web Servers

## Goal

Nginx (or an equivalent reverse proxy / web server) sits in front of almost every production web application. Understanding it precisely prevents an entire class of "works locally, breaks in production" incidents related to headers, buffering, timeouts, and TLS.

## Core Roles Nginx Plays

1. **Reverse proxy** — forwards requests to upstream application servers, hiding internal topology.
2. **Load balancer** — distributes requests across multiple upstream instances.
3. **TLS termination** — handles HTTPS so application servers can speak plain HTTP internally.
4. **Static file serving** — serves static assets directly, far faster than routing them through an application server.
5. **Caching layer** — can cache upstream responses based on headers/rules, reducing load on application servers.
6. **Request buffering / rate limiting** — protects upstream services from slow clients and abusive traffic patterns.

## Minimal Reverse Proxy Config (Reference Shape)

```nginx
server {
    listen 443 ssl http2;
    server_name api.example.com;

    ssl_certificate     /etc/letsencrypt/live/api.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/api.example.com/privkey.pem;

    location / {
        proxy_pass http://app_upstream;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 60s;
    }
}

upstream app_upstream {
    least_conn;
    server 10.0.1.10:3000;
    server 10.0.1.11:3000;
}
```

## Headers That Cause Real Production Bugs When Missed

- `X-Forwarded-For` / `X-Real-IP` — without these, every request your application sees appears to originate from the proxy's IP, breaking rate limiting, geolocation, and audit logs that key on client IP.
- `X-Forwarded-Proto` — without this, an application behind a TLS-terminating proxy thinks every request is plain HTTP, which breaks "secure cookie" logic and any redirect-to-HTTPS logic (causing redirect loops).
- `Host` — must be forwarded correctly for virtual-hosted applications and for any application logic that constructs absolute URLs from the request.

## Timeouts — The Most Common Source of Mysterious 502/504s

- `proxy_connect_timeout`, `proxy_read_timeout`, `proxy_send_timeout` on the Nginx side must be coordinated with the application server's own timeout settings and with any load balancer in front of Nginx. A mismatch (e.g., Nginx times out before a legitimately slow-but-working backend request completes) produces 502/504 errors that look like backend failures but are actually proxy-layer timeout misconfiguration.
- Client-facing timeout budgets should be set deliberately end-to-end: decide the maximum acceptable user-facing latency, then make sure every hop in the chain (CDN → load balancer → Nginx → application → database) has a timeout shorter than the hop in front of it, so failures surface as a clean error rather than a hung connection.

## Buffering

- Nginx buffers responses from upstream by default before sending them to the client — good for slow clients (protects the application server from being tied up waiting on a slow network), bad for use cases needing real-time streaming (Server-Sent Events, chunked long-polling) where `proxy_buffering off;` is required on that specific location block.

## Caching

- `proxy_cache` with appropriate `Cache-Control`/`Expires` headers from upstream can meaningfully offload read-heavy endpoints without a separate caching layer for many small-to-medium applications. Know the difference between caching at Nginx (simple, single-node unless using a shared cache backend) vs. a CDN (distributed, global, but adds another layer to invalidate correctly) vs. an application-level cache like Redis (most control, most complexity).

## Nginx vs. Alternatives — Decision Table

| Tool | When it's the right choice |
|---|---|
| Nginx | Default choice for most self-managed reverse-proxy/LB needs — mature, fast, huge community, well-documented |
| Caddy | Want automatic HTTPS (built-in ACME) with simpler config syntax; good for smaller deployments valuing simplicity over Nginx's ecosystem depth |
| HAProxy | Pure load balancing at very high connection counts with fine-grained L4/L7 control; common in large-scale, performance-critical setups |
| Envoy | Service-mesh / microservices environments needing dynamic service discovery, advanced traffic shaping, and observability integration (see `skills/07_Architecture/reference/service-mesh.md`) |
| Cloud-managed LB (ALB/NLB, Cloud Load Balancing) | Default choice once you're already on a cloud provider and don't have a specific reason to self-manage — less operational burden, native integration with autoscaling and health checks |

## Decision Rule

Default to a cloud-managed load balancer in front of your application for most teams — it removes an entire category of operational burden (patching, scaling the proxy layer itself, TLS cert automation). Reach for self-managed Nginx specifically when you need configuration flexibility a managed LB doesn't expose (complex routing rules, specific caching behavior, on-prem/non-cloud deployment) or when running it as a sidecar/ingress controller inside Kubernetes.

## Common Mistakes

- Forgetting `proxy_set_header` directives, breaking client IP logging, secure cookies, and redirect logic.
- Timeout mismatches between proxy layers causing intermittent 502/504s that look like backend instability.
- Serving static assets through the application server instead of directly via Nginx/CDN, wasting application server capacity on work a proxy does far more efficiently.
- No rate limiting at the proxy layer, leaving the application fully exposed to traffic spikes and abuse.
