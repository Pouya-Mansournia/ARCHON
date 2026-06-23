# Robotics Middleware: ROS/ROS 2 & Alternatives

## Goal

ROS 2 is the dominant framework in robotics research and an increasingly common industry default — but "dominant" doesn't mean "always right." Choose middleware based on the platform's actual real-time requirements, team expertise, certification needs, and product constraints.

## Middleware / Framework Decision Matrix

| Option | Best for | Avoid when |
|---|---|---|
| ROS 2 | Multi-node systems needing rich tooling (visualization, simulation via Gazebo/Ignition, large package ecosystem), teams building on top of existing ROS packages (navigation stacks, MoveIt for manipulation) | Hard real-time deadlines tighter than ROS 2's DDS-based communication reliably guarantees without careful QoS tuning, or a simple single-loop embedded system where ROS's overhead isn't earning its keep |
| Bare embedded (RTOS or bare-metal, no robotics framework) | Tight real-time control loops, resource-constrained microcontrollers, safety-certified systems where framework overhead/complexity works against certification | Complex multi-sensor, multi-behavior systems where hand-rolling all the coordination ROS provides for free becomes its own maintenance burden |
| Custom lightweight pub/sub (e.g., Zenoh, custom DDS usage) | Teams wanting some of ROS's decoupling benefits without its full tooling/dependency footprint, often in production deployments that strip down a ROS-prototyped system | Early-stage prototyping where ROS's tooling/ecosystem accelerates development more than the lighter footprint would help |

## ROS 1 vs. ROS 2

ROS 2 is the right choice for any new system — it addresses ROS 1's lack of real-time support, single point of failure (the ROS master), and weak security model by building on DDS (Data Distribution Service) for discovery and communication. There is no good reason to start a new project on ROS 1 today.

## Quality of Service (QoS) in ROS 2 — Why It Matters

DDS-based communication in ROS 2 exposes QoS policies (reliability, durability, history depth) per topic. Getting this wrong is a common source of subtle bugs: using "best effort" reliability for safety-critical commands, or "keep last 1" history for data a late-joining subscriber needs the history of. Treat QoS configuration as a deliberate design decision per topic, not a default left untouched.

## The Prototype-to-Production Path

A common, often correct pattern: prototype perception/planning logic in ROS 2 (leveraging Gazebo simulation, RViz visualization, existing navigation/manipulation packages) to move fast during R&D, then for the production embedded platform, evaluate whether the full ROS 2 stack should ship as-is, get slimmed down to the specific nodes/communication actually needed, or get reimplemented in a lighter-weight/bare-metal form for the safety-critical real-time core while keeping ROS 2 for the less time-critical behavior/mission layer.

## Common Mistakes

- Defaulting to ROS 2 for a single-loop embedded controller where a simple RTOS task structure would be simpler, more deterministic, and easier to certify.
- Leaving QoS policies at default settings without considering whether "best effort" delivery is acceptable for that specific topic's role (e.g., an e-stop command should never be best-effort).
- Shipping the full research-time ROS 2 stack to a resource-constrained production platform without evaluating what can be trimmed or replaced for the real-time-critical path.
- Treating the ROS master/discovery layer as infinitely reliable in ROS 1-style thinking carried over into ROS 2 designs, without testing network-partition/discovery-failure behavior.

## Decision Rule for This Domain

Default to ROS 2 for multi-node systems benefiting from its tooling and ecosystem, especially during R&D/prototyping. For the real-time-critical control core of a production platform, evaluate a bare embedded/RTOS approach on its own merits rather than assuming the framework used for prototyping is the right choice for the certified production path.
