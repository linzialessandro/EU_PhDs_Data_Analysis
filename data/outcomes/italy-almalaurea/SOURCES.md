# Italy outcomes — AlmaLaurea

**Status: extract present.** Retrieved 2026-08-15 from the official databank.

## What this folder is

Hand-copied cells from AlmaLaurea’s PhD employment survey for the official
disciplinary area **scienze di base** (basic sciences). That is the closest
published field. It is **not** mathematics-only: it also includes physics,
chemistry, computer science, earth sciences, and related programmes.

There is no AlmaLaurea row named mathematics, mathematics and statistics, or
high-school teacher.

## Source

| Item | Value |
| --- | --- |
| Survey | Esiti occupazionali del dottorato di ricerca (11th survey, 2026 report) |
| Survey year | 2025 |
| 1-year cohort | PhDs awarded in 2024, interviewed about 1 year later |
| 3-year cohort | PhDs awarded in 2022, interviewed about 3 years later (fewer universities) |
| Official field (Italian) | `scienze di base` |
| English wording on this site | Basic sciences |
| Universities (1-year query) | any of the 51 that have this area |
| PhD programme filter | any |
| Publisher | Consorzio Interuniversitario AlmaLaurea |
| Last update printed on the sheet | 30 June 2026 |
| Reproduction | Non-commercial reuse allowed with citation |

### Exact databank views

- 1 year: https://www2.almalaurea.it/cgi-asp/universita/statistiche/Pages/visualizza2.aspx?lang=it&dropClasseIndagine=9&dropIndagine=86&anni_da_titolo=1&univ=0&macroarea=1&codicione=&kciclo_dott=0&groupRadioButtonDisaggregazione=nessuna&hidBaseGeo=
- 3 years: https://www2.almalaurea.it/cgi-asp/universita/statistiche/Pages/visualizza2.aspx?lang=it&dropClasseIndagine=9&dropIndagine=86&anni_da_titolo=3&univ=0&macroarea=1&codicione=&kciclo_dott=0&groupRadioButtonDisaggregazione=nessuna&hidBaseGeo=
- Query form: https://www2.almalaurea.it/cgi-asp/universita/indagini/occupazioneDR.aspx?anno=2025&LANG=en
- Methodological notes: https://www2.almalaurea.it/cgi-asp/universita/statistiche/Pages/notemetodologiche/notemetodologiche_occupazioneDR2025.pdf
- Survey page: https://www.almalaurea.it/en/our-data/almalaurea-surveys/phds-employment-status

`macroarea=1` is AlmaLaurea’s code for **scienze di base**.

## Population (as printed)

| Wave | PhD holders | Interviewed | Response rate (all) | Response rate (contactable) |
| --- | ---: | ---: | ---: | ---: |
| 1 year | 1,852 | 1,268 | 68.5% | 83.3% |
| 3 years | 578 | 372 | 64.4% | 83.6% |

The 3-year table is a smaller collective. Do not treat 1-year and 3-year as
the same people followed over time.

## Definitions that matter

- **Employed** includes paid training (research grants, scholarships). Note 7.
- **Education and research** includes schools, universities, and research
  bodies, public and private. Note 26.
- **Other organisation or firm** inside that branch is a residual. It is not
  a high-school teacher count. Note 28.
- Pay is mean net monthly pay from 250-euro bands (note 29).
- Cells shown as a dash were left empty in `outcomes.csv`.

## What was not done

- No recode of *altro ente o impresa* as teaching.
- No mix of the all-PhD national total with this field.
- No interpolation of missing cells.
- No invented or remembered numbers.
