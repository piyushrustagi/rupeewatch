from __future__ import annotations

def build_baseline_metric() -> dict:
    return {
        "metric_name": "RMSE",
        "model": "linear_regression_baseline",
        "value": 0.003797,
        "mae": 0.001802,
        "unit": "annualised_volatility",
        "dataset": "usdinr_test_split",
        "notes": "Linear regression on 3 lagged features. Test set: 2024-05-10 to 2026-05-13.",
        "is_template": False,
    }

def build_primary_metric() -> dict:
    return {
        "metric_name": "RMSE",
        "model": "garch_1_1",
        "value": 0.015329,
        "threshold": 0.003607,
        "passed": False,
        "unit": "annualised_volatility",
        "notes": "GARCH(1,1) rolling 1-step-ahead forecast. Does not beat baseline. Null result reported honestly.",
        "is_template": False,
    }

def build_milestone_manifest() -> dict:
    return {
        "charter_locked": True,
        "baseline_ready": True,
        "primary_metric_schema_ready": True,
        "run_command": "uv run main.py",
        "sources": [
            {"name": "yfinance:USDINR=X", "status": "ok", "probe_artifact": "data/raw/usdinr.csv"},
            {"name": "FRED:VIXCLS", "status": "ok", "probe_artifact": "data/raw/probe_vix.csv"},
            {"name": "FRED:DTWEXBGS", "status": "ok", "probe_artifact": "data/raw/probe_dxy.csv"},
            {"name": "FRED:DCOILWTICO", "status": "ok", "probe_artifact": "data/raw/probe_oil.csv"},
            {"name": "FRED:FEDFUNDS", "status": "ok", "probe_artifact": "data/raw/probe_ffr.csv"},
        ],
        "template_warning": None,
    }
