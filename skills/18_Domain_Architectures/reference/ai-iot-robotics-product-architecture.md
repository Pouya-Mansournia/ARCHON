# Reference Architecture: AI, IoT & Robotics Products

## Goal

AI products, IoT products, and robotics products share a structural pattern that distinguishes them from typical web/SaaS products: a split between a resource-constrained edge/device layer and a cloud/backend layer, connected by a network link that's often unreliable, bandwidth-limited, or both. Reference architecture decisions here are dominated by where computation happens (device vs. edge vs. cloud) and how the system behaves when connectivity is degraded or absent.

## The Cloud-Edge-Device Spectrum

| Layer | Role | Example workload |
|---|---|---|
| Device | Real-time sensing, actuation, and safety-critical control | Motor control loops, immediate sensor fusion, e-stop logic (see `skills/11_Robotics/`) |
| Edge (local gateway/compute) | Aggregation, local inference, and buffering when cloud connectivity is degraded | Local LLM/vision inference for latency-sensitive features, telemetry batching |
| Cloud | Heavy compute, model training/retraining, fleet-wide coordination, long-term storage and analytics | Model training (see `skills/10_AI/reference/mlops-model-lifecycle.md`), fleet dashboards, historical analytics |

The core design question for every capability in the system is: which layer should this run on, given its latency requirement, its compute/power budget, and its tolerance for connectivity loss? Get this placement wrong (e.g., a safety-critical control decision dependent on a cloud round trip) and the failure mode isn't a slow feature, it's a safety incident.

## Representative Stack — AI Product (Cloud-Centric)

| Layer | Choice | Why |
|---|---|---|
| Inference | Managed LLM API for most features; self-hosted/edge inference only for latency- or cost-justified cases | Default to managed APIs per `skills/10_AI/SKILL.md`'s build-vs-buy matrix |
| Grounding | RAG over a vector store (pgvector or a dedicated vector DB) | Grounds responses in private/current data without fine-tuning |
| Evaluation & monitoring | A versioned evaluation set plus production quality/cost/latency monitoring | Treats the model as a critical dependency, not a black box (see `skills/10_AI/reference/mlops-model-lifecycle.md`) |
| Backend | Modular monolith fronting the AI inference calls, handling auth, rate limiting, and business logic | The AI capability is a component within a normal product architecture, not a replacement for one |

## Representative Stack — IoT Product

| Layer | Choice | Why |
|---|---|---|
| Device firmware | RTOS or bare-metal, minimal footprint | Resource-constrained hardware, often battery-powered (see `skills/11_Robotics/reference/embedded-realtime-control.md`) |
| Device-to-cloud protocol | MQTT | Lightweight, designed for unreliable networks and intermittent connectivity (see `skills/06_API/SKILL.md`) |
| Edge gateway (if present) | Local aggregation and buffering, forwarding batched telemetry when connectivity allows | Reduces bandwidth/data costs and tolerates connectivity gaps without losing data |
| Cloud ingestion | A time-series datastore for telemetry (TimescaleDB/InfluxDB) | Matches the time-ordered, high-volume nature of sensor data (see `skills/05_Database/SKILL.md`) |
| Fleet management | A dedicated control plane for device provisioning, configuration, and OTA firmware updates | Devices in the field need remote management distinct from the application backend |

## Representative Stack — Robotics Product

| Layer | Choice | Why |
|---|---|---|
| Real-time control core | RTOS/bare-metal with bounded worst-case execution time | Hard real-time safety requirement (see `skills/11_Robotics/reference/embedded-realtime-control.md`) |
| Perception & planning | ROS 2 (often, though evaluated against the platform's specific real-time needs) | Rich tooling/ecosystem for sensor fusion, simulation, and navigation (see `skills/11_Robotics/reference/robotics-architecture-ros.md`) |
| Safety supervisor | Architecturally independent monitoring layer with override authority | Cannot depend on the logic it's meant to guard against failing |
| Fleet/cloud layer | Mirrors the IoT fleet-management pattern above, plus model/behavior update distribution | Robotics products at fleet scale face the same remote-management needs as IoT, with added behavior/model versioning |

## The Shared Design Principle: Graceful Degradation on Connectivity Loss

Across all three product types, the system must have an explicit, designed answer for "what happens when the cloud link is unavailable" — buffer and resync for IoT telemetry, continue safe local operation for robotics, and degrade gracefully (cached responses, reduced functionality, clear user communication) for AI products dependent on a cloud inference call. Treat connectivity loss as an expected operating condition, not an edge case, for any product with a device/edge component.

## Common Mistakes

- Routing a safety-critical or latency-critical decision through a cloud round trip, making the system's safety properties dependent on network reliability.
- Designing the device/edge layer with no defined behavior for connectivity loss, resulting in undefined or unsafe behavior in the field.
- Treating an AI feature's cloud inference dependency with less operational rigor than other critical external dependencies (see `skills/10_AI/reference/llm-integration-rag.md`).
- Skipping fleet-management tooling until field deployment scale makes manual device management untenable, forcing a rushed retrofit.

## Decision Rule for This Domain

Place each capability deliberately on the cloud-edge-device spectrum based on its actual latency, power, and connectivity-tolerance requirements — never default everything to the cloud just because that's where development is easiest. Design explicit graceful-degradation behavior for connectivity loss as a core requirement, not an edge case.
