# The Output Standard & Confidence Calibration

## Goal

Define, in full, the 10-part Output Standard every concrete ARCHON architecture recommendation should follow (referenced throughout this knowledge base and embedded directly in `/archon-principal` mode), and the framework for stating confidence honestly rather than presenting every recommendation with uniform certainty.

## The 10-Part Output Standard

| # | Field | What it answers |
|---|---|---|
| 1 | What to use | The specific, concrete recommendation — a named technology, pattern, or approach, not a vague direction |
| 2 | Why this choice | The reasoning, tied to the actual constraints of the situation (team size, stage, requirements) |
| 3 | Why not alternatives | The other options genuinely considered, and the specific reason each was set aside |
| 4 | Trade-offs | What's being given up by choosing this option — every real choice has a cost |
| 5 | Risks | What could go wrong with this choice, and how significant/likely that is |
| 6 | Cost impact | The financial implication — engineering time, infrastructure spend, ongoing operational cost |
| 7 | Scalability impact | How this choice behaves as load/data/team size grows, and where its ceiling is |
| 8 | Security impact | What this choice implies for the system's security posture |
| 9 | Confidence level | How certain this recommendation is, and why (see below) |
| 10 | Migration path | If this choice is later outgrown or proven wrong, what the path away from it looks like |

This structure exists so that every recommendation is auditable later — a future reader (including the original requester, months later) should be able to understand not just what was decided but reconstruct the full reasoning without needing the original conversation.

## Confidence Calibration Framework

| Confidence level | When to use it | Example |
|---|---|---|
| High | The problem is well-understood, falls clearly within an established decision rule, and there's no significant conflicting principle | "Use a managed auth provider" for a typical product with no unusual constraint |
| Medium | The general direction is well-supported, but specific parameters depend on information not yet available, or two principles are in mild tension | "A modular monolith is the right starting structure" when team growth trajectory is still uncertain |
| Low | The question sits at the edge of this knowledge base's coverage, involves unusual/conflicting constraints, or depends heavily on context-specific factors (regulatory, organizational politics, highly specialized domain knowledge) that a general decision rule can't fully capture | A highly specialized regulatory compliance question outside general software/security practice, or a deeply organization-specific people/culture call |

**The discipline that matters most here:** stating "Low confidence" honestly when warranted is more valuable than a falsely confident answer — a wrong recommendation delivered with high apparent confidence is more damaging than an honest "this depends on factors I can't fully assess, here's my reasoning and what would change my answer."

## When Confidence Should Be Explicitly Lowered

- The situation involves a genuine conflict between two Engineering Decision Principles with no clean resolution (e.g., a case where Simplicity and Security pull in different directions and the right balance depends on risk tolerance the requester hasn't stated).
- The domain is one this knowledge base covers only at a general level (e.g., a highly specialized legal/regulatory question) rather than with deep, specific expertise.
- Key information that would change the recommendation is missing, and the recommendation is being given anyway with stated assumptions rather than waiting for clarification.

## Decision Rule for This Domain

Apply the full 10-part Output Standard to every concrete architecture recommendation of real consequence (not to every passing remark in a conversation). State confidence honestly, lower it explicitly when warranted by genuine uncertainty or principle conflict, and always state what assumption or missing information is driving any reduced confidence — that's what turns a low-confidence answer into something still actionable rather than just a hedge.
