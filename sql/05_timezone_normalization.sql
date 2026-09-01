-- 05_timezone_normalization.sql
-- Converts UTC and Asia/Dubai timestamps to Asia/Kolkata (IST)
SELECT 
    payment_id,
    event_at AS raw_timestamp,
    timezone,
    CASE 
        WHEN timezone = 'UTC' THEN DATEADD(minute, 330, event_at)
        WHEN timezone = 'Asia/Dubai' THEN DATEADD(minute, 90, event_at)
        ELSE event_at
    END AS event_at_ist
FROM payments p
JOIN accounts a ON p.account_id = a.account_id;