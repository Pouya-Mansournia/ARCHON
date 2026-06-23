# Example Prompts

Quick-reference example prompts for each ARCHON command mode. For full worked transcripts with complete responses, see the `examples/` directory at the repository root.

## `/archon` — General Advisory

```
/archon We're a 4-person team building a B2B analytics tool. Postgres or MongoDB?
/archon What's the simplest way to add background job processing to a Node.js API?
/archon Do we need a CDN at 500 daily active users?
```

## `/archon-cto` — Business-Facing Technical Strategy

```
/archon-cto Should we build our own auth system or use a managed provider, given we have 2 backend engineers and a Series A deadline?
/archon-cto How should we structure our first 3 engineering hires?
/archon-cto Walk me through the cost trade-off between staying on Heroku vs. migrating to AWS.
```

## `/archon-principal` — Architecture Decision / ADR Output

```
/archon-principal Modular monolith vs. microservices for a 6-person team building a logistics platform.
/archon-principal Should our event pipeline use Kafka or a simpler queue like SQS?
/archon-principal We need multi-tenancy — shared schema, schema-per-tenant, or database-per-tenant?
```

## `/archon-robotics` — Robotics / Embedded / Real-Time

```
/archon-robotics ROS 2 or bare embedded for a single-arm pick-and-place prototype?
/archon-robotics How should we architect the safety supervisor for an AMR fleet?
/archon-robotics What RTOS should we use for a battery-powered sensor node?
```

## `/archon-ai` — AI/ML Product & Architecture

```
/archon-ai Should we fine-tune a model or build RAG over our existing docs?
/archon-ai How do we guard against prompt injection in a customer-facing support agent?
/archon-ai What does a sane evaluation pipeline look like before we ship an LLM feature?
```

## `/archon-review` — Critique an Existing Design

```
/archon-review Here's our current checkout flow architecture: [description]. What's wrong with it?
/archon-review Review this PR for security and reliability gaps: [diff or link]
```

## `/archon-plan` — Phased MVP/Growth/Scale Planning

```
/archon-plan We're pre-PMF with a B2B SaaS idea. What should our architecture look like for the first 6 months?
/archon-plan We just hit product-market fit — what infrastructure investment is now justified that wasn't before?
```

## `/archon-reflect` — Revisit a Past Decision

```
/archon-reflect We chose MongoDB 18 months ago for flexibility. We now have 40 tables of relational data bolted on. Was that the right call, and what should we do now?
```

See `docs/QUICKSTART.md` for a guided first session and `COMMAND_REGISTRY.md` for the full command reference.
