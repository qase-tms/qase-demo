# Research: Test Case Generator

**Branch**: `004-case-generator` | **Date**: 2026-02-24

All findings below were derived by inspecting `api-index.md`, the API doc files in `api/`, the live `state/workspace_state.json`, `state/jira_state.json`, `config/workspace.yaml`, `assets/seed-data/QD-2026-02-18.csv`, and the reference implementation `scripts/suite_generator.py`.

---

## F-01: Custom Field Option IDs — Not Present in Current State

**Decision**: `case_generator.py` reads custom field option IDs from `state/workspace_state.json` under `custom_fields.{name}.options: {option_name: option_id}`. If this key is absent, the script exits with a descriptive error.

**Rationale**: The Qase API does not expose option IDs in any documented response — `GET /custom_field` (list) and `GET /custom_field/{id}` (single) return field metadata but no option IDs. The only reliable source is the `scripts/workspace_init.py` create response, which `scripts/workspace_init.py` (spec 001) is responsible for capturing and persisting. `case_generator.py` therefore declares a hard dependency on the post-spec-001 state schema.

**Alternatives considered**:
- Query option IDs at runtime from `GET /custom_field` — rejected: option IDs not present in documented response.
- Hardcode option IDs — rejected: violates constitution reproducibility principle and the `constraints.md` rule.
- Use option names directly as string values — rejected: Qase bulk-create `custom_field` map requires numeric option IDs as strings.

**Impact on spec-001**: `scripts/workspace_init.py` MUST persist options in the following shape:
```json
"custom_fields": {
  "Component": {
    "id": 221,
    "options": { "Web UI": "1", "Backend API": "2", "Payments": "3", "Search": "4", "Admin": "5" }
  },
  "User Journey": { "id": 222, "options": { "New user": "6", ... } },
  "Risk": { "id": 11, "options": { "High": "...", "Medium": "...", "Low": "..." } },
  "Automation Track": { "id": 12, "options": { "Not automated": "...", "Candidate": "...", "Automated": "..." } },
  "Test Data Profile": { "id": 225, "options": { "US address": "...", "EU address": "...", ... } }
}
```
**Note**: Custom field names in `config/workspace.yaml` and `workspace_state.json` are `"Risk"` and `"Automation Track"` — NOT `"Risk Level"` / `"Automation Status"` as in the older plan.md example. The `cf_column_map` in `config/workspace.yaml` is the canonical source.

---

## F-02: jira_state.json — Actual Schema vs Plan.md Example

**Decision**: `case_generator.py` reads Jira story assignments from `jira_state.stories`, filtering by `epic_slug`, NOT from flat `story_ids`/`epic_ids` keys.

**Rationale**: The actual `jira_state.json` produced by `jira_requirements.py` uses the following structure:
```json
{
  "epics": {
    "auth": { "jira_key": "AF-1", "jira_id": 10436 },
    ...
  },
  "stories": {
    "auth-1": { "jira_key": "AF-7", "jira_id": 10443, "epic_slug": "auth", "summary": "..." },
    "auth-2": { "jira_key": "AF-8", "jira_id": 10445, "epic_slug": "auth", "summary": "..." },
    ...
  }
}
```

To build the domain story list for a domain slug (e.g., `"auth"`): filter `stories` entries where `epic_slug == domain_slug`, collect `jira_key` values (e.g., `"AF-7"`) in insertion order for use as the Jira external issue ID in the attach call.

**Empirical correction (production run)**: The original design specified using the numeric `jira_id` (e.g., `"10443"`) as the external issue identifier. This was incorrect. The Qase API returns HTTP 400 "The links.0.external_issues.0 format is invalid." for numeric strings. Only the Jira issue key (e.g., `"AF-7"`) is accepted. This was verified by testing both formats against the live API.

**Alternatives considered**:
- Use `jira_id` numeric string (e.g., `"10443"`) — rejected (empirically): Qase API returns HTTP 400 for this format.
- Use flat `story_ids`/`epic_ids` structure — rejected: actual jira_state.json uses the richer nested structure shown above.

---

## F-03: Attach External Issue — Batch Capability

**Decision**: Batch up to 30 case links per `POST /case/{code}/external-issue/attach` call, using the `links[]` array.

**Rationale**: The `POST /case/{code}/external-issue/attach` endpoint (documented in `api/case-attach-external-issue.md`) accepts a `links` array of `{case_id: int, external_issues: [string]}` objects in a single request. Batching 30 per call reduces link-pass API calls from 120 to 4, significantly reducing elapsed time and rate-limit exposure.

Request shape:
```json
{
  "type": "jira-cloud",
  "links": [
    { "case_id": 201, "external_issues": ["AF-7"] },
    { "case_id": 202, "external_issues": ["AF-8"] }
  ]
}
```

