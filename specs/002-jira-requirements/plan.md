# Implementation Plan: Jira Requirement Provisioning

**Branch**: `002-jira-requirements` | **Date**: 2026-02-19 | **Spec**: [`specs/002-jira-requirements/spec.md`](specs/002-jira-requirements/spec.md)  
**Input**: Jira project + issue provisioning steps described in `specs/002-jira-requirements/spec.md`

## Summary

Script `scripts/jira_requirements.py` will read `config/seeds/jira-requirements.seed.yaml`, prompt for or accept Jira credentials, deduplicate the target project's name/key using the `scripts/workspace_init.py` strategy, bulk-create the epics and stories, and write a complete slug → Jira key/ID mapping to `state/jira_state.json` for downstream linking.

## Technical Context

**Language/Version**: Python 3.11 (matches the rest of the workspace automation suite).  
**Primary Dependencies**: `requests`, `PyYAML`, shared helpers (`scripts/qase_seed_utils.py`).  
**Storage**: `state/jira_state.json` (JSON file, atomic writes).  
**Testing**: `pytest` for unit tests covering seed parsing, project name selection, and mapping persistence.  
**Target Platform**: Linux/macOS developer machines + GitHub Actions runners executing Python scripts.  
**Project Type**: Single CLI automation script invoked sequentially after `scripts/workspace_init.py`.  
**Performance Goals**: Respect Jira throttling by sending ≤5 requests per second (global).  
**Constraints**: Credentials never stored in repo; script performs pre-flight validation, retries with exponential backoff, and fails before mutating state on Jira errors.  
**Scale/Scope**: Limited to ≤50 Jira artifacts (6 epics + ~40 stories); all data comes from the static seed file.

## Constitution Check

All constitution gates pass because the script:
1. Keeps credentials in environment variables / CLI input (Principle I, II, Security Rules).  
2. Operates deterministically via the fixed seed, aligning with Realism and Deterministic Variability.  
3. Creates requirements once and writes state atomically, honoring Full Reproducibility and Fixed Scope.  
4. Enforces rate limiting and logging (Technical Architecture & Security).  
5. Does not alter marketing-visible data manually; obeys the canonical execution order (Core Principles & Activity Simulation Rules).  

## Project Structure

### Documentation (this feature)

```text
specs/002-jira-requirements/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── jira-requirements-api.md
└── tasks.md     # To be authored via /speckit.tasks
```

### Source Code (repository root)

```text
scripts/
├── jira_requirements.py    # Main entry point for this feature
├── qase_seed_utils.py      # Shared state helpers (load/save state)
└── jira_utils.py           # HTTP helpers (if reused for Jira auth)

state/
├── jira_state.json         # Output mapping (created by this script)
└── workspace_state.json    # Read-only dependency for project metadata (populated earlier)
```

**Structure Decision**: Single-script structure so all Jira provisioning logic lives under `scripts/jira_requirements.py`, referencing shared helpers. Documentation tracks the new research/design artifacts plus a TODO `tasks.md` created later.

## Complexity Tracking

No constitution violations were introduced; the work stays within the step-based execution model and obeys all constitutional gates, so no additional tracking rows are required.
