"""
Jira requirement provisioning script.

Reads ``config/seeds/jira-requirements.seed.yaml`` and ``config/workspace.yaml``, creates a
Jira project (with duplicate-safe naming and key selection), bulk-creates Epics
and Stories, then persists a slug → Jira key/ID/type mapping to
``state/jira_state.json``.

Credential lookup order (highest priority first):
  1. ``--email`` / ``--token`` / ``--base-url`` CLI flags
  2. ``JIRA_EMAIL`` / ``JIRA_API_TOKEN`` / ``JIRA_BASE_URL`` environment variables
  3. Interactive prompt (when stdin is a terminal)

Usage:
  python scripts/jira_requirements.py create [--seed PATH] [--dry-run]
  python scripts/jira_requirements.py discover [--project-key KEY]

Design principles:
  - Idempotent project creation (always adds a new project; never overwrites).
  - Rate-limited (≤5 req/sec) with exponential-backoff retry on transient errors.
  - Atomic state write: temp file replaced only after all API calls succeed.
  - Fail-fast: any API error aborts before touching ``state/jira_state.json``.
"""

from __future__ import annotations

import argparse
import base64
import getpass
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from itertools import product
from pathlib import Path
from string import ascii_uppercase
from typing import Any, Dict, List, Optional, Set, Tuple, Union

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None  # type: ignore[assignment]


# ---------------------------------------------------------------------------
# Rate-limiting state  (≤5 requests/sec — matches project constitution)
# ---------------------------------------------------------------------------

_RATE_INTERVAL: float = 1.0 / 5        # 0.20 s minimum gap between requests
_last_req_ts: float = 0.0               # module-level; reset in tests via _reset_rate()
_MAX_RETRIES: int = 3
_RETRY_STATUS_CODES: frozenset = frozenset({429, 500, 502, 503, 504})


def _reset_rate() -> None:
    """Allow tests to reset the rate-limiter between runs."""
    global _last_req_ts
    _last_req_ts = 0.0


# ---------------------------------------------------------------------------
# HTTP helpers
# ---------------------------------------------------------------------------

def _auth_header(email: str, token: str) -> str:
    raw = f"{email}:{token}".encode("utf-8")
    return "Basic " + base64.b64encode(raw).decode("ascii")


def _jira_url(base_url: str, path: str) -> str:
    return base_url.rstrip("/") + path


def _adf(text: str) -> Dict[str, Any]:
    """
    Convert plain text to an Atlassian Document Format (ADF) document.

    YAML ``>`` (folded) scalars replace blank lines with a single ``\\n``,
    while ``|`` (literal) scalars keep ``\\n\\n``. We split on *any* sequence
    of one or more newlines so both scalar styles produce one ADF paragraph
    per logical paragraph, giving Jira rich multi-paragraph rendering.
    """
    import re as _re
    raw = (text or "").strip() or " "
    paragraphs = [p.strip() for p in _re.split(r"\n+", raw) if p.strip()]
    if not paragraphs:
        paragraphs = [" "]
    return {
        "type": "doc",
        "version": 1,
        "content": [
            {"type": "paragraph", "content": [{"type": "text", "text": para}]}
            for para in paragraphs
        ],
    }


class _JiraAPIError(Exception):
    """Carries the HTTP status code and raw response body from a Jira API error."""

    def __init__(self, status: int, url: str, body: str) -> None:
        super().__init__(f"Jira API error {status} for {url}")
        self.status = status
        self.url = url
        self.body = body

    def field_errors(self) -> Dict[str, str]:
        """Return the ``errors`` dict from Jira's JSON error response, or ``{}``."""
        try:
            return json.loads(self.body).get("errors") or {}
        except (json.JSONDecodeError, AttributeError):
            return {}


