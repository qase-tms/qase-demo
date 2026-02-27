from __future__ import annotations

import argparse
import math
import os
import random
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4

from qase_seed_utils import (
    get_qase_token,
    load_maintenance_state,
    load_state,
    save_maintenance_state,
)
from run_simulator import (
    RATE_INTERVAL_SECONDS,
    RateLimiter,
    SimulationError,
    _ensure_attachment_pool,
    _generate_run_results,
    _jira_create_task,
    _load_case_contexts,
    _load_templates,
    _load_timeline_profile,
    _pick_title_and_description,
    _qase_json_request,
    _read_csv_rows,
    _read_json,
    _read_yaml,
    _choose_tags,
)


DEFAULT_MIN_RUNS = 1
DEFAULT_MAX_RUNS = 6
DEFAULT_WEIGHTS = {
    1: 0.30,
    2: 0.25,
    3: 0.20,
    4: 0.12,
    5: 0.08,
    6: 0.05,
}


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


def _is_weekday_utc(now_utc: datetime) -> bool:
    # Monday=0 ... Sunday=6
    return now_utc.weekday() < 5


def _normalize_weights(min_runs: int, max_runs: int, cfg: Any) -> dict[int, float]:
    domain = list(range(min_runs, max_runs + 1))
    weights = {n: 1.0 for n in domain}
    if isinstance(cfg, list):
        for i, value in enumerate(cfg):
            n = min_runs + i
            if n > max_runs:
                break
            try:
                w = float(value)
            except (TypeError, ValueError):
                continue
            if w > 0:
                weights[n] = w
    elif isinstance(cfg, dict):
        for key, value in cfg.items():
            try:
                n = int(key)
                w = float(value)
            except (TypeError, ValueError):
                continue
            if n in weights and w > 0:
                weights[n] = w
    else:
        for n in domain:
            w = DEFAULT_WEIGHTS.get(n)
            if w is not None:
                weights[n] = w
    return weights


def _choose_run_count(min_runs: int, max_runs: int, weights: dict[int, float], rng: random.Random) -> int:
    values = list(range(min_runs, max_runs + 1))
    probs = [weights.get(n, 1.0) for n in values]
    return int(rng.choices(values, weights=probs, k=1)[0])


def _ensure_workspace_shape(workspace_state: dict[str, Any]) -> tuple[int, int]:
    suite_ids = workspace_state.get("suite_ids") or {}
    case_ids = workspace_state.get("case_ids") or {}
    if not isinstance(suite_ids, dict) or not isinstance(case_ids, dict):
        raise SimulationError("workspace_state.json must contain dict suite_ids and case_ids")
    if not case_ids:
        raise SimulationError("workspace_state.json missing required non-empty case_ids map")
    return len(suite_ids), len(case_ids)


def _build_skip_summary(reason: str, cycle_id: str, now_utc: datetime) -> dict[str, Any]:
    return {
        "cycle_id": cycle_id,
        "status": "skipped",
        "skip_reason": reason,
        "started_at_utc": now_utc.isoformat(),
        "ended_at_utc": now_utc.isoformat(),
        "timezone_basis": "UTC",
        "weekday_allowed": _is_weekday_utc(now_utc),
        "run_count_requested": 0,
        "run_count_completed": 0,
        "run_count_incomplete": 0,
        "duration_seconds": 0.0,
    }


