# Idea: review tests the way the code critic reviews code

Status: open
From: the review of [pull request 14](https://github.com/gjkoplik/skills/pull/14) (the code critic), 2026-11-24

## The idea

Tests rot the same way code does, and nothing in the harness looks for it. Give tests the same maintainer's read the
code critic gives code, at two scales: within a workstream, and across a whole test suite.

## Why it seemed worth keeping

Gary raised it: the problems the code critic exists for are "relevant there" too, naming "tests that become cruft,
reinvent code, lose relevance as the code base changes". He also wants a note kept to "maybe make a repo level skill
that can be called from within the harness for holistic test review".

## What is already known

What the harness does about tests today:

- The test engineer is told to write tests that can fail and that test what their name says
  ([test-engineer.md](../../plugins/harness/agents/test-engineer.md)).
- The build adversary looks for tests that cannot fail, and for a lowered bar
  ([build-adversary.md](../../plugins/harness/agents/build-adversary.md)).
- Nobody checks whether tests reuse what exists, or whether a change left tests behind that no longer mean anything.

The problems sort by when they can be seen:

- **In a workstream's diff:** a new fixture or helper duplicating an existing one; near-identical cases that should
  be one parametrized test; a test that re-implements the code it tests; mocking so heavy that nothing real runs.
- **Caused by a workstream, outside its diff:** tests for behavior the change removed, which still pass and now mean
  nothing; fixtures nothing uses any more.
- **In no single workstream:** a suite that has drifted from the codebase over months.

Sketched, not built:

- For the first two, extend two existing agents and add none. The code critic
  ([code-critic.md](../../plugins/harness/agents/code-critic.md)) treats tests as code it maintains: its reuse
  search covers fixtures and test helpers, and it looks for tests the change made obsolete. The test engineer reads
  the existing tests first and updates or deletes what the workstream made stale. A separate test critic would be an
  eleventh agent reading the same diff with the same question.
- For the third, a whole-suite review is a different kind of thing from a build-loop reviewer. Gary's suggestion is
  a skill of its own that can be run on a repo directly and also called from inside the harness.

The research behind the code critic found no measurement of test rot in agent-written code specifically; "a test
that tests nothing" appeared only in practitioner posts
([research notes](https://github.com/gjkoplik/skills/issues/8#issuecomment-7081866441)).

## What would have to be decided

- Whether the two agent changes go in on their own first, since they are small, or wait for the whole-suite skill.
- What the whole-suite skill reports, and whether it only reports or also prunes.
- Where it lives: a skill inside the harness plugin, or a plugin of its own that the harness can call when it is
  installed. A plugin cannot read another plugin's files, so "called from within the harness" needs a defined
  hand-off.
- When the harness would call it: at close, on a schedule, or only when asked.
- How it tells a stale test from a test of something rarely touched.
