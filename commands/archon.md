---
name: archon
description: Ask ARCHON any architecture, technology-selection, or system-design question. Default advisory mode spanning L1-L5.
argument-hint: "<product idea, system, or technical question>"
---

# /archon

Default entry point into ARCHON. Use for any architecture or technology decision question.

## Usage

```
/archon $ARGUMENTS
```

## What Happens

1. ARCHON identifies which seniority level(s) (L1-L5) and which skill domain(s) the question touches, using `SKILL_REGISTRY.md`.
2. ARCHON asks clarifying questions only if missing context would change the answer (scale, stage, team size, budget, compliance).
3. ARCHON loads the relevant `skills/<NN_Domain>/SKILL.md` and reference files.
4. ARCHON runs the Decision Engine (`skills/99_Decision_Engine/`) and the over/under-engineering check (`skills/00_Core/reference/over-under-engineering.md`).
5. ARCHON answers using the 10-part Output Standard: What to use, Why, Why not alternatives, Trade-offs, Risks, Cost impact, Scalability impact, Security impact, Confidence level, Migration path.

## Example

```
/archon We're a 4-person team building a B2B analytics SaaS. What should our initial stack and deployment look like?
```

## Tips

- State your team size, stage (pre-PMF / scaling / enterprise), and any hard constraints (compliance, budget, deadline) upfront — it sharpens the answer and avoids a round of clarifying questions.
- For a deep adversarial review of an existing design, use `/archon-review` instead.
- For converting an accepted decision into a phased build plan, use `/archon-plan`.
