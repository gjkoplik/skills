# The agent-viz wiki

One page per thing. A source gets a page, a study gets a page, a person gets a page, an idea that took work to arrive at gets a page. Pages link to each other rather than repeating each other, so a reader can pick up any single thread without rerunning the research and can see what each source is good for rather than a flat citation list.

Pages carry their facts in frontmatter and their argument in the body. The schema, the status labels and the page templates live in the repo's `agent-viz-wiki` skill, and `validate.py` enforces them.

**Status is not decoration.** `primary-read` means someone opened the source and the quotes come from a local extraction. `secondary-only` means abstracts or summaries, and its quotes are unvouched. `not-reached` means the page says where it looked. `status_partial` means the page covers several artifacts and did not reach them all equally, with `status` recording the principal subject. Several claims here changed when someone opened the primary, so a `secondary-only` page has not earned the trust of a `primary-read` one.

**Current state: 54 `primary-read`, 6 `secondary-only`, 0 `not-reached`, of which 25 are `status_partial`.** Parsed from frontmatter across `sources/`, `studies/` and `people/` by `validate.py`, which fails if this line drifts. `concepts/` and `chart-types/` are synthesis and structure, and are not counted. This is the only count in the wiki, because it is the only one a machine enforces.

## Start here

- [inventory.md](inventory.md): the topics a general figure bar owes, derived blind from the canon, each with a mechanizable-or-judgment verdict and its evidence class. The spine everything else hangs off.
- [refutations.md](refutations.md): widely repeated rules that changed or died when someone read the source.
- [roll-call.md](roll-call.md): the audit trail. Every chapter of every source mapped to an inventory topic or a stated exclusion.

## Chart types

One page per chart type in [chart-types/](chart-types/README.md), stored flat and grouped by index pages rather than by directory, because a data relationship is a view of a chart rather than a property of it: a stacked bar is part-to-whole and magnitude and change-over-time, and a directory tree would have to pick one.

Every FT relationship has an index: [part-to-whole](chart-types/part-to-whole.md), [magnitude](chart-types/magnitude.md), [distribution](chart-types/distribution.md), [correlation](chart-types/correlation.md), [change-over-time](chart-types/change-over-time.md), [deviation](chart-types/deviation.md), [ranking](chart-types/ranking.md), [spatial](chart-types/spatial.md) and [flow](chart-types/flow.md). Four more are this wiki's own: [uncertainty](chart-types/uncertainty.md), for an estimate and its interval, which the FT has no family for; [network-topology](chart-types/network-topology.md); [tables](chart-types/tables.md); and [qualitative](chart-types/qualitative.md). [choose.md](chart-types/choose.md) is the whole chooser on one page: the shape of the data, the reader's question, the forms within each group with their evidence state, and the defense. [aliases.md](chart-types/aliases.md) maps a chart name to the page covering it, or says that nothing here does.

No controlled study has tested a chart type; they test channels. Every claim about a type is a two-step inference whose first step (this chart puts the reader on that channel) is conjecture in the source literature, so type pages inherit evidence from [channels.md](concepts/channels.md) rather than restating it, and most say that no study in the corpus tests the form. Only [pie-and-donut.md](chart-types/pie-and-donut.md) rests on a study that decomposed the type itself.

## Sources

