# Research: Run Simulator Lifecycle

**Branch**: `005-run-simulator-lifecycle` | **Date**: 2026-02-27

This research resolves technical decisions for Script 5 (`run_simulator.py`) using the current spec, constitution, and in-repo API docs.

---

## R-01: Result ingestion endpoint strategy

**Decision**: Use `POST /result/{code}/{run_id}/bulk` as the primary result submission endpoint.

**Rationale**: Bulk submission supports all required result attributes in one payload (`case_id`, `status`, `start_time`, `time_ms`, `defect`, `attachments`, `stacktrace`, `comment`, `param`, `steps`, `author_id`) and is more efficient under strict rate limits.

**Alternatives considered**:
- Use `POST /result/{code}/{run_id}/results` per result — rejected due to high request count and slower execution at demo scale.
- Split runs into many tiny result calls — rejected as unnecessary complexity without user-visible value.

---

## R-02: Inline defect creation behavior

**Decision**: Set `defect=true` only for a controlled subset of failed results (~50% of failed outcomes), and always `defect=false` for passed/skipped statuses.

**Rationale**: Matches feature requirements and keeps defect volume believable while preserving clear failed-result linkage.

**Alternatives considered**:
- Defect for every failed result — rejected as too noisy and less realistic.
- Defect generation in separate script only — rejected for Script 5 because the feature requires inline result-linked defects.

---

## R-03: Run-to-Jira linking identifier format

**Decision**: Create one Jira Task per run via Jira issue create API, persist both returned issue ID and issue key, and use the issue key for `POST /run/{code}/external-issue`.

**Rationale**: Qase run external issue API expects an external issue identifier string (e.g., `PROJ-1234`). Capturing both key and internal ID keeps traceability complete while using the API-compatible linkage value.

**Alternatives considered**:
- Link run using only Jira numeric internal ID — rejected due to API contract expecting external issue identifier format.
- Reuse existing Jira issues across runs — rejected because feature requires per-run fresh Jira task context.

---

## R-04: Timeline realism model

**Decision**: Use seeded worker-scheduler simulation with duration buckets and controlled pauses:
- 3-5 workers with availability timestamps
- duration buckets: fast (200-800ms), medium (2-5s), slow (8-20s)
- explicit idle gaps (2-7s) at interval checkpoints
- overlap enforcement by assigning concurrent work to distinct workers

**Rationale**: Produces deterministic but realistic timeline visuals (concurrency + gaps + variance) instead of random timestamp noise.

**Alternatives considered**:
- Fully random start/end generation — rejected as visually artificial.
- Pure sequential execution — rejected because it cannot demonstrate concurrent bars.

---

## R-05: Weak suite bias and run pass ratio control

**Decision**: Apply weighted status generation with suite-aware bias and forced-green run selection:
- global status weights anchored to pass band
- additional fail bias for configured weak suite (`simulation.weak_suite`)
- precomputed forced-green run indexes to ensure >=30% fully passed runs

**Rationale**: Preserves dashboard storytelling (Checkout weaker) while guaranteeing required fully-passed run share.

**Alternatives considered**:
- Single static pass rate for every suite — rejected as unrealistic.
- Manual hand-picking of failed cases per run — rejected as brittle and non-scalable.

---

## R-06: Parameterized result sourcing

**Decision**: Parse parameter definitions from CSV `parameters` column and submit `param` only when source parameters exist for that case.

**Rationale**: Satisfies “do not invent parameters” requirement and keeps result payloads aligned with seeded case definitions.

**Alternatives considered**:
- Generate synthetic params for realism — rejected by requirement.
- Ignore parameters entirely — rejected because feature requires parameterized submissions when available.

---

## R-07: Step-level result content model

**Decision**: Always submit step-level results with non-empty `action` text using two rotating template pools:
- manual-style execution phrasing
- automation-style technical phrasing

**Rationale**: Qase UI requires explicit `action` text to render meaningful steps; rotating pools maintain realism without over-generation.

**Alternatives considered**:
- Reuse case step text exactly — rejected as unnecessary coupling and not required by feature.
- Submit only top-level result status — rejected because step-level visibility is mandatory.

---

## R-08: Attachment strategy

**Decision**: Reuse a small rotating hash pool for run/result/step attachments, optionally topped up by occasional `POST /attachment/{code}` uploads.

**Rationale**: Provides visible evidence artifacts without storage churn or excessive upload overhead.

**Alternatives considered**:
- New attachment per result/step — rejected as wasteful and likely to hit storage limits.
- No attachments — rejected because feature requires attachment visibility at multiple levels.

---

## R-09: Simulation run count source

**Decision**: Read `simulation.run_count` from config; if absent, default to 20 and log the fallback.

**Rationale**: Current workspace config may still include older fields (e.g., `history_months`), while the approved milestone behavior now targets 20 present-time runs.

**Alternatives considered**:
- Fail hard if `run_count` missing — rejected for poor operator experience.
- Keep using `history_months` for run volume — rejected because backdated generation is no longer valid for this feature.

