-- 17_data_quality.sql
-- Data quality assertions and automated sanity checks
SELECT 'Duplicate Payments' AS check_name, COUNT(*) AS anomaly_count FROM payments GROUP BY payment_reference HAVING COUNT(*) > 1;