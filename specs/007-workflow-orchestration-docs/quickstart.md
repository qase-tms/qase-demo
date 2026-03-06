# Quickstart: Workflow Orchestration and Operator Guide

## Goal

Run a one-time full initialization chain manually, then keep activity healthy with weekday UTC maintenance automation.

## Prerequisites

1. Repository has Actions enabled.
2. Repository secrets are configured:
   - `QASE_API_TOKEN`
   - `JIRA_BASE_URL`
   - `JIRA_EMAIL`
   - `JIRA_API_TOKEN`
   - `JIRA_PROJECT_KEY`
3. Defaults exist in `config/workspace.yaml`.
4. `state/` directory is available for runtime snapshots.
5. Implementation checklist exists in `specs/007-workflow-orchestration-docs/tasks.md`.

## 1) Manual Initialization Run

Trigger parent workflow in `init` mode (manual dispatch).

Expected sequence:
1. `scripts/workspace_init.py`
2. `scripts/suite_generator.py`
3. `scripts/jira_requirements.py create`
4. `scripts/case_generator.py`
5. `scripts/run_simulator.py`

Recommended first run:
- Enable `dry_run=true` once to verify settings.
- Re-run with `dry_run=false` for live initialization.

First-time maintainer walkthrough:

1. Add repository secrets.
2. Open `Workflow Orchestration` workflow.
3. Run with `mode=init` and `dry_run=true`.
4. Verify logs show step ordering and no mutations.
5. Re-run with `mode=init` and `dry_run=false`.
6. Confirm `state/workspace_state.json` exists and is updated.

## 2) Scheduled Maintenance Run

Maintenance mode runs on weekdays in UTC (`Mon-Fri`), and may also be manually dispatched for validation.

Behavior:
- Uses maintenance script controls (`seed`, `min_runs`, `max_runs`, `dry_run`).
- Skips on disallowed windows and overlap conditions.
- Preserves existing suite/case structure.
- Overlap guard is enforced at orchestration level using workflow concurrency.

## 3) State Writeback Policy

- Runtime state remains repository-managed under `state/*.json`.
- Automated workflow writebacks are committed only to dedicated automation/state branch.
- Default branch direct state commit from workflow is disallowed.
- State history retention target is 90 days in `state/history/`, with older snapshots pruned.

## 4) Verification Checklist

1. Initialization completed all five steps in order.
2. `state/workspace_state.json` exists and includes expected project mappings.
3. Manual maintenance dry-run succeeds without external writes.
4. Next weekday scheduled maintenance run succeeds (or intentionally skips with clear reason).
5. Workflow logs show clear remediation for any failed step.
6. Overlap simulation produces queue/skip-safe behavior and clear log messaging.
7. State updates are pushed to `automation/state` branch only.
8. Retention enforcement prunes history snapshots older than 90 days.

## 5) Troubleshooting

| Symptom | Likely Cause | Recovery |
|---|---|---|
| Init stops at step 1 | Missing/invalid Qase token | Verify `QASE_API_TOKEN`, rerun |
| Init stops at Jira step | Jira secrets or permissions issue | Revalidate `JIRA_*` secrets and project key |
| Maintenance fails precondition | Missing state from init | Re-run full initialization chain |
| Maintenance skipped/queued unexpectedly | Weekend UTC or overlap guard | Check trigger time, concurrency queue, and active run |
| No state branch update | Missing write permission | Grant workflow write permissions for automation/state branch |

## Validation runbook

Use this sequence before closing implementation:

1. `init` dry-run
2. `init` live run
3. `maintenance` dry-run
4. weekday scheduled maintenance verification
5. overlap guard validation via two close manual maintenance triggers
6. retention validation by checking `state/history/` pruning behavior

## Failure simulation and recovery checks

Run these scenario checks before sign-off:

1. Remove one required secret in a non-production test repo and verify preflight failure messaging.
2. Trigger `maintenance` before successful `init` and verify missing-state remediation output.
3. Trigger a forced bad numeric input (for example, `min_runs=7`) and verify validation failure.
4. Restore valid settings and confirm successful rerun path.
