# Literature map: AI, thermal monitoring, and digital twins for power electronics

## Scope and reading position

This map supports a teaching studio on power-semiconductor and converter thermal-state estimation. It is an annotated map, not a systematic review or a claim that all approaches are interchangeable. The central distinction is between (1) a learned predictor, (2) a calibrated state estimator, and (3) a synchronized representation that supports a bounded decision.

## What the literature establishes

### AI tasks across the converter lifecycle

Zhao, Blaabjerg, and Wang organize AI applications in power electronics across design, control, and maintenance and across optimization, classification, regression, and data-structure tasks. That framing prevents the course from treating a neural network as a goal in itself: students should start with the engineering decision and then select a task, measurements, baseline, and evaluation boundary. [Zhao et al., 2021](https://doi.org/10.1109/TPEL.2020.3024914)

### Digital twin is stronger than a fitted surrogate

Recent power-electronics reviews describe digital-twin work spanning model construction, communication, synchronization, monitoring, control, and lifecycle use. They also identify open demands in real-time behavior, multiphysics coupling, fidelity, data quality, and deployment. Therefore this course uses the evidence ladder in the studio README: an offline regression result is a model result; it becomes a digital-twin claim only when the data connection, state definition, decision use, and validation justify that stronger language. [Wu et al., 2025](https://doi.org/10.1109/TPEL.2025.3570638); [Ba et al., 2023](https://doi.org/10.1109/MIE.2022.3216719); [Bai et al., 2024](https://doi.org/10.1109/MELE.2024.3423111)

### Thermal state estimation connects physics, sensing, and reliability

Junction temperature matters because thermal cycling and temperature-dependent behavior affect device operation and lifetime. Measurement and inference routes include direct/optical sensing, temperature-sensitive electrical parameters, thermal RC models, observers, and learned signal representations. Each has a different reference target, bandwidth, calibration requirement, and error mode. A course case must never compare estimates without naming the reference measurement and the relevant operating envelope. [Szczepański et al., 2023](https://doi.org/10.3390/mi14081636); [Ciappa et al., 2021](https://doi.org/10.3390/electronics10060683)

### Hybrid and real-time demonstrations are relevant, but do not remove validation duties

Published examples include a real-time digital-twin approach for three-phase converter condition monitoring, thermal-parameter identification for power modules, and a Nature Communications demonstration of a digital twin for DC-DC converter monitoring/control. These examples motivate the studio, but their validation systems, sensor sets, model structures, and decision objectives are not interchangeable. A student must not import a reported accuracy into another topology or laboratory. [Nele et al., 2023](https://doi.org/10.1016/j.apenergy.2022.120606); [Kuprat et al., 2024](https://doi.org/10.1109/JESTPE.2023.3328219); [Lei et al., 2023](https://doi.org/10.1038/s41467-023-41248-z)

## Teaching-to-evidence map

| Engineering question | Appropriate first model | Required comparison | Independent holdout | Do not claim |
| --- | --- | --- | --- | --- |
| What temperature follows a known loss profile? | Lumped RC balance or ARX | Persistence and RC/thermal-resistance baseline | Ambient/cooling or load profile | Device-specific $T_j$ accuracy from generic simulation |
| Can waveforms estimate a calibrated temperature? | Regression/CNN using defined waveform features | Temperature-sensitive parameter or observer | Device/campaign/operating condition | Transfer across packages or aging states without evidence |
| Can the system warn about thermal risk? | Calibrated estimator plus threshold | Existing protection/threshold rule | Near-limit and transient events | Safety qualification from mean error only |
| Can a virtual representation support a control action? | Hybrid state estimator with synchronized telemetry | Existing controller/observer | Full operating scenario and fault cases | A bidirectional twin without latency, safety, and action validation |

## Candidate data path and unresolved items

The course currently uses only the transparent simulated thermal-RC fixture. A contributor-owned waveform/thermal study is a promising future source, but the public case remains blocked until the device topology, target-reference construction, measurement calibration, independent split, safety plan, and redistribution permission are reviewed. No private study data are copied here.

## Reading list

1. Zhao, Z.; Blaabjerg, F.; Wang, H. *An Overview of Artificial Intelligence Applications for Power Electronics.* IEEE Transactions on Power Electronics, 2021. https://doi.org/10.1109/TPEL.2020.3024914
2. Wu, J. et al. *An Overview of Digital Twin Technology for Power Electronics: State-of-the-Art and Future Trends.* IEEE Transactions on Power Electronics, 2025. https://doi.org/10.1109/TPEL.2025.3570638
3. Ba, X. et al. *Digital Twin Techniques for Power Electronics-Based Energy Conversion Systems: A Survey of Concepts, Application Scenarios, Future Challenges, and Trends.* IEEE Industrial Electronics Magazine, 2023. https://doi.org/10.1109/MIE.2022.3216719
4. Bai, H. et al. *Digital Twins for Modern Power Electronics: An investigation into the enabling technologies and applications.* IEEE Electrification Magazine, 2024. https://doi.org/10.1109/MELE.2024.3423111
5. Nele, L. et al. *A real-time digital twin approach on three-phase power converters applied to condition monitoring.* Applied Energy, 2023. https://doi.org/10.1016/j.apenergy.2022.120606
6. Kuprat, M. et al. *Thermal Digital Twin of Power Electronics Modules for Online Thermal Parameter Identification.* IEEE Journal of Emerging and Selected Topics in Power Electronics, 2024. https://doi.org/10.1109/JESTPE.2023.3328219
7. Lei, Y. et al. *Digital twin for DC-DC converters.* Nature Communications, 2023. https://doi.org/10.1038/s41467-023-41248-z
8. Szczepański, A. et al. *Junction Temperature Optical Sensing Techniques for Power Switching Semiconductors: A Review.* Micromachines, 2023. https://doi.org/10.3390/mi14081636
9. Ciappa, M. et al. *Two Decades of Condition Monitoring Methods for Power Devices.* Electronics, 2021. https://doi.org/10.3390/electronics10060683

Before using any paper's figures, data, code, or supplementary files in course materials, check the original license and obtain any needed authorization.
