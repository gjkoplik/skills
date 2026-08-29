---
type: chart-type
relationships: [spatial, flow]
aliases: [Flow map, Origin-destination map]
---

# Flow maps

Movement drawn on a map: a line, arc or tapering band from origin to destination, with width encoding the volume that moved and both endpoints pinned to real geography.

## When to reach for it, and when not

**The form applies where** the states between which something moves are *places*, where those places sit relative to each other is part of what is read, and there is a genuine quantity attached to the movement.

The FT's one-line test turns on its adjective ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)): "For showing unambiguous movement across a map." Unambiguous means the data records a direction and a volume, not a co-occurrence drawn as an arrow.

**Questions the form does not answer:**

| The question | Alternative |
|---|---|
| The places are effectively labels, and distance and direction carry nothing | [Sankey diagram](sankey-diagram.md). A Sankey can order its nodes to reduce crossings; a map cannot |
| How much moved, exactly? | A table, or a labeled origin-destination matrix. There is no axis on a map |
| Where are the things, rather than where did they go? | [Choropleth](choropleth-map.md), [dot density](dot-density-map.md), or a proportional symbol map, and see [spatial.md](spatial.md) |
| Flows run within one entity set with no geography worth showing | [Chord diagram](chord-diagram.md) |
| Every place connects to every other | [Adjacency matrix](adjacency-matrix.md) on the origin-destination table. The map version is a solid block of ink |
| Nothing actually moved; these are two attributes of the same rows | Nothing in [flow.md](flow.md). The arrows would assert a journey the data does not record |
| The totals per place are the message | Proportional symbol map, or a [bar chart](bar-chart.md) with no map at all |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (origin, destination, volume), with both places carrying coordinates |
| Transform | Usually none on the values. Often aggregation of points to region centroids, and sometimes route simplification or edge bundling, both of which move ink without changing a number |
| Geometry | A line, arc or tapering band per flow over a base map, commonly with an arrowhead or a taper carrying direction |
| Scale | Volume to line width. Position is set by the projection, not by the values |
| Coordinates | A map projection |
| Guides | The base map, direction marks, a stated projection, and a width legend, which is the guide most often missing |

## What makes it different from everything else in its group

[flow.md](flow.md) names one cost every form in the group imposes: an ordering the designer sets, that changes the picture, and that the reader cannot see. A Sankey orders nodes within a stage, a chord orders entities around the ring, a waterfall orders its steps.

**The flow map is the exception.** The endpoints are fixed by geography, so there is no ordering artifact and no version of the same data that looks different under a different sort.

The form pays for that twice, and both charges are definitional:

**Crossings cannot be reduced.** They are a fact about the geography and the origin-destination table, and the only remaining moves are aggregating flows, dropping small ones, or bundling edges, all of which change what is on the chart rather than how it is arranged.

**Ink stops being proportional to volume.** A flow's ink is roughly its width times its path length, and only the width comes from the data. A small flow across an ocean lays down more ink than a large one across a city. Nothing on the chart corrects for it, and the reader has no way to discount it. That is a sharper version of the proportional-ink concern than the one [observable-plot.md](../sources/observable-plot.md) discusses by mark, because here the violation is imposed by the coordinate system rather than chosen by the designer.

## Channels

**Width for the volume**, which is a floating length judgment against no common baseline and with no axis anywhere on the figure, and **position on a projected plane** for the endpoints, which is not position along a common scale in the sense [channels.md](../concepts/channels.md) measures. Path length and ink area come along uninvited, as above.

Inherited with the link, and with the standing caveat that the step from this chart to those channels is conjecture. Nothing here has been decomposed the way [Skau & Kosara](../studies/skau-kosara-2016.md) decomposed a pie.

One channel is spent before anything is drawn: **the projection distorts area, and on this form it also distorts the apparent length of every flow.** [spatial.md](spatial.md) carries the rule and the sources for it.

## What it is measurably good at

**Nothing. No study in this corpus tests a flow map.**

The nearest measurement is [Gutwin, Mairena & Bandi (2023)](../studies/gutwin-2023-chord-vs-sankey.md), which compared a radial against a linear layout of the same flow data and found the linear one faster, marginally more accurate and strongly preferred. It does not transfer, and the reason is exactly what this page is about: that study manipulated *layout*, and a flow map has no layout to manipulate. Its participants' stated reason for preferring the Sankey, a familiar left-to-right frame of reference, is a property a map cannot offer either way.

