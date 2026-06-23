# Contributing to ARCHON

ARCHON is a knowledge-based Claude Code / Cowork plugin. Contributions are primarily content contributions (new reference material, corrections, better decision rules) rather than code.

## Ground Rules

1. **English only.** Every file in this repository — agent definitions, skills, commands, docs — must be written in English.
2. **Follow the Output Standard.** Any new or edited architecture guidance must follow the 10-part standard in `skills/99_Decision_Engine/SKILL.md` (What to use, Why, Why not alternatives, Trade-offs, Risks, Cost impact, Scalability impact, Security impact, Confidence level, Migration path).
3. **Optimize for engineering reality, not hype.** Follow the priority order in `skills/99_Decision_Engine/SKILL.md` (Simplicity → Maintainability → Reliability → Dev Speed → Cost → Security → Scalability → Performance → Future Flexibility → Technical Elegance).
4. **Don't create a top-level `modules/` folder.** All content lives under `skills/<NN_Domain>/`. Register new files in `MODULE_INDEX.md`.
5. **Don't delete `docs/SHOWCASE.md`.** Add to it instead.
6. **Never downgrade the plugin version.** See `VERSIONING.md`.

## Adding a New Reference Topic to an Existing Domain

1. Add `skills/<NN_Domain>/reference/<topic-slug>.md` following the structure of sibling files in that folder (Goal, Core Decision, Options/Technologies table, Decision Rules, Anti-Patterns, Required Output Checklist).
2. Link it from the parent `skills/<NN_Domain>/SKILL.md` pointer list.
3. Add a row to `MODULE_INDEX.md`.
4. Bump the plugin version per `VERSIONING.md` (MINOR for new content) and add a `CHANGELOG.md` entry.

## Adding a New Domain (New Top-Level Skill Folder)

This is a structural change — open an issue/discussion first if possible. New domains must:
- Use the `NN_Domain_Name` naming convention, picking an unused number in the 00-99 range that fits logically near related domains.
- Include a `SKILL.md` with the same frontmatter shape as existing skills.
- Be added to all four registry files (`AGENT_REGISTRY.md` only if it changes ARCHON's routing logic, `SKILL_REGISTRY.md`, `COMMAND_REGISTRY.md` if a new shortcut command is warranted, `MODULE_INDEX.md`).

## Adding a New Command

1. Add `commands/<command-name>.md` with YAML frontmatter (`name`, `description`, `argument-hint`).
2. Register it in `COMMAND_REGISTRY.md` and in the root `README.md` Commands table.

## Style

- Prose, tables, and checklists are all fine. Avoid filler — every sentence should change what the reader does next.
- Prefer concrete numbers and named technologies over vague qualifiers ("Postgres handles ~10K writes/sec on a single primary" beats "Postgres scales well").
- Keep the Engineering Decision Principles (see `skills/99_Decision_Engine/`) as the north star for any new judgment call: never optimize for hype, optimize for long-term engineering reality.

## Reporting Issues

Open a GitHub issue describing what's wrong (outdated technology guidance, broken cross-reference, missing topic) and which file(s) are affected.

## Code of Conduct

This project applies the same engineering-reality standard to people that it applies to architecture decisions: be direct, be precise, and argue about the work rather than the person.

- Disagreements are welcome and expected — critique a recommendation's reasoning, trade-offs, or evidence, not its author.
- No harassment, personal attacks, or discriminatory language, in issues, pull requests, or discussions.
- Assume good faith. Most disagreements here are about engineering trade-offs, not character.
- Maintainers may close, edit, or reject contributions that don't meet this standard, with an explanation.

Report a violation by opening a GitHub issue or contacting the maintainer directly. This is a deliberately short code of conduct in the same spirit as the rest of this repository: no filler, only what changes behavior.
