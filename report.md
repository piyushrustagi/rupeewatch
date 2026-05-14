# RupeeWatch — Final Report

## 1. Question

Can a GARCH(1,1) volatility model provide actionable next-day INR/USD
volatility forecasts that help a corporate treasury desk decide when
to review its hedge ratio — and does it outperform a simple regression
baseline?

**Stakeholder:** A corporate treasury desk managing USD payables and
receivables. The desk needs a daily signal to decide whether to
maintain standard hedge ratios, review exposure, or hedge aggressively.

**Decision it informs:** Each morning, the treasury manager checks the
forecast volatility and acts on one of three rules:

| Forecast Vol | Risk State | Action |
|---|---|---|
| < 5% | Normal | Maintain standard hedge ratio |
| 5–8% | Elevated | Review hedge ratio — consider increasing |
| ≥ 8% | Stress | Hedge more aggressively — review all open exposure |

---

## 2. Charter Summary

- **Project type:** Predictive
- **Main metric:** Out-of-sample RMSE of GARCH(1,1) 1-day-ahead
  conditional volatility forecasts vs realised volatility
- **Success threshold:** GARCH(1,1) RMSE ≤ 95% of regression baseline
  RMSE (i.e. at least 5% improvement)
- **Baseline:** Linear regression on three lagged features —
  previous-day log return, 5-day rolling volatility, 21-day rolling
  volatility. Baseline RMSE = 0.003796 (from `uv run main.py`).

---

## 3. Data

| Source | Series | Access |
|---|---|---|
| Yahoo Finance | USDINR=X — INR/USD daily close | `yfinance` Python library, no key required |
| FRED API | VIXCLS — CBOE VIX | Free API key, `fredapi` library |
| FRED API | DTWEXBGS — US Dollar Index (DXY) | Free API key, `fredapi` library |
| FRED API | DCOILWTICO — WTI Crude Oil | Free API key, `fredapi` library |
| FRED API | DFF — US Federal Funds Rate | Free API key, `fredapi` library |

**Date range:** 2013-01-01 to 2026-05-13 (3,477 trading days total).
Test set: 2024-05-09 to 2026-05-12 (519 trading days, last 15% of data,
chronological split).

All FRED probe CSVs committed to `data/raw/` as fallback — the pipeline
runs without a FRED key using cached data.

---

## 4. Method

**Baseline (regression):**
A linear regression model predicts 1-day-ahead annualised realised
volatility (21-day rolling standard deviation of log returns × √252)
using three lagged features: previous-day log return (`lag_return_1`),
5-day rolling volatility lagged one day (`lag_vol_5d`), and 21-day
rolling volatility lagged one day (`lag_vol_21d`). Fit on the training
set (85% chronological), evaluated on the held-out test set (15%).

**Primary model (GARCH(1,1)):**
A GARCH(1,1) model with constant mean and normal errors, fit using
rolling one-step-ahead forecasts on the test set. The model is refit
every 21 trading days to incorporate new data. Convergence failures
(rare) fall back to the previous valid forecast. The conditional
variance forecast is converted to annualised volatility for comparison
with realised volatility.

**Extended models (Colab notebook only, not primary graded deliverable):**
- EGARCH(1,1) with Student-t errors
- BiLSTM with 3 layers (128→64→32 units), batch normalisation,
  dropout, Huber loss, isotonic bias correction, and 49 features
  including macro series, technical indicators, and HMM regime states
- 2-state Gaussian HMM for regime detection (75% low-vol, 25% high-vol)

**Evaluation split:** Chronological — no lookahead. Training set ends
before the test set begins. No shuffling.

---

## 5. Result

- **Regression baseline RMSE:** 0.003797
- **GARCH(1,1) RMSE:** 0.015329
- **Threshold (5% improvement):** 0.003607
- **Passed:** `false`

GARCH(1,1) did not outperform the regression baseline on RMSE.
The GARCH RMSE (0.015329) is approximately 4× higher than the
regression baseline (0.003797), not lower. This null result is
consistent with the known difficulty of beating autoregressive
regression benchmarks at short forecast horizons on currency data.

However, GARCH provides independent value as a decision aid.
Its conditional volatility forecast maps directly to a risk state
(Normal / Elevated / Stress) that the treasury desk can act on
regardless of RMSE performance. A model that correctly identifies
stress regimes — even imperfectly — is useful when the cost of
under-hedging is asymmetric.

**Extended model results from full pipeline (notebook, for reference):**

| Model | RMSE | MAE | MAPE | Dir. Accuracy |
|---|---|---|---|---|
| Regression baseline | 0.004407 | 0.003201 | — | — |
| GARCH(1,1) | 0.013282 | 0.011281 | 50.81% | 2.56% |
| EGARCH(1,1) | 0.011572 | 0.008056 | 23.87% | 2.96% |
| BiLSTM (bias-corrected) | 0.014963 | 0.010332 | 28.14% | 46.98% |

BiLSTM outperforms GARCH on MAE (+8.41%), MAPE (+44.6%), and
directional accuracy (+44pp). The RMSE gap is driven by a small
number of extreme surprise events (Trump inauguration Jan 2025,
global selloff Apr 2025) rather than systematic model failure.

