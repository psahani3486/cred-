import pytest
import os
import pandas as pd
from src.cleaning import clean_payments

def get_csv_path(filename):
    if os.path.exists(os.path.join('dataset', filename)):
        return os.path.join('dataset', filename)
    return filename

def test_payment_deduplication():
    pay = pd.read_csv(get_csv_path('payments.csv'))
    acc = pd.read_csv(get_csv_path('accounts.csv'))
    cleaned = clean_payments(pay, acc)
    
    assert 'is_duplicate' in cleaned.columns
    assert 'is_valid' in cleaned.columns
    
    valid_count = cleaned['is_valid'].sum()
    assert valid_count <= len(pay)
    assert valid_count > 0

def test_payment_positive_amount():
    pay = pd.read_csv(get_csv_path('payments.csv'))
    assert (pay['amount'] > 0).all(), "All payment amounts must be strictly positive"
