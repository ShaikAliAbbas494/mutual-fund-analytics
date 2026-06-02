import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

# Load fund master
fund = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

# Load cleaned NAV history
nav = pd.read_csv(
    "data/processed/02_nav_history_clean.csv"
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

# Load cleaned transactions
txn = pd.read_csv(
    "data/processed/08_transactions_clean.csv"
)

txn.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

# Load cleaned performance
perf = pd.read_csv(
    "data/processed/07_performance_clean.csv"
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Database loaded successfully!")