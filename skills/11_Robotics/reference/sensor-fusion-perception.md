# Sensor Fusion & Perception

## Goal

No single sensor gives a robot a complete or perfectly accurate picture of the world — perception architecture exists to combine noisy, partial, sometimes-conflicting sensor data into a state estimate the planning and control layers can act on with known confidence.

## Common Sensor Modalities

| Sensor | Strength | Weakness |
|---|---|---|
| Camera (RGB) | Rich semantic information (object recognition, color, texture) | No direct depth, sensitive to lighting conditions |
| LiDAR | Accurate direct depth/distance, works in low light | Expensive, lower resolution than camera for fine texture/semantic detail, can struggle with certain weather (rain, fog) |
| IMU (Inertial Measurement Unit) | High-frequency orientation/acceleration data, works regardless of lighting | Drifts over time without correction from another sensor |
| Wheel/motor encoders | Direct, cheap odometry estimate | Drifts with wheel slip, doesn't capture true position in the world frame |
| GPS/GNSS | Absolute position in the world frame | Low update rate, poor/unavailable indoors or in dense urban/forest environments, meter-level accuracy at best without augmentation |
| Ultrasonic/IR proximity | Cheap, simple short-range obstacle detection | Low resolution, narrow field of view, limited range |

## Why Fusion Is Necessary

Each sensor modality's weaknesses are often complementary to another's strengths — an IMU's drift can be corrected by periodic GPS or visual odometry fixes; a camera's lack of direct depth can be supplemented by LiDAR; wheel-encoder drift from slip can be cross-checked against IMU and visual odometry. Fusion combines these complementary strengths into a state estimate more accurate and more robust to individual sensor failure than any single source.

## Fusion Approaches

| Approach | How it works | Use when |
|---|---|---|
| Kalman Filter (KF) / Extended Kalman Filter (EKF) | Recursive estimator combining a motion model prediction with sensor measurement updates, weighted by their respective uncertainties | The classic, well-understood default for state estimation (position, velocity, orientation) — most robotics localization stacks (e.g., ROS 2's `robot_localization` package) are EKF/UKF-based |
| Unscented Kalman Filter (UKF) | Like EKF but handles strong non-linearities in the motion/measurement model more accurately | The system's dynamics are significantly non-linear and EKF's linearization introduces meaningful error |
| Particle Filter | Represents the state estimate as a set of weighted samples (particles) rather than a single Gaussian | Multi-modal uncertainty (e.g., global localization with multiple plausible positions) that a Kalman filter's single-Gaussian assumption can't represent |
| Learned/deep-learning-based fusion | A neural network learns to combine raw sensor inputs directly | Complex perception tasks (object detection/tracking from camera + LiDAR) where hand-engineered models are insufficient — common in modern autonomous vehicle perception stacks |

**Decision rule:** Start with an EKF/UKF-based approach for core state estimation (position, velocity, orientation) — it's well-understood, computationally cheap, and has mature tooling. Reach for particle filters when uncertainty is genuinely multi-modal, and reach for learned fusion approaches specifically for high-level perception tasks (object detection/classification) rather than as a default replacement for classical state estimation.

## Designing for Sensor Failure

Perception architecture should treat sensor dropout/failure as an expected event, not an exception: detect when a sensor's data is stale, out of expected range, or internally inconsistent; degrade gracefully to remaining sensors' estimate (with appropriately increased uncertainty) rather than either trusting clearly-bad data or halting entirely; and surface degraded-confidence states to the planning/safety layers so they can respond appropriately (e.g., slow down, request human intervention).

## Common Mistakes

- Trusting a single sensor's raw output as ground truth for a critical state estimate with no fusion or cross-checking.
- Using an EKF on a system with strongly non-linear dynamics without evaluating whether the linearization error is acceptable, when a UKF would have been a better fit.
- No explicit handling of sensor dropout/failure — the system either silently uses stale data or fails ungracefully.
- Treating perception output as perfectly certain in downstream planning logic, rather than propagating and reasoning about the actual confidence/uncertainty of the estimate.

## Decision Rule for This Domain

Fuse complementary sensor modalities rather than relying on any single source for critical state estimates. Start with EKF/UKF for core localization/state estimation, escalate to particle filters or learned approaches only for specific needs (multi-modal uncertainty, complex semantic perception) those simpler approaches don't address. Always design explicitly for sensor degradation and failure.
