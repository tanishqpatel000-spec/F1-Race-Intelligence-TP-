"""Optional conservative CSV cleaner: trims column names and removes exact duplicate rows."""
from pathlib import Path
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
RAW, OUT = ROOT / "data/raw", ROOT / "data/processed"
OUT.mkdir(parents=True, exist_ok=True)
files = sorted(RAW.glob("*.csv"))
if not files:
    raise SystemExit("No CSV files found in data/raw/.")
for path in files:
    df = pd.read_csv(path)
    df.columns = [str(c).strip() for c in df.columns]
    before = len(df)
    df = df.drop_duplicates()
    target = OUT / f"{path.stem}_cleaned.csv"
    df.to_csv(target, index=False)
    print(f"{path.name}: removed {before-len(df)} exact duplicate rows -> {target.name}")
