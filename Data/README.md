# Dataset

## Overview

This folder contains the synthetic chemical-compound dataset used for the **YUVAIntern Healthcare Data Science Internship** project.

The dataset was created to support the computational analysis of molecular descriptors and bioactivity prediction as part of the four-week project workflow.

## Dataset Description

The dataset contains **500 synthetic chemical compound records**, identified from `CMP1` to `CMP500`.

Each compound is described using the following molecular and chemical features:

| Feature            | Description                                              |
| ------------------ | -------------------------------------------------------- |
| `Compound_ID`      | Unique identifier for each synthetic compound            |
| `Molecular_Weight` | Molecular weight of the compound                         |
| `LogP`             | Lipophilicity-related molecular descriptor               |
| `HBA`              | Number of hydrogen-bond acceptors                        |
| `HBD`              | Number of hydrogen-bond donors                           |
| `TPSA`             | Topological polar surface area                           |
| `Rotatable_Bonds`  | Number of rotatable bonds                                |
| `Bioactivity`      | Synthetic bioactivity classification: Active or Inactive |

## Purpose

The dataset was used throughout the project to demonstrate a computational healthcare data science workflow involving:

* Data preprocessing and cleaning
* Exploratory data analysis (EDA)
* Molecular descriptor analysis
* Predictive modeling
* Bioactivity classification
* Model evaluation
* Data visualization and interpretation

The dataset therefore serves as the common data source for the analytical workflow developed during the internship.

## Data Type

This is a **synthetic dataset** generated for educational and research-training purposes.

It does **not** represent real patient data, clinical data, or experimentally measured bioactivity results.

## File

```text
synthetic_compounds.csv
```

The CSV file contains the 500 compound records and all molecular descriptor and bioactivity fields used in the project.

## Project Context

The dataset supports the implementation phase of the four-week YUVAIntern project, following the initial project proposal and providing the data foundation for subsequent exploratory analysis, predictive modeling, and visualization.

