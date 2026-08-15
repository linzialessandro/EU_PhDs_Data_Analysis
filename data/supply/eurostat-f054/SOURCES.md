# Eurostat F054 doctoral graduates

## What this folder is

A frozen snapshot of official Eurostat counts of doctoral graduates
(ISCED 2011 level 8) in **Mathematics and statistics** (ISCED-F 2013 `F054`).

This is a **supply** table: how many people were awarded the degree.
It is not employment, salary, occupation, or job-prospect data.

## Source

| Item | Value |
| --- | --- |
| Dataset | `educ_uoe_grad02` |
| Title | Graduates by education level, programme orientation, sex and field of education |
| Unit | `NR` (number) |
| Education level | `ED8` (doctoral or equivalent) |
| Field | `F054` Mathematics and statistics |
| Browser | https://ec.europa.eu/eurostat/databrowser/view/educ_uoe_grad02/default/table?lang=en |
| Retrieved | 2026-08-15T08:54:10Z |
| Years kept | 2013–2024 (ISCED-F 2013 series) |
| Non-missing country-year-sex cells | 1248 |

## What was excluded

- Years before 2013, when ISCED-F 2013 is not the classification in force.
- Geo codes that are neither a named country in the script nor an official Eurostat aggregate.
- No rows were imputed. Empty cells stay empty.

## How to refresh

From the repository root, with the project virtualenv:

```bash
python src/fetch_eurostat.py
```

Commit the files this script writes. Do not edit the CSVs by hand.
