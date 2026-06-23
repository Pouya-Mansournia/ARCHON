# Brand Voice

How ARCHON's content should read — for anyone contributing new skill content, commands, or docs to this repository. The goal is a consistent voice across 21 skill modules and 58 reference files, so the knowledge base reads as one coherent system rather than a patchwork of contributions.

## Voice: Senior Engineer, Not a Brochure

Write the way an experienced Principal Engineer or CTO would explain a trade-off to a peer — direct, specific, willing to say "it depends, and here's what it depends on." Avoid:

- Marketing language ("revolutionary," "best-in-class," "cutting-edge") — name the actual trade-off instead of asserting superiority.
- Hedging without substance ("it really depends on many factors" with no factors named) — always name the specific factors.
- False confidence — if a recommendation is context-dependent or genuinely uncertain, say so explicitly rather than picking a side to sound decisive.

## Structure Every Piece of Substantive Content Around a Decision

Every `reference/*.md` file should answer: what's the decision being made, what are the real options, what does each option cost (in complexity, money, operational burden, or risk), and what's the rule for choosing. A file that only describes technology without tying it to a decision isn't pulling its weight — see existing reference files for the pattern (Goal → decision table → staged/contextual nuance → Common Mistakes → Decision Rule for This Domain).

## Default to Tables for Comparisons, Prose for Reasoning

Comparison data (options, trade-offs, stage-by-stage guidance) belongs in a table. The reasoning connecting that data to a recommendation belongs in prose. Don't bullet-point reasoning that needs logical connectors ("because," "which means," "but only when") — that reasoning needs prose to read clearly de-collapsed from bullet fragments.

## Always Name the Alternative, Not Just the Choice

"Use Postgres" is an opinion. "Use Postgres over MongoDB here because the data is genuinely relational and you'd otherwise be reimplementing joins in application code" is an engineering decision. Every recommendation in this knowledge base should carry its rejected alternative and the specific reason it was rejected — this is what makes the Output Standard's "Why not the alternatives" section possible to fill in well.

## Calibrate Certainty Honestly

Distinguish between "this is close to a settled engineering consensus" (e.g., don't hand-roll password hashing) and "this is a genuine judgment call that depends on team/stage/constraints" (e.g., monolith vs. microservices). Content that presents judgment calls as settled facts, or settled facts as open questions, undermines the confidence-calibration system in `skills/99_Decision_Engine/`.

## No Hype Cycles

Don't chase whatever is currently trending in tech discourse. A technology's adoption curve and its actual fitness for a given problem are different things — ground recommendations in the latter. When something genuinely is new and good, say why on its technical/operational merits, not because it's popular.

## Language

All content in this repository is written in English, with no exceptions — including code comments, examples, and file names. See `CONTRIBUTING.md`.
