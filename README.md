# ARCHON

**A Principal Engineer / CTO in your `claude` CLI.**

ARCHON is a Claude Code plugin that turns a product idea, a technology choice, or an existing system into a production-grade engineering decision — with explicit trade-offs, risks, cost impact, and a stated confidence level. It is one persona that operates at five seniority altitudes (L1 Foundations through L5 CTO & Business), backed by a 20-domain, 57-topic engineering knowledge base.

It is not a chatbot that lists options. It is built to give one defensible answer, explain why the alternatives lose, and say plainly when a question hasn't been narrowed enough to answer responsibly yet.

## Why a Single Agent, Not a C-Suite Roster

A lot of "agentic OS" playbooks ship a full executive roster — CEO, CPO, CTO, CFO, CMO, and so on — as separate agents. ARCHON deliberately doesn't. The actual problem this plugin solves is engineering and architecture decision-making, and a simulated executive team for that problem just adds routing ambiguity ("which of ten agents do I call?") without adding decision quality. ARCHON is one cohesive Principal Engineer / CTO voice that scales its altitude to the question — from explaining Nginx routing to a junior engineer to defending a multi-region database decision to a board. The full reasoning is in [`ARCHITECTURE_DECISIONS.md`](ARCHITECTURE_DECISIONS.md) (ADR-001).

## The Five Levels

| Level | Domain | Audience |
|---|---|---|
| **L1** — Foundations | Linux, networking, web servers, Git | Junior engineers, or seniors who need a precise refresher |
| **L2** — Software Engineering | Frontend, backend, databases, APIs, testing | Engineers and tech leads building a system |
| **L3** — Infrastructure & Cloud | Cloud, DevOps/CI-CD, containers, observability, reliability, performance | Infra/platform engineers, EMs |
| **L4** — Principal Engineering | Architecture patterns, AI/robotics/domain architectures, security, technical debt | Principal/staff engineers, architects |
| **L5** — CTO & Business | FinOps, build-vs-buy, team topology, vendor lock-in, executive communication | CTOs, founders, VPs of Engineering |

A real question often spans levels at once — "should we use Kubernetes?" is L3 infrastructure reality and L5 team/cost reality in the same breath. ARCHON addresses every level a question actually touches rather than forcing an artificial single-altitude answer.

## Quick Start

```bash
git clone https://github.com/Pouya-Mansournia/ARCHON.git
cd ARCHON
```

Load it as a local Claude Code plugin, then:

```
claude
> /archon What's the right default backend stack for a B2B SaaS MVP with a 3-person team?
```

Full install instructions: [`docs/INSTALL.md`](docs/INSTALL.md). Guided first session: [`docs/QUICKSTART.md`](docs/QUICKSTART.md).

## Commands

| Command | Mode | Use it for |
|---|---|---|
| `/archon` | Default advisory | General engineering/product question, routed automatically to the right domain |
| `/archon-cto` | CTO | Cost, team, build-vs-buy, board-level framing |
| `/archon-principal` | Principal Engineer | A concrete architecture decision, output in ADR-ready form |
| `/archon-robotics` | Robotics | Embedded, real-time, ROS, sensor fusion |
| `/archon-ai` | AI/ML | LLM integration, RAG, MLOps, AI product safety |
| `/archon-review` | Review/critic | Adversarial critique of an existing design or PR |
| `/archon-plan` | Planner | Phased MVP → Growth → Scale execution plan |
| `/archon-reflect` | Reflection | Re-examine a past decision: Unchanged / Refined / Reversed |

Full detail on each: [`COMMAND_REGISTRY.md`](COMMAND_REGISTRY.md).

## The Output Standard

Every concrete architecture recommendation follows the same ten-part shape — not a free-form essay, not a bare opinion:

1. What to use
2. Why this choice
3. Why not the alternatives
4. Trade-offs
5. Risks
6. Cost impact
7. Scalability impact
8. Security impact
9. Confidence level (High / Medium / Low)
10. Migration path

When trade-offs conflict, ARCHON resolves them in a fixed priority order — Simplicity → Maintainability → Reliability → Development Speed → Cost Efficiency → Security → Scalability → Performance → Future Flexibility → Technical Elegance — and says explicitly when it's overriding that default for the situation at hand (a fintech system promoting Security above Development Speed, for instance). Full rubric: [`skills/99_Decision_Engine/reference/output-standard-and-confidence.md`](skills/99_Decision_Engine/reference/output-standard-and-confidence.md).

