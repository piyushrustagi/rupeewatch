# RupeeWatch — Final Report

---

## 1. Question

Every morning, a corporate treasury manager at an Indian firm faces a
simple but costly decision: should we hedge our USD exposure more
aggressively today, or is the INR stable enough to hold our current
position?

This project asks whether a GARCH(1,1) volatility model can provide
a reliable next-day INR/USD volatility forecast that helps that manager
make a better-informed call — and whether it outperforms a simple
regression baseline.

**Stakeholder:** A corporate treasury desk managing USD payables and
receivables. The cost of getting this wrong is asymmetric: under-hedging
during a volatility spike is far more damaging than over-hedging during
a calm period.

**Decision it informs:** Each morning, the treasury manager reads the
forecast and acts on one of three rules:

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
  RMSE — at least 5% improvement over the naive lagged-volatility
  benchmark
- **Baseline:** Linear regression on three lagged features —
  previous-day log return, 5-day rolling volatility, 21-day rolling
  volatility. Baseline RMSE = 0.003797 (from `uv run main.py`)

---

## 3. Data

The project uses one primary market series and four macroeconomic
control series, all publicly available and fetched programmatically.

| Source | Series | Access |
|---|---|---|
| Yahoo Finance | USDINR=X — INR/USD daily close | `yfinance` — no key required |
| FRED API | VIXCLS — CBOE VIX Index | Free API key, `fredapi` |
| FRED API | DTWEXBGS — US Dollar Index (DXY) | Free API key, `fredapi` |
| FRED API | DCOILWTICO — WTI Crude Oil | Free API key, `fredapi` |
| FRED API | DFF — US Federal Funds Rate | Free API key, `fredapi` |

**Date range:** 2013-01-01 to 2026-05-13 — 3,478 trading days.
Test set: 2024-05-09 to 2026-05-13 — 519 trading days (last 15%,
chronological split). See `outputs/data_overview.png` for the full
picture of INR/USD price, realised volatility, VIX, and crude oil
across the sample period.

All FRED probe CSVs are committed to `data/raw/` — the pipeline runs
without a FRED key using cached data.

---

## 4. Method

**Step 1 — Baseline (regression):**
Before building anything complex, we establish a simple benchmark.
A linear regression model predicts 1-day-ahead annualised realised
volatility using three lagged features: previous-day log return
(`lag_return_1`), 5-day rolling volatility (`lag_vol_5d`), and 21-day
rolling volatility (`lag_vol_21d`). This captures the well-known
persistence of volatility — yesterday's vol is a strong predictor of
today's — without any econometric machinery. Fit on the training set
(85% of data, chronologically), evaluated on the held-out test set
(15%). Baseline RMSE = 0.003797.

**Step 2 — Primary model (GARCH(1,1)):**
GARCH(1,1) is the standard econometric model for volatility
forecasting. It explicitly models volatility clustering — the tendency
of large moves to follow large moves — through an autoregressive
structure on the conditional variance. We fit a rolling 1-step-ahead
forecast on the test set, refitting every 21 trading days to incorporate
new data. On rare convergence failures, the previous valid forecast is
carried forward. The conditional variance is converted to annualised
volatility for comparison with realised vol.

**Step 3 — Extended pipeline (notebook only):**
The Colab notebook extends the analysis to:
- EGARCH(1,1) with Student-t errors — captures asymmetric volatility
- BiLSTM with 49 features — macro series, technical indicators, HMM
  regime states, Huber loss, isotonic bias correction
- 2-state Gaussian HMM — identifies Low/High volatility regimes across
  the full sample

These are not the primary graded deliverable. They are evidence for
the research question. The GARCH vs regression comparison is the core
test.

**Evaluation split:** Strictly chronological. No lookahead. Training
ends before the test set begins. No shuffling at any stage.

---

## 5. Result

- **Regression baseline RMSE:** 0.003797
- **GARCH(1,1) RMSE:** 0.015329
- **Threshold (5% improvement):** 0.003607
- **Passed:** `false`

GARCH(1,1) did not outperform the regression baseline. The GARCH RMSE
(0.015329) is approximately 4× higher than the regression baseline
(0.003797). This is a null result and is reported honestly.

The economic interpretation matters here. The regression baseline
predicts a smoothed 21-day rolling volatility using its own lags —
essentially an autocorrelation machine. GARCH predicts daily conditional
variance, which is a noisier target. At a 1-day horizon, the additional
econometric structure of GARCH adds relatively little over lagged
rolling volatility, consistent with the Meese-Rogoff finding that
simple benchmarks are hard to beat on short-horizon currency forecasts.

