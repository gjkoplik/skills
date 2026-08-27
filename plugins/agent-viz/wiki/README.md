# The agent-viz wiki

One page per thing. A source gets a page, a study gets a page, an idea that took work to arrive at gets a page. Pages link to each other rather than repeating each other.

A later reader can pick up any single thread without rerunning the research, and can see **what each source is actually good for** rather than a flat citation list.

## Page schema

**Facts live in frontmatter. Argument lives in the body.** They are not allowed to be the same thing, because for a long time they were, and it cost accuracy.

```yaml
---
type: source | study | person | concept | chart-type | index
status: primary-read | secondary-only | not-reached   # research pages only
status_partial: true            # present when coverage is not uniform
retrieved: YYYY-MM-DD
author: <people-page slug>      # where a source has a known author
relationships: [part-to-whole]  # chart-type pages only
---
```

**Why this replaced a prose header.** The status label used to live in a sentence, and the sentence had at least four shapes (`**Status.**`, `**Status:**`, a `## Status` heading, and split labels like "`primary-read` for the papers, `secondary-only` for the book"). Three separate attempts to count the corpus produced three different answers, all wrong, because they were regexes over English. The count below is now a parse.

`author` exists because **independence is the wiki's most-used argument** ("three unrelated organizations", "a fourth independent source") and nothing recorded who wrote what. That gap produced a real error: the Urban Institute style guide and Jonathan Schwabish were counted as two voices when he is behind both. See [sources/urban-institute.md](sources/urban-institute.md).

**Status is not decoration.**

- `primary-read`: someone opened the actual source and quotes come from a local extraction.
- `secondary-only`: reached through abstracts or summaries. Treat quotes as unvouched.
- `not-reached`: could not get to it. The page says where it looked.
- `status_partial: true`: the page covers several artifacts and did not reach them all equally. The `status` field then records the **principal** subject, and the body says which parts are which. This is honest rather than sloppy: a page can legitimately be primary-read on the papers and secondary-only on the books. The count is in the state line below rather than repeated here, because the two disagreed within a day of being written.

**Body, by page type.**

- **Source, study, person:** *what it is good for*, *what it does not settle*, and a **"How this was read"** paragraph. That last one is not the status label restated and must never be trimmed as a duplicate: frontmatter carries the *label*, the paragraph carries the *provenance*. Which artifact was opened, how it was extracted, what was rendered to page images for want of a text layer, what was left unopened, and for a split status which label covers which material. Delete it and every `primary-read` in the corpus becomes unauditable, which would remove the one thing separating this wiki from a confident summary.
- **Concept:** keeps the full four-field block, including **What it is**, because a concept's slug does not convey it (`floor-and-ceiling` needs a sentence in a way `wilke-fundamentals` does not). Its `status` describes how the idea was arrived at, usually synthesis by this project, so it stays prose in the body and takes no frontmatter label. **These pages are correct as they stand; do not "fix" them to match the research pages.**
- **Chart-type and index:** no header block at all. One line of definition under the title, then straight to the decision, because that reader has already arrived with data in front of them and does not need to be sold on the page.
- **Directory READMEs** take no frontmatter. A navigation stub takes no header block either. A README that is really the design document for its tier may keep *what it is good for* and *what it does not settle*, but never a `Status` field: coverage belongs in a coverage table, where it can be checked, not in prose that drifts.

Several claims here changed when someone finally opened the primary. One cited paper turned out to contain arithmetically impossible numbers, and a web summarizer once returned, inside quotation marks, the reverse of a paper's stated conclusion. A `secondary-only` page has not earned the same trust as a `primary-read` one.

**Current state: 49 `primary-read`, 6 `secondary-only`, 0 `not-reached`, of which 23 are `status_partial`.** Counted across `sources/` (17), `studies/` (23) and `people/` (15) by parsing frontmatter. `concepts/` and `chart-types/` are synthesis and structure, and are not counted.

Two earlier versions of this line said 27 and then 50. Both were derived by pattern-matching prose and both were wrong, which is the whole argument for the schema above.

One reachability lesson, recorded because it cost a wrong label: Krzywinski et al. (2012) is paywalled with no open-access deposit and was written up as `not-reached` on that basis. A local copy existed the whole time. **Check for a local copy before recording a source as unreachable.**

