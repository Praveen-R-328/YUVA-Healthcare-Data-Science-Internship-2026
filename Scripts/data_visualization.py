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

# --------------------------------------------------
# Molecular descriptors
# --------------------------------------------------

descriptors = [
    "Molecular_Weight",
    "LogP",
    "HBA",
    "HBD",
    "TPSA",
    "Rotatable_Bonds"
]

# --------------------------------------------------
# Distribution of molecular descriptors
# --------------------------------------------------

fig, axes = plt.subplots(
    2,
    3,
    figsize=(15, 9)
)

for ax, descriptor in zip(
    axes.flatten(),
    descriptors
):

    sns.histplot(
        data=df,
        x=descriptor,
        bins=30,
        kde=True,
        ax=ax
    )

    ax.set_title(
        f"Distribution of {descriptor}"
    )

    ax.set_xlabel(descriptor)
    ax.set_ylabel("Number of Compounds")

plt.tight_layout()
plt.show()

# --------------------------------------------------
# Active vs Inactive comparison
# --------------------------------------------------

fig, axes = plt.subplots(
    2,
    3,
    figsize=(15, 9)
)

for ax, descriptor in zip(
    axes.flatten(),
    descriptors
):

    sns.boxplot(
        data=df,
        x="Bioactivity",
        y=descriptor,
        ax=ax
    )

    ax.set_title(
        f"{descriptor} by Bioactivity"
    )

    ax.set_xlabel("Bioactivity")
    ax.set_ylabel(descriptor)

plt.tight_layout()
plt.show()

# --------------------------------------------------
# Correlation heatmap
# --------------------------------------------------

correlation_matrix = df[descriptors].corr()

plt.figure(figsize=(9, 7))

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5
)

plt.title(
    "Correlation Heatmap of Molecular Descriptors"
)

plt.tight_layout()
plt.show()

# --------------------------------------------------
# Pairwise chemical-space analysis
# --------------------------------------------------

sns.pairplot(
    df,
    vars=descriptors,
    hue="Bioactivity",
    diag_kind="hist"
)

plt.suptitle(
    "Pairwise Relationships Among Molecular Descriptors",
    y=1.02
)

plt.show()
