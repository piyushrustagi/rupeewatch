# Source Probe — FRED: DTWEXBGS (US Dollar Index)

- Source name: FRED API — DTWEXBGS
- Access method: fredapi.Fred(api_key).get_series('DTWEXBGS')
- URL: https://fred.stlouisfed.org/series/DTWEXBGS
- One-row proof:

| Date | DXY Value |
|------|-----------|
| 2026-05-09 | 118.42 |

- Notes: Free API key required. Successfully loaded in Colab. Probe cached at data/raw/probe_dxy.csv. Weekly frequency, forward-filled to daily.

