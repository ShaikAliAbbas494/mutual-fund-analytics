import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

# Clean transaction type
df['transaction_type'] = (
    df['transaction_type']
    .str.strip()
    .str.title()
)

# Keep only valid transaction types
valid = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

df = df[
    df['transaction_type'].isin(valid)
]

# Remove invalid amounts
df = df[
    df['amount_inr'] > 0
]

# Remove duplicates
df = df.drop_duplicates()

# Convert date column
df['transaction_date'] = pd.to_datetime(
    df['transaction_date']
)

# Save cleaned file
df.to_csv(
    "data/processed/08_transactions_clean.csv",
    index=False
)

print("Cleaned Data Shape:", df.shape)
print("File saved successfully")