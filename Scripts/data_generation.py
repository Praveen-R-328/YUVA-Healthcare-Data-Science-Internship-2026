import numpy as np
import pandas as pd
from pathlib import Path

# Reproducibility
np.random.seed(42)

# Number of compounds
n = 500

# Generate synthetic chemical-compound dataset
df = pd.DataFrame({
    "Compound_ID": [f"CMP{i+1}" for i in range(n)],
    "Molecular_Weight": np.random.normal(350, 50, n),
    "LogP": np.random.normal(3.0, 1.0, n),
    "HBA": np.random.randint(1, 10, n),
    "HBD": np.random.randint(0, 6, n),
    "TPSA": np.random.normal(75, 20, n),
    "Rotatable_Bonds": np.random.randint(1, 12, n),
    "Bioactivity": np.random.choice(["Active", "Inactive"], n)
})

# Create Data directory if it does not exist
data_dir = Path(__file__).resolve().parent.parent / "Data"
data_dir.mkdir(exist_ok=True)

# Save dataset
output_file = data_dir / "synthetic_compounds.csv"
df.to_csv(output_file, index=False)

print("Synthetic dataset generated successfully.")
print(f"Saved to: {output_file}")
print(f"Number of compounds: {len(df)}")
print(f"Number of features: {len(df.columns)}")
print("\nBioactivity distribution:")
print(df["Bioactivity"].value_counts())