## How the Knowledge Base Is Organized

```
skills/
├── 00_Core/                   Engineering Decision Principles, over/under-engineering detector
├── 01_Foundations/             Linux, networking, web servers, Git
├── 02_Product/                 Product discovery, MVP/PMF, business architecture
├── 03_Frontend/                Frontend & mobile architecture
├── 04_Backend/                 Backend architecture
├── 05_Database/                Database, caching, storage, search
├── 06_API/                     API/communication patterns, messaging
├── 07_Architecture/            Architecture patterns, service mesh
├── 08_Cloud/                   Cloud providers, multi-region, edge/multi-cloud
├── 09_DevOps/                  Containers/Kubernetes, CI/CD, GitOps
├── 10_AI/                      LLM/RAG, MLOps, AI product safety
├── 11_Robotics/                ROS, embedded/real-time control, sensor fusion
├── 12_Security/                AuthN/AuthZ, data protection, threat modeling, compliance
├── 13_Reliability/             Observability, incident management, SLOs/error budgets
├── 14_Performance/             Profiling/load testing, scaling patterns, analytics platforms
├── 15_Engineering_Practices/   Code review, testing strategy, tech debt, documentation
├── 16_Team_Leadership/         Team topology, hiring, technical leadership culture
├── 17_Cost_Business/           FinOps, build-vs-buy/TCO
├── 18_Domain_Architectures/    SaaS, marketplace/e-commerce, AI/IoT/robotics products
├── 19_Review_Outputs/          ADR templates, structured review output format
└── 99_Decision_Engine/         Cross-cutting routing, conflict resolution, confidence calibration
```

Each domain ships a concise `SKILL.md` (scope, decision rules, comparison table, pointer list) plus one detailed `reference/*.md` file per sub-topic — 21 `SKILL.md` files and 58 reference files in total, covering roughly 57 topics. The agent itself carries no hardcoded domain knowledge; it loads the relevant `SKILL.md` and reference files for whatever the question actually touches. See [`SKILL_REGISTRY.md`](SKILL_REGISTRY.md) for the full index and [`ARCHITECTURE_DECISIONS.md`](ARCHITECTURE_DECISIONS.md) (ADR-003, ADR-004) for why it's structured this way.

## Repository Map

| Path | What's there |
|---|---|
| `.claude-plugin/plugin.json` | Plugin manifest |
| `agents/archon.md` | The single ARCHON agent definition |
| `commands/` | The 8 slash commands |
| `skills/` | The 21-module, 58-reference-file knowledge base |
| `docs/` | Install, quickstart, FAQ, examples, showcase, brand voice |
| `examples/` | Full worked transcripts (architecture decision, security review, robotics) |
| `tests/` | Structure validator (`validate_structure.py`) + how to run it |
| `memory/` | How to persist ARCHON-assisted decisions across sessions (ARCHON itself is stateless) |
| `AGENT_REGISTRY.md` / `COMMAND_REGISTRY.md` / `SKILL_REGISTRY.md` / `MODULE_INDEX.md` | Registries and the full repository index |
| `ARCHITECTURE_DECISIONS.md` | Why ARCHON itself is built the way it is (ADR log) |

Full map with every file: [`MODULE_INDEX.md`](MODULE_INDEX.md).

## Quality Bar

A Python structure validator (`tests/validate_structure.py`) runs on every push and pull request via GitHub Actions (`.github/workflows/validate.yml`). It checks plugin manifest validity, required frontmatter on every skill/command/agent file, that every internal cross-reference actually resolves, and that the repository is 100% English-language content — no exceptions, enforced automatically rather than by review discipline alone.

## Contributing

ARCHON is primarily a content project — new reference material, sharper decision rules, corrections — more than a code project. Start with [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Versioning & Roadmap

Semantic versioning, detailed in [`VERSIONING.md`](VERSIONING.md); history in [`CHANGELOG.md`](CHANGELOG.md); what's next in [`ROADMAP.md`](ROADMAP.md).

## License

[MIT](LICENSE) © 2026 Pouya Mansournia
