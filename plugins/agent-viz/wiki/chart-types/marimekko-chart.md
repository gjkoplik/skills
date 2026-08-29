---
type: chart-type
relationships: [part-to-whole, magnitude]
aliases: [Marimekko chart, Mekko, Mosaic plot]
---

# Marimekko charts

A stacked bar chart whose bars also vary in width, each bar's width proportional to its share of the grand total and each segment's height proportional to its share of that bar. Every segment's **area** is then its share of the whole, and the full rectangle is the whole.

Also called a **mekko chart** or just a **Mekko**, and also a **mosaic plot**. [Schwabish](../sources/schwabish.md) catalogs the pair as one entry, "Marimekko and Mosaic", which is the only vouched statement in this wiki about those two names covering one form.

**The FT names the form but not the name.** Its listing has no Marimekko or mosaic entry; the same construction appears as **Proportional stacked bar**, filed under **both Part-to-whole and Magnitude** with identical glosses, and the only further reading it attaches is Chart Doctor's "How to apply Marimekko to data" ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). So the two schemes agree the form is a composition chart and disagree about what to call it, which is the reverse of the mosaic problem below.

It is also a magnitude chart: the bar widths compare the groups against each other, which is a size comparison and not a composition reading. It is indexed under [part-to-whole](part-to-whole.md) first because the full rectangle is the whole, and under [magnitude](magnitude.md) for the widths.

**The name "mosaic plot" collides.** In statistical graphics it names a display built from a contingency table, and **no source in this wiki defines that form**, so this page does not describe it and does not claim it is the same chart. The one document in this corpus's reach that would settle it is Stephen Few's "Are Mosaic Plots Worthwhile", listed among his unread newsletter articles ([stephen-few.md](../people/stephen-few.md)).

**Where it is filed also disagrees.** Schwabish files Marimekko and Mosaic under **Comparing Categories**, verified from the book's own contents pages, while this index files the form under part-to-whole because the rectangle exhausts a real total. The filing is the verified part; what the book argues about the form is not, since its prose is unopened here. Two schemes putting one chart in two groups is the ordinary case rather than a problem, and [README.md](README.md) is where that argument lives.

## When to reach for it, and when not

The form is defined for the case where the data has two categorical dimensions and one count, the reader needs the split inside each group *and* the relative size of the groups, and "this rectangle is all of it" is part of the claim. Where the group sizes are not part of the message, the width channel costs a dimension of reading for nothing.

Questions the form does not answer:

| The question | Alternative |
|---|---|
| How big is this segment? | A table. Three quantities are encoded here and none is read off a value axis |
| Which group is biggest? | Sorted [bar chart](bar-chart.md). Position instead of width |
| How does one segment fare across groups? | Small multiples, or a [bar chart](bar-chart.md) of that series alone. Segments float, and the columns differ in width as well |
| The group totals are all similar | 100% [stacked bar](stacked-bar.md). Equal widths mean the width channel carries nothing and the reader still has to allow for it |
| The columns are a time series | [Stacked bar](stacked-bar.md) or an area chart. Variable widths make the time steps unequal in a way that means something else |
| There is one whole and no second dimension | [Pie](pie-and-donut.md), [stacked bar](stacked-bar.md) or a [treemap](treemap.md) |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (group, part) with a magnitude |
| Transform | Sum within group for the group totals, normalize those to shares of the grand total for the widths, then cumulative-sum within group normalized to 100% for the segment boundaries |
| Geometry | Rectangle |
| Scale | Group total to width, part share to height, and the product to area |
| Coordinates | Cartesian, with both axes percent scales: one of the grand total, one of the group |
| Guides | Two percent axes, a legend or in-place labels, and group labels along the width axis |

**One transform separates this from a form the wiki already covers.** A 100% [stacked bar](stacked-bar.md) is this chart with the width normalization removed and every bar given the same width. Adding it back is what turns a set of within-group compositions into a partition of one grand total, and it is also what puts the reader on area. That is the whole of the marimekko question.

## Channels

**Two nested readings at once, and the segment's share of the whole is on rectangular area.**