Despite failing the RMSE threshold, GARCH retains practical value as a
decision aid. Its conditional volatility forecast maps directly to a
risk state (Normal / Elevated / Stress) that the treasury desk can act
on. The cost of under-hedging is asymmetric — correctly flagging a
Stress regime matters even if the exact vol estimate is imprecise.

**Extended pipeline results (from `notebook/RupeeWatch(CPAI).ipynb`):**

| Model | RMSE | MAE | MAPE | Dir. Accuracy |
|---|---|---|---|---|
| Regression baseline | 0.004407 | 0.003201 | — | — |
| GARCH(1,1) | 0.013282 | 0.011281 | 50.81% | 2.56% |
| EGARCH(1,1) | 0.011572 | 0.008056 | 23.87% | 2.96% |
| BiLSTM (bias-corrected) | 0.014963 | 0.010332 | 28.14% | 46.98% |

The BiLSTM, equipped with macro and regime signals, outperforms GARCH
on MAE (+8.4%), MAPE (+44.6%), and directional accuracy (+44pp). This
suggests that knowing which direction volatility is moving — not just
its level — is where richer models add value for the treasury desk.

**Note on reproducibility:** `uv run main.py` uses 3 lagged features
on a 15% test split (May 2024 → May 2026), producing GARCH RMSE
0.015329 vs baseline 0.003797. The notebook uses 49 features on an
Aug 2024 test set, producing GARCH RMSE 0.013282 vs baseline 0.004407.
Both pipelines reach the same conclusion — GARCH does not beat the
baseline (passed: false).

---

## 6. Evidence

All figures are committed to `outputs/` and open directly in the repo.
The full pipeline is in `notebook/RupeeWatch(CPAI).ipynb`.

**EDA — Data and Volatility Structure**
- [`outputs/data_overview.png`](outputs/data_overview.png) — INR/USD
  price, realised vol, VIX, and WTI crude across 2013–2026
- [`outputs/price_returns.png`](outputs/price_returns.png) — daily
  closing price and log returns with key macro events annotated
- [`outputs/rolling_volatility.png`](outputs/rolling_volatility.png)
  — realised vol across 10/21/63-day windows; volatility clustering
  clearly visible
- [`outputs/acf_pacf.png`](outputs/acf_pacf.png) — ACF/PACF of
  returns and squared returns; ARCH effects confirmed
- [`outputs/macro_corr.png`](outputs/macro_corr.png) — macro feature
  correlation matrix; VIX and DXY show meaningful correlation with vol
- [`outputs/log_returns.png`](outputs/log_returns.png) — fat-tailed
  distribution confirmed by Jarque-Bera test

**HMM Regime Detection**
- [`outputs/regime_price_chart.png`](outputs/regime_price_chart.png)
  — INR/USD price with Low/High vol regime shading across full sample
- [`outputs/regime_transition.png`](outputs/regime_transition.png)
  — regime transition probabilities and detected states over time
- [`outputs/vol_distribution_regime.png`](outputs/vol_distribution_regime.png)
  — return and volatility distributions by regime; High vol median
  6.9% vs Low vol 4.7%

**GARCH/EGARCH Benchmarks**
- [`outputs/garch_forecast_chart.png`](outputs/garch_forecast_chart.png)
  — GARCH and EGARCH conditional volatility vs realised vol; full
  sample in-sample fit and test set out-of-sample forecast
- [`outputs/forecast_vs_actual.png`](outputs/forecast_vs_actual.png)
  — GARCH vs regression vs actual on test set

**BiLSTM Model**
- [`outputs/predictions_vs_actual_test.png`](outputs/predictions_vs_actual_test.png)
  — BiLSTM predicted vs actual; scatter plot and residuals over time
- [`outputs/BiLSTM_forecast.png`](outputs/BiLSTM_forecast.png)
  — BiLSTM forecast with over/under-prediction periods identified
- [`outputs/SHAP_importance.png`](outputs/SHAP_importance.png)
  — SHAP feature importance; `regime_streak` is the top predictor,
  followed by `us_ffr_lag1` and rolling vol features

**Policy Event Study**
- [`outputs/forecast_error.png`](outputs/forecast_error.png)
  — BiLSTM absolute forecast error mapped to policy events; error
  spikes at Trump inauguration (Jan 2025) and global selloff (Apr 2025)
