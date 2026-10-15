---
type: index
---

# Flow

A quantity moving between states or conditions, drawn so that both the size of the movement and where it goes are visible at once.

The FT's definition is the one this index uses ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)):

> "Show the reader volumes or intensity of movement between two or more states or conditions. These might be logical sequences or geographical locations."

A flow needs a volume and a between. Without both, the question belongs to another group.

Flow is the least stable category across the two taxonomies here. [Schwabish](../sources/schwabish.md) has none, filing Sankey and waterfall under Comparing Categories and chord under Relationship. The FT puts Sankey, chord and networks under Flow, and waterfall under both Part-to-whole and Flow. These filings are retrieval aids, not facts about charts.

## Is flow the message, or just the shape of the data?

A form here needs to pass all three tests.

**Is there a quantity?** Dollars, people, packets, kilowatt-hours, students. Data that records only that A relates to B has no volume to give a width to, and the drawing collapses to a network with fat edges.

**Is there a between?** Two or more states, with rows that move between them. A cross-tabulation of two attributes of the same rows is not movement. It draws identically and asserts something the data does not contain, which is this group's characteristic lie.

**Does the movement matter more than the endpoints?** If the message is "the total fell by 12" or "these five sources are the biggest", the end sizes are the answer and the ribbons are decoration.

| The reader's actual question | Group |
|---|---|
| How big is each of these? | [Magnitude](magnitude.md). A [bar chart](bar-chart.md) |
| Which is biggest, and in what order? | Ranking. A sorted bar chart |
| How does this one total break down? | [Part-to-whole](part-to-whole.md). A [stacked bar](stacked-bar.md) or a [treemap](treemap.md) |
| How did the total move across many periods? | [Change over time](change-over-time.md). A [line chart](line-chart.md) |
| Who connects to whom, is there a path, are there communities? | [Network and topology](network-topology.md) |
| How far is each item from a target? | [Deviation](deviation.md) |
| Where does the quantity go, and does it add up on the way? | **This group** |

## Flow is a message; a network is a dataset

The FT files networks here and this wiki does not, because flow is one message relational data can carry, alongside community structure, degree distribution and path ([network-topology.md](network-topology.md)). Schwabish files network, chord, arc and tree under Relationship, the same split. [Sankey](sankey-diagram.md) and [chord](chord-diagram.md) diagrams draw weighted graphs and sit in both indexes. This one holds how much went where, the other how the connections are structured, and neither decides which question a dataset carries.

## What this group costs

Almost nothing here is read as position along a common scale, the channel measured most accurately ([channels.md](../concepts/channels.md)).

- A Sankey ribbon is a width at each node, stacked against its neighbors with no common baseline, so a length reading. Along its path it is closer to area.
- A chord's ring segment is arc length, and its ribbons are widths at two endpoints.
- A waterfall's step is a floating bar. Only the opening bar and any drawn totals touch the axis.

[Part-to-whole](part-to-whole.md) makes the same trade, value-reading accuracy for a constraint the form makes visible. The accuracy claims are inherited. None was measured on a chart in this group.

**Ordering** is a second cost the reader cannot see. Every form here orders something to reduce crossings: nodes and ribbons in a Sankey, entities around a chord's ring, steps along a waterfall. That changes the picture without changing a number, as layout does for a [node-link diagram](node-link.md) and ordering for an [adjacency matrix](adjacency-matrix.md). It is unmeasured everywhere.

## Choosing a form

| Form | What carries the value | Where it applies |
|---|---|---|
| [Sankey diagram](sankey-diagram.md) | Ribbon width | Directed movement through ordered states, with the volume conserving at every node as part of the reading |
| [Chord diagram](chord-diagram.md) | Ring arc length, plus ribbon width at each end | Flows within one set of entities, in both directions, with no natural first and last state |
| [Waterfall chart](waterfall-chart.md) | Floating bar length, with the running total at each bar's end | One total decomposed into an ordered sequence of additions and subtractions |
| Alluvial diagram or parallel sets *(no page yet)* | Ribbon width | Category membership tracked across several steps, with the crossings as the message |
| [Flow map](flow-map.md) | Line width on a geography | The states are places and their positions are the point. The one form here whose arrangement is not a design choice |

