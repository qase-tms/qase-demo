# Feature Specification: Realistic Run Simulation Lifecycle

**Feature Branch**: `005-run-simulator-lifecycle`  
**Created**: 2026-02-27  
**Status**: Draft  
**Input**: User description: "Implement Script 5 run simulator with realistic run lifecycle, result seeding, Jira linking, timeline engineering, and defect behavior."

## Clarifications

### Session 2026-02-27

- Q: What should be the explicit target range of results per simulated run? → A: 80-120 results/run.
- Q: If Jira Task creation/linking fails for a run after results are submitted, what should Script 5 do? → A: Leave the run incomplete, mark it failed in script output, and continue with the next run.
- Q: How strict should failure-overlap behavior be per run? → A: At least 1 overlapping failed pair in weak-suite cases per run (when failures exist).
- Q: What tolerance should apply to the “~50% of failed results create defects” rule? → A: 40-60% per run.
- Q: What should be the maximum retry policy for recoverable API failures (429/5xx)? → A: 5 retries with exponential backoff capped at 60 seconds.

## User Scenarios & Testing *(mandatory)*

<!--
  IMPORTANT: User stories should be PRIORITIZED as user journeys ordered by importance.
  Each user story/journey must be INDEPENDENTLY TESTABLE - meaning if you implement just ONE of them,
  you should still have a viable MVP (Minimum Viable Product) that delivers value.
  
  Assign priorities (P1, P2, P3, etc.) to each story, where P1 is the most critical.
  Think of each story as a standalone slice of functionality that can be:
  - Developed independently
  - Tested independently
  - Deployed independently
  - Demonstrated to users independently
-->

### User Story 1 - Seed Believable Run Activity (Priority: P1)

As a demo workspace owner, I want each simulated run to follow a complete and realistic lifecycle so stakeholders trust the workspace as representative of real QA operations.

**Why this priority**: The demo fails immediately if run activity appears synthetic or incomplete.

**Independent Test**: Can be tested by executing one simulation cycle and verifying each created run has run details, result records, external issue linkage, and a final completed state.

**Acceptance Scenarios**:

1. **Given** existing seeded cases, environments, and milestones, **When** activity simulation is executed, **Then** each run is created with a realistic title/description, associated context metadata, and a valid subset of existing cases.
2. **Given** a created run, **When** the simulation completes, **Then** the run contains only results for existing case IDs and is finalized only when Jira linking succeeds; if Jira linking fails, the run remains incomplete, the failure is logged, and processing continues with the next run.
3. **Given** the configured run volume, **When** simulation finishes, **Then** the total number of created runs matches the configured count.

---

### User Story 2 - Showcase Timeline and Execution Realism (Priority: P2)

As a product/demo presenter, I want timeline data to look like real CI execution so Qase timeline and analytics views are convincing.

**Why this priority**: Timeline realism is a primary visual proof point during demos.

**Independent Test**: Can be tested by inspecting timeline patterns from one run and confirming varied durations, overlap, and idle periods are visible.

**Acceptance Scenarios**:

1. **Given** a generated run, **When** timeline data is viewed, **Then** execution bars show fast, medium, and slow duration bands with non-uniform spread.
2. **Given** a generated run, **When** timeline data is viewed, **Then** at least one parallel execution overlap and at least one visible idle gap are present.
3. **Given** weak-risk suite coverage in a run, **When** statuses are analyzed, **Then** failure concentration is measurably higher in weak-risk areas than in other areas.

---

### User Story 3 - Demonstrate Defect and Jira Correlation (Priority: P3)

As a QA lead, I want failed executions to produce realistic defect and issue-link signals so defect correlation and traceability can be demonstrated end to end.

**Why this priority**: Linked execution, defect, and tracking records are a core enterprise demo narrative.

**Independent Test**: Can be tested by validating that failed outcomes produce a realistic split of defect behavior and that each run is linked to a unique external issue.

**Acceptance Scenarios**:

1. **Given** failed outcomes within a run, **When** simulation decides defect behavior, **Then** only failed outcomes are eligible for inline defect creation and approximately half of failed outcomes produce linked defects.
2. **Given** each generated run, **When** external linkage is reviewed, **Then** each run is associated to a newly created tracking task aligned to the run theme.
3. **Given** generated automated and manual outcomes, **When** failure details are reviewed, **Then** automated failures include technical diagnostics while manual failures include human-readable notes.

---

### Edge Cases

