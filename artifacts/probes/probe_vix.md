\# Source Probe — FRED: VIXCLS (CBOE VIX Index)



\- \*\*Source name:\*\* FRED API — VIXCLS

\- \*\*Access method:\*\* `fredapi.Fred(api\_key).get\_series('VIXCLS')`

\- \*\*URL:\*\* https://fred.stlouisfed.org/series/VIXCLS

\- \*\*One-row proof:\*\*



| Date | VIX Close |

|------|-----------|

| 2026-05-12 | 21.34 |



\- \*\*Notes:\*\* Free API key required. Probe cached at `data/raw/probe\_vix.csv`. Used as lagged macro feature in BiLSTM pipeline.

