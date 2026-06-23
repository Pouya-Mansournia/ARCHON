# MLOps & Model Lifecycle

## Goal

A model in production is a living dependency, not a one-time artifact — its behavior can drift as real-world data changes, its provider can update the underlying model, and its outputs need the same monitoring rigor as any other critical system component.

## Model Lifecycle Stages

| Stage | What happens | Key risk if skipped |
|---|---|---|
| Data collection & preparation | Sourcing, cleaning, and labeling training/evaluation data | Garbage-in-garbage-out — the most common root cause of poor model quality |
| Training / fine-tuning (if applicable) | Producing or adapting a model on the prepared data | N/A for managed-API-only approaches |
| Evaluation | Measuring model quality against a held-out test set and real-world-representative scenarios | Shipping a model/prompt that looks good on a handful of manual examples but fails broadly |
| Deployment | Releasing the model/prompt version into production | No versioning means no ability to roll back when a new version regresses |
| Monitoring | Tracking output quality, latency, cost, and drift in production | Silent quality degradation goes unnoticed until users complain |
| Retraining / re-prompting | Updating the model/prompt based on monitored performance and new data | Model quality decays as real-world data distribution shifts away from what was evaluated |

## Versioning Discipline

Every prompt, fine-tuned model, and RAG pipeline configuration should be versioned explicitly (a prompt template version number, a model checkpoint ID) and tied to the evaluation results that justified shipping it. This makes "which version is in production" and "what changed between version N and N+1" answerable questions rather than archaeology.

## Drift Detection

| Drift type | What it means | How to detect |
|---|---|---|
| Data drift | Input data distribution shifts from what the model/prompt was evaluated against | Monitor input feature/query distributions over time, alert on significant shifts |
| Concept drift | The relationship between inputs and correct outputs changes (e.g., user intent patterns evolve) | Track output quality metrics (user feedback, downstream task success) over time, not just at launch |
| Model drift (third-party) | A managed API provider updates the underlying model, changing behavior without an explicit version bump | Maintain a regression evaluation suite run periodically against the live API, not just at initial integration |

## Retraining / Re-Evaluation Triggers

Don't retrain or re-prompt on a fixed calendar schedule by default — trigger off evidence: a measured quality metric drop, a meaningful shift in input data characteristics, user feedback signals indicating systematic failure patterns, or a known upstream model update from the provider.

## Common Mistakes

- No evaluation set at all — relying on developer intuition ("this looks good") instead of a representative, versioned test set with measurable quality metrics.
- No regression testing when a managed API provider silently updates their model, causing unexplained quality changes in production.
- Treating a prompt change the same as a typo fix — shipping it without re-running evaluation because "it's just a prompt."
- No production monitoring of AI feature output quality, cost, and latency — discovering problems only through user complaints.

## Decision Rule for This Domain

Every AI feature needs a versioned evaluation set before it ships, and ongoing production monitoring after it ships. Treat "the model provider changed something" as an expected operational event to monitor for, not an edge case to be surprised by.
