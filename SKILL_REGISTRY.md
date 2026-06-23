# Skill Registry

The canonical index of every skill module in ARCHON's knowledge base: 21 `SKILL.md` files (20 domain modules plus the cross-cutting Decision Engine) and 58 detailed `reference/*.md` files behind them, organized per ADR-003 and ADR-004 in `ARCHITECTURE_DECISIONS.md`.

Each `SKILL.md` is intentionally short — a goal statement, the highest-leverage decision rule(s) for that domain, and pointers to its `reference/` files for full depth. This progressive-disclosure structure keeps the agent's working context small while still giving it access to comprehensive depth on demand.

## Domain Modules (00-19) + Decision Engine (99)

| Folder | Skill Name | Level | Summary |
|---|---|---|---|
| `00_Core` | `core-principles-decision-engine` | Cross-cutting (L1-L5) | The 8 Core Principles and the over/under-engineering detector — the operating system every other domain runs on top of. |
| `01_Foundations` | `foundations` | L1 | Linux administration, networking fundamentals, Nginx/web servers, Git/version control. |
| `02_Product` | `product-business` | L2, ties to L5 | The 16 product/business discovery questions, product-category patterns, MVP/PMF discipline. |
| `03_Frontend` | `frontend-architecture` | L2 | Web framework and mobile platform selection (React/Next.js/Vue/Svelte/Angular; native vs. cross-platform mobile). |
| `04_Backend` | `backend-architecture` | L2 | Backend language/framework selection (Node/TS, Python, Go, Java, C#/.NET, Rust, PHP). |
| `05_Database` | `database-data-architecture` | L2, extends to L3 | Relational/NoSQL/key-value/time-series/search/vector/object storage selection, caching, search, and storage architecture. |
| `06_API` | `api-communication-architecture` | L2 | REST/GraphQL/gRPC/WebSocket/MQTT/webhooks and messaging/queue systems (RabbitMQ, Kafka, NATS, Celery). |
| `07_Architecture` | `architecture-patterns` | L4 | Monolith → modular monolith → microservices, event-driven, CQRS, event sourcing, DDD, hexagonal architecture, service mesh. |
| `08_Cloud` | `cloud-infrastructure` | L3 | Cloud provider selection, multi-region architecture, edge computing, multi-cloud strategy. |
| `09_DevOps` | `devops-cicd` | L3 | Containers, Docker, Kubernetes, CI/CD pipelines, GitOps. |
| `10_AI` | `ai-ml-architecture` | L4, L2 detail in references | LLM integration, RAG, MLOps/model lifecycle, AI product safety and evaluation. |
| `11_Robotics` | `robotics-systems-architecture` | L4 | ROS/middleware choice, embedded real-time control, sensor fusion and perception. |
| `12_Security` | `security-architecture` | L4 | Authn/authz, data protection and encryption, threat modeling/AppSec, compliance and regulatory governance. |
| `13_Reliability` | `reliability-sre` | L4 | Observability/monitoring, incident management/chaos engineering, SLOs/SLAs/error budgets. |
| `14_Performance` | `performance-engineering` | L3/L4 | Profiling and load testing, scaling patterns, analytics/data-platform architecture. |
| `15_Engineering_Practices` | `engineering-practices` | L4 | Code review, testing strategy, technical debt management, documentation practices. |
| `16_Team_Leadership` | `team-leadership` | L5 | Team topology/org design, hiring engineering talent, technical leadership and culture. |
| `17_Cost_Business` | `cost-business-architecture` | L5 | FinOps/cloud cost optimization, build-vs-buy and total-cost-of-ownership analysis. |
| `18_Domain_Architectures` | `domain-reference-architectures` | L4 (synthesis) | Worked end-to-end architectures: SaaS/B2B, marketplace/e-commerce, AI/IoT/robotics products. |
| `19_Review_Outputs` | `review-output-standards` | L4 (cross-cutting) | ADR/decision-log templates and the structured review-critique output format. |
| `99_Decision_Engine` | `archon-decision-engine` | All levels | Routes questions to the right domain(s), resolves conflicts between domain rules, calibrates confidence. |

## Reference File Index by Domain

| Domain | Reference files |
|---|---|
| `00_Core` | `core-principles.md`, `over-under-engineering.md`, `principal-engineer-thinking.md` |
| `01_Foundations` | `linux-fundamentals.md`, `networking-fundamentals.md`, `nginx-web-servers.md`, `git-version-control.md` |
| `02_Product` | `product-discovery-requirements.md`, `business-architecture-patterns.md`, `product-engineering-mvp-pmf.md` |
| `03_Frontend` | `frontend-architecture.md`, `mobile-architecture.md` |
| `04_Backend` | `backend-architecture.md` |
| `05_Database` | `database-data-architecture.md`, `caching-architecture.md`, `search-architecture.md`, `storage-architecture.md` |
| `06_API` | `communication-architecture.md`, `messaging-event-driven.md` |
| `07_Architecture` | `architecture-patterns.md`, `service-mesh.md` |
| `08_Cloud` | `cloud-providers-infrastructure.md`, `multi-region-architecture.md`, `edge-multi-cloud.md` |
| `09_DevOps` | `containers-docker-kubernetes.md`, `cicd-gitops.md` |
| `10_AI` | `llm-integration-rag.md`, `mlops-model-lifecycle.md`, `ai-product-safety.md` |
| `11_Robotics` | `robotics-architecture-ros.md`, `embedded-realtime-control.md`, `sensor-fusion-perception.md` |
| `12_Security` | `authn-authz.md`, `data-protection-encryption.md`, `threat-modeling-appsec.md`, `compliance-governance.md` |
| `13_Reliability` | `observability-monitoring.md`, `incident-management-chaos.md`, `slo-sla-error-budgets.md` |
| `14_Performance` | `performance-profiling-load-testing.md`, `scaling-patterns.md`, `analytics-data-platform.md` |
| `15_Engineering_Practices` | `code-review-practices.md`, `testing-strategy.md`, `technical-debt-management.md`, `documentation-practices.md` |
| `16_Team_Leadership` | `team-topology-org-design.md`, `hiring-engineering-talent.md`, `technical-leadership-culture.md` |
| `17_Cost_Business` | `finops-cost-optimization.md`, `build-vs-buy-tco.md` |
| `18_Domain_Architectures` | `saas-b2b-architecture.md`, `marketplace-ecommerce-architecture.md`, `ai-iot-robotics-product-architecture.md` |
| `19_Review_Outputs` | `adr-decision-log-templates.md`, `review-output-standards.md` |
| `99_Decision_Engine` | `decision-trees.md`, `output-standard-and-confidence.md` |

Total: 21 `SKILL.md` files, 58 `reference/*.md` files.

## How Skills Compose

No single skill module is meant to be read in isolation for anything but the narrowest question. A realistic question (e.g., "how should we architect our new product") spans `02_Product` (requirements), `07_Architecture` (pattern), several L2/L3 domains for the specific stack, `12_Security` and `13_Reliability` as cross-cutting baselines, and `99_Decision_Engine` to tie the synthesis together and assign confidence. See `skills/99_Decision_Engine/reference/decision-trees.md` for worked routing examples.

## Adding a New Skill Module

New domain modules should follow the existing pattern: a concise `SKILL.md` (goal, the domain's highest-leverage decision rule, a pointer to `reference/`) plus one or more `reference/*.md` files with full depth (decision tables, common mistakes, an explicit "Decision Rule for This Domain" section). Update this file and `MODULE_INDEX.md` when adding or renaming any skill file — broken cross-references are a recurring failure mode this registry exists to prevent. See `CONTRIBUTING.md`.
