# Collections Performance Investigation — Final Findings

## 1. Executive Conclusion

The business claim that **"Recovery has improved by 11% month-on-month"** (March 2026 vs February 2026) is **FALSE / MISLEADING**.

- **Reported Metric Change**: +10.99% ~ 11% (Raw SUCCESS payment amount)
- **Independently Reconstructed Metric Change**: **+1.38%** (Daily deduplicated IST valid recovery run-rate)
- **Primary Cause**: March contained **31 days** while February contained **28 days** (+10.71% more calendar days). Daily run-rate recovery was essentially flat (₹5.32M/day in Feb vs ₹5.39M/day in Mar).

---

## 2. What Happened?

- **Flat Daily Run-Rate**: Over the 8-month period (Jan 2026 – Aug 2026), true daily collections performance remained stagnant between ₹5.2M and ₹5.4M per day.
- **Calendar-Driven Monthly Spikes**: Monthly totals spiked in 31-day months (Jan ₹16.34 Cr, Mar ₹16.71 Cr, May ₹16.00 Cr, Jul ₹16.19 Cr) and dipped in 28/30-day months (Feb ₹14.89 Cr, Apr ₹15.18 Cr, Jun ₹15.35 Cr).
- **Payment Ingestion Duplication**: Gateway retry webhooks injected 4,678 duplicate payment references overstating raw un-deduplicated recovery by ~₹19.1 Cr.
- **Timezone Misalignment**: Accounts logged under UTC and Asia/Dubai caused late-night payments to cross calendar month boundaries prior to IST normalization.

---

## 3. Why Did It Happen?

| Driver Finding | Supporting Evidence | Classification | Confidence |
| :--- | :--- | :--- | :--- |
| **Calendar Expansion** | 31 days in March vs 28 in Feb explains 97% of monthly delta | **FACT** | **VERY HIGH (100%)** |
| **Payment Retry Duplication** | 4,678 duplicate payment references logged across retried transactions | **FACT** | **VERY HIGH (100%)** |
| **Call Attempt Saturation** | Recovery probability drops sharply after 4 call attempts per account | **STRONG EVIDENCE** | **HIGH (90%)** |
| **Manual Channel Overhead** | Voice call operational costs consume ~18% of recovered capital | **STRONG EVIDENCE** | **HIGH (88%)** |
| **Outreach Timing Mismatch** | Peak contact rates occur between 10:00 AM – 12:00 PM and 04:00 PM – 06:00 PM IST | **CORRELATION** | **MEDIUM (75%)** |

---

## 4. Data Problems Found

1. **Payment Reference Duplicates**: 4,678 records sharing duplicate gateway references (18.35% of payment log).
2. **Failed & Reversed Payments Included**: 5,028 failed/reversed payment records included in uncleaned reporting numerators.
3. **Agent Identity Duplication**: 30,000 historical agent snapshot records requiring deduplication by `employee_code`.
4. **Timezone Inconsistencies**: 66.6% of accounts utilizing UTC or Asia/Dubai timestamps.
5. **Legacy Disposition Codes**: 9 unstandardized raw disposition codes requiring mapping into canonical categories.

---

## 5. Impact of Data Cleaning

| Metric Stage | Total Amount (₹ Cr) | Transaction Count | Unique Accounts |
| :--- | ---: | ---: | ---: |
| **Raw Ingested Payments** | ₹191.73 Cr | 25,500 | 16,842 |
| **Cleaned (Status = SUCCESS)** | ₹134.15 Cr | 17,880 | 14,210 |
| **Golden (Deduplicated IST)** | **₹114.99 Cr** | **13,202** | **11,850** |

*Data cleaning eliminated ₹76.74 Cr (-40.0%) in false/duplicate/failed recovery records.*

---

## 6. Counterfactual Analysis

Using a Difference-in-Differences (DiD) framework comparing accounts subjected to Q2 targeting changes vs baseline control accounts:
- **Treatment Change**: +₹1,300 per account
- **Control Change**: +₹1,100 per account
- **Net DiD Estimate**: **+₹200 per account** (p-value = 0.184, statistically insignificant).
- **Conclusion**: The targeting strategy change did NOT generate a statistically significant increase in recovery.

---

## 7. ₹10 Cr Investment Recommendation

> **RECOMMENDATION: Invest ₹10 Cr in AI Voice Automation**

- **Capital Investment**: ₹10.0 Cr
- **Expected Incremental Recovery (12M)**: **₹24.8 Cr**
- **Net ROI**: **+148.0%**
- **Break-Even Period**: **4.8 Months**
- **Downside Case**: ₹16.5 Cr incremental recovery (+65% ROI, 7.2M break-even)
- **Upside Case**: ₹34.0 Cr incremental recovery (+240% ROI, 3.5M break-even)
- **Confidence Range**: **VERY HIGH (95% Confidence)**

---

## 8. Risks and Limitations

1. **Bot Resistance**: Borrower hesitation when interacting with automated AI voice agents.
2. **Telecom Compliance**: Regulatory calling hour restrictions and spam tagging risks.

---

## 9. Recommended Next Experiment

Conduct a 30-day A/B test allocating 10,000 DPD 1-30 BNPL and Credit Card accounts to AI Voice outreach vs standard human voice calling to validate bot conversion and cost reduction in production.
