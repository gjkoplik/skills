# CLAUDE.md

Working instructions for agents in this repo.

## What this repo is

A marketplace plus the plugins that have no subject repo of their own. `agent-viz` is listed here and lives
elsewhere; see the README for the split and the rule of thumb behind it.

## Layout

- `.claude-plugin/marketplace.json` is the only marketplace. One per name per user, so this file is the namespace.
- `plugins/<name>/` is a self-contained plugin: its own `.claude-plugin/plugin.json` and `skills/<name>/SKILL.md`.
- **A plugin is copied to a cache at install time and cannot read files outside its own directory.** No `../shared`.
  If two plugins need the same asset, each gets a copy.

## Conventions

- Do not commit or change git state. The maintainer reviews and commits.
- Run `claude plugin validate . --strict` before publishing, and `claude plugin validate ./plugins/<name> --strict`
  for a plugin you touched. `--strict` is what catches unparseable frontmatter, which loads at runtime as **empty
  metadata with every field silently dropped** rather than as an error.
- A `description` containing `: ` must be quoted. This has already bitten once.
- claude.ai, the Skills API and `package_skill.py` accept only `name`, `description`, `license`, `compatibility`,
  `metadata` and `allowed-tools`. Anything else, including `disable-model-invocation`, pins a skill to Claude Code.
- Releases are tags. See `RELEASING.md`.

## House style

- **No em-dashes** outside a direct quotation.
- **American spelling** outside quotes.
- Direct, slightly informal. No "delve", "moreover", "furthermore", "it is worth noting that". No throat-clearing.
- Do not pad. A page that says less and is true beats a long one.

CI enforces the first two, ignoring quotations, blockquotes and backticks.
