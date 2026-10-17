---
type: chart-type
relationships: [correlation]
aliases: [Parallel coordinates, Parallel coordinates plot, Parallel coordinate plot, PCP]
---

# Parallel coordinates

One vertical axis per quantitative variable, set side by side, with each row drawn as a polyline joining its value on every axis.

The [FT](../sources/ft-visual-vocabulary.md) files **Parallel coordinates** under Magnitude: "An alternative to radar charts – again, the arrngement of the variables is important. Usually benefits from highlighting values." [Schwabish](../sources/schwabish.md) files it under Relationship (contents pages only), and [Munzner's](../sources/munzner-vad.md) slides under table arrangements. [Few](../sources/few-effectiveness-profile.md) says "parallel coordinates plot". No source here defines "parallel coordinate plot" or "PCP".

## When to reach for it, and when not

The form is defined for rows carrying more quantitative variables than a scatterplot's two, and a question about how rows move together across them: which variables rise together or trade off, which rows cluster or stand apart. Only adjacent axes are drawn as pairs.

| The question | Alternative |
|---|---|
| How do these two variables relate? | [Scatterplot](scatterplot.md) |
| Which of many variables are related at all? | [Correlation matrix](correlation-matrix.md) as a screen, then scatterplots |
| How did one variable change between two dates? | [Slope chart](slope-chart.md), this form with two axes on one scale |
| What is one entity's profile across several measures? | [Bar chart](bar-chart.md), or the [radar chart](radar-chart.md) the FT names as the alternative |
| The variables are categorical | Parallel sets *(no page)*, bands showing "how the subgroups relate to each other" ([Wilke](../sources/wilke-fundamentals.md)) |
| What are the exact values? | [A table](tables.md) |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per observation, k quantitative variables, often in different units |
| Transform | Usually a per-axis rescaling (min-max or standardized). Axis order and direction are inputs |
| Geometry | One polyline per row, k-1 segments, a vertex on each axis |
| Scale | Each variable to vertical position on its own axis, with its own range and direction |
| Coordinates | Cartesian, x discrete with one position per variable |
| Guides | k labeled axes, each with its own ticks. A key for any highlight color |

A [radar chart](radar-chart.md) is the same construction with radiating axes and closed polylines. Rows in the same order on two adjacent axes draw segments that do not cross, and rows in reversed order draw segments that all cross. Flipping one axis swaps the two pictures without changing the data.

## Channels

Comparing two rows on one axis is position along a common scale, the most accurately read channel in [channels.md](../concepts/channels.md). Across axes there is no value comparison, since each axis has its own range and often its own units. The relationship between adjacent variables rides on segment slope and crossings. Direction ties with length and angle in the 1984 ordering, where "there is not enough information to separate the ties." Here a slope depends on two independent axis scalings and the spacing between axes, so it encodes no rate. The step from mark to channel is conjecture in the source literature.

Highlighted rows use hue for identity, a job hue does well.

## What is measured

No study in this corpus tests the form. [Talbot et al. (2012)](../studies/talbot-2012-slope-ratio.md) measured slope judgment on segment pairs, and it does not transfer: those slopes were rates on one shared scale, while a slope here joins two variables on independent scales.

## The failure mode it invites

**Axis order.** k variables make k(k-1)/2 pairs, and only k-1 sit side by side, so the order decides which relationships are visible. The FT says "the arrngement of the variables is important", `authority-asserted`.

**Axis scaling.** One scale across all variables flattens any with a narrow range. Per-axis min-max makes a variable spanning 99 to 101 fill its axis like one spanning 0 to 1,000. Either choice, and each axis's direction, sets every slope. Whether readers are misled is untested, `absence of evidence`.

**Overplotting.** With many rows the polylines merge into a band whose density depends on line width, transparency and draw order. The cost is `absence of evidence`. The FT's highlighting and Munzner's "hierarchical parallel coordinates" are the remedies named here, neither tested.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing qualifies. Position along a common scale covers comparisons within one axis, not the relationships between axes.

**Defensible, with the label said out loud:**

- "The axes are ordered so the pairs in question sit side by side. A newsroom taxonomy says the arrangement matters, and nobody here tested an ordering."
- "Each axis is rescaled to its own range, and the caption says so, along with any axis that runs upside down."
- "The audience is analysts. Few calls the form familiar to 'select groups of scientists and statisticians' and unfamiliar to the general public, without a study."

**Commonly repeated, and the evidence does not support it:**

- ~~"Parallel coordinates show every relationship among the variables."~~ Only adjacent pairs.
- ~~"Crossing lines mean a negative correlation."~~ Only when both axes run the same way.
- ~~"It reads better than a radar chart."~~ Neither form has been tested.

## See also

- [correlation.md](correlation.md): the group
- [radar-chart.md](radar-chart.md): the polar version, also untested
- [../concepts/channels.md](../concepts/channels.md): the inherited channel evidence
