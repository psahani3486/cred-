# Data Dictionary — Collections Telemetry Datasets

Observed schemas, column data types, descriptions, primary keys, and key foreign keys across all 17 datasets.

## Table Inventory Summary

| Dataset | Row Count | Column Count | Primary Key | Key Foreign Keys | Description |
| :--- | ---: | ---: | :--- | :--- | :--- |
| account_status_history | 60,000 | 8 | history_id, account_id, borrower_id | None | Historical account status state transitions (ACTIVE, PAID, WRITEOFF, CLOSED) |
| accounts | 30,000 | 11 | account_id, borrower_id | None | Master account directory with outstanding balance, DPD, risk segment, loan type, and native timezone |
| agent_sessions | 15,000 | 7 | session_id, agent_id, device_id | None | Work session logs capturing login timestamps, channel, and device identifiers |
| agents | 30,000 | 8 | agent_id | vendor_id | Agent snapshot directory containing employee codes, names, vendor affiliations, and teams |
| borrowers | 30,600 | 8 | borrower_id | None | Borrower demographic directory with city, phone, email, and registration timestamps |
| call_attempts | 120,000 | 9 | attempt_id, account_id, borrower_id, call_id, agent_id, vendor_id | None | Telephony dialer attempt records prior to call connection |
| call_dispositions | 35,000 | 8 | disposition_id, account_id, borrower_id, call_id, agent_id | None | Agent call outcome dispositions (PTP, Callback, Refused, Dispute, Wrong Number) |
| calls | 91,350 | 11 | call_id, account_id, borrower_id, agent_id | campaign_id, vendor_id | Voice call detail records containing duration, direction, status, and timezone |
| campaigns | 120 | 7 | campaign_id | None | Collection campaign strategy metadata including target definitions and date windows |
| complaints | 8,000 | 9 | complaint_id, account_id, borrower_id | None | Borrower dispute and harassment complaint logs |
| daily_targeting | 45,000 | 7 | target_id, account_id, campaign_id | None | Daily account targeting log specifying outreach priority and treatment allocation |
| field_visits | 25,000 | 10 | visit_id, account_id, borrower_id, agent_id | None | Physical field visit logs with agent locations, outcomes, and collections |
| payments | 25,500 | 9 | payment_id, account_id, borrower_id | provider_id | Payment transaction log with amount, status (SUCCESS/FAILED/REVERSED/PENDING), and reference |
| promises_to_pay | 18,000 | 9 | ptp_id, account_id, borrower_id, agent_id | None | Payment commitments with agreed amount and promised payment due date |
| sms_events | 45,000 | 8 | sms_event_id, account_id, borrower_id, message_id | provider_id | SMS delivery and failure notifications |
| vendor_telephony | 15 | 6 | vendor_id, vendor_account_id | None | Telephony vendor infrastructure configuration and active status |
| whatsapp_events | 60,600 | 8 | whatsapp_event_id, account_id, borrower_id, message_id, provider_id | None | WhatsApp message delivery, read, and payment link click event stream |

---

## Detailed Column Definitions Across All 17 Datasets

### 1. account_status_history
- history_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- account_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- borrower_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- event_at (VARCHAR / TIMESTAMP): Telemetry attribute field.
- status (VARCHAR / TIMESTAMP): Telemetry attribute field.
- changed_by (VARCHAR / TIMESTAMP): Telemetry attribute field.
- source (VARCHAR / TIMESTAMP): Telemetry attribute field.
- recorded_at (VARCHAR / TIMESTAMP): Telemetry attribute field.

### 2. accounts
- account_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- borrower_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- loan_type (VARCHAR / TIMESTAMP): Telemetry attribute field.
- principal_amount (VARCHAR / TIMESTAMP): Telemetry attribute field.
- outstanding_amount (VARCHAR / TIMESTAMP): Telemetry attribute field.
- dpd (VARCHAR / TIMESTAMP): Telemetry attribute field.
- risk_segment (VARCHAR / TIMESTAMP): Telemetry attribute field.
- status (VARCHAR / TIMESTAMP): Telemetry attribute field.
- opened_at (VARCHAR / TIMESTAMP): Telemetry attribute field.
- timezone (VARCHAR / TIMESTAMP): Telemetry attribute field.
- schema_version (VARCHAR / TIMESTAMP): Telemetry attribute field.

### 3. agent_sessions
- session_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- agent_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- login_at (VARCHAR / TIMESTAMP): Telemetry attribute field.
- channel (VARCHAR / TIMESTAMP): Telemetry attribute field.
- device_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- timezone (VARCHAR / TIMESTAMP): Telemetry attribute field.
- logout_at (VARCHAR / TIMESTAMP): Telemetry attribute field.

### 4. agents
- agent_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- employee_code (VARCHAR / TIMESTAMP): Telemetry attribute field.
- agent_name (VARCHAR / TIMESTAMP): Telemetry attribute field.
- vendor_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- team (VARCHAR / TIMESTAMP): Telemetry attribute field.
- status (VARCHAR / TIMESTAMP): Telemetry attribute field.
- joined_at (VARCHAR / TIMESTAMP): Telemetry attribute field.
- updated_at (VARCHAR / TIMESTAMP): Telemetry attribute field.

### 5. borrowers
- borrower_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- name (VARCHAR / TIMESTAMP): Telemetry attribute field.
- phone (VARCHAR / TIMESTAMP): Telemetry attribute field.
- email (VARCHAR / TIMESTAMP): Telemetry attribute field.
- city (VARCHAR / TIMESTAMP): Telemetry attribute field.
- created_at (VARCHAR / TIMESTAMP): Telemetry attribute field.
- updated_at (VARCHAR / TIMESTAMP): Telemetry attribute field.
- state (VARCHAR / TIMESTAMP): Telemetry attribute field.