[Ghoniem et al. (2004)](../studies/ghoniem-2004.md) and [Okoe et al. (2018)](../studies/okoe-2018.md) measured node-link diagrams against adjacency matrices with a free layout, which is the thing this form removes.

## What it is measurably bad at

Nothing measured. Two exposures follow from the structure, and both are stated above rather than repeated here: crossings that cannot be arranged away, and ink that scales with distance.

A third, and it is where the form usually breaks in practice. **Below a couple of pixels a flow line is present and unreadable**, and a map of a hundred origin-destination pairs reads as the three or four widest arcs plus texture. Aggregating the tail is the same move as "other" in [part-to-whole.md](part-to-whole.md), and there is no measured threshold for it here or anywhere else in this corpus.

## What is contested

**Nothing empirical.** There is no record here to disagree with itself.

**Where it belongs is genuinely contested, and both source taxonomies come out against this wiki.** The FT files Flow map under **Spatial**, not under Flow, and [Schwabish](../sources/schwabish.md) files it under **Geospatial**. Only [flow.md](flow.md) names it as a flow form, which is this wiki's own reading, on the grounds that the message is a volume moving between states and the states happen to be places. The page carries both relationships for that reason. This is a retrieval disagreement, not a claim about the chart.

## The failure mode it invites

**Asserting a journey the data does not record.** This is [flow.md](flow.md)'s characteristic lie and the map makes it worse, because an arrow between two real places reads as a route. Migration counts tabulated by birthplace and current residence say where people are now and where they were born; they do not say anyone traveled the line drawn, or when, or by what path. `authority-asserted`, and it follows from what the mark means.

**Being trusted because the exemplar is famous.** The most-cited flow map is Minard's 1869 march on Moscow, which [Tufte](../people/edward-tufte.md) called possibly the best statistical graphic ever drawn. That page records Hugh Small's objection: the figure's temperature curve reads as though the army froze to death, while roughly 300,000 were lost on the advance against 90,000 on the retreat. `secondary-only`, from Small. The causal story everyone takes from that chart is carried by juxtaposition rather than by anything the data encodes, which is a caution about the form and not only about one drawing of it.

## Justifying the choice

**Defensible, evidence-backed:**

Nothing is native to this form. Two sentences are inheritable, with the link:

- "The volumes are labeled, because a line width is a floating length judgment and this chart has no axis" ([channels.md](../concepts/channels.md)).
- "An equal-area projection, because area on a map weights what the reader takes from it whether or not area is the encoding" ([spatial.md](spatial.md), which carries the Urban Institute's projection rule).

**Defensible, with the label said out loud:**

- "A map rather than a Sankey, because where these places are is part of the message, and fixing the endpoints to geography is what buys me an arrangement I did not choose." Structural, and untested.
- "For showing unambiguous movement across a map." The FT's gloss, `authority-asserted` as published.
- "Flows under a hundred units are aggregated into one band, because below about two pixels a line is there and unreadable." Practitioner convention, no measured threshold.

**Commonly repeated, and the evidence does not support it:**

- ~~"A flow map shows where people went."~~ It shows an origin-by-destination tabulation drawn as movement along a straight line nobody traveled. Whether anything moved, and by what route, are facts about the data.
- ~~"The line widths are proportional to the volumes, so readers read the volumes off them."~~ The first half is definitional. The second half is untested here on any flow form, and this one adds a distance term to the ink that the reader cannot discount.
- ~~"Minard's chart is the proof that this form works."~~ It is one much-admired drawing, the admiration is `authority-asserted`, and the causal reading it is admired for has a documented objection.

## See also

- [flow.md](flow.md) — the group, and the free parameter this form is the only member to escape
- [spatial.md](spatial.md) — where both source taxonomies actually file this, and the projection and colormap rules
- [sankey-diagram.md](sankey-diagram.md) — the same data with the geography thrown away and the ordering back as a free parameter
- [chord-diagram.md](chord-diagram.md)
- [../studies/gutwin-2023-chord-vs-sankey.md](../studies/gutwin-2023-chord-vs-sankey.md) — the group's one measurement, and why it does not reach this page
- [../people/edward-tufte.md](../people/edward-tufte.md) — the Minard judgment and the objection to it
