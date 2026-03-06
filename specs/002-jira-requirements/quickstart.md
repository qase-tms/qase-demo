# Quickstart: Jira Requirement Provisioning

## Prerequisites

```bash
pip install pyyaml        # only stdlib + PyYAML required; no requests needed
```

## Prepare credentials

Export environment variables before running (or rely on the interactive prompt):

```bash
export JIRA_BASE_URL="https://yourorg.atlassian.net"
export JIRA_EMAIL="you@example.com"
export JIRA_API_TOKEN="your-api-token"
```

Alternatively pass them as CLI flags:

```bash
python scripts/jira_requirements.py create \
  --base-url https://yourorg.atlassian.net \
  --email you@example.com \
  --token your-api-token
```

## Confirm seed file

Ensure `config/seeds/jira-requirements.seed.yaml` is present in the repo root and contains
all epics and stories.  Run a dry-run first to validate without touching Jira:

```bash
python scripts/jira_requirements.py create --dry-run
```

## Create project + issues

```bash
python scripts/jira_requirements.py create --seed config/seeds/jira-requirements.seed.yaml
```

The script will:
1. Read project metadata from `config/workspace.yaml`.
2. Query Jira for existing projects and pick a unique name/key.
3. Create the project, bulk-create all epics, then bulk-create all stories.
4. Write the slug → Jira key/ID mapping to `state/jira_state.json`.

## Inspect results

```bash
cat state/jira_state.json
```

## Re-run safely

Re-running creates a new project with a suffixed name (e.g. `ShopEase Web App (2)`)
and a fresh two-letter key, leaving the previous project and its issues untouched.

## Discover Jira field IDs (for debugging)

```bash
# requires JIRA_PROJECT_KEY env var or --project-key flag
python scripts/jira_requirements.py discover --project-key AA
```

## Error cases

| Error message | Likely cause | Fix |
|---|---|---|
| `[ERROR] Jira API error 401` | Wrong email or API token | Regenerate token at id.atlassian.com |
| `[ERROR] Duplicate epic slugs` | Seed YAML has two epics with the same slug | Edit `config/seeds/jira-requirements.seed.yaml` |
| `[ERROR] … creation mismatch` | Jira bulk API partial failure | Check Jira project permissions / issue type config |
| `[ERROR] Seed file not found` | Wrong `--seed` path | Verify path relative to current directory |
| `[ERROR] … not set … no interactive terminal` | Running in CI without env vars | Set `JIRA_EMAIL` and `JIRA_API_TOKEN` in the workflow |
