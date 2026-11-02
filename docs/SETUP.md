# Setup and run guide

## 1. Add the source data

The F1 source Excel/CSV files were not present in the supplied files used to assemble this package. Copy your original dataset into `data/raw/`. For the Python and SQLite scripts, CSV files are supported directly. If your source is an Excel workbook, `profile_data.py` can profile `.xlsx` files; export individual sheets as CSV if you want to load them into SQLite.

## 2. Install Python dependencies

```bash
python -m venv .venv
# Windows PowerShell:
.venv\\Scripts\\Activate.ps1
# macOS/Linux:
source .venv/bin/activate
pip install -r requirements.txt
```

## 3. Profile data

```bash
python python/profile_data.py
```

The script writes `data/processed/data_profile.json`. Review column names, missing values, duplicates, and numeric summaries before building analysis queries.

## 4. Optional cleaning and SQLite

```bash
python python/clean_csv.py
python python/load_sqlite.py
```

Cleaning only trims column names and removes exact duplicate rows. Keep the original raw files unchanged. SQLite tables use sanitized source filenames as table names. Inspect table and column names before adapting `sql/load_and_queries.sql`.

## 5. Run the Flask CSV preview app

```bash
python web/app.py
```

Open `http://127.0.0.1:5000`, upload a CSV, and inspect the preview and quality summary. This is a local demo, not a production deployment. Do not upload sensitive data.

## 6. Open Tableau workbook

Open `tableau/F1_Race_Intelligence.twb` in Tableau Desktop. If Tableau reports a missing data source, reconnect it to the original Excel/CSV dataset. Save a copy after verifying all worksheets and dashboard filters.

## 7. Final validation before submission

- Verify the source data and its license/source citation.
- Confirm every worksheet uses the intended field and aggregation.
- Use `COUNTD(Race ID)` when counting distinct races; `COUNT(Race ID)` counts rows.
- Check filters, null handling, labels, tooltips, and dashboard layout.
- Reconcile key totals against source data.
- Record actual test outcomes and add screenshots to the report.
- Package as `.twbx` from Tableau if you need to include extract/data, subject to dataset licensing.
