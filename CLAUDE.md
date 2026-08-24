# CLAUDE.md

Working instructions for agents in this repo. Operational, not subject matter.

## What this repo is

A marketplace plus the plugins it lists, in one tree. Each plugin under `plugins/` is self-contained: its own
`.claude-plugin/plugin.json`, its own skill, its own changelog, its own version.

## Layout

- `.claude-plugin/marketplace.json` is the only marketplace. One per name per user, so this file is the namespace.
- `plugins/<name>/` is a whole plugin. It is copied to a cache at install time and **cannot read files outside its
  own directory**. No `../shared`. If two plugins need the same asset, each gets a copy.
- `.claude/` is this repo's own tooling, not shipped to anyone: the wiki-maintenance skill and the scheduled sweep.
- **Do not put a `CLAUDE.md` inside `plugins/<name>/`.** It would be copied into every user's install and do nothing
  there. This file loads for work anywhere in the tree, so per-plugin instructions belong here, in their own section.

## Versioning

Two levels, and they answer different questions.

- **Per plugin: semantic versioning**, tracked in `plugins/<name>/CHANGELOG.md`. This is what a user sees.
  **Every plugin is pinned to its own `<name>--v<version>` tag in `marketplace.json`.** Never use a relative-path
  source: it resolves against the default branch, so a fresh install would pull unreleased work off `main`. The
  version field gates updates for existing installs; only the pin protects a first install.
- **This repo: calendar versioning**, tracked in the root `CHANGELOG.md`. A repo release records which plugin
  versions moved and does not carry meaning of its own.

`marketplace.json` on `main` decides **which tag** each plugin sits at; the tag decides **what content** ships.
Pushing plugin code to `main` therefore reaches nobody, and pushing a changed pin is the release. See `RELEASING.md`.
Do not invent a version for the repo in any manifest; the repo's version is its tag.

## Working conventions

- Do not commit or change git state. The maintainer reviews and commits.
- When several agents work at once, each owns its own files. Do not edit another agent's pages; report the problem.
- Run `claude plugin validate . --strict` and `claude plugin validate ./plugins/<name> --strict` for anything you
  touched. `--strict` is what catches unparseable frontmatter, which loads at runtime as **empty metadata with every
  field silently dropped** rather than as an error.
- **A `description` containing `: ` must be quoted.** This shipped twice before anyone noticed.
- `claude plugin validate` only scans `skills/<name>/SKILL.md`. A root-level `SKILL.md` is never checked by it, which
  is why CI parses every `SKILL.md` in the tree separately.
- claude.ai, the Skills API and `package_skill.py` accept only `name`, `description`, `license`, `compatibility`,
  `metadata` and `allowed-tools`. Anything else, including `disable-model-invocation`, pins a skill to Claude Code.

## House style

- **No em-dashes** outside a direct quotation.
- **American spelling** outside quotes. Quote British spelling verbatim when quoting.
- Direct, slightly informal. No "delve", "moreover", "furthermore", "it is worth noting that". No throat-clearing.
- Do not pad. A page that says less and is true beats a long one.

Not enforced in CI. It was, and checking punctuation on every push cost more attention than it returned.

---

# plugins/agent-viz

A quality bar for figures (`SKILL.md`), plus the research behind it (`wiki/`). Anything about visualization itself
belongs in `wiki/`, and anything about how to gather it belongs here.

`SKILL.md` is the only file that loads into a user's context. The wiki is for humans reading the repo and for agents
extending it.

## The two labels, and why they exist

Every wiki page carries a **status**: `primary-read` (someone opened the actual source; quotes come from a local
extraction), `secondary-only` (reached through an abstract or summary), `not-reached` (say where you looked).

Every rule carries an **evidence class**: evidence-backed, authority-asserted, or contested.

They are independent, and neither is decoration. Roughly a third of the received wisdom in this field failed when
someone opened the primary. **Never upgrade a convention into a finding.**

## Retrieval

Provenance belongs on the page ("extracted locally with `pdftotext`"). The mechanics below do not; they live here.

- **Never quote from a fetch summary.** A summarizer once returned, inside quotation marks, the reverse of a paper's
  stated conclusion. Download the source and extract locally.
- **A 403 or an apparently broken PDF is usually the server refusing your client.** Try `curl -sL -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"`, and add `-e <referring page>` when a publisher checks the referer. Three sources were wrongly recorded as unreachable before this was understood, including one filed as an encrypted binary that was neither.
- **Check for a local copy** before recording anything as unreachable.
- **PDF text layers misreport tables.** Interleaved metric blocks and vertically centered cells both shift values into the wrong rows. Cross-check any table number against the running text, and prefer an HTML rendering when one exists.
- **Text layers silently drop characters**, notably `±` and comparison operators, which is the difference between a bound and its negation.
- Public-domain and pre-1930 works are often at archive.org, Gallica or Monoskop. Author pages and institutional repositories frequently host a copy the publisher paywalls.

## Page schema

Near the top of every wiki page: what it is, its status, what it is good for, what it does not settle. Then
substance, then links.

Link between pages rather than repeating them. Cite inventory topics by number.

## Topic numbering

`wiki/inventory.md` topic numbers are referenced across the wiki. **They are stable and have gaps.** Do not renumber
to close a gap.

## Scope

How figures encode data and how readers read them. Where a rule has a mechanical and a social reading, the mechanical
one is the one here.

---

# plugins/what-if

A cheap triage skill with no subject of its own. It writes reports into whatever repo it is pointed at, never into
this one.

Its own conventions live in its `SKILL.md`, which is the spec rather than documentation of one. The two that get
broken most often: it never implements and never produces a plan.