## Start here

- [inventory.md](inventory.md): the 92 topics a general figure bar owes, derived blind from the canon. The spine everything else hangs off.
- [refutations.md](refutations.md): the highest-value page. Widely repeated rules that changed or died when someone read the source.
- [roll-call.md](roll-call.md): the audit trail proving the inventory's coverage, source by source, plus the four things the per-source pages found wrong with it.

## Sources

| Page | Status | Good for |
|---|---|---|
| [wilke-fundamentals.md](sources/wilke-fundamentals.md) | `primary-read` | The broadest single reference. Free online, 30 chapters, covers most of the inventory. |
| [munzner-vad.md](sources/munzner-vad.md) | `secondary-only` | Task and data abstraction, marks and channels, the nine rules of thumb. |
| [knaflic-swd.md](sources/knaflic-swd.md) | `primary-read` | Narrative, attention, decluttering. Chapter 1 in full; later chapters via the book's own index. |
| [cairo-truthful-art.md](sources/cairo-truthful-art.md) | `secondary-only` | The five qualities framing. Structure read; the argument was not. |
| [few-effectiveness-profile.md](sources/few-effectiveness-profile.md) | `primary-read` | Effectiveness criteria split into informative and emotive. Recovered after being recorded as unreadable. |
| [tufte.md](sources/tufte.md) | `secondary-only` | Data-ink, chartjunk. **Thin, and its own page explains why that matters.** |
| [matplotlib.md](sources/matplotlib.md) | `primary-read` | Colormap classes, perceptual uniformity, colorbars, style sheets. |
| [seaborn.md](sources/seaborn.md) | `primary-read` | Palettes, and the best short treatment of what an error bar means. |
| [vega-lite.md](sources/vega-lite.md) | `primary-read` | Opinions shipped as defaults, notably `zero: true`. |
| [observable-plot.md](sources/observable-plot.md) | `primary-read` | The turbo default, and a by-mark reading of proportional ink. |
| [bbc-cookbook.md](sources/bbc-cookbook.md) | `primary-read` | A newsroom house style shipped as a package. |
| [urban-institute.md](sources/urban-institute.md) | `primary-read` | The most rule-shaped style guide, plus a real accessibility section. |
| [datawrapper-academy.md](sources/datawrapper-academy.md) | `primary-read` | Color, accessibility, number formats, responsive sizing. |
| [ft-visual-vocabulary.md](sources/ft-visual-vocabulary.md) | `primary-read` | Chart-type selection by data relationship. The spine for any chart-chooser work. |
| [w3c-wai-complex-images.md](sources/w3c-wai-complex-images.md) | `primary-read` | The two-part alt text pattern, as a standard rather than an opinion. |
| [chartability.md](sources/chartability.md) | `primary-read` | 50 accessibility heuristics, CC BY-SA, with a 14-test shortlist. **Import this rather than re-deriving it.** |

## Studies

