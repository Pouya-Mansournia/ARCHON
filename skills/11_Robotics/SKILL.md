---
name: robotics-systems-architecture
description: Robotics and autonomous systems architecture — ROS/middleware choices, embedded real-time control, sensor fusion and perception — with decision rules grounded in safety, determinism, and manufacturability rather than software-only trade-offs.
---

# 11 — Robotics & Autonomous Systems (L4)

**Level:** L4 — Principal Engineering, drawing on the user's own Robotics & Mechatronics background.

## Goal

Apply standard software-architecture thinking (modularity, clear interfaces, testability) to robotics systems while respecting the constraints that make robotics genuinely different from typical backend/web engineering: hard real-time deadlines, physical safety consequences, sensor noise and uncertainty, and the cost/complexity of hardware iteration cycles.

## What Makes Robotics Architecture Different

| Typical software concern | Robotics-specific version |
|---|---|
| Latency budget | Often a hard real-time deadline — missing it isn't slow, it's a control-loop failure with physical consequences |
| Error handling | Must account for sensor noise, partial observability, and the world not matching the model — not just exceptions in code |
| Testing | Simulation-first, then hardware-in-the-loop, then real-world — a bug in the field can damage hardware or cause physical harm, not just corrupt data |
| Deployment | Often constrained by compute/power/thermal budgets on the physical platform, not elastic cloud scaling |
| Safety | A first-class architectural concern (e-stops, fail-safe states, redundancy) — not best-effort, mandatory |

## Architecture Layering for a Robotic System

| Layer | Responsibility |
|---|---|
| Hardware abstraction | Drivers for sensors/actuators, exposing a stable interface to layers above |
| Perception | Sensor fusion, state estimation, object/environment understanding |
| Planning | Path/motion/task planning given the perceived state and goals |
| Control | Real-time execution of planned motion/actions, closing the feedback loop |
| Behavior / mission logic | Higher-level decision-making, task sequencing, often less real-time-critical |
| Safety supervisor | Independent monitoring layer that can override any other layer to reach a safe state |

The safety supervisor should be architecturally independent of the planning/behavior layers it can override — a safety system that depends on the same logic it's meant to guard against failing is not a safety system.

## Decision Rule

Choose middleware/compute architecture based on the real-time and safety requirements of the specific platform, not on what's trendy in the robotics community. A simple deterministic control loop on a microcontroller can be the right answer even when ROS 2 is the "expected" choice — see `reference/robotics-architecture-ros.md`.

## Reference Files

- `reference/robotics-architecture-ros.md` — ROS/ROS 2 architecture, middleware decision rules, and when a simpler embedded approach beats a full robotics framework.
- `reference/embedded-realtime-control.md` — real-time operating systems, control loop design, and embedded systems constraints.
- `reference/sensor-fusion-perception.md` — sensor fusion approaches, state estimation, and perception pipeline design.
