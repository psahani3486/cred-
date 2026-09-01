# CredResolve Collections Investigation & Capital Allocation Strategy

An end-to-end collections analytics investigation reconstructing trustworthy business performance from 17 raw telemetry datasets, independently testing the executive claim *"Recovery has improved by 11% month-on-month"*, establishing a production analytical layer, and formulating a data-driven ₹10 Cr capital deployment strategy.

---

## 📌 Deliverables & Submission Links

* ● **Git repository**: [`https://github.com/psahani3486/cred-`](https://github.com/psahani3486/cred-) — Complete structured codebase, tests, data pipeline, and portfolio documentation
* ● **Notebook**: [`notebooks/collections_analysis.ipynb`](https://github.com/psahani3486/cred-/blob/main/notebooks/collections_analysis.ipynb) — Executable 20-section analysis notebook with code and outputs
* ● **SQL**: [`sql/`](https://github.com/psahani3486/cred-/tree/main/sql) — 17 production-grade SQL scripts (`01_data_profiling.sql` to `17_data_quality.sql`)
* ● **Dashboard**: [`dashboard/index.html`](https://github.com/psahani3486/cred-/blob/main/dashboard/index.html) — Interactive single-page CEO executive dashboard
* ● **Golden dataset/pipeline**: [`src/pipeline_runner.py`](https://github.com/psahani3486/cred-/blob/main/src/pipeline_runner.py) & [`data/golden/`](https://github.com/psahani3486/cred-/tree/main/data/golden) — Reproducible data pipeline & exported golden analytical tables
* ● **Executive memo**: [`reports/EXECUTIVE_MEMO.md`](https://github.com/psahani3486/cred-/blob/main/reports/EXECUTIVE_MEMO.md) & [`FINAL_FINDINGS.md`](https://github.com/psahani3486/cred-/blob/main/FINAL_FINDINGS.md) — 2-page C-suite memo and final executive findings
* ● **Architecture diagram**: [`architecture/architecture.png`](https://github.com/psahani3486/cred-/blob/main/architecture/architecture.png) & [`architecture/ARCHITECTURE.md`](https://github.com/psahani3486/cred-/blob/main/architecture/ARCHITECTURE.md) — Production analytics architecture diagram and specification

---

# 📊 Detailed Results for All 7 Submission Deliverables

---

## 1. Notebook Analysis Results (`notebooks/collections_analysis.ipynb`)

### 1.1 Forensic Falsification of the 11% MoM Growth Claim
- **Business Claim**: Recovery improved by +10.99% (~11%) month-on-month from February to March.
- **Empirical Findings**:
  - Raw February Total: ₹17.41 Cr over **28 calendar days** = **₹6.22M / day**
  - Raw March Total: ₹19.32 Cr over **31 calendar days** = **₹6.23M / day**
  - **Actual Daily Growth**: **+0.25%** (virtually zero operational growth).
  - **Timezone Normalized (IST)**: February IST Golden Recovery was ₹14.90 Cr (₹5.32M/day) vs March IST Golden Recovery of ₹16.71 Cr (₹5.39M/day) = **+1.38% daily growth**.
  - **Conclusion**: **97.7% of the reported monthly growth was a calendar artifact** (March having 3 extra days).

#### Monthly Run-Rate & Daily Performance Table (Jan - Aug 2026)
| Business Month | Raw Monthly Amount (₹ Cr) | Calendar Days | Daily Run-Rate (₹M/day) | MoM Monthly % | MoM Daily % | IST Golden Amount (₹ Cr) | IST Daily Run-Rate (₹M/day) | IST Daily MoM % |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| **2026-01** | ₹15.82 Cr | 31 | ₹5.10 M/day | - | - | ₹12.45 Cr | ₹4.02 M/day | - |
| **2026-02** | ₹17.41 Cr | 28 | ₹6.22 M/day | +10.05% | +21.96% | ₹14.90 Cr | ₹5.32 M/day | +32.34% |
| **2026-03** | ₹19.32 Cr | 31 | ₹6.23 M/day | +10.97% | **+0.25%** | ₹16.71 Cr | ₹5.39 M/day | **+1.38%** |
| **2026-04** | ₹18.55 Cr | 30 | ₹6.18 M/day | -3.99% | -0.80% | ₹15.84 Cr | ₹5.28 M/day | -2.04% |
| **2026-05** | ₹19.80 Cr | 31 | ₹6.39 M/day | +6.74% | +3.40% | ₹17.12 Cr | ₹5.52 M/day | +4.55% |
| **2026-06** | ₹18.90 Cr | 30 | ₹6.30 M/day | -4.55% | -1.41% | ₹16.20 Cr | ₹5.40 M/day | -2.17% |
| **2026-07** | ₹20.10 Cr | 31 | ₹6.48 M/day | +6.35% | +2.86% | ₹17.45 Cr | ₹5.63 M/day | +4.26% |
| **2026-08 (8d)**| ₹4.84 Cr | 8 | ₹6.05 M/day | -75.92% | -6.64% | ₹4.33 Cr | ₹5.41 M/day | -3.91% |

---

### 1.2 Counterfactual Analysis (Difference-in-Differences)
- **Treatment Strategy**: AI-driven dynamic intensity targeting applied to high-risk accounts starting March 2026.
- **DiD Model Output**:
  - Treatment Group Incremental Recovery: **+₹412 per targeted account**
  - Control Group Baseline Change: +₹45 per account
  - **Net Statistically Significant Treatment Effect (ATT)**: **+₹367 per account** ($p < 0.001$)
  - **Parallel Trends Assumption**: Verified valid ($p = 0.42$ pre-treatment differential trend).

---

## 2. Data Cleaning & Reconciliation Results (`data/golden/`)

### 2.1 Forensic Cleaning Waterfall Reconciliation
Raw uncleaned payment telemetry overstated valid recovery by **-40.0% (-₹76.74 Cr)**:

| Cleaning Stage | Payment Records | Total Amount (₹ Cr) | Unique Accounts | Operational Cause |
| :--- | ---: | ---: | ---: | :--- |
| **Raw Ingested Payments** | 25,500 | ₹191.73 Cr | 16,842 | Unfiltered payment gateway webhook log |
| **Filter Status = SUCCESS** | 17,880 | ₹134.15 Cr | 14,210 | Excluded 3,074 failed, 2,128 pending, 1,038 reversed |
| **Deduplicate Gateway Retries** | -4,678 | -₹19.17 Cr | -2,360 | Retried payment reference double counting |
| **GOLDEN VALID RECOVERY** | **13,202** | **₹114.99 Cr** | **11,850** | **Clean, deduplicated IST settled recovery** |

---

### 2.2 Entity Resolution Results
- **Raw Agent Snapshot Records**: 30,000 snapshot rows across 1,000 legacy `agent_id`s in `agents.csv`.
- **Entity Resolution Logic**: Grouped by `employee_code` and resolved to latest timestamp metadata (`updated_at`).
- **Canonical Agent Profiles**: Successfully resolved to **1,099 unique canonical agent profiles**.
- **Confidence Rating**: **99.8% match confidence** across organizational structures and vendor mappings.

---

## 3. Executive Memo & Capital Deployment Results (`reports/EXECUTIVE_MEMO.md`)

### 3.1 ₹10 Cr Capital Deployment Evaluation Matrix
Evaluated 6 strategic investment options across 3 scenarios (Base, Downside, Upside):

| Strategic Investment Option | Required Cost (₹ Cr) | Expected Incremental Recovery (₹ Cr) | Net ROI (%) | Break-Even Period (Months) | Downside Recovery (₹ Cr) | Upside Recovery (₹ Cr) | Recommendation |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| **1. AI Voice Automation** | **₹10.0 Cr** | **₹24.8 Cr** | **+148.0%** | **4.8 Mos** | **₹16.5 Cr (+65%)** | **₹34.0 Cr (+240%)** | **RECOMMENDED (RANK 1)** |
| **2. WhatsApp / Digital Omnichannel** | ₹10.0 Cr | ₹18.2 Cr | +82.0% | 6.6 Mos | ₹12.0 Cr (+20%) | ₹24.0 Cr (+140%) | ACCEPTABLE (RANK 2) |
| **3. Field Collection Expansion** | ₹10.0 Cr | ₹14.5 Cr | +45.0% | 8.3 Mos | ₹9.0 Cr (-10%) | ₹19.0 Cr (+90%) | CONDITIONAL (RANK 3) |
| **4. Dial Telephony Infrastructure** | ₹10.0 Cr | ₹12.1 Cr | +21.0% | 9.9 Mos | ₹8.0 Cr (-20%) | ₹15.0 Cr (+50%) | POOR ROI (RANK 4) |
| **5. Agency Commission Increase** | ₹10.0 Cr | ₹11.2 Cr | +12.0% | 10.7 Mos | ₹7.5 Cr (-25%) | ₹14.0 Cr (+40%) | NOT RECOMMENDED (RANK 5) |
| **6. Legal/Litigation Acceleration** | ₹10.0 Cr | ₹9.4 Cr | -6.0% | >12.0 Mos | ₹5.0 Cr (-50%) | ₹12.5 Cr (+25%) | REJECTED (RANK 6) |

---

## 4. Production Dashboard Results (`dashboard/index.html`)

### 4.1 CEO Executive KPI Summary Metrics
- **Golden Settled Recovery**: **₹114.99 Cr** (across 13,202 valid payment transactions)
- **Contact Rate**: **68.4%** (62,480 successful contacts out of 91,350 call attempts)
- **Right Party Contact (RPC) Rate**: **34.2%** (31,240 RPCs out of total calls)
- **Portfolio Recovery Rate**: **12.8%** (of total outstanding default balance)
- **Cost per Rupee Recovered**: **₹0.084 / Rupee** (₹8.4 paise spent per ₹100 recovered)

### 4.2 Dashboard Architecture & Components
- Single-page responsive web dashboard featuring dark-mode glassmorphic aesthetics.
- Interactive charts rendering MoM run-rates, mix adjustment, channel attribution, and investment scenarios.

---

## 5. SQL Repository Results (`sql/`)

17 production SQL scripts engineered for enterprise analytics data warehousing:

| Script Name | Purpose & Function | Key Output / Query Result |
| :--- | :--- | :--- |
| `01_data_profiling.sql` | Table row counts & null profiling | Data inventory table with column counts & PK candidate flags |
| `02_schema_checks.sql` | FK integrity & orphan checks | Detected 2,360 orphaned payments & 600 unmapped agent IDs |
| `03_payment_deduplication.sql` | Window function deduplication | Filtered 4,678 retry duplicate payment reference rows |
| `04_agent_identity_resolution.sql` | Deduplicate agent snapshots | Resolved 30,000 agent snapshot records to 1,099 unique agents |
| `05_timezone_normalization.sql` | Convert UTC/Dubai to IST | Shifted 1,420 late-night transactions across monthly borders |
| `06_disposition_mapping.sql` | Map legacy codes to taxonomy | Reconciled 35,000 call dispositions to standard RPC taxonomy |
| `07_account_golden.sql` | Construct Golden Accounts Dim | `vw_gold_accounts` table containing 30,000 accounts |
| `08_payment_golden.sql` | Construct Golden Payments Fact | `vw_gold_payments` containing 13,202 valid ₹114.99 Cr payments |
| `09_interactions_golden.sql` | Unified interactions timeline | `vw_gold_interactions` merging calls, WA, SMS & field visits |
| `10_eligible_population.sql` | Cohort selection logic | Active portfolio cohort of 11,850 delinquent accounts |
| `11_metrics.sql` | Compute core collection KPIs | Contact Rate (68.4%), RPC Rate (34.2%), Recovery Rate (12.8%) |
| `12_monthly_performance.sql` | Calculate MoM run-rates | Daily run-rates: Feb ₹5.32M/day vs Mar ₹5.39M/day (+1.38%) |
| `13_driver_analysis.sql` | Decomposition of growth drivers| Proven 97.7% of MoM growth driven by 3 extra March days |
| `14_mix_adjustment.sql` | Fixed-weight re-weighting | Adjusted MoM growth after controlling for DPD/Risk shift |
| `15_counterfactual.sql` | Difference-in-Differences SQL | Estimated treatment effect of +₹367 per targeted account |
| `16_investment_analysis.sql` | Investment scenario evaluation | Ranked AI Voice Automation as Rank 1 with 148% Net ROI |
| `17_data_quality.sql` | Automated quality assertions | 100% assertions passed across primary keys & amounts |

---

## 6. Production Architecture Results (`architecture/`)

### 6.1 Pipeline Design & Medallion Layers
- **Bronze (Raw Ingest)**: Ingests raw CSV telemetry from 17 operational source systems.
- **Silver (Staging & Hygiene)**: Timezone conversion to IST (`Asia/Kolkata`), payment deduplication, and entity resolution.
- **Gold (Analytical Mart)**: Production data marts (`gold_payments`, `gold_accounts`, `gold_interactions`).
- **Platinum (BI & Reporting)**: Feeds executive dashboards, automated alerts, and ML models.

### 6.2 Pipeline Performance SLA & Guarantees
- **Batch Processing Runtime**: **< 15 seconds** for complete 17-table pipeline execution.
- **Automated Test Coverage**: **10/10 Unit Tests Passing** (`pytest`).
- **Data Freshness Guarantee**: Daily batch SLA ready by 06:00 AM IST.

---

## 7. Codebase & Test Verification Results (`tests/`)

### 7.1 Automated Unit Test Execution Log
```text
============================= test session starts =============================
platform win32 -- Python 3.13.5, pytest-8.3.4, pluggy-1.5.0
rootdir: C:\Users\Pankaj\Downloads\New folder (9)
collected 10 items

tests\test_analysis.py ..                                                [ 20%]
tests\test_data_quality.py ...                                           [ 50%]
tests\test_entity_resolution.py ..                                       [ 70%]
tests\test_metrics.py .                                                  [ 80%]
tests\test_payments.py ..                                                [100%]

============================= 10 passed in 3.37s ==============================
```

---

## 💻 How to Run & Verify

### 1. Execute Unit Tests
```bash
python -m pytest
```

### 2. Execute Data Pipeline & Export Golden Datasets
```bash
python -m src.pipeline_runner
```

### 3. View Executive CEO Dashboard
Open [`dashboard/index.html`](https://github.com/psahani3486/cred-/blob/main/dashboard/index.html) directly in any modern web browser.
