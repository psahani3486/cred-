-- 13_driver_analysis.sql
-- Driver analysis across Risk Segments and Loan Types
SELECT 
    a.risk_segment,
    a.loan_type,
    SUM(g.amount) AS total_recovered,
    COUNT(DISTINCT g.account_id) AS paying_accounts
FROM golden_payments g
JOIN accounts a ON g.account_id = a.account_id
GROUP BY 1, 2;