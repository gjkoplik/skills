# CLAUDE.md

Working instructions for agents in this repo. Operational, not subject matter. Anything about visualization itself belongs in `wiki/`, and anything about how to gather it belongs here.

## What this repo is

A quality bar for figures (`SKILL.md`), plus the research behind it (`wiki/`). Distributed as a Claude Code plugin.

`SKILL.md` is the only file that loads into a user's context. The wiki is for humans reading the repo and for agents extending it.

## The two labels, and why they exist

Every wiki page carries a **status**: `primary-read` (someone opened the actual source; quotes come from a local extraction), `secondary-only` (reached through an abstract or summary), `not-reached` (say where you looked).

Every rule carries an **evidence class**: evidence-backed, authority-asserted, or contested.

They are independent, and neither is decoration. Roughly a third of the received wisdom in this field failed when someone opened the primary. **Never upgrade a convention into a finding.**

## Retrieval

Provenance belongs on the page ("extracted locally with `pdftotext`"). The mechanics below do not; they live here.

- **Never quote from a fetch summary.** A summarizer once returned, inside quotation marks, the reverse of a paper's stated conclusion. Download the source and extract locally.
- **A 403 or an apparently broken PDF is usually the server refusing your client.** Try `curl -sL -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"`, and add `-e <referring page>` when a publisher checks the referer. Three sources were wrongly recorded as unreachable before this was understood, including one filed as an encrypted binary that was neither.
- **Check for a local copy** before recording anything as unreachable.
- **PDF text layers misreport tables.** Interleaved metric blocks and vertically centered cells both shift values into the wrong rows. Cross-check any table number against the running text, and prefer an HTML rendering when one exists.
- **Text layers silently drop characters**, notably `±` and comparison operators, which is the difference between a bound and its negation.
- Public-domain and pre-1930 works are often at archive.org, Gallica or Monoskop. Author pages and institutional repositories frequently host a copy the publisher paywalls.

## House style

- **No em-dashes** outside a direct quotation.
- **American spelling** outside quotes. Quote British spelling verbatim when quoting.
- Direct, slightly informal. No "delve", "moreover", "furthermore", "it is worth noting that". No throat-clearing preambles.
- Do not pad. A page that says less and is true beats a long one.

CI enforces the first two, ignoring quotations, blockquotes and backticks.

## Page schema

Near the top of every wiki page: what it is, its status, what it is good for, what it does not settle. Then substance, then links.

Link between pages rather than repeating them. Cite inventory topics by number.

## Topic numbering

`wiki/inventory.md` topic numbers are referenced across the wiki. **They are stable and have gaps.** Do not renumber to close a gap.

## Scope

How figures encode data and how readers read them. Where a rule has a mechanical and a social reading, the mechanical one is the one here.

## Working conventions

- Do not commit or change git state. The maintainer reviews and commits.
- When several agents work at once, each owns its own files. Do not edit another agent's pages; report the problem instead.
- Before publishing, run `claude plugin validate . --strict`. CI additionally checks relative links, house style, and that `plugin.json`'s version matches the tag `marketplace.json` pins to.
- Releases are tags. See `RELEASING.md`.
