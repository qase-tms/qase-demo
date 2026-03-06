# Tasks: Run Simulator Lifecycle

**Input**: Design documents from `/specs/005-run-simulator-lifecycle/`  
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md

**Tests**: No mandatory automated test-first requirement in spec; this task list focuses on implementation plus independent validation checks per story.

**Organization**: Tasks are grouped by user story to enable independent implementation and verification.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependency on incomplete tasks)
- **[Story]**: User story mapping label (`[US1]`, `[US2]`, `[US3]`)
- Every task includes an exact file path

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Prepare script entrypoint and supporting seed data/config surface.

- [x] T001 Create Script 5 scaffold and CLI entrypoint in `scripts/run_simulator.py`
- [x] T002 Add simulation configuration keys (`run_count`, fallback handling notes) in `config/workspace.yaml`
- [x] T003 [P] Create reusable narrative pools (run titles/descriptions/comments/tags) in `assets/run_simulator_templates.yaml`
- [x] T004 [P] Document Script 5 invocation and flags in `scripts/README.md`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Build core engine and validation primitives required by all stories.

**⚠️ CRITICAL**: No user-story work starts before this phase is complete.

- [x] T005 Implement state/config/CSV loading and schema validation in `scripts/run_simulator.py`
- [x] T006 Implement centralized Qase request wrapper with `<=5 req/sec` throttling and recoverable-error retry policy (5 retries, exponential backoff, 60s cap) in `scripts/run_simulator.py`
- [x] T007 Implement Jira Task create helper and response parsing in `scripts/run_simulator.py`
- [x] T008 Implement deterministic RNG initialization and simulation seed plumbing in `scripts/run_simulator.py`
- [x] T009 Build case context index (suite/domain/parameter metadata) from `state/workspace_state.json` + `assets/seed-data/QD-2026-02-18.csv` in `scripts/run_simulator.py`
- [x] T010 [P] Add reusable attachment-hash cache helpers in `scripts/qase_seed_utils.py`
- [x] T011 [P] Define timeline profile defaults (worker ranges, duration buckets, gap ranges) in `assets/run_timeline_profiles.yaml`

**Checkpoint**: Foundation ready for independently testable user-story increments.

---

## Phase 3: User Story 1 - Seed Believable Run Activity (Priority: P1) 🎯 MVP

**Goal**: Generate realistic runs that complete the full lifecycle (create run -> submit results -> create/link Jira issue -> complete run).

**Independent Test**: Run `.venv/bin/python scripts/run_simulator.py --dry-run` then live run; verify each run has valid metadata and existing-case results only, and that runs are completed only when Jira link succeeds (otherwise left incomplete and logged as failed).

### Implementation for User Story 1

- [x] T012 [US1] Implement run planning logic (theme selection, run count, case subset 80-120) in `scripts/run_simulator.py`
- [x] T013 [US1] Implement run creation payload builder and API call (`POST /run/{code}`) in `scripts/run_simulator.py`
- [x] T014 [US1] Implement bulk result payload assembly using only state-backed case IDs in `scripts/run_simulator.py`
- [x] T015 [US1] Implement Jira Task creation per run (`POST /rest/api/3/issue`) in `scripts/run_simulator.py`
- [x] T016 [US1] Implement run external issue linking (`POST /run/{code}/external-issue`) and sequencing guard in `scripts/run_simulator.py`
- [x] T017 [US1] Implement run completion step (`POST /run/{code}/{id}/complete`) after results+link in `scripts/run_simulator.py`
- [x] T018 [US1] Implement dry-run output mode with planned lifecycle summaries in `scripts/run_simulator.py`
- [x] T019 [US1] Implement Jira-link failure handling to leave run incomplete, record failure, and continue remaining runs in `scripts/run_simulator.py`
- [x] T020 [US1] Add US1 validation steps and expected outputs in `specs/005-run-simulator-lifecycle/quickstart.md`

**Checkpoint**: User Story 1 delivers an end-to-end lifecycle and is demoable as MVP.

---

## Phase 4: User Story 2 - Showcase Timeline and Execution Realism (Priority: P2)

**Goal**: Produce deterministic, realistic timeline patterns with spread, overlap, and idle gaps.

**Independent Test**: Inspect timeline for a generated run in Qase and confirm fast/medium/slow durations, overlap, and at least one idle gap.

### Implementation for User Story 2

- [x] T021 [US2] Implement worker-based timeline scheduler (3-5 workers, availability tracking) in `scripts/run_simulator.py`
- [x] T022 [US2] Implement duration-bucket assignment and suite-specific duration bias in `scripts/run_simulator.py`
- [x] T023 [US2] Implement intentional idle-gap injection and overlap enforcement with at least one overlapping failed weak-suite pair when failures exist in `scripts/run_simulator.py`
- [x] T024 [US2] Implement weighted status model with weak-suite fail bias and forced-green run quota (`>=30%`) in `scripts/run_simulator.py`
- [x] T025 [US2] Implement manual/automated execution split enforcement (`>=20%` manual) in `scripts/run_simulator.py`
- [x] T026 [US2] Implement step-level result generation with non-empty `action` text (manual + automation templates) in `scripts/run_simulator.py`
- [x] T027 [US2] Implement parameterized result mapping from CSV `parameters` without synthetic params in `scripts/run_simulator.py`
- [x] T028 [US2] Implement attachment rotation strategy across run/result/step levels in `scripts/run_simulator.py`