| Page | Status | The finding |
|---|---|---|
| [pandey-2015-deceptive-visualizations.md](studies/pandey-2015-deceptive-visualizations.md) | `primary-read` | Distortion measurably works. Also contradicts itself between table and discussion. |
| [correll-2020-truncating-the-y-axis.md](studies/correll-2020-truncating-the-y-axis.md) | `primary-read` | Truncation's exaggeration persists, and break glyphs did not measurably fix it. |
| [talbot-2012-slope-ratio.md](studies/talbot-2012-slope-ratio.md) | `primary-read` | Bank-to-45 is scope-limited, not general. |
| [isenberg-2011-dual-scale-charts.md](studies/isenberg-2011-dual-scale-charts.md) | `primary-read` | The paper cited for a dual-axis ban studied something else. |
| [menge-2018-log-scales.md](studies/menge-2018-log-scales.md) | `secondary-only` | Domain experts misread log-log badly. 56% against 93%. |
| [romano-2020-log-scales-covid.md](studies/romano-2020-log-scales-covid.md) | `primary-read` | Log scales changed comprehension, prediction and policy preference. |
| [ware-2023-rainbow-colormaps.md](studies/ware-2023-rainbow-colormaps.md) | `primary-read` | **Not a study.** A Viewpoints essay. Its page says so and names the real sources. |
| [cumming-2007-error-bars.md](studies/cumming-2007-error-bars.md) | `primary-read` | Numbered rules for error bars, including state what they are and state n. |
| [belia-2005-ci-misconceptions.md](studies/belia-2005-ci-misconceptions.md) | `primary-read` | 473 published authors, severe misconceptions about CIs and SE bars. |
| [correll-gleicher-2014-error-bars-harmful.md](studies/correll-gleicher-2014-error-bars-harmful.md) | `primary-read` | The error encoding changes the decision. Gradient and violin beat bar-and-whisker for inference. |
| [weissgerber-2015-beyond-bar-line.md](studies/weissgerber-2015-beyond-bar-line.md) | `primary-read` | 703-article review. At small n, plot the points. |
| [song-szafir-2019-missing-data.md](studies/song-szafir-2019-missing-data.md) | `primary-read` | Highlighting missing values raises perceived quality; breaking continuity biases interpretation. |
| [matejka-2017-datasaurus.md](studies/matejka-2017-datasaurus.md) | `primary-read` | **A construction, not an experiment.** Cite as illustration only. |
| [bateman-2010-useful-junk.md](studies/bateman-2010-useful-junk.md) | `primary-read` | Embellishment did not hurt accuracy. The long-term recall result does not replicate cleanly. |
| [gillan-richman-1994-data-ink.md](studies/gillan-richman-1994-data-ink.md) | `secondary-only` | Aggregate direction supports Tufte; element-level decomposition does not. |
| [skau-2015-embellished-bars.md](studies/skau-2015-embellished-bars.md) | `primary-read` | Deforming the bar raises error. Compatible with Bateman, not opposed to it. |
| [cleveland-mcgill-1984.md](studies/cleveland-mcgill-1984.md) | `primary-read` | The channel ranking. **It has ties, and length/direction/angle share rank 3.** |
| [heer-bostock-2010.md](studies/heer-bostock-2010.md) | `primary-read` | The replication. Square rectangles are the worst case for area. Length-beats-angle did not reproduce. |
| [skau-kosara-2016.md](studies/skau-kosara-2016.md) | `primary-read` | Pies are not read by angle. Donuts are as accurate as pies. |
| [ghoniem-2004.md](studies/ghoniem-2004.md) | `primary-read` | Matrices beat node-link above ~20 nodes, at densities 0.2-0.6, static. |
| [okoe-2018.md](studies/okoe-2018.md) | `primary-read` | The interactive real-network replication that comes out the other way. |
| [krzywinski-2012-hive-plots.md](studies/krzywinski-2012-hive-plots.md) | `primary-read` | Hive plots. Rules are structural, so no node metadata is needed. **No user study.** |
| [nollenburg-2023-computing-hive-plots.md](studies/nollenburg-2023-computing-hive-plots.md) | `primary-read` | Hive plot construction is three known-hard problems. Also no user study. |

## Concepts

- [floor-and-ceiling.md](concepts/floor-and-ceiling.md): why a figure quality bar has to scope itself by the figure's job, and what breaks when it doesn't.
- [evidence-class.md](concepts/evidence-class.md): labeling a rule evidence-backed versus authority-asserted, and why conflating them is the characteristic failure of viz advice.
- [channels.md](concepts/channels.md): the perceptual channels, the accuracy ordering over them, and the argument that this is the only level at which the literature actually says anything.

## Chart types

One page per chart type in [chart-types/](chart-types/README.md), stored **flat**, grouped by **index pages** rather than by directory. A data relationship is a view of a chart, not a property of it: a stacked bar is part-to-whole and magnitude and change-over-time, and a directory tree would have to pick one and demote the rest.

**No controlled study has ever tested a chart type. They test channels.** Every claim about a type is a two-step inference whose first step (this chart puts the reader on that channel) is conjecture in the source literature. Type pages inherit evidence from [channels.md](concepts/channels.md) rather than restating it.

