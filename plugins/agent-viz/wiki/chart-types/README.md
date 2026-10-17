# Chart types

One page per chart type, stored flat, with index pages that group them by data relationship. The evidence lives one tier up in [../concepts/channels.md](../concepts/channels.md), and these pages inherit it.

A reader with data and a question starts at [choose.md](choose.md), the whole chooser on one page: what shape the data is, what the reader needs to answer, the forms within each group with their evidence state, and the defense. A reader with a group in doubt opens its index. A reader with a chart name starts at its page or at [aliases.md](aliases.md). The answer depends on the reader's question, not only the data's shape, so the pages narrow the candidates, name what each costs, and record which justifications hold up.

## Taxonomy is an index, not a home

A data relationship is a view of a chart, not a property of it. A stacked bar is part-to-whole and magnitude, and change over time once it becomes an area chart. A dot plot is ranking and distribution. A directory tree would force one home and demote the other readings to cross-links. Flat storage lets a type sit in three indexes.

Each page declares its membership in its `relationships:` frontmatter, so an index can be checked against the pages. [roll-call.md](../roll-call.md) audits [inventory.md](../inventory.md) the same way, with the claim written in two places that must agree.

## Inheritance

A type page may inherit an accuracy claim from [../concepts/channels.md](../concepts/channels.md) with a link, but does not restate it as a finding about the form. The step from mark to channel is conjecture in the source literature. A study that decomposed a specific form is a type-level finding, as on [pie-and-donut.md](pie-and-donut.md). Channel evidence is densest for part-to-whole, so that group has the most to inherit.

## The indexes

Each index carries the argument common to its group. Nine follow the FT relationships: part-to-whole, magnitude, distribution, correlation, change over time, deviation, ranking, spatial and flow. Three sit alongside them: network-topology, tables and qualitative, the last two from Schwabish chapters the FT has no slot for ([../sources/schwabish.md](../sources/schwabish.md)).

The FT credits its nine to the Graphic Continuum by Jon Schwabish and Severino Ribecca (2014), so the overlap with Schwabish's *Better Data Visualizations* is descent, not convergence. The FT material is all rights reserved and can be cited but not copied ([../sources/ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). The taxonomy is `authority-asserted`: no experiment shows these are the right nine, exhaustive, or mutually exclusive. It is used here for retrieval, not as a claim.

Other axes fit the same flat store. An index by channel would fall out of each page's decomposition. [aliases.md](aliases.md) indexes names, marking each mapping as recorded in a source read here, stipulated by a page, or in circulation. It carries no `relationships:` field.

## Where the evidence runs out

The graphical-perception literature concentrates almost entirely on proportional judgment: read a value off a mark, report it as a number. Groups with another job inherit little from it. Pie, donut, treemap and bar are well studied. Most other forms, including slope charts, connected scatterplots, bump charts, the flow family and every map, have no study; the violin is measured only for inference about a mean and its error. A page with nothing to inherit says so and stops. [hive-plot.md](hive-plot.md) has two descriptive papers and no user study, so it separates what follows from the construction from what would need an experiment.

## Coverage

