import pandas as pd
import numpy as np

def perform_attribution_all_methods(payments_df, calls_df, wa_df, sms_df, field_df, window_days=7):
    """
    High-performance Multi-Touch Attribution Engine.
    Uses grouped lookups for instant multi-channel attribution across 13,000+ payments.
    """
    pay = payments_df[payments_df['is_valid'] == True].copy()
    pay['pay_dt'] = pd.to_datetime(pay['event_timestamp_ist'])
    
    # Standardize streams
    calls = calls_df.copy()
    calls['interaction_dt'] = pd.to_datetime(calls['event_at'])
    calls['channel'] = 'VOICE_CALL'
    
    wa = wa_df.copy()
    wa['interaction_dt'] = pd.to_datetime(wa['event_at'])
    wa['channel'] = 'WHATSAPP'
    wa['agent_id'] = 'DIGITAL_BOT'
    wa['campaign_id'] = wa['campaign_id'] if 'campaign_id' in wa.columns else 'DIGITAL_CAMPAIGN'
    
    sms = sms_df.copy()
    sms['interaction_dt'] = pd.to_datetime(sms['event_at'])
    sms['channel'] = 'SMS'
    sms['agent_id'] = 'DIGITAL_SMS'
    sms['campaign_id'] = sms['campaign_id'] if 'campaign_id' in sms.columns else 'SMS_CAMPAIGN'
    
    field = field_df.copy()
    field['interaction_dt'] = pd.to_datetime(field['event_at'])
    field['channel'] = 'FIELD_VISIT'
    field['campaign_id'] = 'FIELD_CAMPAIGN'
    
    cols = ['account_id', 'interaction_dt', 'channel', 'agent_id', 'campaign_id']
    
    interactions = pd.concat([
        calls[cols],
        wa[cols],
        sms[cols],
        field[cols]
    ], ignore_index=True)
    
    # Group interactions by account_id for fast lookup
    inter_by_acc = {acc_id: group for acc_id, group in interactions.groupby('account_id')}
    
    results = []
    for idx, prow in pay.iterrows():
        acc_id = prow['account_id']
        p_dt = prow['pay_dt']
        p_amt = prow['amount']
        
        acc_inter = inter_by_acc.get(acc_id, None)
        if acc_inter is not None:
            eligible = acc_inter[(acc_inter['interaction_dt'] <= p_dt) & 
                                 (acc_inter['interaction_dt'] >= p_dt - pd.Timedelta(days=window_days))]
        else:
            eligible = None
            
        if eligible is not None and not eligible.empty:
            acc_inter_sorted = eligible.sort_values('interaction_dt')
            
            last_touch = acc_inter_sorted.iloc[-1]
            last_channel = last_touch['channel']
            last_agent = str(last_touch['agent_id'])
            last_camp = str(last_touch['campaign_id'])
            
            first_touch = acc_inter_sorted.iloc[0]
            first_channel = first_touch['channel']
            
            channel_count = acc_inter_sorted['channel'].nunique()
            attr_type = 'MULTI_TOUCH' if channel_count > 1 else 'SINGLE_TOUCH'
            confidence = 0.92 if last_channel in ['VOICE_CALL', 'FIELD_VISIT'] else 0.85
        else:
            last_channel = 'ORGANIC_SELF_SERVE'
            last_agent = 'ORGANIC'
            last_camp = 'ORGANIC_PAYMENT'
            first_channel = 'ORGANIC_SELF_SERVE'
            attr_type = 'NO_TOUCHPOINT'
            confidence = 0.50
            
        results.append({
            'payment_id': prow['payment_id'],
            'account_id': acc_id,
            'amount': p_amt,
            'business_date': prow['business_date'],
            'attributed_last_channel': last_channel,
            'attributed_first_channel': first_channel,
            'attributed_agent': last_agent,
            'attributed_campaign': last_camp,
            'attribution_type': attr_type,
            'confidence': confidence
        })
        
    return pd.DataFrame(results)
