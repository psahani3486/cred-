import pandas as pd
import numpy as np

def compute_monthly_metrics(gold_payments, accounts_df, calls_df, targeting_df, agent_sessions_df):
    """
    Computes rigorous monthly performance metrics for the Golden Dataset.
    """
    gold_pay = gold_payments[gold_payments['is_valid'] == True].copy()
    
    months = sorted(gold_pay['business_month'].unique())
    metrics_list = []
    
    total_eligible_accounts = accounts_df['account_id'].nunique()
    total_outstanding_balance = accounts_df['outstanding_amount'].sum()
    
    for m in months:
        m_pay = gold_pay[gold_pay['business_month'] == m]
        m_calls = calls_df[calls_df['business_month'] == m] if 'business_month' in calls_df.columns else calls_df
        m_targ = targeting_df[targeting_df['business_month'] == m] if 'business_month' in targeting_df.columns else targeting_df
        
        recovery_amt = m_pay['amount'].sum()
        valid_txns = len(m_pay)
        paying_accounts = m_pay['account_id'].nunique()
        
        targeted_accounts = m_targ['account_id'].nunique() if not m_targ.empty else 0
        attempts_cnt = len(m_calls)
        contacts_cnt = len(m_calls[m_calls['call_status'] == 'ANSWERED'])
        
        # Operational cost estimation (Voice call = ₹3, Agent hour = ₹250, Digital = ₹0.20)
        agent_hours = 1200  # Avg active productive hours per month
        op_cost = (attempts_cnt * 3.0) + (agent_hours * 250.0) + 150000.0
        
        metrics_list.append({
            'business_month': str(m),
            'eligible_accounts': total_eligible_accounts,
            'outstanding_balance': total_outstanding_balance,
            'targeted_accounts': targeted_accounts,
            'attempts': attempts_cnt,
            'contacts': contacts_cnt,
            'contact_rate_pct': round((contacts_cnt / max(1, targeted_accounts)) * 100, 2),
            'golden_recovery_amt': recovery_amt,
            'paying_accounts': paying_accounts,
            'recovery_rate_pct': round((recovery_amt / total_outstanding_balance) * 100, 4),
            'recovery_per_account': round(recovery_amt / total_eligible_accounts, 2),
            'recovery_per_agent_hour': round(recovery_amt / max(1, agent_hours), 2),
            'cost_per_rupee_recovered': round(op_cost / max(1.0, recovery_amt), 4)
        })
        
    return pd.DataFrame(metrics_list)
