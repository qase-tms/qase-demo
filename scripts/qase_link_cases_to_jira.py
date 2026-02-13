from __future__ import annotations

import re
from typing import Dict, List, Tuple

from jira_utils import jira_search_issues
from qase_seed_utils import ensure_local_qase_v1_on_path, get_qase_token


PROJECT_CODE = "QD"
JIRA_KEY_RE = re.compile(r"^\[(?P<key>[A-Z][A-Z0-9]+-\d+)\]\s+")


def main() -> int:
    ensure_local_qase_v1_on_path()
    import qase.api_client_v1 as qase_v1  # noqa: E402

    from qase.api_client_v1.models.test_case_external_issues import TestCaseExternalIssues  # noqa: E402
    from qase.api_client_v1.models.test_case_external_issues_links_inner import (  # noqa: E402
        TestCaseExternalIssuesLinksInner,
    )

    # Jira: map key -> id (id is what Qase expects for external_issues_ids/links)
    jira_stories = jira_search_issues(
        "project = QD AND issuetype = Story ORDER BY key",
        fields=["summary"],
        max_results=300,
    )
    key_to_id: Dict[str, str] = {i["key"]: i["id"] for i in jira_stories if i.get("key") and i.get("id")}
    if not key_to_id:
        raise SystemExit("No Jira stories found/mapped for project QD.")

    token = get_qase_token()
    cfg = qase_v1.Configuration(host="https://api.qase.io/v1")
    cfg.api_key["TokenAuth"] = token

    links: List[TestCaseExternalIssuesLinksInner] = []
    unmatched: List[Tuple[int, str]] = []

    with qase_v1.ApiClient(cfg) as api_client:
        cases_api = qase_v1.CasesApi(api_client)

        offset = 0
        page_size = 100
        while True:
            resp = cases_api.get_cases(PROJECT_CODE, limit=page_size, offset=offset)
            entities = resp.result.entities or []
            if not entities:
                break

            for c in entities:
                cid = int(c.id)
                title = (c.title or "").strip()
                m = JIRA_KEY_RE.match(title)
                if not m:
                    continue
                key = m.group("key")
                issue_id = key_to_id.get(key)
                if not issue_id:
                    unmatched.append((cid, key))
                    continue
                links.append(TestCaseExternalIssuesLinksInner(case_id=cid, external_issues=[issue_id]))

            offset += page_size
            if offset >= int(resp.result.total or 0):
                break

        if unmatched:
            print(f"Unmatched cases (no Jira issue id found): {len(unmatched)}")
            for cid, key in unmatched[:10]:
                print(f"- case {cid} -> {key}")

        if not links:
            print("No cases found to link (expected titles like [QD-123] ...).")
            return 0

        cases_api.case_attach_external_issue(
            PROJECT_CODE,
            TestCaseExternalIssues(type="jira-cloud", links=links),
        )

        print(f"Linked {len(links)} cases to Jira stories (by Jira issue id).")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

