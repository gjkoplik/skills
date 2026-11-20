---
name: close
description: 'Close out a finished harness build. Verifies the whole project and checks the result against the signed spec, asks the user everything it needs in one message, then archives the spec and plan. Use when every workstream of a plan under specs/ has passed and the user says they are ready to merge or wrap up, or runs /harness:close.'
argument-hint: '[spec slug]'
---

# Close

The last stage of the harness. One message from the user, one reply from you with everything you need answered, and
then it is done.

Read `${CLAUDE_PLUGIN_ROOT}/hub.md` first if you have not this session. You are the hub.

Which spec: $ARGUMENTS

If that is empty, use the one plan under `specs/` whose workstreams have all passed, and ask if there is more than
one.

## Checks first

Before asking the user anything, dispatch `harness:qa-engineer` in close mode with the spec and plan paths. It runs
every check in the plan across the whole project, and then does what the spec's "What the user does" section says and
reports whether that gets what the outcome promises.

Also read the plan's log yourself: every workstream has a passing entry, and no `must-fix` is open.

Any failure stops the close. Tell the user what failed and that the way back is `/harness:build`. A spec whose
outcome is not yet true does not close, however many workstreams passed.

## Ask once

One message with everything still open:

- the notes that were never acted on, each with your recommendation: fix now, leave, or write down as follow-up;
- any open question left in the spec;
- whether they want anything done with the branch (push, open a pull request). The default is nothing: merging is
  theirs.

## Then

- Apply the answers. A note to fix now goes to the right agent, then one more QA run.
- Append `Closed <date> by <name>` under the spec's sign-off, and a closing entry to the plan's log.
- Move `specs/<slug>/` to `specs/archive/<slug>/` with `git mv`. If the plan delivers by commit, commit the move.
- Do what they asked with the branch, and only that.

Finish with a short report: what shipped, where the archived spec is, and any follow-up they chose to keep.
