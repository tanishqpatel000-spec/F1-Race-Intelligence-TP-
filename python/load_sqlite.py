"""Load each CSV in data/raw into a local SQLite database using filename as table name."""
from pathlib import Path
import re, sqlite3
import pandas as pd
ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/raw"
DB = ROOT / "data/processed/f1_analysis.sqlite"
DB.parent.mkdir(parents=True, exist_ok=True)
files = sorted(RAW.glob("*.csv"))
if not files:
    raise SystemExit("No CSV files found in data/raw/. Export or copy source sheets as CSV first.")
with sqlite3.connect(DB) as conn:
    for path in files:
        table = re.sub(r"\W+", "_", path.stem).strip("_").lower()
        pd.read_csv(path).to_sql(table, conn, if_exists="replace", index=False)
        print(f"Loaded {path.name} -> {table}")
print(f"SQLite database: {DB}")
