# Changelog

A summary of what changed in the quality bar and the research behind it.

Semantic versioning, most recent release first. A release is a git tag; there is no build or publish step, so see
[RELEASING.md](RELEASING.md). While the version is `0.0.x`, the shape is still moving and anything can change without
ceremony.

## 0.0.1

First public cut, deliberately early. The sourcing is real and the structure is not settled, which is what the version
number is for.

A quality bar for figures aimed at coding agents rather than at people, because that guidance did not appear to exist.
Style guides are written for humans and rubrics are written to grade finished charts; nothing addressed the moment an
agent is about to draw something.

### Added

- `viz-quality-bar` as a general figure bar: a **floor** of quantitative honesty, statistical honesty and accessibility
  that binds on every figure, and a **ceiling** of narrative polish that scales with the figure's job. A deliberately
  minimal figure is judged correct rather than unfinished, which is what keeps a bar this size from turning an API demo
  into a forty-item defect list.
- Evidence class on every rule. What a study established is stated flatly, what a design book asserts is stated as a
  default, and the two are never conflated. Several rules got less authoritative-sounding as a result, which is the
  correct direction.
- The skill translates the field's jargon before speaking to anyone, and asks which kind of figure it is drawing when
  that is not obvious. Almost nobody is in the weeds on visualization and everybody makes figures anyway.
- A wiki with one page per source and per study, each recording whether anyone actually opened the primary. Also
  runnable checks: most of the honesty rules mechanize, and the whole battery runs in well under a second.
- CI that validates the manifests, checks every relative link, holds house style, and refuses a release whose version
  and tag disagree or whose tag was never pushed.

### Fixed

Corrections to things this project itself had wrong before publishing:

- The recommendation to split the skill was withdrawn. Every number behind it was right and the inference was not: an
  invoked skill loads whole, and splitting one into two consumes two slots against the same budget.
- "Bank to 45 degrees" is scope-limited rather than general, the axis-break remedy for truncation was tested and did
  not measurably work, the flat ban on dual axes has no supporting experiment, and "log scales are fine for experts"
  fails at 56% against 93% among 623 ecologists.
- Gray-plus-one-accent, a rule this bar uses and recommends, has no controlled study behind it. Both practitioners it
  is credited to assert it in their own words and neither cites one.
- Bertin describes eight visual variables, not the seven usually quoted, and the collapse breaks the argument it came
  from. He also ran no experiments.
- One cited paper contains arithmetically impossible numbers and is named as not-to-be-cited. Another contradicts
  itself between its table and its discussion.

### Known limits

- Five pages are `secondary-only`. Tufte is thin, and worse, he was never enumerated in the coverage audit, so the
  audit's own guarantee does not cover him.
- Chart-type selection is upstream of everything here and only partly written.
- Accessibility duplicates an existing licensed inventory that should be imported rather than re-derived.
- Every check is matplotlib-tested. Nothing is claimed about how they translate.
