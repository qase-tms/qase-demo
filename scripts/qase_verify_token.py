from __future__ import annotations

import os

from qase_seed_utils import ensure_local_qase_v1_on_path, get_qase_token


def main() -> int:
    ensure_local_qase_v1_on_path()
    import qase.api_client_v1 as qase_v1  # noqa: E402

    token = get_qase_token()
    configuration = qase_v1.Configuration(host="https://api.qase.io/v1")
    configuration.api_key["TokenAuth"] = token

    # Lowest-impact call to confirm auth works
    with qase_v1.ApiClient(configuration) as api_client:
        api = qase_v1.ProjectsApi(api_client)
        resp = api.get_projects(limit=1, offset=0)
        total = getattr(resp.result, "total", None)
        print(f"Qase auth OK. Projects total: {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

