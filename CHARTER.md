# Project Charter — RupeeWatch

> **Course:** Computational Thinking and Programming using AI (ECO-6810)
> **Project:** INR/USD Volatility Forecasting Pipeline
> **Team:** Arushi Sareen · Piyush Rustagi · Saburi Kapoor

---

## Project Objective

The objective of RupeeWatch is to build a reproducible computational pipeline for forecasting INR/USD exchange-rate volatility using econometric and machine learning techniques.

The project combines macroeconomic data engineering, econometric benchmarking, regression-based forecasting, and AI-enabled sequence models, with emphasis on reproducibility, modular computational workflows, economic interpretability, and iterative model development.

---

## Core Research Question

> Can macroeconomic indicators and machine learning methods improve INR/USD volatility forecasting relative to traditional benchmark models?

---

## Scope of Work

### In Scope

- INR/USD exchange-rate data
- Macroeconomic data ingestion using FRED
- Feature engineering and volatility construction
- Regression forecasting baseline
- GARCH benchmark model
- Bidirectional LSTM forecasting model
- Forecast evaluation using RMSE and MAE
- Reproducible repository and workflow pipeline
- Documentation and automated outputs

### Planned Extensions

- Hidden Markov Model regime detection
- Policy-event analysis
- Dashboard and visualization layer
- SHAP interpretability analysis

### Out of Scope

- High-frequency trading systems
- Portfolio optimization
- Live deployment infrastructure
- Transaction-cost modeling


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
GARCH Benchmark
      |
BiLSTM Forecasting
      |
Evaluation & Comparison
      |
Visualization & Interpretation
```

---

## Milestone Plan

| Stage                | Deliverable                          | Status      |
| -------------------- | ------------------------------------ | ----------- |
| Repository setup     | GitHub repo + reproducible structure | Completed   |
| Data pipeline        | INR/USD + macro data ingestion       | Completed   |
| Feature engineering  | Returns + rolling volatility         | Completed   |
| Regression baseline  | Linear regression forecasting        | In Progress |
| GARCH benchmark      | Volatility benchmark model           | Planned     |
| BiLSTM model         | AI forecasting model                 | Planned     |
| Evaluation framework | RMSE / MAE comparison                | Planned     |
| Dashboard layer      | Visualization and presentation       | Planned     |

---

## Success Criteria

The project will be considered successful if it achieves:

1. A fully runnable and reproducible repository
2. Automated data ingestion and preprocessing
3. Successful baseline forecasting pipeline
4. Econometric benchmark implementation
5. Comparative evaluation between benchmark and ML models
6. Clear economic interpretation of results
7. Proper documentation and workflow transparency

---

## Team Workflow

### Communication

- Primary coordination through WhatsApp
- Weekly progress reviews
- Shared GitHub workflow

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
