# qase-demo
A repository for automated GitHub Actions workflows that simulate real user activity via Qase API, creating a self-sustaining demo environment.

## Canonical Execution Order

This project follows a step-based automation approach, with each script building upon the previous one. Execute them in this order:

1. `scripts/workspace_init.py`        — Create Qase project, environments, milestones, and custom fields
2. `scripts/jira_requirements.py`      — Bulk-create Epics + Stories in Jira
3. `scripts/suite_generator.py`        — Create full suite tree in Qase from CSV
4. `scripts/case_generator.py`         — Bulk-create cases from CSV, link to Jira
5. `scripts/run_simulator.py`          — Generate historical test runs + results
6. `scripts/defect_generator.py`       — Create defects from failed results, manage lifecycle
7. `scripts/maintenance.py`            — Daily activity simulation (runs via GitHub Actions)

