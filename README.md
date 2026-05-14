# RupeeWatch — INR/USD Volatility Forecasting

**Course:** ECO-6810 Computational Thinking and Programming using AI  
**Team:** Arushi Sareen · Piyush Rustagi · Saburi Kapoor  
**Project type:** Predictive  
**Repo:** piyushrustagi/rupeewatch  
**Dashboard:** https://piyushrustagi.github.io/rupeewatch/dashboard.html

\---

## Research Question

Can a GARCH(1,1) volatility model provide actionable next-day INR/USD
volatility forecasts that help a corporate treasury desk decide when
to review its hedge ratio — and does it outperform a simple regression
baseline?

**Stakeholder:** Corporate treasury desk managing USD payables/receivables.

**Decision rule:**

|Forecast Vol|Risk State|Action|
|-|-|-|
|< 5%|Normal|Maintain standard hedge ratio|
|5–8%|Elevated|Review hedge ratio|
|> 8%|Stress|Hedge more aggressively|

\---

## Run the Project

```bash
uv sync
uv run main.py
```

\---

## Expected Output

```
=== RupeeWatch Pipeline ===
Fetching INR/USD data from Yahoo Finance...
Regression baseline RMSE: 0.003797

GARCH(1,1) RMSE: 0.015329

Outputs saved to outputs/
Done. Run: uv run main.py
```

\---

## Output Files

|File|Contains|
|-|-|
|`outputs/baseline\_metric.json`|Regression baseline RMSE: 0.003797|
|`outputs/primary\_metric.json`|GARCH RMSE: 0.015329, passed: false|
|`outputs/milestone\_manifest.json`|Charter lock, source probes, run command|
|`outputs/next\_day\_forecast.json`|Next trading day volatility forecast|

\---

## Model Results

|Model|RMSE|MAE|MAPE|Dir. Accuracy|
|-|-|-|-|-|
|Linear Regression (baseline)|0.004407|0.003201|—|—|
|GARCH(1,1)|0.013282|0.011281|50.81%|2.56%|
|EGARCH(1,1)|0.011572|0.008056|23.87%|2.96%|
|BiLSTM (bias-corrected)|0.014963|0.010332|28.14%|46.98%|

**Key finding:** GARCH did not beat the regression baseline on RMSE
(passed: false). This null result is reported honestly. BiLSTM
outperforms GARCH on MAE (+8.4%), MAPE (+44.6%), and directional
accuracy (+44pp).

\---

## Repository Structure

```
rupeewatch/
├── data/raw/
│   ├── usdinr.csv
│   ├── probe\_vix.csv
│   ├── probe\_dxy.csv
│   ├── probe\_oil.csv
│   └── probe\_ffr.csv
├── notebook/
│   └── RupeeWatch(CPAI).ipynb
├── outputs/
│   ├── baseline\_metric.json
│   ├── primary\_metric.json
│   ├── milestone\_manifest.json
│   └── next\_day\_forecast.json
├── .github/workflows/
│   └── daily\_forecast.yml
├── main.py
├── report.md
├── AI\_Usage\_Log.md
├── CHARTER.md
└── README.md
```

\---

## Data Sources

|Source|Series|Access|
|-|-|-|
|Yahoo Finance|USDINR=X|`yfinance` — no key needed|
|FRED API|VIXCLS — VIX|Free API key|
|FRED API|DTWEXBGS — DXY|Free API key|
|FRED API|DCOILWTICO — WTI Crude|Free API key|
|FRED API|DFF — Fed Funds Rate|Free API key|

FRED probe CSVs committed to `data/raw/` — pipeline runs without a FRED key.

\---

## Full Pipeline

The complete analysis pipeline is in `notebook/RupeeWatch(CPAI).ipynb`:

1. Data ingestion — INR/USD + 5 FRED macro series
2. EDA — stationarity, ARCH effects, fat tails
3. Regime detection — 2-state Gaussian HMM (75% low, 25% high vol)
4. Feature engineering — 49 features
5. GARCH(1,1) + EGARCH(1,1) benchmarks
6. BiLSTM — 3-layer bidirectional LSTM with macro + regime features
7. Policy event study — 19 macro events
8. Next-day treasury briefing

\---

## Automated Daily Forecast

A GitHub Action runs every weekday at 5:30 PM IST:

* Fetches fresh INR/USD data
* Runs GARCH pipeline
* Saves updated `outputs/next\_day\_forecast.json`
* Dashboard reads the updated forecast automatically