**Checkpoint**: User Story 2 delivers convincing timeline behavior and execution realism.

---

## Phase 5: User Story 3 - Demonstrate Defect and Jira Correlation (Priority: P3)

**Goal**: Ensure failed outcomes produce realistic defect correlation while each run is linked to a unique Jira task.

**Independent Test**: Verify failed results produce ~50% inline defects, non-failed results never create defects, and every run links to exactly one newly created Jira Task.

### Implementation for User Story 3

- [x] T029 [US3] Implement failed-only inline defect rule and per-run 40-60% failed-defect band in `scripts/run_simulator.py`
- [x] T030 [US3] Implement failure-detail policy (automated failures include stacktrace, manual failures use comment) in `scripts/run_simulator.py`
- [x] T031 [US3] Implement Jira linkage integrity checks (run_id + issue key presence before completion) in `scripts/run_simulator.py`
- [x] T032 [US3] Implement per-run outcome audit summary (pass/fail/skip/manual/defect/link status) in `scripts/run_simulator.py`
- [x] T033 [US3] Persist reusable run-simulation cache/metadata in `state/run_simulator_state.json` via helper calls in `scripts/run_simulator.py`
- [x] T034 [US3] Add US3 verification guidance for defect correlation and Jira traceability in `specs/005-run-simulator-lifecycle/quickstart.md`

**Checkpoint**: User Story 3 delivers defect-to-result and run-to-Jira correlation suitable for enterprise demos.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final quality pass, documentation alignment, and operator safety checks.

- [x] T035 [P] Align Script 5 usage docs and canonical order in `README.md`
- [x] T036 [P] Refresh Milestone 3 notes for Script 5 behavior in `plan.md`
- [x] T037 Add final preflight validation and clear fatal error messages in `scripts/run_simulator.py`
- [x] T038 Run quickstart verification pass and record final expected output examples in `specs/005-run-simulator-lifecycle/quickstart.md`
- [x] T039 Add immutable-scope guard that blocks case/suite mutation operations in `scripts/run_simulator.py`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: starts immediately.
- **Phase 2 (Foundational)**: depends on Phase 1; blocks all user stories.
- **Phase 3 (US1)**: depends on Phase 2; MVP milestone.
- **Phase 4 (US2)**: depends on Phase 3 baseline lifecycle.
- **Phase 5 (US3)**: depends on Phase 3 baseline and Phase 4 result/timeline fields.
- **Phase 6 (Polish)**: depends on completion of all selected stories.

### User Story Dependencies

- **US1 (P1)**: no dependency on other stories after foundational phase.
- **US2 (P2)**: builds on US1 lifecycle plumbing but remains independently verifiable by timeline checks.
- **US3 (P3)**: builds on US1/US2 result model and remains independently verifiable by defect/Jira correlation checks.

### Within Each User Story

- Build payload/state primitives before external API calls.
- Submit results before link/complete lifecycle steps.
- Complete quickstart verification updates before closing the story.

---

## Parallel Opportunities

- **Setup**: `T003` and `T004` can run in parallel.
- **Foundational**: `T010` and `T011` can run in parallel with core foundational implementation.
- **Polish**: `T035` and `T036` can run in parallel.

---

## Parallel Example: User Story 1

```bash
# After T012 run planning is in place, these can be split across collaborators:
Task: "Implement Jira Task creation per run in scripts/run_simulator.py"   # T015
Task: "Add US1 validation steps in specs/005-run-simulator-lifecycle/quickstart.md"   # T020
```

## Parallel Example: User Story 2

```bash
# With scheduler core started, these can proceed independently:
Task: "Implement parameterized result mapping in scripts/run_simulator.py"   # T026
Task: "Implement attachment rotation strategy in scripts/run_simulator.py"   # T027
```

## Parallel Example: User Story 3

```bash
# Correlation logic and docs can progress together:
Task: "Implement per-run outcome audit summary in scripts/run_simulator.py"   # T031
Task: "Add US3 verification guidance in specs/005-run-simulator-lifecycle/quickstart.md"   # T034
```

---

## Implementation Strategy

### MVP First (US1 only)

1. Complete Phase 1 and Phase 2.
2. Complete Phase 3 (US1).
3. Validate lifecycle end-to-end in Qase and Jira.
4. Demo MVP before timeline/defect refinement.

### Incremental Delivery

1. Deliver US1 lifecycle reliability.
2. Add US2 timeline realism and status distribution controls.
3. Add US3 defect/Jira correlation depth.
4. Finish with polish/documentation consistency.

### Suggested MVP Scope

- **MVP** = through **Phase 3 (US1)** only.
- US2 and US3 are incremental enhancements for visual analytics and traceability richness.

