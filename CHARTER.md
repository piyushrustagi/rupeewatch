# Project Charter — RupeeWatch

> **Course:** Computational Thinking and Programming using AI (ECO-6810)
> **Project:** INR/USD Volatility Forecasting Pipeline
> **Team:** Arushi Sareen · Piyush Rustagi · Saburi Kapoor

---

## Project Objective

The objective of RupeeWatch is to build a reproducible computational pipeline for forecasting INR/USD exchange-rate volatility using econometric and machine learning techniques.

The project combines macroeconomic data engineering, econometric benchmarking, regression-based forecasting, and AI-enabled sequence models, with emphasis on reproducibility, modular computational workflows, economic interpretability, and iterative model development.

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

### Primary Evaluation Metric
Held-out RMSE on the test dataset.

### Success Threshold
The project target is to achieve at least 5% lower RMSE than the regression baseline using an extended forecasting model.

---

## Core Research Question

> Can macroeconomic indicators and machine learning methods improve INR/USD volatility forecasting relative to traditional benchmark models?

## Core Deliverable

The core deliverable is a reproducible forecasting pipeline for 1-day-ahead INR/USD realized volatility prediction.

The pipeline must:
- execute successfully using `uv run main.py`
- generate automated JSON metric outputs
- compute held-out RMSE reproducibly
- support baseline forecasting evaluation

---

## Scope of Work

### In Scope

- INR/USD exchange-rate data pipeline
- Data preprocessing and feature engineering
- Lagged-return and rolling-volatility construction
- Regression forecasting baseline
- RMSE evaluation pipeline
- Reproducible repository workflow
- Automated metric export
- Documentation and reproducibility support

### Planned Extensions

- GARCH volatility benchmark
- Bidirectional LSTM forecasting model
- Hidden Markov Model regime detection
- Policy-event analysis
- Dashboard and visualization layer
- SHAP interpretability analysis

### Out of Scope

- High-frequency trading systems
- Portfolio optimization
- Live deployment infrastructure
- Transaction-cost modeling

## Data Source Probes

### Successfully Tested
- INR/USD exchange-rate pipeline using Yahoo Finance (`USDINR=X`)
- Local cached dataset stored at `data/raw/usdinr.csv`

### Planned Integrations
- VIX (FRED)
- DXY (FRED)
- WTI Crude Oil (FRED)
- Federal Funds Rate (FRED)

---

## Workflow Architecture

```text
Data Collection
      |
Data Cleaning
      |
Feature Engineering
      |
Regression Baseline
      |
RMSE Evaluation
      |
Automated Metric Export
      |
Optional Model Extensions
```

---

## Milestone Plan

| Stage | Deliverable | Status |
|---|---|---|
| Repository setup | GitHub repo + reproducible structure | Completed |
| Data pipeline | INR/USD data ingestion | Completed |
| Feature engineering | Returns + rolling volatility | Completed |
| Regression baseline | Linear regression forecasting | Completed |
| Evaluation contract | RMSE baseline + threshold definition | Completed |
| Macroeconomic integration | Additional feature ingestion | In Progress |
| Optional extensions | GARCH / BiLSTM / dashboard | Planned |

---

## Success Criteria

The project will aim that:

1. The repository is fully reproducible and executable.
2. The regression baseline pipeline runs successfully.
3. Automated metric outputs are generated reproducibly.
4. Held-out RMSE is computed on the test dataset.
5. An extended forecasting model achieves the predefined RMSE improvement target relative to the regression baseline.

---

### Git Workflow

- Use feature branches for development
- Merge reviewed code into `main`
- Maintain reproducible commit history
- Push working code frequently

---

## Repository Workflow

The repository is structured as a modular computational pipeline rather than a single notebook-only project.

Execution workflow:

```bash
uv sync
uv run main.py
```

Outputs are automatically generated in:

```text
outputs/
```

---

## Academic Motivation

This project integrates macroeconomics, econometrics, machine learning, and computational thinking. The goal is not only forecasting accuracy, but also building a structured and reproducible AI-assisted economics workflow.

---

## Team Agreement

All team members agree to contribute toward reproducible workflows, clear documentation, collaborative development, and transparent implementation progress.

---
