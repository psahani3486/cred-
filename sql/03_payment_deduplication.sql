-- 03_payment_deduplication.sql
-- Detect and flag duplicate payment references
WITH ranked_payments AS (
    SELECT 
        payment_id,
        account_id,
        payment_reference,
        amount,
        payment_status,
        event_at,
        ROW_NUMBER() OVER (PARTITION BY payment_reference ORDER BY event_at ASC) as rn
    FROM payments
)
SELECT * FROM ranked_payments WHERE rn > 1;