**Alternatives considered**:
- One API call per case link — rejected: 120 separate calls is wasteful when batching is available.
- One single call with all 120 links — rejected: unknown server-side limit; 30 is safe and consistent with bulk-create batch size.

---

## F-04: Link Idempotency — Detection via `include=external_issues`

**Decision**: Use `GET /case/{code}?limit=100&include=external_issues` (paginated) at the start of the link pass to build a `linked_case_ids` set. Cases in this set are skipped in the link pass.

**Rationale**: `GET /case/{code}` with `include=external_issues` returns an `external_issues` array per case entity (documented in `api/get-cases.md`). Cases with a non-empty `external_issues` list are considered already linked. This single paginated preflight replaces per-case GET calls, requiring only 2 API calls (offset 0 and 100) instead of 120.

**Alternatives considered**:
- Per-case GET before each link call — rejected: 120 API calls; too slow and rate-limit heavy.
- Unconditional attach and accept API rejection — rejected: no documented idempotency guarantee on attach; spec FR-012 requires GET-before-POST.
- Track linked IDs in a separate state key — rejected: requires more complex state schema; the existing case response already carries this information.

---

## F-05: System Fields — Runtime Enum Map

**Decision**: Call `GET /system_field` once at script start to build a runtime enum map keyed by field name (lowercased).

**Rationale**: `GET /system_field` (documented in `api/get-system-fields.md`) returns all system fields with their options `{id: int, title: string}`. This eliminates hardcoded integers and respects any workspace-level customisation, as required by FR-005.

Expected response snippet:
```json
{
  "result": [
    { "id": 1, "title": "severity", "options": [{ "id": 1, "title": "blocker" }, ...] },
    { "id": 2, "title": "priority", "options": [{ "id": 1, "title": "high" }, ...] }
  ]
}
```

CSV enum strings observed (from `assets/seed-data/QD-2026-02-18.csv`):
| Field | CSV values |
|---|---|
| priority | `high`, `medium`, `low` |
| severity | `critical`, `major`, `minor` |
| behavior | `positive`, `negative` |
| automation | `automated`, `to-be-automated`, `is-not-automated` |
| layer | `e2e`, `api` |
| status | `actual` |
| is_flaky | `yes`, `no` (converted to `1`/`0` integer — not via system_field) |

`is_flaky` uses a hardcoded map `{"yes": 1, "no": 0}` since it is a boolean integer field, not a system-field enum. The system field query covers the remaining 6 fields.

---

## F-06: Step Parsing — Empty Lines and Alignment

**Decision**: Strip numbered prefix (`"N. "`) from each line, zip `steps_actions`/`steps_result`/`steps_data` by position, drop only leading and trailing empty-action lines; submit remaining steps (including those with empty result/data) as step objects with `position` set to 1-based index.

**Rationale**: Inspection of the CSV shows:
- `steps_actions`: substantive content (e.g., `"1. Open ShopEase and go to Sign up\n2. ..."`)
- `steps_result`: mostly empty lines (`"1. \n2. \n3. \n4. \n"`)
- `steps_data`: mostly empty lines (same pattern)

All 120 case rows have non-empty `steps_actions`. Steps must stay aligned across all three columns — if `steps_actions` has 4 lines, the other two must also contribute 4 positions. Empty `expected_result` and `data` values are valid per the API schema (both are `string|null`). Leading/trailing blank-action lines (after prefix stripping) are dropped to avoid phantom steps.

---

## F-07: Bulk Create Response — ID Ordering

**Decision**: Preserve strict insertion order of the `cases[]` batch array. Map `result.ids[i]` to `csv_case_id[i]` by zip-index.

**Rationale**: `POST /case/{code}/bulk` returns `{ "result": { "ids": [int, ...] } }` where IDs are in the same order as the input cases array. The script must build each batch as an ordered list of `(csv_id, case_payload)` pairs, then zip `csv_ids` against `result.ids` to produce the case_id_map entries.

---

## F-08: Suite Domain Lookup for Leaf Suite Cases

**Decision**: Pre-build a `leaf_to_root_title` map from CSV suite rows by walking parent chains. Used to resolve each case's domain slug for Jira story assignment.

**Rationale**: CSV case rows carry `suite_id` pointing to a **leaf** suite (e.g., suite_id=9 = "Registration", parent=2 = "01 Authentication"). The `suite_domain_map` in `config/workspace.yaml` keys on TOP-LEVEL suite titles. Since ShopEase suites are only 2 levels deep (root → leaf), the lookup is: `leaf_suite_id → parent_suite_id → root_suite_title`. The map is built from the suite-definition rows in the same CSV preflight pass used to validate `suite_ids`.

---

## F-09: Jira Integration Type

**Decision**: Use `"jira-cloud"` as the fixed integration type for the attach-external-issue call.

**Rationale**: The constitution mandates Jira Cloud REST API v3. The `case-attach-external-issue.md` documents `"jira-cloud"` as the appropriate type. No other type is relevant for this project.
