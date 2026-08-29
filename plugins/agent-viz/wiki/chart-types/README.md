# Chart types

One page per chart type, stored flat, with separate **index pages** that group them by data relationship. Deliberately the *shallow* tier of a two-tier structure: the evidence lives one level up in [../concepts/channels.md](../concepts/channels.md), and these pages inherit it.

**What it is good for.** Choosing a form for a specific dataset and question, and being able to defend the choice afterward. Two entry points: arrive with a question ("this is composition") and get pointed at the candidates, or arrive with a named chart and go straight to its page.

**What it does not settle.** It does not hand over an answer from a lookup table, because the answer depends on the reader's question rather than on the shape of the data. What it does is narrow the candidates, name what each one costs, and record which justifications hold up. Where the evidence is silent it says so rather than inventing a tiebreaker.

---

## Taxonomy is an index, not a home

Every type page lives directly in this directory. Grouping happens in index pages that point at them.

**A data relationship is a view of a chart, not a property of it.** A stacked bar is part-to-whole; it is also magnitude, and it is change-over-time once it becomes an area chart. A dot plot is ranking and distribution. A directory tree forces each type into exactly one home and demotes its other readings to cross-links, which encodes a claim about the type that is not true. Flat storage lets a type appear in three indexes with no duplication.

Membership is declared on the page, in the `relationships:` frontmatter field, so an index can be checked against the pages rather than maintained by hand. That is the trick [roll-call.md](../roll-call.md) plays against [inventory.md](../inventory.md): the audit is possible because the claim is written down in two places that must agree.

## The indexes

The indexes are more than pointer lists: each carries the argument that is common to its group, which is the part that would otherwise be repeated on every member page.

**All nine FT relationships now have one**: part-to-whole, magnitude, distribution, correlation, change over time, deviation, ranking, spatial and flow. Three more are ours, sitting alongside the FT nine rather than inside them: **network-topology**, **tables** and **qualitative**. The last two come from Schwabish, whose scheme has chapters the FT has no slot for, and the argument for adding them rather than amending the nine is in [../sources/schwabish.md](../sources/schwabish.md).

**Provenance.** The Visual Vocabulary is not the origin of these nine: it credits the Graphic Continuum by Jon Schwabish and Severino Ribecca (2014). Crediting only the FT credits the derivative, and it explains the heavy overlap with Schwabish's *Better Data Visualizations*, which is descent rather than convergence. The full source page is [../sources/ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md), which also carries the copyright note: the FT material is all rights reserved and can be cited but not copied.

**Evidence class of the taxonomy itself: `authority-asserted`.** No experiment establishes that these are the right nine, that they are exhaustive, or that they are mutually exclusive. It is a well-designed practitioner scheme that works for retrieval. Used here as an index, not as a claim.

Other index axes are possible on the same flat store: an index **by channel** (every type that puts the reader on area) would fall straight out of the decomposition already on each page. [aliases.md](aliases.md) is the first index of this kind built, and it indexes names.

## Where the evidence runs out

Stated up front, because it determines how thin most of this tier has to be:

- The graphical-perception literature concentrates almost entirely on **proportional judgment**: read a value off a mark, report it as a number. Groups whose job is something else inherit very little from it.
- Most individual chart types have **no study at all**. Pie, donut, treemap and bar are unusually well studied. Violin plots, slope charts, connected scatterplots, bump charts, the whole flow family and every map are not.
- A page with nothing to inherit says so and stops. Padding it with plausible practitioner advice dressed as findings is the specific failure this structure exists to avoid. [hive-plot.md](hive-plot.md) is one case: two papers describe the form in detail and neither ran a user study, so the page separates what follows from the construction (secure, and stated flatly) from what would need an experiment (absent, and stated as absent).

## Coverage

**Most type pages say plainly that no study in this corpus tests the form**, marked **None** in the Evidence column
below, and several more inherit everything they have from a channel result rather than from a measurement of the
chart. That is a fact about the literature, not about the pages. The [../README.md](../README.md) schema section
covers why coverage here is stated in words rather than as a number derived by reading prose.

**Type pages**

