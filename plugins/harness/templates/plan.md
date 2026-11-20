# Plan: <topic>

Spec: `specs/<slug>/spec.md`, signed YYYY-MM-DD.

## Approach

<A short paragraph: how this gets the spec's outcome, and why this way over the obvious alternative.>

## Checks

The commands that decide whether this project is healthy. Found by reading the project, not guessed.

- Tests: `<command>`
- Lint and format: `<command, or "none">`
- Types: `<command, or "none">`
- Build or docs: `<command, or "none">`
- Run the app: `<command and URL, or "no UI">`

## Workstreams

In the order they run.

### 1. <name>

- **Delivers:** <what exists when this is done, in one or two sentences>
- **Done when:** <checkable criteria>
- **Needs:** <code | code, tests | code, tests, docs | docs>
- **Interface change:** <yes | no>
- **UI:** <yes | no>
- **After:** <workstream numbers this depends on, or "none">
- **Hard to undo:** <no | yes: what, and why a revert would not restore it>

## Delivery

- **Commits:** <one commit per workstream on branch `<name>` | leave changes in the working tree>
- **Pace:** <run through | pause after each workstream>

## Open decisions

- <A decision the user still owes, with the recommended answer. "None." is fine.>

## Amendments

Append-only. Each entry: the date, what triggered it, what changed, which workstreams it touches.

## Log

Append-only, written by the hub. One entry per event: plan accepted, preflight result, each workstream's outcome with
the findings raised and what was done about each, each halt and how it resolved.
