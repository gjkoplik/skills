# skills

Gary Koplik's Claude Code plugins, and the marketplace that lists them.

```
/plugin marketplace add gjkoplik/skills
```

## What's here

| Plugin | What it does | |
| --- | --- | --- |
| **agent-viz** | A researched quality bar for any figure a person will look at, plus the 41-page wiki it came from. | [`plugins/agent-viz`](plugins/agent-viz) |
| **what-if** | A cheap look at a half-formed idea before committing to a conversation about it. | [`plugins/what-if`](plugins/what-if) |

```
/plugin install agent-viz@skills
/plugin install what-if@skills
```

## Why one repo

Each plugin is self-contained under `plugins/`: its own manifest, its own skill, its own changelog, its own version. A
plugin is copied to a cache at install time and cannot read outside its own directory, so the boundary is real rather
than conventional.

agent-viz lived in its own repo first, on the theory that a body of research plus a skill distilled from it is a
different kind of thing from a skill with no subject. That theory was not wrong, but it cost a two-step release across
two repos, a cross-repo pin CI had to hit the network to verify, and two of everything else, to serve an audience that
did not exist. Splitting one back out is `git subtree split` and a marketplace rename, so being wrong here is cheap in
both directions.

## Versions

Two levels. Plugins use semantic versioning and carry their own changelogs, and that is the number you see when you
install one. The repo cuts calendar-versioned releases that only record which plugin versions were current.

Every plugin is pinned to its own tag, so what you install is a frozen release rather than whatever happened to be on
`main` when you ran the command. See [RELEASING.md](RELEASING.md) and [CHANGELOG.md](CHANGELOG.md).

## License

MIT.
