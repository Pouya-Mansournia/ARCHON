# Example: `/archon-robotics` — ROS 2 vs. Bare Embedded for a Pick-and-Place Prototype

**Prompt:**

```
/archon-robotics We're prototyping a single-arm pick-and-place system. Should we build on ROS 2 or go straight to bare embedded code?
```

**Response:**

### What to Use

ROS 2 for the prototype phase, with an explicit plan to evaluate what (if anything) gets reimplemented for the production/real-time-critical path later.

### Why This Choice

At the prototype stage, the priority is iteration speed on perception and planning logic, not certification or minimal footprint. ROS 2 gives you Gazebo simulation, RViz visualization, and existing manipulation tooling (MoveIt) for free — building that tooling yourself on bare embedded code would be pure overhead that doesn't differentiate your actual pick-and-place logic. See `skills/11_Robotics/reference/robotics-architecture-ros.md`.

### Why Not the Alternatives

**Bare embedded from the start:** Would cost significant upfront engineering effort building visualization, simulation, and motion-planning infrastructure that ROS 2's ecosystem already provides — effort better spent validating whether the pick-and-place approach works at all. This is premature optimization for production constraints (determinism, certification, minimal footprint) that don't yet apply to a prototype.

**A custom lightweight pub/sub layer (e.g., Zenoh):** Reasonable for a production system stripping down a ROS-prototyped design, but adopting it at the prototyping stage forfeits ROS 2's tooling/ecosystem benefit for a footprint advantage that isn't yet relevant — there's no resource-constrained production hardware yet to justify it.

### Trade-Offs

Gaining: fast iteration via existing tooling and ecosystem packages. Giving up: ROS 2's DDS-based communication doesn't give the same worst-case-execution-time guarantees a hand-built real-time core would — acceptable for a prototype's R&D phase, not acceptable if any part of this system has a hard real-time safety requirement before you've evaluated and addressed that specifically.

### Risks

The main risk is QoS misconfiguration on safety-relevant topics (e.g., an e-stop command left at "best effort" reliability) — treat QoS as a deliberate per-topic decision, not a default left untouched. A second risk is shipping the full research-time ROS 2 stack unchanged to production hardware without evaluating what should be trimmed or reimplemented for the real-time-critical path.

### Cost Impact

Lower upfront engineering cost than building tooling from scratch on bare embedded code; the cost trade-off shifts at production scale if ROS 2's overhead becomes a genuine constraint on the target hardware.

### Scalability Impact

Sufficient for single-prototype and small-fleet R&D. Re-evaluate specifically for the production embedded platform — not because ROS 2 "doesn't scale," but because production hardware constraints (power, real-time guarantees, certification) are a different question than prototyping velocity.

### Security Impact

ROS 2's DDS-based discovery and communication has a stronger default security model than ROS 1, but don't assume it's hardened by default — review discovery/communication security settings before any networked deployment beyond a lab bench.

### Confidence Level

**High** for the prototype-phase recommendation itself (well-established pattern, strong consensus). **Medium** for what specifically should change at the production stage — that depends on the target hardware's actual real-time and certification requirements, which aren't yet specified.

### Migration Path

Prototype in ROS 2, leveraging Gazebo/RViz/MoveIt. Before committing to production hardware, explicitly evaluate three options for the real-time-critical control core: ship the ROS 2 stack as-is if profiling shows it meets your latency/determinism requirements, trim it to only the nodes/communication actually needed, or reimplement the safety-critical core in bare embedded/RTOS form while keeping ROS 2 for the non-time-critical behavior/mission layer.

---

*This response demonstrates how the Output Standard composes with domain-specific knowledge from `skills/11_Robotics/`, applied via `/archon-robotics` mode.*
