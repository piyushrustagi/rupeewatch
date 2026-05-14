# Source Probe — FRED: DCOILWTICO (WTI Crude Oil)

- **Source name:** FRED API — DCOILWTICO
- **Access method:** `fredapi.Fred(api_key).get_series("DCOILWTICO")`
- **URL:** https://fred.stlouisfed.org/series/DCOILWTICO

- **One-row proof:**

| Date       | WTI Price (USD/barrel) |
|------------|------------------------|
| 2026-05-12 | 61.53                  |

- **Notes:**  
  Free API key required. Probe cached at `data/raw/probe_oil.csv`.  
  Used as a lagged macroeconomic feature in the forecasting pipeline.
