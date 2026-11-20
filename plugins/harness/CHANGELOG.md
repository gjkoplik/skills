# Changelog: harness

Semantic versioning, most recent release first. A release is a `harness--v<version>` tag; see
[RELEASING.md](../../RELEASING.md). While the version is `0.0.x` the shape is still moving.

## 0.0.1

First draft. Not yet released, and not yet listed in the marketplace.

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
