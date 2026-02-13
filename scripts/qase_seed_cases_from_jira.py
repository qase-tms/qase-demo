from __future__ import annotations

import argparse
import json
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from jira_utils import jira_search_issues
from qase_seed_utils import ensure_local_qase_v1_on_path, get_qase_token


PROJECT_CODE = "QD"


@dataclass(frozen=True)
class SystemFieldOption:
    id: int
    title: str
    slug: str


def _load_bytes(path: Path) -> bytes:
    return path.read_bytes()


def _pick(rng: random.Random, items: List[str]) -> str:
    return items[rng.randrange(0, len(items))]


def _risk_to_priority(risk: str) -> int:
    # system Priority ids: 1 High, 2 Medium, 3 Low (0 Not set)
    return {"High": 1, "Medium": 2, "Low": 3}.get(risk, 2)


def _risk_to_severity(risk: str) -> int:
    # system Severity ids: 2 Critical, 3 Major, 4 Normal, 5 Minor
    return {"High": 2, "Medium": 3, "Low": 5}.get(risk, 3)


def _make_steps(title: str, rng: random.Random, step_attachment_hash: Optional[str]) -> List[Dict[str, object]]:
    # Keep 2–4 steps with action + expected + optional data.
    n = rng.randint(2, 4)
    steps: List[Dict[str, object]] = []
    for i in range(1, n + 1):
        steps.append(
            {
                "position": i,
                "action": f"Step {i}: {title} — perform action {i}",
                "data": "Use demo data from attachments or seeded accounts" if i == 1 else None,
                "expected_result": f"Expected {i}: system behaves as intended for {title.lower()}",
                **({"attachments": [step_attachment_hash]} if (step_attachment_hash and i == n) else {}),
            }
        )
    # remove None keys (client excludes None anyway, but keep clean)
    cleaned: List[Dict[str, object]] = []
    for s in steps:
        cleaned.append({k: v for k, v in s.items() if v is not None})
    return cleaned


