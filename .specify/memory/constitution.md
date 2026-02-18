<!--
SYNC IMPACT REPORT
==================
Version change:      1.0.0 → 1.1.0 (MINOR — new section added; 4 deferred decisions resolved)
Modified principles: None
Added sections:      API Reference Guidance (new §, between Technical Architecture and Workspace Narrative)
Removed sections:    None (4 TODO blocks replaced with concrete decisions)

Resolved TODOs:
  ✅ WORKSPACE_SCOPE  → Option A: Single project ("ShopEase Web App")
  ✅ FAILING_FEATURE  → Checkout (intentionally lower pass rate)
  ✅ RUN_TYPES        → Option B: Mixed — Regression + Feature + Smoke runs
  ✅ REPO_PHILOSOPHY  → Option B: Step-based sequential scripts

Templates reviewed:
  ✅ .specify/templates/plan-template.md    — No changes required
  ✅ .specify/templates/spec-template.md    — No changes required
  ✅ .specify/templates/tasks-template.md   — No changes required
  ✅ .specify/templates/agent-file-template.md  — No changes required
  ✅ .specify/templates/checklist-template.md   — No changes required

Deferred TODOs: None remaining
-->

# Qase Living Workspace Automation Constitution

## Core Principles

### I. Marketing-First Usability

The workspace MUST be visually clean, organized, and ready for immediate screenshot or video
capture at all times. Data MUST be realistic and believable without requiring interpretation.
Marketing MUST always know what each project represents, what each suite contains, what each
persona does, and exactly where to navigate to capture any given feature.

No manual preparation is permitted before a marketing session begins.

### II. Full Reproducibility

Any internal team member MUST be able to reproduce the complete demo workspace by:
1. Cloning the repository
2. Supplying their own API tokens (Qase + Jira)
3. Running the provided scripts

No manual steps, hidden state, or out-of-band configuration may exist. All structure,
data, and configuration MUST be expressible as code or config in the repository.

### III. Realism Over Randomness

All data MUST follow believable QA patterns. This means:
- Logical feature hierarchies that mirror a real engineering team's breakdown
- Natural pass/fail distributions (not flat 100% or random noise)
- Meaningful defect relationships tied to real failed tests
- Realistic naming (no "Test Case 47", "Suite ABC", or lorem ipsum)

Random, meaningless, or placeholder-style data is strictly prohibited.

### IV. Deterministic Variability

Automation MUST be seeded: the same seed input MUST produce the same workspace state.
Output MUST appear organic and realistic (slight variance, sprint-like rhythms) while
remaining stable enough for repeated marketing use across sessions.

Sudden metric drops, activity spikes, or prolonged inactive periods are prohibited.

### V. Stable Visual Health

The workspace MUST always appear active, healthy, and under continuous development.

Rules:
- Overall pass rate MUST remain between **85–92%**
- No long inactive periods (automation runs twice daily)
- No severe metric drops across any consecutive window
- Exactly one feature area MAY carry a consistently lower pass rate; this area is
  intentional and used for dashboard storytelling only

### VI. Fixed Scope, Growing Activity

For the primary marketing workspace, the following MUST remain fixed after initial seeding:
- Total test case count (hard cap: **150**)
- Suite structure
- Requirement set (Jira stories)
- Custom field schema

The following MUST grow continuously over time:
- Test runs
- Test results
- Defect lifecycle (creation → resolution)
- Analytics and trend data

AI-generated test cases in CI are prohibited. Human-authored or human-approved cases only.

---

## Data Constraints

### Test Cases

- Total: **150 maximum (hard limit)**; no growth after initial seeding
- Suite cap: **≤6 test cases per suite** (enforced during generation)
- AI case generation in CI: **prohibited**
- Suite count guideline: 150 cases ÷ 6 = **25 suites minimum**; target **24–30 suites**
  to keep every list visually full without any single suite feeling crowded

### Test Runs and Results

- Scheduled frequency: **twice per day** (via GitHub Actions)
- Historical depth target: **~3 months** of back-filled history at workspace creation
- Runs MUST follow sprint-like patterns with consistent cadence
- Metrics MUST remain visually healthy across the full history window

### Pass/Fail Distribution

- Overall workspace pass rate: **85–92%** (enforced by simulation seed logic)
- **Checkout** is the designated weaker feature area; it MUST maintain a consistently
  lower-than-average pass rate across all simulation runs to enable dashboard storytelling
  (e.g., "Checkout has been flaky this sprint — 3 open defects")
- All other feature areas MUST remain within the 85–92% band

