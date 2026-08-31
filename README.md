# YUVAIntern Healthcare Data Science Internship 2026

## Overview

This repository contains the complete computational work and documentation completed during the **YUVAIntern Healthcare Data Science Internship 2026**.

The internship provided practical exposure to a complete data science workflow covering research planning, data cleaning, exploratory data analysis, predictive modeling, machine-learning evaluation, data visualization, and interpretation.

The project uses a **synthetic chemical-compound dataset** to demonstrate the application of data science and machine-learning techniques in a healthcare and pharmaceutical research context.

---

## Internship Workflow

```text
Week 1
Research Project Proposal & Strategy Development
        |
        v
Week 2
Data Cleaning & Exploratory Data Analysis
        |
        v
Week 3
Predictive Modeling & Evaluation
        |
        v
Week 4
Data Visualization & Interpretation

```
---

## Week 1 - Research Project Proposal and Strategy Development

The first week focused on planning a healthcare data science research project.

The work included:

- Identification of a healthcare-related research problem
- Preliminary literature review
- Research question development
- Research objectives
- Hypothesis formulation
- Data science methodology planning
- Data sourcing strategy
- Python-based analytical approach
- Project timeline
- Potential challenges and mitigation strategies

The complete Week 1 proposal is provided in the corresponding project folder.

---

## Week 2 - Data Cleaning and Exploratory Data Analysis

Week 2 focused on preparing and exploring the synthetic chemical-compound dataset.

The analysis included:

- Dataset loading and inspection
- Data structure and data-type examination
- Missing-value analysis
- Duplicate checking
- Data cleaning
- Descriptive statistics
- Molecular descriptor analysis
- Distribution analysis
- Correlation analysis
- Outlier inspection
- Exploratory visualization
- Interpretation of observed patterns

The molecular descriptors analyzed were:

- Molecular Weight
- LogP
- HBA
- HBD
- TPSA
- Rotatable Bonds

The dataset contains two bioactivity classes:

- Active
- Inactive

---

## Week 3 - Predictive Modeling and Evaluation

Week 3 focused on developing machine-learning models for bioactivity classification.

The models implemented were:

- Logistic Regression
- Random Forest
- Support Vector Machine (SVM)

The workflow included:

- Feature selection
- Train-test splitting
- Feature standardization
- Model training
- 5-fold cross-validation
- Hyperparameter tuning using `GridSearchCV`
- Independent test-set evaluation
- Confusion-matrix analysis
- Classification reports
- Model performance comparison
- ROC-AUC evaluation
- Best-model selection

### Final Test-Set Results

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 0.64 | 0.6400 | 0.64 | 0.6400 | 0.7456 |
| Random Forest | 0.68 | 0.6731 | 0.70 | 0.6863 | 0.7424 |
| SVM | 0.65 | 0.6596 | 0.62 | 0.6392 | 0.7448 |

Based on the test-set F1-score, **Random Forest** was selected as the best-performing model.

---

## Week 4 - Data Visualization and Interpretation

Week 4 focused on visual analysis and interpretation of molecular descriptor data.

The analysis included:

- Molecular descriptor distributions
- Bioactivity class distribution
- Active versus Inactive compound comparison
- Correlation analysis
- Pairwise descriptor relationships
- Molecular Weight and LogP analysis
- TPSA and LogP analysis
- Outlier visualization
- Interpretation of observed patterns
- Data-driven conclusions and recommendations

---

## Dataset

The computational analysis uses:

`Data/synthetic_compounds.csv`

The dataset contains **500 synthetic chemical compounds** represented using molecular descriptors including:

- Molecular Weight
- LogP
- HBA
- HBD
- TPSA
- Rotatable Bonds

The target variable is **Bioactivity**, containing:

- Active
- Inactive

The dataset is synthetic and was created for educational and training purposes.

---

## Technologies Used

The project was developed using:

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

### Machine-Learning Techniques

- Logistic Regression
- Random Forest
- Support Vector Machine
- Feature Standardization
- Cross-Validation
- Grid Search
- Classification Metrics
- ROC-AUC Analysis

---

## Repository Structure

