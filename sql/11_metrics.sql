-- 11_metrics.sql
-- Core metric queries: Contact Rate, RPC Rate, Recovery Rate
SELECT 
    COUNT(DISTINCT account_id) AS total_eligible_accounts,
    SUM(outstanding_amount) AS total_outstanding,
    AVG(dpd) AS avg_dpd
FROM accounts;