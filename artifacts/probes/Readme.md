# Source Probes — RupeeWatch

Each file below provides a minimal proof that the data source is real, reachable, and successfully fetched.  
Full datasets are retrieved programmatically in `main.py`.

| Probe File | Source | Status |
|------------|--------|--------|
| `probe_yfinance.md` | Yahoo Finance — USDINR=X | OK |
| `probe_vix.md` | FRED — VIXCLS (VIX Index) | OK |
| `probe_dxy.md` | FRED — DTWEXBGS (US Dollar Index) | OK |
| `probe_oil.md` | FRED — DCOILWTICO (WTI Crude Oil) | OK |
| `probe_ffr.md` | FRED — DFF (Federal Funds Rate) | OK |

All five sources were successfully validated.  
Machine-readable probe CSVs are also committed in `data/raw/` as reproducibility fallbacks.

---

# Source Probe Guidelines

For the milestone, each primary data source should include a small proof that the source works and is accessible.

Examples include:

- one row from an API response
- one row from a CSV or Excel file
- one screenshot of a successful authenticated fetch
- one small JSON or Markdown snippet showing a successful fetch

These are not full analyses; they are lightweight reproducibility checks confirming that the source is valid and reachable.
Running `main.py` refreshes the underlying datasets and appends newly available observations automatically.