def _http_json(
    method: str,
    url: str,
    headers: Dict[str, str],
    body: Optional[Dict[str, Any]] = None,
    timeout_s: int = 30,
) -> Union[Dict[str, Any], List[Any]]:
    """
    Issue an HTTP request with:
      - Rate limiting: sleeps to maintain ≤5 req/sec.
      - Exponential backoff: retries up to _MAX_RETRIES on transient errors.
    Raises _JiraAPIError on non-retryable HTTP errors.
    """
    global _last_req_ts

    data: Optional[bytes] = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers = {**headers, "Content-Type": "application/json"}

    for attempt in range(1, _MAX_RETRIES + 2):
        # --- rate limiting ---
        gap = _RATE_INTERVAL - (time.monotonic() - _last_req_ts)
        if gap > 0:
            time.sleep(gap)

        req = urllib.request.Request(url=url, method=method, data=data, headers=headers)
        _last_req_ts = time.monotonic()

        try:
            with urllib.request.urlopen(req, timeout=timeout_s) as resp:
                raw = resp.read().decode("utf-8")
                return json.loads(raw) if raw.strip() else {}
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace")
            if exc.code in _RETRY_STATUS_CODES and attempt <= _MAX_RETRIES:
                backoff = 2 ** (attempt - 1)   # 1 s, 2 s, 4 s
                print(
                    f"[WARN] Jira HTTP {exc.code} on {method} {url} — "
                    f"retry {attempt}/{_MAX_RETRIES} in {backoff}s",
                    file=sys.stderr,
                )
                time.sleep(backoff)
                continue
            # Attach the parsed error body so callers can inspect field-level errors.
            raise _JiraAPIError(exc.code, url, detail) from exc

    raise _JiraAPIError(-1, url, f"Max retries ({_MAX_RETRIES}) exceeded")


# ---------------------------------------------------------------------------
# Credential acquisition  (FR-002)
# ---------------------------------------------------------------------------

def _prompt_or_env(
    env_name: str,
    cli_val: Optional[str],
    prompt_text: str,
    secret: bool = False,
) -> str:
    """
    Return the first non-empty value found in:
      cli_val  →  os.environ[env_name]  →  interactive prompt.
    Logs the source for every credential so operators can audit.
    """
    if cli_val and cli_val.strip():
        print(f"[INFO] {env_name}: sourced from CLI flag")
        return cli_val.strip()

    env_val = os.environ.get(env_name, "").strip()
    if env_val:
        print(f"[INFO] {env_name}: sourced from environment variable")
        return env_val

    if not sys.stdin.isatty():
        raise SystemExit(
            f"[ERROR] {env_name} is not set via CLI flag or environment variable, "
            "and there is no interactive terminal available."
        )

    print(f"[INFO] {env_name} not found — please enter it interactively.")
    try:
        value = (
            getpass.getpass(f"  {prompt_text}: ").strip()
            if secret
            else input(f"  {prompt_text}: ").strip()
        )
    except (EOFError, KeyboardInterrupt):
        raise SystemExit("\n[ERROR] Credential input cancelled.") from None

    if not value:
        raise SystemExit(f"[ERROR] {env_name} must not be empty.")

    print(f"[INFO] {env_name}: sourced from interactive prompt")
    return value


# ---------------------------------------------------------------------------
# Config & seed loading / validation  (FR-001, FR-003, FR-006)
# ---------------------------------------------------------------------------

