from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from qase_seed_utils import ensure_local_qase_v1_on_path, get_qase_token


PROJECT_CODE = "QD"


@dataclass(frozen=True)
class FieldSeed:
    title: str
    entity: int  # 0 case, 1 run, 2 defect
    type: int  # 3 selectbox, 6 multiselect, etc
    placeholder: str
    default_value: Optional[str]
    is_filterable: bool
    is_visible: bool
    is_required: bool
    is_enabled_for_all_projects: bool
    projects_codes: List[str]
    options: Optional[List[str]] = None  # titles for selectbox/multiselect/radio


@dataclass(frozen=True)
class SeedResult:
    field_ids: Dict[str, int]              # title -> customFieldId
    option_ids: Dict[str, Dict[str, int]]  # title -> (optionTitle -> optionId)
    created: List[str]


def _make_seed() -> List[FieldSeed]:
    # Keep the number of custom fields small but meaningful.
    return [
        FieldSeed(
            title="Component",
            entity=0,
            type=3,
            placeholder="Which component is primarily covered?",
            default_value="Web UI",
            is_filterable=True,
            is_visible=True,
            is_required=False,
            is_enabled_for_all_projects=False,
            projects_codes=[PROJECT_CODE],
            options=["Web UI", "Backend API", "Payments", "Search", "Admin"],
        ),
        FieldSeed(
            title="User Journey",
            entity=0,
            type=3,
            placeholder="Which user journey does this test represent?",
            default_value="Returning user",
            is_filterable=True,
            is_visible=True,
            is_required=False,
            is_enabled_for_all_projects=False,
            projects_codes=[PROJECT_CODE],
            options=["New user", "Returning user", "Guest", "Admin"],
        ),
        FieldSeed(
            title="Risk",
            entity=0,
            type=3,
            placeholder="How risky is this area for release?",
            default_value="Medium",
            is_filterable=True,
            is_visible=True,
            is_required=False,
            is_enabled_for_all_projects=False,
            projects_codes=[PROJECT_CODE],
            options=["High", "Medium", "Low"],
        ),
        FieldSeed(
            title="Automation Track",
            entity=0,
            type=3,
            placeholder="Where is this test in the automation lifecycle?",
            default_value="Not automated",
            is_filterable=True,
            is_visible=True,
            is_required=False,
            is_enabled_for_all_projects=False,
            projects_codes=[PROJECT_CODE],
            options=["Not automated", "Candidate", "Automated"],
        ),
        FieldSeed(
            title="Test Data Profile",
            entity=0,
            type=6,
            placeholder="Select relevant test data profiles",
            default_value=None,
            is_filterable=True,
            is_visible=True,
            is_required=False,
            is_enabled_for_all_projects=False,
            projects_codes=[PROJECT_CODE],
            options=["US address", "EU address", "Out-of-stock", "Discount eligible", "3DS required"],
        ),
    ]


def _get_existing_by_title(custom_fields) -> Dict[str, int]:
    out: Dict[str, int] = {}
    for cf in custom_fields:
        title = (getattr(cf, "title", "") or "").strip()
        cid = getattr(cf, "id", None)
        if title and cid:
            out[title] = int(cid)
    return out


def seed_custom_fields() -> Tuple[Dict[str, int], List[str]]:
    ensure_local_qase_v1_on_path()
    import qase.api_client_v1 as qase_v1  # noqa: E402

    from qase.api_client_v1.models.custom_field_create import CustomFieldCreate  # noqa: E402
    from qase.api_client_v1.models.custom_field_create_value_inner import (  # noqa: E402
        CustomFieldCreateValueInner,
    )

    token = get_qase_token()
    cfg = qase_v1.Configuration(host="https://api.qase.io/v1")
    cfg.api_key["TokenAuth"] = token

    seeds = _make_seed()

    created: List[str] = []
    option_ids: Dict[str, Dict[str, int]] = {}
    with qase_v1.ApiClient(cfg) as api_client:
        api = qase_v1.CustomFieldsApi(api_client)
        existing = api.get_custom_fields(limit=100, offset=0)
        existing_by_title = _get_existing_by_title(existing.result.entities or [])

        for seed in seeds:
            if seed.title in existing_by_title:
                continue

            value = None
            if seed.options:
                # Provide stable option IDs so cases can set values reliably.
                option_ids[seed.title] = {o: i for i, o in enumerate(seed.options, start=1)}
                value = [
                    CustomFieldCreateValueInner(id=i, title=o)
                    for o, i in option_ids[seed.title].items()
                ]

            payload = CustomFieldCreate(
                title=seed.title,
                value=value,
                entity=seed.entity,
                type=seed.type,
                placeholder=seed.placeholder,
                # For selectbox, default value should be the option ID (string).
                default_value=(
                    str(option_ids[seed.title][seed.default_value])
                    if (seed.default_value and seed.title in option_ids and seed.default_value in option_ids[seed.title])
                    else seed.default_value
                ),
                is_filterable=seed.is_filterable,
                is_visible=seed.is_visible,
                is_required=seed.is_required,
                is_enabled_for_all_projects=seed.is_enabled_for_all_projects,
                projects_codes=seed.projects_codes,
            )

            resp = api.create_custom_field(payload)
            if resp.result and resp.result.id:
                existing_by_title[seed.title] = int(resp.result.id)
                created.append(seed.title)

    # Persist mapping for case seeding (no secrets).
    out = {
        "project_code": PROJECT_CODE,
        "field_ids": existing_by_title,
        "option_ids": option_ids,
    }
    mapping_path = Path(__file__).resolve().parent / "custom_fields_map.json"
    mapping_path.write_text(json.dumps(out, indent=2, sort_keys=True), encoding="utf-8")

    return existing_by_title, created


def reset_custom_fields() -> List[str]:
    """
    Delete previously created demo custom fields (by title) so we can recreate them with stable option IDs.
    """
    ensure_local_qase_v1_on_path()
    import qase.api_client_v1 as qase_v1  # noqa: E402

    token = get_qase_token()
    cfg = qase_v1.Configuration(host="https://api.qase.io/v1")
    cfg.api_key["TokenAuth"] = token

    seeds = _make_seed()
    seed_titles = {s.title for s in seeds}
    deleted: List[str] = []

    with qase_v1.ApiClient(cfg) as api_client:
        api = qase_v1.CustomFieldsApi(api_client)
        existing = api.get_custom_fields(limit=100, offset=0)
        for cf in (existing.result.entities or []):
            title = (cf.title or "").strip()
            if title in seed_titles and cf.id:
                api.delete_custom_field(int(cf.id))
                deleted.append(title)

    return deleted


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", action="store_true", help="Delete existing demo custom fields first.")
    args = parser.parse_args()

    if args.reset:
        deleted = reset_custom_fields()
        if deleted:
            print(f"Deleted: {', '.join(deleted)}")

    ids, created = seed_custom_fields()
    print(f"Custom fields available (project {PROJECT_CODE}):")
    for title, cid in sorted(ids.items(), key=lambda x: x[0].lower()):
        print(f"- {title}: {cid}")
    if created:
        print(f"Created: {', '.join(created)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