### Defects

- MUST be created only from failed test results (no synthetic unlinked defects)
- Volume MUST remain limited (proportional to failure rate, not inflated)
- Majority MUST be resolved over time to show active maintenance
- A small open set MUST be retained at all times for realism

---

## Technical Architecture & Security

### Stack

| Concern          | Choice                                  |
|------------------|-----------------------------------------|
| Language         | Python                                  |
| Orchestrator     | GitHub Actions      Qase                    |
| Primary API      |  API v1 (+ v2 where required)       |
| Requirements API | Jira Cloud REST API v3                  |

### Rate Limiting (Hard Limits)

- Qase API: **≤5 requests/second**; never exceed **600 requests/minute**
- All scripts MUST implement request throttling
- All scripts MUST handle retries with exponential back-off and graceful failure

### Security Rules

Credentials MUST exist only in:
- GitHub Secrets (CI/CD)
- Local environment variables (developer workstations)

Credentials MUST NEVER appear in:
- Notion (even as placeholders)
- Source code or config files committed to the repo
- Documentation files of any kind

Each sales team or internal user supplies their own Qase and Jira tokens; no shared
production credentials exist in the repository.

### Automation Script Inventory

All scripts MUST be:
- **Idempotent** where possible (re-running does not duplicate or corrupt data)
- **Config-driven** (behavior controlled by YAML/env, not hardcoded constants)
- **Fully reproducible** (same config + same seed = same result)

Core scripts required:

| # | Script                     | Responsibility                                      |
|---|----------------------------|-----------------------------------------------------|
| 1 | Workspace initializer      | Create Qase project, add custom fields, environments, milestones, configurations       |
| 2 | Jira requirement generator | Bulk-create Epics + Stories in Jira                 |
| 3 | Suite generator            | Create full suite tree in Qase  (30 suites)  from the CSV                   |
| 4 | Test case generator        | Bulk-create 120 cases with custom fields from the CSV + Jira links |
| 5 | Run simulator              | Create historical and ongoing test runs + results   |
| 6 | Defect generator           | Create defects from failed results, manage lifecycle |
| 7 | Maintenance / cleanup      | Archive stale data, enforce health rules            |

**Execution model: Step-based sequential scripts.**
Each script runs independently in a defined sequence. This is the authoritative approach;
fully-automated one-shot execution is out of scope for this project.

Canonical execution order:
```
Step 1: workspace-init.py        —  Create Qase project, add custom fields, environments, milestones, configurations
Step 2: jira-requirements.py     — Bulk-create Epics + Stories in Jira
Step 3: suite-generator.py       — Create full suite tree in Qase with 30 suites from the CSV
Step 4: case-generator.py        — Bulk-create 120 cases with custom fields from the CSV + Jira links 
Step 5: run-simulator.py         — Seed historical runs + results (~3 months)
Step 6: defect-generator.py      — Create defects from failed results, manage lifecycle
Step 7: maintenance.py           — Ongoing twice-daily activity simulation
```

---

## API Reference Guidance

Any agent or developer implementing scripts that call the Qase API MUST consult the
in-repo documentation before writing any API call at `./api`. Do not rely on general knowledge of the Qase API; use the curated reference files in this repository.

### Entry point

```
api-index.md          ← Start here. Maps every supported endpoint to its doc file.
api/                  ← One file per endpoint (e.g., api/cases.bulk-create.md).
```

### Usage rule

1. Find the endpoint key in `api-index.md`
2. Open only that mapped file in `api/`
3. Read the full file before writing any code against that endpoint

### Currently documented endpoints

| Group         | Operations                                                   |
|---------------|--------------------------------------------------------------|
| Cases         | list, create, get, update, delete, bulk-create, attach/detach external issue |
| Custom Fields | list, create, get, update, delete                            |
| Defects       | list, create, get, update, delete, resolve                   |
| Environments  | list, create, get, update, delete                            |
| Attachments   | list, upload, get, delete                                    |
| Authors       | list, get                                                    |


---

## Workspace Narrative

### Simulated Product: ShopEase — E-commerce Platform

ShopEase is a fictional mid-size e-commerce platform used as the demo product.
All test cases, suites, requirements, and defects MUST map to its feature domains.

Feature domains (fixed):

| # | Domain           |
|---|------------------|
| 1 | Authentication   |
| 2 | Product Catalog  |
| 3 | Search           |
| 4 | Product Detail   |
| 5 | Cart             |
| 6 | Promotions       |
| 7 | Checkout         |
| 8 | Orders           |
| 9 | Admin            |

