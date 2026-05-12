import json
from pathlib import Path

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Create outputs directory
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

# Load data
df = pd.read_csv("data/raw/usdinr.csv")

# Keep adjusted close prices
# Keep close prices
df = df[["Close"]].copy()

# Convert to numeric
df["Close"] = pd.to_numeric(df["Close"], errors="coerce")

# Drop missing values
df = df.dropna()

# Create returns
df["return"] = df["Close"].pct_change()

# Lagged feature
df["lag_return"] = df["return"].shift(1)

# Drop missing values
df = df.dropna()

# Features and target
X = df[["lag_return"]]
y = df["return"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False
)

# Train regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
preds = model.predict(X_test)

# RMSE
rmse = mean_squared_error(y_test, preds) ** 0.5

# Baseline metric
baseline_metric = {
    "metric_name": "RMSE",
    "model": "linear_regression_baseline",
    "value": float(rmse),
    "dataset": "usdinr_test_split"
}

# Placeholder primary model
primary_metric = {
    "metric_name": "RMSE",
    "model": "bilstm_planned",
    "value": float(rmse),
    "threshold": round(float(rmse) * 0.95, 8),
    "passed": False,
    "note": "BiLSTM in progress; baseline RMSE reported until model is complete"
}

# Manifest
manifest = {
    "repo_runnable": True,
    "charter_locked": True,
    "data_pipeline_complete": True,
    "regression_baseline_complete": True,
    "primary_model_complete": False,
    "sources": ["yfinance:USDINR=X", "FRED:VIXCLS", "FRED:DCOILWTICO", "FRED:FEDFUNDS"]
}

# Save outputs
with open(OUTPUT_DIR / "baseline_metric.json", "w") as f:
    json.dump(baseline_metric, f, indent=4)

with open(OUTPUT_DIR / "primary_metric.json", "w") as f:
    json.dump(primary_metric, f, indent=4)

with open(OUTPUT_DIR / "milestone_manifest.json", "w") as f:
    json.dump(manifest, f, indent=4)

print("Regression baseline completed successfully")
print(f"RMSE: {rmse:.6f}")