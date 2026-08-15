#!/usr/bin/env python3
"""Download Eurostat doctoral graduates in Mathematics and statistics (F054).

Writes committed snapshots under data/supply/eurostat-f054/.
Fails if the download is empty. Does not invent values.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import eurostat
import pandas as pd

DATASET = "educ_uoe_grad02"
ISCED_LEVEL = "ED8"
ISCED_FIELD = "F054"
UNIT = "NR"
FIRST_ISCEDF13_YEAR = 2013

REPO_ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = REPO_ROOT / "data" / "supply" / "eurostat-f054"

AGGREGATE_GEOS = {
    "EU27_2020",
    "EU28",
    "EU27_2007",
    "EA",
    "EA19",
    "EA20",
    "EA21",
}

COUNTRY_NAMES = {
    "AL": "Albania",
    "AT": "Austria",
    "BA": "Bosnia and Herzegovina",
    "BE": "Belgium",
    "BG": "Bulgaria",
    "CH": "Switzerland",
    "CY": "Cyprus",
    "CZ": "Czechia",
    "DE": "Germany",
    "DK": "Denmark",
    "EE": "Estonia",
    "EL": "Greece",
    "ES": "Spain",
    "FI": "Finland",
    "FR": "France",
    "GE": "Georgia",
    "HR": "Croatia",
    "HU": "Hungary",
    "IE": "Ireland",
    "IS": "Iceland",
    "IT": "Italy",
    "LI": "Liechtenstein",
    "LT": "Lithuania",
    "LU": "Luxembourg",
    "LV": "Latvia",
    "ME": "Montenegro",
    "MK": "North Macedonia",
    "MT": "Malta",
    "NL": "Netherlands",
    "NO": "Norway",
    "PL": "Poland",
    "PT": "Portugal",
    "RO": "Romania",
    "RS": "Serbia",
    "SE": "Sweden",
    "SI": "Slovenia",
    "SK": "Slovakia",
    "TR": "Türkiye",
    "UK": "United Kingdom",
}

SEX_LABELS = {"T": "Total", "F": "Women", "M": "Men"}


def _geo_column(df: pd.DataFrame) -> str:
    for col in df.columns:
        if str(col).startswith("geo"):
            return col
    raise SystemExit("Eurostat table has no geo column.")


def fetch_raw() -> pd.DataFrame:
    df = eurostat.get_data_df(
        DATASET,
        filter_pars={
            "freq": "A",
            "unit": UNIT,
            "isced11": ISCED_LEVEL,
            "iscedf13": ISCED_FIELD,
        },
    )
    if df is None or df.empty:
        raise SystemExit(f"Eurostat returned no rows for {DATASET} {ISCED_LEVEL} {ISCED_FIELD}.")
    return df


def to_long(raw: pd.DataFrame) -> pd.DataFrame:
    geo_col = _geo_column(raw)
    year_cols = [c for c in raw.columns if str(c).isdigit()]
    if not year_cols:
        raise SystemExit("Eurostat table has no year columns.")

    long = raw.melt(
        id_vars=[geo_col, "sex"],
        value_vars=year_cols,
        var_name="year",
        value_name="graduates",
    )
    long = long.rename(columns={geo_col: "geo"})
    long["year"] = pd.to_numeric(long["year"], errors="coerce")
    long["graduates"] = pd.to_numeric(long["graduates"], errors="coerce")
    long = long.dropna(subset=["year"])
    long["year"] = long["year"].astype(int)
    long = long.loc[long["year"] >= FIRST_ISCEDF13_YEAR].copy()
    long["sex"] = long["sex"].astype(str)
    long["geo"] = long["geo"].astype(str)
    long["country"] = long["geo"].map(COUNTRY_NAMES)
    long["sex_label"] = long["sex"].map(SEX_LABELS)
    long["is_aggregate"] = long["geo"].isin(AGGREGATE_GEOS)
    # Keep official aggregates and named countries. Drop unknown codes.
    long = long.loc[long["is_aggregate"] | long["country"].notna()].copy()
    long["country"] = long["country"].fillna(long["geo"])
    return long.sort_values(["is_aggregate", "country", "year", "sex"]).reset_index(drop=True)


def write_sources(retrieved_at: str, n_country_years: int, year_min: int, year_max: int) -> None:
    text = f"""# Eurostat F054 doctoral graduates

