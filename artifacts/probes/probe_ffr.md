\# Source Probe — FRED: DFF (US Federal Funds Rate)



\- \*\*Source name:\*\* FRED API — DFF

\- \*\*Access method:\*\* `fredapi.Fred(api\_key).get\_series('DFF')`

\- \*\*URL:\*\* https://fred.stlouisfed.org/series/DFF

\- \*\*One-row proof:\*\*



| Date | Fed Funds Rate (%) |

|------|--------------------|

| 2026-05-12 | 4.33 |



\- \*\*Notes:\*\* Free API key required. Probe cached at `data/raw/probe\_ffr.csv`. Used as lagged macro feature in BiLSTM pipeline.

