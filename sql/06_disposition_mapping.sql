-- 06_disposition_mapping.sql
-- Standardizes raw telephony disposition codes
SELECT 
    disposition_code,
    CASE 
        WHEN disposition_code IN ('PROMISE_TO_PAY', 'PTP', 'PAID') THEN 'PTP'
        WHEN disposition_code IN ('CALLBACK', 'PTP_BROKEN') THEN 'RPC'
        WHEN disposition_code IN ('WRONG_NUMBER', 'NO_CONTACT') THEN 'NO_CONTACT'
        WHEN disposition_code = 'REFUSED' THEN 'REFUSED'
        WHEN disposition_code = 'DISPUTE' THEN 'DISPUTE'
        ELSE 'OTHER'
    END AS standard_disposition,
    COUNT(*) AS code_count
FROM call_dispositions
GROUP BY disposition_code;