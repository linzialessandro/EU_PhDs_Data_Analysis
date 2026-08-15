# Mathematics PhDs in Europe

A public notebook of **official** data on mathematics and statistics doctorates.

I have a mathematics PhD and I teach in a high school. This repository is how I keep the numbers honest: Eurostat for how many `F054` doctorates are awarded, AlmaLaurea (when extracted) for what the closest Italian field does next. No synthetic rows, no blended EU job-market headline.

**Site:** [linzialessandro.github.io/EU_PhDs_Data_Analysis](https://linzialessandro.github.io/EU_PhDs_Data_Analysis/)

To view it on your machine:

```bash
source .venv/bin/activate
quarto preview
```

That opens the rendered pages (Home, Supply, Italy, Methods, Downloads) in the browser.

## What is in v1

| Page | Source | Status |
| --- | --- | --- |
| [Supply](supply.qmd) | Eurostat `ED8` × `F054`: degrees, enrolments, degree-mobile graduates | `data/supply/eurostat-*/` |
| [Italy](italy.qmd) | AlmaLaurea *scienze di base* (1–3 years); ISTAT *Scientifico* (4–6 years) | `data/outcomes/italy-*/` |
| [Methods](methods.qmd) | — | Definitions and exclusions |
| [Downloads](downloads.qmd) | The same files the site reads | |

## Refresh (about one evening a year)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/fetch_eurostat.py
quarto render
```

Commit the files under `data/`. Do not edit the Eurostat CSVs by hand. The site never calls an API when a page is opened.

If Quarto is missing:

```bash
brew install --cask quarto
```

## GitHub Pages

The site is built by `.github/workflows/pages.yml` from the committed snapshots. In the repo: **Settings → Pages → Source: GitHub Actions**.

## Non-goals

EU employment / salary / gender-gap headlines, machine-learning forecasts, policy scenarios, scraping AlmaLaurea, inventing a high-school teacher count from AlmaLaurea’s residual “other organisation or firm.”
