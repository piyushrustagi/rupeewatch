# RupeeWatch — INR/USD Volatility Forecasting

**Course:** ECO-6810 Computational Thinking and Programming using AI
**Team:** Arushi Sareen · Piyush Rustagi · Saburi Kapoor
**Project type:** Predictive
**Dashboard:** https://piyushrustagi.github.io/rupeewatch/dashboard.html

---

## Research Question

Can a GARCH(1,1) volatility model provide actionable next-day INR/USD
volatility forecasts that help a corporate treasury desk decide when
to review its hedge ratio — and does it outperform a simple regression
baseline?

**Stakeholder:** Corporate treasury desk managing USD payables and receivables.

**Decision rule:**

| Forecast Vol | Risk State | Action |
|---|---|---|
| < 5% | Normal | Maintain standard hedge ratio |
| 5–8% | Elevated | Review hedge ratio |
| > 8% | Stress | Hedge more aggressively — review all open exposure |

---

## Run the Project

```bash
uv sync
uv run main.py
```

**Runtime:** ~3 minutes (GARCH rolling forecast, 519 test days)

---

## Expected Output

```
=== RupeeWatch Pipeline ===
Fetching INR/USD data from Yahoo Finance...
  Fetched 3,478 trading days  |  2013-01-01 → 2026-05-13
Regression baseline RMSE: 0.003797 | MAE: 0.001802
GARCH(1,1) RMSE: 0.015329 | MAE: 0.012342
Threshold (5%): 0.003607
GARCH passed: False
Next-day forecast (2026-05-14): GARCH 0.088056 annualised vol
Outputs saved to outputs/
Done. Run: uv run main.py
```

---

## Output Files

| File | Contains |
|------|----------|
| `outputs/baseline_metric.json` | Regression baseline RMSE: 0.003797 |
| `outputs/primary_metric.json` | GARCH RMSE: 0.015329, passed: false |
| `outputs/milestone_manifest.json` | Charter lock, source probes, run command |
| `outputs/next_day_forecast.json` | Next trading day volatility and price forecast |
| `outputs/forecast_vs_actual.png` | GARCH vs regression vs actual vol |
| `outputs/model_comparison.png` | RMSE bar chart |
| `outputs/model_metrics.csv` | Tabular RMSE and MAE |

See `outputs/README.md` for the full list of 26 figures and files.

---

## Key Results

| Model | RMSE | MAE | MAPE | Dir. Accuracy |
|-------|------|-----|------|---------------|
| Linear Regression (baseline) | 0.003797 | 0.001802 | — | — |
| GARCH(1,1) | 0.015329 | 0.012342 | — | — |
| EGARCH(1,1)* | 0.011572 | 0.008056 | 23.87% | 2.96% |
| BiLSTM (bias-corrected)* | 0.014963 | 0.010332 | 28.14% | 46.98% |

*From full notebook pipeline (`notebook/RupeeWatch(CPAI).ipynb`)

**Key finding:** GARCH did not beat the regression baseline on RMSE
(passed: false). This null result is reported honestly. BiLSTM
outperforms GARCH on directional accuracy (+44pp) — knowing which
direction volatility is moving matters for the treasury desk even when
RMSE does not improve.

---

## Repository Structure

```
rupeewatch/
├── .github/workflows/
│   └── daily_forecast.yml        # runs uv run main.py daily at 5:30 PM IST
├── artifacts/probes/
│   ├── README.md
│   ├── probe_yfinance.md         # Yahoo Finance one-row proof
│   ├── probe_vix.md              # FRED VIX one-row proof
│   ├── probe_dxy.md              # FRED DXY one-row proof
│   ├── probe_oil.md              # FRED crude oil one-row proof
│   └── probe_ffr.md              # FRED fed funds rate one-row proof
├── data/raw/
│   ├── README.md                 # source descriptions and licence notes
│   ├── usdinr.csv                # full INR/USD dataset 2013–2026
│   ├── probe_vix.csv             # FRED VIX probe (fallback)
│   ├── probe_dxy.csv             # FRED DXY probe (fallback)
│   ├── probe_oil.csv             # FRED crude oil probe (fallback)
│   └── probe_ffr.csv             # FRED fed funds probe (fallback)
├── notebook/
│   ├── README.md                 # section guide and workflow explanation
│   └── RupeeWatch(CPAI).ipynb   # full BiLSTM + HMM + GARCH pipeline
├── outputs/
│   ├── README.md                 # explains all 26 files
│   ├── baseline_metric.json      # required
│   ├── primary_metric.json       # required
│   ├── milestone_manifest.json   # required
│   ├── next_day_forecast.json    # next trading day forecast
│   ├── model_metrics.csv         # tabular RMSE and MAE
│   └── [21 PNG figures]          # see outputs/README.md
├── project_code/
│   ├── __init__.py
│   ├── io.py                     # write_json helper
│   └── template_outputs.py       # metric builders with real values
├── src/
│   └── download_data.py          # original milestone data download script
├── .gitignore
├── AI_USAGE_LOG.md               # detailed tool-by-tool log
├── CHARTER.md                    # V4 — treasury desk framing
├── README.md
├── dashboard.html                # GitHub Pages live dashboard
├── main.py                       # primary reproducible run
├── pyproject.toml
├── report.md                     # final report
└── uv.lock
```

---

## Data Sources

| Source | Series | Access |
|--------|--------|--------|
| Yahoo Finance | USDINR=X — INR/USD daily close | `yfinance` — no key needed |
| FRED API | VIXCLS — CBOE VIX Index | Free API key, `fredapi` |
| FRED API | DTWEXBGS — US Dollar Index | Free API key, `fredapi` |
| FRED API | DCOILWTICO — WTI Crude Oil | Free API key, `fredapi` |
| FRED API | DFF — US Federal Funds Rate | Free API key, `fredapi` |

FRED probe CSVs committed to `data/raw/` — pipeline runs without a
FRED key using cached data.

**Date range:** 2013-01-01 to 2026-05-13 (3,478 trading days)
**Test set:** 2024-05-10 to 2026-05-13 (519 trading days, last 15%)

---

## Full Analysis Pipeline

The complete BiLSTM + HMM + GARCH pipeline is in
`notebook/RupeeWatch(CPAI).ipynb`:

| Section | Contents |
|---------|----------|
| 1 | Data ingestion — INR/USD + 5 FRED macro series |
| 2 | EDA — stationarity (ADF), ARCH effects, fat tails, macro correlations |
| 3 | HMM regime detection — 2-state Gaussian (84% low, 16% high vol) |
| 4 | Feature engineering — 49 features |
| 5 | GARCH(1,1) + EGARCH(1,1) benchmarks, residual diagnostics |
| 6 | BiLSTM — 3-layer bidirectional LSTM, isotonic calibration, SHAP |
| 7 | Policy event study — 19 macro events, surprise vs expected |
| 8 | Next-day treasury briefing — forecast vol, risk state, action |

Stable GARCH + regression logic has been moved to `main.py` for clean
reproducibility. The notebook is the evidence base for the extended
model results in `report.md`.

---

## Automated Daily Forecast

A GitHub Action (`.github/workflows/daily_forecast.yml`) runs every
weekday at 5:30 PM IST:

- Fetches fresh INR/USD data from Yahoo Finance
- Runs GARCH pipeline via `uv run main.py`
- Commits updated `outputs/next_day_forecast.json`
- Dashboard reads the updated forecast automatically
