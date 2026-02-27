# qase-demo
A repository for automated GitHub Actions workflows that simulate real user activity via Qase API, creating a self-sustaining demo environment.

## Canonical Execution Order

This project follows a step-based automation approach, with each script building upon the previous one. Execute them in this order:

1. `scripts/workspace_init.py`        — Create Qase project, environments, milestones, and custom fields
2. `scripts/jira_requirements.py`      — Bulk-create Epics + Stories in Jira
3. `scripts/suite_generator.py`        — Create full suite tree in Qase from CSV
4. `scripts/case_generator.py`         — Bulk-create cases from CSV, link to Jira
5. `scripts/run_simulator.py`          — Generate present-time realistic test runs + results
6. `scripts/maintenance.py`            — Weekday UTC maintenance activity simulation (runs via GitHub Actions)

## GitHub Workflow Orchestration

This repository provides an orchestration flow with:

- a parent workflow: `.github/workflows/workflow-orchestration.yml`
- a reusable runner: `.github/workflows/reusable-script-runner.yml`
- a legacy maintenance entrypoint that delegates to orchestration: `.github/workflows/daily-activity.yml`

### Modes

- `init` mode (manual): runs canonical full chain in fail-fast order:
  1. `scripts/workspace_init.py`
  2. `scripts/suite_generator.py`
  3. `scripts/jira_requirements.py create`
  4. `scripts/case_generator.py`
  5. `scripts/run_simulator.py`
- `maintenance` mode (manual or scheduled): runs `scripts/maintenance.py`

## Token Acquisition and Validation

### Qase token

1. Log in to Qase.
2. Generate a personal API token from your account API token page.
3. Save it securely as `QASE_API_TOKEN`.

### Jira token

1. Log in to your Atlassian account.
2. Create an API token from Atlassian account security settings.
3. Collect:
   - `JIRA_BASE_URL` (for example: `https://your-org.atlassian.net`)
   - `JIRA_EMAIL`
   - `JIRA_API_TOKEN`
   - Optional override: `JIRA_PROJECT_KEY` (only if you want to force a specific project)

### Local verification

Use the repository virtual environment:

```bash
cd "/Users/manju/qase-tms/qase-demo"
.venv/bin/python scripts/qase_verify_token.py
```

## GitHub Secrets and Variables Setup

### Repository secrets (required)

Add these under **Settings -> Secrets and variables -> Actions -> Repository secrets**:

- `QASE_API_TOKEN`
- `JIRA_BASE_URL`
- `JIRA_EMAIL`
- `JIRA_API_TOKEN`
- Optional: `JIRA_PROJECT_KEY` (normally auto-resolved from `state/jira_state.json`)

### Non-secret configuration (required)

Keep defaults and simulation tuning in:

- `config/workspace.yaml`
- `requirements.txt` (workflow runtime dependencies installed in CI)

These values are not GitHub secrets and should be reviewed before the first run.

## Manual Trigger Inputs

When running `Workflow Orchestration` manually (`workflow_dispatch`), use:

| Input | Type | Default | Applies To | Notes |
|---|---|---|---|---|
| `mode` | choice | `init` | init/maintenance | Required; selects execution path |
| `seed` | number | empty | both | Optional deterministic override |
| `run_count` | number | empty | init | Passed to `run_simulator.py --run-count` |
| `min_runs` | number | empty | maintenance | Range `1..6` |
| `max_runs` | number | empty | maintenance | Range `1..6`, must be `>= min_runs` |
| `dry_run` | boolean | `false` | both | Preview mode without external writes |

## How to Run

### First-time safe path

1. Trigger `Workflow Orchestration` with:
   - `mode=init`
   - `dry_run=true`
2. Validate logs and input handling.
3. Re-run with:
   - `mode=init`
   - `dry_run=false`
4. Confirm state files are produced and updated under `state/`.

### Ongoing maintenance

- Scheduled via weekdays UTC cadence (`Mon-Fri`) through `daily-activity.yml`.
- Can also be manually dispatched with `mode=maintenance` for validation.
- Maintenance becomes active only after the init flow has produced bootstrap state (`state/workspace_state.json` + `state/jira_state.json` on `automation/state` branch); until then scheduled maintenance runs are skipped with an info message.

## State Writeback and Branch Protection

- State remains repository-managed in `state/*.json`.
- Workflow writeback targets dedicated branch `automation/state` only.
- Direct default-branch workflow state commits are disallowed by policy.
- Recommended protection for `automation/state`:
  - restrict direct human pushes
  - require workflow-only updates
  - keep history retention policy documented and enforced

## State Retention Policy

Automation/state retention policy:

- keep rolling operational state in `state/*.json`
- keep optional history snapshots in `state/history/`
- prune history snapshots older than 90 days during writeback

## Troubleshooting

| Symptom | Likely Cause | Recovery |
|---|---|---|
| Workflow fails at preflight | Missing repository secret | Add missing secret in repository Actions secrets |
| Init fails mid-chain | Step-specific script failure | Fix failing step cause and rerun init (fail-fast preserves ordering) |
| Maintenance skipped before bootstrap | Missing bootstrap state (`workspace_state.json` or `jira_state.json`) | Run init mode once and let state commit to `automation/state` |
| Maintenance overlap behavior | Existing run in progress | Wait for current run or inspect concurrency queue |
| State branch not updated | Permission/protection mismatch | Verify `contents: write`, branch policy, and workflow token rights |

### Log-reading checklist

When a run fails, review logs in this order:

1. `Validate mode and numeric inputs`
2. `Preflight required credentials`
3. `Verify project virtual environment runtime`
4. `Build execution args`
5. Mode execution step (`Execute init chain` or `Execute maintenance`)
6. `Commit state snapshots to automation/state branch`

Escalate after capturing:

- failed step name
- full error output
- selected workflow inputs
- run URL

### Rollback and rerun guidance

For bad state updates on `automation/state`:

1. Revert the bad commit on `automation/state`.
2. Re-run `Workflow Orchestration` in `init` mode with `dry_run=true`.
3. Re-run with `dry_run=false` once output is confirmed.
4. Re-run maintenance manually (`mode=maintenance`) to confirm stable operation.

