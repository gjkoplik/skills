# Changelog: what-if

Semantic versioning, most recent release first. A release is a `what-if--v<version>` tag; see
[RELEASING.md](../../RELEASING.md). While the version is `0.0.x` the shape is still moving.

## 0.0.1

First cut. Not yet released.

### Added

- A cheap triage skill for half-formed ideas. Two calibration questions, one research pass, an options section, for
  and against at equal length, and a call. Never implements and never produces a plan; a "not worth it" is a
  successful run.
- A report template carrying the disclosure mechanics, both themes, and the `ran` / `sourced` marks. Controls are
  injected from script rather than written into the markup, because some viewers strip JavaScript and a dead button
  is worse than no button. `<details>` is native and survives either way.
- `assets/html-to-markdown-twin.py`, because the HTML report and its markdown twin drifted the first time they were
  written by hand, and the markdown is the copy that ends up in review.

### Notes from the first real run

Three things changed after using it on an actual adoption question rather than on itself:

- **An appetite question was dropped.** It only earns its slot for someone who thinks in durations, and the options
  section answers the better question anyway.
- **Word budgets were relaxed to one cap.** Capping both levels produced a report that hit 97% of its top-level
  budget while spending 45% of its disclosure budget: not brief, thin, and it read as confident hand-waving. Only the
  top level is capped now; elsewhere the test is necessity, not length.
- **The report was reordered** to context, options, trade-offs, surface. The call used to name options by numbers
  defined two sections below it, so every reference in the answer pointed forward.
