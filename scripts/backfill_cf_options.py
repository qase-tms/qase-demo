#!/usr/bin/env python3
"""
backfill_cf_options.py — one-time prerequisite for case_generator.py
=====================================================================
Fetches custom field option IDs from the Qase API and writes them into
``state/workspace_state.json`` under ``custom_fields.{name}.options``.

This is a stopgap until ``scripts/workspace_init.py`` (spec 001) is implemented.
Run this once before running ``case_generator.py`` if the ``options`` key
is absent from any custom field in state (the case generator will exit
immediately with a descriptive error if it finds missing options).

The Qase ``GET /custom_field/{id}`` endpoint returns option IDs in a JSON
string stored in the ``value`` field:
  "value": "[{\"id\": 1, \"title\": \"Web UI\"}, ...]"

Usage
-----
  .venv/bin/python scripts/backfill_cf_options.py
"""

import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.request

_REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
_STATE_PATH = _REPO_ROOT / "state" / "workspace_state.json"
_BASE_URL = "https://api.qase.io/v1"


def _api_get(token: str, path: str) -> dict:
    req = urllib.request.Request(
        _BASE_URL + path,
        headers={"Token": token, "Accept": "application/json"},
    )
    time.sleep(0.25)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read())
    except urllib.error.HTTPError as exc:
        body = exc.read().decode(errors="replace")
        sys.exit(f"Error: GET {path} → HTTP {exc.code}: {body}")


def main() -> None:
    token = os.environ.get("QASE_API_TOKEN", "").strip()
    if not token:
        sys.exit("Error: QASE_API_TOKEN environment variable is not set.")

    if not _STATE_PATH.exists():
        sys.exit(f"Error: {_STATE_PATH} not found. Run suite_generator.py first.")

    state = json.loads(_STATE_PATH.read_text())
    custom_fields: dict = state.get("custom_fields", {})

    if not custom_fields:
        sys.exit(
            "Error: custom_fields is empty in workspace_state.json. "
            "Run scripts/workspace_init.py first."
        )

    # Determine which fields are missing options
    missing = [name for name, cf in custom_fields.items() if "options" not in cf]
    if not missing:
        print("All custom fields already have options in state — nothing to do.")
        return

    print(f"Backfilling options for {len(missing)} field(s): {missing}")

    updated = 0
    for name in missing:
        cf_id = custom_fields[name].get("id")
        if cf_id is None:
            print(f"  SKIP {name!r}: no 'id' key in state entry")
            continue

        resp   = _api_get(token, f"/custom_field/{cf_id}")
        result = resp.get("result", {})
        raw    = result.get("value", "[]") or "[]"

        try:
            opts = json.loads(raw)
        except json.JSONDecodeError:
            print(f"  WARN {name!r}: could not parse 'value' field — skipping")
            continue

        options_map = {opt["title"]: str(opt["id"]) for opt in opts if "title" in opt and "id" in opt}
        if not options_map:
            print(f"  WARN {name!r}: API returned 0 options — skipping")
            continue

        custom_fields[name]["id"]      = cf_id
        custom_fields[name]["options"] = options_map
        print(f"  OK   {name!r} (id={cf_id}): {len(options_map)} options → {options_map}")
        updated += 1

    if updated == 0:
        print("No fields updated.")
        return

    state["custom_fields"] = custom_fields
    tmp = _STATE_PATH.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(state, indent=2))
    tmp.replace(_STATE_PATH)
    print(f"\n{updated} field(s) updated in {_STATE_PATH.relative_to(_REPO_ROOT)}.")


if __name__ == "__main__":
    main()
