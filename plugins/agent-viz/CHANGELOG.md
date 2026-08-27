# Changelog

A summary of what changed in the quality bar and the research behind it.

Semantic versioning, most recent release first. A release is a git tag; there is no build or publish step, so see
[RELEASING.md](../../RELEASING.md). While the version is `0.0.x`, the shape is still moving and anything can change without
ceremony.

**This file answers *what does the bar now tell me to do*.** What the research itself learned, which is usually
a different event on a different clock, is in [wiki/CHANGELOG.md](wiki/CHANGELOG.md). Entries here link there
rather than restating it.

## 0.0.1

First public cut, deliberately early. The sourcing is real and the structure is not settled, which is what the version
number is for.

A quality bar for figures aimed at coding agents rather than at people, because that guidance did not appear to exist.
Style guides are written for humans and rubrics are written to grade finished charts; nothing addressed the moment an
agent is about to draw something.

### What it is

- `viz-quality-bar` as a general figure bar: a **floor** of quantitative honesty, statistical honesty and accessibility
  that binds on every figure, and a **ceiling** of narrative polish that scales with the figure's job. A deliberately
  minimal figure is judged correct rather than unfinished, which is what keeps a bar this size from turning an API demo
  into a forty-item defect list.
- Evidence class on every rule. What a study established is stated flatly, what a design book asserts is stated as a
  default, and the two are never conflated. Several rules got less authoritative-sounding as a result, which is the
  correct direction.
- **Chart-type selection, as a routine rather than a lookup table.** The bar asks whether this should be a chart at
  all, names the reader's question out loud so it can be corrected, routes to exactly one index, and opens the index
  before any type page, because a type page is written to be fair to its subject and reading one first confirms
  whatever was already proposed. It also says how hard to push: floor violations stay firm, form suggestions are
  offered once and let go, and once the user says keep it, it is settled.
- **A two-tier chart-type wiki**: 40 type pages stored flat, grouped by 12 index pages rather than by directory,
  because a data relationship is a view of a chart and not a property of it. All nine FT relationships have an index,
  plus three of ours. Every type page carries a six-slot structural decomposition, and evidence is inherited from the
  channel tier with a link rather than restated as a native finding.
- The skill translates the field's jargon before speaking to anyone, and asks which kind of figure it is drawing when
  that is not obvious. Almost nobody is in the weeds on visualization and everybody makes figures anyway.
- A wiki with one page per source and per study, each recording whether anyone actually opened the primary. Also
  runnable checks: most of the honesty rules mechanize, and the whole battery runs in well under a second.
- CI that validates the manifests, checks every relative link, holds house style, and refuses a release whose version
  and tag disagree or whose tag was never pushed.

### What it says that the received wisdom does not

The reason for the whole project. Each of these is a rule in wide circulation that changed or died when somebody
opened the primary source. Full treatment, with the sources, in
[wiki/refutations.md](wiki/refutations.md).

- The recommendation to split the skill was withdrawn. Every number behind it was right and the inference was not: an
  invoked skill loads whole, and splitting one into two consumes two slots against the same budget.
- "Bank to 45 degrees" is scope-limited rather than general, the axis-break remedy for truncation was tested and did
  not measurably work, the flat ban on dual axes has no supporting experiment, and "log scales are fine for experts"
  fails at 56% against 93% among 623 ecologists.
- **"Pies are read by angle" is refuted** by the one study that isolated the three cues; angle is the least used. The
  case against donut charts collapses with it, and the usual reason given for preferring bars over pies goes with it.
  Bars do beat pies for value extraction, measured and replicated. The mechanism everyone cites for it does not hold.
- **The Cleveland-McGill ranking is two rankings**, 1984 and 1985, which disagree from area downward. The list everyone
  reproduces is the 1985 one, routinely cited to 1984. No page here states a bare rank number, because the number
  silently depends on which table was meant.
- Gray-plus-one-accent, a rule this bar uses and recommends, has no controlled study behind it. Both practitioners it
  is credited to assert it in their own words and neither cites one.
- Bertin describes eight visual variables, not the seven usually quoted, and the collapse breaks the argument it came
  from. He also ran no experiments.
- One cited paper contains arithmetically impossible numbers and is named as not-to-be-cited. Another contradicts
  itself between its table and its discussion.

### Known limits

- Six pages are `secondary-only`. Tufte is thin, and worse, he was never enumerated in the coverage audit, so the
  audit's own guarantee does not cover him.
- **The chart-type tier is broad and thin, and the thinness is the honest part.** 31 of the 40 type pages say
  plainly that no study in this corpus tests the form. Deviation, ranking, spatial and flow have no experiment behind
  any of their forms at all. Those pages inherit what they can and then stop, rather than filling the gap with
  plausible practitioner advice.
- Chart names are only partly resolvable. [wiki/chart-types/aliases.md](wiki/chart-types/aliases.md) maps 103 names
  to pages, but **43 of them are in circulation with no source here defining them**. Several pages say outright
  that no source in the corpus defines the term they are named after, and three collisions are flagged unresolved:
  "mosaic plot", "heat map" and "range plot". A name-resolution index is the next piece of work.
- Accessibility duplicates an existing licensed inventory that should be imported rather than re-derived.
- Every check is matplotlib-tested. Nothing is claimed about how they translate.
