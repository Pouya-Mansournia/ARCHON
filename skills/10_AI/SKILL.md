---
name: ai-ml-architecture
description: AI/ML product architecture — LLM integration patterns, RAG, MLOps and model lifecycle, and AI product safety/evaluation — with decision rules for when to use a managed API vs. fine-tune vs. train from scratch.
---

# 10 — AI & Machine Learning Architecture (L4)

**Level:** L4 — Principal Engineering, with L2-level implementation detail in the reference files.

## Goal

Apply AI/ML capability where it solves a real, validated user problem better than a simpler deterministic approach would — and build the surrounding system (data pipeline, evaluation, monitoring, fallback behavior) with the same engineering rigor as any other production system, since "it's AI" is not an excuse to skip testing, monitoring, or graceful degradation.

## Build vs. Buy vs. Fine-Tune Decision Matrix

| Approach | Use when | Avoid when |
|---|---|---|
| Managed LLM API (OpenAI, Anthropic, Google) | Default starting point for almost every AI feature — fastest to validate, no training infrastructure, continuously improving underlying models | Strict data-residency requirements prohibit sending data to a third party, or per-call cost at scale exceeds self-hosting cost (rare until very high volume) |
| RAG over a managed LLM | Need the model to reason over private/proprietary/current data it wasn't trained on | The knowledge need is small/static enough to fit in a well-crafted prompt directly (skip RAG's retrieval infrastructure for trivial cases) |
| Fine-tuning a base model | A narrow, well-defined task with enough labeled examples, where prompt engineering alone hasn't reached acceptable quality/consistency | Task and quality bar can be met with prompting + RAG — fine-tuning adds real ongoing maintenance (retraining as needs evolve, version management) |
| Training a model from scratch | Effectively never justified for a typical product team — reserved for organizations with a genuinely novel problem, deep ML research capacity, and a clear reason existing foundation models can't be adapted | The default answer for nearly every product-building context — this is the most over-engineered AI choice a team can make |

## Decision Rule

Start with a managed LLM API and prompt engineering. Add RAG only once there's a real need to ground responses in private/current data. Reach for fine-tuning only after prompting + RAG has been tried and measured against a real evaluation set and found insufficient. Training from scratch should almost never be the answer for a product team — treat it the same way Kubernetes-for-an-MVP is treated in `skills/00_Core/reference/over-under-engineering.md`.

## Reference Files

- `reference/llm-integration-rag.md` — LLM API integration patterns, prompt engineering practices, and RAG architecture in depth.
- `reference/mlops-model-lifecycle.md` — model versioning, deployment, monitoring, and retraining triggers.
- `reference/ai-product-safety.md` — evaluation, hallucination mitigation, guardrails, and responsible-AI product practices.