## What this folder is

A frozen snapshot of official Eurostat counts of doctoral graduates
(ISCED 2011 level 8) in **Mathematics and statistics** (ISCED-F 2013 `F054`).

This is a **supply** table: how many people were awarded the degree.
It is not employment, salary, occupation, or job-prospect data.

## Source

| Item | Value |
| --- | --- |
| Dataset | `{DATASET}` |
| Title | Graduates by education level, programme orientation, sex and field of education |
| Unit | `{UNIT}` (number of graduates) |
| Education level | `{ISCED_LEVEL}` (doctoral or equivalent) |
| Field | `{ISCED_FIELD}` Mathematics and statistics |
| Browser | https://ec.europa.eu/eurostat/databrowser/view/educ_uoe_grad02/default/table?lang=en |
| Retrieved | {retrieved_at} |
| Years kept | {year_min}–{year_max} (ISCED-F 2013 series) |
| Non-missing country-year-sex cells | {n_country_years} |

## Why not `educ_uoe_grad03`

The previous notebook called `educ_uoe_grad03`. That table is a **percentage
distribution** (`unit = PC`), not headcounts. Counts come from `{DATASET}`.

## What was excluded

- Years before {FIRST_ISCEDF13_YEAR}, when ISCED-F 2013 is not the classification in force.
- Geo codes that are neither a named country in the script nor an official Eurostat aggregate.
- No rows were imputed. Empty cells stay empty.

## How to refresh

From the repository root, with the project virtualenv:

```bash
python src/fetch_eurostat_f054.py
```

Commit the files this script writes. Do not edit the CSVs by hand.
"""
    (OUT_DIR / "SOURCES.md").write_text(text, encoding="utf-8")


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    retrieved_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    raw = fetch_raw()
    raw_path = OUT_DIR / "raw_educ_uoe_grad02_ed8_f054.csv"
    raw.to_csv(raw_path, index=False)

    long = to_long(raw)
    if long.empty:
        raise SystemExit("Processed table is empty after filters. Refusing to write a blank snapshot.")

    long_path = OUT_DIR / "graduates_long.csv"
    long.to_csv(long_path, index=False)

    totals = long.loc[long["sex"] == "T", ["geo", "country", "year", "graduates", "is_aggregate"]]
    totals.to_csv(OUT_DIR / "graduates_total.csv", index=False)

    observed = long.dropna(subset=["graduates"])
    countries = sorted(long.loc[~long["is_aggregate"], "country"].unique())
    metadata = {
        "dataset": DATASET,
        "isced11": ISCED_LEVEL,
        "iscedf13": ISCED_FIELD,
        "unit": UNIT,
        "retrieved_at_utc": retrieved_at,
        "year_min": int(long["year"].min()),
        "year_max": int(long["year"].max()),
        "n_rows": int(len(long)),
        "n_observed_cells": int(len(observed)),
        "countries": countries,
        "notes": [
            "graduates is a count of degrees awarded, not employment.",
            "Missing cells were not filled.",
            "EU27_2020 is Eurostat's official aggregate, not a sum computed here.",
        ],
    }
    (OUT_DIR / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    write_sources(
        retrieved_at=retrieved_at,
        n_country_years=int(len(observed)),
        year_min=int(long["year"].min()),
        year_max=int(long["year"].max()),
    )

    print(f"Wrote {raw_path.relative_to(REPO_ROOT)}")
    print(f"Wrote {long_path.relative_to(REPO_ROOT)}")
    print(f"Countries: {len(countries)}")
    print(f"Years: {metadata['year_min']}-{metadata['year_max']}")
    print(f"Observed cells: {metadata['n_observed_cells']}")


if __name__ == "__main__":
    main()
