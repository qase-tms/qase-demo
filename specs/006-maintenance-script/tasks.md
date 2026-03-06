# Tasks: Maintenance Script Daily Activity Feed

**Input**: Design documents from `/specs/006-maintenance-script/`  
**Prerequisites**: `plan.md`, `spec.md`, `research.md`, `data-model.md`, `contracts/`, `quickstart.md`

**Tests**: No test-first mandate in the spec; this task list uses executable validation tasks (dry-run/live/verification) rather than mandatory new automated test suites.

**Organization**: Tasks are grouped by user story so each story can be implemented and validated independently.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependency on incomplete tasks)
- **[Story]**: User story mapping (`[US1]`, `[US2]`, `[US3]`)
- Every task includes an exact file path

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Prepare maintenance config surface and documentation skeleton.

- [X] T001 Add `maintenance` configuration block (`min_runs`, `max_runs`, `run_count_weights`, `weekdays_only`, `schedule_timezone`) in `config/workspace.yaml`
- [X] T002 [P] Create maintenance state bootstrap helpers (`maintenance_state.json` load/init/save) in `scripts/qase_seed_utils.py`
- [X] T003 [P] Add maintenance script usage section and canonical step ordering in `scripts/README.md`
- [X] T004 [P] Update root docs for 6-step flow and weekday maintenance cadence in `README.md`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Implement core cycle primitives required by all stories.

**⚠️ CRITICAL**: No user-story work starts before this phase is complete.

- [X] T005 Create `scripts/maintenance.py` CLI scaffold (`--dry-run`, `--seed`, `--min-runs`, `--max-runs`) and argument validation
- [X] T006 Implement centralized throttled request wrapper reuse (`<=5 req/sec`, retry/backoff) in `scripts/maintenance.py`
- [X] T007 Implement state/config preflight validation (`workspace_state`, CSV, env vars, attachment pool) in `scripts/maintenance.py`
- [X] T008 Implement weighted run-count selector for range `1..6` biased low in `scripts/maintenance.py`
- [X] T009 Implement UTC weekday gate (Mon-Fri only) and explicit skip output in `scripts/maintenance.py`
- [X] T010 Implement active-cycle overlap lock read/write against `state/maintenance_state.json` in `scripts/maintenance.py`

**Checkpoint**: Core execution engine ready for independent user-story increments.

---

## Phase 3: User Story 1 - Keep Workspace Active Daily (Priority: P1) 🎯 MVP

**Goal**: Run weekday maintenance cycles that append realistic daily activity.

**Independent Test**: Execute a weekday cycle and verify `1-6` runs are generated with realistic results and attachments.

### Implementation for User Story 1

- [X] T011 [US1] Implement per-cycle run planning (run types, titles, tags, env/milestone selection) in `scripts/maintenance.py`
- [X] T012 [US1] Implement run creation payload/call contract for maintenance runs in `scripts/maintenance.py`
- [X] T013 [US1] Implement bulk result generation/submission using only seeded case IDs in `scripts/maintenance.py`
- [X] T014 [US1] Implement evidence strategy enforcing high attachment coverage (`>=90%`) in `scripts/maintenance.py`
- [X] T015 [US1] Implement dry-run maintenance output (weekday decision, selected run count, planned run summaries) in `scripts/maintenance.py`
- [X] T016 [US1] Update quickstart execution examples and expected outcomes for weekday low-volume cycles in `specs/006-maintenance-script/quickstart.md`
- [X] T017 [US1] Run dry-run validation and record observed run-count distribution sample in `specs/006-maintenance-script/quickstart.md`

**Checkpoint**: Weekday tactical activity generation is functional and demoable.

---

## Phase 4: User Story 2 - Preserve Stable Workspace Structure (Priority: P2)

**Goal**: Guarantee maintenance appends operational activity only and never mutates seeded structure.

**Independent Test**: Run maintenance repeatedly and confirm suite/case counts remain unchanged while run/result activity grows.

### Implementation for User Story 2

- [X] T018 [US2] Add immutable-scope guard to block suite/case mutation endpoints in `scripts/maintenance.py`
- [X] T019 [US2] Add pre/post structural safety checks (suite/case invariants) in `scripts/maintenance.py`
- [X] T020 [US2] Persist cycle summary metadata (`last_cycle`, short history) in `state/maintenance_state.json` via `scripts/maintenance.py`
- [X] T021 [US2] Add verification guidance for structure invariants in `specs/006-maintenance-script/quickstart.md`
- [X] T022 [US2] Add operational notes for lock-file lifecycle and safe rerun behavior in `scripts/README.md`

