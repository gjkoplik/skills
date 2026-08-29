---
type: chart-type
relationships: [deviation]
aliases: [Population pyramid, Spine chart]
---

# Spine charts

One row per category, each row's total split into two contrasting components that run in opposite directions from a shared central line.

**The name is not vouched by any source in this wiki, so read the definition above as this page's stipulation.** Nothing in the corpus defines a spine chart: [ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md) reproduces the nine relationship definitions and a sample of per-chart glosses, and this form is not among the glosses quoted there. The term is not used consistently in the field, so the name alone does not fix which form is meant, and the definition above stands unchecked against any source that later defines it.

The population pyramid is the version everyone has seen: rows are age bands, the two components are men and women. **That one has a primary definition, under a different name.** [Wilke](../sources/wilke-fundamentals.md) builds it as an **age pyramid**: "we can also make two separate histograms, rotate them by 90 degrees, and have the bars in one histogram point into the opposite direction of the other." Read as two mirrored histograms it is also a distribution chart, which is where [Schwabish](../sources/schwabish.md) files Pyramid. The general two-component form above is still this page's stipulation; the pyramid special case is not.

## When to reach for it, and when not

The form is defined for the case where each row is one total split in two, the split is the message, and the two parts are opposed in kind rather than ordered. Two components and one row per category is the whole of its range.

Questions the form does not answer:

| The question | Alternative |
|---|---|
| How big is each row's total? | [Stacked bar](stacked-bar.md) or a [bar chart](bar-chart.md). The total is the one quantity this form makes hard to read, see below |
| One signed number per row, above or below a reference | [Diverging bar chart](diverging-bar-chart.md) |
| There are three or more components per row | [Stacked bar](stacked-bar.md), or the diverging stacked bar on [diverging-bar-chart.md](diverging-bar-chart.md) |
| How does one component compare across rows? | A sorted [bar chart](bar-chart.md) of that component alone |
| Do the parts exhaust the total, and is that the claim? | [Part-to-whole](part-to-whole.md). This form asserts nothing about a whole |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per category, with exactly two component magnitudes |
| Transform | None, or normalize each row to shares. No cumulative sum: the two components share one boundary |
| Geometry | Two filled rectangles per row, meeting at the center line |
| Scale | Component magnitude to length, both anchored at the center, one running each way |
| Coordinates | Cartesian, usually with the category axis vertical |
| Guides | The center line, a legend or direct labels naming the two components, one quantitative axis whose values are unsigned on both sides |

**This is a two-segment [stacked bar](stacked-bar.md) cut at the segment boundary and hinged there,** and the trade that produces is the whole reason the form exists. A stacked bar puts segment one on the baseline and lets segment two float, and its total reads as position along a common scale. Hinging at the boundary puts *both* components on a shared line, so both are read the same way, and the row total stops being a position reading altogether: it is now the sum of two lengths running in opposite directions, which the reader has to add across the center by eye. **The second component's baseline is bought with the total.** Definitional.

Normalizing each row to shares makes the ratios comparable across rows and removes the totals for good, exactly as it does on a [stacked bar](stacked-bar.md).

## Channels

**Length from a shared center line**, twice per row. Within one side that is a reading of position along a common scale, inherited from [channels.md](../concepts/channels.md) with the standing caveat that the mapping from chart to channel is conjecture rather than measurement.

**The comparison the chart is built for crosses the line**, since the point is component A against component B in the same row. Two lengths running in opposite directions from a common origin are not two bars off a common baseline, and nothing in this corpus measures that judgment. `absence of evidence`.

**Which component is which rides on side, doubled in hue.** Neither is a magnitude channel and the accuracy ordering scores neither ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)).

## What it is measurably good at

**Nothing. No study in this corpus tests a spine chart.**

## What it is measurably bad at

Nothing measured. The structural cost is the total, named above, and it is definitional rather than an experimental result.

## What is contested

Nothing. There is no record here to disagree with itself, and there is barely a record.

## The failure mode it invites

**Reading the outer edges as a total.** The two components sit on opposite sides of the center, so the row's overall size is the least legible quantity on a chart that appears to be about sizes. A long row and a short row can hold the same total.

**Normalizing silently.** Rows of shares and rows of counts produce very similar pictures and answer different questions. Both are legitimate; the chart does not say which one it is without a labeled axis.

Both follow from the structure. Neither has been tested on readers.

## Justifying the choice

**Defensible, evidence-backed:**

Nothing. No study here touches this form, and the only inheritance available is the same-side position reading it shares with every bar chart ([bar-chart.md](bar-chart.md), [channels.md](../concepts/channels.md)).

**Defensible, with the label said out loud:**

- "Both components run off one center line, so neither is the floating segment a stacked bar would have made it." That follows from the geometry; what a reader gets from it is untested.
- "Rows are counts rather than shares, and the axis says so, because the size of each band is part of the point."
- "Two components only. Anything more goes back to a stacked form." Convention, with no measured threshold behind it.

**Commonly repeated, and the evidence does not support it:**

- ~~"A spine chart shows the balance between the two groups accurately."~~ It shows which side is longer by construction. The size of the gap is a cross-center comparison that nobody in this corpus has measured.
- ~~"It is just a bar chart mirrored, so the bar chart evidence applies."~~ It applies to each side separately. The comparison the form exists for is the one the evidence does not cover.

## See also

- [diverging-bar-chart.md](diverging-bar-chart.md) — the other form in this group, defined for a row carrying one signed number
- [stacked-bar.md](stacked-bar.md) — the form this one is a hinged two-segment case of, and where the measured baseline result lives
- [deviation.md](deviation.md) — the group, and the argument about the reference point
- [../concepts/channels.md](../concepts/channels.md)
