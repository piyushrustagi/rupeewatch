# Milestone Feedback

Project: P27 - RupeeWatch: INR/USD volatility forecasting
Repo: `piyushrustagi/rupeewatch`
Milestone score locked: 9/20
Raw score before policy caps: 9/20
Band: `not_milestone_ready`
Reviewed at: 2026-05-09T02:03:14

This is the locked milestone evaluation for the May 6 milestone. The score is based on the latest repository snapshot available to the instructor review workflow when this feedback was generated.

## Graduating-Student Timeline

This team includes graduating student(s): Arushi Sareen (ma2024), Piyush Rustagi (ma2024), Saburi Kapoor (ma2024).
To help us meet the May 15 grade-publishing deadline from OAA, please aim to submit the final version by May 13 if possible, and no later than May 14, 2026 at 11:59 PM IST.

## Rubric Breakdown

- Charter lock: 1/4. the charter is not recorded as approved; charter file exists and is not obviously template; the milestone manifest does not confirm charter lock
- Source access proof: 2/4. some data/probe evidence was found, but the manifest source list is incomplete
- Baseline before sophistication: 1/4. baseline exists but metric/value shape is incomplete
- Reproducible dry run: 4/4. `uv run main.py` succeeds and writes the required milestone outputs
- Metric schema readiness: 1/4. primary metric exists but is not yet machine-checkable

## What To Fix Next

- Make the charter unambiguous: final question, dataset, primary metric, baseline, scope limits, and team roles should all be visible in `CHARTER.md`.
- Make source access easy to verify: include a probe file or script, list the source in `outputs/milestone_manifest.json`, and commit a small permitted fallback if the full source is too large/private.
- Keep a simple baseline first. `outputs/baseline_metric.json` should contain a real metric name and value, not template text.
- `outputs/primary_metric.json` should be machine-checkable: include `metric_name`, `value`, `threshold`, and `passed`.

## Final Phase Guidance

- Second priority: make the final metric parseable in `outputs/primary_metric.json` with a value, threshold, and pass/fail status.
- Make the data path boring and reliable: source proof, fallback/sample data, and README instructions should agree.
- This needs urgent repair. A simple, reproducible, well-explained project will score better than an ambitious project that cannot be run or verified.
- For the final submission, keep the repo as the source of truth: `README.md`, `CHARTER.md`, `main.py`, `outputs/`, `report.md`, and `AI_USAGE_LOG.md` should tell one consistent story.

Please treat this feedback as a way to make the final week calmer, not as a ceiling on the final project. A clear, reproducible, honestly interpreted final submission can still be strong.
