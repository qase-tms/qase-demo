# Implementation Plan: Run Simulator Lifecycle

**Branch**: `005-run-simulator-lifecycle` | **Date**: 2026-02-27 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/005-run-simulator-lifecycle/spec.md`

## Summary

Implement `scripts/run_simulator.py` as Step 5 of 7 to generate believable present-time QA activity by creating configured run volume, submitting only existing-case results with timeline-engineered execution spread, creating and linking one Jira Task per run, injecting inline defects for a controlled portion of failures, and completing each run only after lifecycle prerequisites are met (while leaving Jira-link failures incomplete and continuing execution).

---

## Technical Context

**Language/Version**: Python 3.14 via `.venv/bin/python` only  
**Primary Dependencies**: stdlib (`json`, `csv`, `time`, `datetime`, `random`, `urllib`), shared helpers from `scripts/qase_seed_utils.py` and `scripts/jira_utils.py`  
**Storage**: `config/workspace.yaml`, `state/workspace_state.json`, `assets/seed-data/QD-2026-02-18.csv`, optional attachment hash cache in `state/`  
**Testing**: `pytest` (unit + dry-run simulation checks) and manual API smoke validation in Qase UI  
**Target Platform**: Local developer environment and GitHub Actions Linux runners  
**Project Type**: Single Python script within existing step-based automation pipeline  
**Performance Goals**: Create configured run count (default 20) with 80-120 results per run in one execution while maintaining API throttling and consistent completion  
**Constraints**: `<=5` requests/second, exponential backoff retries for recoverable errors (max 5 retries, max 60s delay), deterministic seeded output, no hardcoded IDs, no case/suite mutations, run lifecycle order must be enforced, and Jira link failures leave the run incomplete while simulation continues  
**Scale/Scope**: One Qase project, ~120 seeded cases, mixed run types (Regression/Feature/Smoke), one Jira Task per run

---

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Principle | Status |
|------|-----------|--------|
| Credentials only in env/secrets | Security | ✅ PASS — Qase/Jira auth from env only; no secrets in files |
| No hardcoded project codes or IDs | Security / Reproducibility | ✅ PASS — IDs loaded from `state/workspace_state.json` and API responses |
| API calls consult `api-index.md` first | API Reference Guidance | ✅ PASS — endpoint decisions documented in `research.md` |
| Rate limiting enforced | Technical Architecture | ✅ PASS — centralized throttled request wrapper (`<=5 req/sec`) |
| Idempotent execution model where applicable | Automation Structure | ✅ PASS — deterministic generation and safe retries; no destructive updates |
| Case/suite structure unchanged after seeding | Principle VI | ✅ PASS — script creates runs/results only |
| Realism over randomness | Principle III / IV | ✅ PASS — weighted, seeded timeline/status generation with weak-suite bias |

**Post-design re-check**: All gates hold. Design explicitly preserves fixed workspace structure and uses deterministic variability with controlled defect and timing distributions.

---

## Project Structure

### Documentation (this feature)

```text
specs/005-run-simulator-lifecycle/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── create-run.md
│   ├── create-results-bulk.md
│   ├── run-link-external-issue.md
│   ├── complete-run.md
│   └── jira-create-task.md
└── tasks.md
```

### Source Code (repository root)

```text
scripts/
├── run_simulator.py           ← NEW (this feature)
├── qase_seed_utils.py         ← state + Qase helper reuse
├── jira_utils.py              ← Jira auth/helper reuse
├── case_generator.py          ← reference for state/csv handling
└── suite_generator.py         ← reference for API throttle style

config/
└── workspace.yaml             ← simulation seed + distribution config

state/
├── workspace_state.json       ← read: project/suite/case/env/milestone/configuration IDs
└── run_simulator_state.json   ← optional: reusable attachment hashes/cache

assets/seed-data/QD-2026-02-18.csv              ← read: suite and parameter context for seeded cases
```

**Structure Decision**: Single-script implementation aligned with current step-based architecture. Supporting reusable logic stays in existing helper modules; no new package/module hierarchy is required.

---

## Complexity Tracking

No constitution violations. No justified exceptions required.
