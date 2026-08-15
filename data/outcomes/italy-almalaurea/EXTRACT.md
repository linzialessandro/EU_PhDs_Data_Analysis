# AlmaLaurea extract checklist

Do this once, from the official databank. Do not scrape. Do not fill gaps.

## 1. Open the official table

- English: [PhDs’ Employment Status](https://www.almalaurea.it/en/our-data/almalaurea-surveys/phds-employment-status)
- Databank (latest cycle): [occupazioneDR.aspx](https://www2.almalaurea.it/cgi-asp/universita/indagini/occupazioneDR.aspx?anno=2025&LANG=en)

Use the **latest published 1-year** survey. Add the 3-year table only if the **same official field** is available.

## 2. Select the field

Under **area disciplinare**, choose the official grouping closest to mathematics.

It is often **matematica e informatica** (mathematics and computer science), not pure mathematics. Write the **Italian label exactly as AlmaLaurea prints it** in `SOURCES.md`. On the site we translate it; we do not rename it “mathematics PhDs.”

If the closest field is broader than F054, that is fine. The Italy page will say so.

If the field is suppressed for small *n*, leave this folder empty and say so on the Italy page.

## 3. Copy these cells if they exist

Create `outcomes.csv` with one row per indicator:

| column | meaning |
| --- | --- |
| `indicator` | short English id, e.g. `employment_rate` |
| `official_label_en` | AlmaLaurea wording in English (or your translation of the Italian wording) |
| `official_label_it` | Italian wording from the table, if shown |
| `value` | the number as published |
| `unit` | `percent`, `euro`, `count`, `months`, `score` |
| `n` | respondents for that cell, if printed |
| `notes` | suppression, definition, anything printed next to the cell |

Take only what is printed for **that field**. Preferred indicators:

1. Number of PhD holders in the selected field, number interviewed, response rate
2. Employment rate (total; women and men only if both are printed)
3. Unemployment rate, if printed
4. Occupation: university researchers / other intellectual professions / other
5. Economic branch, including **education and research**
6. Inside education and research: **university** / **research institute** / **other organisation or firm**
7. Contract type (permanent, fixed-term, research grant, scholarship, …)
8. Mean net monthly pay (total; by sex only if printed)
9. Use of doctoral skills; whether the doctorate was required or useful
10. Place of work, including abroad

## 4. What you must not do

- Do not call “other organisation or firm” high-school teaching. Schools sit in that residual with other non-university employers. If there is no school-teacher cell, there is no teacher count.
- Do not mix all-PhD national totals with the field-specific row and call the mix “mathematics.”
- Do not interpolate a missing 3-year figure.
- Do not type numbers from memory.

## 5. Files to commit

- `outcomes.csv` — the cells above
- `SOURCES.md` — filled from the template
- Optional: a screenshot or PDF export of the databank view, if you want an audit trail
