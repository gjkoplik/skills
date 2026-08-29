---
type: chart-type
relationships: [part-to-whole, magnitude]
aliases: [Grid plot, Square pie, Unit chart, Waffle chart]
---

# Waffle charts

A grid of identical cells, one cell per unit of the total, with each part given a whole number of cells. The value is carried by **how many cells a part has**, so the reading is a count rather than a judgment of size.

Also called a **unit chart**, a **grid plot** or a **square pie**. The **isotype** and the **pictogram** are the same construction with a labeled icon in place of the square. **This page treats those two as neighbors rather than as the same form**, for two reasons: the icon carries a pictorial reference the square does not, and the one measured result anywhere near this family is about pictographs specifically rather than about counting (below). Neither icon form has a page in this wiki. [Schwabish](../sources/schwabish.md) files all three as a single catalog entry, "Unit/Isotype/Waffle".

**The FT agrees with this index and splits the family.** It files **Gridplot** under Part-to-whole and **Isotype (pictogram)** under Magnitude, as two separate entries ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). That is independent support for treating the icon forms as neighbors rather than as the same form, arrived at by a scheme that had no stake in this page's decision.

Schwabish files his single entry under **Comparing Categories**, not Part-to-Whole. The filing is verified from the book's own contents pages; what the book argues about the form is not, since its prose is unopened in this corpus. This index files the waffle under part-to-whole because a fixed grid of 100 cells asserts a whole. Both readings are real and the reader's question decides which one is being made, which is the standing position in [README.md](README.md).

## When to reach for it, and when not

The form is defined for the case where the total is a real count, the grid is small enough to tally by eye, one or two shares are the message, and the reader is meant to be able to check the number by counting rather than by trusting the drawing. Being able to check the number by counting is the whole of what this form offers over a pie or a bar.

The first question on [part-to-whole.md](part-to-whole.md) applies here with particular force: where one share is the message, a large number and a sentence may carry it better than a hundred squares.

Questions the form does not answer:

| The question | Alternative |
|---|---|
| How big is this part, precisely? | A table, or a [bar chart](bar-chart.md). A count is only as precise as the grid |
| Which of these is biggest? | Sorted [bar chart](bar-chart.md). Position instead of a tally |
| There are six or more parts | [Pie](pie-and-donut.md) or [treemap](treemap.md). A grid of six colors stops being countable and becomes a texture |
| The shares are not whole numbers at the grid's resolution | A form with a continuous scale. Rounding is the failure this one invites |
| How did composition change between two periods? | [Stacked bar](stacked-bar.md), or a line of shares. Two grids are compared by counting twice, and nothing here says how that goes |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per part with a magnitude, or one row per unit already |
| Transform | Normalize to shares, then **round to a whole number of cells**. The rounding is part of the encoding, not a rendering detail |
| Geometry | Identical small squares, one per cell |
| Scale | Value to a count of cells. Cell size is fixed and carries nothing |
| Coordinates | Cartesian grid, filled in a stated order from one corner |
| Guides | A statement of what one cell is worth, plus a legend or direct labels. No axis exists |

Two slots are doing unusual work. **The transform quantizes**, which no other form in this group does, and everything that goes wrong with this form goes wrong there. **The fill order sits in the coordinates slot** and decides whether a part's cells form one contiguous block or scatter through the grid, which changes what the reader sees without changing a single value.

## Channels

**The reading is a count of discrete cells, and counting is not on the accuracy ordering at all.**

