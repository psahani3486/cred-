import pytest
import pandas as pd
from src.cleaning import clean_payments

def test_payment_deduplication():
    pay = pd.read_csv('payments.csv')
    acc = pd.read_csv('accounts.csv')
    cleaned = clean_payments(pay, acc)
    
    assert 'is_duplicate' in cleaned.columns
    assert 'is_valid' in cleaned.columns
    
    valid_count = cleaned['is_valid'].sum()
    assert valid_count <= len(pay)
    assert valid_count > 0

def test_payment_positive_amount():
    pay = pd.read_csv('payments.csv')
    assert (pay['amount'] > 0).all(), "All payment amounts must be strictly positive"