| Page | Status | Good for |
|---|---|---|
| [wilke-fundamentals.md](sources/wilke-fundamentals.md) | `primary-read` | The broadest single reference. Free online, 30 chapters, covers most of the inventory. |
| [munzner-vad.md](sources/munzner-vad.md) | `secondary-only` | Task and data abstraction, marks and channels, the nine rules of thumb. |
| [knaflic-swd.md](sources/knaflic-swd.md) | `primary-read` | Narrative, attention, decluttering. Chapter 1 in full; later chapters via the book's own index. |
| [cairo-truthful-art.md](sources/cairo-truthful-art.md) | `secondary-only` | The five qualities framing. Structure read; the argument was not. |
| [few-effectiveness-profile.md](sources/few-effectiveness-profile.md) | `primary-read` | Effectiveness criteria split into informative and emotive. |
| [tufte.md](sources/tufte.md) | `secondary-only` | Data-ink, chartjunk. Thin, and its page explains why that matters. |
| [matplotlib.md](sources/matplotlib.md) | `primary-read` | Colormap classes, perceptual uniformity, colorbars, style sheets. |
| [seaborn.md](sources/seaborn.md) | `primary-read` | Palettes, and the best short treatment of what an error bar means. |
| [vega-lite.md](sources/vega-lite.md) | `primary-read` | Opinions shipped as defaults, notably `zero: true`. |
| [observable-plot.md](sources/observable-plot.md) | `primary-read` | The turbo default, and a by-mark reading of proportional ink. |
| [bbc-cookbook.md](sources/bbc-cookbook.md) | `primary-read` | A newsroom house style shipped as a package. |
| [urban-institute.md](sources/urban-institute.md) | `primary-read` | The most rule-shaped style guide, plus a real accessibility section. |
| [datawrapper-academy.md](sources/datawrapper-academy.md) | `primary-read` | Color, accessibility, number formats, responsive sizing. |
| [ft-visual-vocabulary.md](sources/ft-visual-vocabulary.md) | `primary-read` | Chart-type selection by data relationship. The spine for the chart-type tier. |
| [schwabish.md](sources/schwabish.md) | `secondary-only` | A chart catalog with chapters the FT has no slot for. Memberships verified from the contents pages; prose unread. |
| [w3c-wai-complex-images.md](sources/w3c-wai-complex-images.md) | `primary-read` | The two-part alt text pattern, as a standard rather than an opinion. |
| [chartability.md](sources/chartability.md) | `primary-read` | 50 accessibility heuristics, CC BY-SA, with a 14-test shortlist. Import this rather than re-deriving it. |

## Studies

| Page | Status | The finding |
|---|---|---|
| [pandey-2015-deceptive-visualizations.md](studies/pandey-2015-deceptive-visualizations.md) | `primary-read` | Distortion measurably works. The paper's Discussion contradicts its own table. |
| [correll-2020-truncating-the-y-axis.md](studies/correll-2020-truncating-the-y-axis.md) | `primary-read` | Truncation's exaggeration persists, and break glyphs did not measurably fix it. |
| [talbot-2012-slope-ratio.md](studies/talbot-2012-slope-ratio.md) | `primary-read` | Bank-to-45 is scope-limited, not general. |
| [isenberg-2011-dual-scale-charts.md](studies/isenberg-2011-dual-scale-charts.md) | `primary-read` | The paper cited for a dual-axis ban studied something else. |
| [menge-2018-log-scales.md](studies/menge-2018-log-scales.md) | `secondary-only` | Domain experts misread log-log badly. 56% against 93%. |
| [romano-2020-log-scales-covid.md](studies/romano-2020-log-scales-covid.md) | `primary-read` | Log scales changed comprehension, prediction and policy preference. |
| [ware-2023-rainbow-colormaps.md](studies/ware-2023-rainbow-colormaps.md) | `primary-read` | Not a study. A Viewpoints essay. Its page says so and names the real sources. |
| [cumming-2007-error-bars.md](studies/cumming-2007-error-bars.md) | `primary-read` | Numbered rules for error bars, including state what they are and state n. |
| [belia-2005-ci-misconceptions.md](studies/belia-2005-ci-misconceptions.md) | `primary-read` | 473 published authors, severe misconceptions about CIs and SE bars. |
| [correll-gleicher-2014-error-bars-harmful.md](studies/correll-gleicher-2014-error-bars-harmful.md) | `primary-read` | The error encoding changes the decision. Gradient and violin beat bar-and-whisker for inference. |
| [weissgerber-2015-beyond-bar-line.md](studies/weissgerber-2015-beyond-bar-line.md) | `primary-read` | 703-article review. At small n, plot the points. |
| [song-szafir-2019-missing-data.md](studies/song-szafir-2019-missing-data.md) | `primary-read` | Highlighting missing values raises perceived quality; breaking continuity biases interpretation. |
| [matejka-2017-datasaurus.md](studies/matejka-2017-datasaurus.md) | `primary-read` | A construction, not an experiment. Cite as illustration only. |
| [bateman-2010-useful-junk.md](studies/bateman-2010-useful-junk.md) | `primary-read` | Embellishment did not hurt accuracy. The long-term recall result does not replicate cleanly. |
| [gillan-richman-1994-data-ink.md](studies/gillan-richman-1994-data-ink.md) | `secondary-only` | Aggregate direction supports Tufte; element-level decomposition does not. |
| [skau-2015-embellished-bars.md](studies/skau-2015-embellished-bars.md) | `primary-read` | Deforming the bar raises error. Compatible with Bateman, not opposed to it. |
| [cleveland-mcgill-1984.md](studies/cleveland-mcgill-1984.md) | `primary-read` | The channel ranking. It has ties, and length, direction and angle share rank 3. |
| [heer-bostock-2010.md](studies/heer-bostock-2010.md) | `primary-read` | The replication. Square rectangles are the worst case for area. Length-beats-angle did not reproduce. |
| [heer-2009-horizon-graphs.md](studies/heer-2009-horizon-graphs.md) | `primary-read` | Mirroring negatives is free on value comparison. Bands cost time and error, and pay in accuracy only below 24 pixels. |
| [skau-kosara-2016.md](studies/skau-kosara-2016.md) | `primary-read` | Pies are not read by angle. Donuts are as accurate as pies. |
| [ghoniem-2004.md](studies/ghoniem-2004.md) | `primary-read` | Matrices beat node-link above ~20 nodes, at densities 0.2 to 0.6, static. |
| [okoe-2018.md](studies/okoe-2018.md) | `primary-read` | The interactive real-network replication that comes out the other way. |
| [krzywinski-2012-hive-plots.md](studies/krzywinski-2012-hive-plots.md) | `primary-read` | Hive plots. Rules are structural, so no node metadata is needed. No user study. |
| [nollenburg-2023-computing-hive-plots.md](studies/nollenburg-2023-computing-hive-plots.md) | `primary-read` | Hive plot construction is three known-hard problems. Also no user study. |
| [gutwin-2023-chord-vs-sankey.md](studies/gutwin-2023-chord-vs-sankey.md) | `primary-read` | Sankey beat chord on time, errors, effort and preference. The performance effects are tiny and mostly gone by the fourth look. |
| [siqueira-rodrigues-2026-vr-graphical-perception.md](studies/siqueira-rodrigues-2026-vr-graphical-perception.md) | `primary-read` | Position beats length beats area, replicated in a headset. The horizontal-bar penalty is large at oblique angles and absent face-on. |

