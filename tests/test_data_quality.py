import pytest
import pandas as pd
import numpy as np

def test_accounts_primary_key():
    df = pd.read_csv('accounts.csv')
    assert df['account_id'].nunique() == len(df), "account_id must be unique primary key"

def test_payments_non_null():
    df = pd.read_csv('payments.csv')
    assert df['payment_id'].notnull().all(), "payment_id cannot contain nulls"
    assert df['amount'].notnull().all(), "amount cannot contain nulls"

def test_borrowers_duplicate_rate():
    df = pd.read_csv('borrowers.csv')
    dup_rate = df.duplicated().mean() * 100
    assert dup_rate < 5.0, f"Borrowers duplicate rate ({dup_rate:.2f}%) exceeds threshold"