```text
YUVA-Healthcare-Data-Science-Internship-2026/
|
+-- Data/
|   +-- README.md
|   +-- synthetic_compounds.csv
|
+-- Figures/
|   +-- Week_2/
|   +-- Week_3/
|   +-- Week_4/
|   +-- README.md
|
+-- Notebooks/
|   +-- README.md
|   +-- Week-2_Data-Cleaning-and-EDA.ipynb
|   +-- Week_3_Predictive_Modeling.ipynb
|   +-- Week_4_Data_Visualization_and_Interpretation.ipynb
|
+-- Results/
|   +-- README.md
|
+-- Scripts/
|   +-- README.md
|   +-- data_generation.py
|   +-- data_cleaning_eda.py
|   +-- predictive_modelling.py
|   +-- data_visualization.py
|
+-- Week-1_Project-Proposal/
|   +-- Healthcare Data Science Research Internship Week 1.pdf
|   +-- README.md
|
+-- Week-2_Data-Cleaning-and-EDA/
|   +-- Healthcare Data Science Research Internship Week 2.pdf
|   +-- README.md
|
+-- Week-3_Predictive-Modeling/
|   +-- Healthcare Data Science Research Internship Week 3.pdf
|   +-- README.md
|
+-- Week-4_Data-Visualization/
|   +-- Healthcare Data Science Research Internship Week 4.pdf
|   +-- README.md
|
+-- README.md
```

---

## Project Organization

### `Data/`

Contains the synthetic dataset used for the computational analysis.

### `Notebooks/`

Contains the Google Colab/Jupyter notebooks used for the Week 2, Week 3, and Week 4 analyses.

### `Figures/`

Contains visualization outputs generated during the analysis.

### `Results/`

Contains documentation related to the project results.

### `Scripts/`

Contains reusable Python scripts corresponding to the computational workflow.

### Weekly Project Folders

The Week 1-4 folders contain the corresponding written reports and supporting documentation.

---

## Computational Workflow

```text
Synthetic Dataset
        |
        v
Data Inspection
        |
        v
Data Cleaning
        |
        v
Exploratory Data Analysis
        |
        v
Feature Selection
        |
        v
Train-Test Split
        |
        v
Machine-Learning Models
        |
        v
Hyperparameter Tuning
        |
        v
Model Evaluation
        |
        v
Visualization
        |
        v
Interpretation & Conclusions
```

---

## Reproducibility

The project was developed using Python-based Jupyter/Google Colab notebooks.

The same synthetic dataset is used throughout the computational workflow to maintain consistency between the weekly analyses.

Fixed random seeds were used where applicable to improve reproducibility.

The notebooks contain the computational steps required to reproduce the analyses and generate the corresponding figures.

---

## Key Learning Outcomes

Through this internship, I gained practical exposure to:

- Research project planning
- Data preprocessing
- Exploratory data analysis
- Statistical interpretation
- Molecular descriptor analysis
- Machine-learning classification
- Hyperparameter optimization
- Model evaluation
- Data visualization
- Scientific interpretation
- Python-based computational workflows

The project also helped me understand how data science approaches can complement **chemistry, computational research, healthcare, and pharmaceutical research**.

---

## Limitations

The primary limitation of this project is that the dataset is **synthetic** and does not represent experimentally validated chemical bioactivity or real patient data.

Therefore:

- The observed descriptor relationships are exploratory.
- Machine-learning performance should not be interpreted as clinical performance.
- The results cannot be directly generalized to real-world healthcare applications.
- Experimental validation would be required before drawing biological or clinical conclusions.

---

## Conclusion

The YUVAIntern Healthcare Data Science Internship provided practical experience in applying Python-based data science methods to a healthcare and chemical-compound research context.

The project progressed from research planning and data preparation to machine-learning modeling, evaluation, visualization, and interpretation.

Overall, the internship strengthened my understanding of how **data science, machine learning, and computational analysis can support interdisciplinary research involving chemistry, healthcare, and pharmaceutical applications**.

---

## Author

**Praveen R**

BS-MS Student

Indian Institute of Science Education and Research (IISER) Tirupati

---

## Disclaimer

This repository was developed as part of the **YUVAIntern Healthcare Data Science Internship 2026**.

The dataset used in this project is synthetic and intended for educational and training purposes. The analyses and results should not be considered experimentally validated biological, pharmaceutical, or clinical findings.
