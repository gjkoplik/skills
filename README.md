# skills

Gary Koplik's Claude Code plugins, and the marketplace that lists them.

```
/plugin marketplace add gjkoplik/skills
```

## What is here

| Plugin | What it does | Lives in |
| --- | --- | --- |
| [`agent-viz`](https://github.com/gjkoplik/agent-viz) | A researched quality bar for any figure a person will look at, plus the wiki it came from. | its own repo |
| [`what-if`](plugins/what-if) | A cheap look at a half-formed idea before committing to a conversation about it. | `plugins/what-if` |

```
/plugin install agent-viz@skills
/plugin install what-if@skills
```

## Why some plugins are not in this repo

A **subject** repo is a body of research plus a skill distilled from it. `agent-viz` is one: 41 wiki pages, an
evidence-class discipline, a weekly research sweep, and CI that enforces all of it. Folding that into a general
skills repo would put two unlike governance regimes in one tree and dilute a repo whose legibility is part of its
value.

A marketplace can list plugins sourced from other repos, so one install surface does not require one tree. Subject
repos stay where they are and get listed here by tag. Skills with no subject, like `what-if`, live here under
`plugins/`.

The rule of thumb: **if it needs its own contributing guide, it needs its own repo.**

## Releases

Every entry in the marketplace is pinned to a tag, so a push never reaches a user unreviewed. See [RELEASING.md](RELEASING.md).

## License

MIT.
