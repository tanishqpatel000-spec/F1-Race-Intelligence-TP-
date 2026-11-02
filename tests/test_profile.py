import importlib.util
from pathlib import Path
import pandas as pd

MODULE = Path(__file__).resolve().parents[1] / 'python' / 'profile_data.py'
spec = importlib.util.spec_from_file_location('profile_data', MODULE)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

def test_profile_counts_and_missing_values():
    df = pd.DataFrame({'driver': ['A', 'B', 'B'], 'points': [10, None, 10]})
    result = mod.profile(df)
    assert result['rows'] == 3
    assert result['columns'] == 2
    assert result['missing_by_column']['points'] == 1
    assert result['duplicate_rows'] == 0