- [`outputs/pre_vs_post_event_vol.png`](outputs/pre_vs_post_event_vol.png)
  — average volatility pre vs post event by category; RBI Crisis
  events show the largest post-event vol increase
- [`outputs/regime_transition_around_policy_events.png`](outputs/regime_transition_around_policy_events.png)
  — regime transitions concentrated around surprise events

**Model Comparison**
- [`outputs/BiLSTM_vs_GARCH.png`](outputs/BiLSTM_vs_GARCH.png)
  — BiLSTM vs GARCH forecast on test set; green = BiLSTM wins,
  red = GARCH wins
- [`outputs/RupeeWatch_Model_Comparison.png`](outputs/RupeeWatch_Model_Comparison.png)
  — all four models on RMSE, MAE, MAPE, and directional accuracy
- [`outputs/RupeeWatch_combined_forecast.png`](outputs/RupeeWatch_combined_forecast.png)
  — all models vs actual realised volatility on test period

**Live Dashboard:**
[`https://piyushrustagi.github.io/rupeewatch/dashboard.html`](https://piyushrustagi.github.io/rupeewatch/dashboard.html)
— live forecast, signal box, absolute error chart, regime analysis,
model comparison, updated daily via GitHub Actions.

---

## 7. Limits

- **Not trading advice.** This project measures predictive accuracy
  for a decision-aid purpose only. Outputs must not be used to make
  leveraged trading decisions.
- **No causal claims.** The project measures predictive accuracy, not
  the structural reasons why INR/USD volatility moves. SHAP values
  reflect predictive importance, not causal effects.
- **Short horizon only.** All forecasts are 1-day-ahead. The model
  has not been validated for multi-day or multi-week horizons.
- **Daily data only.** The unit of observation is the trading day.
  Intraday dynamics are not captured.
- **Overfitting risk.** BiLSTM and HMM are complex models with many
  parameters fit on 10 years of data. They may overfit and degrade
  on genuinely out-of-sample future data beyond the test window.
- **Regime labels are estimates.** HMM regimes are inferred, not
  observed. The 2-state assumption is a simplification of a continuous
  process. Labels may shift across different random seeds or sample
  lengths.
- **Macro features are predictive signals only.** VIX, DXY, crude oil,
  and FFR are lagged predictors, not causal instruments. No
  identification strategy is claimed.

---

## 8. If The Result Was Null Or Weak

GARCH did not beat the regression baseline. This is the honest result
and is reported as `passed: false` in `outputs/primary_metric.json`.

This is not a failure of the project. It is consistent with a large
empirical literature showing that simple autoregressive benchmarks are
difficult to beat at short forecast horizons on exchange rate data
(Meese & Rogoff 1983). The regression baseline captures strong
volatility persistence through lagged rolling vol features. GARCH adds
relatively little at a 1-day horizon because the conditional variance
update is dominated by the same persistence signal the regression
already captures.

The project is complete, reproducible, and answers the research
question honestly. The BiLSTM extension demonstrates that macro and
regime features do add directional accuracy — suggesting that more
information helps the treasury desk even when raw RMSE does not improve
over a naive benchmark.

---

## 9. Reproducibility

- **Run command:** `uv run main.py`
- **Runtime:** ~3 minutes (GARCH rolling forecast loop, 519 days)
- **Output files written:**
  - `outputs/baseline_metric.json` — regression RMSE and MAE
  - `outputs/primary_metric.json` — GARCH RMSE, threshold, passed
  - `outputs/milestone_manifest.json` — charter lock, source probes
  - `outputs/next_day_forecast.json` — next trading day vol and price
  - `outputs/forecast_vs_actual.png` — GARCH vs regression vs actual
  - `outputs/model_comparison.png` — RMSE bar chart
  - `outputs/model_metrics.csv` — tabular RMSE and MAE

Full BiLSTM + HMM pipeline: `notebook/RupeeWatch(CPAI).ipynb`
(Google Colab, ~45 minutes runtime).

---

## 10. AI Usage

AI tools (Claude, ChatGPT, DeepSeek, Grok) were used throughout for
data pipeline boilerplate, model architecture drafts, repo structure,
and dashboard visualisation. Every model result, metric value, and data
output was verified manually by running the pipeline and cross-checking
against notebook outputs. One data leakage error (scaler fit on full
dataset before split) and one unit mismatch (GARCH annualisation) were
caught and corrected during manual review.

See [AI_USAGE_LOG.md](./AI_USAGE_LOG.md) for the full detailed log.