Vertically, this is a stacked bar and inherits its channel split exactly: the bottom segment of each column starts at the axis and reads as position along a common scale, and every segment above it floats and reads as length ([stacked-bar.md](stacked-bar.md), [channels.md](../concepts/channels.md)). Cleveland & McGill measured that substitution directly on divided bars, "the average errors for length judgments are 40%-250% larger than those for position judgments". That number is **inherited** here, measured on divided bars rather than on a marimekko.

Horizontally the same structure repeats: the leftmost column starts at the axis, and every column after it floats. **So the floating-segment problem appears twice, in two directions**, and the only mark with a common baseline in both is the bottom-left one.

The area reading is the one the form adds. [Heer & Bostock (2010)](../studies/heer-bostock-2010.md) measured rectangular area, and two of their results bear on this form. Rectangular area matches circular area for accuracy, so nothing extra is lost by using rectangles. And aspect ratio 1 was the worst case, "a result robust across both the rectangle and treemap display conditions". That result was two marked rectangles, aspect ratios drawn from a squarified treemap layout, one proportional judgment. It was not a marimekko, whose rectangles come from the data rather than from a layout algorithm, and nobody has run the experiment on this form.

## What it is measurably good at

**Nothing. No study in this corpus tests a marimekko chart.**

Its one secure property is definitional: the drawing is a partition, so the areas sum to the whole by construction and nothing can hide outside the frame.

## What it is measurably bad at

Nothing measured **on this form**. Two inherited results apply, as inheritance:

- **Floating segments read as length rather than position**, at 40% to 250% more error, measured on divided bars ([stacked-bar.md](stacked-bar.md)). This chart has floating segments in both directions.
- **Area is read less accurately than position or angle** ([channels.md](../concepts/channels.md), via Heer & Bostock). The area reading is the one the form exists for.

Nothing here measures what happens when a reader does both at once, which is the actual task this chart sets. `absence of evidence`.

## What is contested

Nothing about how it is read, because nothing has been measured.

What is genuinely unsettled is the **name**, above: the same word covers this form and a statistical-graphics form that no source in this wiki defines. That is a fact about the term rather than about the chart; "marimekko" names this form without the collision.

## The failure mode it invites

**Reading height as area.** Segment heights are shares *within* a group; segment areas are shares of the *whole*. Two segments with the same height have different areas whenever their groups differ in width, and the chart shows both readings at once with nothing to say which one a label refers to. This is the mistake the form is built to invite, and it follows from the geometry rather than from an experiment.

**Tracking one part across the groups.** The stacked bar's worst case, plus a varying column width. The remedy is the same one and it is nearly free: the series the reader has to compare sits on the baseline ([stacked-bar.md](stacked-bar.md)).

**Too many cells.** Every extra group or part shrinks rectangles in one dimension while the labels stay the same size. There is no measured threshold, and the practical one arrives early.

## Justifying the choice

**Defensible, evidence-backed:**

Nothing about this form directly. What is available is inherited, and stated that way: "I put the series in question on the baseline, because floating segments are read as length, which carries 40% to 250% more error than position. That was measured on divided bars, not on this chart."

**Defensible, with the label said out loud:**

- "A marimekko because the group sizes and the split inside each group are both part of the claim, and the rectangle shows they exhaust the total. No study here measures how well readers do that."
- "The widths carry the group totals, so the columns are deliberately unequal. That is the form's second dimension, not a rendering artifact."
- "Five groups and three parts. Convention, with no measured limit behind it."

**Commonly repeated, and the evidence does not support it:**

- ~~"Each segment's area shows its share of the total, so readers can compare segments anywhere in the chart."~~ The first half is definitional and secure. The second does not follow: area is the least accurately read of the channels in play here, and the comparison crosses two floating dimensions.
- ~~"It is a stacked bar, so the stacked bar evidence applies."~~ It applies to the vertical reading. The width dimension and the area reading are exactly what that evidence does not cover.

## See also

- [stacked-bar.md](stacked-bar.md) — the form this one adds a width to, and where the measured floating-segment result lives
- [treemap.md](treemap.md) — the other rectangular-area form in this group, and the aspect-ratio result
- [part-to-whole.md](part-to-whole.md) — the group, and what composition costs
- [../studies/heer-bostock-2010.md](../studies/heer-bostock-2010.md) — what was actually measured about rectangles
- [../concepts/channels.md](../concepts/channels.md)
