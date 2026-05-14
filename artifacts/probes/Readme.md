# Source Probes — RupeeWatch

Each file below is a one-row proof that the data source is real and reachable.
Full datasets are fetched programmatically in `main.py`.

| Probe File | Source | Status |
|------------|--------|--------|
| probe_yfinance.md | Yahoo Finance — USDINR=X | ok |
| probe_vix.md | FRED — VIXCLS (VIX Index) | ok |
| probe_dxy.md | FRED — DTWEXBGS (US Dollar Index) | ok |
| probe_oil.md | FRED — DCOILWTICO (WTI Crude Oil) | ok |
| probe_ffr.md | FRED — DFF (Fed Funds Rate) | ok |

All five sources confirmed working. Probe CSVs also committed at
`data/raw/` as machine-readable fallback.
