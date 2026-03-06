# Quickstart: case_generator.py

**Step 4 of 7** — Bulk-create 120 test cases from CSV and link each to its Jira story.

---

## Prerequisites

All three upstream steps must be complete before running this script:

| Step | Script | State written |
|------|--------|---------------|
| 1 | `scripts/workspace_init.py` | `project_code`, `suite_ids`, `custom_fields` (with `options`) |
| 2 | `jira_requirements.py` | `jira_state.json` with `stories` and `epics` |
| 3 | `suite_generator.py` | `suite_ids` map with all 30 entries |

**Critical dependency**: `scripts/workspace_init.py` MUST write `custom_fields.{name}.options` into `state/workspace_state.json`. If this key is missing, `case_generator.py` will exit with a descriptive error. See `research.md F-01`.

---

## Environment

```bash
# Required
export QASE_API_TOKEN="your-qase-api-token"

# Already configured in config/workspace.yaml:
#   seed.cases_csv: "assets/seed-data/QD-2026-02-18.csv"
#   cf_column_map: {cf_6: Component, ...}
#   suite_domain_map: {"01 Authentication": auth, ...}
```

---

## Run

```bash
# Dry-run first — inspect plan with no API calls
.venv/bin/python scripts/case_generator.py --dry-run

# Live run
.venv/bin/python scripts/case_generator.py

# Override CSV path
.venv/bin/python scripts/case_generator.py --csv path/to/other.csv

# Override config path
.venv/bin/python scripts/case_generator.py --config config/workspace.yaml
```

**Never** use `python` or `python3` directly — always use `.venv/bin/python`.

---

## Expected Output

### Dry-run
```
[DRY-RUN] Case distribution plan (120 cases across 30 suites):

  [  1] csv_id=1   suite="Registration"          jira="AF-7 (auth-1)"  title="Auth: Negative: Failed Registration..."
  [  2] csv_id=2   suite="Login & Sessions"       jira="AF-8 (auth-2)"  title="Auth: Positive: Successful Login..."
  ...

[DRY-RUN] Summary: 120 cases planned, 23 suites affected, 38 unique Jira stories referenced.
[DRY-RUN] No API calls made.
```

### Live run
```
[GET]  Fetched 0 existing case(s) from project HY.
[GET]  Built runtime enum map (7 system fields).
Batch 1/4: 30 created
Batch 2/4: 30 created
Batch 3/4: 30 created
Batch 4/4: 30 created
Cases complete: 120 created, 0 reused (total 120)
[GET]  Fetched link status for 120 cases (0 already linked).
Links batch 1/4: 30 linked, 0 skipped
Links batch 2/4: 30 linked, 0 skipped
Links batch 3/4: 30 linked, 0 skipped
Links batch 4/4: 30 linked, 0 skipped
```

### Re-run (all exist)
```
[GET]  Fetched 120 existing case(s) from project HY.
REUSE case 1: 'Auth: Negative: Failed Registration...' → qase_id=201
... (120 REUSE lines)
Cases complete: 0 created, 120 reused (total 120)
[GET]  Fetched link status for 120 cases (120 already linked).
Links batch 1/4: 0 linked, 30 skipped
...
```

---

## Verify

After a successful run:

1. **Qase**: Navigate to the project → each of the 30 suites should contain the expected number of cases, all with 5 custom fields populated.
2. **State file**: `cat state/workspace_state.json | python3 -c "import json,sys; s=json.load(sys.stdin); print(len(s.get('case_ids',{})), 'cases in state')"` → should print `120`.
3. **Jira links**: Spot-check a few cases in Qase — each should show one Jira issue link.

---

## Troubleshooting

| Error | Cause | Fix |
|-------|-------|-----|
| `Error: custom_fields.Component.options missing` | `scripts/workspace_init.py` didn't write option IDs | Re-run `scripts/workspace_init.py` (spec 001 version) |
| `Error: suite_id '9' not in state suite_ids map` | `suite_generator.py` didn't complete | Run `suite_generator.py` first |
| `Error: domain slug 'checkout' not in jira_state` | `jira_requirements.py` didn't create checkout epic | Re-run `jira_requirements.py` |
| `Error: Check QASE_API_TOKEN permissions (HTTP 401)` | Invalid or missing token | Set `QASE_API_TOKEN` env var |
| `Error: project_code 'HY' not found in Qase (HTTP 404)` | Project was deleted | Re-run `scripts/workspace_init.py` |
