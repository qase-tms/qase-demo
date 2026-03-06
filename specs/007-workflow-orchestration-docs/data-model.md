# Data Model: Workflow Orchestration and Operator Guide

**Branch**: `007-workflow-orchestration-docs` | **Date**: 2026-02-27

## Entities

### OrchestrationWorkflow

| Field | Type | Validation |
|---|---|---|
| `workflow_name` | string | non-empty |
| `mode` | enum | `init`, `maintenance` |
| `trigger_type` | enum | `workflow_dispatch`, `schedule` |
| `uses_reusable_child` | boolean | must be `true` |
| `status` | enum | `queued`, `running`, `success`, `failed`, `skipped` |

### DispatchInputs

| Field | Type | Validation |
|---|---|---|
| `seed` | integer/null | optional; if present must be non-negative |
| `run_count` | integer/null | optional; used for init simulation controls |
| `min_runs` | integer/null | optional; range `1..6` |
| `max_runs` | integer/null | optional; range `1..6` and `max_runs >= min_runs` |
| `dry_run` | boolean | default `false` |
| `force_weekend` | boolean | optional; default `false` for manual maintenance |

### ScriptStep

| Field | Type | Validation |
|---|---|---|
| `name` | string | one of known script identifiers |
| `order` | integer | strictly increasing for init chain |
| `required_env` | list[string] | must include all step-required vars |
| `allow_dry_run` | boolean | true where script supports `--dry-run` |
| `failure_policy` | enum | `fail_fast` for init chain |

Canonical initialization order:
1. `scripts/workspace_init.py`
2. `suite_generator.py`
3. `jira_requirements.py create`
4. `case_generator.py`
5. `run_simulator.py`

### CredentialInventory

| Field | Type | Validation |
|---|---|---|
| `secret_name` | string | exact GitHub secret key |
| `scope` | enum | `repository` |
| `required_for` | list[enum] | `init`, `maintenance` |
| `validation_method` | string | must include preflight presence check |

Required credentials:
- `QASE_API_TOKEN`
- `JIRA_BASE_URL`
- `JIRA_EMAIL`
- `JIRA_API_TOKEN`
- `JIRA_PROJECT_KEY`

### StateSnapshot

| Field | Type | Validation |
|---|---|---|
| `workspace_state_path` | string | `state/workspace_state.json` |
| `run_sim_state_path` | string | `state/run_simulator_state.json` |
| `maintenance_state_path` | string | `state/maintenance_state.json` |
| `writeback_branch` | string | dedicated automation/state branch |
| `writeback_policy` | enum | `branch_only` (no default-branch direct commit) |

### RunbookSection

| Field | Type | Validation |
|---|---|---|
| `section_name` | string | non-empty |
| `purpose` | string | setup/execution/troubleshooting coverage |
| `required_content` | list[string] | must include steps, options, expected results |

## Relationships

- `OrchestrationWorkflow` consumes one `DispatchInputs`.
- `OrchestrationWorkflow` executes many ordered `ScriptStep`.
- Each `ScriptStep` references required `CredentialInventory` entries.
- `OrchestrationWorkflow` reads/writes one `StateSnapshot`.
- README runbook consists of many `RunbookSection` instances aligned to workflow modes.

## State Transitions

### Init Mode Lifecycle

1. `queued` -> `running` (manual dispatch accepted)
2. `running` -> `failed` (first step failure; fail-fast)
3. `running` -> `success` (all five steps complete)

### Maintenance Mode Lifecycle

1. `queued` -> `running` (scheduled or manual trigger)
2. `running` -> `skipped` (weekend UTC or overlap guard)
3. `running` -> `failed` (precondition/credential/runtime failure)
4. `running` -> `success` (cycle completes per script contract)

## Validation Rules

- Inputs must be validated before any script execution.
- Credential preflight must happen before step 1 in each mode.
- Init mode must stop on first failing step.
- Maintenance schedule must default to weekdays UTC.
- Repository-managed state updates must target dedicated automation/state branch only.
- Dry-run mode must avoid external writes.
