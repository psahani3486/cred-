-- 12_monthly_performance.sql
-- 12-Month Golden Recovery Performance Breakdown
SELECT 
    FORMAT_DATE('%Y-%m', event_at_ist) AS business_month,
    SUM(amount) AS golden_recovery,
    COUNT(DISTINCT payment_id) AS valid_transactions,
    COUNT(DISTINCT account_id) AS paying_accounts
FROM golden_payments
GROUP BY 1
ORDER BY 1;