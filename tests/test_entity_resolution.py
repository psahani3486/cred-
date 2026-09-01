import pytest
import os
import pandas as pd
from src.entity_resolution import resolve_agent_identities

def get_csv_path(filename):
    if os.path.exists(os.path.join('dataset', filename)):
        return os.path.join('dataset', filename)
    return filename

def test_agent_identity_resolution():
    agents = pd.read_csv(get_csv_path('agents.csv'))
    identity_map = resolve_agent_identities(agents)
    
    assert not identity_map.empty
    assert 'canonical_agent_id' in identity_map.columns
    assert identity_map['employee_code'].nunique() == len(identity_map)

def test_agent_map_confidence():
    agents = pd.read_csv(get_csv_path('agents.csv'))
    identity_map = resolve_agent_identities(agents)
    assert (identity_map['confidence'] >= 0.90).all()