def _update_metrics(ms_state: dict[str, Any]) -> None:
    history = ms_state.get("history") or []
    if not isinstance(history, list):
        history = []

    def _is_success(item: dict[str, Any]) -> bool:
        return item.get("status") == "completed"

    completed_or_partial = [
        h
        for h in history
        if isinstance(h, dict)
        and h.get("status") in {"completed", "completed_with_incomplete_runs", "failed"}
    ]
    latest_14 = completed_or_partial[-14:]
    successes = sum(1 for h in latest_14 if _is_success(h))
    scheduled_weekday = sum(1 for h in latest_14 if bool(h.get("weekday_allowed")))
    utc_ok = sum(1 for h in latest_14 if h.get("timezone_basis") == "UTC")
    durations = [float(h.get("duration_seconds") or 0.0) for h in latest_14 if h.get("duration_seconds") is not None]
    avg_duration = (sum(durations) / len(durations)) if durations else 0.0

    ms_state["metrics"] = {
        "window_size": len(latest_14),
        "rolling_14_day_success_count": successes,
        "rolling_14_day_success_rate": (successes / len(latest_14)) if latest_14 else 0.0,
        "rolling_14_day_weekday_utc_compliance_count": min(scheduled_weekday, utc_ok),
        "rolling_14_day_weekday_utc_compliance_rate": (
            min(scheduled_weekday, utc_ok) / len(latest_14) if latest_14 else 0.0
        ),
        "rolling_avg_duration_seconds": avg_duration,
    }


