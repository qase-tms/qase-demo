# Technical Plan: Workspace Foundation

## Overview
This plan outlines the technical approach for implementing the `scripts/workspace_init.py` script, which will automate the setup of a Qase project with predefined entities based on a `config/workspace.yaml` file. The script will be idempotent, robust, and include validation and error handling.

## Architecture & Components

### `scripts/workspace_init.py` Script
- **Main Orchestrator**: The central script responsible for parsing configuration, coordinating API calls, managing state, and performing validation.
- **Configuration Loader**: A module to load and parse `config/workspace.yaml`.
- **API Requests**: Use the ./api directory to understand the schema for Qase API and use python's standard packages to make API requests in the script.
- **State Manager**: Handles reading from and writing to `state/workspace_state.json` atomically.
- **Rate Limiter**: Ensures API requests adhere to the global rate limit (5 requests per second).
- **Error Handling & Retry Mechanism**: Implements retries for transient API errors and comprehensive logging.
- **Validation Module**: Performs pre-execution checks and post-execution verification.

### `config/workspace.yaml`
- Defines all Qase entities (project, custom fields, environments, milestones, configurations, shared steps, shared parameters) and their properties.
- Structure will mirror the Qase API's entity creation payloads for clarity.
|
### `state/workspace_state.json`
- Stores IDs of created/reused Qase entities to maintain idempotency across runs.
- Will be updated atomically.

## Detailed Steps

### 1. **Setup and Initialization**
    - **Task**: Implement argument parsing for `--dry-run` and other potential flags.
    - **Task**: Load Qase API key from environment variables or secure configuration.
    - **Task**: Initialize Qase API client.
    - **Task**: Load `config/workspace.yaml` into a structured data format.
    - **Task**: Load existing `state/workspace_state.json` if it exists, or initialize an empty state.

### 2. **Pre-execution Validation**
    - **Task**: Verify API key validity and connectivity to Qase API.
    - **Task**: Check necessary permissions for the API key (e.g., project creation, entity management).
    - **Task**: Validate `config/workspace.yaml` schema and data integrity (e.g., unique project code format).

### 3. **Project Creation/Reconciliation**
    - **Task**: Query existing Qase projects by name.
    - **Task**: If "ShopEase Web App" project exists, do NOT reuse it, but capture its `project_code` so we don't use existing project.
    - **Task**: Generate a unique 2-letter project code that is NOT any of the existing projects' codes, create the project, and capture its details.
    - **Task**: Store `project_code` in `state/workspace_state.json`.

### 4. **Custom Fields Creation/Reconciliation**
    - **Task**: For each custom field defined in `config/workspace.yaml`:
        - Query existing custom fields by name.
        - If found, reuse and update options if necessary.
        - If not found, create the custom field with its defined options.
        - Capture custom field IDs and option IDs in `state/workspace_state.json`.
    - **Consideration**: Handle various custom field types (text, selectbox, multiselect, etc.).

### 5. **Environments Creation/Reconciliation**
    - **Task**: For each environment defined in `config/workspace.yaml`:
        - Query existing environments by `slug` and `host`.
        - If found, reuse and update host if necessary.
        - If not found, create the environment.
        - Capture environment IDs in `state/workspace_state.json`.

### 6. **Milestones Creation/Reconciliation**
    - **Task**: For each milestone defined in `config/workspace.yaml`:
        - Query existing milestones by title.
        - If found, reuse.
        - If not found, create the milestone.
        - Capture milestone IDs in `state/workspace_state.json`.

### 7. **Configurations Creation/Reconciliation**
    - **Task**: For each configuration group (e.g., Browser, OS) defined in `config/workspace.yaml`:
        - Query existing configuration groups by normalized name.
        - If found, reuse and reconcile individual configuration items within the group.
        - If not found, create the group and its items.
        - Capture configuration group and item IDs in `state/workspace_state.json`.

### 8. **Shared Steps Creation/Reconciliation**
    - **Task**: For each shared step defined in `config/workspace.yaml`:
        - Query existing shared steps by title and a hash of their step sequence.
        - If found, reuse.
        - If not found, create the shared step.
        - Capture shared step hashes in `state/workspace_state.json`.

### 9. **Shared Parameters Creation/Reconciliation**
    - **Task**: For each shared parameter defined in `config/workspace.yaml`:
        - Query existing shared parameters by name.
        - If found, reuse.
        - If not found, create the shared parameter.
        - Capture shared parameter IDs in `state/workspace_state.json`.

### 10. **Post-execution Validation**
    - **Task**: Re-query all created/reconciled entities from Qase API.
    - **Task**: Verify counts of entities match expectations from `config/workspace.yaml`.
    - **Task**: Perform consistency checks (e.g., all custom field options are present).

### 11. **State File Finalization**
    - **Task**: Perform atomic write of the final `state/workspace_state.json`.

### 12. **Dry Run Mode**
    - **Task**: Ensure all API mutation calls are conditionally executed based on the `--dry-run` flag.
    - **Task**: In dry-run mode, print detailed reports of intended actions (create, reuse, update) without actual API calls.

## Error Handling & Resilience
- Implement a centralized error handling mechanism to catch and log API errors.
- Use exponential backoff for retries on transient API errors (e.g., rate limits, temporary service unavailability).
- Graceful exit on unrecoverable errors.
- Detailed logging for all operations, including successful creations/reconciliations and errors.

## Idempotency Strategy
- **Project**: Match by name. If name exists, get ID. If not, create.
- **Custom Fields**: Match by name. For options, reconcile by adding missing ones.
- **Environments**: Match by `slug` and `host`.
- **Milestones**: Match by title.
- **Configurations**: Match groups by normalized title. Reconcile items within groups.
- **Shared Steps**: Match by title and a hash of their step sequence.
- **Shared Parameters**: Match by name.

## Performance Considerations
- Implement a global rate limiter to respect Qase API limits (5 requests/second).
- Batch API calls where possible to reduce overall request count.
- Optimize queries for existing entities to minimize API calls.

## Open Questions & Risks
- **Q**: What are the exact API endpoints and payload structures for each Qase entity to be created/updated? (Will be derived from Qase API documentation/SDK)
- **Q**: How will sensitive information (e.g., API key) be securely handled (e.g., environment variables, secret management)? (Assumed environment variables for now, could integrate with more robust secret management later)
- **Risk**: Changes in Qase API schema could break the script. (Mitigation: Use Qase Python SDK and keep it updated; implement robust schema validation of `config/workspace.yaml`.)
- **Risk**: Large number of entities in `config/workspace.yaml` could lead to long execution times due to API rate limits. (Mitigation: Optimize API calls, consider parallel processing with careful rate limiting).

## Next Steps (Tasks)

1. Create `config/workspace.yaml` with initial entity definitions.
2. Set up `qaseio` Python SDK and basic API client in `scripts/workspace_init.py`.
3. Implement rate limiting and basic error handling.
4. Implement project creation/reconciliation logic.
5. Implement custom fields creation/reconciliation logic.
6. Implement environments creation/reconciliation logic.
7. Implement milestones creation/reconciliation logic.
8. Implement configurations creation/reconciliation logic.
9. Implement shared steps creation/reconciliation logic.
10. Implement shared parameters creation/reconciliation logic.
11. Implement state management (read/write `state/workspace_state.json`).
12. Implement `--dry-run` mode.
13. Implement pre-execution and post-execution validation.
14. Write comprehensive unit and integration tests.
