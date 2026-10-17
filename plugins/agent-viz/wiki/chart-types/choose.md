---
type: index
---

# Choosing a chart

The whole chooser on one page: the shape of the data, the reader's question, the form within the group, and its defense. Each linked index and type page is the depth behind its row. The order of the steps is the order they are decided in, and the shape step comes first because people arrive with a dataframe, not a question, and the shape rules out most groups before the question is asked.

## Step 0: what shape is the data

The vocabulary is Munzner's: an encoding arranges a table, spatial data, or a network or tree, and channel type matches data type ([munzner-vad.md](../sources/munzner-vad.md)). Every shape can also reach [tables](tables.md).

| Data shape | Groups that are possible | Groups that are not |
|---|---|---|
| One categorical, one quantitative, one value per category | Magnitude; ranking; deviation, once a reference is fixed; distribution, treating the values as observations | Part-to-whole, unless the values exhaust a real total; correlation; change over time; flow; network |
| The same, parts summing to a whole | Part-to-whole, when the total is real; magnitude; ranking | Correlation; change over time; flow; network |
| One quantitative variable, many observations | Distribution; magnitude only as a bar of a statistic, which is [magnitude.md](magnitude.md)'s failure mode | Correlation; change over time; part-to-whole; flow; network; spatial |
| Two quantitative variables, one row per thing | Correlation; distribution of either; magnitude or ranking on one column | Part-to-whole; flow; network; change over time, unless one variable is time |
| Many quantitative variables, one row per thing | Correlation ([correlation matrix](correlation-matrix.md), [parallel coordinates](parallel-coordinates.md)); distribution of each; [small multiples](small-multiples.md) of any pair | Part-to-whole; flow; network |
| One quantitative at two points per category | Ranking ([dumbbell](dumbbell-plot.md), [slope chart](slope-chart.md)); change over time, when the points are dates; deviation, when one point is the reference; magnitude as grouped bars | Part-to-whole; flow; network |
| A quantitative series over ordered time | Change over time; deviation against a reference; magnitude as columns over few periods; distribution within each period | Correlation; part-to-whole; flow; network |
| Several series over time | Change over time; part-to-whole, when the series compose a real total; ranking ([bump chart](bump-chart.md)); correlation, as a [connected scatterplot](connected-scatterplot.md) of two series | Correlation for series paired only by date, [correlation.md](correlation.md)'s first test; flow; network |
| An estimate with an interval (a mean with SD, SE or CI) | Uncertainty; distribution, when the sample's shape is the subject; ranking, whose failure mode is an order inside the noise | Magnitude as a bar of the mean; part-to-whole; flow; network |
| A quantity per geographic unit | Spatial, when the pattern would not survive as a list of regions; magnitude, ranking, distribution, deviation and correlation, per [spatial.md](spatial.md)'s routing | Flow, unless something moves between places; network; part-to-whole, unless the units exhaust a real total |
| A weighted graph (nodes and links) | Network and topology; flow, when the weight is a volume moving between states; magnitude or ranking on a per-node column | Correlation; distribution; change over time; part-to-whole; spatial, unless nodes are places |
| Flows between stages | Flow; network and topology (Sankey and chord sit in both); part-to-whole for one stage; magnitude for stage totals | Correlation; distribution |
| A hierarchy with sizes | Part-to-whole ([treemap](treemap.md), [sunburst](sunburst-chart.md)); magnitude (treemap) | Correlation; change over time; flow; distribution. Network and topology indexes no tree layout, though Munzner files both under trees |
| Qualitative text | Qualitative, for word frequency alone; tables, for quotes; magnitude, deviation and change over time once codes are counted | Every quantitative group, until something is counted |

## Step 1: what does the reader need to answer

The common error is the wrong group, not the wrong chart within it. From [SKILL.md](../../SKILL.md):

| What the reader needs to answer | Index |
|---|---|
| How big is this one? | [magnitude](magnitude.md) |
| Which is biggest, in what order? | [ranking](ranking.md) |
| What is it made of, and does it add up? | [part-to-whole](part-to-whole.md) |
| How is it spread? Is there enough data to say? | [distribution](distribution.md) |
| How sure is this estimate? Is the difference real? | [uncertainty](uncertainty.md) |
| Do these two move together? | [correlation](correlation.md) |
| How did it change over time? | [change-over-time](change-over-time.md) |
| How far from a baseline or target? | [deviation](deviation.md) |
| Where is it? | [spatial](spatial.md) |
| How does it move through a system? | [flow](flow.md) |
| Who connects to whom? | [network and topology](network-topology.md) |
| Text, quotes or coded qualitative material | [qualitative](qualitative.md) |

