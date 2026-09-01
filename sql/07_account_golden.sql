-- 07_account_golden.sql
-- Golden Account Master
SELECT 
    account_id,
    borrower_id,
    loan_type,
    principal_amount,
    outstanding_amount,
    dpd,
    risk_segment,
    status,
    opened_at,
    timezone
FROM accounts;