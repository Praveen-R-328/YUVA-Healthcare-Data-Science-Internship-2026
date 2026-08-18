# Week 3 – Predictive Modeling and Evaluation

## Overview

Week 3 focused on developing and evaluating machine learning models to predict the bioactivity of chemical compounds using molecular descriptor data.

A synthetic healthcare-related bioactivity dataset was used to simulate a drug discovery scenario without using confidential patient information. The dataset was divided into training and independent testing subsets for model development and evaluation.

## Objective

The main objectives of Week 3 were to:

* Prepare the molecular descriptor dataset for machine learning
* Select relevant features for prediction
* Develop supervised classification models
* Train and evaluate multiple machine learning algorithms
* Compare model performance using multiple evaluation metrics
* Identify the most suitable model for the bioactivity classification task

## Machine Learning Models

Three classification algorithms were developed and compared:

* **Logistic Regression**
* **Random Forest**
* **Support Vector Machine (SVM)**

The models were used to classify chemical compounds as **biologically Active or Inactive** based on molecular descriptor data.

## Dataset and Features

The prediction task used molecular descriptors including:

* Molecular Weight
* LogP
* Hydrogen Bond Acceptors (HBA)
* Hydrogen Bond Donors (HBD)
* Topological Polar Surface Area (TPSA)
* Rotatable Bonds

The dataset consisted of **500 samples**, with **400 samples used for training and 100 samples used for independent testing**.

## Model Evaluation

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix
* ROC-AUC

Using multiple evaluation metrics allowed the models to be compared from different perspectives rather than relying on a single performance measure.

## Key Results

Random Forest achieved the strongest overall performance based on the model-selection criteria used in the project:

* **Accuracy:** 0.680
* **Precision:** 0.6731
* **Recall:** 0.700
* **F1-score:** 0.6863

Logistic Regression achieved the highest ROC-AUC:

* **Logistic Regression:** 0.7456
* **SVM:** 0.7448
* **Random Forest:** 0.7424

Therefore, **Random Forest was selected as the best-performing model based on F1-score**, while Logistic Regression showed the highest ROC-AUC.

## Critical Evaluation

The models demonstrated moderate predictive performance. The report notes that the molecular descriptors used provide useful physicochemical information but do not fully capture the structural and biological factors influencing compound bioactivity.

Because the dataset was synthetically generated, the results should be interpreted as a demonstration of the machine-learning workflow rather than experimentally validated bioactivity predictions.

## Tools and Technologies

* **Python**
* **Pandas**
* **NumPy**
* **Scikit-learn**
* **Matplotlib**
* **Seaborn**
* **Logistic Regression**
* **Random Forest**
* **Support Vector Machine (SVM)**

## Outcome

This week strengthened practical skills in:

* Machine learning model development
* Classification
* Feature-based prediction
* Model evaluation
* Hyperparameter tuning
* Performance comparison
* Scientific interpretation of machine learning results

The Week 3 work forms the predictive modeling component of the overall four-week YUVAIntern project and provides the foundation for the visualization and interpretation work completed in Week 4.

