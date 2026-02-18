"""
Bulk-create Jira requirements (Epics + Stories) from a YAML seed file.

Security:
- Reads Jira credentials from environment variables only.
- Do NOT paste tokens into Notion or commit them to git.

Env vars:
  JIRA_BASE_URL       e.g. https://your-domain.atlassian.net
  JIRA_EMAIL          Jira account email
  JIRA_API_TOKEN      Jira API token
  JIRA_PROJECT_KEY    e.g. SHP
  JIRA_EPIC_ISSUETYPE_NAME   (optional) default: Epic
  JIRA_STORY_ISSUETYPE_NAME  (optional) default: Story
  JIRA_EPIC_NAME_FIELD_ID    (optional) override Epic Name field id
  JIRA_EPIC_LINK_FIELD_ID    (optional) override Epic Link field id (for Story -> Epic)

Usage:
  python jira_bulk_create_requirements.py discover
  python jira_bulk_create_requirements.py create --seed jira-requirements.seed.yaml
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple, Union

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover
    yaml = None


def _env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise SystemExit(f"Missing required env var: {name}")
    return value


def _env_optional(name: str) -> Optional[str]:
    value = os.environ.get(name, "").strip()
    return value or None


def _auth_header(email: str, token: str) -> str:
    raw = f"{email}:{token}".encode("utf-8")
    return "Basic " + base64.b64encode(raw).decode("ascii")


def _jira_url(base_url: str, path: str) -> str:
    return base_url.rstrip("/") + path


def _adf(text: str) -> Dict[str, Any]:
    # Minimal Atlassian Document Format (ADF) document for Jira Cloud v3.
    text = (text or "").strip()
    if not text:
        text = " "
    return {
        "type": "doc",
        "version": 1,
        "content": [
            {
                "type": "paragraph",
                "content": [{"type": "text", "text": text}],
            }
        ],
    }


def _http_json(
    method: str,
    url: str,
    headers: Dict[str, str],
    body: Optional[Dict[str, Any]] = None,
    timeout_s: int = 30,
) -> Union[Dict[str, Any], List[Any]]:
    data = None
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers = {**headers, "Content-Type": "application/json"}
    req = urllib.request.Request(url=url, method=method, data=data, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout_s) as resp:
            raw = resp.read().decode("utf-8")
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Jira API error {e.code} for {method} {url}\n{detail}") from e


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
    issuetype_names: List[str],
) -> Dict[str, Dict[str, Any]]:
    """
    Returns a mapping: issuetype_name -> fields dict.
    Fields dict: field_id -> field meta (includes name/required/schema).
    """
    # NOTE: Jira's createmeta filtering by issuetype name can be inconsistent across configs.
    # Fetch all issue types for the project, then filter in Python.
    url = _jira_url(
        base_url,
        f"/rest/api/3/issue/createmeta?projectKeys={urllib.parse.quote(project_key)}"
        f"&expand=projects.issuetypes.fields",
    )
    data = _http_json("GET", url, headers)
    if not isinstance(data, dict):
        raise SystemExit(f"Unexpected createmeta response type: {type(data)}")

    result: Dict[str, Dict[str, Any]] = {}
    projects = data.get("projects") or []
    for p in projects:
        for it in (p.get("issuetypes") or []):
            name = (it.get("name") or "").strip()
            fields = it.get("fields") or {}
            if name:
                result[name] = fields
    return result


def _find_field_id_by_name(fields: Dict[str, Any], target_name: str) -> Optional[str]:
    target = target_name.strip().lower()
    for fid, meta in fields.items():
        name = (meta.get("name") or "").strip().lower()
        if name == target:
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
    Jira's global /field list is not enough for create: a field can exist but be unavailable
    on the create screen for a given project/issue type ("Field not found"/"cannot be set").

    So we use createmeta to discover fields that are actually settable.
    """
    overrides = FieldMap(
        epic_name_field_id=_env_optional("JIRA_EPIC_NAME_FIELD_ID"),
        epic_link_field_id=_env_optional("JIRA_EPIC_LINK_FIELD_ID"),
        epic_name_required=False,
        story_parent_supported=False,
    )

    cm = _get_createmeta_fields(
        base_url,
        headers,
        project_key,
        issuetype_names=[epic_issuetype_name, story_issuetype_name],
    )

    epic_fields = cm.get(epic_issuetype_name) or {}
    story_fields = cm.get(story_issuetype_name) or {}

    epic_name_fid = overrides.epic_name_field_id or _find_field_id_by_name(epic_fields, "Epic Name")
    epic_link_fid = overrides.epic_link_field_id or _find_field_id_by_name(story_fields, "Epic Link")

    epic_name_required = False
    if epic_name_fid and epic_fields.get(epic_name_fid):
        epic_name_required = bool(epic_fields[epic_name_fid].get("required"))

    story_parent_supported = "parent" in story_fields

    return FieldMap(
        epic_name_field_id=epic_name_fid,
        epic_link_field_id=epic_link_fid,
        epic_name_required=epic_name_required,
        story_parent_supported=story_parent_supported,
    )


def bulk_create(
    base_url: str,
    headers: Dict[str, str],
    issue_updates: List[Dict[str, Any]],
) -> Dict[str, Any]:
    return _http_json(
        "POST",
        _jira_url(base_url, "/rest/api/3/issue/bulk"),
        headers,
        body={"issueUpdates": issue_updates},
    )


