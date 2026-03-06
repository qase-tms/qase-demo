# Data Model: Test Case Generator

**Branch**: `004-case-generator` | **Date**: 2026-02-24

---

## Input Sources

### `assets/seed-data/QD-2026-02-18.csv` — Case Rows

Filtered by `suite_without_cases != "1"`. Exactly 120 rows.

| Column | Type | Example | Notes |
|--------|------|---------|-------|
| `id` | string (int) | `"1"` | CSV case ID — used as key in `case_ids` state map |
| `title` | string | `"Auth: Negative: Failed Registration..."` | Required; max 255 chars |
| `description` | string | `"Validates Web UI behavior..."` | Optional |
| `preconditions` | string | `"Seeded demo users exist..."` | Optional |
| `postconditions` | string | `"No persistent side effects..."` | Optional |
| `priority` | string | `"low"`, `"medium"`, `"high"` | Maps via EnumMap |
| `severity` | string | `"minor"`, `"major"`, `"critical"` | Maps via EnumMap |
| `behavior` | string | `"positive"`, `"negative"` | Maps via EnumMap |
| `type` | string | `"functional"` | Maps via EnumMap |
| `layer` | string | `"e2e"`, `"api"` | Maps via EnumMap |
| `automation` | string | `"automated"`, `"to-be-automated"`, `"is-not-automated"` | Maps via EnumMap |
| `status` | string | `"actual"` | Maps via EnumMap |
| `is_flaky` | string | `"yes"`, `"no"` | Hardcoded map → `1` / `0` integer |
| `suite_id` | string (int) | `"9"` | Leaf CSV suite ID — resolves to Qase suite ID via `suite_ids` state |
| `milestone_id` | string | `""` | Empty in all 120 rows; omitted from payload |
| `steps_actions` | string | `"1. Open ShopEase...\n2. Enter..."` | Multi-line; split + strip prefix |
| `steps_result` | string | `"1. \n2. \n3. \n"` | Often empty lines; aligned with actions |
| `steps_data` | string | `"1. \n2. \n3. \n"` | Often empty lines; aligned with actions |
| `cf_6` | string | `"Payments"` | Custom field "Component" — maps via CFOptionMap |
| `cf_7` | string | `"New user"` | Custom field "User Journey" — maps via CFOptionMap |
| `cf_8` | string | `"Low"` | Custom field "Risk" — maps via CFOptionMap |
| `cf_9` | string | `"Candidate"` | Custom field "Automation Track" — maps via CFOptionMap |
| `cf_10` | string | `"3DS required, Discount eligible"` | Custom field "Test Data Profile" — multiselect; comma-split each value → option IDs → comma-joined |

---

## Runtime Data Structures

### EnumMap

Built from `GET /system_field` at script start. Used to translate CSV string values to API integers.

```python
EnumMap = {
    "severity":   {"blocker": 1, "critical": 2, "major": 3, "normal": 4, "minor": 5, "trivial": 6},
    "priority":   {"high": 1, "medium": 2, "low": 3},
    "behavior":   {"positive": 2, "negative": 3, "destructive": 4},
    "type":       {"other": 1, "functional": 2, "smoke": 3, ...},
    "layer":      {"unknown": 0, "e2e": 1, "api": 2, "unit": 3},
    "automation": {"is-not-automated": 0, "to-be-automated": 1, "automated": 2},
    "status":     {"actual": 0, "draft": 1, "deprecated": 2},
}
# is_flaky uses a fixed map (not from system_field):
IS_FLAKY_MAP = {"no": 0, "yes": 1}
```

Keys are lowercased field titles from the API response. All lookups are case-insensitive.

### CFColumnMap

Built from `config/workspace.yaml` → `cf_column_map`. Maps CSV column names to canonical CF names.

```python
CFColumnMap = {
    "cf_6":  "Component",
    "cf_7":  "User Journey",
    "cf_8":  "Risk",
    "cf_9":  "Automation Track",
    "cf_10": "Test Data Profile",
}
```

### CFOptionMap

Built from `state/workspace_state.json` → `custom_fields.{name}.options`. Maps `(canonical_cf_name, option_title)` → option ID string.

```python
CFOptionMap = {
    "Component": {"Web UI": "1", "Backend API": "2", "Payments": "3", "Search": "4", "Admin": "5"},
    "User Journey": {"New user": "6", "Returning user": "7", "Guest": "8", "Admin": "9"},
    "Risk": {"High": "10", "Medium": "11", "Low": "12"},
    "Automation Track": {"Not automated": "13", "Candidate": "14", "Automated": "15"},
    "Test Data Profile": {"US address": "16", "EU address": "17", "Out-of-stock": "18",
                          "Discount eligible": "19", "3DS required": "20"},
}
```

### CFIDMap

Built from `state/workspace_state.json` → `custom_fields.{name}.id`. Maps canonical CF name → field ID integer.

