# ISTAT extract checklist

Refresh when Istat publishes the next doctorate-placement release.

1. Open the press release: https://www.istat.it/comunicato-stampa/linserimento-professionale-dei-dottori-di-ricerca-anno-2025/
2. Download the Excel tables and the PDF report.
3. Confirm the official group closest to mathematics. In 2025 that was **Scientifico**, defined in footnote iii (biology, chemistry, biotechnology, nutrition, mathematics, statistics, physics).
4. Copy only printed cells into `outcomes.csv`. Keep `field` = `Scientifico`, `STEM`, or `all`.
5. Do not treat *istruzione non universitaria* as a mathematics-teacher count unless Istat prints that cross.
6. Replace `Tavole.xlsx` with the new official file and update `SOURCES.md`.
