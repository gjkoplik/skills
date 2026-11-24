# Changelog: test-review

Semantic versioning, most recent release first. A release is a `test-review--v<version>` tag; see
[RELEASING.md](../../RELEASING.md). While the version is `0.0.x` the shape is still moving.

## 0.0.1 (released Nov 24, 2026)

First cut.

### Added

- `/test-review`, a whole-suite review of test code for cruft. It reads every test against the codebase and git
  history, runs nothing, and writes one report to `test-review/YYYY-MM-DD-<scope>.md` in the repo it is pointed at.
  It changes nothing else and does not act on what it finds.
- Four kinds of finding and no others: a subject that is gone, a fixture or helper nothing uses, test code that
  remakes what the suite already has, and a test that repeats another test.
- Two groups. "Safe to act on" carries evidence the reader can check and tells whoever acts to run the affected
  tests with coverage before and after. Everything else is a question with options. Doubt makes a finding a
  question, because a wrong finding costs more than a missed one.
- Runs only when typed. A whole-suite review is expensive, so the model does not start one on its own.

### Notes from the first real run

One run on a Python library with 28 test files and about 32,000 lines of tests, split across six reading agents.
It returned 12 safe findings and 22 questions, all of them redundant or reinvented. Four of the safe findings were
read side by side by hand and the duplication was real in each.

- It found no test whose subject was gone and no unused fixture. That repo enforces full coverage and lints its
  tests, so there may have been none; the run does not show the review can find them.
- The first draft let a redundant test count as safe whenever some other test happened to cover it. Several findings
  leaned on a survivor that tests something else and only passes through the same call. That is now a question,
  since the named test is what tells someone which behavior broke.
- "The same setup in three or more tests" fired dozens of times in a large suite. Reinvented findings are now one
  per thing reinvented, with the places as a count.
- A suite that deselects some tests by default cannot be protected by "run the suite". A safe finding now names
  the command that runs the test it touches.
