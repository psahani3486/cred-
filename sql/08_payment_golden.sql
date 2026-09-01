-- 08_payment_golden.sql
-- Golden Deduplicated Valid Payments Table
WITH dedup AS (
    SELECT 
        p.payment_id,
        p.account_id,
        p.amount,
        p.payment_status,
        p.payment_reference,
        p.event_at,
        a.timezone,
        ROW_NUMBER() OVER (PARTITION BY p.payment_reference ORDER BY p.event_at ASC) AS rn
    FROM payments p
    JOIN accounts a ON p.account_id = a.account_id
    WHERE p.payment_status = 'SUCCESS'
)
SELECT 
    payment_id,
    account_id,
    amount,
    payment_reference,
    event_at,
    CASE 
        WHEN timezone = 'UTC' THEN DATEADD(minute, 330, event_at)
        WHEN timezone = 'Asia/Dubai' THEN DATEADD(minute, 90, event_at)
        ELSE event_at
    END AS event_at_ist
FROM dedup
WHERE rn = 1;