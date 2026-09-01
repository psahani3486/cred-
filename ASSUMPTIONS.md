# Explicit Analytical Assumptions & Business Rules

Documentation of all core assumptions, timezone rules, cost structures, and analytical choices.

---

## 1. Timezone Normalization Rules
- All timestamps in `accounts`, `calls`, `payments`, `call_attempts`, `call_dispositions`, `field_visits`, `whatsapp_events`, `sms_events`, `promises_to_pay`, `account_status_history`, and `agent_sessions` are parsed and converted to `Asia/Kolkata` (IST, UTC+5:30).
- `UTC` timestamps add +5 hours 30 minutes.
- `Asia/Dubai` timestamps add +1 hour 30 minutes.
- Business reporting utilizes `business_date` (calendar date in IST) and `business_month` (calendar month in IST).

---

## 2. Payment Validity & Deduplication Rules
- A payment is classified as **VALID GOLDEN RECOVERY** if and only if:
  1. `payment_status` == `'SUCCESS'`.
  2. `payment_reference` is unique (the earliest timestamp record is kept; subsequent identical references are flagged as `DUPLICATE_PAYMENT_REFERENCE`).
  3. `amount` > 0.
- Transactions marked as `FAILED`, `PENDING`, or `REVERSED` are explicitly excluded from recovery numerators and tracked in the Data Quality audit.

---

## 3. Telephony & Interaction Assumptions
- Voice calls with status `'ANSWERED'` and disposition codes `'RPC'`, `'PTP'`, or `'CALLBACK'` are classified as Right Party Contacts (RPC).
- Interaction attribution window is set to **7 days** prior to payment date.

---

## 4. Cost Structure & Operational Unit Economics
- Voice Call Attempt Cost: ₹3.00 per attempt
- Productive Agent Hourly Rate: ₹250.00 / hour
- AI Voice Automated Call Cost: ₹0.30 per minute (1/10th human cost)
- WhatsApp Message Delivery Cost: ₹0.20 per delivered message
- Physical Field Visit Cost: ₹350.00 per visit
