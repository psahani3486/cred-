-- 01_data_profiling.sql
-- Table profiling, row counts, distinct key checks
SELECT 'borrowers' AS table_name, COUNT(*) AS row_count, COUNT(DISTINCT borrower_id) AS unique_pk FROM borrowers
UNION ALL
SELECT 'accounts', COUNT(*), COUNT(DISTINCT account_id) FROM accounts
UNION ALL
SELECT 'payments', COUNT(*), COUNT(DISTINCT payment_id) FROM payments;