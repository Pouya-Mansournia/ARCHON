# ARCHON

> **A Principal Engineer / CTO decision system for Claude Code.**  
> From idea to production — architecture decisions optimized for engineering reality, not hype.

![License](https://img.shields.io/badge/license-MIT-green)
![Version](https://img.shields.io/badge/version-v1.1-blue)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen)
![Open Source](https://img.shields.io/badge/open--source-yes-black)

---

## What Is ARCHON?

ARCHON is an open-source engineering decision system designed for **Claude Code**.

It acts like a senior Principal Engineer, Staff Engineer, or CTO inside your development workflow. You give it a product idea, architecture question, stack decision, scaling concern, AI system design, robotics architecture, cloud trade-off, or technical review — and it returns a structured, defensible engineering recommendation.

Not a generic answer.  
Not a list of trendy tools.  
Not “it depends” without direction.

ARCHON is built to answer:

- what to use
- why it is the right choice
- why not the alternatives
- trade-offs
- risks
- cost impact
- scalability impact
- security impact
- confidence level
- migration path

Its purpose is simple:

> **Help builders make better technical decisions before writing the wrong code.**

---

## Why ARCHON Exists

Many engineering mistakes do not start in code.

They start earlier:

- choosing Kubernetes before the team needs it
- splitting into microservices too soon
- picking a database because it is popular
- adding Kafka because “we might need it later”
- building custom auth when a managed provider would be safer
- using an AI stack without evaluation, monitoring, or fallback logic
- designing robotics software without thinking about real-time constraints, safety, and field maintenance

ARCHON exists to slow down those decisions just enough to make them better.

It gives the kind of second opinion a strong technical founder, CTO, or Principal Engineer would give:

> “Here is the simplest thing that will work.  
> Here is what will break first.  
> Here is what this costs.  
> Here is when you should migrate.  
> Here is what not to build yet.”

---

## Core Philosophy

ARCHON optimizes for engineering reality.

Every recommendation follows a fixed priority order:

```text
Simplicity
  ↓
Maintainability
  ↓
Reliability
  ↓
Development Speed
  ↓
Cost Efficiency
  ↓
Security
  ↓
Scalability
  ↓
Performance
  ↓
Future Flexibility
  ↓
Technical Elegance
```

The system prefers boring, proven, maintainable technology until complexity is justified.

That does not mean ARCHON avoids advanced systems.  
It means advanced systems must earn their place.

---

## Who Is It For?

ARCHON is useful for:

- technical founders deciding the first real stack for a startup
- engineers who want a strong second opinion before implementation
- staff and principal engineers reviewing architecture decisions
- CTOs and engineering leaders explaining technical trade-offs to business teams
- product managers who need to understand engineering scope and risk
- AI teams building LLM, RAG, evaluation, and MLOps systems
- robotics and IoT teams working with embedded systems, real-time control, ROS, and sensor fusion
- students, researchers, and builders who want structured technical reasoning

---

## What ARCHON Can Help With

ARCHON can support decisions such as:

```text
Should this backend be Python, Go, Node.js, Java, or Rust?

Should we use PostgreSQL, MongoDB, Redis, TimescaleDB, or InfluxDB?

Should this system start as a modular monolith or microservices?

Do we need Kafka, RabbitMQ, MQTT, Redis Streams, or simple HTTP?

Should we deploy with Docker Compose, Kubernetes, serverless, or managed PaaS?

Should we build authentication ourselves or use Clerk/Auth0/Cognito?

How should we design an AI SaaS architecture?

How should we structure a RAG pipeline before production?

How should we design an IoT/robotics data platform?

What breaks first in this architecture?

What is the cheapest safe architecture for our current stage?

How do we migrate later without rewriting everything?
```

---

## Architecture

ARCHON is intentionally designed as **one agent with five seniority levels**, not a fake multi-agent executive team.

```text
User Question
    ↓
ARCHON Agent
    ↓
Decision Engine
    ↓
Relevant Skill Modules
    ↓
Trade-off Resolution
    ↓
Output Standard
    ↓
Defensible Engineering Recommendation
```

The reason is simple:

Engineering decisions need one coherent answer.

A CTO, Principal Engineer, Cloud Architect, AI Engineer, and Cost Reviewer may all have useful perspectives — but the final output must be one clear decision, not five disconnected opinions.

---

## The Five Levels

ARCHON thinks across five levels of engineering maturity.

| Level | Focus | Best For |
|---|---|---|
| **L1 — Foundations** | Linux, networking, web servers, Git, basic infrastructure | Junior engineers or quick technical refreshers |
| **L2 — Software Engineering** | Frontend, backend, databases, APIs, testing | Engineers and tech leads building systems |
| **L3 — Infrastructure & Cloud** | DevOps, CI/CD, containers, observability, reliability, performance | Platform, DevOps, and infrastructure decisions |
| **L4 — Principal Engineering** | System architecture, AI systems, robotics, security, technical debt | Staff, principal, and architecture-level reviews |
| **L5 — CTO & Business** | Cost, team size, build-vs-buy, hiring, vendor lock-in, roadmap | Founders, CTOs, VPs, and business-facing technical leaders |

A real question often touches multiple levels at once.

For example:

> “Should we use Kubernetes?”

This is not only an infrastructure question.  
It is also a team-size, cost, reliability, hiring, and operational maturity question.

ARCHON evaluates all relevant levels before giving an answer.

---

## Knowledge Base

ARCHON is built from a structured engineering knowledge base.

```text
skills/
├── 00_Core/                   Decision principles and over/under-engineering detector
├── 01_Foundations/             Linux, networking, web servers, Git
├── 02_Product/                 Product discovery, MVP, PMF, business architecture
├── 03_Frontend/                Frontend and mobile architecture
├── 04_Backend/                 Backend languages, frameworks, and service design
├── 05_Database/                SQL, NoSQL, caching, storage, search, time-series data
├── 06_API/                     REST, GraphQL, gRPC, messaging, event-driven systems
├── 07_Architecture/            Monoliths, microservices, DDD, CQRS, service mesh
├── 08_Cloud/                   Cloud providers, multi-region, edge, multi-cloud
├── 09_DevOps/                  Containers, Kubernetes, CI/CD, GitOps
├── 10_AI/                      LLMs, RAG, MLOps, AI safety, evaluation
├── 11_Robotics/                ROS, embedded systems, real-time control, sensor fusion
├── 12_Security/                Auth, data protection, threat modeling, compliance
├── 13_Reliability/             Observability, incident response, SLOs, error budgets
├── 14_Performance/             Profiling, load testing, scaling patterns, analytics
├── 15_Engineering_Practices/   Code review, testing, documentation, technical debt
├── 16_Team_Leadership/         Team topology, hiring, engineering culture
├── 17_Cost_Business/           FinOps, TCO, build-vs-buy, vendor lock-in
├── 18_Domain_Architectures/    SaaS, marketplace, AI, IoT, robotics systems
├── 19_Review_Outputs/          ADR templates and structured review formats
└── 99_Decision_Engine/         Routing, conflict resolution, confidence calibration
```

Each skill contains decision rules, comparison logic, and reference material.  
ARCHON loads the relevant parts depending on the question.

---

## Output Standard

Every concrete ARCHON recommendation follows this structure:

```text
1. What to use
2. Why this choice
3. Why not the alternatives
4. Trade-offs
5. Risks
6. Cost impact
7. Scalability impact
8. Security impact
9. Confidence level
10. Migration path
```

This makes the output suitable for:

- architecture decision records
- technical planning
- founder decision-making
- engineering review
- product/engineering alignment
- investor or board-level technical explanation
- roadmap planning

---

## Commands

ARCHON includes eight focused command modes.

| Command | Mode | Use It For |
|---|---|---|
| `/archon` | Default advisor | General engineering and product architecture questions |
| `/archon-principal` | Principal Engineer | Concrete architecture decisions and ADR-ready answers |
| `/archon-cto` | CTO | Cost, team, build-vs-buy, vendor lock-in, business impact |
| `/archon-ai` | AI Architect | LLM, RAG, MLOps, evaluation, AI product safety |
| `/archon-robotics` | Robotics Architect | ROS, embedded systems, real-time control, sensor fusion |
| `/archon-review` | Critic / Reviewer | Review an existing architecture, PRD, design, or technical plan |
| `/archon-plan` | Planner | MVP → Growth → Scale execution planning |
| `/archon-reflect` | Reflection | Re-check a past decision and mark it Unchanged, Refined, or Reversed |

---

## Quick Start

Clone the repository:

```bash
git clone https://github.com/Pouya-Mansournia/ARCHON.git
cd ARCHON
```

Load it as a local Claude Code plugin.

Then run:

```text
/archon-principal
We are a 6-person team building a B2B SaaS product.
We expect around 10k users in year one.
What should our default architecture and stack be?
```

Example response shape:

```text
What to use:
Start with a modular monolith using Next.js, a backend service in Go or Python,
PostgreSQL as the primary database, Redis for caching and queues where needed,
and a simple managed cloud deployment.

Why:
At this stage, the main risk is not scale. The main risk is moving too slowly,
over-splitting the system, and creating operational complexity before the team
has enough product signal.

Why not microservices:
Microservices add deployment, observability, tracing, service ownership,
network failure, and operational overhead. For a 6-person team and 10k expected
users, that complexity is not justified yet.

Confidence:
High.

Migration path:
Keep strong module boundaries inside the monolith. Extract services only when
team ownership, scaling pressure, or deployment independence becomes real.
```

---

## Example Prompts

```text
/archon
Should we use Django, FastAPI, or Node.js for this backend?

/archon-principal
We are designing a warehouse automation dashboard.
Should we use PostgreSQL, TimescaleDB, or InfluxDB for sensor data?

/archon-cto
We are a small startup. Should we build our own auth or use Clerk/Auth0?

/archon-ai
How should we evaluate a RAG pipeline before exposing it to customers?

/archon-robotics
For an indoor mobile robot fleet, should we use ROS 2, MQTT, or a custom control layer?

/archon-review
Here is our proposed architecture. What breaks first?

/archon-plan
Create an MVP → Production → Scale architecture plan for an AI SaaS product.

/archon-reflect
We chose microservices 8 months ago. Was that still the right decision?
```

---

## Example Use Cases

### Startup Stack Decision

```text
Question:
We are building a B2B SaaS product with a small team.
Should we start with microservices?

ARCHON direction:
No, unless there is a clear team or scaling reason.
Start with a modular monolith and clean boundaries.
Optimize for shipping speed, maintainability, and low operational overhead.
```

### AI Product Architecture

```text
Question:
We are building an AI assistant with RAG.
What should we consider before production?

ARCHON direction:
Do not only focus on the model.
Design retrieval quality checks, evaluation datasets, fallback behavior,
observability, prompt/version tracking, privacy rules, and human review paths.
```

### Robotics / IoT System

```text
Question:
Should our robotics platform send all telemetry directly to the cloud?

ARCHON direction:
No, not by default.
Separate real-time control from cloud telemetry.
Keep safety-critical loops local.
Use cloud systems for monitoring, analytics, fleet management, and non-real-time decisions.
```

### Cloud Cost Review

```text
Question:
Our AWS bill is increasing faster than usage.
What should we check first?

ARCHON direction:
Start with compute utilization, managed database sizing, storage lifecycle,
egress cost, logging volume, idle environments, and over-provisioned Kubernetes resources.
Do not start by rewriting the architecture.
```

---

## What ARCHON Is Not

ARCHON is not:

- a code generator
- a replacement for engineering judgment
- a magic architecture oracle
- a trend-based tool recommender
- a cloud deployment platform
- a monitoring system
- a multi-agent company simulator

ARCHON is a structured decision layer.

It helps you think before you build.

---

## Design Principles

ARCHON follows these principles:

1. **Default to simplicity**
2. **Prefer boring technology until complexity is justified**
3. **Make trade-offs explicit**
4. **State confidence clearly**
5. **Include migration paths**
6. **Separate real requirements from imagined future scale**
7. **Respect team size and operational maturity**
8. **Treat cost as an architecture constraint**
9. **Do not hide uncertainty**
10. **Optimize for maintainable execution**

---

## Repository Structure

```text
ARCHON/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── ROADMAP.md
├── CONTRIBUTING.md
├── VERSIONING.md
├── ARCHITECTURE_DECISIONS.md
├── MODULE_INDEX.md
├── AGENT_REGISTRY.md
├── SKILL_REGISTRY.md
├── COMMAND_REGISTRY.md
├── agents/
├── commands/
├── docs/
├── examples/
├── memory/
├── skills/
├── tests/
└── .claude-plugin/
```

---

## Documentation

| File | Purpose |
|---|---|
| `docs/INSTALL.md` | Installation guide |
| `docs/QUICKSTART.md` | First-session guide |
| `docs/EXAMPLES.md` | Prompt examples |
| `docs/SHOWCASE.md` | Narrative use cases |
| `SKILL_REGISTRY.md` | Full skill index |
| `COMMAND_REGISTRY.md` | Command list and behavior |
| `MODULE_INDEX.md` | Complete repository map |
| `ARCHITECTURE_DECISIONS.md` | Why ARCHON is designed this way |
| `ROADMAP.md` | Current and future development plan |
| `CONTRIBUTING.md` | Contribution guide |

---

## Quality Bar

ARCHON is designed as a serious engineering knowledge project.

The repository includes validation logic for:

- plugin structure
- required metadata
- internal references
- command definitions
- skill organization
- documentation consistency

The goal is to keep the project maintainable as the knowledge base grows.

---

## Roadmap

### Current

- Single ARCHON decision agent
- Five seniority levels
- Engineering decision engine
- 20+ skill domains
- Claude Code command interface
- Architecture review and reflection modes

### Next

- More worked architecture review examples
- More real-world stack comparison cases
- Dedicated FinOps shortcut command
- More robotics and AI system design references
- Expanded ADR-ready output examples

### Later

- Optional team-specific customization layer
- More domain architecture packs
- Community-contributed decision modules
- Optional integrations only where they add real value

---

## Contributing

ARCHON is primarily a knowledge and decision-quality project.

Good contributions include:

- sharper decision rules
- better comparison tables
- real-world architecture examples
- improved trade-off explanations
- corrections to technical references
- new domain-specific architecture patterns
- stronger examples for AI, robotics, cloud, security, and cost

Please read `CONTRIBUTING.md` before opening a pull request.

---

## Suggested GitHub About

Use this in the repository **About** section:

```text
A Principal Engineer / CTO decision system for Claude Code. ARCHON helps founders and engineers make production-grade architecture, AI, cloud, robotics, cost, and scaling decisions with explicit trade-offs, risks, confidence levels, and migration paths.
```

Suggested GitHub topics:

```text
claude-code
ai-agent
engineering
software-architecture
system-design
technical-decision-making
cto
principal-engineer
ai-architecture
robotics
devops
cloud-architecture
startup
open-source
architecture-decision-records
```

---

## License

MIT License  
© 2026 Pouya Mansournia

---

## Final Line

**One question. One defensible answer. Optimize for engineering reality — never for hype.**
