# Results

## Overview

This folder contains the key outputs generated from the computational analysis performed during **Weeks 2–4** of the YUVAIntern Healthcare Data Science Internship 2026.

The results cover:

* **Week 2:** Data Cleaning and Exploratory Data Analysis
* **Week 3:** Predictive Modeling and Evaluation
* **Week 4:** Data Visualization and Interpretation

Week 1 focused on project proposal and methodology development and therefore does not contain computational results.

## Week 2 – Data Cleaning and Exploratory Data Analysis

The Week 2 analysis focused on examining and understanding a synthetic dataset of **500 chemical compounds**.

The analysis included:

* Dataset inspection
* Missing-value checking
* Duplicate checking
* Descriptive statistical analysis
* Molecular Weight distribution
* LogP distribution
* Bioactivity class distribution
* Correlation analysis
* Box-plot-based outlier inspection
* Molecular Weight vs LogP analysis

The exploratory analysis provided an initial understanding of the molecular descriptors and bioactivity classes and established the dataset for subsequent predictive modeling and visualization.

## Week 3 – Predictive Modeling

Three machine-learning classification models were evaluated for chemical-compound bioactivity classification:

* Logistic Regression
* Random Forest
* Support Vector Machine (SVM)

The reported results identified **Random Forest as the best-performing model based on F1-score**.

### Reported Model Results

| Model               |     Accuracy |    Precision |       Recall |     F1-score | ROC-AUC |
| ------------------- | -----------: | -----------: | -----------: | -----------: | ------: |
| Logistic Regression |        0.640 | Not reported | Not reported | Not reported |  0.7456 |
| Random Forest       |        0.680 |       0.6731 |        0.700 |       0.6863 |  0.7424 |
| SVM                 | Not reported | Not reported | Not reported | Not reported |  0.7448 |

Logistic Regression achieved the highest ROC-AUC of **0.7456**, followed by SVM (**0.7448**) and Random Forest (**0.7424**). The relatively small differences indicate similar discriminatory capabilities among the three models.

### Confusion Matrices

The reported confusion matrices were:

#### Logistic Regression

```text
[[32, 18],
 [18, 32]]
```

#### Random Forest

```text
[[33, 17],
 [15, 35]]
```

#### SVM

```text
[[34, 16],
 [19, 31]]
```

## Week 4 – Data Visualization and Interpretation

The Week 4 analysis focused on visual exploration and interpretation of molecular descriptor data.

The analysis included visualizations of:

* Molecular descriptor distributions
* Active versus inactive compound comparisons
* Correlation between molecular descriptors
* Pairwise relationships between molecular descriptors

These visualizations were used to examine patterns in the chemical-property space and differences between active and inactive compounds.

The analysis provided a visual perspective on molecular descriptor distributions, relationships, correlations, and potential patterns relevant to computational drug discovery.

## Overall Outcome

The combined results from Weeks 2–4 demonstrate a complete computational workflow involving:

**Data Cleaning → Exploratory Data Analysis → Predictive Modeling → Model Evaluation → Data Visualization → Interpretation**

The workflow provided practical experience in applying Python-based data science methods to a synthetic chemical-compound dataset in a healthcare and computational drug discovery context.

## Important Note

The dataset used in this project is **synthetic and intended for educational and training purposes**. It does not represent experimentally validated bioactivity data or real patient information.

The numerical results reported above correspond to the results documented in the weekly reports. **No unreported metrics have been inferred or added.**

