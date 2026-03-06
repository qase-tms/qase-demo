# Feature Specification: Maintenance Script Daily Activity Feed

**Feature Branch**: `006-maintenance-script`  
**Created**: 2026-02-27  
**Status**: Draft  
**Input**: User description: "for script: maintenance.py"

## Clarifications

### Session 2026-02-27

- Q: How should overlapping maintenance triggers be handled? → A: Enforce one active cycle at a time; skip new trigger if a cycle is in progress.
- Q: What should the daily maintenance run volume be? → A: Vary between 1-6 runs per cycle, weighted toward lower counts; run on weekdays only (Mon-Fri).
- Q: Which timezone should define weekday scheduling? → A: UTC.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Keep Workspace Active Daily (Priority: P1)

As a QA workspace owner, I want a daily maintenance activity run so that the workspace continuously receives fresh realistic run activity and does not look stale.

**Why this priority**: This is the core business value of the feature and the reason the script exists.

**Independent Test**: Execute one scheduled daily maintenance cycle and verify that new runs and results are added without changing existing case or suite structure.

**Acceptance Scenarios**:

1. **Given** a seeded workspace with valid state and credentials, **When** the daily maintenance cycle executes, **Then** new run activity is added for the current day.
2. **Given** a completed daily cycle, **When** users review the workspace timeline, **Then** they can see fresh activity and outcome variation from that day.
3. **Given** a weekday trigger, **When** maintenance starts, **Then** the cycle selects between 1 and 6 runs with a distribution biased toward lower values.

---

### User Story 2 - Preserve Stable Workspace Structure (Priority: P2)

As a QA admin, I want maintenance activity to only add operational execution data so that the seeded workspace structure remains stable over time.

**Why this priority**: Structural drift breaks trust in seeded datasets and makes demos inconsistent.

**Independent Test**: Run maintenance multiple times and confirm no net change to suite and case inventory while run/result activity continues to grow.

**Acceptance Scenarios**:

1. **Given** baseline counts for suites and cases, **When** maintenance runs, **Then** suite and case counts remain unchanged while new runs/results are created.
2. **Given** prior maintenance history, **When** maintenance runs again, **Then** it appends new activity instead of mutating historical seeded entities.
3. **Given** a maintenance cycle is already running, **When** another trigger arrives, **Then** the new trigger is skipped and no overlapping cycle starts.

---

### User Story 3 - Operate Reliably With Recoverable Failures (Priority: P3)

As an operator, I want maintenance runs to continue safely even when some external actions fail so that daily activity remains dependable without manual intervention.

**Why this priority**: Reliability reduces operational overhead and keeps the workspace alive despite intermittent integration errors.

**Independent Test**: Simulate an external-link failure and verify the cycle records the issue, continues other runs, and exits with a clear outcome summary.

**Acceptance Scenarios**:

1. **Given** one run in a cycle encounters a link or external issue error, **When** maintenance continues, **Then** unaffected runs still complete and the failed run is clearly marked incomplete.
2. **Given** a maintenance cycle finishes, **When** an operator checks logs/summary output, **Then** they can identify completed vs incomplete runs and why incompletes occurred.

---

### Edge Cases

- Daily maintenance starts with missing required state keys (project, cases, environments, milestones).
- External integration is temporarily unavailable for part of the cycle.
- A daily cycle is triggered close to another execution window and must avoid duplicate or conflicting behavior.
- Attachment pool is limited or partially unavailable during a cycle.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST execute a daily maintenance simulation cycle that generates new run activity for the active workspace.
- **FR-002**: The system MUST select 1-6 runs per maintenance cycle using a low-biased weighted distribution, while allowing configurable overrides.
- **FR-003**: The system MUST create run results only from existing seeded case identifiers and MUST NOT create new suites or new cases.
- **FR-004**: The system MUST include realistic result distributions (pass/fail/skip/manual mix) with visible evidence attachments on most results.
- **FR-005**: The system MUST generate defect activity from failed execution outcomes during maintenance cycles and MUST NOT rely on a separate standalone defect-generation script.
- **FR-006**: The system MUST continue processing remaining runs when one run cannot complete due to external-link or downstream integration failure.
- **FR-007**: The system MUST produce a cycle summary reporting requested runs, completed runs, incomplete runs, and incomplete reasons.
- **FR-008**: The system MUST enforce safe rate limits for external service activity.
- **FR-009**: The system MUST support deterministic execution via configurable seed values for repeatable simulation behavior.
- **FR-010**: The system MUST support non-destructive preview mode for maintenance planning and validation without external writes.
- **FR-011**: The system MUST allow only one active maintenance cycle at a time and MUST skip overlapping triggers received during an in-progress cycle.
- **FR-012**: The system MUST execute scheduled maintenance cycles on weekdays only (Monday through Friday).
- **FR-013**: Weekday-only schedule evaluation MUST use UTC as the canonical timezone.
- **FR-014**: The default run-count weighting for values `1..6` MUST be `1:0.30, 2:0.25, 3:0.20, 4:0.12, 5:0.08, 6:0.05`.

### Key Entities *(include if feature involves data)*

- **Maintenance Cycle**: A single scheduled keep-alive execution with inputs (configuration, state, seed) and outputs (runs/results plus completion summary).
- **Operational Run**: A realistic present-time run record generated during maintenance with metadata, associated results, and completion status.
- **Result Evidence**: Attachment data associated with results (and optionally steps) used to make activity look realistic and reviewable.
- **Cycle Outcome Summary**: Aggregate counts and reason details for completed and incomplete runs in a maintenance cycle.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: On a 14-day observation window, at least 13 daily maintenance cycles complete successfully without operator intervention.
- **SC-002**: Each successful daily cycle creates new run activity on the same day, and 100% of cycles preserve existing suite and case counts.
- **SC-003**: At least 90% of generated results in maintenance cycles include visible attachment evidence.
- **SC-004**: When partial failures occur, 100% of affected cycles provide a clear incomplete reason for each incomplete run.
- **SC-005**: For default execution settings, the average maintenance cycle duration remains under 10 minutes.
- **SC-006**: Over a 4-week period, 100% of scheduled maintenance executions occur on weekdays only.
- **SC-007**: Over a 4-week period, 100% of schedule evaluations use UTC weekday boundaries.

## Assumptions

- The workspace is already bootstrapped by earlier setup scripts and contains valid seeded cases.
- Required credentials are provided through environment or secret management before execution.
- Weekday-only scheduling (Mon-Fri) is preferred for this feature scope.
- Default run-count weighting may be overridden via config for controlled tuning.
