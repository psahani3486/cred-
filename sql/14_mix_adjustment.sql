-- 14_mix_adjustment.sql
-- Raw vs Mix-Adjusted Recovery Comparison
SELECT 
    b_month,
    raw_recovery,
    mix_adjusted_recovery,
    (raw_recovery - mix_adjusted_recovery) / mix_adjusted_recovery * 100 AS variance_pct
FROM monthly_mix_summary;