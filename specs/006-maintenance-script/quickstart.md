# Quickstart: maintenance.py

Step 6 of 6 - run weekday operational maintenance to keep workspace activity fresh.

---

## Prerequisites

Run setup and seeding first:

1. `scripts/workspace_init.py`
2. `jira_requirements.py create`
3. `suite_generator.py`
4. `case_generator.py`
5. `run_simulator.py` (initial baseline activity)

Required files:

- `config/workspace.yaml`
- `state/workspace_state.json`
- `state/run_simulator_state.json` (optional but recommended for attachment pool reuse)
- `assets/seed-data/QD-2026-02-18.csv`

Required environment variables:

- `QASE_API_TOKEN`
- `JIRA_BASE_URL`
- `JIRA_EMAIL`
- `JIRA_API_TOKEN`
- `JIRA_PROJECT_KEY`

---

## Run

```bash
# Dry-run: validate weekday/scope/volume planning only
.venv/bin/python scripts/maintenance.py --dry-run

# Live maintenance cycle
.venv/bin/python scripts/maintenance.py

# Optional overrides
.venv/bin/python scripts/maintenance.py --seed 42 --min-runs 1 --max-runs 6
```

---

## Expected Outcome

- On weekdays (UTC), one maintenance cycle runs.
- Cycle selects `1-6` runs with low-biased distribution.
- Runs generate realistic result activity using existing seeded cases only.
- Most results show attachment evidence (`>=90%` target).
- If one run has Jira/link failure, that run is marked incomplete and remaining runs continue.
- Cycle summary reports requested/completed/incomplete counts with reasons.
- No new suites/cases are created.

### Observed Sample Distribution (seed sweep)

Example dry-run sample across seeds `1..20`:

- Run count `1`: 7 cycles
- Run count `2`: 6 cycles
- Run count `3`: 3 cycles
- Run count `4`: 1 cycle
- Run count `5`: 1 cycle
- Run count `6`: 2 cycles

This confirms a low-biased selection profile in the configured `1..6` range.

---

## Verification Checklist

1. Confirm cycle is skipped on weekends (UTC) with explicit skip reason.
2. Confirm cycle is skipped when another cycle is currently active.
3. Confirm weekday live run creates between 1 and 6 runs.
4. Confirm created runs include result submissions and Jira external issue links when successful.
5. Confirm incomplete runs (if any) include explicit failure reason.
6. Confirm suite and case counts remain unchanged before/after maintenance.
7. Spot-check results to verify attachment coverage is high.
8. Confirm cycle metadata reports rolling 14-day success rate and weekday/UTC compliance counters.
9. Confirm cycle metadata reports per-cycle duration and rolling average duration (target under 10 minutes).

---

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---|---|---|
| `workspace_state.json missing required non-empty case_ids map` | Seeding not complete | Re-run `case_generator.py` |
| `Missing required env var: JIRA_PROJECT_KEY` | Jira key not configured in environment/secrets | Export `JIRA_PROJECT_KEY` and rerun |
| Cycle skipped unexpectedly | Weekend UTC or active overlap lock | Check UTC day and active cycle metadata |
| Low attachment coverage | Attachment hash pool unavailable | Rebuild attachment pool via simulator run or upload flow |
| Missing rolling metrics in cycle state | Older state schema without maintenance metrics | Run one successful maintenance cycle to initialize rolling metrics fields |
| Average duration over 10 minutes | API retries or high run/result volume overrides | Review retry logs, reduce override range, and verify API health |
