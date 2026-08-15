# Mathematics PhDs in Europe

A public notebook of **official** data on mathematics and statistics doctorates.

I have a mathematics PhD and I teach in a high school. This repository is how I keep the numbers honest: Eurostat for how many `F054` doctorates are awarded, AlmaLaurea (when extracted) for what the closest Italian field does next. No synthetic rows, no blended EU job-market headline.

**Live site:** after GitHub Pages is enabled, `https://linzialessandro.github.io/EU_PhDs_Data_Analysis/`

## What is in v1

| Page | Source | Status |
| --- | --- | --- |
| [Supply](supply.qmd) | Eurostat `educ_uoe_grad02`, ISCED `ED8`, field `F054` | Snapshot in `data/supply/eurostat-f054/` |
| [Italy](italy.qmd) | AlmaLaurea PhD employment survey, official area **scienze di base** | [outcomes.csv](data/outcomes/italy-almalaurea/outcomes.csv) |
| [Methods](methods.qmd) | — | Definitions and exclusions |
| [Downloads](downloads.qmd) | The same files the site reads | |

## Refresh (about one evening a year)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/fetch_eurostat_f054.py
# optional: fill data/outcomes/italy-almalaurea/ from EXTRACT.md
quarto render
```

Commit the files under `data/`. Do not edit the Eurostat CSVs by hand. The site never calls an API when a page is opened.

If Quarto is missing:

```bash
brew install --cask quarto
```

## GitHub Pages

On the first publish, in the GitHub repo: **Settings → Pages → Build and deployment → Source: Deploy from a branch → `gh-pages` / root**. The workflow `.github/workflows/pages.yml` renders from the committed snapshots only.

## Non-goals

EU employment / salary / gender-gap headlines, machine-learning forecasts, policy scenarios, scraping AlmaLaurea, inventing a high-school teacher count from AlmaLaurea’s residual “other organisation or firm.”
