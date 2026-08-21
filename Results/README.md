# Results

## Overview

This folder contains the key outputs generated from the computational analysis performed during the YUVAIntern Healthcare Data Science Internship 2026.

The results primarily include the machine-learning evaluation outputs from **Week 3** and the corresponding visual analysis outputs from **Week 4**.

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

## Week 3 – Confusion Matrices

The reported confusion matrices were:

### Logistic Regression

```text
[[32, 18],
 [18, 32]]
```

### Random Forest

```text
[[33, 17],
 [15, 35]]
```

### SVM

```text
[[34, 16],
 [19, 31]]
```

## Week 4 – Visualization Outputs

The Week 4 analysis included visualizations of:

* Molecular descriptor distributions
* Active versus inactive compound comparisons
* Correlation between molecular descriptors
* Pairwise relationships between molecular descriptors

These visualizations were used to interpret patterns within the synthetic chemical-compound dataset.

## Important Note

The dataset used in this project is **synthetic and intended for educational and training purposes**. The reported results should therefore be interpreted as outputs from a computational learning exercise rather than experimentally validated bioactivity predictions.

The numerical results in this folder correspond to the results documented in the weekly reports. **No unreported metrics have been inferred or added.**

