# LLM Integration & RAG Architecture

## Goal

Integrate large language models into a product the way any external dependency should be integrated: with explicit error handling, cost awareness, latency budgets, and a clear understanding of failure modes — not as a black box that "just works."

## LLM API Integration Patterns

| Pattern | Description | Use when |
|---|---|---|
| Direct synchronous call | Request blocks until the model responds | Simple, low-latency-tolerant features (short completions, classification) |
| Streaming response | Tokens streamed to the client as generated | User-facing chat/generation UX where perceived latency matters most |
| Async/queued generation | Request queued, result delivered later (webhook, polling, websocket push) | Long-running generation tasks (large documents, batch processing) where blocking a request thread isn't viable |
| Function calling / tool use | Model output triggers a structured function call back into application code | Agents that need to take actions (query a database, call an API) rather than just generate text |

## Prompt Engineering Practices

- **Be explicit about output format** — request structured output (JSON schema, XML tags) when the result needs to be parsed programmatically; don't parse free-form prose.
- **Few-shot examples** for tasks with a specific desired style/format the model doesn't reliably produce zero-shot.
- **Separate system instructions from user content** clearly, and never concatenate untrusted user input directly into instructions that control privileged behavior (this is the foundation of prompt-injection defense — see `reference/ai-product-safety.md`).
- **Version and test prompts like code** — a prompt change is a behavior change; treat it with the same review/testing rigor as a code change, not as a casual text edit.

## RAG (Retrieval-Augmented Generation) Architecture

| Component | Role |
|---|---|
| Document ingestion pipeline | Chunking, cleaning, and preparing source documents for embedding |
| Embedding model | Converts text chunks into vector representations |
| Vector store | Stores embeddings for similarity search (pgvector, Pinecone, Weaviate — see `skills/05_Database/SKILL.md`) |
| Retriever | Given a query, finds the most relevant chunks via vector similarity (and often hybrid keyword + vector search) |
| Generator (LLM) | Produces the final response grounded in the retrieved chunks |

### RAG Design Decisions That Actually Matter

- **Chunking strategy** — chunk size and overlap materially affect retrieval quality; too large dilutes relevance, too small loses context. Start with semantic-boundary chunking (paragraph/section) over fixed-character splitting.
- **Hybrid search** (combining vector similarity with traditional keyword search) often outperforms pure vector search, especially for queries containing specific terms/names/codes that embeddings can blur.
- **Re-ranking** retrieved chunks with a lighter-weight model before passing to the generator improves relevance when the initial retrieval set is noisy.
- **Source citation** — surfacing which retrieved chunks informed the answer both builds user trust and gives a debugging trail when the model gets something wrong.

## Common Mistakes

- Treating the LLM API as infallible — no timeout handling, no retry/backoff, no fallback behavior when the provider has an outage or returns an error.
- Concatenating raw user input into privileged system prompts, opening the door to prompt injection.
- Skipping evaluation entirely — shipping a prompt or RAG pipeline change based on a few manual spot-checks rather than a real evaluation set (see `reference/ai-product-safety.md`).
- Chunking documents naively (fixed character count with no regard for semantic boundaries), degrading retrieval quality silently.
- Not monitoring token usage/cost per feature, leading to surprise bills once usage scales (see `skills/17_Cost_Business/` for FinOps treatment of AI API costs).

## Decision Rule for This Domain

Treat the LLM provider as a critical external dependency: budget for latency, cost per call, and failure handling explicitly. Add RAG only once there's a real grounding need beyond what a well-crafted prompt provides, and treat chunking/retrieval quality as a first-class design decision, not an afterthought.
