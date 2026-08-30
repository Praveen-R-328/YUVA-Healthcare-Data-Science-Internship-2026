# Notebooks

## Overview

This folder contains the Jupyter/Google Colab notebooks used for the computational analysis performed during the **YUVAIntern Healthcare Data Science Internship 2026**.

The notebooks document the practical implementation of the project workflow from **Week 2 to Week 4**.

Week 1 focused on research project proposal and strategy development and was primarily documented as a written project proposal. Therefore, no separate computational notebook is included for Week 1.

## Notebook Structure

The notebooks are organized according to the weekly internship tasks.

### Week 2 – Data Cleaning and Exploratory Data Analysis

The Week 2 notebook documents the preparation, cleaning, and exploratory analysis of the synthetic chemical-compound dataset.

The notebook includes:

- Dataset loading and inspection
- Dataset structure and data types
- Missing-value checking
- Duplicate checking
- Descriptive statistics
- Data cleaning and preprocessing
- Molecular descriptor analysis
- Distribution analysis
- Correlation analysis
- Outlier inspection
- Exploratory visualizations
- Interpretation of observed patterns

The dataset contains **500 synthetic chemical compounds** represented using the following molecular descriptors:

- Molecular Weight
- LogP
- HBA
- HBD
- TPSA
- Rotatable Bonds

The bioactivity variable contains the **Active** and **Inactive** classes.

### Week 3 – Predictive Modeling and Evaluation

The Week 3 notebook implements machine-learning models for bioactivity classification.

The notebook includes:

- Dataset loading
- Feature selection
- Train-test splitting
- Feature standardization
- Logistic Regression
- Random Forest
- Support Vector Machine (SVM)
- Hyperparameter tuning using GridSearchCV
- 5-fold cross-validation
- Model evaluation
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion matrices
- Classification reports
- Model comparison
- Best-model selection based on F1-score

The optimized models are evaluated on the independent test dataset.

### Week 4 – Data Visualization and Interpretation

The Week 4 notebook focuses on visualization and interpretation of molecular descriptor data.

The notebook includes:

- Dataset inspection
- Data-quality checks
- Molecular descriptor selection
- Descriptive statistical analysis
- Molecular descriptor distributions
- Bioactivity class distribution
- Active versus Inactive compound comparison
- Correlation heatmap
- Pairwise descriptor analysis
- Molecular Weight versus LogP analysis
- Outlier visualization
- IQR-based outlier identification
- Interpretation of visualization results
- Recommendations and conclusion

The visualizations are generated directly from the existing synthetic dataset.

## Dataset

The notebooks use the common dataset:

`../Data/synthetic_compounds.csv`

The same dataset is used across the computational workflow to maintain consistency between the weekly analyses.

The dataset is synthetic and intended for educational and training purposes. It does not represent experimentally validated bioactivity data or real patient information.

## Technologies Used

The notebooks use:

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

## Workflow

The computational workflow follows:

**Synthetic Dataset → Data Cleaning & EDA → Predictive Modeling → Data Visualization & Interpretation**

### Week 2

**Data → Cleaning → Preprocessing → EDA → Statistical Analysis → Exploratory Visualization**

### Week 3

**Data → Feature Selection → Train-Test Split → Scaling → Model Training → Hyperparameter Tuning → Evaluation → Model Selection**

### Week 4

**Data → Descriptor Analysis → Visualization → Comparison → Correlation → Pairwise Analysis → Outlier Analysis → Interpretation**

## Reproducibility

The notebooks are designed to use the same synthetic dataset throughout the project.

Where random processes are involved, fixed random seeds are used where applicable to support reproducibility.

The notebooks should be executed in sequence within each weekly workflow.

If using Google Colab, ensure that the required dataset is uploaded or that the repository is mounted/accessed correctly before running the notebook.

## Relationship with Other Project Folders

The notebooks contain the detailed computational implementation of the project.

The repository is organized so that:

- `Data/` contains the dataset used for analysis.
- `Notebooks/` contains the Jupyter/Google Colab notebooks.
- `Scripts/` contains reusable Python scripts corresponding to the computational workflow.
- `Figures/` contains visualization outputs generated during the analysis.
- `Results/` contains summarized analysis and model results.
- `Reports/` contains the weekly written reports and documentation.

The notebooks provide the detailed computational record supporting the analysis documented in the weekly reports.

## Important Note

The project uses a **synthetic chemical-compound dataset** for educational purposes.

The computational results and visualization patterns should therefore be interpreted as exploratory findings from a simulated dataset and should not be considered experimentally validated biological or clinical conclusions.
