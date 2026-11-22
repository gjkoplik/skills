# Changelog: harness

Semantic versioning, most recent release first, each with the day it shipped. A release is a
`harness--v<version>` tag; see [RELEASING.md](../../RELEASING.md). While the version is `0.0.x` the shape is still
moving.

## Unreleased

### Added

- **Ideas are kept.** Something worth doing that is not part of the spec in hand is written to its own file in
  `ideas/` the moment it comes up, at any stage, with enough of the discussion to pick it up later. Until now the
  most such an idea got was a one-line bullet under another spec's Out of scope, and often not that. An idea that a
  later spec picks up, or that is dropped, is archived with its outcome, so "we considered that" has an answer.
- The spec stage reads that history first: open and archived ideas, and archived specs.
- The build stage parks ideas that come up mid-build as idea files too.

### Changed

- Paths are relative to one spec home, `specs/` by default, with `archive/` and `ideas/` inside it.
- Moving a spec or an idea into an archive fixes the links that pointed at it. Archived documents take link fixes
  and nothing else.

## 0.0.4 (released Nov 22, 2026)

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

- The spec's "What the user does" section is now "User API", and asks for the whole shape of anything new or
  changed: every argument with its default, every flag, every field.
- The design adversary opens the spec's citations, and does it last, after forming its own view of the code.
  Its fixed angles are now described as a floor.

## 0.0.3 (released Nov 22, 2026)

### Added

- **Model pins.** A session on the most expensive model no longer runs every agent on it. The orchestrator and the
  design adversary follow the session, everything in the build runs on Opus, and the UI evaluator runs on Sonnet.
  Pins are defaults; ask for an agent on a different model and you get it.
- **Appearance checks in the UI evaluator.** It measures contrast, overlap, clipping and movement, and something a
  user cannot read or would take for broken now fails the workstream. Taste is still a note.
- **A hand-off check at the end of planning.** Anything the build would need that exists only in the conversation
  goes into the plan, so the build can start in a fresh session with the spec and the plan alone.

### Changed

- **The adversary is two agents.** `design-adversary` attacks the spec and the plan; `build-adversary` attacks each
  built workstream. The bare `adversary` agent is gone. It is the same role, split so the per-workstream reviews,
  which are the frequent ones, can be pinned to a model.
- **The UI evaluator scripts its walk.** One script does the steps and saves the screenshots, and the evaluator
  opens only the ones that matter. It used to drive the browser a click at a time, which costs far more.
- Agents are asked for their report and no narration, since the hub carries every report for the rest of the
  session.

## 0.0.2 (released Nov 22, 2026)

### Changed

- The four stages can be started by asking for them in words, not only by typing the command. 0.0.1 blocked the
  model from loading them at all, which made them unusable by voice. The rule that only the user advances a stage
  is now held by the skill descriptions and `hub.md` instead of by a hard block.

## 0.0.1 (released Nov 22, 2026)

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
