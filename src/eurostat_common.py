"""Shared Eurostat helpers. No imputation. Empty cells stay empty."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

FIRST_ISCEDF13_YEAR = 2013

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

REPO_ROOT = Path(__file__).resolve().parents[1]


def geo_column(df: pd.DataFrame) -> str:
    for col in df.columns:
        if str(col).startswith("geo"):
            return col
    raise SystemExit("Eurostat table has no geo column.")


def to_long(raw: pd.DataFrame, value_name: str) -> pd.DataFrame:
    geo_col = geo_column(raw)
    year_cols = [c for c in raw.columns if str(c).isdigit()]
    if not year_cols:
        raise SystemExit("Eurostat table has no year columns.")

    long = raw.melt(
        id_vars=[geo_col, "sex"],
        value_vars=year_cols,
        var_name="year",
        value_name=value_name,
    )
    long = long.rename(columns={geo_col: "geo"})
    long["year"] = pd.to_numeric(long["year"], errors="coerce")
    long[value_name] = pd.to_numeric(long[value_name], errors="coerce")
    long = long.dropna(subset=["year"])
    long["year"] = long["year"].astype(int)
    long = long.loc[long["year"] >= FIRST_ISCEDF13_YEAR].copy()
    long["sex"] = long["sex"].astype(str)
    long["geo"] = long["geo"].astype(str)
    long["country"] = long["geo"].map(COUNTRY_NAMES)
    long["sex_label"] = long["sex"].map(SEX_LABELS)
    long["is_aggregate"] = long["geo"].isin(AGGREGATE_GEOS)
    long = long.loc[long["is_aggregate"] | long["country"].notna()].copy()
    long["country"] = long["country"].fillna(long["geo"])
    return long.sort_values(["is_aggregate", "country", "year", "sex"]).reset_index(drop=True)
