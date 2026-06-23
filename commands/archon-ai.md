---
name: archon-ai
description: Ask ARCHON about AI/LLM product architecture — RAG, vector databases, AI agents, tool calling, MLOps, model routing, evaluation, guardrails.
argument-hint: "<AI or ML architecture question>"
---

# /archon-ai

Bias ARCHON's answer toward AI infrastructure and AI agent architecture.

## Usage

```
/archon-ai $ARGUMENTS
```

## What Happens

ARCHON loads `skills/10_AI/` (AI architecture, AI agent architecture, MLOps reference files) and answers using the standard Output Standard, with explicit attention to: model selection vs fine-tuning vs RAG trade-offs, vector database choice, latency/cost per request, evaluation strategy, guardrails/safety, and the operational reality of running AI features in production (drift, monitoring, fallback behavior).

## Example

```
/archon-ai Should we fine-tune a small model or build a RAG pipeline over our internal docs for a customer support assistant?
```

## Tips

- Mention your expected request volume and latency budget — this is usually the single biggest factor in AI architecture decisions.
- If building an agent (not a single-shot LLM call), specify what tools/actions it needs — this changes the safety and guardrail requirements significantly.
