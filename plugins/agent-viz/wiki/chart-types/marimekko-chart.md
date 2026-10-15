---
type: chart-type
relationships: [part-to-whole, magnitude]
aliases: [Marimekko chart, Mekko, Mosaic plot]
---

# Marimekko charts

A stacked bar chart whose bars also vary in width, each bar's width proportional to its share of the grand total and each segment's height proportional to its share of that bar, so every segment's area is its share of the whole and the full rectangle is the whole.

Also called a mekko. [Schwabish](../sources/schwabish.md) catalogs "Marimekko and Mosaic" as one entry under Comparing Categories (contents pages only), the only vouched statement here that the names cover one form. The FT's **Proportional stacked bar** is the same construction, filed under both Part-to-whole and Magnitude, with Chart Doctor's "How to apply Marimekko to data" as further reading ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). This index files it under [part-to-whole](part-to-whole.md) for the rectangle and [magnitude](magnitude.md) for the widths ([README.md](README.md) on divergent filings).

In statistical graphics "mosaic plot" also names a contingency-table display that no source here defines, so this page does not claim it is the same chart. Stephen Few's "Are Mosaic Plots Worthwhile", unread ([stephen-few.md](../people/stephen-few.md)), would settle it.

## When to reach for it, and when not

The form is defined for two categorical dimensions and one count, where the split inside each group, the relative group sizes, and "this rectangle is all of it" are all part of the claim. Without the group sizes, the width channel costs a dimension of reading for nothing.

| The question | Alternative |
|---|---|
| How big is this segment? | A table. Three quantities are encoded and none is read off a value axis |
| Which group is biggest? | Sorted [bar chart](bar-chart.md). Position instead of width |
| How does one segment fare across groups? | Small multiples, or a [bar chart](bar-chart.md) of that series. Segments float, and columns differ in width too |
| The group totals are all similar | 100% [stacked bar](stacked-bar.md). Near-equal widths carry nothing but still cost reading |
| The columns are a time series | [Stacked bar](stacked-bar.md) or an area chart. Variable widths would read as unequal time steps |
| There is one whole and no second dimension | [Pie](pie-and-donut.md), [stacked bar](stacked-bar.md) or a [treemap](treemap.md) |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (group, part) with a magnitude |
| Transform | Group totals normalized to shares of the grand total (widths); cumulative sum within group normalized to 100% (segment boundaries) |
| Geometry | Rectangle |
| Scale | Group total to width, part share to height, the product to area |
| Coordinates | Cartesian, both axes percent scales: one of the grand total, one of the group |
| Guides | Two percent axes, a legend or in-place labels, and group labels along the width axis |

Drop the width normalization and it is a 100% [stacked bar](stacked-bar.md). The widths turn within-group compositions into a partition of one total, and put the reader on area.

## Channels

Vertically it is a stacked bar: each column's bottom segment is position along a common scale and the rest float as length ([stacked-bar.md](stacked-bar.md), [channels.md](../concepts/channels.md)). On divided bars Cleveland & McGill found "the average errors for length judgments are 40%-250% larger than those for position judgments", a figure inherited here. Horizontally the leftmost column sits on the axis and the rest float, so only the bottom-left mark is anchored both ways. The mark-to-channel step is conjecture in the source literature.

Share of the whole is rectangular area, the reading this form adds. [Heer & Bostock (2010)](../studies/heer-bostock-2010.md) found rectangular area as accurate as circular area, with aspect ratio 1 the worst case, "a result robust across both the rectangle and treemap display conditions". That was one proportional judgment between two rectangles shaped by a squarified treemap layout. A marimekko's shapes come from the data, and the form is untested.

## What it is measurably good at

No study in this corpus tests the form. By definition the drawing is a partition: the areas sum to the whole and nothing hides outside the frame.

## What it is measurably bad at

Nothing measured on this form. Two results are inherited: floating segments carry 40% to 250% more error than position on divided bars ([stacked-bar.md](stacked-bar.md)), and here they float both ways. Area, the reading the form exists for, is read less accurately than position or angle ([channels.md](../concepts/channels.md), via Heer & Bostock). Doing both at once is unmeasured. `absence of evidence`.

## What is contested

Nothing about how it is read. The name is unsettled, as above; "marimekko" avoids the collision.

## The failure mode it invites

**Reading height as area.** Heights are shares within a group, areas shares of the whole. Equal heights in columns of different width are different areas, and nothing says which a label means. This follows from the geometry, not an experiment.

**Tracking one part across the groups.** The stacked bar's worst case plus varying widths. The nearly free remedy is the compared series on the baseline ([stacked-bar.md](stacked-bar.md)).

**Too many cells.** Rectangles shrink while labels do not. No threshold is measured.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing about this form directly. The inherited sentence, stated as such: "I put the series in question on the baseline, because floating segments are read as length, which carries 40% to 250% more error than position. That was measured on divided bars, not on this chart."

**Defensible, with the label said out loud:**

- "A marimekko because the group sizes and the split inside each group are both part of the claim, and the rectangle shows they exhaust the total. No study here measures how well readers do that."
- "The widths carry the group totals, so the columns are deliberately unequal. That is the form's second dimension, not a rendering artifact."
- "Five groups and three parts. Convention, with no measured limit behind it."

**Commonly repeated, and the evidence does not support it:**

- ~~"Each segment's area shows its share of the total, so readers can compare segments anywhere in the chart."~~ The first half is definitional. The second does not follow: area is the weakest channel in play, and the comparison crosses two floating dimensions.
- ~~"It is a stacked bar, so the stacked bar evidence applies."~~ Only to the vertical reading. The width dimension and the area reading are what that evidence does not cover.

## See also

- [stacked-bar.md](stacked-bar.md): this form without the widths, and the floating-segment result
- [treemap.md](treemap.md): the other rectangular-area form here
- [part-to-whole.md](part-to-whole.md): the group
- [../studies/heer-bostock-2010.md](../studies/heer-bostock-2010.md): what was measured about rectangles
- [../concepts/channels.md](../concepts/channels.md): the inherited channel evidence
