import pandas as pd
import numpy as np

def convert_to_ist(df, date_col='event_at', tz_col='timezone'):
    """
    Normalizes mixed UTC, Asia/Dubai, and Asia/Kolkata timestamps into Asia/Kolkata IST.
    """
    df = df.copy()
    dt = pd.to_datetime(df[date_col], errors='coerce')
    
    offsets = pd.Series(pd.Timedelta(hours=0), index=df.index)
    if tz_col in df.columns:
        offsets.loc[df[tz_col] == 'UTC'] = pd.Timedelta(hours=5, minutes=30)
        offsets.loc[df[tz_col] == 'Asia/Dubai'] = pd.Timedelta(hours=1, minutes=30)
    
    ist_dt = dt + offsets
    df['event_timestamp_utc'] = dt
    df['event_timestamp_ist'] = ist_dt
    df['business_date'] = ist_dt.dt.date
    df['business_hour'] = ist_dt.dt.hour
    df['business_month'] = ist_dt.dt.to_period('M')
    return df

def clean_payments(pay_df, acc_df):
    """
    Deduplicates payments, filters valid SUCCESS transactions, maps timezones,
    and flags exclusions with explicit reasons.
    """
    pay = pay_df.copy()
    if 'timezone' not in pay.columns and 'account_id' in pay.columns:
        pay = pay.merge(acc_df[['account_id', 'timezone']], on='account_id', how='left')
    
    pay = convert_to_ist(pay, 'event_at', 'timezone')
    
    # Exclusion flags
    pay['is_duplicate'] = pay.duplicated(subset=['payment_reference'], keep='first')
    pay['is_valid_status'] = pay['payment_status'] == 'SUCCESS'
    pay['is_valid'] = (~pay['is_duplicate']) & pay['is_valid_status']
    
    reasons = []
    for idx, row in pay.iterrows():
        if row['is_duplicate']:
            reasons.append('DUPLICATE_PAYMENT_REFERENCE')
        elif row['payment_status'] == 'FAILED':
            reasons.append('PAYMENT_FAILED')
        elif row['payment_status'] == 'REVERSED':
            reasons.append('PAYMENT_REVERSED')
        elif row['payment_status'] == 'PENDING':
            reasons.append('PAYMENT_PENDING')
        else:
            reasons.append('NONE')
    pay['exclusion_reason'] = reasons
    return pay

def map_disposition_codes(disp_df):
    """
    Standardizes raw disposition codes into canonical categories:
    RPC, PTP, NO_CONTACT, REFUSED, DISPUTE.
    """
    disp = disp_df.copy()
    mapping = {
        'PROMISE_TO_PAY': 'PTP',
        'PTP': 'PTP',
        'PAID': 'PTP',
        'CALLBACK': 'RPC',
        'WRONG_NUMBER': 'NO_CONTACT',
        'NO_CONTACT': 'NO_CONTACT',
        'REFUSED': 'REFUSED',
        'DISPUTE': 'DISPUTE',
        'PTP_BROKEN': 'RPC'
    }
    disp['standard_disposition'] = disp['disposition_code'].map(mapping).fillna('OTHER')
    disp['is_rpc'] = disp['standard_disposition'].isin(['RPC', 'PTP'])
    disp['is_ptp'] = disp['standard_disposition'] == 'PTP'
    return disp
