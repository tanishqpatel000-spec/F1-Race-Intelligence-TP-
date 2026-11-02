"""Discover and profile CSV/XLSX files in data/raw without assuming a schema."""
from pathlib import Path
import json
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "processed"


def load_file(path: Path) -> pd.DataFrame:
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path)
    if path.suffix.lower() in {".xlsx", ".xls"}:
        return pd.read_excel(path)
    raise ValueError(f"Unsupported file type: {path.suffix}")


def profile(df: pd.DataFrame) -> dict:
    numeric = df.select_dtypes(include="number")
    return {
        "rows": int(len(df)),
        "columns": int(len(df.columns)),
        "column_names": [str(c) for c in df.columns],
        "missing_by_column": {str(k): int(v) for k, v in df.isna().sum().items()},
        "duplicate_rows": int(df.duplicated().sum()),
        "numeric_summary": json.loads(numeric.describe().to_json()),
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    files = sorted([*RAW.glob("*.csv"), *RAW.glob("*.xlsx"), *RAW.glob("*.xls")])
    if not files:
        raise SystemExit("No CSV/XLSX files found. Add the original F1 dataset to data/raw/ first.")
    report = {}
    for path in files:
        df = load_file(path)
        report[path.name] = profile(df)
        print(f"{path.name}: {len(df):,} rows x {len(df.columns)} columns")
    output = OUT / "data_profile.json"
    output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(f"Saved profile: {output}")

if __name__ == "__main__":
    main()
