# Spec: <topic>

## Problem

<What exists today and what is wrong or missing, in a few sentences. Who runs into it, doing what. Every claim about
the current code cites `path:line`; every claim about something external links to its source; a claim nobody checked
is marked (unverified).>

Code is cited as of commit `<short sha>`.

## Outcome

<What is true for a user once this ships, in the words that user would use. A few sentences. Written so that a
plausible wrong implementation contradicts it.>

## User API

<What a user touches to get each benefit the outcome claims: the function they call, the command they type, the
setting they change, the screen they click through. Show it as they would actually use it, starting from nothing,
with real code or real commands and no placeholders. One block per benefit. For anything new or changed, show its
whole shape: every argument with its default, every flag, every field. Where it needs something that does not exist
yet, name it.>

## Out of scope

- <What this deliberately does not do, especially the adjacent thing a reader would assume it covers. If it was
  parked as an idea, link the idea. "None." is fine.>

## Failure modes

<The ways this could be hollow, wrong, or fake with everything shipped and green. Named by the user, in their words,
one line each. If the user chose not to name any, say so here.>

- <failure mode>

## Open questions

- <A question that would change this spec if it resolved differently, and what would settle it. "None." is fine.>

## Sign-off

Only the user signs. A change to what this spec promises is a re-sign, recorded as a new line below. Lines here are
never edited or removed.

```
Signed YYYY-MM-DD by <name>.
```
