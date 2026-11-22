---
name: build
description: 'Build an accepted plan, one workstream at a time. Each workstream is checked against the signed spec, implemented by specialist agents, reviewed blind by the adversary, verified by QA, and tested in a browser when it has a UI, with failures routed back through the plan. The third of four stages; needs an accepted plan under specs/. Run it again to resume a build that stopped. Run it when the user asks for this stage, by typing /harness:build or by saying so ("run the harness build", "build the plan", "resume the build"). Never run it on your own initiative, and never to carry on from the previous stage without being asked.'
argument-hint: '[spec slug]'
---

# Build

The third stage of the harness: the engineering loop. It starts from an accepted plan and ends with every workstream
built and verified.

Read `${CLAUDE_PLUGIN_ROOT}/hub.md` first if you have not this session. You are the hub.

Everything you need is in the spec and the plan. This stage is designed to start in a fresh session; if you are in
the session that did the planning, do not lean on what you remember of it over what the files say.

Which plan: $ARGUMENTS

If that is empty, use the one accepted, unfinished plan under `specs/`, and ask if there is more than one. If the
plan's log has no acceptance line, stop and say so. If the log shows the build already started, pick up where it
left off.

## Preflight, once

Before the first workstream, find out whether the project runs as it stands. Dispatch `harness:qa-engineer` in
preflight mode with the plan path: it runs the plan's checks and changes nothing.

Clean: log it and go on. Not clean: this is the user's call, so stop and give them the failures and three options.
Fix now (a workstream of its own, before the plan's), carry on (the failures are logged as the baseline, so they are
not later blamed on this work), or stop.

If the plan delivers by commit:

- Check `git status` first. Uncommitted changes that are not this spec and plan belong to someone, and
  per-workstream commits must not absorb them. Stop and ask how the user wants them handled.
- If the user is on the default branch, create the working branch.
- Commit the spec and plan on their own, so they do not ride in with the first workstream.

## The loop, per workstream

Take workstreams in plan order. Ones that do not depend on each other and do not touch the same files can run side
by side.

**1. Spec gate.** Before dispatching anything, open the spec and state in chat, in a sentence or two, what a user
will do to get what this workstream delivers, and whether that still matches the spec's outcome and "User API". Quote the spec, not the plan's paraphrase of it. A match proceeds without waiting for a reply. A mismatch is a
re-sign: stop. If the plan flags this workstream as hard to undo, stop here too and get an explicit go-ahead, whatever
the plan's pace.

**2. Specialists.** Dispatch what the workstream's `Needs` line calls for: `harness:code-engineer`, then
`harness:test-engineer`, then `harness:docs-engineer`. Each gets the plan path, the spec path, and the workstream by
name. Give the test engineer the workstream and the spec, not the code engineer's account of what it built: the tests
should check the contract, not the implementation's opinion of itself.

**3. Adversary, blind.** Dispatch `harness:build-adversary`. Its brief contains exactly:

- how to see the diff (the commit range, or the list of changed files);
- the workstream's `Delivers` and `Done when`, copied in;
- the spec's failure modes, copied in.

No plan path, no spec path, no implementer reports, no earlier findings. When it reports, send the same agent a
follow-up with the spec and plan paths and ask two things: does what was built still match the spec, and did earlier
findings in the log that were marked resolved actually stay resolved. If you cannot continue the same agent, do that
second check with a fresh `harness:build-adversary` and say in the log that it was not the same one.

If the workstream changes an interface, dispatch `harness:api-critic` on the diff alongside the adversary.

**4. QA.** Dispatch `harness:qa-engineer` with the plan path, the workstream, and the `must-fix` findings from step
3 that are mechanical to fix. It runs the checks and fixes what it can, up to three rounds.

**5. UI, when the workstream has one.** Dispatch `harness:ui-evaluator` with the workstream and the spec. A `must-fix`
inside the workstream's scope, in behavior or in appearance, goes to `harness:qa-engineer` to fix, then back to the evaluator, up to three rounds.

**6. Settle.** The workstream passes when the checks are clean, the UI passes or there is none, and no `must-fix` is
open. Then:

- commit it, if the plan delivers by commit: stage only the files this workstream touched, never everything, with a
  message that describes the change and not the process (no workstream numbers, no agent names);
- append a log entry: what shipped, each finding and what was done about it, any notes still open;
- give the user two or three lines in chat and go on to the next workstream, or stop here if the plan pauses.

## When a workstream does not pass

Anything the loop could not fix (a `must-fix` that is a design problem, QA or the UI loop out of rounds, a done-when
that turns out to be wrong) goes to `harness:orchestrator` as an amendment request, with the findings. It amends the
plan and the workstream re-enters at the spec gate.

Two things stop the loop instead:

- The orchestrator reports that the fix needs the spec to change. That is a re-sign.
- The same workstream has been amended twice and still does not pass. Bring the user the history and your read of
  why it is not converging.

## When a new idea arrives mid-build

From the user or from an agent, a good idea that the spec does not cover goes in the log as follow-up and the build
carries on. Scope changes between specs, not during one. If the user wants it in now, that is a re-sign.

## When the last workstream passes

Report in chat: what was built, the notes still open, and anything the user should look at first. Say the next step
is `/harness:close`, and stop.