- **One width-per-unit scale** across the whole figure. Per-column scaling breaks comparison in the direction the reader is looking, and nothing on the chart shows it.
- **Labels on the volumes meant to be read**, since every value here sits on a channel worse than position, usually with no axis.

## Justifying the choice

**Defensible, evidence-backed:**

One result, about layout rather than flow. [Gutwin, Mairena & Bandi (2023)](../studies/gutwin-2023-chord-vs-sankey.md) put 51 novices through 2,040 trials on static [Sankey](sankey-diagram.md) and [chord](chord-diagram.md) drawings of the same 8-to-15-node directed data. The linear layout won on time (18.35s against 22.01s), on errors (0.96 against 1.07 per question), on four effort scales and on preference, 42 to 9.

- "A Sankey rather than a chord diagram, because this is a one-look audience with no interaction available." Defensible with the numbers said out loud. The performance gap is small by the paper's own thresholds (generalized η² of 0.02 and 0.001), largest on first exposure (9.2s and 0.42 errors) and close to gone by the fourth, and the stimuli had no hover highlighting. The large effect is subjective.

No study here tests a waterfall, an alluvial diagram or a [flow map](flow-map.md), or whether a reader can get a volume off a ribbon width, the reading every form here rests on. [Ghoniem et al. (2004)](../studies/ghoniem-2004.md) and [Okoe et al. (2018)](../studies/okoe-2018.md) compared node-link diagrams with adjacency matrices and included no form in this index. Channel-level evidence carries over:

- "The flow volumes are labeled, because a ribbon width is a floating length judgment rather than a position one" ([channels.md](../concepts/channels.md)).

**Defensible, with the label said out loud:**

- "This is a Sankey rather than two stacked bars because the reader needs to see which parts of the first total became which parts of the second." The conservation reading follows from the construction. That readers do better with it is untested.
- "The steps are in the order the accounts are reported, not in the order things happened." Structural, and not recoverable from the drawing.
- "The entities are ordered around the ring by region rather than by size, so the groups read together." Practitioner convention, no measured threshold.

**Commonly repeated, and the evidence does not support it:**

- ~~"A Sankey shows the reader where the money went."~~ It shows one tabulation of source against destination, drawn as movement. Whether anything moved is a property of the data.
- ~~"These forms make the volumes obvious."~~ Unmeasured, and the one study here never asked for a quantity. They make the volumes *visible*.
- ~~"The circular layout is the intuitive one for flows between groups."~~ Novices reading a static chord diagram were slower, more error-prone and much more frustrated than with the linear equivalent, and said the left-to-right frame was why.

## The failure mode this group invites

**Asserting movement the data does not contain.** A ribbon says a quantity left one state and arrived in another. Cross-tabulated attributes, answers to two survey questions and a spend breakdown by two dimensions all make a valid-looking Sankey, and none describes anything moving. The reader cannot check. If what happened to the rows can only be told without a verb of motion the data recorded, the chart is a composition drawn as a flow.

## Types in this index

- [sankey-diagram.md](sankey-diagram.md): also a weighted-network drawing
- [chord-diagram.md](chord-diagram.md): also a weighted-network drawing
- [waterfall-chart.md](waterfall-chart.md): a stacked bar taken apart along an axis of steps
- [flow-map.md](flow-map.md): node positions fixed by geography. Both source taxonomies file it under Spatial, so its flow membership is this wiki's reading

Alluvial diagrams and parallel sets belong here and have no page; the [streamgraph](streamgraph.md) is indexed under change over time. No study in this corpus tests any of them, and no source read here defines the first two names.

## See also

- [network-topology.md](network-topology.md): the other reading of weighted-graph data
- [part-to-whole.md](part-to-whole.md): the same trade, for a different constraint
- [../concepts/channels.md](../concepts/channels.md): what the widths and arcs are read on
- [../sources/ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md): the category definition
- [../sources/schwabish.md](../sources/schwabish.md): a taxonomy with no Flow category
