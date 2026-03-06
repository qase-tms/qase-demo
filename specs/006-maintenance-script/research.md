# Research: Maintenance Script Daily Activity Feed

**Branch**: `006-maintenance-script` | **Date**: 2026-02-27

This research resolves implementation decisions for `maintenance.py` based on the approved feature spec and constitution constraints.

---

## R-01: Overlap handling policy

**Decision**: Enforce a single active maintenance cycle; if another trigger arrives while one is active, skip the new cycle and log a skip reason.

**Rationale**: Prevents duplicate activity bursts, conflicting writes, and noisy analytics while preserving deterministic cadence.

**Alternatives considered**:
- Queue overlapping cycle for immediate follow-up — rejected because it can create bursty back-to-back activity.
- Allow parallel cycles — rejected due to duplication/conflict risk.

---

## R-02: Daily volume selection

**Decision**: Choose run volume from range `1-6` using a low-biased weighted distribution.

**Rationale**: Satisfies tactical keep-alive requirement while avoiding unrealistic daily spikes.

**Alternatives considered**:
- Fixed run count per day — rejected as too mechanical.
- Uniform random `1-6` — rejected because it overproduces high days relative to intent.

---

## R-03: Weekday schedule boundary

**Decision**: Evaluate weekday eligibility in UTC and run only Monday through Friday.

**Rationale**: UTC avoids daylight-saving drift and gives deterministic scheduler behavior across environments.

**Alternatives considered**:
- Local timezone weekdays — rejected for ambiguity across environments.
- Configurable timezone defaulting local — rejected due to added complexity for limited value.

---

## R-04: Run lifecycle endpoint strategy

**Decision**: Reuse existing lifecycle sequence for each maintenance run:
1) create run, 2) submit results in bulk, 3) create Jira task, 4) link external issue, 5) complete run.

**Rationale**: Preserves proven behavior from `run_simulator.py` and keeps traceability rich for each run.

**Alternatives considered**:
- Skip Jira linkage during maintenance — rejected because it weakens enterprise traceability storytelling.
- Complete runs before link — rejected due to lifecycle integrity requirement.

---

## R-05: Defect activity policy

**Decision**: Generate defect activity only from failed results in maintenance runs; no standalone defect stream.

**Rationale**: Aligns with current direction to remove `defect_generator.py` and keeps defects causally tied to execution failures.

**Alternatives considered**:
- Standalone synthetic defects — rejected by scope change.
- Defect on all failed results — rejected as too noisy and less realistic.

---

## R-06: Evidence attachment coverage

**Decision**: Enforce attachment presence on most maintenance results (target >=90%), with optional step-level evidence.

**Rationale**: Improves demo realism and directly satisfies measurable spec outcome.

**Alternatives considered**:
- Opportunistic sparse attachments — rejected as inconsistent with acceptance target.
- Attachments on every step of every result — rejected due to overhead/noise.

---

## R-07: Failure tolerance behavior

**Decision**: Continue cycle execution after per-run external failures (Jira create/link), mark affected runs incomplete with reason, and emit aggregate summary.

**Rationale**: Preserves operational continuity and supports unattended weekday scheduling.

**Alternatives considered**:
- Fail entire cycle on first downstream error — rejected as brittle.
- Ignore failures silently — rejected due to poor observability.

---

## R-08: State model for maintenance execution lock

**Decision**: Persist minimal cycle metadata in `state/maintenance_state.json` (last start/end timestamps, active-cycle marker, last status).

**Rationale**: Enables overlap guard and operator diagnostics without mutating seeded workspace state.

**Alternatives considered**:
- In-memory lock only — rejected because scheduler retries and process restarts would bypass protection.
- External lock service — rejected as unnecessary complexity for this scope.
