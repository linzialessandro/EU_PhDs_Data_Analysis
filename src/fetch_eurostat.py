#!/usr/bin/env python3
"""Download Eurostat ED8 × F054 snapshots: graduates, enrolments, mobile graduates.

Fails if a download is empty. Does not invent values.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import sys

import eurostat

sys.path.insert(0, str(Path(__file__).resolve().parent))
from eurostat_common import FIRST_ISCEDF13_YEAR, REPO_ROOT, to_long

ISCED_LEVEL = "ED8"
ISCED_FIELD = "F054"
UNIT = "NR"

JOBS = [
    {
        "dataset": "educ_uoe_grad02",
        "title": "Graduates by education level, programme orientation, sex and field of education",
        "out_dir": REPO_ROOT / "data" / "supply" / "eurostat-f054",
        "value_name": "graduates",
        "long_name": "graduates_long.csv",
        "total_name": "graduates_total.csv",
        "heading": "Eurostat F054 doctoral graduates",
        "what": (
            "A frozen snapshot of official Eurostat counts of doctoral graduates\n"
            "(ISCED 2011 level 8) in **Mathematics and statistics** (ISCED-F 2013 `F054`).\n\n"
            "This is a **supply** table: how many people were awarded the degree.\n"
            "It is not employment, salary, occupation, or job-prospect data."
        ),
        "note": "graduates is a count of degrees awarded, not employment.",
    },
    {
        "dataset": "educ_uoe_enrt03",
        "title": "Students enrolled in tertiary education by education level, programme orientation, sex and field of education",
        "out_dir": REPO_ROOT / "data" / "supply" / "eurostat-enrt03-f054",
        "value_name": "enrolments",
        "long_name": "enrolments_long.csv",
        "total_name": "enrolments_total.csv",
        "heading": "Eurostat F054 doctoral enrolments",
        "what": (
            "A frozen snapshot of official Eurostat counts of students **enrolled**\n"
            "in doctoral programmes (ISCED 2011 level 8) in **Mathematics and statistics**\n"
            "(ISCED-F 2013 `F054`).\n\n"
            "This is a **stock**: people in the programme that year, not degrees awarded.\n"
            "It is not employment data."
        ),
        "note": "enrolments is a headcount of students in the programme, not graduates.",
    },
    {
        "dataset": "educ_uoe_mobg01",
        "title": "Degree mobile graduates from abroad by education level, sex and field of education",
        "out_dir": REPO_ROOT / "data" / "supply" / "eurostat-mobg01-f054",
        "value_name": "mobile_graduates",
        "long_name": "mobile_graduates_long.csv",
        "total_name": "mobile_graduates_total.csv",
        "heading": "Eurostat F054 degree-mobile doctoral graduates",
        "what": (
            "A frozen snapshot of official Eurostat counts of **degree-mobile** doctoral\n"
            "graduates (ISCED 2011 level 8) in **Mathematics and statistics** (`F054`):\n"
            "people who obtained the degree in this country and had received their prior\n"
            "education in another country.\n\n"
            "This is not employment, and it is not all international residents — only\n"
            "degree mobility as Eurostat defines it."
        ),
        "note": "mobile_graduates counts degree-mobile awards, not jobs or all foreign citizens.",
    },
]


def fetch_raw(dataset: str):
    df = eurostat.get_data_df(
        dataset,
        filter_pars={
            "freq": "A",
            "unit": UNIT,
            "isced11": ISCED_LEVEL,
            "iscedf13": ISCED_FIELD,
        },
    )
    if df is None or df.empty:
        raise SystemExit(f"Eurostat returned no rows for {dataset} {ISCED_LEVEL} {ISCED_FIELD}.")
    return df


def write_sources(job: dict, retrieved_at: str, n_obs: int, year_min: int, year_max: int) -> None:
    dataset = job["dataset"]
    text = f"""# {job["heading"]}

## What this folder is

{job["what"]}

## Source

| Item | Value |
| --- | --- |
| Dataset | `{dataset}` |
| Title | {job["title"]} |
| Unit | `{UNIT}` (number) |
| Education level | `{ISCED_LEVEL}` (doctoral or equivalent) |
| Field | `{ISCED_FIELD}` Mathematics and statistics |
| Browser | https://ec.europa.eu/eurostat/databrowser/view/{dataset}/default/table?lang=en |
| Retrieved | {retrieved_at} |
| Years kept | {year_min}–{year_max} (ISCED-F 2013 series) |
| Non-missing country-year-sex cells | {n_obs} |

## What was excluded

- Years before {FIRST_ISCEDF13_YEAR}, when ISCED-F 2013 is not the classification in force.
- Geo codes that are neither a named country in the script nor an official Eurostat aggregate.
- No rows were imputed. Empty cells stay empty.

## How to refresh

From the repository root, with the project virtualenv:

```bash
python src/fetch_eurostat.py
```

Commit the files this script writes. Do not edit the CSVs by hand.
"""
    Path(job["out_dir"]).joinpath("SOURCES.md").write_text(text, encoding="utf-8")


def run_job(job: dict, retrieved_at: str) -> None:
    out_dir: Path = job["out_dir"]
    out_dir.mkdir(parents=True, exist_ok=True)
    value_name = job["value_name"]

    raw = fetch_raw(job["dataset"])
    raw_path = out_dir / f"raw_{job['dataset']}_ed8_f054.csv"
    raw.to_csv(raw_path, index=False)

    long = to_long(raw, value_name)
    if long.empty:
        raise SystemExit(f"Processed table for {job['dataset']} is empty. Refusing to write a blank snapshot.")

    long_path = out_dir / job["long_name"]
    long.to_csv(long_path, index=False)
    totals = long.loc[long["sex"] == "T", ["geo", "country", "year", value_name, "is_aggregate"]]
    totals.to_csv(out_dir / job["total_name"], index=False)

    observed = long.dropna(subset=[value_name])
    countries = sorted(long.loc[~long["is_aggregate"], "country"].unique())
    metadata = {
        "dataset": job["dataset"],
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
            job["note"],
            "Missing cells were not filled.",
            "EU27_2020 is Eurostat's official aggregate, not a sum computed here.",
        ],
    }
    (out_dir / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    write_sources(job, retrieved_at, int(len(observed)), int(long["year"].min()), int(long["year"].max()))

    rel = raw_path.relative_to(REPO_ROOT)
    print(f"Wrote {rel}  countries={len(countries)}  years={metadata['year_min']}-{metadata['year_max']}  observed={metadata['n_observed_cells']}")


def main() -> None:
    retrieved_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    for job in JOBS:
        run_job(job, retrieved_at)


if __name__ == "__main__":
    main()
