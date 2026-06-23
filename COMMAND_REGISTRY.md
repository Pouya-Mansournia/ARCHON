# Command Registry

All 8 ARCHON slash commands, their purpose, and which level(s)/skill domains they primarily draw on.

| Command | Mode | Primary use | Key domains drawn on |
|---|---|---|---|
| `/archon` | Default advisory | General-purpose engineering/product advisory question | All — routes via `skills/99_Decision_Engine/` |
| `/archon-cto` | CTO mode | Business-facing technical strategy, cost, team, build-vs-buy | `skills/16_Team_Leadership/`, `skills/17_Cost_Business/`, `skills/02_Product/` |
| `/archon-principal` | Principal Engineer / ADR mode | A concrete architecture decision, output in the full 10-part Output Standard | `skills/07_Architecture/`, `skills/99_Decision_Engine/reference/output-standard-and-confidence.md`, plus the relevant domain(s) |
| `/archon-robotics` | Robotics mode | Robotics/embedded/real-time systems questions | `skills/11_Robotics/` |
| `/archon-ai` | AI mode | AI/ML/LLM product and architecture questions | `skills/10_AI/` |
| `/archon-review` | Review/critic mode | Critique an existing system, PR, or proposal | `skills/19_Review_Outputs/`, `skills/00_Core/reference/over-under-engineering.md` |
| `/archon-plan` | Planner mode | Phased MVP/Growth/Scale planning | `skills/02_Product/reference/product-engineering-mvp-pmf.md`, cross-domain |
| `/archon-reflect` | Reflection mode | Revisit a past decision — Unchanged/Refined/Reversed | `skills/19_Review_Outputs/reference/adr-decision-log-templates.md` |

## Files

Each command is defined in `commands/<name>.md` with frontmatter (`name`, `description`, `argument-hint`) and a consistent body structure (Usage / What Happens / Example / Tips or Output).

| File | Command |
|---|---|
| `commands/archon.md` | `/archon` |
| `commands/archon-cto.md` | `/archon-cto` |
| `commands/archon-principal.md` | `/archon-principal` |
| `commands/archon-robotics.md` | `/archon-robotics` |
| `commands/archon-ai.md` | `/archon-ai` |
| `commands/archon-review.md` | `/archon-review` |
| `commands/archon-plan.md` | `/archon-plan` |
| `commands/archon-reflect.md` | `/archon-reflect` |

## Choosing a Command

When more than one command seems applicable, prefer the most specific mode (e.g., `/archon-robotics` over `/archon` for a robotics question) — the specific modes carry sharper framing for their domain. Default to `/archon` when the question is genuinely general or spans multiple domains without an obvious specialist lens.

## Adding a New Command

New commands should represent a genuinely distinct interaction mode (a different output shape or framing), not just a new topic — new topics belong in `skills/` and are automatically available to every existing command. See `CONTRIBUTING.md`.
