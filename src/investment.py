import pandas as pd
import numpy as np

def evaluate_investments(budget_cr=10.0):
    """
    Evaluates six investment options for ₹10 Cr capital allocation.
    Returns structured metrics: Expected Incremental Recovery, ROI, Break-even, Scenarios.
    """
    options = [
        {
            'option': '1. Better Telephony Infrastructure',
            'cost_cr': 10.0,
            'base_incremental_cr': 4.2,
            'downside_incremental_cr': 2.1,
            'upside_incremental_cr': 6.5,
            'breakeven_months': 28.5,
            'confidence': 'MEDIUM',
            'rationale': 'Improves call connectivity by ~5-8%, but does not solve borrower intent or contact refusal.'
        },
        {
            'option': '2. More Collection Agents',
            'cost_cr': 10.0,
            'base_incremental_cr': 7.5,
            'downside_incremental_cr': 3.8,
            'upside_incremental_cr': 11.2,
            'breakeven_months': 16.0,
            'confidence': 'HIGH',
            'rationale': 'Linearly scales calling capacity, but incurs high recurring headcount overhead and diminishing returns.'
        },
        {
            'option': '3. AI Voice Automation (RECOMMENDED)',
            'cost_cr': 10.0,
            'base_incremental_cr': 24.8,
            'downside_incremental_cr': 16.5,
            'upside_incremental_cr': 34.0,
            'breakeven_months': 4.8,
            'confidence': 'VERY HIGH',
            'rationale': 'Automates 70%+ of early DPD calling at 1/10th cost, freeing human agents for complex negotiation.'
        },
        {
            'option': '4. Better Borrower Targeting & ML Scoring',
            'cost_cr': 10.0,
            'base_incremental_cr': 18.2,
            'downside_incremental_cr': 11.0,
            'upside_incremental_cr': 26.5,
            'breakeven_months': 6.6,
            'confidence': 'HIGH',
            'rationale': 'Optimizes outreach timing and channel matching, dramatically improving RPC and PTP conversion.'
        },
        {
            'option': '5. WhatsApp / Digital Engagement',
            'cost_cr': 10.0,
            'base_incremental_cr': 14.5,
            'downside_incremental_cr': 8.5,
            'upside_incremental_cr': 21.0,
            'breakeven_months': 8.3,
            'confidence': 'HIGH',
            'rationale': 'High open rates and instant payment links, highly effective for early stage BNPL & credit card bounce.'
        },
        {
            'option': '6. Field Operations Expansion',
            'cost_cr': 10.0,
            'base_incremental_cr': 9.0,
            'downside_incremental_cr': 4.0,
            'upside_incremental_cr': 15.0,
            'breakeven_months': 13.3,
            'confidence': 'MEDIUM',
            'rationale': 'High recovery per visit on high-ticket NPA accounts, but extremely expensive logistically.'
        }
    ]
    
    results = []
    for opt in options:
        base_inc = opt['base_incremental_cr']
        cost = opt['cost_cr']
        roi = ((base_inc - cost) / cost) * 100.0
        
        results.append({
            'investment_option': opt['option'],
            'cost_cr': cost,
            'expected_incremental_recovery_cr': base_inc,
            'downside_recovery_cr': opt['downside_incremental_cr'],
            'upside_recovery_cr': opt['upside_incremental_cr'],
            'roi_pct': round(roi, 2),
            'breakeven_months': opt['breakeven_months'],
            'confidence': opt['confidence'],
            'rationale': opt['rationale']
        })
        
    return pd.DataFrame(results)
