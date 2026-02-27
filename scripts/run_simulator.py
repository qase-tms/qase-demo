from __future__ import annotations

import argparse
import csv
import json
import math
import os
import random
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4

import yaml

from jira_utils import jira_auth_headers
from qase_seed_utils import get_qase_token, load_state, save_state


QASE_BASE_URL = "https://api.qase.io/v1"
RATE_INTERVAL_SECONDS = 0.2  # <= 5 req/sec
MAX_RETRIES = 5
MAX_BACKOFF_SECONDS = 60.0
DEFAULT_RUN_COUNT = 20
DEFAULT_MIN_CASES_PER_RUN = 80
DEFAULT_MAX_CASES_PER_RUN = 120
DEFAULT_ATTACHMENT_HASH = "950a99059f21f1852033c4153b035136"

ALLOWED_MUTATING_PREFIXES = (
    "/run/",
    "/result/",
    "/attachment/",
)

STATUS_PASSED = "passed"
STATUS_FAILED = "failed"
STATUS_SKIPPED = "skipped"


class SimulationError(RuntimeError):
    pass


class RateLimiter:
    def __init__(self, min_interval_seconds: float) -> None:
        self._min_interval = min_interval_seconds
        self._last_request_ts = 0.0

    def wait(self) -> None:
        now = time.monotonic()
        elapsed = now - self._last_request_ts
        if elapsed < self._min_interval:
            time.sleep(self._min_interval - elapsed)
        self._last_request_ts = time.monotonic()


