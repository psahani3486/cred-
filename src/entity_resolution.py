import pandas as pd
import numpy as np

def resolve_agent_identities(agents_df):
    """
    Builds an agent_identity_map resolving employee_code to canonical_agent_id.
    Returns 1 row per unique employee_code.
    """
    ag = agents_df.copy()
    
    ag['updated_at_dt'] = pd.to_datetime(ag['updated_at'], errors='coerce')
    ag = ag.sort_values('updated_at_dt', ascending=False)
    
    # Keep latest record per employee_code
    canonical_map = ag.groupby('employee_code').first().reset_index()
    canonical_map = canonical_map.rename(columns={
        'agent_id': 'canonical_agent_id',
        'agent_id': 'original_agent_id'
    })
    canonical_map['canonical_agent_id'] = canonical_map['original_agent_id']
    canonical_map['confidence'] = 0.95
    canonical_map['resolution_reason'] = 'Deterministic employee_code & latest timestamp match'
    
    return canonical_map[['canonical_agent_id', 'original_agent_id', 'employee_code', 'agent_name', 'vendor_id', 'team', 'status', 'confidence', 'resolution_reason']]
