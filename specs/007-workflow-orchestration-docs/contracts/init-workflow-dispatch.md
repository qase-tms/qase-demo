# Contract: Init Workflow Dispatch

**Endpoint**: `workflow_dispatch` (GitHub Actions manual trigger)  
**Used in**: Parent orchestration workflow (`mode=init`)

---

## Input Contract

| Input | Type | Required | Default | Validation |
|---|---|---|---|---|
| `mode` | string | yes | `init` | must be `init` |
| `seed` | number | no | config value | integer if provided |
| `run_count` | number | no | config value | positive integer if provided |
| `dry_run` | boolean | no | `false` | boolean |

---

## Execution Contract

The workflow must execute this strict order and fail fast on first failure:

1. `scripts/workspace_init.py`
2. `scripts/suite_generator.py`
3. `scripts/jira_requirements.py create`
4. `scripts/case_generator.py`
5. `scripts/run_simulator.py`

If any step fails:
- downstream steps are skipped
- workflow status is `failed`
- logs include remediation guidance

Post-run behavior (non-dry-run):
- state snapshots under `state/*.json` are eligible for writeback to `automation/state` branch only
