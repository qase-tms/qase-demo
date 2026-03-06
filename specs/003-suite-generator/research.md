# Research: Suite Generator

**Feature**: `003-suite-generator`
**Date**: 2026-02-20
**Consulted**: `api/get-suites.md`, `api/create-suite.md`, `api-index.md`, `scripts/jira_requirements.py`, `scripts/qase_seed_utils.py`, `constraints.md`, `.specify/memory/constitution.md`

---

## F-01 — No bulk suite creation endpoint

**Question**: Is there a bulk `POST` endpoint for suites (similar to `cases.bulk-create`)?

**Finding**: The `api-index.md` lists no bulk suite create endpoint. The only creation path is `POST /suite/{code}` (single suite). The `create-suite.md` confirms this: one suite per request, returning `{"status": true, "result": {"id": N}}`.

**Decision**: Create suites individually in two sequential passes. With 30 suites and a ≤5 req/sec rate limit, the total POST time is at most ~6 seconds of enforced sleep — well within the 60-second SC-001 target.

**Alternatives considered**: Parallel requests — rejected because the rate limit applies globally and parent IDs must be known before child suites can be created; sequential two-pass ordering is required by design.

---

## F-02 — `GET /suite/{code}` response does not include `parent_id`

**Question**: Does the `GET /suite/{code}` response include `parent_id` in the suite entity, enabling `(title, parent_id)` deduplication?

**Finding**: `api/get-suites.md` documents the suite entity as:
```json
{
  "id": 1,
  "title": "Test Suite",
  "description": "Description for Test Suite",
  "cases_count": 10,
  "created_at": "...",
  "updated_at": "..."
}
```
`parent_id` is not in the documented schema.

**Decision**: Key the idempotency map on `title` alone. This is safe for the ShopEase workspace because all 30 suite titles are globally unique within the project (verified by CSV inspection — no two rows share the same `suite` value). The implementation uses a `dict[str, int]` of `title → qase_suite_id`.

**Risk and mitigation**: If the Qase API returns `parent_id` in practice (the docs may be incomplete), the code can be upgraded to use `(title, parent_id)` as the key without any other change. The fallback of title-only matching is safe for this dataset.

**Note for future scripts**: If a project has suites with non-unique titles at different levels, title-only matching would break. This script should be re-evaluated if the suite structure changes.

---

## F-03 — `GET /suite/{code}` is paginated

**Question**: Does `GET /suite/{code}` return all suites in a single call?

**Finding**: The `SuiteListResponse` schema shows `total`, `filtered`, and `count` as separate fields, with `count: 20` in the example while `total: 100`. This confirms the endpoint is paginated with a default page size (likely 20 or 30).

**Decision**: Always request with `?limit=100` query parameter to fetch all suites in one call. With exactly 30 suites and a limit of 100, no pagination logic is needed. If the API ignores the `limit` param and returns fewer results than `total`, the implementation must loop until `len(entities) == total`. Add a safety loop for this case.

**Alternatives considered**: Pagination loop from the start — overkill for 30 suites; `limit=100` is the pragmatic default.

---

## F-04 — HTTP client pattern: `urllib.request` (no third-party HTTP library)

**Question**: Should the script use `requests`, `httpx`, or stdlib `urllib.request`?

**Finding**: `jira_requirements.py` uses `urllib.request` exclusively (no third-party HTTP library). The `qase_seed_utils.py` helper introduces no HTTP dependency. Using `requests` would add a dependency not present in the repo's other scripts.

**Decision**: Use `urllib.request` with a Qase-specific `_qase_request()` helper, mirroring the `_http_json()` pattern from `jira_requirements.py`. The rate-limiter and retry loop follow the same structure (`_MAX_RETRIES = 3`, `_RATE_INTERVAL = 0.2`).

---

## F-05 — Config YAML loading: PyYAML already used

**Question**: Is PyYAML already a dependency in this project?

**Finding**: `jira_requirements.py` imports `yaml` with a graceful fallback (`try: import yaml except: yaml = None`). The `config/workspace.yaml` file is in use by the existing workspace scripts.

**Decision**: Import PyYAML the same way (with graceful fallback and a clear startup error if missing). The `seed.cases_csv` key is read as a plain string from the `seed` section.

---

## F-06 — CSV parsing: stdlib `csv` module sufficient

**Question**: Is pandas or another CSV library needed for parsing `assets/seed-data/QD-2026-02-18.csv`?

**Finding**: Suite rows are identified by a single column filter (`suite_without_cases == "1"`) and use only four columns (`suite_id`, `suite_parent_id`, `suite`, `suite_without_cases`). No numeric aggregation, date parsing, or join operations are needed.

**Decision**: Use Python's stdlib `csv.DictReader`. Zero new dependencies.

---

## F-07 — `qase_seed_utils.save_state` provides atomic write

**Question**: Is there an existing utility for atomic state writes, or must the script implement its own temp-file rename?

**Finding**: `scripts/qase_seed_utils.py` already provides:
```python
def save_state(name: str, data: dict) -> None:
    path = _STATE_DIR / f"{name}.json"
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, indent=2), encoding="utf-8")
    tmp.replace(path)
```
`load_state(name)` complements it.

**Decision**: Use `load_state("workspace_state")` to read current state, merge `suite_ids`, then `save_state("workspace_state", merged)`. No custom atomic-write code needed.

---

## F-08 — Qase API base URL and authentication header

**Question**: What is the Qase API v1 base URL and the authentication scheme?

**Finding**: From `api/qase-api-docs.md` and the existing `qase_seed_utils.get_qase_token()` pattern, the base URL is `https://api.qase.io/v1` and authentication uses the header `Token: <QASE_API_TOKEN>`.

**Decision**: Build requests as:
```
GET  https://api.qase.io/v1/suite/{code}?limit=100
POST https://api.qase.io/v1/suite/{code}
Header: Token: <QASE_API_TOKEN>
Header: Content-Type: application/json  (POST only)
```

---

## Summary of Decisions

| # | Decision | Rationale |
|---|----------|-----------|
| F-01 | 30 individual `POST /suite/{code}` calls | No bulk endpoint exists |
| F-02 | Idempotency keyed on `title` alone | `parent_id` absent from GET response |
| F-03 | `GET /suite/{code}?limit=100` + safety pagination loop | Default page size < 30 suites |
| F-04 | `urllib.request` HTTP client | Matches repo pattern; no new deps |
| F-05 | PyYAML with graceful fallback import | Already used in jira_requirements.py |
| F-06 | stdlib `csv.DictReader` | No complex CSV operations needed |
| F-07 | `load_state` / `save_state` from `qase_seed_utils` | Atomic write utility already exists |
| F-08 | Base URL `https://api.qase.io/v1`, `Token:` header | Confirmed from api docs |
