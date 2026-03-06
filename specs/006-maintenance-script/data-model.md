# Data Model: Maintenance Script Daily Activity Feed

**Branch**: `006-maintenance-script` | **Date**: 2026-02-27

---

## Input Sources

### `state/workspace_state.json`

| Key | Type | Purpose |
|---|---|---|
| `project_code` | string | Qase project identifier for API paths |
| `case_ids` | object `{csv_case_id: qase_case_id}` | Existing case pool for maintenance results |
| `environments` | object `{name: id}` | Environment selection for created runs |
| `milestones` | object `{title: id}` | Milestone selection for created runs |

### `config/workspace.yaml`

| Key | Type | Purpose |
|---|---|---|
| `seed.seed_value` | integer | Deterministic cycle generation |
| `maintenance.min_runs` | integer | Lower bound of daily runs (default `1`) |
| `maintenance.max_runs` | integer | Upper bound of daily runs (default `6`) |
| `maintenance.run_count_weights` | map/int list | Low-biased weighting for run-count selection |
| `maintenance.weekdays_only` | boolean | Enables weekday-only execution gate |
| `maintenance.schedule_timezone` | string | Canonical timezone for weekday evaluation (`UTC`) |

### `state/run_simulator_state.json`

| Key | Type | Purpose |
|---|---|---|
| `attachment_hashes` | list[string] | Reusable evidence hashes for high attachment coverage |

### `state/maintenance_state.json` (new)

| Key | Type | Purpose |
|---|---|---|
| `active_cycle` | object/null | Overlap guard marker while cycle is running |
| `last_cycle` | object | Latest completed/failed/skip metadata |
| `history` | list[object] | Optional recent execution summaries |

---

## Runtime Entities

### MaintenanceCycle

| Field | Type | Validation |
|---|---|---|
| `cycle_id` | string | unique per invocation |
| `started_at_utc` | datetime string | required |
| `ended_at_utc` | datetime string/null | required on completion |
| `status` | enum | `skipped`, `completed`, `completed_with_incomplete_runs`, `failed` |
| `skip_reason` | string/null | required when `status=skipped` |
| `run_count_requested` | int | range `1..6` by default |
| `run_count_completed` | int | `>=0` and `<= run_count_requested` |
| `run_count_incomplete` | int | `>=0` |
| `timezone_basis` | string | `UTC` |
| `weekday_allowed` | bool | true only on Mon-Fri UTC |

### MaintenanceRunPlan

| Field | Type | Validation |
|---|---|---|
| `run_index` | int | sequential in cycle |
| `run_type` | string | from allowed run type set |
| `title` | string | non-empty realistic title |
| `description` | string | non-empty contextual text |
| `environment_id` | int | exists in workspace state |
| `milestone_id` | int | exists in workspace state |
| `selected_case_ids` | list[int] | all values exist in seeded case pool |

### MaintenanceResult

| Field | Type | Validation |
|---|---|---|
| `case_id` | int | must map to existing seeded case |
| `status` | enum | `passed`, `failed`, `skipped` |
| `is_autotest` | bool | manual share must remain meaningful |
| `start_time` | int | epoch seconds |
| `time_ms` | int | positive |
| `defect` | bool | true only when `status=failed` |
| `comment` | string | non-empty |
| `attachments` | list[string] | present on >=90% of results |
| `steps` | list[ResultStep] | each step has non-empty action |

### ResultStep

| Field | Type | Validation |
|---|---|---|
| `position` | int | sequential, 1-based |
| `status` | enum | valid step status |
| `action` | string | required, non-empty |
| `comment` | string | optional |
| `attachments` | list[string] | optional |

### RunLifecycleLink

| Field | Type | Validation |
|---|---|---|
| `run_id` | int | created run identifier |
| `jira_issue_key` | string | required before run completion |
| `link_status` | enum | `linked`, `link_failed` |
| `incomplete_reason` | string/null | required when not linked |

---

## State Transitions

### MaintenanceCycle lifecycle

1. `initialized` -> `skipped` (weekday false OR overlap guard active)
2. `initialized` -> `running` (weekday true, no active cycle)
3. `running` -> `completed` (all planned runs complete)
4. `running` -> `completed_with_incomplete_runs` (at least one run incomplete)
5. `running` -> `failed` (fatal unrecoverable cycle error)

### Per-run lifecycle within cycle

1. `planned` -> `created`
2. `created` -> `results_submitted`
3. `results_submitted` -> `jira_created`
4. `jira_created` -> `linked`
5. `linked` -> `completed`

If step 3 or 4 fails, transition to `incomplete` and continue next planned run.

---

## Validation Rules Summary

- Run count must be selected within configured bounds (default `1..6`) using low-biased weighting.
- Cycle must not start on Saturday/Sunday in UTC.
- If `active_cycle` exists and is still in-progress, new cycle must be skipped.
- No suite/case create/update operations are allowed in maintenance flow.
- At least 90% of results must include attachments.
- All incomplete runs must include a reason in cycle summary output/state.
