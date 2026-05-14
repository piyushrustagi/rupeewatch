# Outputs — RupeeWatch

This folder contains all files written by `uv run main.py` and
figures from the full analysis pipeline.

## Required JSON Files

| File | Contains |
|------|----------|
| `baseline_metric.json` | Regression baseline RMSE: 0.003797 |
| `primary_metric.json` | GARCH(1,1) RMSE: 0.015329, passed: false |
| `milestone_manifest.json` | Charter lock, source probes, run command |
| `next_day_forecast.json` | Next trading day volatility and price forecast |

## Figures (from notebook pipeline)

| File | Section | Description |
|------|---------|-------------|
| `data_overview.png` | Section 1 | INR/USD price, realised vol, VIX, crude oil |
| `price_returns.png` | Section 2 | Daily closing price and log returns |
| `log_returns.png` | Section 2 | Log returns distribution |
| `acf_pacf.png` | Section 2 | ACF/PACF — returns and squared returns |
| `macro_corr.png` | Section 2 | Macro feature correlation matrix |
| `rolling_volatility.png` | Section 2 | Realised volatility — multiple windows |
| `regime_price_chart.png` | Section 3 | HMM regime detection — price and vol |
| `regime_transition.png` | Section 3 | Regime transitions around policy events |
| `vol_distribution_regime.png` | Section 3 | Volatility distribution by regime |
| `garch_forecast_chart.png` | Section 5 | GARCH benchmark conditional volatility |
| `forecast_vs_actual.png` | Section 5 | GARCH vs regression vs actual |
| `predictions_vs_actual_test.png` | Section 6 | BiLSTM predicted vs actual |
| `BiLSTM_forecast.png` | Section 6 | BiLSTM forecast residuals over time |
| `SHAP_importance.png` | Section 6 | SHAP feature importance — top 20 |
| `forecast_error.png` | Section 7 | Policy event study — forecast error spikes |
| `pre_vs_post_event_vol.png` | Section 7 | Pre vs post event volatility |
| `regime_transition_around_policy_events.png` | Section 7 | Regime transitions around events |
| `BiLSTM_vs_GARCH.png` | Section 8 | BiLSTM vs GARCH forecast comparison |
| `RupeeWatch_Model_Comparison.png` | Section 8 | All models — RMSE, MAE, MAPE, Dir. Accuracy |
| `RupeeWatch_combined_forecast.png` | Section 8 | All models vs actual realised volatility |

## Tables

| File | Description |
|------|-------------|
| `model_metrics.csv` | RMSE and MAE for regression and GARCH |
| `model_comparison.png` | Model comparison bar chart |
