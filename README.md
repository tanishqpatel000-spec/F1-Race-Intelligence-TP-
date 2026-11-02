# Formula 1 Race Intelligence — End-to-End Analytics Project

An educational analytics project built around the supplied Tableau workbook. The repository is organized for reproducible data profiling, SQL exploration, dashboard delivery, and a small optional Flask data-preview app.

> **Data note:** The source Excel/CSV dataset was not included with the files available when this package was assembled. The original Tableau `.twb` workbook is included unchanged, but it may ask you to reconnect its original data source. Put your licensed/source dataset in `data/raw/` and follow `docs/SETUP.md` before running the analysis or app. No results or tests are represented as completed unless you run them locally.

## Repository structure

```text
f1_project/
├── tableau/                 # Original Tableau workbook (.twb)
├── data/raw/                # Add source CSV/XLSX files here (not included)
├── data/processed/          # Generated profiling outputs
├── python/                  # Dataset discovery and profiling
├── sql/                     # SQLite loading and example queries
├── web/                     # Flask CSV preview/profiling app
├── tests/                   # Basic automated tests
└── docs/                    # Setup, methodology, report
```

## What is included

- Original Tableau workbook copied without editing.
- Python script to discover CSV files, profile columns, missing values, and numeric summaries.
- SQLite loader and reusable SQL examples after data is supplied.
- Flask app to upload a CSV and inspect a preview and basic profile.
- Setup and validation instructions.

## Quick start

1. Add the source dataset files to `data/raw/`.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run profiling: `python python/profile_data.py`.
4. Load CSV files into SQLite: `python python/load_sqlite.py`.
5. Start the optional web app: `python web/app.py` and open `http://127.0.0.1:5000`.
6. Open `tableau/F1_Race_Intelligence.twb` in Tableau Desktop and reconnect the original data source if prompted.

See [`docs/SETUP.md`](docs/SETUP.md) for details.

## Tableau analysis topics

The supplied workbook was previously developed to explore driver/team points, race results, circuits, qualifying, lap times, reliability, tyre strategy, weather, race duration, safety-car activity, overtakes, fastest laps, and positions gained. Confirm each worksheet's field definitions and aggregations against the actual dataset before presenting findings.

## Data integrity and interpretation

- `COUNT(Race ID)` counts rows/entries; use `COUNTD(Race ID)` for distinct races.
- Average lap time is not pit-stop time unless a verified pit-stop field is used.
- Weather charts show associations, not proof of causation.
- Do not publish numerical findings until they are checked against the source data.

## Project status

This is a structured project package, not a claim that the missing source dataset, Flask deployment, SQL execution, or final testing have already been completed. Add your actual dataset, run the checks, capture dashboard screenshots, and update the report with verified findings.

## Author

name Tanishq patel, enrollment number en25ca3020184, course bca , and institution medicaps.ac.in

## Companion HTML Website

A responsive static website is included in `web/`.

- Open `web/index.html` in a modern browser to view the project website.
- The page includes project overview sections, responsive styling, sample visualizations, and a CSV preview loader.
- The demo chart values are illustrative placeholders, not verified Formula 1 results.
- To preview your own data, upload a CSV with `Driver` and `Points` columns; `Team` is optional.
- The companion website is separate from the Tableau workbook and does not automatically synchronize Tableau data.