def _read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise SimulationError(f"Required JSON file not found: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def _read_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise SimulationError(f"Required YAML file not found: {path}")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SimulationError(f"Expected YAML object at root: {path}")
    return data


def _read_csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise SimulationError(f"CSV file not found: {path}")
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def _assert_safe_mutating_path(path: str) -> None:
    if not path.startswith(ALLOWED_MUTATING_PREFIXES):
        raise SimulationError(f"Blocked mutating endpoint path by immutable scope guard: {path}")


def _build_multipart_file_payload(filename: str, content: bytes) -> tuple[bytes, str]:
    boundary = f"----qase-boundary-{uuid4().hex}"
    body = bytearray()
    body.extend(f"--{boundary}\r\n".encode("utf-8"))
    body.extend(
        f'Content-Disposition: form-data; name="file[]"; filename="{filename}"\r\n'.encode("utf-8")
    )
    body.extend(b"Content-Type: text/plain\r\n\r\n")
    body.extend(content)
    body.extend(b"\r\n")
    body.extend(f"--{boundary}--\r\n".encode("utf-8"))
    return bytes(body), boundary


def _http_json(
    method: str,
    url: str,
    headers: dict[str, str],
    *,
    body: bytes | None = None,
    limiter: RateLimiter | None = None,
    retry_on: tuple[int, ...] = (429, 500, 502, 503, 504),
) -> dict[str, Any]:
    attempt = 0
    last_error: Exception | None = None
    while attempt <= MAX_RETRIES:
        if limiter is not None:
            limiter.wait()
        req = urllib.request.Request(url=url, method=method, headers=headers, data=body)
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                raw = resp.read()
                if not raw:
                    return {"status": True}
                return json.loads(raw.decode("utf-8"))
        except urllib.error.HTTPError as exc:
            status = exc.code
            payload = exc.read().decode("utf-8", errors="replace")
            if status in retry_on and attempt < MAX_RETRIES:
                backoff = min(MAX_BACKOFF_SECONDS, 2**attempt)
                print(f"[WARN] HTTP {status} on {method} {url}; retrying in {backoff:.1f}s")
                time.sleep(backoff)
                attempt += 1
                last_error = exc
                continue
            raise SimulationError(f"{method} {url} failed with HTTP {status}: {payload}") from exc
        except urllib.error.URLError as exc:
            if attempt < MAX_RETRIES:
                backoff = min(MAX_BACKOFF_SECONDS, 2**attempt)
                print(f"[WARN] URL error on {method} {url}; retrying in {backoff:.1f}s")
                time.sleep(backoff)
                attempt += 1
                last_error = exc
                continue
            raise SimulationError(f"{method} {url} failed after retries: {exc}") from exc
    raise SimulationError(f"Request failed after retries: {last_error}")


def _qase_json_request(
    method: str,
    path: str,
    token: str,
    limiter: RateLimiter,
    *,
    payload: dict[str, Any] | None = None,
) -> dict[str, Any]:
    if method.upper() != "GET":
        _assert_safe_mutating_path(path)
    url = QASE_BASE_URL + path
    headers = {
        "Token": token,
        "Accept": "application/json",
    }
    body: bytes | None = None
    if payload is not None:
        headers["Content-Type"] = "application/json"
        body = json.dumps(payload).encode("utf-8")
    return _http_json(method.upper(), url, headers, body=body, limiter=limiter)


def _qase_upload_attachment(
    project_code: str,
    token: str,
    limiter: RateLimiter,
    filename: str,
    content: bytes,
) -> list[str]:
    _assert_safe_mutating_path("/attachment/")
    multipart_body, boundary = _build_multipart_file_payload(filename, content)
    url = QASE_BASE_URL + f"/attachment/{urllib.parse.quote(project_code)}"
    headers = {
        "Token": token,
        "Accept": "application/json",
        "Content-Type": f"multipart/form-data; boundary={boundary}",
    }
    resp = _http_json("POST", url, headers, body=multipart_body, limiter=limiter)
    result = resp.get("result") or []
    hashes: list[str] = []
    for item in result:
        if isinstance(item, dict):
            h = item.get("hash")
            if isinstance(h, str) and h:
                hashes.append(h)
    return hashes


def _jira_create_task(
    summary: str,
    description: str,
    labels: list[str],
    limiter: RateLimiter,
) -> dict[str, str]:
    headers, base_url = jira_auth_headers()
    jira_project_key = str((os.environ.get("JIRA_PROJECT_KEY") or "").strip())
    if not jira_project_key:
        raise SimulationError("Missing required env var: JIRA_PROJECT_KEY")
    payload = {
        "fields": {
            "project": {"key": jira_project_key},
            "issuetype": {"name": "Task"},
            "summary": summary,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [{"type": "text", "text": description}],
                    }
                ],
            },
            "labels": labels,
        }
    }
    url = base_url + "/rest/api/3/issue"
    body = json.dumps(payload).encode("utf-8")
    resp = _http_json(
        "POST",
        url,
        {**headers, "Content-Type": "application/json"},
        body=body,
        limiter=limiter,
    )
    issue_id = str(resp.get("id") or "")
    issue_key = str(resp.get("key") or "")
    if not issue_id or not issue_key:
        raise SimulationError(f"Jira issue create response missing id/key: {resp}")
    return {"id": issue_id, "key": issue_key}


def _load_templates(path: Path) -> dict[str, Any]:
    if path.exists():
        data = _read_yaml(path)
        if isinstance(data, dict):
            return data
    return {
        "run_titles": {
            "Regression": [
                "Regression - Sprint 3 Checkout Stabilization",
                "Regression - Release Candidate Validation",
                "Regression - Cart and Checkout Reliability Sweep",
            ],
            "Feature": [
                "Feature Validation - 3DS Payment Flow",
                "Feature Validation - Guest Checkout Address Rules",
                "Feature Validation - Cart Merge Duplication Fix",
            ],
            "Smoke": [
                "Smoke - Post Deployment Production Check",
                "Smoke - Pre-Release Critical Path",
                "Smoke - Hotfix Verification Pass",
            ],
        },
        "run_descriptions": {
            "Regression": [
                "Covers broad suite scope after payment and checkout reliability changes.",
                "Validates regressions across authentication, cart, checkout, and orders after merge.",
            ],
            "Feature": [
                "Targets a focused feature area impacted by current sprint change scope.",
                "Verifies feature behavior under realistic data and execution mix.",
            ],
            "Smoke": [
                "Confirms critical user journeys remain stable after a deployment event.",
                "Exercises high-risk happy-path and key guardrail checks.",
            ],
        },
        "result_comments": [
            "Observed expected behavior under current build and environment settings.",
            "Execution matched acceptance criteria with no additional side effects.",
            "Behavior aligned with expected outcome; no regression indicators found.",
            "Result indicates intermittent instability under realistic execution timing.",
            "Validation completed with environment-specific observations captured.",
        ],
        "tags": [
            "regression",
            "checkout",
            "release-candidate",
            "hotfix",
            "stability",
            "payments",
            "critical-path",
            "smoke",
            "feature-validation",
        ],
        "manual_step_actions": [
            "Open the application and navigate to the target workflow",
            "Execute the user action sequence with provided test data",
            "Review expected outcome and capture any visible mismatch",
        ],
        "auto_step_actions": [
            "Launch browser context and navigate to scenario entry point",
            "Execute workflow action through automated control path",
            "Assert expected response and telemetry signals",
        ],
    }