### Workspace Scope

**Single project: "ShopEase Web App" (Option A).**
The initial workspace contains one Qase project only. Multi-platform projects (iOS, Android,
API) are out of scope for this constitution and MUST NOT be added without a MINOR amendment.

### Personas

Personas MUST be:
- Fixed and pre-defined (not dynamically generated)
- Simulated only — not linked to real Qase user accounts
- Represented through metadata only: naming, descriptions, and run authorship fields

Implementation constraint: **one API token** is used for all API operations.
Personas do not require a dynamic lifecycle; they exist as narrative scaffolding only.

---

## Requirement Linkage

Every test case in the workspace MUST:
- Link to **exactly one Jira Story** via Qase's external issue link mechanism
- Represent a specific, named requirement from that Story

Jira usage rules:
- Jira is a **requirement store only** — no sprint boards, velocity tracking, or workflow automation
- Each deployment or sales team creates their own Jira instance and supplies their own tokens
- Jira issue structure: **Epics** (one per feature domain) + **Stories** (2–4 per sub-feature)

### Custom Fields (Mandatory Set)

All five fields MUST be present and populated on every test case:

| # | Field Name         | Purpose                                         |
|---|--------------------|-------------------------------------------------|
| 1 | Component          | Web UI / Backend API / Payments / Search / Admin |
| 2 | User Journey       | New / Returning / Guest / Admin                 |
| 3 | Risk Level         | High / Medium / Low                             |
| 4 | Automation Status  | Not Automated / Candidate / Automated           |
| 5 | Test Data Profile  | US address / EU address / out-of-stock / discount-eligible / etc. |

Fields MUST support filtering and dashboard views. No additional custom fields are permitted
without a constitution amendment.

---

## Activity Simulation Rules

### Scheduling

- Automation MUST run **twice per day** (morning + evening cadence via GitHub Actions)
- Each run batch MUST appear as organic team activity, not mechanical repetition
- Seeded randomness ensures deterministic yet varied output

### Run Types

**Mixed run types (Option B).** The simulation engine MUST produce a realistic mix:

| Run Type   | Cadence / Purpose                                      |
|------------|--------------------------------------------------------|
| Regression | Full suite coverage; run on every simulated "release"  |
| Feature    | Scoped to one feature domain; run mid-sprint           |
| Smoke      | Small critical-path subset; run after every deployment |

The mix MUST vary naturally across the history window so dashboards show distinct run
categories rather than a uniform flat pattern.

### Health Enforcement Rules

The simulation engine MUST enforce:
- No two consecutive days with zero activity
- No pass rate outside the **85–92%** band in any rolling 7-day window
- The designated weaker feature area stays below average but not critically broken
- Defect open/close ratio trends toward closure over a sprint window

---

## Success Criteria

The workspace is considered successful when all of the following hold simultaneously:

1. **Marketing readiness**: Marketing can open the workspace and capture screenshots
   immediately, with no preparation required.
2. **Believable dashboards**: All analytics views show non-flat charts, believable trends,
   and consistent sprint-like activity.
3. **Reproducibility verified**: An internal team member with no prior knowledge can clone
   the repo, add tokens, run scripts, and reach an equivalent workspace state.
4. **Zero manual setup**: After the initializer scripts complete, no manual configuration
   steps remain.

---

## Governance

This constitution is the authoritative document for the Qase Living Workspace Automation
project. It supersedes all other design notes, Notion pages, and informal decisions.

### Amendment Procedure

1. Identify the change category:
   - **MAJOR** (x.0.0): A principle is removed, fundamentally redefined, or a hard data
     constraint is broken
   - **MINOR** (x.y.0): A new principle or section is added, or existing guidance is
     materially expanded
   - **PATCH** (x.y.z): Clarifications, wording improvements, typo fixes, or non-semantic
     refinements
2. Update this file with a new version number, today's `LAST_AMENDED` date, and a new
   Sync Impact Report HTML comment at the top
3. Review and update all affected templates in `.specify/templates/`
4. Commit with message: `docs: amend constitution to vX.Y.Z (<change summary>)`

### Compliance

Before any new implementation phase begins, the implementing agent or developer MUST:
- Read this constitution
- Verify the planned work does not violate any principle
- Document any necessary deviation in the plan file as a justified exception

The `Constitution Check` section in every `plan.md` file exists for this purpose.

---

**Version**: 1.1.0 | **Ratified**: 2026-02-18 | **Last Amended**: 2026-02-18
