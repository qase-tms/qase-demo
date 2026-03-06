# Quickstart: run_simulator.py

Step 5 of 7 — create realistic present-time runs, results, Jira task links, and run completion events.

---

## Prerequisites

Run Steps 1-4 first:

1. `scripts/workspace_init.py`
2. `jira_requirements.py`
3. `suite_generator.py`
4. `case_generator.py`

Required files:

- `config/workspace.yaml`
- `state/workspace_state.json` (must contain `project_code`, `case_ids`, `environments`, `milestones`)
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
# Dry-run: plan generation only, no external writes
.venv/bin/python scripts/run_simulator.py --dry-run

# Live simulation
.venv/bin/python scripts/run_simulator.py

# Optional overrides
.venv/bin/python scripts/run_simulator.py --config config/workspace.yaml --state state/workspace_state.json --seed 42
```

---

## Expected Outcome

- Configured run volume created (default 20 if `simulation.run_count` not set)
- Every run includes:
  - realistic title/description and contextual tags
  - result set referencing only existing case IDs (80-120 results per run)
  - one newly created Jira Task linked to the run
  - completion event after results and link (or intentionally left incomplete if Jira link fails)
- Timeline shows:
  - fast/medium/slow duration spread
  - concurrent execution overlap
  - visible idle gaps
- Outcome quality:
  - at least 30% fully green runs
  - weak suite has lower pass rate
  - manual results >=20%
  - defect flag on approximately half of failed results only

---

## Verification Checklist

1. In Qase Runs view, confirm new runs are present with realistic names and mixed themes.
2. Open several runs and verify each has an external Jira issue link.
3. Confirm any Jira-link failures were logged and those runs remain incomplete while later runs still proceed.
4. In Timeline view, confirm overlap and gap patterns are visible (not flat serial bars).
5. Spot-check failed automated results for stack trace presence.
6. Spot-check failed manual results for comment-based diagnostics.
7. Confirm step results are visible with non-empty action text.

---

## Troubleshooting

| Symptom | Likely Cause | Resolution |
|---|---|---|
| `Missing case_ids in state` | Step 4 has not populated case mapping | Re-run `case_generator.py` |
| `No environment or milestone IDs available` | State incomplete or malformed | Re-run Step 1 and verify state keys |
| Run created but not linked to Jira | Jira issue creation/link API failure | Validate Jira env vars and project key |
| Timeline looks too uniform | Seed logic not applying worker scheduling/gaps | Run with `--dry-run` and inspect scheduling diagnostics |
| Too many defects | Incorrect failure/defect weighting | Verify failed-only defect rule and 50% failed subset targeting |