def _load_timeline_profile(path: Path) -> dict[str, Any]:
    if path.exists():
        data = _read_yaml(path)
        if isinstance(data, dict):
            return data
    return {
        "worker_range": [3, 5],
        "duration_buckets_ms": {
            "fast": [200, 800],
            "medium": [2000, 5000],
            "slow": [8000, 20000],
        },
        "idle_gap_ms": [2000, 7000],
        "gap_frequency": 0.2,
    }


def _parse_params(raw: str) -> dict[str, str] | None:
    txt = (raw or "").strip()
    if not txt:
        return None
    if txt.startswith("{") and txt.endswith("}"):
        try:
            parsed = json.loads(txt)
            if isinstance(parsed, dict):
                return {str(k): str(v) for k, v in parsed.items()}
        except json.JSONDecodeError:
            pass
    pairs: dict[str, str] = {}
    for chunk in txt.replace("|", ";").split(";"):
        chunk = chunk.strip()
        if not chunk:
            continue
        sep = ":" if ":" in chunk else "=" if "=" in chunk else None
        if not sep:
            continue
        key, value = chunk.split(sep, 1)
        key = key.strip()
        value = value.strip()
        if key and value:
            pairs[key] = value
    return pairs or None


def _build_suite_tree(csv_rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    suites: dict[str, dict[str, str]] = {}
    for row in csv_rows:
        suite_id = (row.get("suite_id") or "").strip()
        if not suite_id:
            continue
        suites[suite_id] = {
            "title": (row.get("suite") or "").strip(),
            "parent_id": (row.get("suite_parent_id") or "").strip(),
        }
    return suites


def _resolve_root_suite_title(suite_id: str, suites: dict[str, dict[str, str]]) -> str:
    current = suite_id
    visited: set[str] = set()
    while current and current in suites and current not in visited:
        visited.add(current)
        parent = suites[current].get("parent_id") or ""
        if not parent:
            return suites[current].get("title") or "Unknown Suite"
        current = parent
    return suites.get(suite_id, {}).get("title", "Unknown Suite")


def _is_weak_case(case_ctx: dict[str, Any], weak_suite_title: str) -> bool:
    return case_ctx.get("root_suite_title") == weak_suite_title


def _pick_duration_ms(
    rng: random.Random,
    profile: dict[str, Any],
    root_suite_title: str,
) -> int:
    buckets = profile["duration_buckets_ms"]
    if root_suite_title.startswith("01 Authentication") or root_suite_title.startswith("07 Admin"):
        lo, hi = buckets["fast"]
        return rng.randint(int(lo), int(max(hi, lo)))
    if root_suite_title.startswith("04 Checkout"):
        lo, hi = buckets["slow"]
        return rng.randint(int(lo), int(max(hi, lo)))
    roll = rng.random()
    if roll < 0.4:
        lo, hi = buckets["fast"]
    elif roll < 0.8:
        lo, hi = buckets["medium"]
    else:
        lo, hi = buckets["slow"]
    return rng.randint(int(lo), int(max(hi, lo)))


def _pick_status(
    rng: random.Random,
    is_weak: bool,
    force_green: bool,
) -> str:
    if force_green:
        return STATUS_PASSED
    pass_weight = 0.85
    fail_weight = 0.12
    skip_weight = 0.03
    if is_weak:
        pass_weight = max(0.0, pass_weight - 0.15)
        fail_weight = min(1.0, fail_weight + 0.15)
    roll = rng.random()
    if roll < pass_weight:
        return STATUS_PASSED
    if roll < pass_weight + fail_weight:
        return STATUS_FAILED
    return STATUS_SKIPPED


def _build_steps(
    rng: random.Random,
    is_autotest: bool,
    status: str,
    templates: dict[str, Any],
    attachment_hashes: list[str],
) -> list[dict[str, Any]]:
    actions = (
        templates.get("auto_step_actions", []) if is_autotest else templates.get("manual_step_actions", [])
    )
    if not actions:
        actions = ["Execute step action", "Observe expected behavior", "Record execution outcome"]
    steps: list[dict[str, Any]] = []
    for idx, action in enumerate(actions[:3], start=1):
        step_status = STATUS_PASSED
        if status == STATUS_FAILED and idx == 2:
            step_status = STATUS_FAILED
        elif status == STATUS_SKIPPED:
            step_status = STATUS_SKIPPED
        step: dict[str, Any] = {
            "position": idx,
            "status": step_status,
            "action": action,
            "comment": "Step executed by simulator.",
        }
        if attachment_hashes and rng.random() < 0.7:
            step["attachments"] = [rng.choice(attachment_hashes)]
        steps.append(step)
    return steps


def _ensure_manual_ratio(rng: random.Random, entries: list[dict[str, Any]], min_ratio: float = 0.2) -> None:
    target_manual = int(math.ceil(len(entries) * min_ratio))
    current_manual = sum(1 for item in entries if not item["is_autotest"])
    while current_manual < target_manual:
        idx = rng.randrange(0, len(entries))
        if entries[idx]["is_autotest"]:
            entries[idx]["is_autotest"] = False
            current_manual += 1


def _enforce_defect_ratio(rng: random.Random, entries: list[dict[str, Any]]) -> None:
    failed_idxs = [i for i, e in enumerate(entries) if e["status"] == STATUS_FAILED]
    for i in failed_idxs:
        entries[i]["defect"] = False
    if not failed_idxs:
        return
    lo = int(math.floor(len(failed_idxs) * 0.4))
    hi = int(math.ceil(len(failed_idxs) * 0.6))
    lo = max(1, lo)
    hi = max(lo, hi)
    choose_n = rng.randint(lo, hi)
    chosen = set(rng.sample(failed_idxs, k=min(choose_n, len(failed_idxs))))
    for i in failed_idxs:
        entries[i]["defect"] = i in chosen


def _enforce_failed_overlap(
    rng: random.Random,
    entries: list[dict[str, Any]],
    weak_suite_title: str,
) -> None:
    weak_failed = [
        e for e in entries if e["status"] == STATUS_FAILED and e.get("root_suite_title") == weak_suite_title
    ]
    if len(weak_failed) < 2:
        return
    first, second = rng.sample(weak_failed, 2)
    second["start_time"] = first["start_time"]
    min_duration = min(int(first["time_ms"]), int(second["time_ms"]))
    if min_duration < 1200:
        first["time_ms"] = max(1200, int(first["time_ms"]))
        second["time_ms"] = max(1200, int(second["time_ms"]))


def _generate_run_results(
    rng: random.Random,
    case_contexts: list[dict[str, Any]],
    weak_suite_title: str,
    force_green: bool,
    profile: dict[str, Any],
    templates: dict[str, Any],
    attachment_hashes: list[str],
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    workers_min, workers_max = profile.get("worker_range", [3, 5])
    workers = max(2, rng.randint(int(workers_min), int(workers_max)))
    now_sec = int(time.time())
    worker_available = [now_sec for _ in range(workers)]
    entries: list[dict[str, Any]] = []
    idle_gap_used = False

    for idx, case_ctx in enumerate(case_contexts):
        if idx > 0 and idx % max(10, len(case_contexts) // 4) == 0:
            if rng.random() < float(profile.get("gap_frequency", 0.2)):
                gap_lo, gap_hi = profile.get("idle_gap_ms", [2000, 7000])
                gap_sec = rng.randint(int(gap_lo), int(gap_hi)) // 1000
                worker_available = [t + gap_sec for t in worker_available]
                idle_gap_used = True

        worker_idx = min(range(workers), key=lambda i: worker_available[i])
        start_time = worker_available[worker_idx]
        duration_ms = _pick_duration_ms(rng, profile, case_ctx["root_suite_title"])
        end_time = start_time + max(1, duration_ms // 1000)
        worker_available[worker_idx] = end_time

        is_weak = _is_weak_case(case_ctx, weak_suite_title)
        status = _pick_status(rng, is_weak, force_green)
        is_autotest = rng.random() < 0.8

        comment_pool = templates.get("result_comments", [])
        comment = rng.choice(comment_pool) if comment_pool else "Execution completed by simulation."

        entry: dict[str, Any] = {
            "case_id": case_ctx["qase_case_id"],
            "status": status,
            "start_time": start_time,
            "time_ms": duration_ms,
            "is_autotest": is_autotest,
            "defect": False,
            "comment": comment,
            "root_suite_title": case_ctx["root_suite_title"],
            "param": case_ctx.get("params"),
        }
        # Keep evidence on almost all results for richer demo timelines.
        if attachment_hashes and (status == STATUS_FAILED or rng.random() < 0.9):
            entry["attachments"] = [rng.choice(attachment_hashes)]
        if status == STATUS_FAILED and is_autotest:
            entry["stacktrace"] = (
                "Error: locator.click: Timeout 5000ms exceeded.\n"
                "  at CheckoutPage.submitPayment (checkout.page.ts:118:15)\n"
                "  at tests/checkout.spec.ts:42:9"
            )
        entry["steps"] = _build_steps(rng, is_autotest, status, templates, attachment_hashes)
        entries.append(entry)

    if entries and not idle_gap_used:
        # Guarantee at least one visible gap by shifting second half.
        midpoint = len(entries) // 2
        for item in entries[midpoint:]:
            item["start_time"] = int(item["start_time"]) + 3

    _ensure_manual_ratio(rng, entries, 0.2)
    _enforce_defect_ratio(rng, entries)
    _enforce_failed_overlap(rng, entries, weak_suite_title)

    for entry in entries:
        if entry["status"] != STATUS_FAILED:
            entry["defect"] = False
            entry.pop("stacktrace", None)
        if entry["status"] == STATUS_FAILED and not entry["is_autotest"]:
            entry.pop("stacktrace", None)
            entry["comment"] = "Manual execution failed; observed mismatch and captured notes for triage."
        if entry["status"] == STATUS_FAILED and entry["is_autotest"] and "stacktrace" not in entry:
            entry["stacktrace"] = (
                "Error: expect(received).toBeVisible() failed.\n"
                "  at checkout.spec.ts:58:11"
            )
        entry.pop("root_suite_title", None)
        if not entry.get("param"):
            entry.pop("param", None)
        if not entry.get("attachments"):
            entry.pop("attachments", None)

    audit = {
        "total": len(entries),
        "passed": sum(1 for e in entries if e["status"] == STATUS_PASSED),
        "failed": sum(1 for e in entries if e["status"] == STATUS_FAILED),
        "skipped": sum(1 for e in entries if e["status"] == STATUS_SKIPPED),
        "manual": sum(1 for e in entries if not e["is_autotest"]),
        "defect": sum(1 for e in entries if e.get("defect")),
    }
    return entries, audit


def _pick_title_and_description(
    rng: random.Random, run_type: str, templates: dict[str, Any], run_index: int
) -> tuple[str, str]:
    titles = templates.get("run_titles", {}).get(run_type, [])
    descs = templates.get("run_descriptions", {}).get(run_type, [])
    title = rng.choice(titles) if titles else f"{run_type} - Simulation Run {run_index}"
    desc = (
        rng.choice(descs)
        if descs
        else "Simulation run generated for realistic timeline, defect, and traceability data."
    )
    return title, desc


def _choose_tags(rng: random.Random, templates: dict[str, Any], run_type: str) -> list[str]:
    pool = list(templates.get("tags", []))
    if run_type.lower() not in pool:
        pool.append(run_type.lower())
    size = rng.randint(1, 3)
    if len(pool) < size:
        return pool
    return rng.sample(pool, k=size)


def _mark_incomplete_run(
    run_summaries: list[dict[str, Any]], run_id: int, reason: str
) -> None:
    run_summaries.append(
        {
            "run_id": run_id,
            "status": "incomplete",
            "reason": reason,
        }
    )


def _resolve_paths(args: argparse.Namespace) -> dict[str, Path]:
    repo_root = Path(__file__).resolve().parents[1]
    config_path = Path(args.config).resolve() if args.config else repo_root / "config" / "workspace.yaml"
    state_path = Path(args.state).resolve() if args.state else repo_root / "state" / "workspace_state.json"
    csv_path = Path(args.csv).resolve() if args.csv else repo_root / "QD-2026-02-18.csv"
    templates_path = repo_root / "assets" / "run_simulator_templates.yaml"
    timeline_profile_path = repo_root / "assets" / "run_timeline_profiles.yaml"
    return {
        "repo_root": repo_root,
        "config": config_path,
        "state": state_path,
        "csv": csv_path,
        "templates": templates_path,
        "timeline_profile": timeline_profile_path,
    }


def _load_case_contexts(
    csv_rows: list[dict[str, str]],
    workspace_state: dict[str, Any],
    *,
    allow_placeholder_ids: bool = False,
) -> list[dict[str, Any]]:
    case_ids_map = workspace_state.get("case_ids") or {}
    if not isinstance(case_ids_map, dict):
        case_ids_map = {}
    if not case_ids_map and not allow_placeholder_ids:
        raise SimulationError("workspace_state.json missing required non-empty case_ids map")
    suites = _build_suite_tree(csv_rows)
    contexts: list[dict[str, Any]] = []
    for row in csv_rows:
        if (row.get("suite_without_cases") or "").strip() == "1":
            continue
        csv_case_id = (row.get("id") or "").strip()
        if not csv_case_id:
            continue
        qase_case_id = case_ids_map.get(csv_case_id)
        if qase_case_id is None and allow_placeholder_ids:
            try:
                qase_case_id = int(csv_case_id)
            except ValueError:
                qase_case_id = None
        if qase_case_id is None:
            continue
        suite_id = (row.get("suite_id") or "").strip()
        root_title = _resolve_root_suite_title(suite_id, suites)
        contexts.append(
            {
                "csv_case_id": csv_case_id,
                "qase_case_id": int(qase_case_id),
                "suite_id": suite_id,
                "root_suite_title": root_title,
                "suite_title": (row.get("suite") or "").strip(),
                "params": _parse_params((row.get("parameters") or "").strip()),
            }
        )
    if not contexts:
        raise SimulationError("No runnable case contexts resolved from CSV + state.case_ids")
    return contexts


def _ensure_attachment_pool(
    token: str,
    limiter: RateLimiter,
    project_code: str,
    dry_run: bool,
) -> list[str]:
    rs_state = load_state("run_simulator_state")
    hashes = rs_state.get("attachment_hashes")
    if not isinstance(hashes, list):
        hashes = []
    hashes = [h for h in hashes if isinstance(h, str) and h]

    if not hashes:
        hashes.append(DEFAULT_ATTACHMENT_HASH)

    desired = 3
    if dry_run:
        return hashes[:desired]

    while len(hashes) < desired:
        content = f"run-simulator-evidence-{uuid4().hex}\n".encode("utf-8")
        try:
            uploaded = _qase_upload_attachment(
                project_code=project_code,
                token=token,
                limiter=limiter,
                filename=f"evidence-{len(hashes)+1}.txt",
                content=content,
            )
            if not uploaded:
                break
            hashes.extend(uploaded)
        except SimulationError as exc:
            print(f"[WARN] Attachment upload failed; continuing with available hashes: {exc}")
            break
    deduped = list(dict.fromkeys(hashes))[:desired]
    rs_state["attachment_hashes"] = deduped
    save_state("run_simulator_state", rs_state)
    return deduped


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simulate realistic Qase runs and results.")
    parser.add_argument("--config", help="Path to workspace YAML config")
    parser.add_argument("--state", help="Path to workspace_state.json")
    parser.add_argument("--csv", help="Path to cases CSV")
    parser.add_argument("--seed", type=int, help="Override deterministic seed")
    parser.add_argument("--run-count", type=int, help="Override simulation run count")
    parser.add_argument("--dry-run", action="store_true", help="Print planned actions without API writes")
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    paths = _resolve_paths(args)
    token = get_qase_token() if not args.dry_run else (os.environ.get("QASE_API_TOKEN") or "")
    limiter = RateLimiter(RATE_INTERVAL_SECONDS)

    config = _read_yaml(paths["config"])
    workspace_state = _read_json(paths["state"])
    csv_rows = _read_csv_rows(paths["csv"])
    templates = _load_templates(paths["templates"])
    timeline_profile = _load_timeline_profile(paths["timeline_profile"])

    simulation = config.get("simulation") or {}
    seed_cfg = config.get("seed") or {}
    seed_value = args.seed if args.seed is not None else int(seed_cfg.get("seed_value") or 42)
    rng = random.Random(seed_value)

    run_count = args.run_count if args.run_count is not None else int(simulation.get("run_count") or DEFAULT_RUN_COUNT)
    if run_count <= 0:
        raise SimulationError("run_count must be positive")

    project_code = (workspace_state.get("project_code") or "").strip()
    if not project_code:
        raise SimulationError("workspace_state.json missing project_code")

    environments = workspace_state.get("environments") or workspace_state.get("environment_ids") or {}
    milestones = workspace_state.get("milestones") or workspace_state.get("milestone_ids") or {}
    if not environments or not milestones:
        raise SimulationError("workspace_state.json must contain non-empty environments and milestones maps")

    run_types = simulation.get("run_types") or ["Regression", "Feature", "Smoke"]
    weak_suite_title = str(simulation.get("weak_suite") or "04 Checkout")
    case_contexts = _load_case_contexts(csv_rows, workspace_state, allow_placeholder_ids=args.dry_run)

    env_ids = [int(v) for v in environments.values()]
    milestone_ids = [int(v) for v in milestones.values()]
    attachment_hashes = _ensure_attachment_pool(token, limiter, project_code, args.dry_run)

    forced_green_count = max(1, math.ceil(run_count * 0.3))
    forced_green_runs = set(rng.sample(range(run_count), k=min(run_count, forced_green_count)))

    run_summaries: list[dict[str, Any]] = []
    print(
        f"[INFO] Starting simulation: runs={run_count}, seed={seed_value}, dry_run={args.dry_run}, "
        f"cases_available={len(case_contexts)}"
    )
    for run_idx in range(run_count):
        run_type = str(rng.choice(run_types))
        title, description = _pick_title_and_description(rng, run_type, templates, run_idx + 1)
        tags = _choose_tags(rng, templates, run_type)
        env_id = int(rng.choice(env_ids))
        milestone_id = int(rng.choice(milestone_ids))

        max_cases = min(DEFAULT_MAX_CASES_PER_RUN, len(case_contexts))
        min_cases = min(DEFAULT_MIN_CASES_PER_RUN, max_cases)
        desired = rng.randint(min_cases, max_cases) if max_cases >= min_cases else max_cases
        selected = rng.sample(case_contexts, k=desired)
        force_green = run_idx in forced_green_runs

        run_payload = {
            "title": title,
            "description": description,
            "environment_id": env_id,
            "milestone_id": milestone_id,
            "tags": tags,
            "start_time": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        }

        results_payload, audit = _generate_run_results(
            rng=rng,
            case_contexts=selected,
            weak_suite_title=weak_suite_title,
            force_green=force_green,
            profile=timeline_profile,
            templates=templates,
            attachment_hashes=attachment_hashes,
        )

        if args.dry_run:
            print(
                f"[DRY-RUN] Run {run_idx+1}/{run_count} | type={run_type} | title={title!r} | "
                f"results={len(results_payload)} | passed={audit['passed']} failed={audit['failed']} "
                f"skipped={audit['skipped']} manual={audit['manual']} defects={audit['defect']}"
            )
            continue

        run_resp = _qase_json_request("POST", f"/run/{project_code}", token, limiter, payload=run_payload)
        run_id = int(((run_resp.get("result") or {}).get("id") or 0))
        if run_id <= 0:
            raise SimulationError(f"Create run response missing run id: {run_resp}")
        print(f"[INFO] Created run {run_id}: {title}")

        # Submit results in API-safe chunks.
        batch_size = 100
        for start in range(0, len(results_payload), batch_size):
            batch = results_payload[start : start + batch_size]
            _qase_json_request(
                "POST",
                f"/result/{project_code}/{run_id}/bulk",
                token,
                limiter,
                payload={"results": batch},
            )
        print(f"[INFO] Submitted {len(results_payload)} results for run {run_id}")

        jira_summary = f"{run_type} run follow-up: {title}"
        jira_desc = (
            f"Run {run_id} exists to validate {run_type.lower()} scope with focus on "
            f"{weak_suite_title} risk behavior and linked execution outcomes."
        )
        jira_labels = ["qa-simulation", run_type.lower(), "qase-run"]

        try:
            jira_issue = _jira_create_task(jira_summary, jira_desc, jira_labels, limiter)
        except Exception as exc:
            _mark_incomplete_run(run_summaries, run_id, f"jira-create-failed: {exc}")
            print(f"[ERROR] Run {run_id} left incomplete due to Jira create failure: {exc}")
            continue

        try:
            _qase_json_request(
                "POST",
                f"/run/{project_code}/external-issue",
                token,
                limiter,
                payload={
                    "type": "jira-cloud",
                    "links": [{"run_id": run_id, "external_issue": jira_issue["key"]}],
                },
            )
        except Exception as exc:
            _mark_incomplete_run(run_summaries, run_id, f"jira-link-failed: {exc}")
            print(f"[ERROR] Run {run_id} left incomplete due to Jira link failure: {exc}")
            continue

        _qase_json_request("POST", f"/run/{project_code}/{run_id}/complete", token, limiter)
        run_summaries.append(
            {
                "run_id": run_id,
                "status": "completed",
                "jira_issue_key": jira_issue["key"],
                "result_total": len(results_payload),
                "passed": audit["passed"],
                "failed": audit["failed"],
                "skipped": audit["skipped"],
                "manual": audit["manual"],
                "defect": audit["defect"],
            }
        )
        print(f"[INFO] Completed run {run_id} and linked Jira issue {jira_issue['key']}")

    completed = sum(1 for r in run_summaries if r.get("status") == "completed")
    incomplete = sum(1 for r in run_summaries if r.get("status") == "incomplete")
    if not args.dry_run:
        rs_state = load_state("run_simulator_state")
        rs_state["last_execution"] = {
            "timestamp_utc": datetime.now(timezone.utc).isoformat(),
            "run_count": run_count,
            "completed_runs": completed,
            "incomplete_runs": incomplete,
            "seed": seed_value,
            "project_code": project_code,
            "runs": run_summaries,
        }
        save_state("run_simulator_state", rs_state)

    print(
        f"[DONE] Simulation complete | dry_run={args.dry_run} | requested_runs={run_count} "
        f"| completed={completed} | incomplete={incomplete}"
    )


if __name__ == "__main__":
    try:
        main()
    except SimulationError as exc:
        print(f"[ERROR] {exc}")
        raise SystemExit(1)
