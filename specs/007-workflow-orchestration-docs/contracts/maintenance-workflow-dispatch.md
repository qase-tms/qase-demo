# Contract: Maintenance Workflow Dispatch

**Endpoint**: `schedule` + `workflow_dispatch` (GitHub Actions)  
**Used in**: Parent orchestration workflow (`mode=maintenance`)

---

## Trigger Contract

- Scheduled cadence: weekdays (`Mon-Fri`) in UTC.
- Manual dispatch permitted for validation and override scenarios.

## Input Contract (manual)

| Input | Type | Required | Default | Validation |
|---|---|---|---|---|
| `mode` | string | yes | `maintenance` | must be `maintenance` |
| `seed` | number | no | config value | integer if provided |
| `min_runs` | number | no | config value | integer in `1..6` |
| `max_runs` | number | no | config value | integer in `1..6`, `>= min_runs` |
| `dry_run` | boolean | no | `false` | boolean |

---

## Execution Contract

Execution target:

```bash
.venv/bin/python scripts/maintenance.py [overrides]
```

Behavior:
- must honor overlap safeguards
- must report skipped reasons for weekend/overlap cases
- must preserve seeded suite/case structure
- must commit state updates to `automation/state` branch only (non-dry-run)
- must enforce 90-day retention pruning for optional `state/history/` snapshots
