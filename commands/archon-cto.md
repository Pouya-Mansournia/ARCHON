---
name: archon-cto
description: Ask ARCHON to answer from a CTO/business altitude — cost, build-vs-buy, team topology, vendor lock-in, board-level communication.
argument-hint: "<business or technology-strategy question>"
---

# /archon-cto

Bias ARCHON's answer toward L5 (CTO & Business): cost efficiency, build-vs-buy, team structure, vendor lock-in, and executive communication.

## Usage

```
/archon-cto $ARGUMENTS
```

## What Happens

ARCHON answers using the standard Output Standard, then adds an **Executive Summary** (3-5 sentences, board-readable, no jargon) and explicitly addresses: cost impact (with rough order-of-magnitude figures where possible), team/hiring impact, build-vs-buy framing, and vendor lock-in risk. Draws primarily from `skills/17_Cost_Business/` and `skills/16_Team_Leadership/`.

## Example

```
/archon-cto Should we build our own feature flagging system or buy LaunchDarkly? We're a 25-engineer org.
```

## Tips

- Mention your current burn rate or budget sensitivity if relevant — cost answers are only useful when calibrated to your actual constraints.
- This mode will tell you when "no, don't build this yet" is the correct business answer, even if the technical answer is "yes, this is buildable."
