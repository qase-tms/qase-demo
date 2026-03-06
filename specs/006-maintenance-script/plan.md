# Implementation Plan: Maintenance Script Daily Activity Feed

**Branch**: `006-maintenance-script` | **Date**: 2026-02-27 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/006-maintenance-script/spec.md`

## Summary

Implement `scripts/maintenance.py` as an operational keep-alive simulation that appends realistic weekday activity to the existing workspace by creating a weighted low-volume run set (1-6, biased low), submitting result evidence for most outcomes, enforcing non-overlapping execution, and preserving fixed seeded structure (no suite/case mutation).

---

## Technical Context

**Language/Version**: Python 3.14 via `.venv/bin/python` only  
**Primary Dependencies**: Python stdlib (`argparse`, `json`, `random`, `time`, `datetime`, `urllib`), `PyYAML`, shared helpers from `scripts/qase_seed_utils.py`, `scripts/jira_utils.py`, and lifecycle logic from `scripts/run_simulator.py`  
**Storage**: `config/workspace.yaml`, `state/workspace_state.json`, `state/run_simulator_state.json`, optional `state/maintenance_state.json`, and `assets/seed-data/QD-2026-02-18.csv`  
**Testing**: Dry-run CLI verification, live smoke execution in Qase/Jira, and targeted failure-path checks (overlap skip, partial external failures)  
**Target Platform**: Local macOS/Linux developer shell and GitHub Actions Linux runners  
**Project Type**: Single-repository step-based automation script  
**Performance Goals**: Complete default daily cycle within 10 minutes while creating 1-6 runs and preserving API reliability  
**Constraints**: `<=5` req/sec throttling, deterministic seeded behavior, weekday-only UTC schedule, skip overlapping triggers, no suite/case creation, no hardcoded IDs/secrets, evidence on >=90% results, default run-count weights `1:0.30, 2:0.25, 3:0.20, 4:0.12, 5:0.08, 6:0.05`  
**Scale/Scope**: One workspace project, ~120 seeded cases, weekday cadence, low tactical activity volume

---

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Principle | Status |
|------|-----------|--------|
| Credentials only in env/secrets | Security | ✅ PASS — tokens remain environment/secret sourced only |
| No hardcoded project codes or IDs | Security / Reproducibility | ✅ PASS — all IDs loaded from state and runtime API responses |
| API calls consult `api-index.md` first | API Reference Guidance | ✅ PASS — endpoint usage captured in `research.md` and contracts |
| Rate limiting enforced | Technical Architecture | ✅ PASS — centralized throttle remains required (`<=5 req/sec`) |
| Case count/suite structure fixed post-seeding | Principle VI | ✅ PASS — maintenance only appends runs/results/defect outcomes |
| Deterministic variability | Principle IV | ✅ PASS — seeded weighted volume and result generation |
| Scheduled cadence alignment | Principle V / Activity Simulation Rules | ✅ PASS — weekday-only daily UTC cadence aligned with constitution |

**Post-design re-check**: All gates remain satisfied; no exceptions required.

---

## Project Structure

### Documentation (this feature)

```text
specs/006-maintenance-script/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   ├── create-maintenance-run.md
│   ├── create-maintenance-results-bulk.md
│   ├── create-maintenance-jira-task.md
│   ├── link-maintenance-run-external-issue.md
│   └── complete-maintenance-run.md
└── tasks.md
```

### Source Code (repository root)

```text
scripts/
├── maintenance.py              ← NEW (this feature)
├── run_simulator.py            ← reused lifecycle primitives and payload patterns
├── qase_seed_utils.py          ← state helper reuse
└── jira_utils.py               ← Jira auth/helper reuse

config/
└── workspace.yaml              ← maintenance volume/seed/schedule config

state/
├── workspace_state.json        ← read: project/case/env/milestone IDs
├── run_simulator_state.json    ← read/write: evidence attachment hash pool
└── maintenance_state.json      ← NEW optional lock/last-cycle metadata

.github/workflows/
└── daily-activity.yml          ← weekday UTC schedule trigger
```

**Structure Decision**: Keep implementation in the existing single-project, step-based script architecture; add one dedicated maintenance script and minimal state extension for overlap safety.

---

## Complexity Tracking

No constitution violations. No justified exceptions required.
