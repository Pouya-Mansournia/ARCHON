# Hiring Engineering Talent

## Goal

Hiring decisions are architecture decisions with a multi-year time horizon — the team you hire constrains the technology choices that are sustainable to operate, and the technology choices you make constrain who you can hire and how steep their ramp-up will be. Reason about both together, not hiring in isolation from technical strategy.

## Hiring for Stage, Not Aspiration

| Stage | What to prioritize in hiring |
|---|---|
| Pre-PMF | Generalists who can move across the stack and tolerate ambiguity — the product itself is still being discovered, and narrow specialists are often a poor fit before there's a stable problem to specialize against |
| Growth | A mix of generalists and the first specialists in areas becoming genuine bottlenecks (e.g., the first dedicated DevOps/infrastructure hire once deployment complexity outgrows ad hoc handling) |
| Scale | Deeper specialization becomes justified as distinct domains (security, ML, platform, robotics) reach a size and criticality that warrants dedicated expertise |

Hiring a narrow specialist before the company has a stable enough problem in their specialty to keep them productively engaged is a common, costly mismatch — both for the company (paying for underutilized expertise) and for the hire (frustration at being underused or pulled into generalist work they didn't sign up for).

## Defining the Role Before Hiring

A role definition should specify the actual problems the hire will solve in their first 90 days, not just a list of technology keywords — a requisition that's just a tech stack list filters for keyword-matching rather than for the judgment and problem-solving ability that actually predicts success, especially at the senior/principal level where the job is largely about making good trade-off decisions, not executing a known checklist.

## Technical Interviewing — What to Actually Assess

| What's commonly over-weighted | What actually predicts on-the-job performance |
|---|---|
| Algorithmic puzzle-solving disconnected from the actual job | Ability to reason about trade-offs on a problem resembling real work |
| Memorized trivia about a specific framework/language | Fundamentals (data structures, system design judgment, debugging approach) that transfer across specific technology choices |
| A single high-pressure whiteboard session | A process that also reveals how the candidate communicates, asks clarifying questions, and handles being told they're wrong or missing information |

Calibrate the interview process to the actual role — a senior/principal hire should be evaluated heavily on judgment and trade-off reasoning (close to what `/archon-principal` mode produces), while a more junior hire can reasonably be evaluated more on fundamentals and growth trajectory.

## Avoiding Resume-Driven Hiring (and Resume-Driven Architecture)

There's a feedback loop worth being deliberate about: hiring people experienced in a trendy technology creates internal pressure to adopt that technology regardless of fit, and adopting a trendy technology to "stay competitive for talent" can drive premature architectural complexity. Make the technology choice first based on actual product/system needs (per the rest of this knowledge base), then hire for it — not the reverse.

## Common Mistakes

- Hiring a narrow specialist before the company has a stable, sufficiently large problem in their specialty, leading to underutilization and attrition.
- Writing role requisitions as technology-keyword checklists rather than descriptions of the actual problems to be solved.
- Over-indexing technical interviews on algorithmic trivia disconnected from the role's actual day-to-day demands, especially for senior/principal roles where trade-off judgment matters more than implementation speed.
- Letting hiring trends or candidate-pool technology familiarity drive architecture decisions rather than the reverse.

## Decision Rule for This Domain

Hire generalists early, add specialists only against a demonstrated, sustained need in that specialty. Define roles around problems to be solved, not technology keyword lists. Calibrate interview emphasis (fundamentals vs. trade-off judgment) to seniority. Let architecture decisions drive hiring needs, not the other way around.
