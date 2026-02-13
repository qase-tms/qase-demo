## Seeding scripts (local, token-based)

These scripts use:
- Jira API token from your shell env (already in your zsh config)
- Qase API token from env var `QASE_API_TOKEN`
- The generated **local** Qase v1 python client under `qase-api-client/` (no pip install required)

### Verify Qase token works

```bash
source "/Users/manju/qase-tms/venv/bin/activate"
cd "/Users/manju/qase-tms/qase-demo"
python scripts/qase_verify_token.py
```

### Jira requirement bulk creation (already set up)

```bash
source "/Users/manju/qase-tms/venv/bin/activate"
cd "/Users/manju/qase-tms/qase-demo"
export JIRA_BASE_URL="https://demoqase-1765364237285.atlassian.net"
export JIRA_EMAIL="demoqase@gmail.com"
export JIRA_PROJECT_KEY="QD"
python jira_bulk_create_requirements.py create --seed jira-requirements.seed.yaml
```