That ordering scores one task, reading a value off a mark and reporting it as a number, and the source states the scope limit itself ([channels.md](../concepts/channels.md#what-the-ranking-is-not-about)):

> "We do not argue that this accuracy of quantitative extraction is the only aspect of a graph for which one might want to develop a theory, but it is an important one."

A tally is a different task. The ranking does not cover it, and no study in this corpus measures it.

**That cuts both ways.** Nothing here supports "a waffle is read more accurately than a pie". The ordering that would have to back such a claim does not reach the task, so the claim has no evidence rather than weak evidence. What the form does is move the reader off the channels the literature measured, onto one it did not.

Two things ride along, both unmeasured here. **Hue carries identity**, which is what hue is good at and what neither Cleveland & McGill table scores ([channels.md](../concepts/channels.md)). And **the filled block has an area**, since one part's cells are usually contiguous. Whether a reader counts the cells or estimates the block is what nobody has tested. `absence of evidence`.

## What it is measurably good at

**Nothing. No study in this corpus tests a waffle chart.**

The nearest measured result is not about this form. Haroz, Kosara & Franconeri (2015) on ISOTYPE visualization is `primary-read` here with no page of its own ([robert-kosara.md](../people/robert-kosara.md)), and found that "superfluous images can distract. But we find no user costs, and some intriguing benefits, when pictographs are used to represent the data." That is a result about embellishment, measured on pictographs used as data marks. It says nothing about counting, and it belongs to the icon variant this page treats as a neighbor.

## What it is measurably bad at

Nothing measured.

The structural cost is **resolution**: a 100-cell grid cannot express anything finer than one percent. That is arithmetic, not an experimental finding.

## What is contested

Nothing. There is no record here to disagree with itself.

Stephen Few's "Unit Charts Are For Kids" sits in the list of his unread newsletter articles ([stephen-few.md](../people/stephen-few.md)). It is the one document within this corpus's reach that would put a named authority against the form, and it is unopened, so the case against the waffle is not in this wiki at all.

## The failure mode it invites

**Rounding, presented as a count.** A part worth 0.4% of the total gets zero cells or one, and either way the grid asserts a whole number the data does not have. The form's entire promise is that the reader can verify by counting, and rounding breaks that promise without leaving a mark.

**Slicing a cell to repair the rounding.** The FT's gloss for the isotype variant states the constraint ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)):

> "use only with whole numbers (do not slice off an arm to represent a decimal)"

It follows from what the mark is rather than from an experiment: a partial glyph is not a countable unit, so a chart containing one has quietly stopped being a tally and become an area estimate. `authority-asserted`, with a definitional argument behind it.

**A grid nobody actually counts.** A hundred cells is a lot of counting, and a reader who stops counting is estimating a block of color, which is the reading the form was chosen to avoid. Where that switch happens is untested here.

## Justifying the choice

**Defensible, evidence-backed:**

Nothing. No study here touches this form, and there is no channel result to inherit either, because the task is a count and the accuracy ordering does not cover counts.

**Defensible, with the label said out loud:**

- "A waffle because the reader should be able to count the units rather than judge a size. That is what the form is for, and no study here measures whether they do."
- "One square is one percentage point and every part is a whole number of squares, so nothing is rounded into the picture."
- "Five parts is about the limit before the grid reads as texture. Convention, with no measured threshold behind it."

**Commonly repeated, and the evidence does not support it:**

- ~~"A waffle is more accurate than a pie, because counting beats estimating an area."~~ Nothing in this corpus measures counting, so this is not a weaker claim than the pie evidence, it is an unmeasured one. Bars beating pies for value extraction is measured ([pie-and-donut.md](pie-and-donut.md)); nothing analogous exists here.
- ~~"Icons are worse than plain squares, because the pictures are chartjunk."~~ The one nearby study found no user cost for pictographs used as data marks.

## See also

- [part-to-whole.md](part-to-whole.md) — the group, and the question of whether a chart is needed at all
- [pie-and-donut.md](pie-and-donut.md) — the same job on channels the literature actually measured
- [../concepts/channels.md](../concepts/channels.md) — the ranking, and the scope limit that keeps it off this page
- [../sources/ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md) — the whole-numbers gloss
- [../sources/schwabish.md](../sources/schwabish.md) — where the unit/isotype/waffle entry is filed, and why the filing is verified while what the book argues about the form is not
