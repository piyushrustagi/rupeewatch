# Data Sources — RupeeWatch

## Committed Files

| File | Source | Series | Licence |
|------|--------|--------|---------|
| usdinr.csv | Yahoo Finance | USDINR=X — INR/USD daily close | Public market data, free for academic use |
| probe_vix.csv | FRED API | VIXCLS — CBOE VIX Index | Public domain, free API |
| probe_dxy.csv | FRED API | DTWEXBGS — US Dollar Index | Public domain, free API |
| probe_oil.csv | FRED API | DCOILWTICO — WTI Crude Oil | Public domain, free API |
| probe_ffr.csv | FRED API | DFF — US Federal Funds Rate | Public domain, free API |

## How Data Is Fetched

All data is fetched programmatically in 'main.py':

- Yahoo Finance: yfinance.download('USDINR=X', start='2013-01-01') — no API key required
- FRED API: fredapi.Fred(api_key).get_series('VIXCLS') — free API key required; probe CSVs committed as fallback so pipeline runs without a key

## Access Rules

- Yahoo Finance data is public and free for academic use
- FRED data is public domain, provided by the Federal Reserve Bank of St. Louis
- No data purchase or subscription required

## Intentionally Excluded

- Raw FRED full series CSVs — only probe rows committed to keep repo size small
- Intraday or tick data — not used in this project
