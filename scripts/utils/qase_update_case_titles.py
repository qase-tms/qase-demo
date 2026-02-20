from __future__ import annotations

import argparse
import csv
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from qase_seed_utils import ensure_local_qase_v1_on_path, get_qase_token


@dataclass(frozen=True)
class TitleUpdate:
    case_id: int
    new_title: str


def read_title_updates(csv_path: Path) -> list[TitleUpdate]:
    if not csv_path.exists():
        raise SystemExit(f"CSV not found: {csv_path}")

    updates: list[TitleUpdate] = []
    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise SystemExit(f"CSV has no header row: {csv_path}")
        if "id" not in reader.fieldnames or "new_title" not in reader.fieldnames:
            raise SystemExit(
                f"CSV must have headers 'id' and 'new_title'. Got: {reader.fieldnames}"
            )

        for i, row in enumerate(reader, start=2):
            raw_id = (row.get("id") or "").strip()
            raw_title = (row.get("new_title") or "").strip()
            if not raw_id:
                continue
            try:
                case_id = int(raw_id)
            except ValueError:
                raise SystemExit(f"Invalid id on line {i}: {raw_id!r}")
            if not raw_title:
                raise SystemExit(f"Missing new_title on line {i} (id={case_id})")
            updates.append(TitleUpdate(case_id=case_id, new_title=raw_title))
    return updates


def batched(items: list[TitleUpdate], limit: int | None) -> Iterable[TitleUpdate]:
    if limit is None:
        return items
    return items[:limit]


def parse_args() -> argparse.Namespace:
    repo_root = Path(__file__).resolve().parents[1]
    default_csv = repo_root / "QD-2026-02-13-title-updates.csv"

    p = argparse.ArgumentParser(
        description="Update Qase test case titles by case ID (Qase API v1)."
    )
    p.add_argument(
        "--project-code",
        required=True,
        help="Qase project code (e.g. QD)",
    )
    p.add_argument(
        "--csv",
        type=Path,
        default=default_csv,
        help=f"CSV file with columns id,new_title (default: {default_csv})",
    )
    p.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would change; don't call Qase API",
    )
    p.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Only process the first N rows (useful for a safe test run)",
    )
    p.add_argument(
        "--sleep-seconds",
        type=float,
        default=0.15,
        help="Delay between API calls to reduce rate limiting (default: 0.15)",
    )
    return p.parse_args()


def main() -> int:
    args = parse_args()

    ensure_local_qase_v1_on_path()
    import qase.api_client_v1 as qase_v1  # noqa: E402
    from qase.api_client_v1.models.test_case_update import TestCaseUpdate  # noqa: E402
    from qase.api_client_v1.rest import ApiException  # noqa: E402

    token = get_qase_token()
    updates = read_title_updates(args.csv)
    updates = list(batched(updates, args.limit))
    if not updates:
        print("No rows to update.")
        return 0

    if args.dry_run:
        for u in updates:
            print(f"[dry-run] case {u.case_id}: {u.new_title}")
        print(f"[dry-run] total: {len(updates)}")
        return 0

    configuration = qase_v1.Configuration(host="https://api.qase.io/v1")
    configuration.api_key["TokenAuth"] = token

    with qase_v1.ApiClient(configuration) as api_client:
        api = qase_v1.CasesApi(api_client)

        updated = 0
        failed = 0
        for idx, u in enumerate(updates, start=1):
            payload = TestCaseUpdate(title=u.new_title)
            tries = 0
            while True:
                tries += 1
                try:
                    api.update_case(args.project_code, u.case_id, payload)
                    updated += 1
                    print(f"[{idx}/{len(updates)}] updated case {u.case_id}")
                    break
                except ApiException as e:
                    # Retry a small number of times on common transient errors.
                    status = getattr(e, "status", None)
                    if status in {429, 500, 502, 503, 504} and tries < 4:
                        backoff = min(2.0 ** (tries - 1), 8.0)
                        print(
                            f"[{idx}/{len(updates)}] retry {tries}/3 for case {u.case_id} "
                            f"(HTTP {status}); sleeping {backoff:.1f}s"
                        )
                        time.sleep(backoff)
                        continue
                    failed += 1
                    print(
                        f"[{idx}/{len(updates)}] FAILED case {u.case_id} "
                        f"(HTTP {status}): {e}"
                    )
                    break
                finally:
                    if args.sleep_seconds:
                        time.sleep(args.sleep_seconds)

        print(f"Done. Updated: {updated}. Failed: {failed}. Total: {len(updates)}.")
        return 0 if failed == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())