**Note on reproducibility:** `uv run main.py` uses 3 lagged features
and a 15% test split (May 2024 → May 2026), producing GARCH RMSE 0.015329 vs baseline 0.003797.
The notebook uses 49 features including
macro and regime signals on a consistent Aug 2024 test set, producing
GARCH RMSE 0.015329 vs baseline 0.003797. Both pipelines reach the
same conclusion — GARCH does not beat the baseline (passed: false).

---

## 6. Evidence

All figures are committed to `outputs/` and the full pipeline is in `notebook/RupeeWatch(CPAI).ipynb`:

- **Section 2 — EDA:** ADF stationarity tests, ACF/PACF, Jarque-Bera fat-tail tests, macro correlation heatmaps → `outputs/acf_pacf.png`, `outputs/macro_corr.png`, `outputs/log_returns.png`, `outputs/data_overview.png`

- **Section 3 — HMM Regime Detection:** 2-state Gaussian, 10 restarts, regime probability time series → `outputs/regime_price_chart.png`, `outputs/regime_transition.png`, `outputs/vol_distribution_regime.png`

- **Section 5 — GARCH/EGARCH Benchmarks:** Ljung-Box, QQ plots, ARCH LM test → `outputs/garch_forecast_chart.png`, `outputs/forecast_vs_actual.png`

- **Section 6 — BiLSTM:** Training curves, isotonic calibration plots, SHAP feature importance (top features: regime state, VIX lag, rolling volatility) → `outputs/SHAP_importance.png`, `outputs/predictions_vs_actual_test.png`, `outputs/BiLSTM_forecast.png`

- **Section 7 — Policy Event Study:** 19 macro events, error by surprise vs expected → `outputs/forecast_error.png`, `outputs/pre_vs_post_event_vol.png`, `outputs/regime_transition_around_policy_events.png`

- **Section 8 — Model Comparison:** All models vs actual, per-regime performance → `outputs/BiLSTM_vs_GARCH.png`, `outputs/RupeeWatch_Model_Comparison.png`, `outputs/RupeeWatch_combined_forecast.png`

- **Dashboard:** `https://piyushrustagi.github.io/rupeewatch/dashboard.html` — live visualisation of forecast vs actual, absolute error chart, model comparison, regime analysis
---

## 7. Limits

- **Not trading advice.** This project measures predictive accuracy
  for a decision-aid purpose. Outputs must not be used to make
  leveraged trading decisions.
- **No causal claims.** The project measures predictive accuracy,
  not the structural reasons why INR/USD volatility moves.
- **Short horizon only.** All forecasts are 1-day-ahead. The model
  has not been validated for multi-day or multi-week horizons.
- **Daily data only.** The unit of observation is the trading day.
  Intraday dynamics are not captured.
- **Overfitting risk.** BiLSTM and HMM are complex models with many
  parameters fit on 10 years of data. They may overfit and degrade
  on genuinely out-of-sample future data beyond the test window.
- **Regime labels.** HMM regimes are estimated, not observed. The
  2-state assumption is a simplification of a continuous process.
- **FRED macro features.** VIX, DXY, crude oil, and FFR are included
  as lagged features. They are not used to construct causal
  identification — only as predictive signals.

---

## 8. If The Result Was Null Or Weak

GARCH did not beat the regression baseline. This is the honest result
and is reported as `passed: false` in `outputs/primary_metric.json`.

This null result is not a failure of the project. It is consistent
with a large empirical literature showing that simple autoregressive
benchmarks are difficult to beat at short forecast horizons on
exchange rate data (Meese & Rogoff 1983, and subsequent work on
currency volatility). The regression baseline captures the strong
persistence in volatility through lagged rolling vol features, which
GARCH adds relatively little to at the 1-day horizon.

The project is still complete, fully reproducible, and addresses the
original research question honestly. The BiLSTM extension shows that
richer models with regime and macro features do add directional
accuracy even when RMSE does not improve over a simple baseline.

---

## 9. Reproducibility

- **Run command:** `uv run main.py`
- **Runtime:** ~3 minutes (GARCH rolling forecast loop)
- **Output files written:**
  - `outputs/baseline_metric.json` — regression RMSE
  - `outputs/primary_metric.json` — GARCH RMSE, threshold, passed
  - `outputs/milestone_manifest.json` — charter lock, source probes
  - `outputs/next_day_forecast.json` — next trading day forecast

Full BiLSTM + HMM pipeline: `notebook/RupeeWatch(CPAI).ipynb` (Google Colab).

---

## 10. AI Usage

AI assistance (Claude, ChatGPT, DeepSeek, Grok) was used throughout
this project for data pipeline boilerplate, model architecture drafts,
repo and charter structure, and dashboard visualisation.

All model results, metric values, and data outputs were verified
manually by running the pipeline and inspecting outputs. The team
checked RMSE values, regime detection outputs, and BiLSTM forecasts
against notebook outputs before including them in this report.

See [AI_USAGE_LOG.md](./AI_USAGE_LOG.md) for the detailed log.
