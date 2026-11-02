-- Run after loading your CSV tables into SQLite using python/load_sqlite.py.
-- Table names are derived from source filenames. Inspect them first with: SELECT name FROM sqlite_master WHERE type='table';

-- 1) Inspect available tables
SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;

-- 2) Row count template (replace table_name with an actual imported table)
-- SELECT COUNT(*) AS row_count FROM table_name;

-- 3) Missing-value checks are best handled from the Python profile output.
-- 4) Driver/constructor/circuit analysis queries depend on the exact source column names.
--    Inspect columns with: PRAGMA table_info('table_name');
-- 5) Example once a table and fields are confirmed:
-- SELECT driver_name, SUM(points) AS total_points
-- FROM race_results
-- GROUP BY driver_name
-- ORDER BY total_points DESC;
