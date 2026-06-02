import pandas as pd

df = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

# Convert return columns to numeric
return_cols = [
    'return_1yr_pct',
    'return_3yr_pct',
    'return_5yr_pct'
]

for col in return_cols:
    df[col] = pd.to_numeric(
        df[col],
        errors='coerce'
    )

# Convert expense ratio to numeric
df['expense_ratio_pct'] = pd.to_numeric(
    df['expense_ratio_pct'],
    errors='coerce'
)

# Remove invalid expense ratios
df = df[
    (df['expense_ratio_pct'] >= 0)
    &
    (df['expense_ratio_pct'] <= 5)
]

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned data
df.to_csv(
    "data/processed/07_performance_clean.csv",
    index=False
)

print("Cleaned Data Shape:", df.shape)
print("File saved successfully")