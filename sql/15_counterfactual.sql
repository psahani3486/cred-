-- 15_counterfactual.sql
-- Counterfactual Difference-in-Differences Model Query
SELECT 
    treatment_group,
    pre_period_recovery,
    post_period_recovery,
    (post_period_recovery - pre_period_recovery) AS treatment_diff
FROM counterfactual_analysis;