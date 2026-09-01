# Comprehensive Data Quality Audit Report — CredResolve

Data hygiene, anomaly detection, deduplication results, timezone normalization impact, and cleaning reconciliation across 17 datasets.

---

## Data Quality Summary Table

| Data Issue | Detection Method | Count / Volume | Affected Rate (%) | Pipeline Treatment | Business Impact |
| :--- | :--- | ---: | ---: | :--- | :--- |
| **Payment Reference Duplicates** | Exact matching on `payment_reference` | 4,678 rows | 18.35% | Deduplicate keeping earliest SUCCESS record | Eliminates ₹19.1 Cr in artificial recovery inflation |
| **Failed Payments Ingestion** | `payment_status` == `'FAILED'` | 3,744 rows | 14.68% | Filter out of recovery numerator | Prevents non-existent revenue recognition |
| **Reversed / Chargeback Payments** | `payment_status` == `'REVERSED'` | 1,284 rows | 5.04% | Reconcile against net recovery | Excludes ₹9.5 Cr in uncollected revenue |
| **Agent Identity Duplication** | Multiple `agent_id`s per `employee_code` | 396 duplicates | 1.32% | Map to canonical `employee_code` | Fixes skewed agent productivity & tenure metrics |
| **Timezone Boundary Shifts** | Unnormalized UTC & Dubai timestamps | 19,979 accounts | 66.60% | Convert all timestamps to `Asia/Kolkata` IST | Adjusts transaction assignment across monthly bounds |
| **Legacy Disposition Codes** | 9 unstandardized string codes | 35,000 disps | 100.0% | Map into 5 standard canonical categories | Standardizes Contact Rate & PTP Rate reporting |
| **Borrower Table Duplicates** | Duplicate `borrower_id` rows | 600 rows | 1.96% | Deduplicate by `borrower_id` & latest timestamp | Ensures clean 1:1 borrower metadata mapping |

---

## Raw -> Clean -> Golden Reconciliation Table

| Cleaning Stage | Total Payment Records | Total Amount (₹ Cr) | Unique Accounts |
| :--- | ---: | ---: | ---: |
| **Raw Payments Ingested** | 25,500 | ₹191.73 Cr | 16,842 |
| **Excluded: FAILED Payments** | -3,744 | -₹28.40 Cr | -2,105 |
| **Excluded: PENDING Payments** | -2,592 | -₹19.49 Cr | -1,650 |
| **Excluded: REVERSED Payments** | -1,284 | -₹9.69 Cr | -890 |
| **Excluded: Reference Duplicates** | -4,678 | -₹19.17 Cr | -2,340 |
| **GOLDEN VALID PAYMENTS** | **13,202** | **₹114.99 Cr** | **11,850** |

---

## Key Data Quality Insights

1. **Massive Over-Reporting in Raw Data**: Raw ingested payments contained ₹191.73 Cr, but valid settled Golden payments totaled only **₹114.99 Cr** (-40.0% reduction!).
2. **Duplicate Webhook Ingestion**: Gateway retry webhooks resulted in 4,678 duplicate payment references being logged. Without deduplication, monthly recovery reports suffered severe artificial inflation.
3. **Agent Master Snapshot Inconsistency**: The `agents.csv` file contained 30,000 historical snapshot records for 1,000 unique agent IDs and 1,099 employee codes. Deduplicating by `employee_code` established a clean canonical mapping.
