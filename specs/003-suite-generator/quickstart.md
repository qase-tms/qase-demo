# Quickstart: suite_generator.py

**Script**: `scripts/suite_generator.py`
**Step**: 3 of 7 in the canonical execution sequence
**Prerequisite**: Steps 1 (`scripts/workspace_init.py`) and 2 (`jira_requirements.py`) must have completed successfully and `state/workspace_state.json` must contain a valid `project_code`.

---

## Prerequisites checklist

```bash
# 1. QASE_API_TOKEN must be set
echo $QASE_API_TOKEN    # should print your token (not empty)

# 2. workspace_state.json must exist and have project_code
cat state/workspace_state.json | python3 -c "import sys,json; d=json.load(sys.stdin); print('project_code:', d['project_code'])"

# 3. CSV must be present
ls assets/seed-data/QD-2026-02-18.csv    # or the path configured in config/workspace.yaml
```

---

## Common invocations

### Dry run (no API calls — inspect the creation plan)

```bash
python scripts/suite_generator.py --dry-run
```

Expected output:
```
[DRY-RUN] Pass 1 — top-level suites (7 total):
  [ 1] suite_id=2    title='01 Authentication'  parent=none
  [ 2] suite_id=1    title='02 Search & Browse'  parent=none
  ...

[DRY-RUN] Pass 2 — child suites (23 total):
  [ 8] suite_id=9    title='Registration'  parent='01 Authentication' (csv_id=2)
  ...

[DRY-RUN] Total: 30 suites. No API calls made.
```

### Normal run (uses CSV path from `config/workspace.yaml`)

```bash
python scripts/suite_generator.py
```

### Run with an explicit CSV path

```bash
python scripts/suite_generator.py --csv path/to/assets/seed-data/QD-2026-02-18.csv
```

### Run with an alternate config file

```bash
python scripts/suite_generator.py --config path/to/workspace.yaml
```

---

## Expected output (clean run)

```
[GET]  Fetched 0 existing suites from project AB.
[PASS1] suite_id=2  → CREATED  qase_id=101  title="01 Authentication"
[PASS1] suite_id=1  → CREATED  qase_id=102  title="02 Search & Browse"
[PASS1] suite_id=3  → CREATED  qase_id=103  title="03 Cart & Promotions"
[PASS1] suite_id=6  → CREATED  qase_id=104  title="04 Checkout"
[PASS1] suite_id=4  → CREATED  qase_id=105  title="05 Orders"
[PASS1] suite_id=7  → CREATED  qase_id=106  title="06 Returns & Refunds"
[PASS1] suite_id=5  → CREATED  qase_id=107  title="07 Admin"
[PASS2] suite_id=9  → CREATED  qase_id=108  title="Registration"
...
Suites complete: 30 created, 0 reused (total 30)
```

## Expected output (idempotent re-run)

```
[GET]  Fetched 30 existing suites from project AB.
[PASS1] suite_id=2  → REUSED   qase_id=101  title="01 Authentication"
...
Suites complete: 0 created, 30 reused (total 30)
```

---

## Verifying the result

```bash
# Check state file has 30 suite_ids
python3 -c "
import json
state = json.load(open('state/workspace_state.json'))
ids = state.get('suite_ids', {})
print(f'suite_ids count: {len(ids)}')
assert len(ids) == 30, 'Expected 30!'
print('All other keys preserved:', [k for k in state if k != 'suite_ids'])
"
```

---

## CLI reference

```
usage: suite_generator.py [-h] [--csv PATH] [--config PATH] [--dry-run]

Create Qase suite hierarchy from CSV.

options:
  -h, --help     show this help message and exit
  --csv PATH     Path to the CSV file. Overrides config/workspace.yaml
                 seed.cases_csv.
  --config PATH  Path to workspace config YAML (default:
                 config/workspace.yaml).
  --dry-run      Print the ordered creation plan without making any API calls
                 or modifying state/workspace_state.json.
```

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| `Missing env var QASE_API_TOKEN` | Token not exported | `export QASE_API_TOKEN=your_token` |
| `state/workspace_state.json missing or project_code absent` | Step 1 not run | Run `scripts/workspace_init.py` first |
| `CSV file not found: ...` | Wrong path or missing file | Pass `--csv <correct-path>` or update `seed.cases_csv` in `config/workspace.yaml` |
| `No suite rows found in CSV` | Filter issue | Verify CSV has rows with `suite_without_cases == "1"` |
| `Orphaned suite_parent_id: ...` | CSV data integrity issue | Check the CSV for rows referencing a suite_id that doesn't exist |
| `Qase API 401` | Token invalid or expired | Verify token at `https://app.qase.io/user/api` |
| `Qase API 403` | Token lacks access to project | Check project permissions for the token owner |
| `Qase API 404` | Wrong project code | Verify `project_code` in `state/workspace_state.json` matches a real project |
