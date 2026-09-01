-- 02_schema_checks.sql
-- Verify null percentages and column data types
SELECT 
    COUNT(*) AS total_rows,
    SUM(CASE WHEN account_id IS NULL THEN 1 ELSE 0 END) AS null_account_ids,
    SUM(CASE WHEN payment_reference IS NULL THEN 1 ELSE 0 END) AS null_references
FROM payments;