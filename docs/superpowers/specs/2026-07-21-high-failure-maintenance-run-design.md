# Design: guaranteed high-failure maintenance run

**Date:** 2026-07-21
**Status:** Approved

## Problem

The daily maintenance cycle (`scripts/maintenance.py`, invoked by the
`Daily Maintenance Activity` workflow) creates a random number of Qase runs
each weekday. The `force_green` sampling already guarantees at least one
all-passed run per cycle (`forced_green_count = max(1, ...)`), so "all tests
passed" runs are already covered.

What is missing is a run that is deliberately mostly-failing, so the demo
workspace always shows a clearly-broken build alongside the healthy ones.

## Goal

Every weekday maintenance cycle appends exactly **one** guaranteed
high-failure run in addition to the existing random runs. It goes through the
same lifecycle as every other run (create run → bulk-submit results → create +
link a Jira issue → complete) and is distinguished only by a tag, so it blends
into the daily timeline.

Failure intensity: **heavy (~60–75% of results fail)**, with defects and
stacktraces (produced by the existing decoration logic once results are marked
failed).

## Changes

### `scripts/run_simulator.py`

- `_pick_status(rng, is_weak, force_green, fail_bias=0.0)` — new optional
  `fail_bias`. When `fail_bias > 0` and `force_green` is `False`, failures
  dominate at that rate; weak-suite cases fail slightly more. Default `0.0`
  keeps every existing caller unchanged.
- `_generate_run_results(..., fail_bias=0.0)` — threads `fail_bias` through to
  `_pick_status`. The existing defect-ratio, failed-overlap, and stacktrace
  decoration then apply naturally to the failures.

### `scripts/maintenance.py`

- Extract the per-run lifecycle (create run, bulk results, Jira create + link,
  complete, plus the dry-run print) into a helper `_execute_run(...)` returning
  a summary dict, or `None` on dry-run. The existing loop and the new
  high-failure run both call it, removing duplication.
- After the main loop, build and execute one high-failure run:
  `fail_bias = high_failure_fail_bias` (default `0.68`), tags include the
  high-failure tag plus the run-type tag, normal random title/description,
  same case-selection sizing as the loop.
- `run_count_requested` in the cycle summary becomes `run_count + 1` to reflect
  the extra run. `forced_green_runs` sampling stays scoped to the main loop.

### `config/workspace.yaml` (`simulation:`)

Optional knobs, all with in-code defaults so absence changes nothing:

- `high_failure_fail_bias` (default `0.68`)
- `high_failure_tag` (default `high-failure`)

### Workflow YAML

No change — the daily cron already runs `maintenance.py`.

## Testing

- Unit test the new `fail_bias` path: `_generate_run_results` with
  `fail_bias=0.68` over a fixed seed yields an audit whose failed count is a
  clear majority. Pure, no network.
- `scripts/maintenance.py --dry-run` prints the extra high-failure run with a
  failed-dominant audit and the high-failure tag.

## Out of scope

- A guaranteed all-passed run (already provided by `force_green`).
- Any change to run volume beyond the single added run.
