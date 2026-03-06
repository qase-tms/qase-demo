# Data Model: Run Simulator Lifecycle

**Branch**: `005-run-simulator-lifecycle` | **Date**: 2026-02-27

---

## Input Sources

### `state/workspace_state.json`

Required keys consumed by Script 5:

| Key | Type | Purpose |
|---|---|---|
| `project_code` | string | Qase API project path parameter |
| `case_ids` | object `{csv_case_id: qase_case_id}` | Existing case IDs for result submissions |
| `suite_ids` | object `{csv_suite_id: qase_suite_id}` | Suite context mapping for weak-suite bias |
| `environments` | object `{name: id}` | Run environment selection |
| `milestones` | object `{title: id}` | Run milestone selection |
| `configurations` | nested object | Optional run configuration context |

### `config/workspace.yaml`

Simulation keys:

| Key | Type | Notes |
|---|---|---|
| `seed.seed_value` | integer | Deterministic randomness seed |
| `simulation.run_count` | integer | Number of runs to create (fallback default: 20) |
| `simulation.pass_rate_range` | tuple/array | Baseline pass distribution |
| `simulation.weak_suite` | string | Suite title with fail bias |
| `simulation.run_types` | list | Run themes (Regression, Feature, Smoke) |

### `assets/seed-data/QD-2026-02-18.csv`

Required columns for Script 5 contextualization:

| Column | Type | Purpose |
|---|---|---|
| `id` | string/int | CSV case key joined against `state.case_ids` |
| `suite_id` | string/int | Weak-suite and domain-aware weighting |
| `suite` | string | Human-readable suite context for titles/comments |
| `parameters` | string | Parameterized result data source (if present) |

---

## Runtime Entities

### SimulatedRunPlan

| Field | Type | Validation |
|---|---|---|
| `run_index` | int | `>= 1` |
| `run_type` | enum | one of configured run types |
| `title` | string | non-empty, contextual |
| `description` | string | non-empty, realistic domain language |
| `environment_id` | int | exists in state `environments` |
| `milestone_id` | int | exists in state `milestones` |
| `tags` | list[string] | length 1-3 |
| `selected_case_ids` | list[int] | all IDs must exist in state `case_ids` values |
| `jira_task_payload` | object | required fields for Jira Task creation |

### SimulatedResult

| Field | Type | Validation |
|---|---|---|
| `case_id` | int | must exist in selected run cases |
| `status` | enum | `passed`, `failed`, `skipped` |
| `is_autotest` | bool | at least 20% overall must be `false` |
| `start_time` | int | epoch seconds; must be `< end_time` |
| `end_time` | int | epoch seconds |
| `time_ms` | int | `> 0`; matches duration class |
| `defect` | bool | only true when status is failed |
| `comment` | string | from rotated realistic pool |
| `stacktrace` | string/null | required for automated failures; omitted for manual |
| `param` | map[string,string]/null | only when parameters exist in source |
| `attachments` | list[string] | optional, hash references |
| `steps` | list[StepResult] | required, non-empty `action` |

### StepResult

| Field | Type | Validation |
|---|---|---|
| `position` | int | sequential, 1-based |
| `status` | enum | `passed`, `failed`, `skipped`, `blocked`, `invalid` |
| `action` | string | required, non-empty |
| `comment` | string | optional, concise |
| `attachments` | list[string] | optional, limited |
| `expected_result` | string | optional |
| `data` | string | optional |

### JiraRunTask

| Field | Type | Validation |
|---|---|---|
| `id` | string/int | returned by Jira create issue |
| `key` | string | external issue key format (e.g., `AB-123`) |
| `summary` | string | aligns with run theme |
| `description` | string | includes why/run-risk/change context |
| `issue_type` | string | must be `Task` |

### RunExternalLink

| Field | Type | Validation |
|---|---|---|
| `run_id` | int | created run ID |
| `external_issue` | string | Jira issue key used for Qase run linkage |
| `type` | enum | `jira-cloud` |

---

## State Transitions

### Run Lifecycle

1. `planned` -> `created` (Qase run created, run ID assigned)
2. `created` -> `results_submitted` (bulk results posted successfully)
3. `results_submitted` -> `jira_created` (Jira Task created)
4. `jira_created` -> `linked` (Qase run external issue link updated)
5. `linked` -> `completed` (run complete endpoint called)

No run may transition to `completed` before `results_submitted` and `linked`.

### Result Lifecycle

1. `generated` (timings/status/metadata produced)
2. `validated` (case_id/timing/defect rules checked)
3. `persisted` (included in successful bulk result submission)

Invalid results are excluded before API submission.

---

## Validation Rules Summary

- All submitted results must map to existing Qase case IDs from state.
- At least 30% of runs must resolve to fully passed results.
- At least 20% of total results must be manual (`is_autotest=false`).
- Around 50% of failed results must set `defect=true`; 0 non-failed results may do so.
- Every run must include at least one timeline overlap and one idle gap.
- Every result must include at least one step with non-empty action.
- Parameter payloads may only contain values from source definitions.

