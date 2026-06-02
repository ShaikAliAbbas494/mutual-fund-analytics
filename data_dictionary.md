# Mutual Fund Analytics - Data Dictionary

## dim_fund

| Column | Description |
|----------|------------|
| amfi_code | Unique AMFI Scheme Code |
| scheme_name | Fund Name |
| fund_house | AMC Name |
| category | Fund Category |

## fact_nav

| Column | Description |
|----------|------------|
| amfi_code | Scheme Code |
| nav | Net Asset Value |
| date | NAV Date |

## fact_transactions

| Column | Description |
|----------|------------|
| investor_id | Investor Identifier |
| transaction_date | Transaction Date |
| transaction_type | SIP/Lumpsum/Redemption |
| amount_inr | Transaction Amount |

## fact_performance

| Column | Description |
|----------|------------|
| return_1yr_pct | 1 Year Return |
| return_3yr_pct | 3 Year Return |
| return_5yr_pct | 5 Year Return |
| expense_ratio_pct | Expense Ratio |
| risk_grade | Risk Category |