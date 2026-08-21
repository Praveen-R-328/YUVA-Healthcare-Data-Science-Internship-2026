import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    roc_auc_score,
    roc_curve
)

# --------------------------------------------------
# Load dataset
# --------------------------------------------------

data_file = (
    Path(__file__).resolve().parent.parent
    / "Data"
    / "synthetic_compounds.csv"
)

df = pd.read_csv(data_file)

print("Dataset shape:", df.shape)

# --------------------------------------------------
# Convert bioactivity labels to binary values
# --------------------------------------------------

df["Bioactivity_Binary"] = df["Bioactivity"].map({
    "Inactive": 0,
    "Active": 1
})

# Check that conversion was successful
if df["Bioactivity_Binary"].isnull().any():
    raise ValueError("Unexpected bioactivity label found.")

# --------------------------------------------------
# Features
# --------------------------------------------------

features = [
    "Molecular_Weight",
    "LogP",
    "HBA",
    "HBD",
    "TPSA",
    "Rotatable_Bonds"
]

X = df[features]
y = df["Bioactivity_Binary"]

# --------------------------------------------------
# Train-test split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# --------------------------------------------------
# Standardization
# --------------------------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# --------------------------------------------------
# Logistic Regression
# --------------------------------------------------

lr_parameters = {
    "C": [0.01, 0.1, 1, 10, 100],
    "solver": ["liblinear", "lbfgs"]
}

lr_grid = GridSearchCV(
    LogisticRegression(
        random_state=42,
        max_iter=1000
    ),
    lr_parameters,
    cv=5,
    scoring="f1"
)

lr_grid.fit(X_train_scaled, y_train)

lr_model = lr_grid.best_estimator_

# --------------------------------------------------
# Random Forest
# --------------------------------------------------

rf_parameters = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 5, 10],
    "min_samples_split": [2, 5]
}

rf_grid = GridSearchCV(
    RandomForestClassifier(
        random_state=42
    ),
    rf_parameters,
    cv=5,
    scoring="f1"
)

rf_grid.fit(X_train, y_train)

rf_model = rf_grid.best_estimator_

# --------------------------------------------------
# Support Vector Machine
# --------------------------------------------------

svm_parameters = {
    "C": [0.1, 1, 10],
    "kernel": ["linear", "rbf"],
    "gamma": ["scale", "auto"]
}

svm_grid = GridSearchCV(
    SVC(
        probability=True,
        random_state=42
    ),
    svm_parameters,
    cv=5,
    scoring="f1"
)

svm_grid.fit(X_train_scaled, y_train)

svm_model = svm_grid.best_estimator_

# --------------------------------------------------
# Predictions
# --------------------------------------------------

lr_prediction = lr_model.predict(X_test_scaled)
rf_prediction = rf_model.predict(X_test)
svm_prediction = svm_model.predict(X_test_scaled)

# Probabilities for ROC-AUC
lr_probability = lr_model.predict_proba(X_test_scaled)[:, 1]
rf_probability = rf_model.predict_proba(X_test)[:, 1]
svm_probability = svm_model.predict_proba(X_test_scaled)[:, 1]

# --------------------------------------------------
# Evaluation function
# --------------------------------------------------

def evaluate_model(name, y_true, predictions, probabilities):

    accuracy = accuracy_score(y_true, predictions)
    precision = precision_score(y_true, predictions, zero_division=0)
    recall = recall_score(y_true, predictions, zero_division=0)
    f1 = f1_score(y_true, predictions, zero_division=0)
    roc_auc = roc_auc_score(y_true, probabilities)

    print("\n" + "=" * 60)
    print(name)
    print("=" * 60)

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1-score : {f1:.4f}")
    print(f"ROC-AUC  : {roc_auc:.4f}")

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_true, predictions))

    print("\nClassification Report:")
    print(
        classification_report(
            y_true,
            predictions,
            target_names=["Inactive", "Active"],
            zero_division=0
        )
    )

    return {
        "Accuracy": accuracy,
        "Precision": precision,
        "Recall": recall,
        "F1-score": f1,
        "ROC-AUC": roc_auc
    }


# --------------------------------------------------
# Evaluate models
# --------------------------------------------------

lr_results = evaluate_model(
    "Logistic Regression",
    y_test,
    lr_prediction,
    lr_probability
)

rf_results = evaluate_model(
    "Random Forest",
    y_test,
    rf_prediction,
    rf_probability
)

svm_results = evaluate_model(
    "Support Vector Machine",
    y_test,
    svm_prediction,
    svm_probability
)

# --------------------------------------------------
# ROC Curves
# --------------------------------------------------

lr_fpr, lr_tpr, _ = roc_curve(y_test, lr_probability)
rf_fpr, rf_tpr, _ = roc_curve(y_test, rf_probability)
svm_fpr, svm_tpr, _ = roc_curve(y_test, svm_probability)

plt.figure(figsize=(8, 6))

plt.plot(
    lr_fpr,
    lr_tpr,
    label=f"Logistic Regression (AUC = {lr_results['ROC-AUC']:.4f})"
)

plt.plot(
    rf_fpr,
    rf_tpr,
    label=f"Random Forest (AUC = {rf_results['ROC-AUC']:.4f})"
)

plt.plot(
    svm_fpr,
    svm_tpr,
    label=f"SVM (AUC = {svm_results['ROC-AUC']:.4f})"
)

plt.plot(
    [0, 1],
    [0, 1],
    linestyle="--"
)

plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curves for Classification Models")
plt.legend()
plt.tight_layout()
plt.show()