**None** marks a type page that says no study in this corpus tests the form. Several more inherit everything from a channel result. That is a fact about the literature, not the pages. The [../README.md](../README.md) schema section explains why coverage is stated in words.

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
| [density-plot.md](density-plot.md) | Distribution | **None**; the bandwidth caution is Wilke's |
| [diverging-bar-chart.md](diverging-bar-chart.md) | Deviation | **None**; inherits the floating-segment result from stacked bar |
| [dot-density-map.md](dot-density-map.md) | Spatial | **None** |
| [dot-strip-plot.md](dot-strip-plot.md) | Ranking, Distribution | **None** |
| [dumbbell-plot.md](dumbbell-plot.md) | Ranking, Change over time | **None** |
| [ecdf-plot.md](ecdf-plot.md) | Distribution | **None** on the form. Two primary sources agree it has no free parameter and that shape is harder to see on it, neither tested a reader |
| [flow-map.md](flow-map.md) | Spatial, Flow | **None**, and the one flow study does not reach it |
| [gauge-and-bullet.md](gauge-and-bullet.md) | Magnitude | **None.** Few's design spec reports no test |
| [gradient-plot.md](gradient-plot.md) | Uncertainty | Measured against bar-plus-error-bar and the violin; unranked against the violin |
| [heatmap.md](heatmap.md) | Magnitude, Correlation | **None** on value extraction from a colored cell |
| [histogram.md](histogram.md) | Distribution | **None**, and the bin width is a free parameter |
| [hive-plot.md](hive-plot.md) | Network and topology | Two `primary-read` sources, **neither containing a user study** |
| [horizon-graph.md](horizon-graph.md) | Change over time | One study read at primary, recorded on a person page; no study page yet |
| [interval-plot.md](interval-plot.md) | Uncertainty | The best-measured group: expert misreading, the bar's containment bias |
| [line-chart.md](line-chart.md) | Change over time | None against an alternative; the manipulations are measured |
| [lollipop-chart.md](lollipop-chart.md) | Magnitude, Ranking | **None** |
| [marimekko-chart.md](marimekko-chart.md) | Part-to-whole, Magnitude | **None**; inherits rectangular area |
| [node-link.md](node-link.md) | Network and topology | Two studies that disagree |
| [parallel-coordinates.md](parallel-coordinates.md) | Correlation | **None** |
| [pie-and-donut.md](pie-and-donut.md) | Part-to-whole | Two studies, one a direct channel decomposition |
| [radar-chart.md](radar-chart.md) | Magnitude | **None** |
| [ridgeline-plot.md](ridgeline-plot.md) | Distribution, Change over time | **None** |
| [sankey-diagram.md](sankey-diagram.md) | Flow, Network and topology | One study, against a chord diagram; the large effect is preference |
| [scatterplot.md](scatterplot.md) | Correlation | Position is measured; trend and cluster reading is not |
| [slope-chart.md](slope-chart.md) | Change over time, Ranking | **None** |
| [small-multiples.md](small-multiples.md) | Change over time, Part-to-whole, Distribution | **None** on the device |
| [sparkline.md](sparkline.md) | Change over time | **None** on the form; Gillan & Richman on axis removal is the nearest |
| [spine-chart.md](spine-chart.md) | Deviation | **None**, and the name itself is unvouched by any source here |
| [stacked-area-chart.md](stacked-area-chart.md) | Change over time, Part-to-whole | **None** |
| [stacked-bar.md](stacked-bar.md) | Part-to-whole, Change over time, Magnitude | Directly tested; it was the 1984 stimulus |
| [streamgraph.md](streamgraph.md) | Change over time | **None**, and the name is unvouched by any source here |
| [sunburst-chart.md](sunburst-chart.md) | Part-to-whole | **None** |
| [treemap.md](treemap.md) | Part-to-whole, Magnitude | One study, incl. the aspect-ratio result |
| [violin-plot.md](violin-plot.md) | Distribution, Uncertainty | Measured for inference about a mean and its error |
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
| [uncertainty.md](uncertainty.md) | Ours. The FT has no uncertainty family, and half the evidence in the corpus is about estimates and their intervals |

`tables.md` and `qualitative.md` index nothing. [tables.md](tables.md) argues that is right, since every form it names leaves the chart tier, and it gives [../inventory.md](../inventory.md) topic 4, "should this be a chart at all", a place to land.

## See also

- [../concepts/channels.md](../concepts/channels.md): the evidence tier these pages inherit from
- [../concepts/evidence-class.md](../concepts/evidence-class.md): the labeling discipline, and the definitional exemption
- [../inventory.md](../inventory.md): topic 5 is the chart-type-selection rule these pages serve
