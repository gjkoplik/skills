# Changelog

Releases of this repo, most recent first. Calendar versioned, `vYYYY.MM.DD`. A repo release carries no meaning of its
own: it records which plugin versions were current at a point in time.

Per-plugin history, which is the one that matters to a user, lives with the plugin:

- [plugins/agent-viz/CHANGELOG.md](plugins/agent-viz/CHANGELOG.md)
- [plugins/what-if/CHANGELOG.md](plugins/what-if/CHANGELOG.md)

See [RELEASING.md](RELEASING.md).

## Unreleased

| Plugin | Version |
| --- | --- |
| agent-viz | 0.0.1 |
| what-if | 0.0.1 |

### Added

- `what-if`, a cheap sunk-cost circuit breaker for half-formed ideas. New in this repo.

### Changed

- **agent-viz moved here from its own repo**, with history, and is now `plugins/agent-viz`. It was a day old with no
  stars, forks or inbound references, so nothing depended on the old location. The split had been costing a two-step
  release across two repos, a cross-repo pin that CI had to reach the network to verify, two CI configs and two
  release procedures, for a separation with no audience to serve.
- The marketplace pins each plugin to its own `<name>--v<version>` tag with a `git-subdir` source. A relative-path
  source resolves against the default branch, so a fresh install would have pulled unreleased work off `main`; the
  `version` field gates updates for existing installs but does nothing for a first install.
- House style is no longer checked in CI. Punctuation checks on every push cost more attention than they returned.
- Repo tooling that is not shipped to anyone (the wiki-maintenance skill, the weekly sweep) moved to `.claude/` at the
  repo root. A `CLAUDE.md` inside a plugin directory is copied into every install and does nothing there, so
  agent-viz's working instructions moved into the root `CLAUDE.md` as a section.

### Fixed

- **agent-viz CI had never run a single job.** Its workflow file contained a literal `0x08` byte where `\b` was meant
  in a regex, and GitHub refuses to load a workflow containing a control character. Every check the repo believed it
  had was decorative.
- **Two `SKILL.md` files had unparseable frontmatter**, both from a bare `: ` in an unquoted description. Such a skill
  loads with every frontmatter field silently dropped. `claude plugin validate` never caught agent-viz's because it
  only scans `skills/<name>/SKILL.md` and that skill sits at its plugin root; CI now parses every `SKILL.md` in the
  tree.
