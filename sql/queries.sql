-- Total Funds
SELECT COUNT(*) FROM dim_fund;

-- Fund Houses
SELECT fund_house, COUNT(*)
FROM dim_fund
GROUP BY fund_house;

-- Categories
SELECT category, COUNT(*)
FROM dim_fund
GROUP BY category;

-- Average Expense Ratio
SELECT AVG(expense_ratio_pct)
FROM fact_performance;

-- Top 10 Funds by 5Y Return
SELECT scheme_name, return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- Risk Distribution
SELECT risk_grade, COUNT(*)
FROM fact_performance
GROUP BY risk_grade;

-- NAV Records Count
SELECT COUNT(*)
FROM fact_nav;

-- Transaction Type Distribution
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- Average Investment
SELECT AVG(amount_inr)
FROM fact_transactions;

-- Highest Investment
SELECT MAX(amount_inr)
FROM fact_transactions;