| | |
|---|---|
| Indexes written (12) | All nine FT relationships: [part-to-whole](chart-types/part-to-whole.md), [magnitude](chart-types/magnitude.md), [distribution](chart-types/distribution.md), [correlation](chart-types/correlation.md), [change-over-time](chart-types/change-over-time.md), [deviation](chart-types/deviation.md), [ranking](chart-types/ranking.md), [spatial](chart-types/spatial.md) and [flow](chart-types/flow.md). Plus three of ours: [network-topology](chart-types/network-topology.md), [tables](chart-types/tables.md) and [qualitative](chart-types/qualitative.md) |
| Type pages written | 40 |
| Name resolution | [aliases.md](chart-types/aliases.md), which resolves 103 chart names to the page that covers them, or says plainly that nothing here does. Every mapping is marked as source-recorded, page-stipulated, or in circulation only |
| Indexing nothing yet | [tables](chart-types/tables.md) and [qualitative](chart-types/qualitative.md). Both come from Schwabish's catalog, which has a chapter where the FT has no slot, and [sources/schwabish.md](sources/schwabish.md) argues they are real holes. Both are `secondary-only` on the book's prose |

## Checks

- [matplotlib.md](checks/matplotlib.md): reference implementation. Every snippet executed against a real figure.

**The rules are ecosystem-neutral; the checks are not.** matplotlib is where this was built and tested, so it is the reference implementation rather than the intended scope. Equivalents in ggplot2, Vega-Lite, plotly and D3 are wanted and absent. If you write one, the schema is: the rule, the literal check, what it costs to run, and any trap you hit implementing it.

## Coverage and gaps

Stated plainly, because a wiki that hides its holes is worse than a short one.

**The six `secondary-only` pages** are Munzner, Cairo, Tufte (the source page), Gillan & Richman, Menge, and the Edward Tufte person page, which is `status_partial` because the sparklines chapter of *Beautiful Evidence* is read at primary from an excerpt on his own site while the four books are not. Anything resting on them is weaker than it looks. Cairo's *How Charts Lie* was never reached and would sharpen the truncation, inverted-axis and map-projection topics.

**Tufte is the structural gap**, and it is worse than a thin page. He has no row in the roll-call and appears nowhere in the inventory except by quotation through Wilke. The roll-call's guarantee is that an omission shows up as an unmapped chapter, and that guarantee **cannot cover a source nobody enumerated**. The canon's most-cited author on this subject entered 92 topics secondhand.

**Two inventory topics are missing**, found only because Few's primary turned out readable. His *Completeness* is about comparison context, not legends and notes, and nothing covers it. His *Truthfulness* includes **validity**, which has no topic at all.

**Accessibility should be imported, not derived.** The four accessibility topics here map onto eight of Chartability's fifty heuristics, one of them only partially; the mapping is in [sources/chartability.md](sources/chartability.md). Its page carries the license analysis and a six-step adoption plan.

**Chart-type coverage is broad and thin, which is the correct shape.** Forty type pages and twelve indexes exist, and every FT relationship now has an index. **31 of the 40 state that no study in this corpus tests the form**. Named types still without a page include the horizon graph, arc diagram, flow map, Gantt, cycle plot, stem-and-leaf, candlestick, ECDF, Venn and Euler diagrams, and the isotype and pictogram, which [chart-types/waffle-chart.md](chart-types/waffle-chart.md) deliberately treats as neighbors rather than as the same form.

**Chart names are not stable, and the tier cannot yet resolve them.** Several wave-three pages had to record that the name they are filed under is unvouched by any source in this corpus, and three genuine collisions are flagged and unresolved: "mosaic plot" (a business chart and a contingency-table display), "heat map" (a categorical grid, a geographic density surface, and loosely a choropleth), and "range plot" (two measurements, or an interval around an estimate). A name-resolution index is the next piece of work.

**The chart-type tier is mostly `authority-asserted` by necessity.** The graphical-perception literature tests proportional judgment almost exclusively, so groups whose job is something else inherit very little. Only [pie-and-donut.md](chart-types/pie-and-donut.md) rests on a study that decomposed the type itself. Deviation, ranking, spatial and flow have no experiment behind any of their forms at all, and their pages say so rather than filling the gap.

**Everything is matplotlib-tested.** No claim is made about how the checks translate.
