# RupeeWatch: INR/USD Exchange Rate Volatility Forecasting

### A Reproducible Computational Economics Pipeline using Econometric and AI Models

> **Course:** Computational Thinking and Programming using AI (ECO-6810)
> **Team:** Arushi Sareen · Piyush Rustagi · Saburi Kapoor
> **Project Type:** Computational Macroeconomics and AI Forecasting Pipeline

---

## Project Overview

The Indian Rupee (INR) is one of the most actively traded emerging-market currencies and is highly sensitive to global risk sentiment, crude oil shocks, US dollar strength, monetary policy changes, and macroeconomic uncertainty.

Traditional econometric volatility models capture volatility clustering well but struggle during structural breaks and regime changes. Modern machine learning approaches can capture non-linear temporal patterns but often lack strong benchmark comparison and economic interpretation.

**RupeeWatch** is a reproducible computational economics project that builds a forecasting workflow for INR/USD volatility using econometric benchmarks, regression-based forecasting, macroeconomic feature engineering, and machine learning models.

The project is designed as an iterative AI-enabled forecasting pipeline for the course:

> **Computational Thinking and Programming using AI (ECO-6810)**

---

## Research Question

> Does incorporating macroeconomic indicators and volatility features improve INR/USD volatility forecasting relative to standard benchmark approaches?

Secondary questions include:

- How do volatility regimes affect forecasting performance?
- Can machine learning models improve predictive accuracy over econometric benchmarks?
- Which macroeconomic variables appear most relevant during periods of stress?

---

## Core Evaluation Framework

### Outcome Variable
1-day-ahead INR/USD realized volatility measured using daily percentage returns.

### Forecast Horizon
1 trading day ahead.

### Baseline Model
Linear regression using:
- lagged returns
- rolling 5-day volatility

### Primary Metric
Held-out RMSE on the test dataset.

### Success Threshold
The project target is to achieve at least 5% lower RMSE than the regression baseline using an extended forecasting model.

The current project focuses on building a reproducible forecasting pipeline for 1-day-ahead INR/USD realized volatility.

### Core Workflow

1. INR/USD exchange-rate data ingestion
2. Data preprocessing and feature engineering
3. Lagged-return and rolling-volatility feature construction
4. Linear regression forecasting baseline
5. Held-out RMSE evaluation
6. Automated JSON metric export

### Optional Extensions

The following components are planned as extensions after the core evaluation pipeline is stable:

- GARCH volatility benchmarks
- Bidirectional LSTM forecasting
- Hidden Markov Model regime detection
- Dashboard and visualization layer
- Policy-event analysis

---

## Data Sources

| Feature               | Source                     | Frequency |
| --------------------- | -------------------------- | --------- |
| INR/USD Exchange Rate | Yahoo Finance (`USDINR=X`) | Daily     |
| VIX Index             | FRED                       | Daily     |
| WTI Crude Oil         | FRED                       | Daily     |
| US Dollar Index (DXY) | FRED                       | Daily     |
| India Interest Rate   | FRED                       | Monthly   |
| US Federal Funds Rate | FRED                       | Daily     |

All datasets are publicly available.

## Data Source Probes

### Successfully Tested
- INR/USD exchange-rate pipeline using Yahoo Finance (`USDINR=X`)
- Local cached dataset generated at `data/raw/usdinr.csv`

### Planned Integrations
- VIX (FRED)
- DXY (FRED)
- WTI Crude Oil (FRED)
- Federal Funds Rate (FRED)

---

## Repository Structure

```text
rupeewatch/
│
├── data/
│   └── raw/
│       └── usdinr.csv
│
├── outputs/
│   ├── baseline_metric.json
│   ├── primary_metric.json
│   └── milestone_manifest.json
│
├── src/
│   └── download_data.py
│
├── main.py
├── README.md
├── CHARTER.md
├── pyproject.toml
├── uv.lock
└── .gitignore
```

---

## Implementation Status

### Completed

- Reproducible GitHub repository setup
- Executable pipeline using `uv`
- INR/USD data ingestion pipeline
- Local cached dataset generation
- Automated output generation
- Feature engineering pipeline
- Rolling volatility computation
- Regression baseline workflow
- JSON metric export pipeline

### In Progress

- Regression baseline refinement
- RMSE evaluation pipeline
- Macroeconomic feature integration

### Planned Extensions

- GARCH volatility benchmark
- Bidirectional LSTM forecasting model
- HMM volatility regime detection
- RBI policy-event analysis
- Streamlit dashboard
- Model comparison framework

---

## Tech Stack

| Category         | Libraries                   |
| ---------------- | --------------------------- |
| Data Processing  | pandas, numpy               |
| Data APIs        | yfinance, fredapi           |
| Econometrics     | arch, statsmodels           |
| Machine Learning | scikit-learn, tensorflow    |
| Regime Detection | hmmlearn                    |
| Visualization    | matplotlib, seaborn, plotly |
| Workflow         | uv, GitHub                  |

---

## Setup

Install dependencies:

```bash
uv sync
```

---

## Running the Project

Run from repository root:

```bash
uv run main.py
```

---

## Expected Outputs

Running the pipeline generates:

```text
outputs/
├── baseline_metric.json
├── primary_metric.json
└── milestone_manifest.json
```

---

## Current Baseline Workflow

The current baseline workflow:

1. Loads INR/USD exchange-rate data
2. Computes daily returns
3. Generates lagged-return features
4. Computes rolling volatility
5. Runs linear regression forecasting
6. Computes RMSE
7. Exports metrics to JSON files

---

## Current Limitations

- The current pipeline relies primarily on lagged-return and rolling-volatility features.
- Macroeconomic variables are not yet fully integrated into the forecasting workflow.
- The current implementation focuses on establishing a reproducible baseline evaluation pipeline before advanced modeling extensions.

---

## Planned Extensions

Future project extensions may include:

- Regime-aware forecasting using Hidden Markov Models
- SHAP-based feature interpretability
- Real-time data updates
- Multi-currency forecasting framework
- Temporal Fusion Transformer (TFT) experimentation

---

## Academic Context

This project is being developed as part of **Computational Thinking and Programming using AI (ECO-6810)**, with emphasis on computational workflows, reproducibility, economic data pipelines, econometric benchmarking, and AI-assisted forecasting systems.

---

