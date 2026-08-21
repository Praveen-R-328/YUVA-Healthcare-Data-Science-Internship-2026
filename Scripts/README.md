# Scripts

## Overview

This folder contains the Python scripts used to implement the computational workflow of the **YUVAIntern Healthcare Data Science Internship 2026** project.

The scripts cover the practical analysis performed during **Weeks 2–4**, including synthetic dataset generation, data cleaning and exploratory data analysis, predictive modeling, and data visualization.

Week 1 was focused on the project proposal and methodology, so no separate Python implementation script is included for Week 1.

## Scripts

### `data_generation.py`

Generates the synthetic chemical-compound dataset used in the project.

The script creates **500 synthetic compounds** with the following variables:

* Compound ID
* Molecular Weight
* LogP
* Hydrogen Bond Acceptors (HBA)
* Hydrogen Bond Donors (HBD)
* Topological Polar Surface Area (TPSA)
* Rotatable Bonds
* Bioactivity

The generated dataset is saved as:

`Data/synthetic_compounds.csv`

### `data_cleaning_eda.py`

Performs the Week 2 data-cleaning and exploratory-analysis workflow.

The script includes:

* Dataset inspection
* Missing-value checking
* Duplicate checking
* Descriptive statistics
* Molecular-weight distribution
* LogP distribution
* Bioactivity class distribution
* Correlation analysis
* Box-plot-based outlier inspection
* Molecular Weight vs LogP analysis

### `predictive_modeling.py`

Implements the Week 3 machine-learning workflow for bioactivity classification.

The script includes:

* Feature selection
* Training/testing split
* Feature standardization
* Logistic Regression
* Random Forest
* Support Vector Machine (SVM)
* Hyperparameter tuning using GridSearchCV
* 5-fold cross-validation
* Accuracy
* Precision
* Recall
* F1-score
* Confusion matrices
* ROC-AUC
* ROC curves

### `data_visualization.py`

Implements the Week 4 visualization workflow.

The script generates visualizations for:

* Molecular descriptor distributions
* Active vs inactive compound comparisons
* Correlation between molecular descriptors
* Pairwise relationships between molecular descriptors

## Technologies

The scripts use:

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

## Workflow

The scripts are intended to follow this sequence:

**Data Generation → Data Cleaning & EDA → Predictive Modeling → Data Visualization**

The same synthetic dataset is used as the common data source for the analysis scripts.

## Reproducibility

The scripts use a fixed random seed where applicable to support reproducibility of the synthetic dataset and computational workflow.

The dataset used in this project is synthetic and intended for educational and training purposes. It does not represent experimentally validated bioactivity data or real patient information.

The weekly reports document the results obtained during the internship, while the scripts in this repository provide the corresponding computational workflow.

## Project Context

These scripts form the computational component of the four-week YUVAIntern project and complement the weekly reports, dataset, visualizations, and results included elsewhere in this repository.