```python
CFIDMap = {
    "Component": 221,
    "User Journey": 222,
    "Risk": 11,
    "Automation Track": 12,
    "Test Data Profile": 225,
}
```

### SuiteIDMap

Read from `state/workspace_state.json` → `suite_ids`. Maps CSV suite ID string → Qase suite ID integer.

```python
SuiteIDMap = {
    "2": 1,   # "01 Authentication"
    "9": 8,   # "Registration" (child of 2)
    ...
}
```

### LeafToRootMap

Built from CSV suite-definition rows (preflight). Maps leaf CSV suite ID → top-level suite title.

```python
LeafToRootMap = {
    "9":  "01 Authentication",   # Registration → parent 2 → root "01 Authentication"
    "11": "01 Authentication",   # Login & Sessions
    "12": "01 Authentication",   # Password Reset
    "8":  "02 Search & Browse",  # Filters & Facets
    ...
}
```

### DomainStoriesMap

Built from `state/jira_state.json` → `stories` filtered by `epic_slug`. Maps domain slug → ordered list of Jira internal IDs (as strings).

```python
DomainStoriesMap = {
    "auth":     ["10443", "10445", "10447", "10449", "10451"],
    "search":   ["10453", "10455", "10457", "10459", "10461"],
    "cart":     ["10463", "10465", "10467", ...],
    "checkout": [...],
    "orders":   [...],
    "admin":    [...],
}
```

### DomainRoundRobinCursors

One integer counter per domain slug, incremented (mod list length) each time a case from that domain is assigned a story. Advances in CSV row order.

```python
DomainRoundRobinCursors = {"auth": 0, "search": 0, "cart": 0, ...}
```

### CaseIDMap (persisted)

Written to `state/workspace_state.json` → `case_ids` after Phase 4 completes.

```python
CaseIDMap = {
    "1":   201,   # csv_id "1" → qase_case_id 201
    "2":   202,
    ...
    "120": 320,
}
```

---

## Step Object Schema

Each case's steps are built by zipping `steps_actions`, `steps_result`, `steps_data`:

```python
Step = {
    "action":          str,   # from steps_actions line (prefix stripped)
    "expected_result": str,   # from steps_result line (prefix stripped; may be empty)
    "data":            str,   # from steps_data line (prefix stripped; may be empty)
    "position":        int,   # 1-based index
}
```

Prefix-strip regex: `r"^\d+\.\s*"` — removes leading `"N. "` pattern.

---

## Bulk Create Payload Schema

```python
BulkCreatePayload = {
    "cases": [
        {
            "title":        str,           # required
            "description":  str | None,
            "preconditions": str | None,
            "postconditions": str | None,
            "priority":     int,           # from EnumMap
            "severity":     int,           # from EnumMap
            "behavior":     int,           # from EnumMap
            "type":         int,           # from EnumMap
            "layer":        int,           # from EnumMap
            "automation":   int,           # from EnumMap
            "status":       int,           # from EnumMap
            "is_flaky":     int,           # 0 or 1 (never bool)
            "suite_id":     int,           # from SuiteIDMap
            "steps":        [Step],
            "custom_field": {
                "{field_id_str}": "{option_id_str}",  # selectbox
                "{field_id_str}": "{opt1_id},{opt2_id}",  # multiselect (comma-joined)
            }
        }
    ]
}
```

**Custom field encoding example** for a case with `cf_6="Payments"`, `cf_10="3DS required, Discount eligible"`:
```python
{
    "221": "3",         # Component → Payments
    "222": "6",         # User Journey → New user
    "11":  "12",        # Risk → Low
    "12":  "14",        # Automation Track → Candidate
    "225": "20,19",     # Test Data Profile → "3DS required" + "Discount eligible"
}
```

---

## State Schema: workspace_state.json (expected post-spec-001)

```json
{
  "project_code": "HY",
  "project_id": "LR",
  "custom_fields": {
    "Component": {
      "id": 221,
      "options": { "Web UI": "1", "Backend API": "2", "Payments": "3", "Search": "4", "Admin": "5" }
    },
    "User Journey": {
      "id": 222,
      "options": { "New user": "6", "Returning user": "7", "Guest": "8", "Admin": "9" }
    },
    "Risk": {
      "id": 11,
      "options": { "High": "10", "Medium": "11", "Low": "12" }
    },
    "Automation Track": {
      "id": 12,
      "options": { "Not automated": "13", "Candidate": "14", "Automated": "15" }
    },
    "Test Data Profile": {
      "id": 225,
      "options": { "US address": "16", "EU address": "17", "Out-of-stock": "18",
                   "Discount eligible": "19", "3DS required": "20" }
    }
  },
  "suite_ids": { "2": 1, "9": 8, ... },
  "case_ids": { "1": 201, "2": 202, ... }
}
```

**Note**: The `options` sub-key per custom field is required by `case_generator.py` and MUST be written by `scripts/workspace_init.py` (spec 001). If absent, `case_generator.py` exits with a descriptive error.
