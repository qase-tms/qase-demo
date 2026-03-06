# Research: Workflow Orchestration and Operator Guide

**Branch**: `007-workflow-orchestration-docs` | **Date**: 2026-02-27

## Decision 1: Workflow Topology

- **Decision**: Use one parent orchestration workflow that invokes a reusable child workflow for shared execution logic.
- **Rationale**: This preserves a single operator entrypoint while avoiding duplicated job setup between initialization and maintenance paths.
- **Alternatives considered**:
  - Two independent workflows: clearer separation but duplicated logic and drift risk.
  - One monolithic workflow only: simpler file count but harder to maintain and test.

## Decision 2: Manual Initialization Sequence

- **Decision**: Manual initialization must run full chain: `workspace_init -> suite_generator -> jira_requirements(create) -> case_generator -> run_simulator`.
- **Rationale**: Produces a fully demo-ready workspace state in one operator action.
- **Alternatives considered**:
  - Bootstrap-only chain without simulator: lower runtime, but incomplete first-use experience.
  - Minimal init (`workspace_init` only): too much manual follow-up.

## Decision 3: Failure Policy for Init Chain

- **Decision**: Fail fast on first failing step, skip downstream steps, and emit remediation instructions.
- **Rationale**: Prevents partial mixed state that is expensive to recover and hard to diagnose.
- **Alternatives considered**:
  - Best-effort continuation: increases partial-state risk.
  - Retry-and-continue: can mask structural failures.

## Decision 4: State Persistence and Writeback

- **Decision**: Persist state in repository-managed `state/*.json`; workflow writebacks go to a dedicated automation/state branch.
- **Rationale**: Retains auditability and continuity while isolating state churn from default branch workflows.
- **Alternatives considered**:
  - Direct default-branch commits: simpler but risky/noisy.
  - Artifact-only retention: expiration risks breaking continuity.
  - External store: robust but adds operational overhead outside current scope.

## Decision 5: Scheduling Policy

- **Decision**: Maintenance schedule is weekdays only, UTC-based.
- **Rationale**: Aligns with constitution cadence and reduces unnecessary weekend churn.
- **Alternatives considered**:
  - 7-day schedule: higher cost/noise with limited demo value gain.
  - Manual-only maintenance: weak continuity for visual workspace health.

## Decision 6: Trigger Input Contract

- **Decision**: Manual triggers expose deterministic controls (`seed`, `run-count`/bounds, `dry-run`) with strict validation.
- **Rationale**: Balances operator flexibility with reproducibility and safety.
- **Alternatives considered**:
  - No inputs: simpler UI but inflexible operations.
  - Broad unrestricted inputs: too error-prone for first-time operators.

## Decision 7: Secrets and Token Handling

- **Decision**: Use repository-level GitHub Secrets as default for CI credentials; validate token presence before script invocation; document local verification path.
- **Rationale**: Matches existing project policy and supports straightforward onboarding.
- **Alternatives considered**:
  - Environment/org-only secrets: stronger governance, but higher setup friction not currently required.
  - Embedded config credentials: prohibited by constitution.
