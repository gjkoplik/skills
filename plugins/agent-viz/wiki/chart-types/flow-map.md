---
type: chart-type
relationships: [spatial, flow]
aliases: [Flow map, Origin-destination map]
---

# Flow maps

Movement drawn on a map: a line, arc or tapering band from origin to destination, with width encoding the volume that moved and both endpoints pinned to real geography.

## When to reach for it, and when not

The form applies where a quantity moves between places and where those places sit is part of the message. The FT's test ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)) is "For showing unambiguous movement across a map": the data records a direction and a volume, not a co-occurrence.

| The question | Alternative |
|---|---|
| The places are just labels; distance and direction carry nothing | [Sankey diagram](sankey-diagram.md), which can order nodes to reduce crossings |
| How much moved, exactly? | A table, or a labeled origin-destination matrix. A map has no axis |
| Where are things, not where did they go? | [Choropleth](choropleth-map.md), [dot density](dot-density-map.md) or proportional symbol map ([spatial.md](spatial.md)) |
| Flows within one entity set, with no geography worth showing | [Chord diagram](chord-diagram.md) |
| Every place connects to every other | [Adjacency matrix](adjacency-matrix.md). The map would be a block of ink |
| Nothing moved; these are two attributes of the same rows | Nothing in [flow.md](flow.md). Arrows would assert a journey |
| The totals per place are the message | Proportional symbol map, or a [bar chart](bar-chart.md) with no map |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (origin, destination, volume), both places carrying coordinates |
| Transform | Usually none on values. Often aggregation to region centroids, sometimes route simplification or edge bundling, which move ink without changing a number |
| Geometry | A line, arc or tapering band per flow over a base map, with an arrowhead or taper for direction |
| Scale | Volume to line width. Position is set by the projection, not the values |
| Coordinates | A map projection |
| Guides | Base map, direction marks, a stated projection, and a width legend, the one most often missing |

Every other form in [flow.md](flow.md) carries an ordering the designer sets and the reader cannot see (Sankey nodes, a chord's ring, waterfall steps). Geography fixes a flow map's endpoints, so it has none. By definition it pays twice:

- **Crossings cannot be reduced.** Aggregating, dropping or bundling flows changes what is on the chart, not its arrangement.
- **Ink stops being proportional to volume.** Ink is roughly width times path length, and only width is data, so a small flow across an ocean outweighs a large one across a city. The coordinate system imposes this, unlike the per-mark violations [observable-plot.md](../sources/observable-plot.md) discusses.

## Channels

Volume is width, a floating length with no baseline or axis. Endpoints are position on a projected plane, not position along a common scale as [channels.md](../concepts/channels.md) measures it. Path length and ink area come uninvited. The mark-to-channel step is conjecture in the source literature, and nobody has decomposed the form as [Skau & Kosara](../studies/skau-kosara-2016.md) did a pie. The projection distorts area and the apparent length of every flow ([spatial.md](spatial.md)).

## What it is measurably good at

No study in this corpus tests the form. [Gutwin, Mairena & Bandi (2023)](../studies/gutwin-2023-chord-vs-sankey.md) found a linear flow layout faster, marginally more accurate and strongly preferred over a radial one, for a familiar left-to-right frame. That manipulated layout, which a flow map does not have. [Ghoniem et al. (2004)](../studies/ghoniem-2004.md) and [Okoe et al. (2018)](../studies/okoe-2018.md) tested node-link diagrams with the free layout this form removes.

## What it is measurably bad at

Nothing measured. Beyond the two structural costs, a flow line under a couple of pixels is present and unreadable, so a hundred origin-destination pairs read as the three or four widest arcs plus texture. Aggregating the tail is the "other" move in [part-to-whole.md](part-to-whole.md), with no measured threshold.

## What is contested

Nothing empirical. The filing is contested: the FT files Flow map under Spatial and [Schwabish](../sources/schwabish.md) under Geospatial. Only this wiki's [flow.md](flow.md) treats it as a flow form, since the message is a volume moving between places. The page carries both relationships. That is a retrieval disagreement, not a claim about the chart.

## The failure mode it invites

**Asserting a journey the data does not record.** The characteristic lie of [flow.md](flow.md) is worse on a map, where an arrow reads as a route. Migration counts by birthplace and residence say nothing about who traveled the line, when, or how. `authority-asserted`.

**Trusting the famous exemplar.** [Tufte](../people/edward-tufte.md) called Minard's 1869 march on Moscow, the most-cited flow map, possibly the best statistical graphic ever drawn. Hugh Small objects that its temperature curve implies the army froze, while roughly 300,000 were lost on the advance against 90,000 on the retreat. `secondary-only`, from Small. The causal story rests on juxtaposition, not on anything the data encodes.

## Justifying the choice

**Defensible, evidence-backed:**

Nothing native. Two sentences inherit:

- "The volumes are labeled, because a line width is a floating length judgment and this chart has no axis" ([channels.md](../concepts/channels.md)).
- "An equal-area projection, because area on a map weights what the reader takes from it whether or not area is the encoding" ([spatial.md](spatial.md), which carries the Urban Institute's projection rule).

**Defensible, with the label said out loud:**

- "A map rather than a Sankey, because where these places are is part of the message, and fixing the endpoints to geography is what buys me an arrangement I did not choose." Structural, and untested.
- "For showing unambiguous movement across a map." The FT's gloss, `authority-asserted` as published.
- "Flows under a hundred units are aggregated into one band, because below about two pixels a line is there and unreadable." Practitioner convention, no measured threshold.

**Commonly repeated, and the evidence does not support it:**

- ~~"A flow map shows where people went."~~ It shows an origin-by-destination tabulation drawn as movement along a line nobody traveled.
- ~~"The line widths are proportional to the volumes, so readers read the volumes off them."~~ The first half is definitional. The second is untested, and this form adds distance to the ink.
- ~~"Minard's chart is the proof that this form works."~~ One drawing, admired on `authority-asserted` grounds, with a documented objection to its causal reading.

## See also

- [flow.md](flow.md): the group, and the ordering parameter this form escapes
- [spatial.md](spatial.md): the source taxonomies' filing, and the projection and colormap rules
- [sankey-diagram.md](sankey-diagram.md): the same data without geography
- [chord-diagram.md](chord-diagram.md): flows within one entity set
- [../studies/gutwin-2023-chord-vs-sankey.md](../studies/gutwin-2023-chord-vs-sankey.md): the group's one measurement
- [../people/edward-tufte.md](../people/edward-tufte.md): the Minard judgment and the objection
