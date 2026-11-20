---
name: spec
description: 'Turn a request into a one-page spec the user signs before any planning or code. Interviews the user where the request leaves the outcome open, drafts the spec from their answers, has them name how it could fail, gets a cold adversarial read, and stops for their signature. Use when the user asks to spec something out, wants to start spec-driven work on a feature or change, or runs /harness:spec. Not for one-line fixes.'
argument-hint: '[what you want built]'
---

# Spec

The first stage of the harness. It ends with a signed spec and nothing else: no plan, no code.

Read `${CLAUDE_PLUGIN_ROOT}/hub.md` first if you have not this session. You are the hub.

The request: $ARGUMENTS

If there is no request above, ask for one. If the work is trivial (a one-line fix, a typo), say so and suggest doing
it directly; the harness costs more than it returns on small things.

## What a spec is

One page stating what will be true for a user when the work ships and the literal thing they do to get it. It is the
intent, written down so that the user can sign it and every later agent can be held to it.

It is not a plan. No approach, no file lists, no sequencing, no done-when criteria. A spec that reads like a plan is
one the user will skim, and a skimmed signature is worth nothing. Keep it to a page; if it will not fit, ask whether
it is two specs.

## The stage

**1. Understand the request.** Pick a short slug. Read enough of the repo to know what exists, what the request
would touch, and whether something already does it. Check `specs/` for a related or archived spec.

**2. Interview, where the request leaves the outcome open.** One question at a time, each with your recommended
answer. Go after the forks that change what gets built: how ambitious (all of it, or the core), what is deliberately
out, what the user is assuming but has not said, what they would literally type or click. Skip anything the request
or the repo already settles. Stop when the outcome is determined or the user says enough. If the request already
determines it, skip the interview and say that you did.

**3. Draft.** Copy `${CLAUDE_PLUGIN_ROOT}/templates/spec.md` to `specs/<slug>/spec.md` and fill it from the user's
words. Write the outcome so a plausible wrong implementation contradicts it: "search is faster" cannot be checked
against a diff, "a search over 100k documents returns in under a second from the existing search box" can. Write
"What the user does" from the entry point a user would actually reach for, and try it against the code as it stands
so you know which parts do not exist yet. Leave Failure modes empty for now.

**4. Ask the user how it could fail.** What would make this hollow, wrong, or fake even with every test green? A
feature nobody needed, a default that quietly breaks a common case, a result that only holds the way it was measured.
Ask first and write down what they say in their words. Do not lead with your own list: a list you wrote has your
blind spots, and the user will nod along to it. If they would rather skip this, record that in the section and move
on.

**5. Get the cold read.** Dispatch `harness:adversary` with the spec path and the instruction that this is the spec
stage. Nothing else: no summary of the interview, no account of why the spec says what it says. If the spec adds or
changes anything a user calls, types, or clicks, dispatch `harness:api-critic` on the spec at the same time.

**6. Bring it to the user.** In chat, in this order:

- If the adversary's verdict is `should not exist`, that first, with its reasoning, before anything else.
- The spec in full, and its path.
- The findings, each with what you recommend: fold it in, or decline it and why.

**7. Amend or sign.** Fold in what the user accepts. If the outcome changed materially, offer one more adversary pass
rather than running it unasked. When the user says they sign, fill in the sign-off line with today's date and their
name. Signing is theirs alone; "looks good" about one section is not a signature.

Then say the next step is `/harness:plan` and stop.