Each index opens with the test that sends a reader elsewhere:

| Group | The question that routes out |
|---|---|
| [Magnitude](magnitude.md) | Is the comparison within one item, or is the order needed rather than the size? |
| [Ranking](ranking.md) | Does the sentence need the value, or is the order too unstable to be the message? |
| [Part-to-whole](part-to-whole.md) | Is the total an artifact of which categories were included, or is "and that is all of it" not part of the claim? |
| [Distribution](distribution.md) | Too little data for a shape, a computed estimate rather than the values, or an n that does not count independent things? |
| [Uncertainty](uncertainty.md) | Is the subject the sample's shape rather than an estimate? Is the interval descriptive (SD, range) or inferential (SE, CI)? |
| [Correlation](correlation.md) | Do the variables share only a time index, is one level the message, or is the question causal? |
| [Change over time](change-over-time.md) | Would the answer survive deleting the middle, is the space between points meaningless, or does the window decide it? |
| [Deviation](deviation.md) | Does the reference need arguing for, does the level matter rather than the difference, or does the sign mean nothing? |
| [Spatial](spatial.md) | Is geography only how values were looked up, or would the pattern survive as a list of regions? |
| [Flow](flow.md) | Is there no volume, no between, or do the endpoints matter more than the movement? |
| [Network and topology](network-topology.md) | Does a per-node column answer it? Then a sorted bar chart does |
| [Qualitative](qualitative.md) | Has anything been counted yet? A count goes to magnitude |
| [Tables](tables.md) | Is the reader seeing a pattern rather than looking up or checking a value? |

## Step 2: pick the form within the group

