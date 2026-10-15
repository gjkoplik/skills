# Contributing

The most useful contribution is not a new rule. It is opening a source somebody else could not reach and correcting what was written from a summary.

## The one rule that matters

Every claim carries where it came from and how good the warrant is, as two independent labels.

**Status**, on every wiki page: `primary-read` (you opened it, and quotes come from a local extraction), `secondary-only` (an abstract or summary; say so next to the quote), `not-reached` (say where you looked).

**Evidence class**, on every rule: evidence-backed (a study, experiment or standard), authority-asserted (a practitioner says so, which is fine as a default), or contested (the record disagrees with itself; say so rather than picking a side).

Never upgrade a convention into a finding.

## Worth doing, in order

1. **Clear a `secondary-only` page.** Munzner, Cairo, Tufte, Gillan & Richman and Menge are waiting on someone with a copy.
2. **Correct something.** A wrong quote, a misattributed citation, an overstated rule. This has happened repeatedly here, including to the maintainer.
3. **Add a checks file for another ecosystem.** Everything is matplotlib-tested. Schema: the rule, the literal check, what it costs to run, and any trap you hit.
4. **Add a chart-type page.** The tier is organized by data relationship and is incomplete; the coverage table in [wiki/chart-types/README.md](wiki/chart-types/README.md) lists what is missing.

The page schema, the required sections and the validator live in the repo's own `.claude/skills/agent-viz-wiki/` and are not shipped with the plugin.

## Retrieval hazards

Each of these produced confidently wrong output here.

- **A summarizer once returned the reverse of a paper's conclusion inside quotation marks.** Never quote from a fetch summary. Download and extract locally.
- **A 403 is usually the server refusing your client.** Try `curl -sL -A "Mozilla/5.0"`, and `-e` for a referer. Three sources were wrongly recorded as unreachable before this was understood.
- **PDF text layers misreport tables** and silently drop characters like `±` and comparison operators. Cross-check any table value against the running text.
- **Check for a local copy** before recording anything as unreachable.

## House style

No em-dashes outside a quotation. American spelling outside quotes. Direct, slightly informal, no filler. Do not pad. Not machine-checked; read your own prose.

## Scope

How figures encode data and how readers read them. Where a rule has a mechanical and a social reading, the mechanical one is the one here.

## Checks

```
claude plugin validate ./plugins/agent-viz --strict
```

CI additionally checks that relative links resolve, that every `SKILL.md` has parseable frontmatter, and that each plugin is pinned to a tag that exists.

## Cutting a release

Add the entry to [CHANGELOG.md](CHANGELOG.md). In one commit, bump `version` in `.claude-plugin/plugin.json` and set this plugin's `ref` in the repo's `.claude-plugin/marketplace.json` to the matching `agent-viz--v<version>`. Then:

```
claude plugin tag ./plugins/agent-viz --push
```

Pushing plugin code to `main` reaches nobody. Pushing the changed pin is the release. Full detail in [RELEASING.md](../../RELEASING.md).
