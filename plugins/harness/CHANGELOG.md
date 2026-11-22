# Changelog: harness

Semantic versioning, most recent release first. A release is a `harness--v<version>` tag; see
[RELEASING.md](../../RELEASING.md). While the version is `0.0.x` the shape is still moving.

## Unreleased

### Added

- **Specs cite their sources.** Claims about the current code carry `path:line` as of a commit the spec names, so
  the citation survives later pushes. External claims carry a link the drafter actually opened, and anything
  unchecked is marked (unverified). Plans cite the code they reason from the same way.
- **A Problem section at the top of the spec template**: what exists today and what is wrong with it. The adversary
  was already attacking the premise; now the premise is written down where it can be attacked.
- **An unprompted first read for both adversaries.** Before working their fixed angles they write down what strikes
  them as wrong in their own terms, and report that first. What is odd about one particular spec or diff may not be
  on a list written for all of them.

### Changed

- The design adversary opens the spec's citations, and does it last, after forming its own view of the code.
  Its fixed angles are now described as a floor.

## 0.0.3

### Changed

- **Agents are pinned to models.** A session on the most expensive model no longer runs every agent on it. The
  orchestrator and the design adversary follow the session; everything in the build runs on Opus; the
  UI evaluator runs on Sonnet. Pins are defaults and can be overridden by asking.
- **The adversary is two agents.** `design-adversary` attacks the spec and the plan; `build-adversary` attacks each
  built workstream. The bare `adversary` agent is gone. Same role, split so the per-workstream reviews, which are the frequent ones, can be pinned.
- **The UI evaluator checks appearance, and costs less doing it.** It writes one script that walks the steps and
  measures contrast, overlap, clipping and movement, then looks only at the screenshots that matter. Something a
  user cannot read or would take for broken now fails the workstream; taste is still a note.

- **Planning and building are separable sessions.** The plan stage now checks that nothing the build needs is left
  only in the conversation, and the build stage works from the spec and plan alone. Agents are asked for their
  report and no narration, since the hub carries every report for the rest of the session.

## 0.0.2

### Changed

- The four stages can be started by asking for them in words, not only by typing the command. 0.0.1 blocked the
  model from loading them at all, which made them unusable by voice. The rule that only the user advances a stage
  is now held by the skill descriptions and `hub.md` instead of by a hard block.

## 0.0.1

First release. Loads and validates; not yet run end to end on real work, so expect the shape to move.

### Added

- Four skills, one per stage: `spec`, `plan`, `build`, `close`. Each ends at a decision that belongs to the user.
- Eight agents the skills dispatch: `orchestrator`, `adversary`, `api-critic`, `code-engineer`, `test-engineer`,
  `docs-engineer`, `qa-engineer`, `ui-evaluator`.
- `hub.md`, the rules for the dispatching session, shared by the four skills.
- Spec and plan templates.

### Where it came from

A generalization of the harness built for hiveplotlib, rewritten rather than ported. That one carried about 4,500
lines of rules, per-agent expertise files, a wiki, and a plan file with ten writers. This one keeps the parts that
are structural (the signed spec, the cold reviewer, blind review after a build, one dispatcher, bounded loops) and
leaves the rest to the agents' judgment.

Cross-checked against Addy Osmani's [agent-skills](https://github.com/addyosmani/agent-skills) at its 2026-11-18
state. Taken from there: stages that only the user advances, assumptions stated before the interview, the explicit-yes
rule for signatures, vertical slicing with the riskiest slice early, a clean baseline before per-workstream commits,
stopping for anything a revert cannot undo, parking mid-build ideas, and a floor the checks cannot be lowered under.
