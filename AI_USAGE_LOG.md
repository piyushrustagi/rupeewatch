# AI Usage Log — RupeeWatch

Following is a record of how AI helped us in this project, what we
trusted, and what we checked ourselves. Development began in Colab
on May 1; the GitHub repo was formalised on May 6.

---

## Log

| Date | Tool | What we used it for | What we verified ourselves |
|---|---|---|---|
| 2026-05-01 | Claude | Drafted the Yahoo Finance ingestion cell: `yf.download`, MultiIndex column flattening, `dropna(subset=['Close'])` guard, and CSV cache write | Ran the cell and checked first/last rows against Yahoo Finance web quotes; noticed `Volume` was all zeros for a currency pair — confirmed it doesn't affect downstream features; verified date index was timezone-naive |
| 2026-05-01 | ChatGPT | Asked for an overview of standard FX volatility feature engineering approaches — which rolling windows are used in practice and why | Used the suggested 5/21/63-day windows as a starting point; verified that `np.sqrt(252)` annualisation was applied consistently and not double-counted in the chart vs the feature pipeline |
| 2026-05-02 | Claude | Built the FRED API fetch loop for all five macro series and the `ffill` logic to align monthly `repo_rate` to daily trading days | Verified `INDIRLTLT01STM` is a long-term bond rate proxy, not the RBI policy repo rate — added a comment; confirmed DXY failed to load on one run and added probe CSV fallback rather than silently dropping |
| 2026-05-02 | DeepSeek | Asked which statistical tests belong in an FX volatility EDA and how to interpret ADF and Jarque-Bera outputs in plain language | Cross-checked every interpretation against our actual p-values; dropped the Ljung-Box suggestion at this stage because residuals didn't exist yet — added it correctly in the GARCH diagnostics section later |
| 2026-05-04 | Claude | Drafted the 3-layer BiLSTM architecture: `Bidirectional(LSTM(128→64→32))`, `BatchNormalization`, `Dropout(0.3)`, `EarlyStopping`, `ReduceLROnPlateau`, and `MinMaxScaler` fit-on-train-only pattern | Caught that Claude's draft called `scaler.fit_transform` on the full dataset before the split — a data leakage error; fixed to `fit` only on training rows; moved `Dropout` after each layer not just the last; re-ran training from scratch after the fix |
| 2026-05-04 | Grok | Asked whether isotonic calibration or Platt scaling is more appropriate for correcting LSTM forecast bias on financial time series | Chose isotonic regression based on the explanation; verified calibration was fit only on validation set and that calibrated forecasts were monotone before applying to test set |
| 2026-05-05 | Claude | Generated the GARCH(1,1) rolling 1-step-ahead forecast loop using the `arch` library — `arch_model` setup, `model.fit(disp='off')`, variance forecast extraction, refit-every-21-days logic | Found Claude used a slightly outdated variance-forecast index path; corrected against current `arch` 5.x docs; confirmed GARCH output was annualised consistently with BiLSTM before computing RMSE — unit mismatch would have invalidated the comparison |
| 2026-05-05 | ChatGPT | Asked for a plain-English explanation of why GARCH models often fail to beat simple autoregressive benchmarks at short horizons | Used the explanation to frame Section 8 of the report honestly; confirmed our result matches the Meese-Rogoff literature rather than being a modelling error |
| 2026-05-06 | Claude | Set up the GitHub repo: `pyproject.toml` with `uv` dependencies, `CHARTER.md` V1 template, `README.md` with run command, probe CSV commits, and three required JSON output schemas | Verified all three JSON files matched the course-required schema field by field; caught that `primary_metric.json` was missing `threshold` and `passed` fields — added them; confirmed `uv run main.py` ran cleanly |
| 2026-05-06 | Grok | Asked for a review of the milestone manifest structure — whether the source probe format matched what an automated grader would expect | Added `"charter_locked": true` field that was missing; verified all five probe file paths existed in `data/raw/` before committing |
| 2026-05-07 | Claude | Drafted `CHARTER.md` V1 through V3 — research question (initially asymmetric shocks framing), stakeholder (initially RBI), falsifiable hypothesis, data sources, reproducibility checklist | Changed stakeholder from RBI to corporate treasury desk after instructor feedback; revised research question to GARCH-vs-baseline framing to match what the code actually tests; verified updated question matched README exactly |
| 2026-05-07 | ChatGPT | Asked how a corporate treasury desk frames currency volatility risk in practice — wanted the stakeholder framing grounded rather than academic | Rewrote the action-rule language ourselves to match actual model output scale (annualised vol, not daily); added "not financial advice" disclaimer that was missing from the AI draft |
| 2026-05-09 | Claude | Drafted the 2-state Gaussian HMM cell using `hmmlearn`, including the regime-label assignment that sorts states by mean volatility to keep Low/High labels stable across seeds | Re-ran with three different random seeds to confirm stability; visually checked high-vol periods aligned with COVID (Mar 2020), 2022 Fed tightening, and 2024 global selloff; verified regime probabilities summed to 1.0 per row |
| 2026-05-09 | Claude | Built the policy event study cell — 19 macro events with dates, `event_window` function for ±5-day forecast errors, surprise vs expected classification, bar chart | Verified all 19 event dates against public records; confirmed surprise/expected classification matched economic understanding — Trump inauguration marked "expected", COVID crash marked "surprise" |
| 2026-05-10 | Grok | Asked for a review of the per-regime performance table — whether the BiLSTM vs GARCH comparison in high-vol periods told a coherent economic story | Rewrote the economic interpretation paragraph — the AI draft used causal language which we softened to predictive language |
| 2026-05-10 | DeepSeek | Asked how to frame a volatility model output as an actionable signal for a non-technical treasury audience — Normal/Elevated/Stress tier structure | Kept the three-tier structure and 5%/8% thresholds; verified the current GARCH forecast level correctly triggered the right tier; rewrote all action-rule copy in treasury language |
| 2026-05-11 | Claude | Generated the Streamlit dashboard (Cell 71): forecast chart with model selector, regime donut chart, per-regime table, hedging signal box, daily move and paise range | Fixed a `KeyError` when Naive model was deselected — Claude assumed all four models always present; added `.get()` guard; toned down signal-box language that read like a real trading system |
| 2026-05-11 | ChatGPT | Asked for a review of the SHAP feature importance chart — whether colour coding by feature category was readable and axis labels were correct | Fixed the x-axis label from "SHAP value" to "Mean |SHAP value|"; removed a caption line that implied SHAP values reflect causal importance |
| 2026-05-12 | Claude | Drafted the final project summary cell (Section 8) — metrics table, key findings, limitations list, treasury action rule recap, `next_day_forecast.json` save | Removed a line stating BiLSTM "achieves the 5% RMSE improvement target" — it does not; kept null result in limitations honestly; confirmed JSON saved correctly with all required fields |
| 2026-05-12 | Grok | Asked whether the isotonic-calibrated BiLSTM directional accuracy of 46.98% vs GARCH 2.56% was plausible or a sign of data leakage | Confirmed the gap is plausible — GARCH conditional variance forecasts are not designed to predict direction; verified directional accuracy was computed on strictly out-of-sample test rows |
| 2026-05-13 | Claude | Built the GitHub Pages dashboard (`dashboard.html`) — Chart.js, embedded real forecast arrays from notebook, time range buttons, absolute error chart, next-day price prediction, treasury signal text, live JSON fetch from GitHub Actions output | Verified all embedded arrays matched notebook output by cross-checking 10 random rows; confirmed risk state logic matched charter decision rule; fixed dashboard that initially showed sample data instead of real arrays |
| 2026-05-13 | Claude | Set up GitHub Actions workflow for automated daily forecast updates — runs `uv run main.py` every weekday at 5:30 PM IST, commits updated `outputs/next_day_forecast.json` | Debugged exit code 128 (missing write permissions) and exit code 1 (missing `arch` dependency); added `permissions: contents: write` and `arch` to `pyproject.toml`; verified Action ran successfully |
| 2026-05-13 | Claude | Drafted `CHARTER.md` V4 — updated stakeholder, research question, hypothesis, scope limits, team roles with detailed workstreams and ~50hr estimates | Verified every change against instructor PR feedback before committing; confirmed research question matches README and report.md exactly |
| 2026-05-13 | ChatGPT | Asked for a final review of `report.md` — whether Section 8 (null result) was framed honestly enough for the course rubric | Added the Meese-Rogoff citation; removed a sentence that could be read as minimising the null result rather than explaining it |

---

## Summary

**Where AI accelerated work most:**
- Data pipeline boilerplate — ingestion, FRED alignment, caching. We caught one data leakage error (scaler fit on full dataset) and one unit mismatch (GARCH annualisation) that would have invalidated results.
- Model architecture drafts — BiLSTM, GARCH loop, HMM. Each required meaningful correction before use.
- Repo and charter structure — JSON schemas, README, charter sections. We verified every field against the course rubric.
- Dashboard — Chart.js layout and JS logic. We replaced sample data with real arrays and corrected signal-box language.

**What the team checked manually every time:**
- All RMSE, MAE, MAPE, and directional accuracy values computed and cross-verified in the notebook before reporting
- Data leakage audit — every feature confirmed lagged by at least one day
- Regime label stability across random seeds
- Event study dates verified against public records
- Null result reported honestly — no AI framing was accepted that overstated the GARCH result
