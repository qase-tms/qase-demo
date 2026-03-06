# Feature Specification: Workspace Foundation

**Feature Branch**: `001-workspace-foundation`
**Created**: 2026-02-18
**Status**: Draft
**Input**: Revised automation plan for `scripts/workspace_init.py`

## User Scenarios & Testing

### User Story 1 - Initialize a New Qase Project (Priority: P1)

As an internal team member,
I want to initialize a new Qase project with a unique code, essential configurations, and predefined entities
so that I can quickly set up a fully functional demo workspace without manual intervention and ensure its reproducibility.

**Why this priority**: This is the foundational step for all subsequent automation and is critical for reproducibility and efficiency.

**Independent Test**: Can be fully tested by running `scripts/workspace_init.py --dry-run` and verifying the console output against expected project details, custom fields, environments, milestones, configurations, shared steps, and shared parameters. A subsequent non-dry-run execution should complete without errors and populate Qase with the specified entities.

**Acceptance Scenarios**:

1. **Given** no existing Qase project with the name "ShopEase Web App", **When** `scripts/workspace_init.py` is run, **Then** a new Qase project with a unique 2-letter code is created, named "ShopEase Web App", and its `project_code` and `project_id` are stored in `state/workspace_state.json`.
2. **Given** existing custom fields, environments, milestones, configurations, shared steps, and shared parameters matching the `config/workspace.yaml` definitions, **When** `scripts/workspace_init.py` is run, **Then** the script reuses these existing entities, updating their options/hosts if necessary, and captures their IDs in `state/workspace_state.json`.
3. **Given** no existing custom fields, environments, milestones, configurations, shared steps, and shared parameters matching the `config/workspace.yaml` definitions, **When** `scripts/workspace_init.py` is run, **Then** the script creates all missing entities as defined in `config/workspace.yaml` and captures their IDs in `state/workspace_state.json`.
4. **Given** a successful run, **When** `scripts/workspace_init.py --dry-run` is executed, **Then** the script accurately reports all actions it would take (create/reuse) without making any API calls or modifying state.

---

## Requirements

### Functional Requirements

- **FR-001**: The script MUST query existing Qase projects to identify and select a unique 2-letter alphabetic project code for the "ShopEase Web App" project.
- **FR-002**: The script MUST idempotently create the "ShopEase Web App" project in Qase, reusing it if a project with the same name already exists.
- **FR-003**: The script MUST query existing custom fields and, for each of the five constitutional custom fields, reuse existing fields by name or create new ones if not found.
- **FR-004**: The script MUST ensure that custom field options are reconciled, adding missing options to existing fields if discrepancies are detected.
- **FR-005**: The script MUST idempotently create the six predefined environments (Staging, Production, Development, QA, UAT, Performance) from `config/workspace.yaml`.
- **FR-006**: The script MUST identify and match environments by `slug` and `host` for idempotency.
- **FR-007**: The script MUST idempotently create the three predefined milestones (Sprint 1 – Foundation, Sprint 2 – Cart & Checkout, Sprint 3 – Orders & Admin) from `config/workspace.yaml`.
- **FR-008**: The script MUST idempotently create the four predefined configuration groups (Browser, Device, OS, Network) and their items from `config/workspace.yaml`, normalizing group names for comparison.
- **FR-009**: The script MUST idempotently create the three predefined shared steps (Login with valid credentials, Add item to cart, Complete checkout with default payment) from `config/workspace.yaml`, identifying them by title and a hash of their step sequence.
- **FR-010**: The script MUST idempotently create the three predefined shared parameters (TestUserEmail, TestUserPassword, DefaultProductName) from `config/workspace.yaml`.
- **FR-011**: The script MUST store all created and reused entity IDs (project, custom fields, options, environments, milestones, configurations, shared steps, shared parameters) in `state/workspace_state.json`.- **FR-012**: The script MUST perform atomic writes to `state/workspace_state.json` by writing to a temporary file first, then renaming upon successful completion.
- **FR-013**: The script MUST enforce a global rate limit of no more than 5 API requests per second.
- **FR-014**: The script MUST include an `--dry-run` mode that performs no API mutations and only prints the intended actions.
- **FR-015**: The script MUST NOT mark created Qase entities with an ownership marker to distinguish them from manually created items.
- **FR-016**: The script MUST perform a final validation step after all creations/reconciliations to re-query entities and confirm counts match expectations before finalizing the state file.
- **FR-017**: The script MUST implement comprehensive error handling with retry mechanisms for API calls and clear logging of failures.
- **FR-018**: The script MUST implement both pre-execution validation (e.g., check API key, network connectivity, permissions) and post-execution validation (e.g., verify created entity counts, consistency checks).

### Key Entities

- **Project**: "ShopEase Web App" (created, unique 2-letter code, ID captured)
- **Custom Fields**: Component, User Journey, Risk Level, Automation Status, Test Data Profile (created/reused, IDs and option IDs captured)
- **Environments**: Staging, Production, Development, QA, UAT, Performance (created/reused, IDs captured)
- **Milestones**: Sprint 1 – Foundation, Sprint 2 – Cart & Checkout, Sprint 3 – Orders & Admin (created/reused, IDs captured)
- **Configurations**: Browser, Device, OS, Network (groups and items created/reused, IDs captured)
- **Shared Steps**: Login with valid credentials, Add item to cart, Complete checkout with default payment (created/reused, hashes captured)
- **Shared Parameters**: TestUserEmail, TestUserPassword, DefaultProductName (created/reused, IDs captured)

## Success Criteria

### Measurable Outcomes

- **SC-001**: A new Qase project for "ShopEase Web App" can be initialized from scratch in under 30 seconds (excluding API call latency) on a clean workspace.
- **SC-002**: Re-running `scripts/workspace_init.py` on an already-initialized workspace completes successfully in under 15 seconds, making no duplicate API calls.
- **SC-003**: The `state/workspace_state.json` file is accurately populated with all entity IDs and reflects the current Qase workspace state after every successful run.
- **SC-004**: The `--dry-run` mode provides a complete and accurate report of all planned API interactions without making any actual changes.
- **SC-005**: All 5 custom fields, 6 environments, 3 milestones, 4 configuration groups, 3 shared steps, and 3 shared parameters are correctly created or identified in Qase as specified by `config/workspace.yaml`.
## Clarifications

### Session 2026-02-18

- Q: How will the entities (custom fields, environments, etc.) and their properties be defined for the `scripts/workspace_init.py` script? → A: Use a dedicated YAML configuration file (`config/workspace.yaml`) to define all entities and their properties.
- Q: What level of error handling and retry mechanisms should be implemented for API interactions in `scripts/workspace_init.py`? → A: Implement comprehensive error handling with retry mechanisms for API calls and clear logging of failures.
- Q: How will the script ensure idempotency and track the IDs of created/reused entities across multiple runs? → A: Use a persistent `state/workspace_state.json` file to store and retrieve IDs and other relevant information about created/reused entities.
- Q: How will automatically created Qase entities be distinguished from manually created ones for management and cleanup purposes? → A: Do not include any special markers for automatically created entities.
- Q: What level of pre-execution and post-execution validation should be performed by `scripts/workspace_init.py`? → A: Implement both pre-execution validation (e.g., check API key, network connectivity, permissions) and post-execution validation (e.g., verify created entity counts, consistency checks).
