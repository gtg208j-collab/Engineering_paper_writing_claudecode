# Draft Plan

## Research Configuration

- **Working title:** Communication-Aware Decentralized Artificial Potential Field Control for Multi-UAV Formation and Collision Avoidance
- **Target journal:** IEEE/ASME Transactions on Mechatronics (provisional)
- **Journal family:** IEEE
- **Paper type:** Algorithm and experimental validation

## Key Message

A decentralized artificial potential field controller can coordinate quadrotor formation motion and collision avoidance using local position information. Incorporating communication range, neighbor limits, packet loss, transmission period, and stochastic delay into the swarm model enables evaluation of how communication conditions affect formation and collision-avoidance behavior; a delay-dependent velocity suppression rule is then examined in simulation and indoor flight tests.

## Research Problem

Multi-UAV formation control must maintain a desired formation while avoiding obstacles and inter-UAV collisions. In a decentralized implementation, each vehicle relies on locally exchanged information that may be delayed, lost, or limited by communication range and neighbor capacity. The draft will formulate this problem for quadrotor UAVs whose low-level attitude dynamics are assumed to track attitude setpoints sufficiently quickly for the formation controller to generate velocity commands.

## Candidate Contributions

1. A decentralized artificial potential field framework that combines goal-formation attraction, obstacle repulsion, and inter-UAV repulsion for formation motion and collision avoidance.
2. A communication-aware swarm simulation model with communication range, maximum neighbor count, packet-loss probability, transmission period, and stochastic transmission delay.
3. A delay-dependent velocity-suppression rule and a connectivity-informed repulsion adjustment intended to reduce collision risk when communication quality degrades.
4. Indoor quadrotor demonstrations of known-obstacle avoidance and circular formation generation using motion-capture feedback.

> These are candidate contributions. They must be narrowed and supported by literature and result files before submission. No numerical improvement claim is made because the supplied presentation does not provide a complete baseline dataset.

## Claim-to-Evidence Mapping

| Claim | Evidence currently available | Required before final draft |
|---|---|---|
| APF combines attraction and repulsion for formation and obstacle avoidance | Presentation slides on APF formulation and formation structure | Formal derivation, parameter definitions, citations |
| Communication variables affect swarm behavior | Presentation simulations varying communication period, delay, packet loss, and connectivity | Raw simulation data, repeated trials, metrics |
| Delay-dependent velocity suppression can reduce collision risk | Presentation comparison of velocity suppression enabled/disabled | Collision-rate and safety-distance data, baseline definition |
| Indoor experiments demonstrate obstacle avoidance and circular formation | Presentation indoor test architecture and images | Time histories, tracking-error metrics, experiment protocol |

## Source-Reported Results to Reflect in Draft

- Communication rate of 1 packets/s: 6 collisions and 58 warnings in the reported example.
- Communication rate of 0.5 packets/s: 242 collisions and 373 warnings in the reported example.
- Cluster packet-loss rates for the listed `CWmin` settings: 4.45%, 4.20%, and 4.16%.
- Circle packet-loss rates for the listed `CWmin` settings: 2.84%, 2.61%, and 2.52%.
- Cluster average delays: 167, 680, and 1130 microseconds; maximum delays: 2031, 8270, and 13439 microseconds.
- Circle average delays: 146, 287, and 429 microseconds; maximum delays: 18090, 48603, and 48796 microseconds.
- Indoor tests show known-obstacle avoidance and a circle formation at 1 m altitude with 2 m target radius.

These values are presentation-reported observations. Raw logs, trial counts, definitions, and uncertainty estimates are required before generalizing them as validated performance claims.

## Proposed Paper Structure

1. **Introduction:** Multi-UAV formation-control motivation, decentralized communication challenge, APF background, research gap, contributions.
2. **Related Work:** Decentralized swarm control, APF formation control, communication-aware multi-agent control, collision avoidance.
3. **Problem Formulation:** Quadrotor abstraction, local position exchange, formation objective, obstacle and collision constraints, communication model.
4. **Communication-Aware APF Controller:** Goal-formation attraction, obstacle repulsion, inter-UAV repulsion, communication-aware velocity suppression, connectivity-aware adjustment.
5. **Simulation Study:** Baseline 25-UAV triangular formation, communication-period study, delay study, packet-loss study, connectivity study.
6. **Indoor Experiments:** Motion-capture and companion-computer architecture, obstacle avoidance, circular formation at 1 m altitude with 2 m radius.
7. **Discussion:** Safety, scalability, decentralization limitations, local-minimum issue, and assumptions.
8. **Conclusion:** Evidence-supported findings and future work.

## Figures and Tables

- **Fig. 1:** Overall communication-aware decentralized APF architecture.
- **Fig. 2:** APF components: formation attraction, obstacle repulsion, and inter-UAV repulsion.
- **Fig. 3:** Communication model and packet-delay/loss abstraction.
- **Fig. 4:** 25-UAV triangular formation simulation.
- **Fig. 5:** Effect of communication period on formation and collision behavior.
- **Fig. 6:** Velocity suppression as a function of communication delay.
- **Fig. 7:** Indoor experimental system architecture.
- **Fig. 8:** Obstacle-avoidance experiment.
- **Fig. 9:** Circular formation experiment.
- **Table I:** Controller and communication parameters.
- **Table II:** Simulation metrics and results for each communication condition.
- **Table III:** Indoor experiment metrics.

## Required Inputs Before Full Manuscript Drafting

- Verified literature and entries in `knowledge/evidence.md`.
- Complete mathematical definitions in `method/notation.md`.
- Simulation plan and user approval in `simulation/sim_plan.md`.
- Raw simulation results in CSV format.
- Experimental plan and user approval in `experiment/exp_plan.md`.
- Time-series experimental data and tracking/safety metrics.
- Explicit baseline methods and comparison protocol in `comparison/baselines.md`.
- Confirmation of the target journal and author list.

## Approval

- [x] 사용자 승인 완료
