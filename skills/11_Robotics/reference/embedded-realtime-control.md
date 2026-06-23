# Embedded Systems & Real-Time Control

## Goal

Real-time control is the layer where "fast" and "correct" are the same requirement — a control loop that's usually fast enough but occasionally misses its deadline isn't a performance issue, it's a correctness failure that can destabilize a physical system.

## Hard Real-Time vs. Soft Real-Time

| Type | Definition | Consequence of missing a deadline |
|---|---|---|
| Hard real-time | A deadline that must never be missed | System failure, instability, potential physical harm (e.g., a motor control loop, a flight controller) |
| Soft real-time | A deadline that should usually be met, with graceful degradation if occasionally missed | Degraded quality of service, not catastrophic failure (e.g., a UI update, a non-critical telemetry log) |

Identify which category each control loop in the system actually belongs to — this determines whether it belongs on an RTOS/bare-metal real-time core or can tolerate a general-purpose OS's scheduling jitter.

## RTOS Selection

| RTOS | Best for |
|---|---|
| FreeRTOS | Resource-constrained microcontrollers, huge ecosystem/community, permissive licensing, the default starting point for most embedded real-time work |
| Zephyr | Modern, actively developed, strong driver/peripheral support breadth, good fit for connected/IoT embedded devices |
| VxWorks / QNX | Safety-/certification-critical systems (aerospace, automotive, medical) needing a commercially supported, certified RTOS with a long track record |
| Bare-metal (no RTOS) | The simplest single-loop control systems where an RTOS's task-scheduling overhead isn't needed at all |

## Control Loop Design Principles

- **Determinism over raw speed** — a control loop that takes a consistent 2ms every cycle is more valuable than one that averages 1ms but occasionally spikes to 10ms.
- **Bound worst-case execution time (WCET)**, not just average-case — real-time guarantees are about the worst case, and profiling only the average case hides the failures that matter.
- **Isolate the real-time-critical path from non-deterministic operations** — dynamic memory allocation, unbounded loops, and blocking I/O have no place inside a hard real-time loop; pre-allocate, bound all loops, and use non-blocking/asynchronous patterns for anything that can't complete deterministically.
- **Watchdog timers** to detect a hung/crashed control loop and force the system to a safe state rather than leaving it unresponsive in an unknown state.

## Power, Thermal & Resource Budgets

Embedded robotics platforms operate under hard constraints that cloud/server software rarely faces: limited battery capacity, thermal dissipation limits, and fixed compute/memory budgets that can't be elastically scaled. Architecture decisions (sensor sampling rates, on-device vs. offloaded compute, sleep/wake cycling) need to be evaluated against these budgets explicitly, not assumed to be "fast enough" based on desktop/cloud intuition.

## Safety-Critical Patterns

- **Fail-safe default state** — on any fault (sensor dropout, communication loss, watchdog timeout), the system should default to a known-safe state (motors off, brakes engaged) rather than continuing with stale/uncertain data.
- **Redundancy for safety-critical sensing** — critical state estimates (e.g., is a human in the workspace) should not depend on a single sensor with no cross-check.
- **Independent safety supervisor** (as noted in the parent SKILL.md) that can force a safe state regardless of what the primary control/planning logic is doing.

## Common Mistakes

- Using dynamic memory allocation or unbounded loops inside a hard real-time control path, introducing non-deterministic latency spikes.
- Profiling only average-case execution time and missing worst-case scenarios that occasionally blow the deadline.
- No watchdog timer, leaving a hung control loop silently unresponsive instead of forcing a safe state.
- Treating a single sensor's reading as ground truth for a safety-critical decision with no redundancy or sanity-checking.

## Decision Rule for This Domain

Classify every control loop as hard or soft real-time before choosing its execution environment. Put hard real-time loops on a real RTOS or bare-metal with bounded worst-case execution time, watchdogs, and a fail-safe default state — never on a general-purpose OS's best-effort scheduler.
