# Core Principles — Full Reference

These eight principles are the philosophical foundation underneath every recommendation ARCHON produces. They are not platitudes — each one has a concrete failure mode it prevents.

## 1. Simplicity First

**Rule:** The simplest design that satisfies real, current requirements wins by default. Complexity must be earned by a demonstrated, current need — never by an anticipated future one.

**Why it matters:** Every additional moving part (a new service, a new datastore, a new queue, a new language) multiplies operational surface area: more failure modes, more things to monitor, more things a new hire has to learn, more places a bug can hide.

**Violating it looks like:** Choosing microservices for a 3-person team's first product because "that's how big companies do it." Adding Kafka for a feature that processes 200 events/day. Splitting a monolith into 12 services before there's a single paying customer.

**Satisfying it looks like:** Starting with a modular monolith and a single Postgres database, with clear internal module boundaries that *could* become service boundaries later if and when a real scaling or team-ownership need shows up.

**Test before adding complexity:** "What specific problem, that we have today, does this solve? If we cut it, what actually breaks right now?" If the answer is "nothing breaks today, but it might help later," the answer is: not yet.

## 2. MVP Before Scale

**Rule:** Build for the load you actually have, plus a reasonable safety margin (commonly 3-10x) — not the load you might have if everything goes perfectly.

**Why it matters:** Scaling problems are good problems — they mean the product is succeeding. Most products never reach the scale that justifies the complexity teams pre-build for. Premature scale work is a direct tax on time-to-market, paid whether or not the scale ever arrives.

**Violating it looks like:** Designing a globally-distributed, multi-region active-active database architecture for a product with zero users, "in case we go viral."

**Satisfying it looks like:** Single-region deployment with a documented, known path to multi-region (read replicas → multi-region read replicas → active-active) that you execute only when you have the specific metric (latency complaints from a specific geography, a specific compliance requirement) that justifies it.

**Test:** "What is our actual current or near-term (next 2 quarters) load? Does this design comfortably handle that plus 5x?" If yes, stop there.

## 3. Trade-Off Thinking

**Rule:** Every architectural choice trades something for something else. State both sides explicitly, every time — there is no free option.

**Why it matters:** Decisions presented as having no downside are either incompletely analyzed or being sold, not engineered. Naming the cost up front is what lets a team make an informed bet instead of discovering the cost later, under pressure.

**Examples of trade-offs that are easy to forget to state:**
- Managed services (lower ops burden) vs. self-hosted (lower cost at scale, more control) — the trade-off is operational burden vs. unit economics at scale.
- Strong consistency (simpler reasoning) vs. eventual consistency (better availability/partition tolerance) — the trade-off is developer cognitive load vs. system resilience.
- Monorepo (simpler dependency management, atomic cross-cutting changes) vs. polyrepo (clearer ownership boundaries, independent deploy cadence) — the trade-off is coordination overhead vs. autonomy.

**Test:** "If I had to argue against my own recommendation, what would I say?" If you can't generate a real counter-argument, you haven't finished the analysis.

## 4. Hiring Reality

**Rule:** A technology you cannot staff is a technology you cannot operate — no matter how technically superior it is on paper.

**Why it matters:** Architecture decisions are also staffing decisions. Choosing Erlang, Haskell, or a niche distributed database because it's technically elegant, when your hiring pool and team's existing skill set is Python/JS/Postgres, creates a long-term key-person dependency risk and slows every future hire's ramp-up.

**Violating it looks like:** A 5-person startup choosing a bleeding-edge, low-adoption framework because the founding engineer likes it, with no plan for what happens when that engineer leaves.

**Satisfying it looks like:** Defaulting to technologies with deep, liquid hiring markets (mainstream languages, Postgres, mainstream cloud providers) unless there's a specific, named capability gap that only the niche technology closes — and even then, budgeting explicitly for the training/hiring cost.

**Test:** "If our most senior person on this technology left tomorrow, how long would it take to backfill that expertise?"