def load_workspace_config(path: Union[str, Path]) -> Dict[str, Any]:
    """Load ``config/workspace.yaml`` and return its contents (or ``{}`` if absent)."""
    if yaml is None:
        raise SystemExit("PyYAML is required.  Install with: pip install pyyaml")
    p = Path(path)
    if not p.exists():
        return {}
    with open(p, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def load_seed(path: Union[str, Path]) -> Dict[str, Any]:
    """Load the requirements seed YAML, aborting if the file does not exist."""
    if yaml is None:
        raise SystemExit("PyYAML is required.  Install with: pip install pyyaml")
    p = Path(path)
    if not p.exists():
        raise SystemExit(f"[ERROR] Seed file not found: {path}")
    with open(p, "r", encoding="utf-8") as fh:
        return yaml.safe_load(fh) or {}


def validate_seed(seed: Dict[str, Any]) -> None:
    """
    Abort early when epic slugs are missing or duplicate, or when story epic
    references point to an unknown slug.  No API calls are made until this passes.
    """
    epics: List[Dict[str, Any]] = seed.get("epics") or []
    stories: List[Dict[str, Any]] = seed.get("stories") or []

    epic_slugs: List[str] = []
    for i, epic in enumerate(epics):
        slug = str(epic.get("slug") or "").strip()
        if not slug:
            raise SystemExit(f"[ERROR] Epic at index {i} is missing a 'slug' field.")
        epic_slugs.append(slug)

    dupes = {s for s in epic_slugs if epic_slugs.count(s) > 1}
    if dupes:
        raise SystemExit(f"[ERROR] Duplicate epic slugs: {sorted(dupes)}")

    epic_slug_set = set(epic_slugs)
    for i, story in enumerate(stories):
        ref = str(story.get("epic") or "").strip()
        if not ref:
            raise SystemExit(f"[ERROR] Story at index {i} is missing an 'epic' field.")
        if ref not in epic_slug_set:
            raise SystemExit(
                f"[ERROR] Story at index {i} references unknown epic slug '{ref}'. "
                f"Known slugs: {sorted(epic_slug_set)}"
            )

    print(
        f"[INFO] Seed validated: {len(epics)} epic(s), {len(stories)} story/ies. "
        "No slug problems found."
    )


# ---------------------------------------------------------------------------
# Project key & name deduplication helpers  (FR-004 / US-2)
# ---------------------------------------------------------------------------

def _all_two_letter_codes() -> List[str]:
    """Returns all 676 two-letter codes in order: AA, AB, … ZZ."""
    return [a + b for a, b in product(ascii_uppercase, repeat=2)]


def select_project_key(existing_keys: Set[str]) -> str:
    """
    Return the lexicographically first two-letter alphabetic project key that
    is not present in ``existing_keys`` (case-insensitive).
    Mirrors the ``scripts/workspace_init.py`` strategy.
    """
    upper_existing = {k.upper() for k in existing_keys}
    for code in _all_two_letter_codes():
        if code not in upper_existing:
            return code
    raise SystemExit("[ERROR] All 676 two-letter project keys are occupied.")


def _select_project_name(base_name: str, existing_names: List[str]) -> str:
    """
    If ``base_name`` (case-insensitive) already exists among ``existing_names``,
    append `` (2)``, `` (3)``, … until a unique candidate is found.
    Never reuses an existing name without a suffix.
    """
    lower_existing = {n.lower() for n in existing_names}
    if base_name.lower() not in lower_existing:
        return base_name
    n = 2
    while True:
        candidate = f"{base_name} ({n})"
        if candidate.lower() not in lower_existing:
            print(
                f"[INFO] Project name '{base_name}' already taken; "
                f"using '{candidate}'."
            )
            return candidate
        n += 1


# ---------------------------------------------------------------------------
# Jira project API helpers  (FR-004, FR-005)
# ---------------------------------------------------------------------------

def _fetch_all_projects(base_url: str, headers: Dict[str, str]) -> List[Dict[str, Any]]:
    """Page through ``/rest/api/3/project/search`` and return every project."""
    projects: List[Dict[str, Any]] = []
    start_at = 0
    page_size = 50
    while True:
        url = _jira_url(
            base_url,
            f"/rest/api/3/project/search?startAt={start_at}&maxResults={page_size}",
        )
        data = _http_json("GET", url, headers)
        values: List[Dict[str, Any]] = (data.get("values") or [])  # type: ignore[union-attr]
        projects.extend(values)
        if data.get("isLast") or len(values) < page_size:  # type: ignore[union-attr]
            break
        start_at += page_size
    return projects


def _get_my_account_id(base_url: str, headers: Dict[str, str]) -> str:
    """Return the accountId of the authenticated user (required as project lead)."""
    data = _http_json("GET", _jira_url(base_url, "/rest/api/3/myself"), headers)
    account_id = (data.get("accountId") or "") if isinstance(data, dict) else ""  # type: ignore[union-attr]
    if not account_id:
        raise SystemExit("[ERROR] Could not determine accountId from /rest/api/3/myself.")
    return str(account_id)


def _create_jira_project(
    base_url: str,
    headers: Dict[str, str],
    name: str,
    key: str,
    description: str,
) -> Dict[str, Any]:
    """POST ``/rest/api/3/project`` and return the response dict."""
    lead_account_id = _get_my_account_id(base_url, headers)
    payload: Dict[str, Any] = {
        "key": key,
        "name": name,
        "projectTypeKey": "software",
        "projectTemplateKey": "com.pyxis.greenhopper.jira:gh-scrum-template",
        "description": description,
        "leadAccountId": lead_account_id,
        "assigneeType": "UNASSIGNED",
    }
    return _http_json("POST", _jira_url(base_url, "/rest/api/3/project"), headers, body=payload)  # type: ignore[return-value]


def provision_project(
    base_url: str,
    headers: Dict[str, str],
    base_name: str,
    description: str,
    dry_run: bool,
) -> Dict[str, Any]:
    """
    Determine the final project name and key (deduplication-safe), then create
    the project.  Returns ``{"name": …, "key": …, "id": …}``.

    Handles Jira's soft-delete window: if the chosen name/key is still reserved
    by a recently-deleted project (returns 400 conflict), increments the suffix
    and retries up to 10 times with the next candidate name/key.
    """
    print("[INFO] Fetching existing Jira projects …")
    all_projects = _fetch_all_projects(base_url, headers)
    existing_names = [p["name"] for p in all_projects]
    existing_keys: Set[str] = {p["key"] for p in all_projects}

    final_name = _select_project_name(base_name, existing_names)
    final_key = select_project_key(existing_keys)

    print(f"[INFO] Target project: name='{final_name}'  key='{final_key}'")

    if dry_run:
        print(f"[DRY-RUN] Would create project '{final_name}' (key: {final_key})")
        return {"name": final_name, "key": final_key, "id": 0}

    # Retry loop: guard against soft-deleted name/key still being reserved.
    #
    # Strategy: parse the 400 field-level errors to decide what to increment.
    #  - Key conflict only  → keep name, try next key (avoids needless name suffix)
    #  - Name conflict only → keep key, try next name suffix
    #  - Both              → ban both and pick next name suffix + key
    for attempt in range(20):
        try:
            resp = _create_jira_project(base_url, headers, final_name, final_key, description)
            project_id = resp.get("id") or resp.get("projectId") or 0
            returned_key = resp.get("key") or final_key
            print(
                f"[INFO] Project created: name='{final_name}'  "
                f"key='{returned_key}'  id={project_id}"
            )
            return {"name": final_name, "key": str(returned_key), "id": int(project_id)}
        except _JiraAPIError as exc:
            if exc.status != 400:
                raise SystemExit(f"[ERROR] {exc}\n{exc.body}") from exc

            field_errs = exc.field_errors()
            key_conflict = bool(field_errs.get("projectKey"))
            name_conflict = bool(field_errs.get("projectName"))

            if not key_conflict and not name_conflict:
                # Unexpected 400 — propagate as fatal.
                raise SystemExit(f"[ERROR] {exc}\n{exc.body}") from exc

            existing_keys.add(final_key)   # always ban the tried key
            next_key = select_project_key(existing_keys)

            if name_conflict and not key_conflict:
                # The name itself is genuinely taken — increment the name suffix.
                existing_names.append(final_name)
                final_name = _select_project_name(base_name, existing_names)
                final_key = next_key
                print(
                    f"[WARN] Project name '{final_name}' is taken — "
                    f"retrying as '{final_name}' / '{final_key}'"
                )
            elif key_conflict and not name_conflict:
                # Only the key is soft-deleted; the name is still free — keep it.
                final_key = next_key
                print(
                    f"[WARN] Key '{existing_keys - {next_key} - set(p['key'] for p in all_projects)}' "
                    f"still in soft-delete hold — retrying with key '{final_key}' "
                    f"(name '{final_name}' unchanged)"
                )
            else:
                # Both fields conflict — ban the name too and increment both.
                existing_names.append(final_name)
                final_name = _select_project_name(base_name, existing_names)
                final_key = next_key
                print(
                    f"[WARN] Both name and key in conflict — "
                    f"retrying as '{final_name}' / '{final_key}'"
                )

    raise SystemExit(
        f"[ERROR] Could not create project after 20 attempts. "
        "Too many keys are in Jira's soft-delete hold. "
        "Wait a few minutes and try again."
    )


# ---------------------------------------------------------------------------
# Issue-type / field discovery  (FR-006)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class FieldMap:
    epic_name_field_id: Optional[str]
    epic_link_field_id: Optional[str]
    epic_name_required: bool
    story_parent_supported: bool


def _get_createmeta_fields(
    base_url: str,
    headers: Dict[str, str],
    project_key: str,
) -> Dict[str, Dict[str, Any]]:
    """
    Fetch ``/rest/api/3/issue/createmeta`` for ``project_key`` and return a dict
    mapping issue-type name → fields dict.
    """
    url = _jira_url(
        base_url,
        f"/rest/api/3/issue/createmeta"
        f"?projectKeys={urllib.parse.quote(project_key)}"
        f"&expand=projects.issuetypes.fields",
    )
    data = _http_json("GET", url, headers)
    if not isinstance(data, dict):
        raise SystemExit(f"[ERROR] Unexpected createmeta response type: {type(data)}")

    result: Dict[str, Dict[str, Any]] = {}
    for proj in (data.get("projects") or []):
        for it in (proj.get("issuetypes") or []):
            name = (it.get("name") or "").strip()
            if name:
                result[name] = it.get("fields") or {}
    return result


def _find_field_id_by_name(fields: Dict[str, Any], target_name: str) -> Optional[str]:
    target = target_name.strip().lower()
    for fid, meta in fields.items():
        if (meta.get("name") or "").strip().lower() == target:
            return fid
    return None


def discover_fields(
    base_url: str,
    headers: Dict[str, str],
    project_key: str,
    epic_issuetype_name: str,
    story_issuetype_name: str,
) -> FieldMap:
    """
    Use createmeta to find field IDs that are actually settable on the create screen
    (the global ``/field`` list is insufficient because a field can be unsettable for
    a given project/issue-type combination).
    Environment overrides: JIRA_EPIC_NAME_FIELD_ID, JIRA_EPIC_LINK_FIELD_ID.
    """
    cm = _get_createmeta_fields(base_url, headers, project_key)
    epic_fields = cm.get(epic_issuetype_name) or {}
    story_fields = cm.get(story_issuetype_name) or {}

    epic_name_fid: Optional[str] = (
        (os.environ.get("JIRA_EPIC_NAME_FIELD_ID") or "").strip() or None
    ) or _find_field_id_by_name(epic_fields, "Epic Name")

    epic_link_fid: Optional[str] = (
        (os.environ.get("JIRA_EPIC_LINK_FIELD_ID") or "").strip() or None
    ) or _find_field_id_by_name(story_fields, "Epic Link")

    epic_name_required = bool(
        epic_name_fid and (epic_fields.get(epic_name_fid) or {}).get("required")
    )
    story_parent_supported = "parent" in story_fields

    return FieldMap(
        epic_name_field_id=epic_name_fid,
        epic_link_field_id=epic_link_fid,
        epic_name_required=epic_name_required,
        story_parent_supported=story_parent_supported,
    )


# ---------------------------------------------------------------------------
# Issue payload builders  (FR-006)
# ---------------------------------------------------------------------------

def build_epic_updates(
    project_key: str,
    field_map: FieldMap,
    epics: List[Dict[str, Any]],
    epic_issuetype_name: str,
) -> Tuple[List[Dict[str, Any]], List[str]]:
    """Return (issueUpdates list, ordered slug list) for a bulk epic creation."""
    updates: List[Dict[str, Any]] = []
    slugs: List[str] = []
    for epic in epics:
        slug = str(epic["slug"]).strip()
        summary = str(epic["summary"]).strip()
        description = str(epic.get("description") or "").strip()

        fields: Dict[str, Any] = {
            "project": {"key": project_key},
            "issuetype": {"name": epic_issuetype_name},
            "summary": summary,
            "description": _adf(description),
        }
        if field_map.epic_name_field_id:
            fields[field_map.epic_name_field_id] = summary

        updates.append({"fields": fields})
        slugs.append(slug)

    return updates, slugs


def build_story_updates(
    project_key: str,
    field_map: FieldMap,
    stories: List[Dict[str, Any]],
    epic_slug_to_key: Dict[str, str],
    story_issuetype_name: str,
) -> List[Dict[str, Any]]:
    """Return an issueUpdates list for a bulk story creation."""
    updates: List[Dict[str, Any]] = []
    for story in stories:
        epic_slug = str(story["epic"]).strip()
        epic_key = epic_slug_to_key.get(epic_slug)
        if not epic_key:
            raise SystemExit(
                f"[ERROR] Story references unknown epic slug '{epic_slug}'. "
                "Validate your seed file."
            )

        summary = str(story["summary"]).strip()
        description = str(story.get("description") or "").strip()
        labels: List[str] = [str(x) for x in (story.get("labels") or [])]

        fields: Dict[str, Any] = {
            "project": {"key": project_key},
            "issuetype": {"name": story_issuetype_name},
            "summary": summary,
            "description": _adf(description),
        }
        if labels:
            fields["labels"] = labels

        # Team-managed (next-gen) projects expose "parent"; classic projects use "Epic Link".
        if field_map.epic_link_field_id:
            fields[field_map.epic_link_field_id] = epic_key
        elif field_map.story_parent_supported:
            fields["parent"] = {"key": epic_key}
        else:
            raise SystemExit(
                "[ERROR] Cannot link Story → Epic: neither 'Epic Link' nor 'parent' "
                "is settable.  Set JIRA_EPIC_LINK_FIELD_ID, or verify issue types."
            )

        updates.append({"fields": fields})

    return updates


# ---------------------------------------------------------------------------
# Bulk creation with response validation  (FR-006 / T011)
# ---------------------------------------------------------------------------

def validated_bulk_create(
    base_url: str,
    headers: Dict[str, str],
    issue_updates: List[Dict[str, Any]],
    label: str,
    dry_run: bool,
) -> List[Dict[str, Any]]:
    """
    POST ``/rest/api/3/issue/bulk`` and verify that Jira returned exactly
    ``len(issue_updates)`` issues.  Aborts (without touching state) if the
    counts differ.  In dry-run mode returns synthetic stubs.
    """
    if dry_run:
        print(f"[DRY-RUN] Would bulk-create {len(issue_updates)} {label}(s)")
        return [{"key": f"DRY-{label.upper()[:3]}-{i + 1}", "id": str(i)} for i in range(len(issue_updates))]

    print(f"[INFO] Bulk-creating {len(issue_updates)} {label}(s) …")
    resp = _http_json(
        "POST",
        _jira_url(base_url, "/rest/api/3/issue/bulk"),
        headers,
        body={"issueUpdates": issue_updates},
    )
    created: List[Dict[str, Any]] = (resp.get("issues") or []) if isinstance(resp, dict) else []  # type: ignore[union-attr]

    if len(created) != len(issue_updates):
        raise SystemExit(
            f"[ERROR] {label.capitalize()} creation mismatch: "
            f"requested {len(issue_updates)}, Jira returned {len(created)}.\n"
            f"Full response (truncated):\n{json.dumps(resp, indent=2)[:3000]}"
        )

    print(f"[INFO] {label.capitalize()}s created: {len(created)}")
    return created


# ---------------------------------------------------------------------------
# Story slug generation  (FR-007 / T016)
# ---------------------------------------------------------------------------

def _story_slug(epic_slug: str, idx: int) -> str:
    """
    Generate a stable, namespaced story slug.
    ``idx`` is 1-based position within the epic.
    Example: epic_slug='auth', idx=3  →  'auth-3'
    """
    return f"{epic_slug}-{idx}"


# ---------------------------------------------------------------------------
# Mapping builder  (FR-007 / T016)
# ---------------------------------------------------------------------------

def build_jira_state(
    project: Dict[str, Any],
    epic_slugs: List[str],
    created_epics: List[Dict[str, Any]],
    stories_seed: List[Dict[str, Any]],
    created_stories: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """
    Build the complete ``jira_state`` dict.  Story slugs are namespaced as
    ``{epic_slug}-{n}`` (1-based index per epic) to guarantee uniqueness.
    """
    epics_map: Dict[str, Any] = {}
    for slug, issue in zip(epic_slugs, created_epics):
        epics_map[slug] = {
            "jira_key": issue["key"],
            "jira_id": int(issue["id"]),
            "issue_type": "Epic",
        }

    # Track per-epic counters to generate deterministic story indices.
    epic_counters: Dict[str, int] = {}
    stories_map: Dict[str, Any] = {}
    for story_seed, issue in zip(stories_seed, created_stories):
        epic_slug = str(story_seed["epic"]).strip()
        epic_counters[epic_slug] = epic_counters.get(epic_slug, 0) + 1
        slug = _story_slug(epic_slug, epic_counters[epic_slug])
        stories_map[slug] = {
            "jira_key": issue["key"],
            "jira_id": int(issue["id"]),
            "issue_type": "Story",
            "epic_slug": epic_slug,
            "summary": str(story_seed.get("summary") or "").strip(),
        }

    return {
        "project": project,
        "epics": epics_map,
        "stories": stories_map,
    }


# ---------------------------------------------------------------------------
# Atomic state write  (FR-007 / T017)
# ---------------------------------------------------------------------------

def write_jira_state(
    state_dir: Union[str, Path],
    state: Dict[str, Any],
    dry_run: bool,
) -> None:
    """
    Write ``state/jira_state.json`` atomically: serialize to a ``.tmp`` file,
    then call ``Path.replace()`` (atomic on POSIX, near-atomic on Windows).
    The previous file is left untouched until the write succeeds.
    """
    state_path = Path(state_dir) / "jira_state.json"

    if dry_run:
        print(f"[DRY-RUN] Would write mapping to {state_path}")
        print(
            f"[DRY-RUN] Preview — "
            f"{len(state['epics'])} epic(s), {len(state['stories'])} story/ies"
        )
        print(json.dumps(state, indent=2))
        return

    Path(state_dir).mkdir(parents=True, exist_ok=True)
    tmp_path = state_path.with_suffix(".json.tmp")
    try:
        tmp_path.write_text(json.dumps(state, indent=2), encoding="utf-8")
        tmp_path.replace(state_path)
    except Exception as exc:
        tmp_path.unlink(missing_ok=True)
        raise SystemExit(f"[ERROR] Could not write {state_path}: {exc}") from exc

    print(f"[INFO] Mapping written → {state_path}")
    print(
        f"[INFO] Summary: {len(state['epics'])} epic(s) and "
        f"{len(state['stories'])} story/ies persisted."
    )


# ---------------------------------------------------------------------------
# Sub-commands
# ---------------------------------------------------------------------------

def cmd_create(args: argparse.Namespace) -> int:
    """Provision a Jira project + all epics/stories from the seed file."""
    try:
        return _cmd_create_inner(args)
    except _JiraAPIError as exc:
        raise SystemExit(f"[ERROR] Jira API error {exc.status}: {exc.body[:500]}") from exc


def _cmd_create_inner(args: argparse.Namespace) -> int:
    # ── credentials ────────────────────────────────────────────────────────
    base_url = _prompt_or_env(
        "JIRA_BASE_URL",
        getattr(args, "base_url", None),
        "Jira base URL (e.g. https://yourorg.atlassian.net)",
    )
    email = _prompt_or_env(
        "JIRA_EMAIL",
        getattr(args, "email", None),
        "Jira account email",
    )
    token = _prompt_or_env(
        "JIRA_API_TOKEN",
        getattr(args, "token", None),
        "Jira API token",
        secret=True,
    )

    headers = {"Accept": "application/json", "Authorization": _auth_header(email, token)}
    dry_run: bool = args.dry_run

    # ── config + seed ───────────────────────────────────────────────────────
    repo_root = Path(__file__).resolve().parents[1]
    ws_cfg = load_workspace_config(repo_root / "config" / "workspace.yaml")
    project_cfg = ws_cfg.get("project") or {}
    # --project-name CLI flag takes priority over config/workspace.yaml.
    cli_project_name = (getattr(args, "project_name", None) or "").strip()
    base_name: str = cli_project_name or str(project_cfg.get("name") or "ShopEase Requirements").strip()
    description: str = str(project_cfg.get("description") or "").strip()
    if cli_project_name:
        print(f"[INFO] Project name overridden via --project-name: '{base_name}'")

    seed = load_seed(args.seed)
    validate_seed(seed)

    epics: List[Dict[str, Any]] = seed.get("epics") or []
    stories: List[Dict[str, Any]] = seed.get("stories") or []

    epic_issuetype = (os.environ.get("JIRA_EPIC_ISSUETYPE_NAME") or "Epic").strip()
    story_issuetype = (os.environ.get("JIRA_STORY_ISSUETYPE_NAME") or "Story").strip()

    # ── project creation ────────────────────────────────────────────────────
    project = provision_project(base_url, headers, base_name, description, dry_run)
    project_key = project["key"]

    # ── field discovery ─────────────────────────────────────────────────────
    if dry_run:
        print("[DRY-RUN] Skipping field discovery in dry-run mode")
        fm = FieldMap(
            epic_name_field_id=None,
            epic_link_field_id=None,
            epic_name_required=False,
            story_parent_supported=True,
        )
    else:
        print("[INFO] Discovering issue fields via createmeta …")
        fm = discover_fields(base_url, headers, project_key, epic_issuetype, story_issuetype)
        print(
            f"[INFO] Fields found: "
            f"epic_name={fm.epic_name_field_id or '(none)'}  "
            f"epic_link={fm.epic_link_field_id or '(none)'}  "
            f"story_parent={fm.story_parent_supported}"
        )

    # ── bulk create epics ───────────────────────────────────────────────────
    epic_updates, epic_slugs = build_epic_updates(project_key, fm, epics, epic_issuetype)
    created_epics = validated_bulk_create(base_url, headers, epic_updates, "epic", dry_run)

    if not dry_run:
        for slug, issue in zip(epic_slugs, created_epics):
            print(f"[INFO] Epic: {slug} → {issue['key']} (id={issue['id']})")

    epic_slug_to_key = {slug: issue["key"] for slug, issue in zip(epic_slugs, created_epics)}

    # ── bulk create stories ─────────────────────────────────────────────────
    story_updates = build_story_updates(
        project_key, fm, stories, epic_slug_to_key, story_issuetype
    )
    created_stories = validated_bulk_create(
        base_url, headers, story_updates, "story", dry_run
    )

    # ── build mapping and persist ───────────────────────────────────────────
    state = build_jira_state(project, epic_slugs, created_epics, stories, created_stories)
    write_jira_state(repo_root / "state", state, dry_run)

    print(
        f"\n[INFO] Done.  "
        f"project={project_key!r}  "
        f"epics={len(created_epics)}  "
        f"stories={len(created_stories)}"
    )
    return 0


def cmd_discover(args: argparse.Namespace) -> int:
    """Print discoverable Jira field IDs for an existing project."""
    try:
        return _cmd_discover_inner(args)
    except _JiraAPIError as exc:
        raise SystemExit(f"[ERROR] Jira API error {exc.status}: {exc.body[:500]}") from exc


def _cmd_discover_inner(args: argparse.Namespace) -> int:
    base_url = _prompt_or_env(
        "JIRA_BASE_URL",
        getattr(args, "base_url", None),
        "Jira base URL (e.g. https://yourorg.atlassian.net)",
    )
    email = _prompt_or_env(
        "JIRA_EMAIL",
        getattr(args, "email", None),
        "Jira account email",
    )
    token = _prompt_or_env(
        "JIRA_API_TOKEN",
        getattr(args, "token", None),
        "Jira API token",
        secret=True,
    )

    project_key = (
        getattr(args, "project_key", None)
        or (os.environ.get("JIRA_PROJECT_KEY") or "")
    ).strip()
    if not project_key:
        raise SystemExit(
            "[ERROR] --project-key (or JIRA_PROJECT_KEY env var) is required for 'discover'."
        )

    epic_issuetype = (os.environ.get("JIRA_EPIC_ISSUETYPE_NAME") or "Epic").strip()
    story_issuetype = (os.environ.get("JIRA_STORY_ISSUETYPE_NAME") or "Story").strip()

    headers = {"Accept": "application/json", "Authorization": _auth_header(email, token)}
    fm = discover_fields(base_url, headers, project_key, epic_issuetype, story_issuetype)

    print(f"Project key            : {project_key}")
    print(f"Epic issue type        : {epic_issuetype}")
    print(f"Story issue type       : {story_issuetype}")
    print(f"Epic Name field id     : {fm.epic_name_field_id or '(not found)'}")
    print(f"Epic Name required     : {fm.epic_name_required}")
    print(f"Epic Link field id     : {fm.epic_link_field_id or '(not found)'}")
    print(f"Story parent supported : {fm.story_parent_supported}")
    return 0


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def _add_credential_args(p: argparse.ArgumentParser) -> None:
    p.add_argument(
        "--base-url", dest="base_url", default=None,
        help="Jira base URL (overrides JIRA_BASE_URL env var)",
    )
    p.add_argument(
        "--email", default=None,
        help="Jira account email (overrides JIRA_EMAIL env var)",
    )
    p.add_argument(
        "--token", default=None,
        help="Jira API token (overrides JIRA_API_TOKEN env var)",
    )


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Provision Jira epics/stories from config/seeds/jira-requirements.seed.yaml",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  python scripts/jira_requirements.py create --dry-run\n"
            "  python scripts/jira_requirements.py create --seed config/seeds/jira-requirements.seed.yaml\n"
            "  python scripts/jira_requirements.py discover --project-key AB\n"
        ),
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_discover = sub.add_parser("discover", help="Print discoverable Jira field IDs")
    _add_credential_args(p_discover)
    p_discover.add_argument(
        "--project-key", dest="project_key", default=None,
        help="Existing Jira project key (overrides JIRA_PROJECT_KEY env var)",
    )

    p_create = sub.add_parser("create", help="Create Jira project + issues from seed")
    _add_credential_args(p_create)
    p_create.add_argument(
        "--seed", default="config/seeds/jira-requirements.seed.yaml",
        help="Path to requirements seed YAML (default: config/seeds/jira-requirements.seed.yaml)",
    )
    p_create.add_argument(
        "--project-name", dest="project_name", default=None,
        help="Override the Jira project name (skips config/workspace.yaml lookup and "
             "suffix auto-increment; a unique key is still chosen automatically)",
    )
    p_create.add_argument(
        "--dry-run", action="store_true",
        help="Simulate without making any Jira API mutations",
    )

    args = parser.parse_args(argv)

    if args.cmd == "discover":
        return cmd_discover(args)
    if args.cmd == "create":
        return cmd_create(args)

    raise SystemExit("Unknown command")


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
