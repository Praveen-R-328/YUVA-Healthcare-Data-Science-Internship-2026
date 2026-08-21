import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# --------------------------------------------------
# Load dataset
# --------------------------------------------------

data_file = (
    Path(__file__).resolve().parent.parent
    / "Data"
    / "synthetic_compounds.csv"
)

df = pd.read_csv(data_file)

print("First five rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

# --------------------------------------------------
# Dataset information
# --------------------------------------------------

print("\nDataset information:")
df.info()

# --------------------------------------------------
# Missing-value check
# --------------------------------------------------

print("\nMissing values:")
print(df.isnull().sum())

# --------------------------------------------------
# Duplicate check
# --------------------------------------------------

print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# --------------------------------------------------
# Descriptive statistics
# --------------------------------------------------

print("\nDescriptive statistics:")
print(df.describe())

# --------------------------------------------------
# Molecular Weight distribution
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="Molecular_Weight",
    bins=20,
    kde=True
)

plt.title("Distribution of Molecular Weight")
plt.xlabel("Molecular Weight")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# --------------------------------------------------
# LogP distribution
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="LogP",
    bins=20,
    kde=True
)

plt.title("Distribution of LogP")
plt.xlabel("LogP")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# --------------------------------------------------
# Bioactivity distribution
# --------------------------------------------------

plt.figure(figsize=(6, 4))

sns.countplot(
    data=df,
    x="Bioactivity"
)

plt.title("Bioactivity Class Distribution")
plt.xlabel("Bioactivity")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# --------------------------------------------------
# Correlation heatmap
# --------------------------------------------------

descriptors = [
    "Molecular_Weight",
    "LogP",
    "HBA",
    "HBD",
    "TPSA",
    "Rotatable_Bonds"
]

correlation_matrix = df[descriptors].corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap of Molecular Descriptors")
plt.tight_layout()
plt.show()

# --------------------------------------------------
# Box plot
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.boxplot(
    x=df["Molecular_Weight"]
)

plt.title("Molecular Weight Distribution and Outliers")
plt.xlabel("Molecular Weight")
plt.tight_layout()
plt.show()

# --------------------------------------------------
# Molecular Weight vs LogP
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Molecular_Weight",
    y="LogP",
    hue="Bioactivity"
)

plt.title("Molecular Weight vs LogP")
plt.xlabel("Molecular Weight")
plt.ylabel("LogP")
plt.tight_layout()
plt.show()
