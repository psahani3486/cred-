import pytest
import pandas as pd
from src.cleaning import clean_payments
from src.metrics import compute_monthly_metrics

def test_metrics_calculation():
    pay = pd.read_csv('payments.csv')
    acc = pd.read_csv('accounts.csv')
    calls = pd.read_csv('calls.csv')
    targ = pd.read_csv('daily_targeting.csv')
    sessions = pd.read_csv('agent_sessions.csv')
    
    cleaned_pay = clean_payments(pay, acc)
    metrics_df = compute_monthly_metrics(cleaned_pay, acc, calls, targ, sessions)
    
    assert not metrics_df.empty
    assert 'golden_recovery_amt' in metrics_df.columns
    assert (metrics_df['recovery_rate_pct'] >= 0).all()
