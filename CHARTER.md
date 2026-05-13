# Project Charter — RupeeWatch

| Field | Value |
|-------|-------|
| Team members | Piyush Rustagi, Arushi Sareen, Saburi Kapoor |
| Project type | Predictive |
| Estimated hours per person | ~50 hours |
| Charter version | V4 |
| Date | 13_05_2026 |

---

## 1. Problem and Stakeholder

**Stakeholder:** A corporate treasury desk managing USD payables and
receivables, which needs next-day INR/USD volatility forecasts to
decide whether to hedge more aggressively or maintain standard
hedge ratios.

**Research question:** Can a GARCH(1,1) volatility model provide
actionable next-day INR/USD volatility forecasts that help a
corporate treasury desk decide when to review its hedge ratio —
and does it outperform a simple regression baseline?

**What this project does:**
- Fetches live INR/USD data daily and forecasts next-day
  annualised realised volatility
- Classifies the forecast into a risk state:
  Normal (vol < 5%), Elevated (5–8%), Stress (> 8%)
- Tells the treasury desk whether to maintain or review
  its hedge ratio based on the risk state
- Compares GARCH(1,1) against a regression baseline honestly
  with a pass/fail RMSE threshold
- Reports limitations clearly: not trading advice, models
  can overfit

**Economic Motivation:**

The Indian Rupee is one of the most actively traded emerging-market
currencies and is highly sensitive to global risk sentiment, crude
oil prices, and US dollar strength. Accurate short-horizon volatility
forecasts are directly useful for currency risk management and
hedging decisions.

GARCH models are the standard econometric tool for volatility
forecasting because they capture volatility clustering — the
well-known tendency of large moves to follow large moves. Whether
GARCH outperforms a macro-enhanced regression baseline on INR/USD
is an empirically open question and the core testable claim of
this project.

---

## 2. Main Outcome Variable

- **Name of variable:** 1-day-ahead INR/USD annualised realised
  volatility
- **Unit:** annualised_volatility
- **Construction:** 21-day rolling standard deviation of daily log
  returns, multiplied by √252
- **Source:** Yahoo Finance ticker `USDINR=X`, daily close prices,
  2010-01-01 to present
- **Population/panel:** All trading days in the sample period

---

## 3. Main Quantitative Success Threshold

**Project type:** Predictive

The primary metric is out-of-sample RMSE of GARCH(1,1) conditional
volatility forecasts against realised volatility on the held-out
test set (last 20% of data, chronological split).

The success threshold is: GARCH(1,1) RMSE ≤ 95% of regression
baseline RMSE (i.e. at least 5% improvement). This threshold is
anchored to the baseline computed from the data and saved to
`outputs/baseline_metric.json` before any modelling begins.

A result where GARCH does not beat the baseline is still a valid,
reportable result and will be reported honestly with `passed: false`.

---

## 4. Baseline to Beat

The baseline is computed before any advanced modelling. Using the
INR/USD dataset already committed under `data/`, we fit a linear
regression predicting realised volatility using three lagged features:

- `lag_return_1`: previous day log return
- `lag_vol_5d`: 5-day rolling volatility, lagged 1 day
- `lag_vol_21d`: 21-day rolling volatility, lagged 1 day

The baseline RMSE on the held-out test set is saved to
`outputs/baseline_metric.json` in the required format.

**Baseline result:** RMSE = 0.004407 annualised_volatility.

---

## 5. Falsifiable Hypothesis

GARCH(1,1) will produce a test-set RMSE at least 5% below the
linear regression baseline RMSE of 0.004407
(threshold: 0.004187 annualised_volatility), as estimated by
rolling one-step-ahead conditional variance forecasts on the
held-out test set (last 20% of data, chronological split).

**Current result:** GARCH(1,1) RMSE = 0.013282. `passed: false`.
GARCH did not outperform the regression baseline on RMSE.
This null result is reported honestly and is consistent with
the known difficulty of beating simple regression benchmarks
at short horizons.