**Checkpoint**: Maintenance runs are append-only and preserve fixed seeded workspace structure.

---

## Phase 5: User Story 3 - Operate Reliably With Recoverable Failures (Priority: P3)

**Goal**: Continue cycle execution when downstream integration failures occur and emit clear outcomes.

**Independent Test**: Simulate Jira/link failure in one run and verify later runs continue; incomplete run includes explicit reason.

### Implementation for User Story 3

- [X] T023 [US3] Implement Jira task creation per maintenance run in `scripts/maintenance.py`
- [X] T024 [US3] Implement run external issue linking and completion sequencing in `scripts/maintenance.py`
- [X] T025 [US3] Implement recoverable failure path (mark run incomplete, continue remaining runs) in `scripts/maintenance.py`
- [X] T026 [US3] Implement cycle-level summary output (requested/completed/incomplete + reasons) in `scripts/maintenance.py`
- [X] T027 [US3] Implement weekend skip + overlap skip telemetry in cycle summary state in `scripts/maintenance.py`
- [X] T028 [US3] Add troubleshooting and failure-verification steps in `specs/006-maintenance-script/quickstart.md`

**Checkpoint**: Maintenance cycles are resilient and operationally observable.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Finalize scheduling and end-to-end operator readiness.

- [X] T029 [P] Update workflow schedule/guards for weekday UTC execution in `.github/workflows/daily-activity.yml`
- [X] T030 [P] Align top-level implementation roadmap references to maintenance-only defect strategy in `plan.md`
- [X] T031 Run full quickstart validation pass (dry-run + weekday live + overlap skip) and capture final operator checklist in `specs/006-maintenance-script/quickstart.md`
- [X] T032 Final documentation consistency sweep across `specs/006-maintenance-script/plan.md`, `specs/006-maintenance-script/spec.md`, and `specs/006-maintenance-script/tasks.md`
- [X] T033 Implement rolling 14-day success-rate and weekday/UTC compliance metric persistence in `scripts/maintenance.py`
- [X] T034 Implement per-cycle duration capture and rolling average computation in `scripts/maintenance.py`
- [X] T035 Update measurable verification steps for SC-001/SC-005/SC-006/SC-007 in `specs/006-maintenance-script/quickstart.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: starts immediately.
- **Phase 2 (Foundational)**: depends on Phase 1 and blocks all user stories.
- **Phase 3 (US1)**: depends on Phase 2; delivers MVP.
- **Phase 4 (US2)**: depends on Phase 3 baseline maintenance flow.
- **Phase 5 (US3)**: depends on Phase 3 lifecycle path and Phase 4 state/lock behavior.
- **Phase 6 (Polish)**: depends on completion of selected user stories.

### User Story Dependencies

- **US1 (P1)**: no dependency on other stories after foundational phase.
- **US2 (P2)**: builds on US1 execution path to enforce structural invariants.
- **US3 (P3)**: builds on US1 lifecycle and US2 state/lock surfaces for resilience.

### Within Each User Story

- Implement core lifecycle path before docs/verification updates.
- Implement state persistence before skip/failure telemetry.
- Finish quickstart validation updates before closing the story.

---

## Parallel Opportunities

- **Setup**: `T002`, `T003`, and `T004` can run in parallel.
- **Polish**: `T029` and `T030` can run in parallel.

---

## Parallel Example: User Story 1

```bash
# After foundational primitives are complete:
Task: "Implement run planning and creation in scripts/maintenance.py"        # T011-T012
Task: "Implement result/evidence generation in scripts/maintenance.py"       # T013-T014
```

## Parallel Example: User Story 3

```bash
# With lifecycle baseline in place:
Task: "Implement Jira create/link/complete sequencing in scripts/maintenance.py"  # T023-T024
Task: "Implement failure telemetry and troubleshooting docs updates"               # T027-T028
```

---

## Implementation Strategy

### MVP First (US1 only)

1. Complete Phase 1 and Phase 2.
2. Complete Phase 3 (US1).
3. Validate weekday dry-run + weekday live behavior.
4. Demo baseline daily keep-alive feed.

### Incremental Delivery

1. Deliver US1 weekday low-volume activity generation.
2. Add US2 append-only and structural-safety guarantees.
3. Add US3 resilience, failure continuation, and operational summaries.
4. Finalize workflow/docs in Phase 6.

### Suggested MVP Scope

- **MVP** = through **Phase 3 (US1)**.
- US2 and US3 are hardening increments for governance and operations.
