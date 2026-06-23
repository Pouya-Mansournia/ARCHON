# AI Product Safety, Evaluation & Guardrails

## Goal

Shipping an AI feature without an evaluation and safety plan is the AI-era equivalent of shipping a payment feature without testing the failure paths — the consequences are just as real, even though the failure mode (a wrong or harmful generated answer) looks different from a traditional bug.

## Evaluation Before Shipping

| Evaluation type | What it measures | Example |
|---|---|---|
| Accuracy / task success | Does the output correctly solve the intended task | Did the RAG answer correctly reflect the source documents |
| Groundedness | Is the output actually supported by retrieved/provided context, or fabricated | Hallucination rate against a labeled test set |
| Safety / harm | Does the output avoid harmful, biased, or inappropriate content | Red-team test set of adversarial prompts |
| Latency & cost | Is the feature fast and affordable enough at expected volume | p95 latency and per-request cost under realistic load |

Build a representative evaluation set (real or realistic example inputs, with expected/acceptable outputs or grading criteria) before launch, and re-run it on every meaningful prompt/model/pipeline change.

## Hallucination Mitigation

- Ground responses in retrieved/provided source material (RAG) rather than relying on the model's parametric knowledge for facts that matter.
- Require/encourage citation of sources in the output, both for user trust and as a built-in self-check mechanism.
- For high-stakes outputs, add a verification step (a second model call or deterministic check) that validates the answer against the source before returning it to the user.
- Communicate confidence/uncertainty to the user rather than presenting every generated answer with identical authority.

## Prompt Injection & Adversarial Input

Treat any user-controllable text that flows into a prompt as untrusted input, the same way user input into a SQL query is treated as untrusted (see `skills/12_Security/`). Mitigations: clearly delineate system instructions from user content (structurally, not just with a label the model might be tricked into ignoring), constrain what actions a model's output can trigger (especially for function-calling/agentic systems — never let model output directly execute unreviewed destructive actions), and monitor for anomalous output patterns that suggest a successful injection.

## Guardrails for Agentic / Tool-Using Systems

When an LLM's output can trigger real actions (calling APIs, modifying data, sending messages), apply the same caution as any automated system with side effects: scope the available actions to the minimum needed (least privilege, same principle as IAM), require human confirmation for irreversible/high-impact actions, and log every action taken so behavior is auditable after the fact.

## Responsible AI Product Practices

- Be transparent with users that they're interacting with an AI system where that matters for trust/expectations.
- Provide a clear escalation/fallback path to a human or deterministic process when the AI system is uncertain or the stakes are high (financial decisions, medical-adjacent content, safety-critical contexts).
- Consider bias and fairness in training/evaluation data, particularly for any feature making decisions that affect people (hiring, lending, access) — this is both an ethical and, increasingly, a regulatory consideration.

## Common Mistakes

- Shipping a customer-facing AI feature with no hallucination mitigation, then discovering fabricated answers in production via user complaints.
- Allowing an agentic system to take irreversible actions (sending an email, deleting data) directly from model output with no confirmation step or audit log.
- No red-teaming/adversarial testing before launch for a feature processing untrusted user input.
- Presenting AI-generated content with the same unconditional authority as verified deterministic output, misleading users about its reliability.

## Decision Rule for This Domain

Every AI feature that's user-facing or has side effects needs: a pre-launch evaluation set covering accuracy and safety, explicit handling of untrusted input flowing into prompts, and guardrails proportional to the stakes of what the system can do. The higher the stakes (financial, medical, irreversible actions), the more conservative the guardrails and the more human-in-the-loop checkpoints belong in the flow.
