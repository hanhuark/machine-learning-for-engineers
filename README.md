# MEEG-44403/54403: Machine Learning for Mechanical Engineers

An open, engineering-first curriculum for learning to formulate, build, verify, and critique machine-learning workflows using mechanical-engineering data and systems. It is intended for upper-level undergraduate and graduate students, instructors adapting individual modules, and engineers building stronger data-driven analysis habits.

The course uses Python tutorials as the primary reproducible pathway. MATLAB tutorials remain available where supplied, including a direct [MATLAB Online launch](https://matlab.mathworks.com/open/github/v1?repo=hanhuark/MEEG-54403), but new course development should not assume students have access to proprietary software.

## What students learn

- translate an engineering question into inputs, labels, assumptions, and appropriate metrics;
- construct and test regression, classification, clustering, computer-vision, sequence-learning, reinforcement-learning, and physics-informed models;
- identify leakage, domain shift, model-form error, and failure cases;
- connect model outputs to physical quantities, limits, and engineering decisions;
- use generative-AI tools responsibly while independently verifying their outputs;
- communicate reproducible, evidence-bounded technical conclusions.

## Course map

| Module | Engineering question and core methods | Primary learning evidence |
| --- | --- | --- |
| [I. Regression](course_content/i_regression/) | Predict a continuous engineering outcome; baselines, cross-validation, residuals | Valid time-aware split, model comparison, error analysis |
| [II. Classification](course_content/ii_classification/) | Sort nuts and bolts from images; CNNs and deployment constraints | Grouped split, robustness/failure analysis, deployment test |
| [III. Dimensionality reduction and clustering](course_content/iii_dimensionality_reduction_and_clustering/) | Extract structure from boiling images; PCA/SVD and clustering | Reconstruction, stability, physical interpretation |
| [IV. Segmentation and object detection](course_content/iv_segmentation_and_object_detection/) | Identify bubbles and objects; U-Net, YOLO, transfer learning | Held-out condition performance, visual error audit |
| [V. Advanced topics](course_content/v_reinforcement_learning/) | Explore reinforcement learning, generative models, or sequence prediction | Hypothesis, baseline, controlled evaluation, defense |
| [VI. Physics-informed neural networks](course_content/vi_physics_informed_neural_networks/) | Solve and invert transient heat conduction; PINNs | Analytical/numerical verification, inverse estimate, failure audit |

See [COURSE_MAP.md](COURSE_MAP.md) for prerequisites, suggested sequencing, and instructor-facing assessment checkpoints.

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
- [current Homework 1 specification](course_content/i_regression/ASSIGNMENT_AI_RESILIENT.md) and [current Homework 2 specification](course_content/ii_classification/ASSIGNMENT_AI_RESILIENT.md).

Legacy PDF/DOCX assignments remain available for historical context. Instructors should identify the current assessment version and keep answer keys, rubrics, and instructor-held test data outside the public repository.

## Reproducibility and data use

Each module should state data provenance, evidence class, units, split rules, licenses/permissions, and limitations. The [data-card template](teaching_resources/DATA_CARD_TEMPLATE.md) and [reproducibility checklist](teaching_resources/REPRODUCIBILITY_CHECKLIST.md) provide the common standard. The PINN module demonstrates this pattern with synthetic data, metadata, deterministic generation, and tests.

Do not upload student records, unpublished data, confidential sponsor data, restricted datasets, or material without redistribution permission.

## For instructors and adopters

- [Instructor guide](INSTRUCTOR_GUIDE.md): suggested pacing, assessment design, and operating boundaries.
- [Adoption guide](ADOPTION_GUIDE.md): how to use one or more modules in another course.
- [Contributing guide](CONTRIBUTING.md): how to suggest corrections or improvements.
- [Citation metadata](CITATION.cff): how to cite this repository.

## Acknowledgments and evidence of impact

The course was developed by [Han Hu](https://engineering.uark.edu/directory/index/uid/hanhu/name/Han+Hu/) and [Christy Dunlap](https://cldunlap73.github.io/) in the [Department of Mechanical Engineering](https://mechanical-engineering.uark.edu/) at the University of Arkansas. Course development has been supported by the department, the Arkansas NSF EPSCoR DART Project, and the MathWorks Curriculum Development Support program. Experimental datasets and instructional material were prepared with contributions acknowledged in the module materials.

Related educational and project outcomes are listed below. The course's mechanical-engineering integration, real data, peer review, and project work are deliberate parts of its learning design.

## Related publications and project outcomes

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
