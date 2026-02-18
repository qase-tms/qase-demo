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


def get_qase_token() -> str:
    token = (os.environ.get("QASE_API_TOKEN") or "").strip()
    if not token:
        raise SystemExit("Missing env var QASE_API_TOKEN")
    return token

