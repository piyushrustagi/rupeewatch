\# Data Sources — RupeeWatch



\## Committed Files



| File | Source | Series | Licence |

|------|--------|--------|---------|

| `usdinr.csv` | Yahoo Finance | USDINR=X — INR/USD daily close | Public market data, free for academic use |

| `probe\_vix.csv` | FRED API | VIXCLS — CBOE VIX Index | Public domain, free API |

| `probe\_dxy.csv` | FRED API | DTWEXBGS — US Dollar Index | Public domain, free API |

| `probe\_oil.csv` | FRED API | DCOILWTICO — WTI Crude Oil | Public domain, free API |

| `probe\_ffr.csv` | FRED API | DFF — US Federal Funds Rate | Public domain, free API |



\## How Data Is Fetched



All data is fetched programmatically in `main.py`:



\- \*\*Yahoo Finance:\*\* `yfinance.download('USDINR=X', start='2013-01-01')`

&#x20; — no API key required

\- \*\*FRED API:\*\* `fredapi.Fred(api\_key).get\_series('VIXCLS')` etc.

&#x20; — free API key required; probe CSVs are committed as fallback so

&#x20; the pipeline runs without a key



\## Access Rules



\- Yahoo Finance data is public and free for academic use

\- FRED data is public domain, provided by the Federal Reserve Bank of St. Louis

\- No data purchase or subscription required



\## Intentionally Excluded



\- Raw FRED full series CSVs — only probe rows committed to keep repo size small

\- Intraday or tick data — not used in this project

