# Memory: Persisting ARCHON's Decisions Across Sessions

ARCHON itself is stateless between invocations — each `/archon*` call reasons from the skill library and the conversation it's given, with no built-in long-term memory of past sessions. For decisions worth remembering, the recommended pattern is to make ARCHON's output part of your own project's durable record, not to rely on ARCHON to recall a past conversation.

## The Recommended Pattern

1. **Capture significant decisions as ADRs.** When `/archon-principal` (or any mode) produces a recommendation worth outliving the conversation, save it using the template in `skills/19_Review_Outputs/reference/adr-decision-log-templates.md`, in your own project's `docs/adr/` (or wherever your project keeps decision records).
2. **Feed past ADRs back in when relevant.** When asking a related question later, paste or reference the prior ADR in your prompt. ARCHON reasons over whatever context it's given in the conversation — it doesn't need a special memory mechanism, it needs the prior decision in front of it.
3. **Use `/archon-reflect` to revisit a decision deliberately.** This mode is specifically structured to take a past decision (which you provide) and produce an explicit Unchanged / Refined / Reversed verdict with reasoning — see `commands/archon-reflect.md` and `skills/19_Review_Outputs/reference/adr-decision-log-templates.md`.

## Why ARCHON Doesn't Ship Its Own Memory Store

A custom memory/persistence layer for a single plugin would duplicate what your project's own documentation and version control already do better — an ADR committed to your repository is durable, diffable, and reviewable in a PR, which a plugin-internal memory store would not be by default. This follows the same Simplicity-First principle ARCHON applies to every other recommendation (`skills/00_Core/reference/core-principles.md`): don't build infrastructure a simpler, already-existing mechanism handles well.

## If You're Using ARCHON Across Many Related Decisions

For a project with a growing set of ARCHON-assisted decisions, keep a single running `DECISIONS.md` (or a `docs/adr/` directory with one file per decision) in that project — not in this repository — and reference the relevant prior entries in future prompts. This repository's own `ARCHITECTURE_DECISIONS.md` is an example of exactly this pattern, applied to ARCHON's own design.
