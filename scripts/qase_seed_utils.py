from __future__ import annotations

import os
import sys
from pathlib import Path


def ensure_local_qase_v1_on_path() -> None:
    """
    Use the generated Python client that lives in this repo (no pip install needed).
    """
    repo_root = Path(__file__).resolve().parents[1]
    client_src = repo_root / "qase-api-client" / "src"
    sys.path.insert(0, str(client_src))


import json
def get_qase_token() -> str:
    token = (os.environ.get("QASE_API_TOKEN") or "").strip()
    if not token:
        raise SystemExit("Missing env var QASE_API_TOKEN")
    return token

_STATE_DIR = Path(__file__).resolve().parents[1] / "state"
_STATE_DIR.mkdir(exist_ok=True)


def load_state(name: str) -> dict:
    path = _STATE_DIR / f"{name}.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def save_state(name: str, data: dict) -> None:
    """Write ``state/<name>.json`` atomically via a temp file + replace."""
    path = _STATE_DIR / f"{name}.json"
    tmp = path.with_suffix(".json.tmp")
    try:
        tmp.write_text(json.dumps(data, indent=2), encoding="utf-8")
        tmp.replace(path)
    except Exception:
        tmp.unlink(missing_ok=True)
        raise
