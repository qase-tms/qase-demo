# Implementation Plan: Workflow Orchestration and Operator Guide

**Branch**: `007-workflow-orchestration-docs` | **Date**: 2026-02-27 | **Spec**: [spec.md](spec.md)  
**Input**: Feature specification from `specs/007-workflow-orchestration-docs/spec.md`

## Summary

Design and deliver a parent GitHub Actions orchestration workflow plus reusable child workflow that (1) supports operator-invoked canonical step-sequence initialization (`workspace_init -> suite_generator -> jira_requirements -> case_generator -> run_simulator`) with fail-fast behavior and per-step visibility and (2) executes weekday UTC maintenance cadence. Document complete operator runbook coverage in README, including token acquisition, secret/variable setup, trigger inputs, dry-run/live procedures, troubleshooting, and repository-managed state handling through a dedicated automation/state branch with explicit retention policy.

## Technical Context

**Language/Version**: Python 3.14 for scripts; GitHub Actions YAML for orchestration  
**Primary Dependencies**: Repo scripts under `scripts/`; `PyYAML`; GitHub-hosted actions (`actions/checkout`, `actions/setup-python`)  
**Storage**: Repository-managed files in `config/`, `state/`, and workflow metadata in `.github/workflows/`  
**Testing**: Script `--dry-run` execution, manual `workflow_dispatch` test runs, scheduled maintenance verification, and README walkthrough validation  
**Target Platform**: GitHub Actions (`ubuntu-latest`) plus local macOS/Linux operator environment  
**Project Type**: Single-repository automation and documentation enhancement  
**Performance Goals**: Initialization completes reliably in one manual run; weekday maintenance completes within existing script SLOs and no overlap collisions  
**Constraints**: `.venv/bin/python` invocation only, repo-level secrets, weekday UTC schedule, fail-fast init chain, explicit overlap prevention for maintenance triggers, no direct default-branch state commits, dedicated automation/state branch retention policy, Qase rate limit compliance (`<=5 req/s`)  
**Scale/Scope**: One marketing workspace automation path, one parent orchestration workflow, one reusable child workflow, and one comprehensive README runbook update

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Principle | Status |
|------|-----------|--------|
| No credential leakage into repository/docs | Security Rules | ✅ PASS - plan keeps tokens in GitHub Secrets/local env only; README documents secure setup without embedding secrets |
| Reproducible setup from repo + tokens | Principle II (Full Reproducibility) | ✅ PASS - workflow and README specify deterministic, script-driven setup path |
| Deterministic seeded simulation support | Principle IV | ✅ PASS - manual trigger includes deterministic seed controls and documents behavior |
| Stable visual activity cadence | Principle V | ✅ PASS - maintenance schedule remains weekday UTC with overlap safeguards |
| Fixed scope after seeding | Principle VI | ✅ PASS - initialization/maintenance orchestration preserves suite/case immutability post-seed |
| API usage aligned with in-repo references | API Reference Guidance | ✅ PASS - contracts and quickstart map required calls and sequence explicitly |

**Post-design re-check**: ✅ PASS - Phase 0/1 artifacts preserve all gates with no justified exceptions required.

## Project Structure

### Documentation (this feature)

```text
specs/007-workflow-orchestration-docs/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── init-workflow-dispatch.md
│   ├── maintenance-workflow-dispatch.md
│   ├── create-run.md
│   ├── create-results-bulk.md
│   ├── jira-create-task.md
│   ├── run-link-external-issue.md
│   └── complete-run.md
└── tasks.md
```

### Source Code (repository root)

```text
.github/
└── workflows/
    ├── daily-activity.yml                    # Existing maintenance workflow to evolve
    └── (new parent/reusable orchestration)   # This feature adds/updates workflow definitions

scripts/
├── scripts/workspace_init.py
├── suite_generator.py
├── jira_requirements.py
├── case_generator.py
├── run_simulator.py
├── maintenance.py
└── README.md                                 # Script-level usage reference

config/
└── workspace.yaml                            # Source of defaults and runtime tuning

state/
├── workspace_state.json
├── run_simulator_state.json
└── maintenance_state.json

README.md                                     # Primary operator runbook (this feature updates)
```

**Structure Decision**: Use existing single-project automation layout; add workflow orchestration and documentation artifacts without introducing new runtime services.

## Phase 0: Research Plan

Research tasks generated from unknowns/dependencies/integrations:

1. Establish recommended parent + reusable workflow topology for manual init and scheduled maintenance.
2. Define repository-managed state branch strategy (writeback, conflict avoidance, and rollback posture).
3. Define secure token onboarding and validation flow for Qase/Jira in GitHub repository scope.
4. Determine fail-fast orchestration sequencing and idempotent retry boundaries across scripts.
5. Define operator-facing input contract for workflow_dispatch (seed, run-count bounds, dry-run) with validation rules.

Outputs produced in `research.md`:
- Decision logs with rationale
- Alternatives considered
- Explicit implementation guardrails for Phase 1 design

## Phase 1: Design & Contracts Plan

Design outputs to generate:

1. `data-model.md` - orchestration entities, state transitions, validation rules.
2. `contracts/` - workflow dispatch input contracts and external API interaction contracts.
3. `quickstart.md` - end-to-end operator guide for setup, first run, scheduled run, and troubleshooting.
4. Agent context refresh via `.specify/scripts/bash/update-agent-context.sh cursor-agent`.

## Complexity Tracking

No constitution violations. No justified exceptions required.
