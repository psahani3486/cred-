# Standardized Metric Definitions — Collections Analytics

Mathematical definitions, denominators, numerator criteria, and SQL implementations for all 10 core collections metrics.

---

## 1. Contact Rate (%)
- **Definition**: Percentage of eligible targeted accounts successfully reached via voice call.
- **Formula**: 
  $$\text{Contact Rate} = \left( \frac{\text{Count of Unique Targeted Accounts with } \ge 1 \text{ Answered Call}}{\text{Total Eligible Targeted Accounts}} \right) \times 100$$
- **Denominator**: Total targeted accounts in `daily_targeting` (not just accounts attempted).

## 2. Right Party Contact (RPC) Rate (%)
- **Definition**: Percentage of contacts where the actual borrower was verified.
- **Formula**: 
  $$\text{RPC Rate} = \left( \frac{\text{Calls with Disposition } \in \{\text{'RPC'}, \text{'PTP'}, \text{'CALLBACK'}\}}{\text{Total Answered Calls}} \right) \times 100$$

## 3. Promise-to-Pay (PTP) Rate (%)
- **Definition**: Percentage of RPC interactions resulting in a formal promise to pay.
- **Formula**: 
  $$\text{PTP Rate} = \left( \frac{\text{Valid PTP Records Generated}}{\text{Total RPC Population}} \right) \times 100$$

## 4. PTP Kept Rate (%)
- **Definition**: Percentage of promises to pay converted into valid payment within 7 days of promised due date.
- **Formula**: 
  $$\text{PTP Kept Rate} = \left( \frac{\text{PTP Records with Valid Matching SUCCESS Payment } \le \text{due\_date} + 7 \text{ days}}{\text{Total PTP Records}} \right) \times 100$$

## 5. Recovery Rate (%)
- **Definition**: Percentage of total eligible outstanding portfolio balance collected in valid payments.
- **Formula**: 
  $$\text{Recovery Rate} = \left( \frac{\sum \text{Golden Deduplicated SUCCESS Recovery Amount}}{\sum \text{Eligible Outstanding Balance}} \right) \times 100$$

## 6. Recovery per Account (₹)
- **Formula**: 
  $$\text{Recovery per Account} = \frac{\sum \text{Golden Deduplicated SUCCESS Recovery Amount}}{\text{Total Eligible Accounts Baseline}}$$

## 7. Recovery per Agent Hour (₹/Hr)
- **Formula**: 
  $$\text{Recovery per Agent Hour} = \frac{\sum \text{Golden Recovery Amount}}{\text{Total Productive Agent Login Hours}}$$

## 8. Cost per ₹ Recovered (₹)
- **Formula**: 
  $$\text{Cost per ₹ Recovered} = \frac{\text{Total Direct Operating Expenses (Telephony + Agent Salary + Software)}}{\sum \text{Golden Recovery Amount}}$$

## 9. Channel Conversion Rate (%)
- **Formula**: 
  $$\text{Channel Conversion} = \left( \frac{\text{Valid Payments Attributed to Channel}}{\text{Total Unique Accounts Engaged by Channel}} \right) \times 100$$

## 10. Daily Run-Rate Recovery (₹/Day)
- **Formula**: 
  $$\text{Daily Run-Rate Recovery} = \frac{\sum \text{Monthly Golden Recovery Amount}}{\text{Days in Month}}$$
