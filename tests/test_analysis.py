import pytest
import pandas as pd
from src.investment import evaluate_investments
from src.analysis import perform_mix_adjustment, perform_counterfactual_did

def test_evaluate_investments():
    inv_df = evaluate_investments(10.0)
    assert len(inv_df) == 6
    assert 'roi_pct' in inv_df.columns
    
    rec_option = inv_df[inv_df['investment_option'].str.contains('AI Voice')]
    assert not rec_option.empty
    assert rec_option.iloc[0]['roi_pct'] > 100.0

def test_counterfactual_did():
    pay = pd.read_csv('payments.csv')
    targ = pd.read_csv('daily_targeting.csv')
    res = perform_counterfactual_did(targ, pay)
    assert 'did_estimate_per_account' in res
    assert 'parallel_trends_valid' in res
