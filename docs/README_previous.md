# Formula 1 Race Intelligence Dashboard

An interactive Tableau project for exploring Formula 1 racing data, driver and team performance, circuit information, qualifying results, lap intelligence, and race strategies.

## Project Overview

The **Formula 1 Race Intelligence Dashboard** brings multiple Formula 1 datasets together to make race information easier to explore. The Tableau workbook contains worksheets and dashboards designed to help users compare performance and investigate racing patterns.

## Project Objectives

- Explore driver and constructor performance.
- Compare championship points and race results.
- Examine qualifying positions and lap-time patterns.
- Explore circuits, countries, and track distances.
- Investigate reliability, tyre strategy, weather, safety-car activity, and overtakes where the dataset provides the relevant fields.
- Present the analysis through interactive Tableau dashboards.

## Tools and Technologies

- **Tableau** – data visualization and dashboard development.
- **Microsoft Excel** – dataset storage and preparation.
- **GitHub** – project versioning and sharing.

## Dataset

The Tableau data source uses the following tables/sheets:

- `race_results`
- `championship_standings`
- `circuits`
- `lap_intelligence`
- `qualifying_results`

The tables are connected in Tableau using the relevant race, circuit, season, and driver fields. Please refer to the workbook for the exact relationship configuration.

## Analysis and Visualizations

The workbook includes analysis areas such as:

1. Driver championship points
2. Team championship points
3. Circuits by country
4. Race results by driver
5. Average lap time by driver
6. Average qualifying position by driver
7. Driver reliability and DNF analysis
8. Tyre compound and strategy analysis
9. Weather analysis
10. Circuit distance analysis
11. Race duration analysis
12. Safety-car analysis
13. DRS overtakes analysis
14. Fastest-lap analysis
15. Positions-gained analysis

> Note: The exact measures and conclusions depend on the fields available in the supplied dataset. Average lap time should not be interpreted as pit-stop time unless a verified pit-stop-time field is used. Weather charts show patterns or associations and do not, by themselves, prove causation.

## Repository Contents

| File | Description |
|---|---|
| `Book1.twb` | Tableau workbook |
| `F1 racing dashboard tp.twb` | Tableau project workbook |
| `F1_Race_Intelligence_Project_Report.pdf` | Project documentation report |

## How to View the Project

1. Download one of the `.twb` workbook files from this repository.
2. Open it using Tableau Desktop or a compatible Tableau application.
3. If Tableau asks for the original data source, reconnect the workbook to the Excel dataset used to build the project.
4. Open the dashboards and interact with the available charts and filters.

**Important:** A `.twb` file stores workbook definitions and may refer to an external data file. If the Excel dataset is not included in this repository, the workbook may ask you to reconnect that data source.

## Documentation

The project report is available here:

`F1_Race_Intelligence_Project_Report.pdf`

It describes the project objectives, data tables, preparation, visualizations, testing considerations, and future scope. Any placeholders in the report should be completed with verified project details before final submission.

## Future Improvements

- Add and validate interactive dashboard filters.
- Improve dashboard layout, titles, labels, and tooltips.
- Include the source dataset or package the workbook with its data, subject to dataset licensing.
- Add verified findings and screenshots to the documentation.
- Publish a short project walkthrough video.

## Author

**Tanishq Patel**

## Disclaimer

This project is intended for educational and analytical purposes. Findings should be interpreted according to the coverage, quality, and limitations of the underlying dataset.
