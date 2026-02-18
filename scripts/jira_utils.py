from __future__ import annotations

import base64
import json
import os
import urllib.parse
import urllib.request
from typing import Any, Dict, List, Optional


def _env(name: str) -> str:
    value = (os.environ.get(name) or "").strip()
    if not value:
        raise SystemExit(f"Missing required env var: {name}")
    return value


def jira_auth_headers() -> Dict[str, str]:
    base_url = _env("JIRA_BASE_URL").rstrip("/")
    email = _env("JIRA_EMAIL")
    token = _env("JIRA_API_TOKEN")
    raw = f"{email}:{token}".encode("utf-8")
    auth = "Basic " + base64.b64encode(raw).decode("ascii")
    return {"Authorization": auth, "Accept": "application/json"}, base_url


def jira_search_issues(jql: str, fields: Optional[List[str]] = None, max_results: int = 100) -> List[Dict[str, Any]]:
    headers, base = jira_auth_headers()
    payload = {
        "jql": jql,
        "maxResults": max_results,
        "fields": fields or ["summary", "issuetype", "labels"],
    }
    # Jira Cloud has been removing /rest/api/3/search (410 Gone).
    # Use the enhanced search endpoint instead.
    url = base + "/rest/api/3/search/jql"
    req = urllib.request.Request(
        url,
        method="POST",
        data=json.dumps(payload).encode("utf-8"),
        headers={**headers, "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    return data.get("issues") or []


