## Qase Demo Workspace Automation (WIP / Handoff)

This doc is intentionally concise but “sticky”: it captures the current plan, key decisions, and where to look so a new agent can continue without re-discovering everything.

### Goal
- Build a **living Qase workspace** with realistic, data-rich content for demos/screenshots/videos.
- Keep data fresh via automation (later: scheduled workflows like GitHub Actions).

### Current working docs (source of truth)
- **Notion page**: `demo-workspace` (`https://www.notion.so/2a1fa76398a980c98b0bc458ac136dec`)
  - Contains the “Personas (demo team)” section.
  - Keep Notion **short and curated**; put long details in repo docs.
- **Outline (starter only)**: `very-rough-and-incomplete-outline.md` (not complete; just initial notes).

### Repos/folders in this workspace
- **OpenAPI specs**: `specs/`
  - TestOps v1: `specs/testops-api/v1/src.yaml`
  - TestOps v2: `specs/testops-api/v2/src.yaml`
- **Python clients (generated)**:
  - v1 client: `qase-api-client/` (import `qase.api_client_v1`)
  - v2 client: `qase-api-v2-client/` (import `qase.api_client_v2`)
- **Qase MCP server**: `qase-mcp-server/` (TypeScript MCP server; used via Cursor MCP settings)

### Tooling available in this Cursor session
- **Notion tools**: confirmed read + write works (a write-check line was added previously).
- **Qase tools (MCP)**: confirmed reachable (e.g., listing projects works).

### Demo “story” (draft; adaptable)
- Proposed product narrative: **ShopEase e-commerce** release cycle (auth/search/cart/checkout/orders/admin).
- “Requirements first”: requirements are authored in **Jira**; Qase test cases map back to those requirements.

### Requirement ↔ Test case linkage (mandatory)
- Treat Jira issues (Stories) as “requirements”.
- **Every Qase test case must be linked to its Jira requirement** using Qase “external issue” linking.
  - In v1 API: cases support external issue attach/detach (`/case/{code}/external-issue/attach`).

### Scale targets
- Total test cases: **100–150**.
- UX constraint (new): **max 5–6 test cases per suite** → increase suite count.
  - Rule of thumb: 120 cases ÷ 6 ≈ **20 suites** (minimum); 120 ÷ 5 ≈ **24 suites**.
  - Recommended: **24–30 suites** so lists look “full” without any suite feeling crowded.

### Suite structure (direction)
- Use numbered top-level suites for tidy sidebar ordering.
- Demonstrate suite nesting in the first few areas (at least 2–3 levels deep).
- Approach: split by **feature area** + **sub-feature** + **test type** (happy/negative/permissions/integrations) to naturally justify more suites.

Example outline (not final):
- 01 Authentication
  - 01.1 Registration
  - 01.2 Login & Sessions
  - 01.3 Password Reset
- 02 Browse
- 03 Search
- 04 Product Detail (PDP)
- 05 Cart
- 06 Promotions
- 07 Checkout – Address
- 08 Checkout – Shipping
- 09 Checkout – Payment
- 10 Checkout – Confirmation
- 11 Orders – History
- 12 Orders – Returns/Refunds
- 13 Admin – Catalog
- 14 Admin – Orders Ops
- 15 Admin – Permissions
…expand as needed to keep ≤6 cases per suite.

### Custom fields (direction; keep minimal but meaningful)
Start with ~5 fields that enable filtering/storytelling without clutter:
- Component (e.g., Web UI / Backend API / Payments / Search / Admin)
- User Journey (New / Returning / Guest / Admin)
- Risk (High/Medium/Low)
- Automation Status (Not automated / Candidate / Automated)
- Test Data Profile (US/EU address, out-of-stock, discount eligible, etc.)

### Jira bulk requirement creation (what we need)
To create requirements in Jira via API “in bulk”, we’ll need:
- Jira deployment type:
  - Jira Cloud: `https://<your-domain>.atlassian.net`
  - Jira DC/Server: base URL (may be different API paths/auth)
- Auth method + credential:
  - Cloud: **email + API token** (Basic auth) OR OAuth (more setup)
  - DC/Server: PAT / Basic / cookie-based depending on configuration
- Target Jira project key (e.g., `SHP`) and desired issue types:
  - Epics + Stories (and optional Tasks/Bugs if you want realism)
- Required fields in your Jira instance:
  - Epic Name field behavior (varies by Jira configuration)
  - Whether Description supports Atlassian Document Format (ADF) (Cloud v3) vs plain text
- Naming conventions:
  - Epic titles, story titles, component labels, sprint/release naming

Implementation note:
- Jira Cloud bulk create endpoint is typically `/rest/api/3/issue/bulk` (v3); we’ll script against that with Python.
- Secrets should live in **GitHub Secrets** later (never committed), or be supplied via local env vars.
- **Do not store tokens in Notion** (even if it feels convenient). Keep Notion as curated narrative, not a credential store.

Local run (example):
```bash
export JIRA_BASE_URL="https://your-domain.atlassian.net"
export JIRA_EMAIL="demoqase@gmail.com"
export JIRA_API_TOKEN="***"
export JIRA_PROJECT_KEY="SHP"

python jira_bulk_create_requirements.py discover
python jira_bulk_create_requirements.py create --seed jira-requirements.seed.yaml
```

Known demo Jira (current):
- Base URL: `https://demoqase-1765364237285.atlassian.net`
- Project key: `QD`
- Created Epics: `QD-5`..`QD-10` (auth/search/cart/checkout/orders/admin)

### Immediate next steps (when ready to implement)
1. Finalize Jira project key + auth type for API calls (Cloud/DC).
2. Generate a requirements set:
   - ~6 epics, ~20–30 stories total (enough to map cleanly across 24–30 suites).
3. Create Qase suite tree + custom fields.
4. Create 100–150 cases in bulk (Python), ensuring:
   - ≤6 per suite
   - each case links to exactly one Jira Story (mandatory)
5. Later: runs/results/defects/milestones/environments + activity simulation.

### “If you’re a new agent picking this up”
Read in this order:
1. `WORK_IN_PROGRESS.md` (this file)
2. Notion `demo-workspace` page for the concise narrative + personas
3. `very-rough-and-incomplete-outline.md` for the broad vision
4. `specs/testops-api/v1/src.yaml` + `qase-api-client/` docs for linkage endpoints

