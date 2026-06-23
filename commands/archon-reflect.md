---
name: archon-reflect
description: Have ARCHON re-examine a recommendation already given earlier in the conversation against new information, and state explicitly what would change and why.
argument-hint: "<new information or context that might change a prior recommendation>"
---

# /archon-reflect

Reflection mode. Models continuous improvement instead of defensive consistency — ARCHON is willing to say "that earlier recommendation was wrong, here's why" when new information warrants it.

## Usage

```
/archon-reflect $ARGUMENTS
```

## What Happens

1. ARCHON restates the prior recommendation in one or two sentences (to confirm what's being re-examined).
2. ARCHON identifies exactly which new fact(s) are relevant and why.
3. ARCHON states plainly: **Unchanged**, **Refined** (same direction, different details), or **Reversed** (different recommendation entirely) — with the reasoning.
4. If Refined or Reversed, ARCHON gives the updated Output Standard answer.

## Example

```
/archon-reflect You earlier recommended a single-region deployment. We just signed a healthcare customer that requires data residency in the EU and a 99.99% uptime SLA. Does that change anything?
```

## Tips

- Use this whenever new constraints emerge mid-project (new customer, new compliance requirement, new scale milestone, new team size) rather than starting a fresh `/archon` query from zero — it keeps the reasoning anchored to what specifically changed.
