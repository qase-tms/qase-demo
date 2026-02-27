## Seeding scripts (local, token-based)

These scripts use:
- Jira API token from your shell environment
- Qase API token from env var `QASE_API_TOKEN`
- The generated local Qase v1 python client under `qase-api-client/` (no pip install required)

Always run with the repo-local interpreter:

```bash
cd "/Users/manju/qase-tms/qase-demo"
.venv/bin/python scripts/qase_verify_token.py
```

## Script 5: run simulator

Required env vars:

- `QASE_API_TOKEN`
- `JIRA_BASE_URL`
- `JIRA_EMAIL`
- `JIRA_API_TOKEN`
- optional `JIRA_PROJECT_KEY` override (default source is `state/jira_state.json -> project.key`)

Dry-run:

```bash
.venv/bin/python scripts/run_simulator.py --dry-run
```

Live run:

```bash
.venv/bin/python scripts/run_simulator.py
```

## Script 6: maintenance

Required env vars:

- `QASE_API_TOKEN`
- `JIRA_BASE_URL`
- `JIRA_EMAIL`
- `JIRA_API_TOKEN`
- optional `JIRA_PROJECT_KEY` override (default source is `state/jira_state.json -> project.key`)

Dry-run:

```bash
.venv/bin/python scripts/maintenance.py --dry-run
```

Live run:

```bash
.venv/bin/python scripts/maintenance.py
```

Optional overrides:

```bash
.venv/bin/python scripts/maintenance.py --seed 42 --min-runs 1 --max-runs 6
```

## Workflow integration

GitHub Actions orchestration for these scripts is documented in:

- `README.md` (root): workflow setup, secrets, trigger inputs, dry-run/live process
- `.github/workflows/workflow-orchestration.yml`: parent dispatcher
- `.github/workflows/reusable-script-runner.yml`: step runner and state writeback

Use this script README for local script semantics, and the root README for repository-level workflow operation.

