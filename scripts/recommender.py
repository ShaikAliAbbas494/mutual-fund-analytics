import pandas as pd

print("Script started")

scorecard = pd.read_csv(
    "data/processed/fund_scorecard.csv"
)

print(scorecard.head())

top_funds = scorecard.sort_values(
    "score",
    ascending=False
).head(5)

print("\nTop 5 Recommended Funds")
print(top_funds)