Groups in routing order, [tables](tables.md) last. Evidence states summarize the [coverage table](README.md#coverage); "measured" means a study in this corpus tested the form or a manipulation of it, "channel-inherited" means only the channel is measured and the form is conjecture, "none" means no study here touches it.

### Magnitude

The value sits on position along a common scale, so the costs are row count fixing the height, a zero baseline under filled marks, and no whole.

| Form | What is drawn | Applies when | Evidence state |
|---|---|---|---|
| [Bar chart](bar-chart.md) | Bar end on a common scale | The default; categories few enough to label | Measured: the best-measured form |
| [Lollipop chart](lollipop-chart.md) | A point at the value, a stem | Many categories, where bars become a block of ink | None |
| [Stacked bar](stacked-bar.md) | Segment length; total as position | The total is the magnitude and its composition matters | Measured: the 1984 stimulus |
| [Treemap](treemap.md) | Rectangular area | Hundreds of items, approximate sizes enough | Measured: one study |
| [Radar chart](radar-chart.md) | Radial distance per axis | Several measures profiling one entity | None on profiling; low or chance precision when drawn to show a correlation |
| [Heatmap](heatmap.md) | Cell color on a two-key grid | One value per key pair, the pattern over any cell | None |
| [Gauge and bullet](gauge-and-bullet.md) | Arc position, or bar length against a marker | One value against a target and context band | None |
| [Waffle](waffle-chart.md) | A count of cells | A small count, tallied | None |
| [Cartogram](cartogram.md) | Area of a distorted region | A total per place, the land-area mismatch the message | None |
| [Marimekko](marimekko-chart.md) | Width times height | Two categorical dimensions, sizes and splits both matter | None; inherits rectangular area |

### Ranking

The accuracy ordering measures value extraction, the task this group excludes, and sort order and item set are free parameters the reader cannot see.

| Form | What is drawn | Applies when | Evidence state |
|---|---|---|---|
| Sorted [bar chart](bar-chart.md) | Arrangement, value on position | The default; few categories, sizes useful too | Measured: value extraction, not order |
| [Lollipop chart](lollipop-chart.md) | Arrangement, value on a dot | Too many categories for bars | None |
| [Dot strip plot](dot-strip-plot.md) | Position on one axis, groups stacked | Many items across several groups at once | None |
| [Dumbbell plot](dumbbell-plot.md) | Two positions per row and the gap | Two values per item, levels and gap both matter | None |
| [Slope chart](slope-chart.md) | Two endpoints; crossings are reorderings | Exactly two periods or conditions | None |
| [Bump chart](bump-chart.md) | Rank on the axis, value discarded | Several periods, who overtook whom | None |

### Part-to-whole

Outside the stacked bar's bottom segment and the marimekko's corner, share sits on arc length, unaligned length, area or a cell count, the price of showing that the parts exhaust the total.

| Form | What is drawn | Applies when | Evidence state |
|---|---|---|---|
| [Pie and donut](pie-and-donut.md) | Arc length and area, not angle | Few parts; "these make a whole" is the point | Measured: channel decomposition |
| [Stacked bar](stacked-bar.md) | Length; bottom segment on position | The total matters, or composition repeats across groups | Measured: the 1984 stimulus |
| [Marimekko](marimekko-chart.md) | Width times height | Two categorical dimensions, sizes and splits both matter | None; inherits rectangular area |
| [Stacked area](stacked-area-chart.md) | Band thickness on a continuous axis | Composition changes continuously, total worth seeing | None |
| [Treemap](treemap.md) | Rectangular area | Many parts, or a hierarchy | Measured: one study |
| [Sunburst](sunburst-chart.md) | Angular extent by ring | A shallow hierarchy, all levels at once | None |
| [Waffle](waffle-chart.md) | A count of cells | A small count, tallied | None |
| [Small multiples](small-multiples.md) of any of these | The same chart per group, shared scales | Composition compared across groups | None |

### Distribution

Every form but the plotted points computes a statistic and hides the computation, and shape judgments fall outside the accuracy ranking.

| Form | What is drawn | Applies when | Evidence state |
|---|---|---|---|
| [Strip plot](dot-strip-plot.md) | Every observation | n is small | Recommended from measured sample sizes; no reader test |
| [Beeswarm](beeswarm-plot.md) | Every observation, displaced sideways | As the strip plot, with collisions resolved | None |
| [Histogram](histogram.md) | Counts per bin | Enough data; modality or gaps matter | None |
| [Density plot](density-plot.md) | A smoothed density | As the histogram, where a curve reads better than bars and the bandwidth is stated | None |
| [ECDF](ecdf-plot.md) | Value against rank, as steps | Fractions below a threshold, or quantiles | None |
| [Box plot](boxplot.md) | Five numbers per group | Many groups, within-group shape not asked | Measured: summary versus sample |
| [Violin plot](violin-plot.md) | Mirrored density | Shape across groups | Measured: inference about a mean |
| [Ridgeline](ridgeline-plot.md) | Overlapping densities, stacked | Many ordered groups, occlusion accepted | None |
| [Small multiples](small-multiples.md) of histograms | One panel per group, shared axes | Many groups where overlap would hide them | None |

### Uncertainty

An interval drawn without its meaning is ambiguous between four things, and expert readers misread even labeled ones.

| Form | What is drawn | Applies when | Evidence state |
|---|---|---|---|
| [Interval plot](interval-plot.md) | A point and a labeled interval per category | The estimate and its uncertainty are the message | Measured: expert misreading, the bar's containment bias |
| [Gradient plot](gradient-plot.md) | Opacity fading with distance from the estimate | An inferential comparison, with no hard edge wanted | Measured: beat bar-plus-error-bar, unranked against the violin |
| [Violin plot](violin-plot.md) | Mirrored density | A mean and its error on a symmetric continuous mark | Measured: beat bar-plus-error-bar for inference |
| [Strip plot](dot-strip-plot.md) | Every observation | n is small enough to show | Recommended from measured sample sizes |
| [Fan chart](fan-chart.md) | Nested probability bands around a projected path | A forecast, where the range at each horizon is the message | None |

### Correlation

One point reads as position. Telling two correlations apart is measured on nine forms and the scatterplot led in both directions; trend, tightness and outliers remain unmeasured, and the aspect ratio decides which slopes show.

| Form | What is drawn | Applies when | Evidence state |
|---|---|---|---|
| [Scatterplot](scatterplot.md) | Two positions | The default; enough paired observations for a shape | Measured: top precision group for telling correlations apart, both directions |
| [Bubble chart](bubble-chart.md) | A third quantity on circle area | The third quantity matters only roughly | Channel-inherited: area, not the form |
| [Connected scatterplot](connected-scatterplot.md) | A path through the plane | Two time series, the joint trajectory the point | Measured: one study. Understood with little explanation, time reversed on 13% of translations, correlational language rare |
| [Correlation matrix](correlation-matrix.md) | Coefficient as cell color | Too many variables for every pair | None |
| [Parallel coordinates](parallel-coordinates.md) | One polyline per row across parallel axes | Many variables, the rows' profiles the point | Measured with two axes: matches the scatterplot on negative correlations, two groups down on positive |
| [Heatmap](heatmap.md) | Cell color on a two-key grid | A value per key pair where the pattern is the point | None |
| [Small multiples](small-multiples.md) of scatterplots | One panel per group, shared axes | The relationship compared across a categorical variable | None |

### Change over time

Slope and shape reading falls outside the accuracy ordering, and aspect ratio and axis range move the apparent trend without moving a number, both measured.

| Form | What is drawn | Applies when | Evidence state |
|---|---|---|---|
| [Line chart](line-chart.md) | Position, read as slope and shape | Many ordered, truly connected points | Measured: the manipulations, not alternatives |
| [Area chart](area-chart.md) | The same, filled | Area under the curve is a real quantity | None; inherits truncation and aspect ratio |
| [Stacked area chart](stacked-area-chart.md) | Band thickness | A few components, total as important | None |
| [Streamgraph](streamgraph.md) | Bands on a computed baseline | Many components, read as a silhouette | None |
| [Slope chart](slope-chart.md) | Two endpoints | Exactly two periods, many categories | None |
| [Dumbbell plot](dumbbell-plot.md) | Two positions per row | Two dates per category, levels and gap both matter | None |
| [Stacked bar](stacked-bar.md) | Segment length | Few discrete periods, composition and total | Measured: the 1984 stimulus |
| [Connected scatterplot](connected-scatterplot.md) | Two-variable plane, time as path | A joint trajectory is the message | Measured: one study, small samples |
| [Bump chart](bump-chart.md) | Rank axis, value discarded | Several periods, few items | None |
| [Sparkline](sparkline.md) | Shape, axes removed | Inside a sentence or table row | None |
| [Fan chart](fan-chart.md) | Nested bands around a projection | A forecast past the last observation | None |
| [Horizon graph](horizon-graph.md) | Mirrored, layered bands | Many series in little vertical space | Measured, recorded on a person page |
| [Ridgeline](ridgeline-plot.md) | Stacked densities | A distribution per period, in order | None |
| [Small multiples](small-multiples.md) of line charts | One panel per series, shared scales | Several series where overlaid lines tangle | None |

### Deviation

The reference is a free parameter invisible on the chart, the difference discards the level, and comparing bars across the line is unmeasured.

| Form | What is drawn | Applies when | Evidence state |
|---|---|---|---|
| [Diverging bar chart](diverging-bar-chart.md) | Length from a reference line, side as sign | One signed number per category | None; inherits floating segments |
| [Spine chart](spine-chart.md) | Two lengths outward from a center | Each row splits one total in two | None |
| Diverging stacked bar, on [diverging-bar-chart.md](diverging-bar-chart.md) | Segments accumulating outward | Ordered responses per row, usually Likert | Channel-inherited: floating segments |
| Surplus or deficit filled line *(no page)* | Area between series and reference | The deviation runs over time | No page |

### Spatial

The map spends the plane on location, leaving the data color, mark area or counted marks, and land area sets each region's share of the page.

| Form | What is drawn | Applies when | Evidence state |
|---|---|---|---|
| [Choropleth](choropleth-map.md) | Fill color of a fixed region | A rate, in boundaries the reader thinks in | None |
| [Cartogram](cartogram.md) | Area of a distorted region | A total, the land-area mismatch the message | None |
| [Dot density](dot-density-map.md) | Dots per unit area | A count, locations known | None |
| Proportional symbol map *(no page)* | Symbol area at a point | A total | No page |
| [Flow map](flow-map.md) | Line width between places | A movement whose places matter | None |

### Flow

Almost nothing reads as position along a common scale (ribbon widths, arc lengths, floating bars), and node and ribbon ordering changes the picture without changing a number.

| Form | What is drawn | Applies when | Evidence state |
|---|---|---|---|
| [Sankey diagram](sankey-diagram.md) | Ribbon width | Directed movement through ordered states, volume conserved | Measured: one study against chord |
| [Chord diagram](chord-diagram.md) | Arc length, ribbon width at each end | Flows within one set, both ways | Measured: one study against Sankey |
| [Waterfall chart](waterfall-chart.md) | Floating bars on a running total | One total as ordered gains and losses | None |
| Alluvial diagram or parallel sets *(no page)* | Ribbon width | Membership tracked across steps | No page |
| [Flow map](flow-map.md) | Line width on a geography | The states are places | None |

### Network and topology

Position is mostly an optimization output rather than an encoding, so the design axis is whether position means anything.

| Form | What is drawn | Applies when | Evidence state |
|---|---|---|---|
| [Node-link](node-link.md) | Points and lines, placed by a layout algorithm | Sparse, interactive; paths and connectivity | Measured: two studies that disagree |
| [Adjacency matrix](adjacency-matrix.md) | A filled cell per edge | Dense, static; groups and clusters | Measured: two studies that disagree |
| [Hive plot](hive-plot.md) | Nodes on radial axes by rule | Comparing networks, given variables to partition and sort | None |
| [Chord diagram](chord-diagram.md) | A circular weighted graph | Flows within one set, few entities | Measured: one study against Sankey |
| [Sankey diagram](sankey-diagram.md) | A layered weighted directed graph | A quantity moving between states | Measured: one study against chord |

### Qualitative

Nothing is measured. A word cloud puts frequency on text size, an area-like channel distorted by squaring and word length, and discards order and context. No forms table and no indexed types; the candidates, each without a page or a study, are the word cloud, the word tree, the icon array and colored phrases in a passage.

### Tables

A table spends no perceptual channel and gives up shape, trend, outliers and clusters, so every comparison is serial.

| Form | What is drawn | Applies when | Evidence state |
|---|---|---|---|
| A sentence | The conclusion in words | One comparison, no numbers needed | `authority-asserted` |
| A big aggregate number | One value, a line of context | A single quantity | `authority-asserted` |
| A plain table | Digits in a grid | Values looked up, checked or copied | No table-versus-chart study |
| A table beside a chart | Shape in the chart, values in the table | Both tasks real, or Chartability heuristic 30 binds | A published obligation |

## Step 3: defend it

The justification sentence lives on the type page under "Justifying the choice", in three lists: evidence-backed, defensible with the label said out loud, and commonly repeated but unsupported. The refuted reason most often given for each group:

| Group | Refuted reason | Where |
|---|---|---|
| Magnitude | An axis-break glyph makes truncation honest | [refutations.md](../refutations.md#axis-break-glyphs-as-the-truncation-remedy) |
| Ranking | Bars beat pies, so a sorted bar is the most accurate ranking chart | [ranking.md](ranking.md#justifying-the-choice) |
| Part-to-whole | Pies are bad because angle is a weak channel | [refutations.md](../refutations.md#pie-charts-are-read-by-angle) |
| Distribution | Use a box plot instead of a bar chart | [distribution.md](distribution.md#justifying-the-choice) |
| Uncertainty | Error bars are fine as long as you label them | [belia-2005-ci-misconceptions.md](../studies/belia-2005-ci-misconceptions.md) |
| Correlation | Bank the chart to 45 degrees | [refutations.md](../refutations.md#bank-to-45-degrees) |
| Change over time | A log scale is fine for a technical audience | [refutations.md](../refutations.md#log-scales-are-fine-for-expert-audiences) |
| Deviation | A diverging bar makes any two items easy to compare | [deviation.md](deviation.md#justifying-the-choice) |
| Spatial | An equal-area projection fixes the area problem | [spatial.md](spatial.md#justifying-the-choice) |
| Flow | The circular layout is the intuitive one | [refutations.md](../refutations.md#chord-diagrams-are-harder-to-read-than-sankey-diagrams) |
| Network and topology | Matrices beat node-link above twenty nodes | [refutations.md](../refutations.md#matrices-beat-node-link-diagrams-above-twenty-nodes) |
| Qualitative | The word cloud shows what the document is about | [qualitative.md](qualitative.md#justifying-the-choice) |
| Tables | A table is more accurate than a chart | [tables.md](tables.md#justifying-the-choice) |

How hard each finding is pushed, from [SKILL.md](../../SKILL.md): floor violations stay firm, form suggestions are offered once with the trade named, justification corrections are a footnote, and a choice the reader keeps is settled.
