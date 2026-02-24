# Entity Identification & Uniqueness Constraints

## Test Cases
**Unique Identifier**
- Each test case has:
  - A human-readable `internal_id` (integer) unique within a project

**Project Scoping**
- Test cases are scoped to a project.

**Display Format**
- Cases are referenced as:
  - `{project_code}-{internal_id}`
  - Example: `SHOP-42`

---

## Test Runs
**Unique Identifier**
- Runs have both:
  - `id`

---

## Defects
**Unique Identifier**
- Defects have:
  - `id`

---
name
# Test Case Constraints

## Required Fields
- `title` (string, max 255 chars)
- `author_id` (int64) - automatically assumed based on the token owner

## Optional Fields
- `description` (string, nullable)
- `preconditions` (string, nullable)
- `postconditions` (string, nullable)
- `suite_id` (int64, nullable)
- `milestone_id` (int64, nullable)

## Enumerated Fields

### Status
- `ACTUAL` = 0
- `DRAFT` = 1
- `DEPRECATED` = 2

### Automation
- `NONE` = 0
- `PLANNED` = 1
- `AUTOMATED` = 2

### Severity
- `NOT_SET` = 0
- `BLOCKER` = 1
- `CRITICAL` = 2
- `MAJOR` = 3
- `NORMAL` = 4
- `MINOR` = 5
- `TRIVIAL` = 6

### Priority
- `NOT_SET` = 0
- `HIGH` = 1
- `MEDIUM` = 2
- `LOW` = 3

---

## Custom Fields
- Stored in a separate custom field table.
- Each value links to a `custom_field_id`.
- Values are stored as **strings**, regardless of field type.

---

## External Issue Links
- Test cases can link to external issues (e.g., Jira).

---

# Test Run & Result Constraints

## Run Creation
**Required**
- `project_code`
- `title`

**Optional**
- `environment_id`
- `milestone_id`
- `description`

---

## Result Status Values

### Valid Result Statuses
- `UNTESTED` = 0
- `PASSED` = 1
- `FAILED` = 2
- `BLOCKED` = 3
- `RETEST` = 4
- `SKIPPED` = 5
- `DELETED` = 6
- `IN_PROGRESS` = 7
- `INVALID` = 8

### Valid Step Statuses
- `UNTESTED`
- `PASSED`
- `FAILED`
- `BLOCKED`
- `SKIPPED`

---

## Result Required Fields
- `case_id`
- `run_id`
- `status`
- `author_id`

## Result Optional Fields
- `start_time` (datetime)
- `end_time` (datetime)
- `time_spent_ms` (integer)
- `comment` (text)
- `stacktrace` (text)
- `steps` (JSON array)

---

# Defect Constraints

## Required Fields
- `title`
- `project_code`
- `author_id`
- `status`

## Status Values
- `OPEN` = 0
- `RESOLVED` = 1
- `IN_PROGRESS` = 2
- `INVALID` = 3

**Finished Statuses**
- `RESOLVED`
- `INVALID`

---

# Hierarchical & Relational Constraints

## Suite Hierarchy
- Suites may have a `parent_id` for nesting.
- Test cases belong to suites via `suite_id`.

## Author Attribution
All entities include an `author_id`:
- Test cases
- Runs
- Results
- Defects

---

# Versioning & History

## Test Case Revisions
- Every modification creates a revision record.
- Revisions track:
  - Revision number
  - `author_id`
  - Hash
  - Diff
  - Type:
    - `CREATED`
    - `UPDATED`

---

# API-Specific Constraints

## Project Code Format
- 2–10 characters
- Alphanumeric
- Used in API paths

---

## Bulk Operations
- Bulk case creation uses a dedicated bulk payload.

---

# Key Implementation Rules

1. Always use `internal_id` for human-readable references.
2. Respect enumerated values; do not use arbitrary integers.
3. Maintain referential integrity:
   - `project_code`
   - `author_id`
   - `suite_id`
4. Use proper datetime formats.
5. Store custom field values as strings.
6. Link defects to results (primary relationship), not just test cases.