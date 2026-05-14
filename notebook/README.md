# Notebooks — RupeeWatch

## RupeeWatch(CPAI).ipynb

This notebook contains the full analysis pipeline run in Google Colab.

| Section | Contents |
|---------|----------|
| Section 1 | Data ingestion — INR/USD + 5 FRED macro series |
| Section 2 | EDA — stationarity (ADF), fat tails (Jarque-Bera), ACF/PACF, macro correlations |
| Section 3 | HMM regime detection — 2-state Gaussian, Low/High volatility labels |
| Section 4 | Feature engineering — 49 features including macro, technical, regime signals |
| Section 5 | GARCH(1,1) + EGARCH(1,1) benchmarks, residual diagnostics |
| Section 6 | BiLSTM — 3-layer bidirectional LSTM, isotonic calibration, SHAP interpretability |
| Section 7 | Policy event study — 19 macro events, surprise vs expected |
| Section 8 | Next-day treasury briefing — forecast vol, risk state, recommended action |

## Workflow

Exploration and full BiLSTM + HMM pipeline live here.
Stable GARCH + regression logic has been moved to `main.py` for
clean reproducibility — `uv run main.py` runs end-to-end without
opening this notebook.

The notebook is the evidence base for the extended model results
reported in `report.md` Section 5 and Section 6.
