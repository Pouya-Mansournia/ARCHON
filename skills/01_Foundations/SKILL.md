---
name: foundations
description: L1 foundational engineering knowledge — Linux systems administration, networking fundamentals, Nginx/web server configuration, and Git/version control. Load for junior-engineer-level questions or fast, precise refreshers on building-block technology.
---

# 01 — Foundations (L1)

**Level:** L1 — Foundations. Audience: junior engineers, or any engineer needing a precise refresher on building blocks everything else is built on.

## Goal

Make sure the fundamentals underneath every higher-level architecture decision are solid: how Linux actually behaves, how networking actually routes traffic, how a reverse proxy actually works, and how Git actually models history. Weak L1 foundations are the most common hidden cause of "mysterious" production incidents at every other level.

## Scope

| Topic | Covers |
|---|---|
| Linux Fundamentals | Processes, file permissions, systemd, package management, filesystems, shell tooling |
| Networking Fundamentals | TCP/IP, DNS, TLS/SSL, load balancing concepts, firewalls, common ports |
| Nginx & Web Servers | Reverse proxy configuration, load balancing, TLS termination, caching headers |
| Git & Version Control | Branching models, merge vs rebase, commit hygiene, monorepo vs polyrepo basics |

## Decision Rule

L1 questions rarely need a full Output Standard treatment — they usually need a precise, correct explanation plus a concrete example. Use the full Output Standard only when the L1 question is actually a disguised architecture decision (e.g., "should I use Nginx or a managed load balancer" — that's an L3 Cloud/DevOps question wearing an L1 costume; route accordingly).

## Reference Files

- `reference/linux-fundamentals.md`
- `reference/networking-fundamentals.md`
- `reference/nginx-web-servers.md`
- `reference/git-version-control.md`
