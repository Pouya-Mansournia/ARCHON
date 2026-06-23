---
name: archon-robotics
description: Ask ARCHON about robotics, embedded systems, or IoT architecture — ROS2, SLAM, sensor fusion, RTOS, fleet management, edge AI, safety.
argument-hint: "<robotics, embedded, or IoT architecture question>"
---

# /archon-robotics

Bias ARCHON's answer toward robotics, embedded systems, and IoT architecture.

## Usage

```
/archon-robotics $ARGUMENTS
```

## What Happens

ARCHON loads `skills/11_Robotics/` (robotics architecture, embedded systems, IoT architecture reference files) and answers using the standard Output Standard, with explicit attention to: real-time constraints, safety architecture (including fail-safe/fail-operational requirements), power budget, hardware-software co-design, OTA update strategy, and fleet-scale operational concerns.

## Example

```
/archon-robotics We're building a warehouse picking robot fleet. What's the right edge-compute vs cloud-compute split for perception and fleet coordination?
```

## Tips

- Specify whether this is a single prototype, a small fleet, or a production fleet at scale — the right answer differs enormously by stage (see `skills/11_Robotics/reference/robotics-architecture-ros.md` for stage-aware guidance).
- Mention any certification/safety requirements (e.g., ISO 13849, IEC 61508) upfront if applicable.