## People

One page per author in [people/](people/), covering the person across their work: what they are known for, what coming to them buys you, and where their authority stops. `sources/` covers one work; `people/` covers the person. A prolific author has both.

## Concepts

- [floor-and-ceiling.md](concepts/floor-and-ceiling.md): why a figure quality bar has to scope itself by the figure's job.
- [evidence-class.md](concepts/evidence-class.md): labeling a rule evidence-backed versus authority-asserted, and why conflating them is the characteristic failure of viz advice.
- [channels.md](concepts/channels.md): the perceptual channels, the accuracy ordering over them, and why this is the only level at which the literature says anything.

## Checks

[checks/matplotlib.md](checks/matplotlib.md) is the reference implementation of the mechanizable rules, every snippet executed against a real figure. The rules are ecosystem-neutral; the checks are not. Equivalents in ggplot2, Vega-Lite, plotly and D3 are wanted and absent. The schema for one is: the rule, the literal check, what it costs to run, and any trap hit implementing it.

## Coverage and gaps

**The `secondary-only` pages** are Munzner, Cairo, Tufte, Schwabish, Gillan & Richman, and Menge. Anything resting on them is weaker than it looks. Cairo's *How Charts Lie* was never reached and would sharpen the truncation, inverted-axis and map-projection topics.

**Tufte is the structural gap.** He has no row in the roll-call and appears in the inventory only by quotation through Wilke. The roll-call's guarantee is that an omission shows up as an unmapped chapter, and that guarantee cannot cover a source nobody enumerated.

**Two inventory topics are missing**, found when Few's primary turned out readable. His *Completeness* is about comparison context, not legends and notes, and nothing covers it. His *Truthfulness* includes validity, which has no topic.

**Accessibility should be imported, not derived.** The four accessibility topics here map onto eight of Chartability's fifty heuristics; the mapping, the license analysis and an adoption plan are on [sources/chartability.md](sources/chartability.md).

**Chart-type coverage is broad and thin.** Most type pages record that no study in this corpus tests the form; the per-page position is in the coverage table at [chart-types/README.md](chart-types/README.md). Deviation, ranking and spatial have no experiment behind any of their forms. Named types without a page include the arc diagram, Gantt, cycle plot, stem-and-leaf, candlestick, Venn and Euler diagrams, and the isotype and pictogram, which [waffle-chart.md](chart-types/waffle-chart.md) treats as neighbors rather than the same form. Three name collisions are flagged and unresolved on [aliases.md](chart-types/aliases.md): "mosaic plot", "heat map" and "range plot".

**Everything is matplotlib-tested.** No claim is made about how the checks translate.
