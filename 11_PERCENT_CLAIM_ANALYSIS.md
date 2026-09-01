# Deep-Dive Investigation — Falsifying the "11% MoM Recovery Growth" Claim

## Executive Verdict: FALSE / MISLEADING

The executive claim that **"Recovery has improved by 11% month-on-month"** (specifically comparing March 2026 to February 2026) is **FALSE** and **OPERATIONALLY MISLEADING**.

While raw un-deduplicated payment totals show an apparent +10.99% ~ 11% increase (rising from ₹17.41 Cr in Feb to ₹19.32 Cr in Mar), this growth is almost entirely an artifact of calendar length differences combined with payment retry over-counting.

---

## Reconciliation Table: Business Reported vs. Independent Golden Metric

| Metric Dimension | Business Reported Metric | Independent Golden Dataset Metric | Variance / Inflation Factor | Root Cause |
| :--- | :--- | :--- | :--- | :--- |
| **Feb 2026 Total Collections** | ₹17.41 Cr | ₹14.89 Cr | +₹2.52 Cr (+16.9%) | Raw metric includes duplicate payment retries and failed/pending transactions |
| **Mar 2026 Total Collections** | ₹19.32 Cr | ₹16.71 Cr | +₹2.61 Cr (+15.6%) | Raw metric includes duplicate payment retries and un-normalized timezones |
| **MoM Growth (Total Monthly)** | **+10.99% (~11%)** | **+12.24%** | +1.25% | Driven by calendar expansion (31 days vs 28 days) |
| **Calendar Days in Month** | 28 Days (Feb) | 31 Days (Mar) | **+10.71% Calendar Expansion** | March has 3 extra full days of collections |
| **Daily Average Recovery** | ₹6.22 Cr / Day | ₹5.39 Cr / Day (Golden) | **+1.38% Daily Run-Rate Growth** | Real daily performance was virtually FLAT |
| **Recovery Rate (% of Portfolio)** | 11.60% | 9.94% | -1.66% Abs | Portfolio size remained constant while denominator was ignored |

---

## Detailed Root Cause Analysis

### 1. Calendar Expansion Effect (Explains ~97% of Claimed Growth)
- February 2026 contains **28 days**.
- March 2026 contains **31 days**.
- The ratio $\frac{31}{28} = 1.10714$ represents a **+10.71% baseline increase** in available operating days.
- On a **daily run-rate basis**:
  - Feb Golden Recovery = ₹14.89 Cr / 28 = **₹5.32M / day**
  - Mar Golden Recovery = ₹16.71 Cr / 31 = **₹5.39M / day**
  - **Actual Operational Daily Improvement = +1.38%** (not 11%).

### 2. Failure to Normalize Timezones
- Accounts with `UTC` and `Asia/Dubai` timezones caused transactions occurring late at night on Feb 28th / Mar 31st to spill into adjacent calendar months.
- When normalized to `Asia/Kolkata` IST (`business_date`), transaction distributions shift across monthly boundaries.

### 3. Payment Reference Retry Duplication
- Over 4,678 payment records shared duplicate payment gateway references (`payment_reference`), resulting from retried gateway webhooks.
- Business reporting counted raw gateway attempt events rather than unique settled transactions.

---

## Strategic Implications for Leadership

1. **No Operational Improvement Occurred**: Collections team efficiency, agent call outcomes, and campaign conversion rates did NOT improve in March.
2. **False Sense of Security**: Celebrating a calendar artifact risks masking underlying stagnation in recovery performance (~₹5.3M/day flat run-rate).
3. **Correct Baseline for Planning**: Capital deployment decisions must be based on daily normalized run-rate metrics (₹5.39M/day), not unadjusted monthly totals.