| Page | Relationships | Evidence |
|---|---|---|
| [adjacency-matrix.md](adjacency-matrix.md) | Network and topology | Two studies that disagree |
| [area-chart.md](area-chart.md) | Change over time | None on the form; inherits truncation and aspect-ratio results |
| [bar-chart.md](bar-chart.md) | Magnitude | The best-measured form in the corpus |
| [beeswarm-plot.md](beeswarm-plot.md) | Distribution | **None.** Weissgerber argues for plotting points, not for this layout |
| [boxplot.md](boxplot.md) | Distribution | Two results, the only ones bearing on summary-versus-sample |
| [bubble-chart.md](bubble-chart.md) | Correlation | Area is measured; the bubble form is not |
| [bump-chart.md](bump-chart.md) | Ranking, Change over time | **None** |
| [cartogram.md](cartogram.md) | Spatial, Magnitude | **None.** Heer & Bostock on rectangular area is adjacent, not transferable |
| [chord-diagram.md](chord-diagram.md) | Flow, Network and topology | One study, against a Sankey; small effects, mostly first-exposure |
| [choropleth-map.md](choropleth-map.md) | Spatial | **None** |
| [connected-scatterplot.md](connected-scatterplot.md) | Correlation, Change over time | **None** |
| [correlation-matrix.md](correlation-matrix.md) | Correlation | **None**; the Datasaurus bears on what the coefficient hides |
| [diverging-bar-chart.md](diverging-bar-chart.md) | Deviation | **None**; inherits the floating-segment result from stacked bar |
| [dot-density-map.md](dot-density-map.md) | Spatial | **None** |
| [dot-strip-plot.md](dot-strip-plot.md) | Ranking, Distribution | **None** |
| [flow-map.md](flow-map.md) | Spatial, Flow | **None**, and the one flow study does not reach it |
| [dumbbell-plot.md](dumbbell-plot.md) | Ranking, Change over time | **None** |
| [gauge-and-bullet.md](gauge-and-bullet.md) | Magnitude | **None.** Few's design spec reports no test |
| [heatmap.md](heatmap.md) | Magnitude, Correlation | **None** on value extraction from a colored cell |
| [histogram.md](histogram.md) | Distribution | **None**, and the bin width is a free parameter |
| [hive-plot.md](hive-plot.md) | Network and topology | Two `primary-read` sources, **neither containing a user study** |
| [line-chart.md](line-chart.md) | Change over time | None against an alternative; the manipulations are measured |
| [lollipop-chart.md](lollipop-chart.md) | Magnitude, Ranking | **None** |
| [marimekko-chart.md](marimekko-chart.md) | Part-to-whole, Magnitude | **None**; inherits rectangular area |
| [node-link.md](node-link.md) | Network and topology | Two studies that disagree |
| [pie-and-donut.md](pie-and-donut.md) | Part-to-whole | Two studies, one a direct channel decomposition |
| [radar-chart.md](radar-chart.md) | Magnitude | **None** |
| [ridgeline-plot.md](ridgeline-plot.md) | Distribution, Change over time | **None**, and the name is unvouched by any source here |
| [sankey-diagram.md](sankey-diagram.md) | Flow, Network and topology | One study, against a chord diagram; the large effect is preference |
| [scatterplot.md](scatterplot.md) | Correlation | Position is measured; trend and cluster reading is not |
| [slope-chart.md](slope-chart.md) | Change over time, Ranking | **None** |
| [sparkline.md](sparkline.md) | Change over time | **None** on the form; Gillan & Richman on axis removal is the nearest |
| [spine-chart.md](spine-chart.md) | Deviation | **None**, and the name itself is unvouched by any source here |
| [stacked-area-chart.md](stacked-area-chart.md) | Change over time, Part-to-whole | **None** |
| [stacked-bar.md](stacked-bar.md) | Part-to-whole, Change over time, Magnitude | Directly tested; it was the 1984 stimulus |
| [streamgraph.md](streamgraph.md) | Change over time | **None**, and the name is unvouched by any source here |
| [sunburst-chart.md](sunburst-chart.md) | Part-to-whole | **None** |
| [treemap.md](treemap.md) | Part-to-whole, Magnitude | One study, incl. the aspect-ratio result |
| [violin-plot.md](violin-plot.md) | Distribution | Measured for inference about a mean and its error |
| [waffle-chart.md](waffle-chart.md) | Part-to-whole, Magnitude | **None** |
| [waterfall-chart.md](waterfall-chart.md) | Flow | **None** |

**Indexes**

| Index | Whose scheme |
|---|---|
| [part-to-whole.md](part-to-whole.md) | FT |
| [magnitude.md](magnitude.md) | FT |
| [distribution.md](distribution.md) | FT |
| [correlation.md](correlation.md) | FT |
| [change-over-time.md](change-over-time.md) | FT |
| [deviation.md](deviation.md) | FT |
| [ranking.md](ranking.md) | FT |
| [spatial.md](spatial.md) | FT |
| [flow.md](flow.md) | FT |
| [network-topology.md](network-topology.md) | Ours |
| [tables.md](tables.md) | Ours, after Schwabish |
| [qualitative.md](qualitative.md) | Ours, after Schwabish |

**Plus [aliases.md](aliases.md), which indexes names rather than a data relationship.** A reader arrives with a chart name, not with a data relationship, and the names are not stable. It resolves chart names and marks each mapping as recorded in a source read here, stipulated by a page, or in circulation with nothing here defining it. It carries no `relationships:` field.

**The last two index nothing, and `tables.md` argues it should stay that way**: every form it names is a way of
leaving the chart tier rather than a chart with a page, and routing the reader out is what the page is for. It still
earns its place by giving [../inventory.md](../inventory.md) topic 4, "should this be a chart at all", somewhere to
land inside the tier.

Part-to-whole is where the channel evidence is densest, so it is the group where the inheritance rule has the most
to work with and the group where getting it wrong would show.

## See also

- [../concepts/channels.md](../concepts/channels.md) — the evidence tier these pages inherit from
- [../concepts/evidence-class.md](../concepts/evidence-class.md) — the labeling discipline, and the definitional exemption
- [../inventory.md](../inventory.md) — topic 5 is the chart-type-selection rule these pages serve
