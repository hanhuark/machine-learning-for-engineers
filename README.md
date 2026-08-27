# Machine Learning for Engineers

> **Originating implementation:** [MEEG 54403: Machine Learning for Mechanical Engineers](https://mechanical-engineering.uark.edu/) at the University of Arkansas. The course is ongoing; this repository is designed for that course and for adaptation by other engineering programs.

An open, project-based curriculum for learning to formulate, build, verify, and critique machine-learning workflows for physical engineering systems. It is intended for upper-level undergraduate and graduate students, instructors adapting individual modules, and engineers building stronger data-driven analysis habits.

**Start with the [course gateway](docs/index.md),** choose a module from the map below, and use the [adoption guide](ADOPTION_GUIDE.md) to adapt it responsibly.

See [IMPLEMENTATIONS.md](IMPLEMENTATIONS.md) for the originating course and a transparent record of confirmed implementations as the curriculum is adopted elsewhere.

The course uses Python tutorials as the primary reproducible pathway. MATLAB tutorials remain available where supplied, including a direct [MATLAB Online launch](https://matlab.mathworks.com/open/github/v1?repo=hanhuark/machine-learning-for-engineers), but new course development should not assume students have access to proprietary software.

## What students learn

- translate an engineering question into inputs, labels, assumptions, and appropriate metrics;
- construct and test regression, classification, clustering, computer-vision, sequence-learning, reinforcement-learning, and physics-informed models;
- identify leakage, domain shift, model-form error, and failure cases;
- connect model outputs to physical quantities, limits, and engineering decisions;
- use generative-AI tools responsibly while independently verifying their outputs;
- design and audit bounded AI-agent harnesses for engineering workflows;
- communicate reproducible, evidence-bounded technical conclusions.

## Course map

| Module | Engineering question and core methods | Primary learning evidence |
| --- | --- | --- |
| [I. Regression](course_content/i_regression/) | Predict a continuous engineering outcome; baselines, cross-validation, residuals | Valid time-aware split, model comparison, error analysis |
| [II. Classification](course_content/ii_classification/) | Sort nuts and bolts from images; CNNs and deployment constraints | Grouped split, robustness/failure analysis, deployment test |
| [III. Dimensionality reduction and clustering](course_content/iii_dimensionality_reduction_and_clustering/) | Extract structure from boiling images; PCA/SVD and clustering | Reconstruction, stability, physical interpretation |
| [IV. Segmentation and object detection](course_content/iv_segmentation_and_object_detection/) | Identify bubbles and objects; U-Net, YOLO, transfer learning | Held-out condition performance, visual error audit |
| [V. Reinforcement learning](course_content/v_reinforcement_learning/) | Make bounded sequential decisions; Q-learning and policy evaluation | Baseline policy, constraint audit, perturbed-condition evaluation |
| [VI. Generative models and inverse engineering design](course_content/vi_generative_models/) | Evaluate synthetic/reconstructed data and design candidates under physical constraints | **Under development**; not yet a current assignment |
| [VII. Time-series forecasting and prognostics](course_content/vii_time_series_forecasting/) | Forecast boiling dynamics; sequence-to-sequence RNN/GRU/LSTM candidates | **Validation refresh required** before graded use |
| [VIII. Physics-informed neural networks](course_content/viii_physics_informed_neural_networks/) | Solve and invert transient heat conduction; PINNs | Analytical/numerical verification, inverse estimate, failure audit |
| [IX. AI agent harnesses](course_content/ix_ai_agent_harnesses/) | Constrain and verify AI-assisted engineering workflows; skills, MCP, and plugins | Harness specification, independent verification, failure audit, individual defense |

See [COURSE_MAP.md](COURSE_MAP.md) for prerequisites, suggested sequencing, and instructor-facing assessment checkpoints.
See [CURRICULUM_ARCHITECTURE.md](CURRICULUM_ARCHITECTURE.md) for the module-readiness review, decisions on module boundaries, and the planned industrial-AI roadmap.

## Start here

1. Read the relevant module README and its data-access instructions.
2. Use the tutorial as a guided learning resource, not as a finished assessment submission.
3. Complete the current assignment specification and document assumptions, data provenance, validation, and limitations.
4. Run the module's documented environment and tests when they are provided.

The [prerequisites](prerequisites/) folder includes a Visual Studio Code introduction. The [project gallery](project_examples/) contains student-contributed examples shared with permission.

## Assessment and generative AI

This repository does not rely on AI detection as evidence of learning. Current assignments should distinguish AI-free foundational checks, permitted AI-assisted work, and AI-audited tasks. Students remain responsible for every submitted result and must be able to explain and modify their work.

Use:

- [assessment policy](teaching_resources/ASSESSMENT_AND_AI_POLICY.md) for course-level expectations;
- [AI-use record template](teaching_resources/AI_USE_TEMPLATE.md) for AI-assisted work;
- [shared rubric](teaching_resources/ENGINEERING_ML_RUBRIC.md) for grading;
- [current Homework 1 specification](course_content/i_regression/ASSIGNMENT_AI_RESILIENT.md), [current Homework 2 specification](course_content/ii_classification/ASSIGNMENT_AI_RESILIENT.md), [current structure-discovery specification](course_content/iii_dimensionality_reduction_and_clustering/ASSIGNMENT_AI_RESILIENT.md), and [current visual-measurement specification](course_content/iv_segmentation_and_object_detection/ASSIGNMENT_AI_RESILIENT.md).

Legacy PDF/DOCX assignments remain available for historical context. Instructors should identify the current assessment version and keep answer keys, rubrics, and instructor-held test data outside the public repository.

## Reproducibility and data use

Each module should state data provenance, evidence class, units, split rules, licenses/permissions, and limitations. The [data-card template](teaching_resources/DATA_CARD_TEMPLATE.md) and [reproducibility checklist](teaching_resources/REPRODUCIBILITY_CHECKLIST.md) provide the common standard. The PINN module demonstrates this pattern with synthetic data, metadata, deterministic generation, and tests.

Do not upload student records, unpublished data, confidential sponsor data, restricted datasets, or material without redistribution permission.

## Cite this curriculum

If this curriculum, its modules, or substantial adapted material informs a publication, course design, or other scholarly work, please cite the curriculum paper:

> C. Li, H. Hu, C. Dunlap, N. House, and J. Wai, “Giving Mechanical Engineers Intelligent Tools: A Project-Based AI Education Curriculum in Thermal Engineering,” *arXiv:2608.26056* [cs.CY], 2026. https://doi.org/10.48550/arXiv.2608.26056

```bibtex
@article{li2026giving,
  title = {Giving Mechanical Engineers Intelligent Tools: A Project-Based AI Education Curriculum in Thermal Engineering},
  author = {Li, Changgen and Hu, Han and Dunlap, Christy and House, Nathaniel and Wai, Jonathan},
  year = {2026},
  eprint = {2608.26056},
  archivePrefix = {arXiv},
  primaryClass = {cs.CY},
  doi = {10.48550/arXiv.2608.26056},
  url = {https://arxiv.org/abs/2608.26056}
}
```

This is a request for scholarly attribution, not a condition of the [BSD 3-Clause License](LICENSE). The repository's machine-readable metadata, including this preferred citation, is in [CITATION.cff](CITATION.cff).

## For instructors and adopters

- [Instructor guide](INSTRUCTOR_GUIDE.md): suggested pacing, assessment design, and operating boundaries.
- [Adoption guide](ADOPTION_GUIDE.md): how to use one or more modules in another course.
- [Contributing guide](CONTRIBUTING.md): how to suggest corrections or improvements.
- [Citation metadata](CITATION.cff): preferred scholarly citation and repository metadata.

## Acknowledgments and evidence of impact

The course was developed by [Han Hu](https://engineering.uark.edu/directory/index/uid/hanhu/name/Han+Hu/) and [Christy Dunlap](https://cldunlap73.github.io/) in the [Department of Mechanical Engineering](https://mechanical-engineering.uark.edu/) at the University of Arkansas. Course development has been supported by the department, the Arkansas NSF EPSCoR DART Project, and the MathWorks Curriculum Development Support program. Experimental datasets and instructional material were prepared with contributions acknowledged in the module materials.

Related educational and project outcomes are listed below as context. The course's mechanical-engineering integration, real data, peer review, and project work are deliberate parts of its learning design.

## Related course and project outcomes

These papers are contextual course and project outcomes, not the requested citation for reuse or adaptation of this repository; please use the curriculum paper above.

### Course/project outcomes

- [J. K. Hoskins, H. Hu, and M. Zou, “Exploring Machine Learning and Machine Vision in Femtosecond Laser Machining,” ASME Open Journal of Engineering, 2023.](https://asmedigitalcollection.asme.org/openengineering/article/doi/10.1115/1.4063646/1169944/Exploring-Machine-Learning-and-Machine-Vision-in)
- [A. C. Iradukunda et al., “Toward Direct Cooling in High Voltage Power Electronics,” IEEE TCPMT, 2024.](https://ieeexplore.ieee.org/abstract/document/10443930)
- [C. Dunlap, H. Pandey, and H. Hu, “Supervised and Unsupervised Learning Models for Detection of Critical Heat Flux during Pool Boiling,” ASME HT, 2022.](https://asmedigitalcollection.asme.org/HT/proceedings/HT2022/85796/V001T08A004/1146566)
- [L. M. Jr, D. Jensen, and H. Hu, “Supporting Condition-Based Maintenance for Rotary Systems Under Multiple Fault Scenarios,” ASME IDETC/CIE, 2023.](https://asmedigitalcollection.asme.org/IDETC-CIE/proceedings/IDETC-CIE2023/87295/V002T02A075/1170350)

### Educational papers

- [H. Hu and C. Heo, “Integration of Data Science Into Thermal-Fluids Engineering Education,” ASME IMECE, 2022.](https://asmedigitalcollection.asme.org/IMECE/proceedings/IMECE2022/86694/V007T09A023/1157305)
- [Y. Xu, B. Zhao, S. Tung, and H. Hu, “Infusing Data Science into Mechanical Engineering Curriculum with Course-Specific Machine Learning Modules,” ASEE, 2023.](https://peer.asee.org/infusing-data-science-into-mechanical-engineering-curriculum-with-course-specific-machine-learning-modules)

## License

This repository is released under the [BSD 3-Clause License](LICENSE).