def load_seed(path: str) -> Dict[str, Any]:
    if yaml is None:
        raise SystemExit(
            "PyYAML is required. Install with: pip install pyyaml"
        )
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def build_epic_updates(
    project_key: str,
    field_map: FieldMap,
    epics: List[Dict[str, Any]],
    epic_issuetype_name: str,
) -> Tuple[List[Dict[str, Any]], List[str]]:
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

        # Some Jira configs require the Epic Name custom field.
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
    updates: List[Dict[str, Any]] = []

    for story in stories:
        epic_slug = str(story["epic"]).strip()
        epic_key = epic_slug_to_key.get(epic_slug)
        if not epic_key:
            raise SystemExit(f"Story references unknown epic slug: {epic_slug}")

        summary = str(story["summary"]).strip()
        description = str(story.get("description") or "").strip()
        labels = story.get("labels") or []

        fields: Dict[str, Any] = {
            "project": {"key": project_key},
            "issuetype": {"name": story_issuetype_name},
            "summary": summary,
            "description": _adf(description),
        }

        if labels:
            fields["labels"] = [str(x) for x in labels]

        # Prefer classic "Epic Link" field if present; otherwise attempt team-managed style "parent".
        if field_map.epic_link_field_id:
            fields[field_map.epic_link_field_id] = epic_key
        elif field_map.story_parent_supported:
            fields["parent"] = {"key": epic_key}
        else:
            raise SystemExit(
                "Unable to link Story -> Epic: neither 'Epic Link' nor 'parent' field is settable. "
                "Try setting JIRA_EPIC_LINK_FIELD_ID, or verify issue types for this Jira project."
            )

        updates.append({"fields": fields})

    return updates


def cmd_discover() -> int:
    base_url = _env("JIRA_BASE_URL")
    email = _env("JIRA_EMAIL")
    token = _env("JIRA_API_TOKEN")
    project_key = _env("JIRA_PROJECT_KEY")
    epic_issuetype_name = _env_optional("JIRA_EPIC_ISSUETYPE_NAME") or "Epic"
    story_issuetype_name = _env_optional("JIRA_STORY_ISSUETYPE_NAME") or "Story"

    headers = {
        "Accept": "application/json",
        "Authorization": _auth_header(email, token),
    }

    fm = discover_fields(base_url, headers, project_key, epic_issuetype_name, story_issuetype_name)
    # Print only field IDs/names; no secrets.
    print("Discovered fields:")
    print(f"- Project key: {project_key}")
    print(f"- Epic issue type name: {epic_issuetype_name}")
    print(f"- Story issue type name: {story_issuetype_name}")
    print(f"- Epic Name field id: {fm.epic_name_field_id or '(not found)'}")
    print(f"- Epic Name required: {fm.epic_name_required}")
    print(f"- Epic Link field id: {fm.epic_link_field_id or '(not found)'}")
    print(f"- Story supports parent field: {fm.story_parent_supported}")
    return 0


def cmd_create(seed_path: str) -> int:
    base_url = _env("JIRA_BASE_URL")
    email = _env("JIRA_EMAIL")
    token = _env("JIRA_API_TOKEN")
    project_key = _env("JIRA_PROJECT_KEY")
    epic_issuetype_name = _env_optional("JIRA_EPIC_ISSUETYPE_NAME") or "Epic"
    story_issuetype_name = _env_optional("JIRA_STORY_ISSUETYPE_NAME") or "Story"

    headers = {
        "Accept": "application/json",
        "Authorization": _auth_header(email, token),
    }

    fm = discover_fields(base_url, headers, project_key, epic_issuetype_name, story_issuetype_name)
    seed = load_seed(seed_path)

    epics = seed.get("epics") or []
    stories = seed.get("stories") or []

    epic_updates, epic_slugs = build_epic_updates(project_key, fm, epics, epic_issuetype_name)
    epic_resp = bulk_create(base_url, headers, epic_updates)
    created_epics = epic_resp.get("issues") or []

    if len(created_epics) != len(epic_slugs):
        # Jira may partially succeed; surface as much as possible.
        raise SystemExit(
            f"Epic creation mismatch: expected {len(epic_slugs)} issues, got {len(created_epics)}.\n"
            f"Response: {json.dumps(epic_resp, indent=2)[:4000]}"
        )

    epic_slug_to_key = {slug: issue["key"] for slug, issue in zip(epic_slugs, created_epics)}

    story_updates = build_story_updates(project_key, fm, stories, epic_slug_to_key, story_issuetype_name)
    story_resp = bulk_create(base_url, headers, story_updates) if story_updates else {"issues": []}

    print("Created epics:")
    for slug, key in epic_slug_to_key.items():
        print(f"- {slug}: {key}")

    created_stories = story_resp.get("issues") or []
    print(f"Created stories: {len(created_stories)}")
    return 0


def main(argv: List[str]) -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    sub.add_parser("discover")

    p_create = sub.add_parser("create")
    p_create.add_argument("--seed", default="jira-requirements.seed.yaml")

    args = parser.parse_args(argv)

    if args.cmd == "discover":
        return cmd_discover()
    if args.cmd == "create":
        return cmd_create(args.seed)

    raise SystemExit("Unknown command")


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

