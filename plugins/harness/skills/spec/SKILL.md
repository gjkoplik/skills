---
name: spec
description: 'Turn a request into a one-page spec the user signs before any planning or code. Interviews the user where the request leaves the outcome open, drafts the spec from their answers, has them name how it could fail, gets a cold adversarial read, and stops for their signature. The first of four stages. Not for one-line fixes. Run it when the user asks for this stage, by typing /harness:spec or by saying so ("run the harness spec", "spec this out with the harness"). Never run it on your own initiative, and never to carry on from the previous stage without being asked.'
argument-hint: '[what you want built]'
---

# Spec

The first stage of the harness. It ends with a signed spec and nothing else: no plan, no code.

Read `${CLAUDE_PLUGIN_ROOT}/hub.md` first if you have not this session. You are the hub.

The request: $ARGUMENTS

If there is no request above, ask for one. If the work is trivial (a one-line fix, a typo), say so and suggest doing
it directly; the harness costs more than it returns on small things. This stage needs the user present. If nobody is
there to answer, stop and say so; do not guess your way to a draft.

## What a spec is

One page stating the problem, what will be true for a user when the work ships, and the user API: the literal thing
they call, type, or click to get it. It is the
intent, written down so that the user can sign it and every later agent can be held to it.

It is not a plan. No approach, no file lists, no sequencing, no done-when criteria. A spec that reads like a plan is
one the user will skim, and a skimmed signature is worth nothing. Keep it to a page; if it will not fit, ask whether
it is two specs.

## The stage

**1. Understand the request.** Pick a short slug. Read enough of the repo to know what exists, what the request
would touch, and whether something already does it. Check `specs/` for a related or archived spec. A change to
something an archived spec already shipped gets a new, small spec that names what it changes; archived specs are not
reopened.

If the request bundles several things that could each ship and be checked on their own, propose the split before
drafting anything: a few lines naming each piece and the order. One spec per piece.

**2. Interview, where the request leaves the outcome open.** Open with your read: one sentence on what you think
they want, and the assumptions you would otherwise fill in silently, so they can correct those first. Then one
question at a time, each with your recommended answer. Go after the forks that change what gets built: how ambitious
(all of it, or the core), what is deliberately out, what they would literally type or click, and why now. Skip
anything the request or the repo already settles.

Listen for the answer that sounds like what a careful engineer is supposed to say ("scalable", "the standard way")
with nothing specific behind it. That is usually not what they want; ask what they would want if they did not have
to justify it. You are done when you could predict their reaction to your next three questions, or when they say
enough. If the request already determines the outcome, skip the interview and say that you did.

**3. Draft.** Copy `${CLAUDE_PLUGIN_ROOT}/templates/spec.md` to `specs/<slug>/spec.md` and fill it from the user's
words. Write the outcome so a plausible wrong implementation contradicts it: "search is faster" cannot be checked
against a diff, "a search over 100k documents returns in under a second from the existing search box" can. Write
"User API" from the entry point a user would actually reach for, and try it against the code as it stands
so you know which parts do not exist yet. Leave Failure modes empty for now.

**Cite what you assert.** The user signs this page without re-deriving it, so every factual claim on it has to be
checkable from the page. A claim about the current code carries `path:line`, and the spec names the
commit those lines were read at, once, under Problem. Lines move as other people push; the commit is what keeps a
citation checkable next month. A claim about a library, a standard, or
an earlier decision carries a link to where it says so, and you open that source yourself before citing it; do not
cite from memory. A claim you could not check stays in only if it is marked (unverified), which tells the user and
the adversary exactly where the spec is resting on a guess. What the user told you needs no citation; it is theirs.

**4. Ask the user how it could fail.** What would make this hollow, wrong, or fake even with every test green? A
feature nobody needed, a default that quietly breaks a common case, a result that only holds the way it was measured.
Ask first and write down what they say in their words. Do not lead with your own list: a list you wrote has your
blind spots, and the user will nod along to it. If they would rather skip this, record that in the section and move
on.

**5. Get the cold read.** Dispatch `harness:design-adversary` with the spec path and the instruction that this is the spec
stage. Nothing else: no summary of the interview, no account of why the spec says what it says. If the spec adds or
changes anything a user calls, types, or clicks, dispatch `harness:api-critic` on the spec at the same time.

**6. Bring it to the user.** In chat, in this order:

- If the adversary's verdict is `should not exist`, that first, with its reasoning, before anything else.
- The spec in full, and its path.
- The findings, each with what you recommend: fold it in, or decline it and why.

**7. Amend or sign.** Fold in what the user accepts. If the outcome changed materially, offer one more adversary pass
rather than running it unasked. When the user says they sign, fill in the sign-off line with today's date and their
name. Signing is theirs alone, and it is an explicit yes. "Looks good", "sure", and "whatever you think" are not
signatures; ask plainly.

Then say the next step is `/harness:plan` and stop.
