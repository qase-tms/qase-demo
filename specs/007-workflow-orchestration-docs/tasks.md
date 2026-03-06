# Tasks: Workflow Orchestration and Operator Guide

**Input**: Design documents from `/specs/007-workflow-orchestration-docs/`  
**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/`, `quickstart.md`

**Tests**: No mandatory TDD requirement in the spec; this plan uses runnable workflow validation tasks (`workflow_dispatch`, dry-run/live checks, and README verification) instead of creating new automated test suites.

**Organization**: Tasks are grouped by user story so each story can be implemented and validated independently.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependency on incomplete tasks)
- **[Story]**: User story mapping (`[US1]`, `[US2]`, `[US3]`)
- Every task includes an exact file path

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Establish workflow/documentation skeleton and feature-scoped contracts.

- [X] T001 Create parent orchestration workflow scaffold in `.github/workflows/workflow-orchestration.yml`
- [X] T002 [P] Create reusable child workflow scaffold in `.github/workflows/reusable-script-runner.yml`
- [X] T003 [P] Add feature runbook section headers for workflow setup/usage in `README.md`
- [X] T004 [P] Add workflow integration section headers in `scripts/README.md`
- [X] T005 Add `tasks.md` references and cross-links in `specs/007-workflow-orchestration-docs/quickstart.md`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Implement shared orchestration controls required by all user stories.

**⚠️ CRITICAL**: No user-story work starts before this phase is complete.

- [X] T006 Implement common workflow inputs (`mode`, `seed`, `run_count`, `min_runs`, `max_runs`, `dry_run`) in `.github/workflows/workflow-orchestration.yml`
- [X] T007 [P] Implement UTC weekday schedule trigger and manual dispatch trigger in `.github/workflows/workflow-orchestration.yml`
- [X] T008 [P] Implement reusable workflow input schema and validation guards in `.github/workflows/reusable-script-runner.yml`
- [X] T009 Implement credential preflight checks for `QASE_API_TOKEN`, `JIRA_BASE_URL`, `JIRA_EMAIL`, `JIRA_API_TOKEN`, `JIRA_PROJECT_KEY` in `.github/workflows/reusable-script-runner.yml`
- [X] T010 Implement `.venv/bin/python` runtime usage in `.github/workflows/reusable-script-runner.yml` without introducing workflow-time dependency installation steps
- [X] T011 Implement centralized argument builder for dry-run and numeric overrides in `.github/workflows/reusable-script-runner.yml`
- [X] T012 Implement dedicated state writeback branch configuration (`automation/state`) in `.github/workflows/reusable-script-runner.yml`
- [X] T013 Implement guarded git writeback step for `state/*.json` changes only in `.github/workflows/reusable-script-runner.yml`
- [X] T014 Add minimal workflow permission model (`contents: write`) in `.github/workflows/workflow-orchestration.yml` and document branch-targeted state writes with branch protections in `README.md`

**Checkpoint**: Shared workflow infrastructure is complete and user-story implementations can begin.

---

## Phase 3: User Story 1 - Bootstrap and Automate Workspace Activity (Priority: P1) 🎯 MVP

**Goal**: Deliver manual full-chain initialization and weekday UTC automated maintenance using parent + reusable workflows.

**Independent Test**: Trigger initialization manually and verify the full script chain succeeds; verify scheduled maintenance executes on weekday UTC and blocks overlapping unsafe conditions.

### Implementation for User Story 1

- [X] T015 [US1] Implement parent-to-reusable call for `mode=init` in `.github/workflows/workflow-orchestration.yml`
- [X] T016 [US1] Implement fail-fast init chain execution order (`workspace_init`, `suite_generator`, `jira_requirements create`, `case_generator`, `run_simulator`) in `.github/workflows/reusable-script-runner.yml`
- [X] T017 [US1] Implement parent-to-reusable call for `mode=maintenance` in `.github/workflows/workflow-orchestration.yml`
- [X] T018 [US1] Implement maintenance command path (`scripts/maintenance.py`) with override propagation in `.github/workflows/reusable-script-runner.yml`
- [X] T019 [US1] Implement precondition guard that blocks maintenance when `state/workspace_state.json` is missing in `.github/workflows/reusable-script-runner.yml`
- [X] T020 [US1] Align or replace legacy maintenance workflow wiring by updating `.github/workflows/daily-activity.yml` to call parent orchestration path
- [X] T021 [US1] Update initialization and maintenance execution flow documentation in `README.md`
- [X] T022 [US1] Record expected success outputs and state artifacts for US1 in `specs/007-workflow-orchestration-docs/quickstart.md`
- [X] T043 [US1] Implement orchestration-level overlap guard (GitHub Actions concurrency + skip messaging) in `.github/workflows/workflow-orchestration.yml`
- [X] T044 [US1] Add overlap guard validation steps and expected log output in `specs/007-workflow-orchestration-docs/quickstart.md`

**Checkpoint**: Full init + scheduled maintenance orchestration is functional and demoable.

---

## Phase 4: User Story 2 - Operate Safely With Clear Inputs and Secrets (Priority: P2)

**Goal**: Provide complete operator guidance for tokens, secrets/variables, trigger options, and safe execution modes.

**Independent Test**: A new maintainer can configure secrets, understand every workflow input, run dry-run successfully, then run live without external guidance.

### Implementation for User Story 2

- [X] T023 [US2] Document token acquisition and token verification steps in `README.md`
- [X] T024 [P] [US2] Document repository secret setup (names, purpose, where configured) in `README.md`
- [X] T025 [P] [US2] Document non-secret variable/config setup (`config/workspace.yaml`, workflow inputs) in `README.md`
- [X] T026 [US2] Add workflow trigger input table (name, type, default, allowed range, impact) in `README.md`
- [X] T027 [US2] Add safe run sequence (dry-run first, then live) with command-level examples in `README.md`
- [X] T028 [US2] Add state writeback policy for dedicated automation/state branch in `README.md`
- [X] T029 [US2] Add cross-reference from script-level docs to workflow-level setup in `scripts/README.md`
- [X] T030 [US2] Update `specs/007-workflow-orchestration-docs/quickstart.md` with first-time maintainer walkthrough and validation checklist
- [X] T045 [US2] Define and document state retention lifecycle (window, pruning, and archival rules) for the automation/state branch in `README.md`
- [X] T046 [US2] Implement retention policy enforcement step for automation/state branch updates in `.github/workflows/reusable-script-runner.yml`

**Checkpoint**: Setup and trigger usage are self-serve for first-time maintainers.

---

## Phase 5: User Story 3 - Troubleshoot and Recover Operationally (Priority: P3)

**Goal**: Make failures diagnosable and recoverable with explicit remediation paths.

**Independent Test**: Simulate missing secret, missing state, and partial downstream failure; operator can identify cause and recover using workflow logs + README.

### Implementation for User Story 3

- [X] T031 [US3] Add explicit failure messages for credential preflight failures in `.github/workflows/reusable-script-runner.yml`
- [X] T032 [US3] Add explicit failure messages for init-chain fail-fast stopping point in `.github/workflows/reusable-script-runner.yml`
- [X] T033 [US3] Add explicit skip/failure remediation hints for maintenance preconditions in `.github/workflows/reusable-script-runner.yml`
- [X] T034 [US3] Add troubleshooting matrix for workflow failures and recovery actions in `README.md`
- [X] T035 [US3] Add rollback and rerun guidance for automation/state branch issues in `README.md`
- [X] T036 [US3] Add operator log-reading checklist and escalation path in `README.md`
- [X] T037 [US3] Add failure simulation and recovery verification steps in `specs/007-workflow-orchestration-docs/quickstart.md`

**Checkpoint**: Operational recovery guidance is complete and actionable.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final consistency, governance checks, and end-to-end validation.

- [X] T038 [P] Validate all contracts align with implemented workflow inputs and behavior in `specs/007-workflow-orchestration-docs/contracts/init-workflow-dispatch.md`
- [X] T039 [P] Validate all contracts align with implemented workflow inputs and behavior in `specs/007-workflow-orchestration-docs/contracts/maintenance-workflow-dispatch.md`
- [X] T040 Validate README/runbook consistency across `README.md`, `scripts/README.md`, and `specs/007-workflow-orchestration-docs/quickstart.md`
- [ ] T041 Execute end-to-end dry-run and live validation steps and record results in `specs/007-workflow-orchestration-docs/quickstart.md`
- [X] T042 Final traceability sweep mapping FR-001..FR-018 to implemented files in `specs/007-workflow-orchestration-docs/tasks.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: Starts immediately.
- **Phase 2 (Foundational)**: Depends on Phase 1 and blocks all user stories.
- **Phase 3 (US1)**: Depends on Phase 2; delivers MVP orchestration.
- **Phase 4 (US2)**: Depends on US1 workflow behavior to document actual operator flows.
- **Phase 5 (US3)**: Depends on US1/US2 outputs for realistic recovery guidance.
- **Phase 6 (Polish)**: Depends on completion of selected user stories.

### User Story Dependencies

- **US1 (P1)**: No dependency on other stories after foundational work.
- **US2 (P2)**: Depends on US1 implementation details for accurate setup/runbook documentation.
- **US3 (P3)**: Depends on US1 runtime behavior and US2 documentation surfaces for recovery workflows.

### Within Each User Story

- Implement workflow behavior before documentation that references it.
- Add remediation outputs before troubleshooting guide finalization.
- Complete quickstart validations before closing story phase.

---

## Parallel Opportunities

- **Phase 1**: `T002`, `T003`, `T004` can run in parallel.
- **Phase 2**: `T007`, `T008`, `T010` can run in parallel after `T006`.
- **US2**: `T024` and `T025` can run in parallel.
- **Polish**: `T038` and `T039` can run in parallel.

---

## Parallel Example: User Story 1

```bash
# After foundational tasks are complete:
Task: "Implement init mode workflow call in .github/workflows/workflow-orchestration.yml"      # T015
Task: "Implement init script sequence in .github/workflows/reusable-script-runner.yml"         # T016
```

## Parallel Example: User Story 2

```bash
# After US1 behavior is merged:
Task: "Document repository secret setup in README.md"                                            # T024
Task: "Document variable/config setup in README.md"                                              # T025
```

## Parallel Example: User Story 3

```bash
# With remediation logging strategy defined:
Task: "Add credential and fail-fast remediation outputs in reusable workflow"                    # T031-T033
Task: "Write troubleshooting matrix and escalation guidance in README.md"                        # T034-T036
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1 and Phase 2.
2. Complete Phase 3 (US1).
3. Validate manual init + weekday maintenance paths.
4. Demo orchestration baseline.

### Incremental Delivery

1. Deliver US1 orchestration workflow behavior.
2. Deliver US2 onboarding/runbook completeness.
3. Deliver US3 recovery and troubleshooting hardening.
4. Finish with Phase 6 consistency and traceability checks.

### Parallel Team Strategy

1. One contributor handles workflow implementation (`.github/workflows/*`).
2. One contributor handles README and script docs (`README.md`, `scripts/README.md`).
3. One contributor handles quickstart/contracts consistency (`specs/007-workflow-orchestration-docs/*`).

### Suggested MVP Scope

- **MVP** = through **Phase 3 (US1)** only.
- US2/US3 are operational excellence increments that follow MVP behavior.

---

## Notes

- [P] tasks target separate files and no incomplete dependencies.
- User-story labels preserve traceability to independent test criteria.
- Prefer validating in dry-run mode before live changes in every story.

## FR Traceability (T042)

- `FR-001`: `workflow-orchestration.yml` (mode inputs), `reusable-script-runner.yml` (init sequence)
- `FR-002`: `workflow-orchestration.yml` (schedule + maintenance mode), `daily-activity.yml`
- `FR-003`: `reusable-script-runner.yml` (init fail-fast execution and preflight)
- `FR-004`: `reusable-script-runner.yml` (maintenance precondition checks)
- `FR-005`: `workflow-orchestration.yml` (manual override inputs)
- `FR-006`: `reusable-script-runner.yml` (dry-run argument propagation)
- `FR-007`: `README.md` (manual trigger input table)
- `FR-008`: `README.md` (secret setup documentation)
- `FR-009`: `README.md` (non-secret config setup)
- `FR-010`: `README.md`, `scripts/README.md`, `quickstart.md` (step-by-step runbook)
- `FR-011`: `reusable-script-runner.yml` + `README.md` (log and remediation guidance)
- `FR-012`: `workflow-orchestration.yml` (concurrency guard) + `quickstart.md` overlap validation
- `FR-013`: `README.md` (token acquisition + local token verification)
- `FR-014`: `.github/workflows/workflow-orchestration.yml` + `.github/workflows/reusable-script-runner.yml`
- `FR-015`: `README.md` (state policy) + `reusable-script-runner.yml` (state lifecycle handling)
- `FR-015a`: `reusable-script-runner.yml` (automation/state writeback only)
- `FR-016`: `README.md` (repository-level secret model and names)
- `FR-017`: `workflow-orchestration.yml` and `daily-activity.yml` (weekday UTC schedule)
- `FR-018`: `reusable-script-runner.yml` (init chain fail-fast behavior)
