-- 16_investment_analysis.sql
-- Investment evaluation comparison across 6 options
SELECT 
    option_name,
    cost_cr,
    expected_incremental_recovery_cr,
    (expected_incremental_recovery_cr - cost_cr) / cost_cr * 100 AS roi_pct,
    breakeven_months
FROM investment_options;