## 5. Operational Reality

**Rule:** If your team cannot run it during a 3am incident, it is not production-ready — regardless of how good it looks in a design doc or a demo.

**Why it matters:** Most architecture failures are operational failures, not design failures: nobody knew how to roll back, nobody had alerting on the right signal, nobody had run a failover drill, the runbook didn't exist or was stale.

**Violating it looks like:** Shipping a Kubernetes cluster with no one on the team who has operated Kubernetes in production before, no documented runbooks, and no on-call rotation that has practiced an incident.

**Satisfying it looks like:** Every production system has: an owner, a runbook, basic alerting tied to user-facing symptoms (not just infrastructure metrics), and at least one person other than the original author who could operate it under pressure.

**Test:** "Could the on-call engineer who didn't build this system diagnose and mitigate a failure in it at 3am, using only what's documented?"

## 6. Cost Awareness

**Rule:** Cost is an architecture input from day one, not a line item to optimize after launch.

**Why it matters:** Architectural decisions made without cost modeling routinely produce 5-10x cost surprises at scale (e.g., chatty cross-AZ traffic, unindexed full-table scans run per-request, over-provisioned managed services, egress fees from a multi-cloud design that wasn't actually required).

**Violating it looks like:** Choosing a serverless-everything architecture for a steady, predictable, high-volume workload without comparing it against reserved-capacity costs — serverless's per-invocation premium can be 3-5x more expensive than reserved compute at sustained high volume.

**Satisfying it looks like:** Every non-trivial recommendation includes a rough cost-impact estimate and names the cost driver (compute, storage, egress, per-seat licensing, managed-service markup) so the team can sanity-check it against budget.

**Test:** "What does this cost at our current scale, and what does it cost at 10x? Is the cost curve linear, sub-linear, or super-linear?"

## 7. Security by Default

**Rule:** Security controls are part of the initial design, not a hardening pass scheduled "before launch" or "after we get traction."

**Why it matters:** Security retrofitted after the fact is dramatically more expensive and more likely to be incomplete than security designed in from the start — auth, input validation, secrets management, and least-privilege access patterns are foundational, not additive.

**Violating it looks like:** "We'll add proper auth once we have users" — which usually means real user data sits behind a half-finished auth system at the exact moment it starts mattering.

**Satisfying it looks like:** Every MVP ships with: managed authentication (don't roll your own unless there's a specific reason), secrets in a secrets manager (never in code or plaintext env files committed to git), input validation at every trust boundary, and least-privilege IAM from the first deploy.

**Test:** "If this system were breached tomorrow, what's the blast radius, and would we even know it happened?"

## 8. Evolutionary Architecture

**Rule:** Design for the next stage of growth, not the final imagined stage. Architecture should be a sequence of deliberate, justified transitions — not a single upfront bet on where the company will be in five years.

**Why it matters:** Nobody can correctly predict a product's scale trajectory, usage patterns, or org structure five years out. Betting the whole architecture on that prediction is a bet against your own future flexibility — which is precisely the opposite of what "ambitious" architecture should buy you.

**Violating it looks like:** Designing a 50-microservice architecture upfront because "we'll eventually need to scale teams independently," when the company currently has 6 engineers who all need to move fast across the whole codebase.

**Satisfying it looks like:** A modular monolith with clean internal seams that map to likely future service boundaries, so that splitting out a service later (when a team or scale need actually appears) is a mechanical extraction, not a rewrite.

**Test:** "If our assumptions about scale or team size turn out wrong in either direction, how expensive is it to course-correct from here?"

## How These Principles Interact With the Engineering Decision Principles Priority Order

When two of these principles pull in opposite directions on a specific decision, defer to the priority order in `skills/99_Decision_Engine/SKILL.md` (Simplicity → Maintainability → Reliability → Dev Speed → Cost → Security → Scalability → Performance → Future Flexibility → Technical Elegance) — but always state explicitly which principle you're prioritizing and why, so the trade-off is visible rather than implicit.
