---
type: chart-type
relationships: [part-to-whole, magnitude]
aliases: [Grid plot, Square pie, Unit chart, Waffle chart]
---

# Waffle charts

A grid of identical cells, one per unit of the total, with each part given a whole number of cells, so the reading is a count rather than a judgment of size.

It is also called a unit chart, a grid plot or a square pie. The isotype and pictogram, with a labeled icon for the square, are treated as neighbors without pages of their own: the icon carries a pictorial reference, and the one nearby measured result is about pictographs, not counting. The FT splits the family the same way, Gridplot under Part-to-whole and Isotype (pictogram) under Magnitude ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). [Schwabish](../sources/schwabish.md) files all three as one entry, "Unit/Isotype/Waffle", under Comparing Categories, verified from the contents pages with the prose unopened. This index uses part-to-whole because a fixed grid of 100 cells asserts a whole. The reader's question decides the reading ([README.md](README.md)).

## When to reach for it, and when not

The form is defined for a total that is a real count, a grid small enough to tally by eye, and one or two shares as the message. Its offer over a pie or a bar is that the reader can check the number by counting. Where one share is the message, a large number and a sentence may do better ([part-to-whole.md](part-to-whole.md)).

| The question | Alternative |
|---|---|
| How big is this part, precisely? | A table, or a [bar chart](bar-chart.md). A count is only as precise as the grid |
| Which of these is biggest? | Sorted [bar chart](bar-chart.md) |
| There are six or more parts | [Pie](pie-and-donut.md) or [treemap](treemap.md). Six colors stop being countable and become a texture |
| The shares are not whole numbers at the grid's resolution | A form with a continuous scale |
| How did composition change between two periods? | [Stacked bar](stacked-bar.md), or a line of shares. Comparing two grids means counting twice, untested here |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per part with a magnitude, or one row per unit already |
| Transform | Normalize to shares, then round to a whole number of cells. The rounding is part of the encoding |
| Geometry | Identical small squares, one per cell |
| Scale | Value to a count of cells. Cell size carries nothing |
| Coordinates | Cartesian grid, filled in a stated order from one corner |
| Guides | What one cell is worth, plus a legend or direct labels. No axis exists |

The transform quantizes, unlike any other form in the group, and most failures start there. The fill order decides whether a part's cells form one block or scatter.

## Channels

The reading is a count of discrete cells, and counting is not on the accuracy ordering. That ordering scores reading a value off a mark, and the source states the limit itself ([channels.md](../concepts/channels.md#what-the-ranking-is-not-about)):

> "We do not argue that this accuracy of quantitative extraction is the only aspect of a graph for which one might want to develop a theory, but it is an important one."

No study in this corpus measures a tally, so "a waffle is read more accurately than a pie" has no evidence, not weak evidence.

Hue carries identity, which neither Cleveland & McGill table scores ([channels.md](../concepts/channels.md)). A part's contiguous block also has an area, and whether readers count cells or estimate the block is `absence of evidence`.

## What it is measurably good at

No study in this corpus tests the form.

The nearest result is Haroz, Kosara & Franconeri (2015) on ISOTYPE visualization, `primary-read` here with no page of its own ([robert-kosara.md](../people/robert-kosara.md)): "superfluous images can distract. But we find no user costs, and some intriguing benefits, when pictographs are used to represent the data." That is about embellishment on the icon neighbor, not counting.

## What it is measurably bad at

Nothing measured. A 100-cell grid cannot express anything finer than one percent, which is arithmetic.

## What is contested

Nothing contested in this corpus. Stephen Few's "Unit Charts Are For Kids", the one reachable case against the form, is among his unread newsletter articles ([stephen-few.md](../people/stephen-few.md)).

## The failure mode it invites

**Rounding presented as a count.** A part worth 0.4% of the total gets zero cells or one, and either way the grid asserts a whole number the data lacks, invisibly.

**Slicing a cell to repair the rounding.** The FT's gloss on the isotype variant ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)):

> "use only with whole numbers (do not slice off an arm to represent a decimal)"

A partial glyph is not a countable unit, so the chart becomes an area estimate. `authority-asserted`, with a definitional argument behind it.

**A grid nobody counts.** A reader who stops counting is estimating a block of color, at an untested point.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing. No study here touches the form, and there is no channel result to inherit, because the accuracy ordering does not cover counts.

**Defensible, with the label said out loud:**

- "A waffle because the reader should be able to count the units rather than judge a size. That is what the form is for, and no study here measures whether they do."
- "One square is one percentage point and every part is a whole number of squares, so nothing is rounded into the picture."
- "Five parts is about the limit before the grid reads as texture. Convention, with no measured threshold behind it."

**Commonly repeated, and the evidence does not support it:**

- ~~"A waffle is more accurate than a pie, because counting beats estimating an area."~~ Counting is unmeasured. Bars beating pies for value extraction is measured ([pie-and-donut.md](pie-and-donut.md)); nothing analogous exists here.
- ~~"Icons are worse than plain squares, because the pictures are chartjunk."~~ The one nearby study found no user cost for pictographs used as data marks.

## See also

- [part-to-whole.md](part-to-whole.md): the group, and whether a chart is needed at all
- [pie-and-donut.md](pie-and-donut.md): the same job on measured channels
- [../concepts/channels.md](../concepts/channels.md): the ranking, and the scope limit that keeps it off this page
- [../sources/ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md): the whole-numbers gloss
- [../sources/schwabish.md](../sources/schwabish.md): where the unit/isotype/waffle entry is filed, and why the filing is verified while the book's argument is not
