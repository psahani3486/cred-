import json
import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

nb = {
    'cells': [],
    'metadata': {
        'language_info': {
            'name': 'python'
        }
    },
    'nbformat': 4,
    'nbformat_minor': 2
}

def add_md(text):
    nb['cells'].append({
        'cell_type': 'markdown',
        'metadata': {},
        'source': [line + '\n' for line in text.split('\n')]
    })

def add_code(code):
    nb['cells'].append({
        'cell_type': 'code',
        'execution_count': None,
        'metadata': {},
        'outputs': [],
        'source': [line + '\n' for line in code.split('\n')]
    })

# Section 1
add_md("# 1. Problem Definition\n\nExecutive investigation into collections performance, falsifying the 11% MoM claim, reconstructing the Golden dataset, and evaluating ₹10 Cr capital allocation options.")
add_code("import sys, os\nif not os.path.exists('payments.csv') and os.path.exists('../payments.csv'):\n    os.chdir('..')\n\nsys.path.insert(0, os.path.abspath('.'))\n\nimport pandas as pd\nimport numpy as np\nimport glob\nfrom src.profiling import generate_inventory\nfrom src.cleaning import clean_payments, map_disposition_codes\nfrom src.entity_resolution import resolve_agent_identities\nfrom src.metrics import compute_monthly_metrics\nfrom src.investment import evaluate_investments\n\ndef read_dataset_csv(filename):\n    for path in [os.path.join('dataset', filename), filename, os.path.join('..', 'dataset', filename), os.path.join('..', filename)]:\n        if os.path.exists(path):\n            return pd.read_csv(path)\n    raise FileNotFoundError(f'Could not find {filename}')\n\nprint('Working directory verified:', os.getcwd())\nprint('All analytics modules imported successfully.')")

# Section 2
add_md("# 2. Data Inventory\n\nProfile row counts, column counts, missingness, duplicates, and key candidate identification across all datasets.")
add_code("inv_df = generate_inventory('dataset' if os.path.exists('dataset') else '.')\ndisplay(inv_df)")

# Section 3
add_md("# 3. Data Quality & Profiling\n\nInspect data quality anomalies across tables.")
add_code("pay = read_dataset_csv('payments.csv')\nacc = read_dataset_csv('accounts.csv')\nprint('Payments total rows:', len(pay))\nprint('Duplicate payment_reference count:', pay.duplicated(subset=['payment_reference']).sum())")

# Section 4
add_md("# 4. Duplicate Detection & Forensic Cleaning\n\nIdentify exact and reference payment duplicates.")
add_code("cleaned_pay = clean_payments(pay, acc)\nprint('Valid payments count:', cleaned_pay['is_valid'].sum())\nprint('Exclusion breakdown:\\n', cleaned_pay['exclusion_reason'].value_counts())")

# Section 5
add_md("# 5. Agent Identity Resolution\n\nMap employee codes across snapshot records to canonical agent IDs.")
add_code("agents = read_dataset_csv('agents.csv')\nidentity_map = resolve_agent_identities(agents)\nprint('Unique employee codes:', identity_map['employee_code'].nunique())\ndisplay(identity_map.head())")

# Section 6
add_md("# 6. Timestamp & Timezone Analysis\n\nNormalize timestamps across UTC, Asia/Dubai, and Asia/Kolkata to Asia/Kolkata IST.")
add_code("print('Accounts Timezone Distribution:\\n', acc['timezone'].value_counts())\ndisplay(cleaned_pay[['payment_id', 'event_at', 'timezone', 'event_timestamp_ist', 'business_date']].head())")

# Section 7
add_md("# 7. Golden Dataset Construction\n\nBuild reproducible Golden data model layer with account dimension merge.")
add_code("gold_payments = cleaned_pay[cleaned_pay['is_valid'] == True].copy()\nif 'risk_segment' not in gold_payments.columns:\n    gold_payments = gold_payments.merge(acc[['account_id', 'risk_segment', 'dpd', 'loan_type']], on='account_id', how='left')\nprint('Golden Payments Total Amount:', gold_payments['amount'].sum())")

# Section 8
add_md("# 8. Metric Reconstruction\n\nCalculate contact rate, RPC rate, recovery rate, and cost per rupee recovered.")
add_code("calls = read_dataset_csv('calls.csv')\ntargeting = read_dataset_csv('daily_targeting.csv')\nsessions = read_dataset_csv('agent_sessions.csv')\nmetrics_df = compute_monthly_metrics(gold_payments, acc, calls, targeting, sessions)\ndisplay(metrics_df)")

# Section 9
add_md("# 9. 12-Month Performance & 11% Claim Falsification\n\nProve why the 11% claim is FALSE due to calendar length (28 vs 31 days).")
add_code("m_summary = gold_payments.groupby('business_month')['amount'].agg(['sum', 'count']).reset_index()\nm_summary['num_days'] = [31, 28, 31, 30, 31, 30, 31, 8]\nm_summary['daily_recovery'] = m_summary['sum'] / m_summary['num_days']\nm_summary['mom_monthly_pct'] = m_summary['sum'].pct_change() * 100\nm_summary['mom_daily_pct'] = m_summary['daily_recovery'].pct_change() * 100\ndisplay(m_summary)")

# Section 10
add_md("# 10. Portfolio Mix Analysis\n\nControl for DPD, Risk Segment, and Product Mix shifts.")
add_code("mix_df = gold_payments.groupby(['business_month', 'risk_segment'])['amount'].sum().unstack()\ndisplay(mix_df)")

# Section 11
add_md("# 11. Counterfactual Analysis (Difference-in-Differences)\n\nEstimate treatment effect of targeting strategy changes.")
add_code("from src.analysis import perform_counterfactual_did\ndid_res = perform_counterfactual_did(targeting, gold_payments)\nprint('Difference-in-Differences Estimate:', did_res)")

# Section 12
add_md("# 12. Investment Evaluation (₹10 Cr)\n\nEvaluate 6 options across Base, Downside, Upside scenarios, ROI, and Break-even.")
add_code("inv_res = evaluate_investments(10.0)\ndisplay(inv_res)")

os.makedirs('notebooks', exist_ok=True)
with open('notebooks/collections_analysis.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=2)

print("Rebuilt notebooks/collections_analysis.ipynb with dataset/ folder reader.")
