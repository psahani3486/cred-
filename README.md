# CredResolve Collections Investigation & Capital Allocation Strategy

An end-to-end collections analytics investigation reconstructing trustworthy business performance from 17 raw telemetry datasets, independently testing the executive claim *"Recovery has improved by 11% month-on-month"*, establishing a production analytical layer, and formulating a data-driven ₹10 Cr capital deployment strategy.

---

## 📌 Submit:

* ● **Git repository**: [`https://github.com/psahani3486/cred-`](https://github.com/psahani3486/cred-) — Complete structured codebase, tests, data pipeline, and portfolio documentation
* ● **Notebook**: [`notebooks/collections_analysis.ipynb`](https://github.com/psahani3486/cred-/blob/main/notebooks/collections_analysis.ipynb) — Executable 20-section analysis notebook with code and outputs
* ● **SQL**: [`sql/`](https://github.com/psahani3486/cred-/tree/main/sql) — 17 production-grade SQL scripts (`01_data_profiling.sql` to `17_data_quality.sql`)
* ● **Dashboard**: [`dashboard/index.html`](https://github.com/psahani3486/cred-/blob/main/dashboard/index.html) — Interactive single-page CEO executive dashboard
* ● **Golden dataset/pipeline**: [`src/pipeline_runner.py`](https://github.com/psahani3486/cred-/blob/main/src/pipeline_runner.py) & [`data/golden/`](https://github.com/psahani3486/cred-/tree/main/data/golden) — Reproducible data pipeline & exported golden analytical tables
* ● **Executive memo**: [`reports/EXECUTIVE_MEMO.md`](https://github.com/psahani3486/cred-/blob/main/reports/EXECUTIVE_MEMO.md) & [`FINAL_FINDINGS.md`](https://github.com/psahani3486/cred-/blob/main/FINAL_FINDINGS.md) — 2-page C-suite memo and final executive findings
* ● **Architecture diagram**: [`architecture/architecture.png`](https://github.com/psahani3486/cred-/blob/main/architecture/architecture.png) & [`architecture/ARCHITECTURE.md`](https://github.com/psahani3486/cred-/blob/main/architecture/ARCHITECTURE.md) — Production analytics architecture diagram and specification

---

## 🔍 Key Investigation Findings & Executive Summary

### 1. Is the 11% Month-on-Month Improvement Claim Real?
> **VERDICT: FALSE / OPERATIONALLY MISLEADING**

- **Business Reported Metric**: Raw SUCCESS payment amount jumped from **₹17.41 Cr in February 2026** to **₹19.32 Cr in March 2026** (+10.99% ~ 11%).
- **My Reconstructed Golden Metric**: Daily run-rate IST recovery rose from **₹5.32M / day in Feb** to **₹5.39M / day in Mar** (**+1.38%**).
- **Root Cause**: **February has 28 days** while **March has 31 days** (+10.71% calendar days). 97% of the reported monthly recovery delta was purely a calendar expansion artifact. Real operational recovery was essentially flat.

---

### 2. Impact of Forensic Data Cleaning
Raw uncleaned payment telemetry overstated valid collections by **-40.0% (-₹76.74 Cr)**:

| Cleaning Stage | Payment Records | Total Amount (₹ Cr) | Unique Accounts |
| :--- | ---: | ---: | ---: |
| **Raw Ingested Payments** | 25,500 | ₹191.73 Cr | 16,842 |
| **Cleaned (Status = SUCCESS)** | 17,880 | ₹134.15 Cr | 14,210 |
| **GOLDEN VALID RECOVERY** | **13,202** | **₹114.99 Cr** | **11,850** |

*Data cleaning eliminated 4,678 duplicate payment references (retried gateway webhooks) and 5,028 failed/reversed payments.*

---

### 3. Recommended ₹10 Cr Capital Deployment Strategy

> **RECOMMENDATION: Invest ₹10 Cr in AI Voice Automation**

- **Capital Investment**: ₹10.0 Cr
- **Expected 12-Month Incremental Recovery**: **₹24.8 Cr**
- **Net ROI**: **+148.0%**
- **Break-Even Period**: **4.8 Months**
- **Downside Case**: ₹16.5 Cr incremental recovery (+65% Net ROI, 7.2M break-even)
- **Upside Case**: ₹34.0 Cr incremental recovery (+240% Net ROI, 3.5M break-even)
- **Confidence Rating**: **VERY HIGH (95% Confidence)**

---

## 🛠️ Repository Architecture & Codebase Layout

```text
collections-analytics/
│
├── README.md                           # Main portfolio documentation & submission guide
├── DATA_DICTIONARY.md                  # Comprehensive data dictionary for all 17 datasets
├── METRIC_DEFINITIONS.md               # Standardized mathematical & SQL metric definitions
├── 11_PERCENT_CLAIM_ANALYSIS.md        # Detailed forensic report falsifying the 11% claim
├── ASSUMPTIONS.md                      # Explicit record of analytical assumptions & rules
├── FINAL_FINDINGS.md                   # Executive findings structured per Section 39 schema
├── data_inventory.csv                  # Dataset row counts, column counts & PK/FK summary
├── requirements.txt                    # Python environment dependencies
│
├── dataset/                            # Cleanly organized raw CSV dataset directory
│   ├── account_status_history.csv
│   ├── accounts.csv
│   ├── agent_sessions.csv
│   ├── agents.csv
│   ├── borrowers.csv
│   ├── call_attempts.csv
│   ├── call_dispositions.csv
│   ├── calls.csv
│   ├── campaigns.csv
│   ├── complaints.csv
│   ├── daily_targeting.csv
│   ├── data_dictionary.csv
│   ├── data_inventory.csv
│   ├── field_visits.csv
│   ├── payments.csv
│   ├── promises_to_pay.csv
│   ├── sms_events.csv
│   ├── vendor_telephony.csv
│   └── whatsapp_events.csv
│
├── data/
│   ├── staging/                        # Cleaned IST transaction data
│   └── golden/                         # Exported Golden analytical tables
│
├── src/                                # Production Python Analytics Package
│   ├── __init__.py
│   ├── profiling.py                    # Automated dataset profiling module
│   ├── cleaning.py                     # Timezone normalization to IST & payment deduplication
│   ├── entity_resolution.py            # Agent identity resolution & canonical mapping
│   ├── attribution.py                  # Multi-touch interaction attribution engine
│   ├── metrics.py                      # Monthly performance metric calculation engine
│   ├── analysis.py                     # Mix adjustment, Simpson's paradox & DiD model
│   ├── investment.py                   # ₹10 Cr capital allocation & ROI evaluation
│   └── pipeline_runner.py              # End-to-end master execution pipeline
│
├── sql/                                # 17 Production SQL Scripts
│   ├── 01_data_profiling.sql
│   ├── 02_schema_checks.sql
│   ├── 03_payment_deduplication.sql
│   ├── 04_agent_identity_resolution.sql
│   ├── 05_timezone_normalization.sql
│   ├── 06_disposition_mapping.sql
│   ├── 07_account_golden.sql
│   ├── 08_payment_golden.sql
│   ├── 09_interactions_golden.sql
│   ├── 10_eligible_population.sql
│   ├── 11_metrics.sql
│   ├── 12_monthly_performance.sql
│   ├── 13_driver_analysis.sql
│   ├── 14_mix_adjustment.sql
│   ├── 15_counterfactual.sql
│   ├── 16_investment_analysis.sql
│   └── 17_data_quality.sql
│
├── notebooks/                          # Jupyter Analysis Notebook
│   └── collections_analysis.ipynb      # Executable 20-section analysis notebook
│
├── tests/                              # Automated Unit Test Suite (10/10 Passing)
│   ├── test_data_quality.py
│   ├── test_payments.py
│   ├── test_metrics.py
│   ├── test_entity_resolution.py
│   └── test_analysis.py
│
├── reports/                            # Executive Reports
│   ├── DATA_QUALITY_REPORT.md          # Data quality audit & cleaning reconciliation
│   └── EXECUTIVE_MEMO.md               # 2-page C-suite memo for CEO & leadership
│
├── architecture/                       # Production Pipeline Architecture
│   ├── ARCHITECTURE.md                 # Architecture design, contracts, SLA & lineage
│   └── architecture.png                # Pipeline flowchart diagram
│
├── golden/                             # Golden Layer Specifications
│   └── README.md
│
└── dashboard/                          # Interactive CEO Dashboard
    ├── index.html                      # Single-page HTML/CSS/JS dashboard
    └── README.md
```

---

## 💻 How to Run & Verify

### 1. Execute Unit Tests
```bash
python -m pytest
```
*Output: `10 passed in ~3.30s`*

### 2. Execute Data Pipeline & Export Golden Datasets
```bash
python -m src.pipeline_runner
```
*Exports all golden data tables to `data/golden/`.*

### 3. View Executive CEO Dashboard
Open [`dashboard/index.html`](https://github.com/psahani3486/cred-/blob/main/dashboard/index.html) directly in any modern web browser.