def _record_cycle(ms_state: dict[str, Any], summary: dict[str, Any]) -> None:
    history = ms_state.get("history")
    if not isinstance(history, list):
        history = []
    history.append(summary)
    ms_state["history"] = history[-30:]
    ms_state["last_cycle"] = summary
    _update_metrics(ms_state)
    save_maintenance_state(ms_state)


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run weekday maintenance activity simulation.")
    parser.add_argument("--config", help="Path to workspace YAML config")
    parser.add_argument("--state", help="Path to workspace_state.json")
    parser.add_argument("--csv", help="Path to cases CSV")
    parser.add_argument("--seed", type=int, help="Override deterministic seed")
    parser.add_argument("--min-runs", type=int, help="Override minimum runs per cycle")
    parser.add_argument("--max-runs", type=int, help="Override maximum runs per cycle")
    parser.add_argument("--dry-run", action="store_true", help="Print planned actions without API writes")
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    paths = _resolve_paths(args)
    config = _read_yaml(paths["config"])
    workspace_state = _read_json(paths["state"])
    csv_rows = _read_csv_rows(paths["csv"])
    templates = _load_templates(paths["templates"])
    timeline_profile = _load_timeline_profile(paths["timeline_profile"])
    maintenance_cfg = config.get("maintenance") or {}
    simulation_cfg = config.get("simulation") or {}
    seed_cfg = config.get("seed") or {}

    seed_value = args.seed if args.seed is not None else int(seed_cfg.get("seed_value") or 42)
    rng = random.Random(seed_value)
    limiter = RateLimiter(RATE_INTERVAL_SECONDS)
    token = get_qase_token() if not args.dry_run else (os.environ.get("QASE_API_TOKEN") or "")
    if not args.dry_run:
        required = ["JIRA_BASE_URL", "JIRA_EMAIL", "JIRA_API_TOKEN", "JIRA_PROJECT_KEY"]
        missing = [name for name in required if not (os.environ.get(name) or "").strip()]
        if missing:
            raise SimulationError(f"Missing required env vars for live maintenance run: {', '.join(missing)}")

    project_code = str((workspace_state.get("project_code") or "")).strip()
    if not project_code:
        raise SimulationError("workspace_state.json missing project_code")
    environments = workspace_state.get("environments") or workspace_state.get("environment_ids") or {}
    milestones = workspace_state.get("milestones") or workspace_state.get("milestone_ids") or {}
    if not environments or not milestones:
        raise SimulationError("workspace_state.json must contain non-empty environments and milestones maps")
    before_suite_count, before_case_count = _ensure_workspace_shape(workspace_state)

    min_runs = int(args.min_runs if args.min_runs is not None else maintenance_cfg.get("min_runs") or DEFAULT_MIN_RUNS)
    max_runs = int(args.max_runs if args.max_runs is not None else maintenance_cfg.get("max_runs") or DEFAULT_MAX_RUNS)
    if min_runs <= 0 or max_runs <= 0 or min_runs > max_runs:
        raise SimulationError("Invalid run range: expected positive min/max with min <= max")
    if min_runs < 1 or max_runs > 6:
        raise SimulationError("Maintenance run range must stay within 1..6")
    weights = _normalize_weights(min_runs, max_runs, maintenance_cfg.get("run_count_weights"))
    run_count = _choose_run_count(min_runs, max_runs, weights, rng)
    weak_suite_title = str(simulation_cfg.get("weak_suite") or "04 Checkout")
    run_types = list(simulation_cfg.get("run_types") or ["Regression", "Feature", "Smoke"])

    now_utc = datetime.now(timezone.utc)
    cycle_id = f"maint-{now_utc.strftime('%Y%m%dT%H%M%S')}-{uuid4().hex[:8]}"
    enforce_weekdays = bool(maintenance_cfg.get("weekdays_only", True))
    weekday_allowed = _is_weekday_utc(now_utc)
    ms_state = load_maintenance_state()
    active = ms_state.get("active_cycle")
    if enforce_weekdays and not weekday_allowed:
        summary = _build_skip_summary("weekend-utc-skip", cycle_id, now_utc)
        _record_cycle(ms_state, summary)
        print("[SKIP] Weekend UTC detected; maintenance cycle skipped.")
        return
    if isinstance(active, dict) and active.get("status") == "running":
        summary = _build_skip_summary("overlap-skip-active-cycle", cycle_id, now_utc)
        _record_cycle(ms_state, summary)
        print("[SKIP] Active maintenance cycle lock detected; overlapping trigger skipped.")
        return

    ms_state["active_cycle"] = {
        "cycle_id": cycle_id,
        "status": "running",
        "started_at_utc": now_utc.isoformat(),
    }
    save_maintenance_state(ms_state)

    started_monotonic = time.monotonic()
    case_contexts = _load_case_contexts(csv_rows, workspace_state, allow_placeholder_ids=args.dry_run)
    attachment_hashes = _ensure_attachment_pool(token, limiter, project_code, args.dry_run)
    env_ids = [int(v) for v in environments.values()]
    milestone_ids = [int(v) for v in milestones.values()]
    forced_green_count = max(1, math.ceil(run_count * 0.3))
    forced_green_runs = set(rng.sample(range(run_count), k=min(run_count, forced_green_count)))

    print(
        f"[INFO] Starting maintenance cycle: cycle_id={cycle_id} runs={run_count} seed={seed_value} "
        f"dry_run={args.dry_run} weekday_utc={weekday_allowed}"
    )

    run_summaries: list[dict[str, Any]] = []
    try:
        for run_idx in range(run_count):
            run_type = str(rng.choice(run_types))
            title, description = _pick_title_and_description(rng, run_type, templates, run_idx + 1)
            tags = _choose_tags(rng, templates, run_type)
            env_id = int(rng.choice(env_ids))
            milestone_id = int(rng.choice(milestone_ids))

            # Tactical run size for maintenance: smaller than Script 5, but still realistic.
            desired = rng.randint(35, min(70, len(case_contexts)))
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
                    f"[DRY-RUN] Run {run_idx+1}/{run_count} | type={run_type} | title={title!r} "
                    f"| results={len(results_payload)} | passed={audit['passed']} failed={audit['failed']} "
                    f"skipped={audit['skipped']} manual={audit['manual']} defects={audit['defect']}"
                )
                continue

            run_resp = _qase_json_request("POST", f"/run/{project_code}", token, limiter, payload=run_payload)
            run_id = int(((run_resp.get("result") or {}).get("id") or 0))
            if run_id <= 0:
                raise SimulationError(f"Create run response missing run id: {run_resp}")
            print(f"[INFO] Created maintenance run {run_id}: {title}")

            for start in range(0, len(results_payload), 100):
                batch = results_payload[start : start + 100]
                _qase_json_request(
                    "POST",
                    f"/result/{project_code}/{run_id}/bulk",
                    token,
                    limiter,
                    payload={"results": batch},
                )
            print(f"[INFO] Submitted {len(results_payload)} results for run {run_id}")

            jira_summary = f"Maintenance follow-up: {title}"
            jira_desc = (
                f"Maintenance cycle {cycle_id} run {run_id} validates weekday activity continuity "
                f"with focus on {weak_suite_title} behavior."
            )
            jira_labels = ["qa-maintenance", run_type.lower(), "qase-run"]
            try:
                jira_issue = _jira_create_task(jira_summary, jira_desc, jira_labels, limiter)
            except Exception as exc:
                run_summaries.append({"run_id": run_id, "status": "incomplete", "reason": f"jira-create-failed: {exc}"})
                print(f"[ERROR] Run {run_id} incomplete due to Jira create failure: {exc}")
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
                run_summaries.append({"run_id": run_id, "status": "incomplete", "reason": f"jira-link-failed: {exc}"})
                print(f"[ERROR] Run {run_id} incomplete due to Jira link failure: {exc}")
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
            print(f"[INFO] Completed maintenance run {run_id} and linked Jira issue {jira_issue['key']}")

        # Re-read workspace state at cycle end to ensure append-only behavior.
        workspace_state_after = _read_json(paths["state"])
        after_suite_count, after_case_count = _ensure_workspace_shape(workspace_state_after)
        if before_suite_count != after_suite_count or before_case_count != after_case_count:
            raise SimulationError("Structure safety check failed: suite/case counts changed during maintenance cycle")

        completed = sum(1 for r in run_summaries if r.get("status") == "completed")
        incomplete = sum(1 for r in run_summaries if r.get("status") == "incomplete")
        duration = time.monotonic() - started_monotonic
        final_status = "completed" if incomplete == 0 else "completed_with_incomplete_runs"
        if args.dry_run:
            completed = 0
            incomplete = 0
            final_status = "completed"

        summary = {
            "cycle_id": cycle_id,
            "status": final_status,
            "skip_reason": None,
            "started_at_utc": now_utc.isoformat(),
            "ended_at_utc": datetime.now(timezone.utc).isoformat(),
            "timezone_basis": "UTC",
            "weekday_allowed": True,
            "run_count_requested": run_count,
            "run_count_completed": completed,
            "run_count_incomplete": incomplete,
            "duration_seconds": round(duration, 3),
            "seed": seed_value,
            "dry_run": args.dry_run,
            "runs": run_summaries,
        }
        ms_state = load_maintenance_state()
        ms_state["active_cycle"] = None
        _record_cycle(ms_state, summary)
        print(
            f"[DONE] Maintenance cycle complete | dry_run={args.dry_run} | requested_runs={run_count} "
            f"| completed={completed} | incomplete={incomplete} | duration_s={duration:.2f}"
        )
    except Exception as exc:
        ms_state = load_maintenance_state()
        ms_state["active_cycle"] = None
        summary = {
            "cycle_id": cycle_id,
            "status": "failed",
            "skip_reason": None,
            "started_at_utc": now_utc.isoformat(),
            "ended_at_utc": datetime.now(timezone.utc).isoformat(),
            "timezone_basis": "UTC",
            "weekday_allowed": True,
            "run_count_requested": run_count,
            "run_count_completed": 0,
            "run_count_incomplete": 0,
            "duration_seconds": round(time.monotonic() - started_monotonic, 3),
            "seed": seed_value,
            "dry_run": args.dry_run,
            "runs": run_summaries,
            "error": str(exc),
        }
        _record_cycle(ms_state, summary)
        raise


if __name__ == "__main__":
    try:
        main()
    except SimulationError as exc:
        print(f"[ERROR] {exc}")
        raise SystemExit(1)
