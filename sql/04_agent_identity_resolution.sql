-- 04_agent_identity_resolution.sql
-- Maps multiple agent records to canonical employee code
SELECT 
    employee_code,
    COUNT(DISTINCT agent_id) AS distinct_agent_ids,
    MAX(agent_name) AS agent_name,
    MAX(updated_at) AS latest_update
FROM agents
GROUP BY employee_code;