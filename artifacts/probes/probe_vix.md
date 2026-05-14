# Source Probe — FRED: VIXCLS (CBOE VIX Index)

- **Source name:** FRED API — VIXCLS
- **Access method:** `fredapi.Fred(api_key).get_series("VIXCLS")`
- **URL:** https://fred.stlouisfed.org/series/VIXCLS

- **One-row proof:**

| Date       | VIX Close |
|------------|------------|
| 2026-05-12 | 21.34      |

- **Notes:**  
  Free API key required. Probe cached at `data/raw/probe_vix.csv`.  
  Used as a lagged macroeconomic feature in the BiLSTM pipeline.
