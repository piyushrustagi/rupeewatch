import pandas as pd
import yfinance as yf
from pathlib import Path

# Create folders
DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)

# Download INR/USD data
ticker = "USDINR=X"

df = yf.download(ticker, start="2013-01-01")

# Save locally
df.to_csv(DATA_DIR / "usdinr.csv")

print("USDINR data downloaded successfully")