def _get_leaf_suites(suites) -> List[Tuple[int, str]]:
    # suites: List[Suite]
    by_id = {int(s.id): s for s in suites if getattr(s, "id", None) is not None}
    children: Dict[int, int] = {}
    for s in suites:
        pid = getattr(s, "parent_id", None)
        if pid is not None:
            children[int(pid)] = children.get(int(pid), 0) + 1
    leaf: List[Tuple[int, str]] = []
    for sid, s in by_id.items():
        if children.get(sid, 0) == 0:
            leaf.append((sid, (getattr(s, "title", "") or "").strip()))
    # stable order for consistent distribution
    return sorted(leaf, key=lambda x: x[1].lower())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, default=120, help="Total cases to create (100–150 recommended).")
    parser.add_argument("--dry-run", action="store_true", help="Plan only; do not create in Qase.")
    parser.add_argument("--skip-linking", action="store_true", help="Create cases but do not link to Jira (useful until Jira integration is configured in Qase).")
    args = parser.parse_args()

    if args.count < 100 or args.count > 150:
        raise SystemExit("--count should be between 100 and 150 for this demo.")

    ensure_local_qase_v1_on_path()
    import qase.api_client_v1 as qase_v1  # noqa: E402

    from qase.api_client_v1.models.test_casebulk import TestCasebulk  # noqa: E402
    from qase.api_client_v1.models.test_casebulk_cases_inner import TestCasebulkCasesInner  # noqa: E402
    from qase.api_client_v1.models.test_case_external_issues import TestCaseExternalIssues  # noqa: E402
    from qase.api_client_v1.models.test_case_external_issues_links_inner import (  # noqa: E402
        TestCaseExternalIssuesLinksInner,
    )
    from qase.api_client_v1.models.test_step_create import TestStepCreate  # noqa: E402

    # Fetch Jira story keys (requirements)
    jira_stories = jira_search_issues('project = QD AND issuetype = Story ORDER BY key', fields=["summary", "labels"], max_results=200)
    story_keys = [i["key"] for i in jira_stories]
    if not story_keys:
        raise SystemExit("No Jira stories found in project QD.")

    token = get_qase_token()
    cfg = qase_v1.Configuration(host="https://api.qase.io/v1")
    cfg.api_key["TokenAuth"] = token

    rng = random.Random(42)  # deterministic seed for repeatable seeding

    assets_dir = Path(__file__).resolve().parents[1] / "assets"
    asset_login = assets_dir / "shopease-login-error.png"
    asset_checkout = assets_dir / "shopease-checkout-3ds.png"
    asset_users = assets_dir / "test-data-users.csv"
    asset_checkout_matrix = assets_dir / "checkout-matrix.csv"
    asset_promo_rules = assets_dir / "promo-rules.txt"
    for p in [asset_login, asset_checkout, asset_users, asset_checkout_matrix, asset_promo_rules]:
        if not p.exists():
            raise SystemExit(f"Missing asset file: {p}")

    with qase_v1.ApiClient(cfg) as api_client:
        suites_api = qase_v1.SuitesApi(api_client)
        suites_resp = suites_api.get_suites(PROJECT_CODE, limit=100, offset=0)
        suites = suites_resp.result.entities or []
        leaf_suites = _get_leaf_suites(suites)
        if not leaf_suites:
            raise SystemExit("No leaf suites found in Qase project QD.")

        # Enforce <=6 per suite.
        max_per_suite = 6
        if args.count > len(leaf_suites) * max_per_suite:
            raise SystemExit(
                f"Not enough leaf suites for {args.count} cases at <=6 per suite. "
                f"Leaf suites: {len(leaf_suites)}"
            )

        # Upload a small attachment set once; reuse hashes across cases/steps.
        attach_api = qase_v1.AttachmentsApi(api_client)
        upload = attach_api.upload_attachment(
            PROJECT_CODE,
            file=[
                (asset_login.name, _load_bytes(asset_login)),
                (asset_checkout.name, _load_bytes(asset_checkout)),
                (asset_users.name, _load_bytes(asset_users)),
                (asset_checkout_matrix.name, _load_bytes(asset_checkout_matrix)),
                (asset_promo_rules.name, _load_bytes(asset_promo_rules)),
            ],
        )
        # AttachmentUploadsResponse.result is a list[Attachmentupload] with hash+filename.
        uploaded = (upload.result or []) if upload else []
        by_name = {getattr(a, "filename", None): getattr(a, "hash", None) for a in uploaded}
        needed = [asset_login.name, asset_checkout.name, asset_users.name, asset_checkout_matrix.name, asset_promo_rules.name]
        missing = [n for n in needed if not by_name.get(n)]
        if missing:
            raise SystemExit(f"Attachment upload succeeded but hashes missing for: {missing}")

        case_level_hash = str(by_name[asset_login.name])
        step_level_hash = str(by_name[asset_checkout.name])
        data_hash = str(by_name[asset_users.name])
        matrix_hash = str(by_name[asset_checkout_matrix.name])
        rules_hash = str(by_name[asset_promo_rules.name])

        # Pull system fields so we can fill ids consistently.
        sys_api = qase_v1.SystemFieldsApi(api_client)
        sys_fields = sys_api.get_system_fields()
        sys_by_slug = {f.get("slug"): f for f in sys_fields if isinstance(f, dict)}

        # Case generation plan
        component_values = ["Web UI", "Backend API", "Payments", "Search", "Admin"]
        journey_values = ["New user", "Returning user", "Guest", "Admin"]
        risk_values = ["High", "Medium", "Low"]
        automation_track_values = ["Not automated", "Candidate", "Automated"]
        data_profiles = ["US address", "EU address", "Out-of-stock", "Discount eligible", "3DS required"]

        # Custom field IDs + option IDs come from the mapping file created by qase_seed_custom_fields.py.
        mapping_path = Path(__file__).resolve().parent / "custom_fields_map.json"
        if not mapping_path.exists():
            raise SystemExit("Missing scripts/custom_fields_map.json (run qase_seed_custom_fields.py first).")
        mapping = json.loads(mapping_path.read_text(encoding="utf-8"))
        cf_by_title: Dict[str, int] = mapping.get("field_ids") or {}
        opt_by_title: Dict[str, Dict[str, int]] = mapping.get("option_ids") or {}

        required_cfs = ["Component", "User Journey", "Risk", "Automation Track", "Test Data Profile"]
        for t in required_cfs:
            if t not in cf_by_title or t not in opt_by_title:
                raise SystemExit(f"Missing custom field mapping for: {t}")

        # Allocate cases across leaf suites in a round-robin way, staying <=6 per suite.
        per_suite_counts: Dict[int, int] = {sid: 0 for sid, _ in leaf_suites}
        suite_cycle = [sid for sid, _ in leaf_suites]

        cases: List[TestCasebulkCasesInner] = []
        case_to_story: List[str] = []

        for i in range(args.count):
            # choose next suite with room
            for _ in range(len(suite_cycle) * 2):
                sid = suite_cycle[i % len(suite_cycle)]
                if per_suite_counts[sid] < max_per_suite:
                    break
                i += 1
            per_suite_counts[sid] += 1

            story_key = story_keys[i % len(story_keys)]
            risk = _pick(rng, risk_values)
            component = _pick(rng, component_values)
            journey = _pick(rng, journey_values)
            auto_track = _pick(rng, automation_track_values)
            profiles = rng.sample(data_profiles, k=rng.randint(1, 2))

            title = f"[{story_key}] {component}: {journey} flow validation #{per_suite_counts[sid]}"

            # Contextual attachments: sparse, not everywhere.
            attachments: List[str] = []
            if rng.random() < 0.12:
                attachments.append(case_level_hash)
            if component == "Payments" and rng.random() < 0.35:
                attachments.append(matrix_hash)
            if component == "Search" and rng.random() < 0.20:
                attachments.append(data_hash)
            if component == "Admin" and rng.random() < 0.20:
                attachments.append(rules_hash)

            # Steps: occasionally attach an image to the final step.
            step_attach = step_level_hash if rng.random() < 0.08 else None
            steps = _make_steps(title, rng, step_attach)
            step_models = [TestStepCreate.from_dict(s) for s in steps]

            # System fields
            priority = _risk_to_priority(risk)
            severity = _risk_to_severity(risk)
            behavior = 2 if rng.random() < 0.78 else 3  # mostly positive
            ttype = 8  # Functional
            layer = 1 if rng.random() < 0.70 else 2  # mostly E2E, some API
            automation = 0 if auto_track == "Not automated" else (1 if auto_track == "Candidate" else 2)

            # Custom fields: map id(string) -> value(string)
            custom_field = {
                str(cf_by_title["Component"]): str(opt_by_title["Component"][component]),
                str(cf_by_title["User Journey"]): str(opt_by_title["User Journey"][journey]),
                str(cf_by_title["Risk"]): str(opt_by_title["Risk"][risk]),
                str(cf_by_title["Automation Track"]): str(opt_by_title["Automation Track"][auto_track]),
                # multiselect: comma-separated option IDs (string)
                str(cf_by_title["Test Data Profile"]): ",".join(str(opt_by_title["Test Data Profile"][p]) for p in profiles),
            }

            desc = f"Requirement: {story_key}. Validates {component} behavior for {journey.lower()} scenarios."
            pre = "Seeded demo users exist (see attached CSV) and API is reachable."
            post = "No persistent side effects beyond demo data; cleanup not required."

            tags = ["demo", f"jira:{story_key}", f"component:{component.lower().replace(' ','-')}"]
            if risk == "High":
                tags.append("risk:high")

            cases.append(
                TestCasebulkCasesInner(
                    title=title[:255],
                    description=desc,
                    preconditions=pre,
                    postconditions=post,
                    suite_id=sid,
                    priority=priority,
                    severity=severity,
                    behavior=behavior,
                    type=ttype,
                    layer=layer,
                    automation=automation,
                    status=0,  # Actual
                    attachments=attachments or None,
                    steps=step_models,
                    tags=tags,
                    custom_field=custom_field,
                    is_flaky=1 if rng.random() < 0.04 else 0,
                )
            )
            case_to_story.append(story_key)

        plan = {
            "total_cases": args.count,
            "leaf_suites": len(leaf_suites),
            "max_per_suite": max_per_suite,
            "attachments_uploaded": len(uploaded),
        }
        print(json.dumps(plan, indent=2))

        if args.dry_run:
            print("Dry run only; no cases created.")
            return 0

        cases_api = qase_v1.CasesApi(api_client)

        # Create in batches to stay safe with payload sizes.
        created_ids: List[int] = []
        batch_size = 30
        start = 0
        while start < len(cases):
            batch = cases[start : start + batch_size]
            resp = cases_api.bulk(PROJECT_CODE, TestCasebulk(cases=batch))
            ids = (resp.result.ids or []) if resp and resp.result else []
            if len(ids) != len(batch):
                raise SystemExit(f"Bulk create mismatch: expected {len(batch)} ids, got {len(ids)}")
            created_ids.extend([int(x) for x in ids])
            start += batch_size

        # Persist mapping so linking can be retried later (no secrets).
        state_path = Path(__file__).resolve().parent / "seed_state_qd_cases.json"
        state_path.write_text(
            json.dumps(
                [{"case_id": cid, "jira_key": skey} for cid, skey in zip(created_ids, case_to_story)],
                indent=2,
            ),
            encoding="utf-8",
        )

        if args.skip_linking:
            print(f"Created cases: {len(created_ids)} (linking skipped).")
            return 0

        # Attach Jira links (mandatory for the final demo), but this will fail until the Jira integration
        # is configured in Qase for this workspace/project.
        links: List[TestCaseExternalIssuesLinksInner] = [
            TestCaseExternalIssuesLinksInner(case_id=cid, external_issues=[skey])
            for cid, skey in zip(created_ids, case_to_story)
        ]
        try:
            cases_api.case_attach_external_issue(
                PROJECT_CODE,
                TestCaseExternalIssues(type="jira-cloud", links=links),
            )
            print(f"Created cases: {len(created_ids)} and linked to Jira stories.")
        except Exception as e:
            print("Created cases, but Jira linking failed. This usually means Jira integration is not configured in Qase.")
            print(f"Error: {e}")
            print(f"You can retry later once Jira integration is enabled using scripts/qase_link_cases_to_jira.py")
            return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

