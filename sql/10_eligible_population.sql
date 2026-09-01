-- 10_eligible_population.sql
-- Defines full eligible account population baseline
SELECT 
    account_id,
    borrower_id,
    outstanding_amount,
    dpd,
    risk_segment
FROM accounts
WHERE status IN ('ACTIVE', 'PAID', 'CLOSED');