-- 09_interactions_golden.sql
-- Unified Golden Interactions Table across Voice, WhatsApp, SMS, Field
SELECT 'VOICE_CALL' AS channel, call_id AS interaction_id, account_id, event_at, call_status AS outcome FROM calls
UNION ALL
SELECT 'WHATSAPP', whatsapp_event_id, account_id, event_at, status FROM whatsapp_events
UNION ALL
SELECT 'SMS', sms_event_id, account_id, event_at, status FROM sms_events
UNION ALL
SELECT 'FIELD_VISIT', visit_id, account_id, event_at, outcome FROM field_visits;