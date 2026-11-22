---
name: plan
description: 'Turn a signed spec into an accepted plan. The orchestrator agent writes the plan, the adversary attacks it without having written it, the user answers the findings that need a decision, and the user accepts the plan at a high level. The second of four stages; needs a signed spec. Run it when the user asks for this stage, by typing /harness:plan or by saying so ("run the harness plan", "plan that spec"). Never run it on your own initiative, and never to carry on from the previous stage without being asked.'
argument-hint: '[spec slug]'
---

# Plan

The second stage of the harness. It starts from a signed spec and ends with a plan the user has accepted. No code.

Read `${CLAUDE_PLUGIN_ROOT}/hub.md` first if you have not this session. You are the hub.

Which spec: $ARGUMENTS

If that is empty, use the one signed spec in the spec home that has no accepted plan, and ask if there is more than
one. If the spec is not signed, stop and say so; planning around a missing signature makes the signature decorative.

## The stage

**1. The orchestrator writes the plan.** Dispatch `harness:orchestrator` with the spec path, asking for a new plan at
`<slug>/plan.md` in the spec home, beside the spec.

**2. The adversary attacks it.** Dispatch `harness:design-adversary` with the plan path and the spec path, and the
instruction that this is the plan stage. Do not pass along the orchestrator's report or your own view of the plan.
If the plan settles interface details the spec left open, dispatch `harness:api-critic` on the plan alongside.

**3. The user answers the findings.** Sort what came back:

- A finding with an obvious right answer goes to the orchestrator as an amendment. Tell the user you did it; do not
  make them rule on it.
- A finding that is a real decision goes to the user, one at a time, each with the context and your recommendation.
- A finding that means the spec itself is wrong stops the stage. That is a re-sign, per the hub rules.

Expect to be argued with. When the user pushes back, find the real argument or concede; a round that only ratifies
the plan did nothing.

**4. Amend.** Dispatch the orchestrator once with everything accepted. If the amendment reshapes the workstreams,
offer a second adversary pass.

**5. Leave nothing in the conversation.** The build is meant to start in a fresh session that has only the spec and
the plan. Before asking for acceptance, go back over this conversation for anything the build would need that is in neither
file: a preference the user stated, a constraint mentioned in passing, a decision made while answering a finding.
Send it to the orchestrator to put in the plan. If you would brief a build agent differently for having been in
this conversation, something is still missing from the files.

**6. High-level acceptance.** The user accepts the plan from what you put in chat, without opening the file:

- the approach, in two or three sentences;
- the workstreams in order, one line each with what "done" means;
- the checks that will gate each one;
- how it will be delivered. The default is one commit per workstream on a working branch (created if the user is on
  the default branch), never pushed or merged by the harness, and running through all workstreams without pausing.
  The alternatives are leaving changes uncommitted in the working tree, and pausing after each workstream. If the
  project's own instructions say agents do not commit, default to the working tree. Ask only if the default looks
  wrong for this project;
- any workstream the orchestrator flagged as hard to undo, since the build will stop for you before each of those;
- any decision still open.

Acceptance is an explicit yes, the same as a signature. When the user accepts, append `Plan accepted <date>` to the
plan's log, with the delivery choices if they differ from what the plan says.

Then say the next step is `/harness:build`, best started in a fresh session, and stop.