However, GARCH provides value as a decision aid independently
of RMSE: its conditional volatility forecast maps directly to
a risk state (Normal / Elevated / Stress) that tells the
treasury desk whether to review its hedge ratio. A model that
correctly identifies stress regimes is useful even if its RMSE
does not beat a naive benchmark.

---

## 6. Data Sources and Access Plan

**Source 1 — Primary**
- Name: Yahoo Finance via `yfinance` Python library
- Ticker: `USDINR=X`
- Frequency: Daily
- Licence: Public market data, free for academic use
- Access method: Programmatic download via `yfinance.download()`
- File used: `data/raw/usdinr.csv` (committed to repo)
- Columns used: Date, Close

**Source 2 — Macroeconomic Features (FRED)**
- Name: FRED API (Federal Reserve Economic Data)
- Series: VIXCLS, DTWEXBGS, DCOILWTICO, DFF
- Frequency: Daily
- Licence: Public domain, free API
- Access method: `fredapi` Python library with free API key
- Probe files: `data/raw/probe_vix.csv`, `data/raw/probe_dxy.csv`,
  `data/raw/probe_oil.csv`, `data/raw/probe_ffr.csv`

---

## 7. Scope Limits

- This is a decision aid for a corporate treasury desk, not
  trading advice. Outputs should not be used to make leveraged
  trading decisions.
- We are not making causal claims. This project measures
  predictive accuracy, not the reasons why INR/USD volatility
  moves.
- We are not building a live dashboard or web app. The output
  is a JSON file and a report, not a production system.
- We are not using high-frequency or intraday data. Unit of
  observation is the trading day.
- The primary graded model is GARCH(1,1). BiLSTM and HMM regime
  detection are extended analyses in the Colab notebook and are
  not the primary graded deliverable.
- Portfolio optimisation, transaction-cost modelling, and
  structural causal inference are out of scope.
- More complex models (BiLSTM, HMM) may overfit on this dataset.
  The regression baseline is a strong benchmark at short horizons
  and this limitation is reported honestly.

---

## 8. Risks and Fallback

**Risk 1:** Yahoo Finance API changes format or becomes unavailable.
Fallback: `data/raw/usdinr.csv` is committed to the repo and the
pipeline loads from cache if the download fails.

**Risk 2:** FRED API key unavailable.
Fallback: Probe CSVs committed as sample data. Pipeline runs
without FRED key using cached data.

**Risk 3:** GARCH fitting fails to converge on some windows.
Fallback: Failed windows use the previous valid forecast.

**Risk 4:** GARCH does not beat the baseline.
This has occurred. Result is reported honestly with `passed: false`.
The project is still complete and fully gradeable.

---

## 9. Reproducibility Checklist

- [x] `uv run main.py` runs end-to-end with no manual intervention
- [x] It writes `outputs/primary_metric.json` containing
  `metric_name`, `value`, `threshold`, `passed`
- [x] It writes `outputs/baseline_metric.json` in the same shape
- [x] `README.md` documents the run command and expected outputs
- [x] All data sources are fetched in-script or committed under
  `data/` with a licence note

---

## Team Roles and Responsibilities

| Member | Primary Responsibility | Est. Hours |
|--------|----------------------|------------|
| Piyush Rustagi | GARCH(1,1) and EGARCH(1,1) modelling, rolling 1-step-ahead forecast pipeline, residual diagnostics, `outputs/` JSON schema validation, repository setup, GitHub workflow | ~50 hrs |
| Arushi Sareen | Data ingestion (Yahoo Finance + FRED), feature engineering, full EDA (ADF, ACF/PACF, fat-tail diagnostics, macro correlations), `README.md` | ~50 hrs |
| Saburi Kapoor | BiLSTM architecture, HMM regime detection, SHAP interpretability, policy event study, RMSE/MAE evaluation, `report.md`, `AI_USAGE_LOG.md` | ~50 hrs |

All three members contributed to project scoping, charter drafting, and final review.

---

**Charter status:** V4 — Updated 2026-05-13, submitted for approval

---

## Sign-off

| Name | Date |
|------|------|
| Piyush Rustagi | 2026-05-13 |
| Arushi Sareen | 2026-05-13 |
| Saburi Kapoor | 2026-05-13 |