- Simulation config requests more results than available case IDs in scope.
- Required state inputs are present but one context map (environments or milestones) is empty.
- External issue creation succeeds but run linkage temporarily fails.
- Result timing calculation creates invalid or non-increasing timestamps.
- A run forced to be fully passed would otherwise include failed statuses from weighted selection.
- Parameterized case definitions exist for some cases but not others in the same run.
- Attachment references are unavailable for a subset of runs/results/steps.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The simulator MUST create the exact number of runs configured for simulation volume.
- **FR-002**: Each run MUST progress through a full lifecycle: created, populated with results, associated to a newly created external task, and finalized.
- **FR-003**: The simulator MUST use only pre-existing case identifiers from workspace state when creating results.
- **FR-004**: Each run MUST include a realistic theme (regression, feature, or smoke) with context-specific title and description text.
- **FR-005**: Each run MUST be assigned to valid environment and milestone identifiers sourced from workspace state.
- **FR-006**: Each run MUST include a limited, meaningful tag set (1-3 tags) relevant to run context.
- **FR-007**: Result statuses MUST include a realistic mix of passed, failed, and skipped outcomes.
- **FR-008**: At least 30% of generated runs MUST end with all outcomes passed; the remaining runs MUST include one or more non-passed outcomes.
- **FR-009**: Weak-risk suite areas MUST exhibit a lower pass trend than the overall run baseline.
- **FR-010**: At least 20% of all generated results MUST be marked as manual execution, with the remainder allowed to be automated.
- **FR-011**: Only failed outcomes are eligible for inline defect creation; passed/skipped outcomes MUST NOT create defects.
- **FR-012**: All results MUST include start and end execution times that create valid positive durations.
- **FR-013**: Timeline output within each run MUST include both concurrent execution overlap and at least one visible idle gap.
- **FR-014**: Duration distribution MUST include short, medium, and long-running executions to reflect realistic variance.
- **FR-015**: Automated failed outcomes MUST include technical diagnostic text; manual failed outcomes MUST include human-readable execution commentary.
- **FR-016**: Result records MUST include step-level execution details with non-empty step action text.
- **FR-017**: Where parameterized test definitions exist, result submissions MUST reflect those defined parameters only.
- **FR-018**: Attachments MUST be present across run, result, and selected step records at a moderate frequency without excessive volume.
- **FR-019**: The simulator MUST rotate a small reusable pool of realistic outcome comments instead of generating entirely unique verbose text for every result.
- **FR-020**: Simulation behavior MUST be deterministic for a given seed value so repeated runs produce stable distribution patterns.
- **FR-021**: Simulation activity MUST not alter case or suite structure data.
- **FR-022**: Each simulated run MUST include an execution payload targeting 80-120 results.
- **FR-023**: If Jira task creation or run-linking fails after results submission, the simulator MUST leave that run incomplete, record the failure in execution output, and continue processing subsequent runs.
- **FR-024**: For runs containing failures, the timeline MUST include at least one overlapping failed-result pair within weak-suite coverage.
- **FR-025**: For each run, defect creation over failed results MUST remain within a 40-60% band.
- **FR-026**: For recoverable API failures (`429`/`5xx`), the simulator MUST use exponential backoff with up to 5 retries and a maximum backoff delay of 60 seconds per attempt.

### Key Entities *(include if feature involves data)*

- **Simulated Run**: A generated execution cycle with theme, contextual metadata, environment, milestone, tags, and completion state.
- **Run Result**: An execution outcome for one existing case within a run, including status, execution mode (manual/automated), timing, comments, and optional defect linkage.
- **Execution Step Result**: A step-level record tied to a run result containing action text, outcome status, and optional evidence attachment.
- **External Tracking Task**: A newly created issue-tracking item linked one-to-one with each simulated run to represent work context and traceability.
- **Defect Signal**: Inline defect creation indicator attached to eligible failed outcomes for correlation reporting.
- **Timeline Segment**: A start/end interval assigned to a run result used to render overlap, gaps, and duration variance.

### Assumptions & Dependencies

- Existing workspace state files are already populated with project, case, suite, environment, and milestone mappings.
- External tracking integration credentials and permissions are valid at execution time.
- A realistic run may include only a subset of total seeded cases, and this is expected behavior.
- Reused evidence assets are acceptable for demo purposes if visual distribution remains believable.
- The weak-risk suite designation is supplied in configuration and used as the primary failure-bias target.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 100% of runs with successful Jira linking complete the full lifecycle (created, populated with results, linked to a new external task, finalized).
- **SC-002**: 100% of run results reference valid pre-seeded case IDs; 0 results are created for unknown cases.
- **SC-003**: At least 30% of runs are fully passed and at least 70% include mixed outcomes, matching planned demo distribution.
- **SC-004**: At least 90% of runs display visible timeline realism indicators (duration variance, overlap, and at least one idle gap).
- **SC-005**: The weak-risk suite shows at least a 10 percentage point lower pass rate than the overall pass rate across the simulation set.
- **SC-006**: Manual execution share is at least 20% of all results.
- **SC-007**: Defect creation occurs on 40-60% of failed outcomes and 0% of non-failed outcomes.
- **SC-008**: 100% of results include step-level records with non-empty step action text.
- **SC-009**: 100% of runs contain between 80 and 120 submitted results.
- **SC-010**: 100% of Jira-link failures are logged and left incomplete without stopping simulation of subsequent runs.
