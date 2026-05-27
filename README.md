# Objective Quality Evaluation of Point Clouds: Quality Features and Fusion Metrics

This repository contains the implementation and benchmarking framework for the paper:

> **Objective Quality Evaluation of Point Clouds: Quality Features and Fusion Metrics**

The work presents a comprehensive feature-level analysis of state-of-the-art full-reference point cloud quality metrics and proposes a novel fusion framework, named **Feature Selection Model (FSM)**, for objective point cloud quality assessment.

The proposed FSM combines the most relevant perceptual features extracted from existing metrics.

The best-performing configuration uses:

- PCQM features:
  - f2
  - f4
  - f5
  - f7

- GraphSIM:
  - mg

- PSNR MSE D2

with **Ridge Regression**.



Additional external metric implementations are required:
- PCQM
- PointSSIM
- MS-GraphSIM
- MPEG PCC tools

---

# Acknowledgements

This work was supported by:
- Instituto de Telecomunicações
- Universidade da Beira Interior
- FCT/MECI
- MultImagePCQ Project
