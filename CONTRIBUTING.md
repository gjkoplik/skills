# Contributing

The most useful contribution is not a new rule. It is **opening a source somebody else could not reach** and correcting what we wrote from a summary.

## The one rule that matters

Every claim carries where it came from and how good the warrant is. Two independent labels.

**Status**, on every wiki page: `primary-read` (you opened it, quotes come from a local extraction), `secondary-only` (abstract or summary, say so next to the quote), `not-reached` (say where you looked).

**Evidence class**, on every rule: **evidence-backed** (study, experiment, standard), **authority-asserted** (a practitioner says so, which is fine as a default), or **contested** (the record disagrees with itself; say so rather than picking a side).

Never upgrade a convention into a finding. That is the failure this repo exists to correct.

## Worth doing, in order

1. **Clear a `secondary-only` page.** Munzner, Cairo, Tufte, Gillan & Richman and Menge are waiting on someone with a copy.
2. **Correct something.** Wrong quote, misattributed citation, overstated rule. This has happened repeatedly here, including to the maintainer.
3. **Add a checks file for another ecosystem.** Everything is matplotlib-tested. Schema: the rule, the literal check, what it costs to run, and any trap you hit.
4. **Fill a chart-type page.** That tier is organized by data relationship and is incomplete.

## Retrieval hazards

Each of these produced confidently wrong output here:

- **A summarizer once returned the reverse of a paper's conclusion inside quotation marks.** Never quote from a fetch summary. Download and extract locally.
- **A 403 is usually the server refusing your client, not an unreachable source.** Try `curl -sL -A "Mozilla/5.0"`, and `-e` for a referer. Three sources were wrongly recorded as unreachable before this was understood.
- **PDF text layers lie about tables** and silently drop characters like `±` and comparison operators. Cross-check any table value against the running text.
- **Check for a local copy** before recording anything as unreachable.

## House style

No em-dashes outside a quotation. American spelling outside quotes. Direct, slightly informal, no filler. Do not pad. CI enforces the first two, ignoring quotations, blockquotes and backticks.

## Scope

How figures encode data and how readers read them. Where a rule has a mechanical and a social reading, the mechanical one is the one here.

## Checks

```
claude plugin validate . --strict
```

CI additionally checks that relative links resolve, that house style holds, and that `plugin.json`'s version has a tag that was actually pushed.

## Cutting a release

Bump `version` in `.claude-plugin/plugin.json`, commit, then:

```
git tag v0.0.2 && git push origin main --follow-tags
```

Then move the pin in the marketplace repo, which is a separate step in a separate repo.

The `release-tag` CI job fails if the tag named by the version does not exist. That check matters: **a marketplace pinned to a tag nobody pushed fails at install time for everyone, and you will not see it locally.**

Full detail in [RELEASING.md](RELEASING.md).
