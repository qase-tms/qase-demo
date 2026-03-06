# Data Model: Suite Generator

**Feature**: `003-suite-generator`
**Date**: 2026-02-20

---

## Entities

### 1. `SuiteRow` (read from CSV)

Represents one suite-definition row extracted from `assets/seed-data/QD-2026-02-18.csv`.

| Field | Type | Source column | Constraints |
|-------|------|---------------|-------------|
| `csv_suite_id` | `str` | `suite_id` | Non-empty; unique within the CSV suite rows; used as dict key |
| `title` | `str` | `suite` | Non-empty; max 255 chars (Qase title limit); globally unique across all 30 suite rows |
| `parent_csv_id` | `str \| None` | `suite_parent_id` | Empty string → `None` (top-level); otherwise must reference a known `csv_suite_id` |
| `is_suite_row` | `bool` | `suite_without_cases` | True when value == `"1"` |

**Filter**: Only rows where `is_suite_row == True` are processed (31 such rows in the CSV; one is the header — net 30 data rows).

**Validation rule (FR-008)**: Every non-null `parent_csv_id` must appear as a `csv_suite_id` in the same filtered set. Checked before any API call.

---

### 2. `QaseSuite` (returned by / sent to Qase API)

Represents a suite object in the Qase project.

| Field | Type | Direction | Notes |
|-------|------|-----------|-------|
| `id` | `int` | Response only | Qase-assigned integer ID; stored in `SuiteIDMap` |
| `title` | `str` | Request + Response | Must match `SuiteRow.title` exactly |
| `parent_id` | `int \| None` | Request only | `None` for top-level suites; resolved from `SuiteIDMap` for children |
| `description` | `str` | Response only | Not populated by this script; ignored |
| `cases_count` | `int` | Response only | Not used by this script |

---

### 3. `SuiteIDMap` (in-memory, persisted to state)

The central mapping that links CSV identifiers to Qase identifiers.

```python
# In memory
suite_id_map: dict[str, int]
# Key:   SuiteRow.csv_suite_id  (e.g. "2", "9", "11")
# Value: QaseSuite.id           (e.g. 101, 102, 103)
```

**Built in two phases**:
- After Pass 1: contains 7 entries (top-level suites)
- After Pass 2: contains 30 entries (all suites)

**Persisted as** `suite_ids` in `state/workspace_state.json`:
```json
{
  "suite_ids": {
    "1": 101,
    "2": 102,
    "3": 103,
    ...
  }
}
```

Note: JSON keys are always strings; integer Qase IDs are stored as JSON numbers.

---

### 4. `ExistingSuitesMap` (in-memory only, from pre-fetch)

Built from the bulk `GET /suite/{code}` response at script start. Used for idempotency checking.

```python
existing_suites: dict[str, int]
# Key:   QaseSuite.title  (e.g. "01 Authentication")
# Value: QaseSuite.id     (e.g. 101)
```

**Populated once** before any `POST` call. If a `SuiteRow.title` is found in this map, its existing Qase ID is reused and no `POST` is issued.

**Design note** (from research F-02): Keyed on `title` alone because the `GET /suite/{code}` response does not include `parent_id`. Safe because all 30 ShopEase suite titles are globally unique.

---

### 5. `WorkspaceState` (read/write file)

The persistent JSON state file at `state/workspace_state.json`.

| Key | Type | Set by | Used by |
|-----|------|--------|---------|
| `project_code` | `str` | `scripts/workspace_init.py` | This script (read) |
| `custom_field_ids` | `dict` | `scripts/workspace_init.py` | Not used by this script |
| `milestone_ids` | `dict` | `scripts/workspace_init.py` | Not used by this script |
| `suite_ids` | `dict[str, int]` | This script (write) | `case_generator.py` (read) |

**Merge rule**: This script reads the full current state dict, adds/replaces only `suite_ids`, and writes the entire dict back atomically.

---

## Data Flow

```
assets/seed-data/QD-2026-02-18.csv
      │
      ▼ csv.DictReader + filter suite_without_cases == "1"
  [SuiteRow × 30]
      │
      ├── validation: all parent_csv_ids resolve ──► ERROR if orphan found
      │
      ├── dry-run path: print ordered plan, exit 0
      │
      └── live path:
            │
            ▼ GET /suite/{code}?limit=100
        ExistingSuitesMap {title → qase_id}
            │
            ├── Pass 1 (7 top-level SuiteRows)
            │     ├── title in ExistingSuitesMap → reuse id
            │     └── title not found → POST /suite/{code} → new qase_id
            │     → SuiteIDMap updated (7 entries)
            │
            └── Pass 2 (23 child SuiteRows)
                  ├── resolve parent_qase_id from SuiteIDMap
                  ├── title in ExistingSuitesMap → reuse id
                  └── title not found → POST /suite/{code} + parent_id → new qase_id
                  → SuiteIDMap updated (30 entries)
                        │
                        ▼ atomic merge write
              state/workspace_state.json  ← suite_ids added
```

---

## State Transitions

```
Script start
    │
    ├── workspace_state.json missing or no project_code → EXIT (error)
    │
    ├── CSV missing or no suite rows → EXIT (error)
    │
    ├── CSV structure invalid (orphan parent_csv_id) → EXIT (error)
    │
    └── All checks pass
          │
          ├── --dry-run → print plan → EXIT 0 (state unchanged)
          │
          └── Live run
                │
                ├── GET /suite fails (auth error, project not found) → EXIT (error, state unchanged)
                │
                ├── POST /suite fails after 3 retries → EXIT (error, state unchanged)
                │   Note: suites already created in this run remain in Qase;
                │   re-run will detect them via ExistingSuitesMap and reuse their IDs.
                │
                └── All 30 suites confirmed
                      │
                      └── atomic write → state/workspace_state.json updated
                            │
                            └── print summary → EXIT 0
```
