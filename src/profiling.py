import os
import glob
import pandas as pd
import numpy as np

def generate_inventory(data_dir='.'):
    csv_files = glob.glob(os.path.join(data_dir, '*.csv'))
    inventory = []
    
    for f in sorted(csv_files):
        fname = os.path.basename(f)
        if fname in ['data_inventory.csv', 'data_dictionary.csv']:
            continue
        tname = fname.replace('.csv', '')
        df = pd.read_csv(f, low_memory=False)
        rows, cols = df.shape
        
        date_cols = [c for c in df.columns if 'at' in c or 'date' in c or 'time' in c]
        min_d, max_d = None, None
        for dc in date_cols:
            parsed = pd.to_datetime(df[dc], errors='coerce')
            if parsed.notnull().any():
                min_d = str(parsed.min())[:10]
                max_d = str(parsed.max())[:10]
                break
        
        dup_rate = df.duplicated().mean() * 100
        null_rate = df.isnull().mean().mean() * 100
        pk = [c for c in df.columns if c.endswith('_id') and df[c].nunique() == rows]
        pk_str = ', '.join(pk) if pk else 'None'
        
        fk_list = [c for c in df.columns if c.endswith('_id') and c not in pk]
        fk_str = ', '.join(fk_list) if fk_list else 'None'
        
        inventory.append({
            'table': tname,
            'rows': rows,
            'columns': cols,
            'date_min': min_d or 'N/A',
            'date_max': max_d or 'N/A',
            'duplicate_rate': f"{dup_rate:.2f}%",
            'null_rate': f"{null_rate:.2f}%",
            'suspected_pk': pk_str,
            'suspected_fk': fk_str,
            'issues': 'Duplicates / Unresolved FKs' if dup_rate > 0 or null_rate > 1 else 'None'
        })
        
    inv_df = pd.DataFrame(inventory)
    inv_df.to_csv('data_inventory.csv', index=False)
    print("Generated data_inventory.csv successfully.")
    return inv_df

if __name__ == '__main__':
    generate_inventory()
