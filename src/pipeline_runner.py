import os
import pandas as pd
import numpy as np
from src.profiling import generate_inventory
from src.cleaning import clean_payments, map_disposition_codes
from src.entity_resolution import resolve_agent_identities
from src.attribution import perform_attribution_all_methods
from src.metrics import compute_monthly_metrics
from src.analysis import perform_mix_adjustment, perform_counterfactual_did, detect_simpsons_paradox, run_did_statistical_model
from src.investment import evaluate_investments

def load_table(name, data_dir='dataset'):
    path = os.path.join(data_dir, f"{name}.csv")
    if not os.path.exists(path):
        path = f"{name}.csv"
    return pd.read_csv(path)

def run_full_pipeline():
    print("=== EXECUTING COMPLETE PRODUCTION ANALYTICS PIPELINE ===")
    
    os.makedirs('data/raw', exist_ok=True)
    os.makedirs('data/staging', exist_ok=True)
    os.makedirs('data/golden', exist_ok=True)
    
    data_dir = 'dataset' if os.path.exists('dataset') else '.'
    
    # 1. Profile datasets
    print("[1/8] Generating dataset inventory...")
    inv_df = generate_inventory(data_dir)
    
    # 2. Load tables
    print(f"[2/8] Reading raw CSV telemetry files from '{data_dir}'...")
    pay = load_table('payments', data_dir)
    acc = load_table('accounts', data_dir)
    agents = load_table('agents', data_dir)
    calls = load_table('calls', data_dir)
    disps = load_table('call_dispositions', data_dir)
    targ = load_table('daily_targeting', data_dir)
    sessions = load_table('agent_sessions', data_dir)
    wa = load_table('whatsapp_events', data_dir)
    sms = load_table('sms_events', data_dir)
    field = load_table('field_visits', data_dir)
    
    # 3. Entity Resolution
    print("[3/8] Resolving agent employee codes to canonical IDs...")
    agent_map = resolve_agent_identities(agents)
    agent_map.to_csv('data/golden/agent_identity_map.csv', index=False)
    
    # 4. Cleaning & Timezones
    print("[4/8] Deduplicating payment references & converting timezones to IST...")
    cleaned_pay = clean_payments(pay, acc)
    cleaned_pay.to_csv('data/staging/payments_cleaned.csv', index=False)
    
    gold_pay = cleaned_pay[cleaned_pay['is_valid'] == True].copy()
    gold_pay.to_csv('data/golden/gold_payments.csv', index=False)
    
    # 5. Multi-Touch Attribution
    print("[5/8] Running multi-touch channel attribution model...")
    attr_df = perform_attribution_all_methods(cleaned_pay, calls, wa, sms, field, window_days=7)
    attr_df.to_csv('data/golden/payment_attribution.csv', index=False)
    
    # 6. Monthly Metrics & Mix Adjustment
    print("[6/8] Computing monthly Golden metrics & mix adjustment...")
    metrics_df = compute_monthly_metrics(gold_pay, acc, calls, targ, sessions)
    metrics_df.to_csv('data/golden/monthly_performance_metrics.csv', index=False)
    
    mix_df = perform_mix_adjustment(gold_pay, acc)
    mix_df.to_csv('data/golden/mix_adjusted_recovery.csv', index=False)
    
    # 7. DiD & Simpson's Paradox
    print("[7/8] Executing DiD counterfactual statistical model...")
    did_res = run_did_statistical_model(targ, gold_pay, acc)
    pd.DataFrame([did_res]).to_csv('data/golden/did_counterfactual_results.csv', index=False)
    
    simpson_res = detect_simpsons_paradox(gold_pay, acc)
    
    # 8. Investment Scenarios
    print("[8/8] Evaluating 10 Cr INR capital deployment options...")
    inv_df = evaluate_investments(10.0)
    inv_df.to_csv('data/golden/investment_scenarios.csv', index=False)
    
    print("=== COMPLETE PIPELINE EXECUTED! All golden artifacts exported to data/golden/ ===")

if __name__ == '__main__':
    run_full_pipeline()