### 6. call_attempts
- attempt_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- account_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- borrower_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- event_at (VARCHAR / TIMESTAMP): Telemetry attribute field.
- call_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- agent_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- attempt_no (VARCHAR / TIMESTAMP): Telemetry attribute field.
- vendor_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- attempt_status (VARCHAR / TIMESTAMP): Telemetry attribute field.

### 7. call_dispositions
- disposition_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- account_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- borrower_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- event_at (VARCHAR / TIMESTAMP): Telemetry attribute field.
- call_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- agent_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- disposition_code (VARCHAR / TIMESTAMP): Telemetry attribute field.
- disposition_version (VARCHAR / TIMESTAMP): Telemetry attribute field.

### 8. calls
- call_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- account_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- borrower_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- event_at (VARCHAR / TIMESTAMP): Telemetry attribute field.
- agent_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- campaign_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- direction (VARCHAR / TIMESTAMP): Telemetry attribute field.
- vendor_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- call_status (VARCHAR / TIMESTAMP): Telemetry attribute field.
- duration_sec (VARCHAR / TIMESTAMP): Telemetry attribute field.
- timezone (VARCHAR / TIMESTAMP): Telemetry attribute field.

### 9. campaigns
- campaign_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- campaign_name (VARCHAR / TIMESTAMP): Telemetry attribute field.
- channel (VARCHAR / TIMESTAMP): Telemetry attribute field.
- strategy_version (VARCHAR / TIMESTAMP): Telemetry attribute field.
- start_at (VARCHAR / TIMESTAMP): Telemetry attribute field.
- target_definition (VARCHAR / TIMESTAMP): Telemetry attribute field.
- end_at (VARCHAR / TIMESTAMP): Telemetry attribute field.

### 10. complaints
- complaint_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- account_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- borrower_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- event_at (VARCHAR / TIMESTAMP): Telemetry attribute field.
- complaint_type (VARCHAR / TIMESTAMP): Telemetry attribute field.
- severity (VARCHAR / TIMESTAMP): Telemetry attribute field.
- status (VARCHAR / TIMESTAMP): Telemetry attribute field.
- source (VARCHAR / TIMESTAMP): Telemetry attribute field.
- resolution_at (VARCHAR / TIMESTAMP): Telemetry attribute field.

### 11. daily_targeting
- target_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- account_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- campaign_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- target_date (VARCHAR / TIMESTAMP): Telemetry attribute field.
- priority (VARCHAR / TIMESTAMP): Telemetry attribute field.
- recommended_channel (VARCHAR / TIMESTAMP): Telemetry attribute field.
- status (VARCHAR / TIMESTAMP): Telemetry attribute field.

### 14. field_visits
- visit_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- account_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- borrower_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- event_at (VARCHAR / TIMESTAMP): Telemetry attribute field.
- agent_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- visit_type (VARCHAR / TIMESTAMP): Telemetry attribute field.
- outcome (VARCHAR / TIMESTAMP): Telemetry attribute field.
- latitude (VARCHAR / TIMESTAMP): Telemetry attribute field.
- longitude (VARCHAR / TIMESTAMP): Telemetry attribute field.
- scheduled_at (VARCHAR / TIMESTAMP): Telemetry attribute field.

### 15. payments
- payment_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- account_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- borrower_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- event_at (VARCHAR / TIMESTAMP): Telemetry attribute field.
- payment_reference (VARCHAR / TIMESTAMP): Telemetry attribute field.
- amount (VARCHAR / TIMESTAMP): Telemetry attribute field.
- payment_status (VARCHAR / TIMESTAMP): Telemetry attribute field.
- payment_method (VARCHAR / TIMESTAMP): Telemetry attribute field.
- provider_id (VARCHAR / TIMESTAMP): Telemetry attribute field.

### 16. promises_to_pay
- ptp_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- account_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- borrower_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- event_at (VARCHAR / TIMESTAMP): Telemetry attribute field.
- agent_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- promised_amount (VARCHAR / TIMESTAMP): Telemetry attribute field.
- promised_date (VARCHAR / TIMESTAMP): Telemetry attribute field.
- status (VARCHAR / TIMESTAMP): Telemetry attribute field.
- source (VARCHAR / TIMESTAMP): Telemetry attribute field.

### 17. sms_events
- sms_event_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- account_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- borrower_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- event_at (VARCHAR / TIMESTAMP): Telemetry attribute field.
- message_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- event_type (VARCHAR / TIMESTAMP): Telemetry attribute field.
- template_code (VARCHAR / TIMESTAMP): Telemetry attribute field.
- provider_id (VARCHAR / TIMESTAMP): Telemetry attribute field.

### 18. vendor_telephony
- vendor_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- vendor_name (VARCHAR / TIMESTAMP): Telemetry attribute field.
- vendor_account_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- timezone (VARCHAR / TIMESTAMP): Telemetry attribute field.
- status (VARCHAR / TIMESTAMP): Telemetry attribute field.
- schema_version (VARCHAR / TIMESTAMP): Telemetry attribute field.

### 19. whatsapp_events
- whatsapp_event_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- account_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- borrower_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- event_at (VARCHAR / TIMESTAMP): Telemetry attribute field.
- message_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
- event_type (VARCHAR / TIMESTAMP): Telemetry attribute field.
- template_code (VARCHAR / TIMESTAMP): Telemetry attribute field.
- provider_id (VARCHAR / TIMESTAMP): Telemetry attribute field.
