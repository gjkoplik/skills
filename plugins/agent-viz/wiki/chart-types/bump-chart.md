---
type: chart-type
relationships: [ranking, change-over-time]
aliases: [Bump chart]
---

# Bump charts

One line per item across several periods, with the vertical axis carrying **position in the ordering** rather than the value, so each line traces where its item sat at each period and the crossings are the reorderings.

## When to reach for it, and when not

**The form applies where** there are several periods, few enough items to label at the ends, and the reader's question is who overtook whom. It is the only form in this wiki that puts the rank itself on an axis, which is both what it offers and what it costs.

It is also a change-over-time chart. It is indexed under [ranking](ranking.md) because the ordering is what it draws; the amounts do not survive the transform. [change-over-time.md](change-over-time.md) carries the group's other free parameters.

**Questions the form does not answer:**

| The question | Alternative |
|---|---|
| How much did each one change? | [Line chart](line-chart.md). The rank axis has already thrown the amount away |
| There are exactly two periods | [Slope chart](slope-chart.md). Same crossings, and it keeps the values |
| How big is each item now? | [Magnitude](magnitude.md). A [bar chart](bar-chart.md), sorted |
| Is one item's trend accelerating or plateauing? | [Line chart](line-chart.md). Shape in the value, which is not on this axis |
| Which items are close together and which are far apart? | Nothing here answers it. The values, drawn |
| There are fifty items | Nothing here works either. Aggregation, faceting, or a drawn subset |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per item per period, with a value |
| Transform | **Rank within each period.** The only slot doing real work, and it is destructive: the value does not survive it |
| Geometry | One line per item across the periods, usually with a marker at each period |
| Scale | Rank to position on a common vertical scale, conventionally inverted so that first place sits at the top |
| Coordinates | Cartesian, with x taking one position per period |
| Guides | A rank axis or per-period rank labels, direct item labels at one or both ends, and highlighting for the items the reader is meant to follow |

**It is a [line chart](line-chart.md) with a rank transform in front of it.** That is the whole structural difference, and two consequences follow that carry no evidence label because they are definitional.

**A rank axis throws away the magnitude, which is the point and the cost at the same time.** The transform maps every value to its place, so the spacing between adjacent lines is a property of the item count rather than of the data. Two lines crossing means a reordering **of any size**, including one that turned on a rounding error. Two lines running parallel a long way apart may be separated by a hair. The chart is built to make the ordering unambiguous and it does that by deleting the only thing that would say whether the ordering mattered.

**The vertical range is not a free parameter.** It runs from first place to last and the item count fixes it, so the axis-range manipulation measured on other charts in this family has no handle here. There is nothing to truncate. The aspect ratio remains a free parameter, and so does the choice of periods.

## Channels

**Position along a common scale**, carrying the rank. That inheritance from [channels.md](../concepts/channels.md) comes with the usual caveat that the mapping is conjecture in the source literature, and with a second one specific to this form: the accuracy ordering measures how well a reader gets a *value* off a mark, and by the time the mark is drawn here the value has been replaced by an ordinal. The best-measured channel in the literature is being used to carry something the literature never measured anyone reading. See [the scope limit](../concepts/channels.md#what-the-ranking-is-not-about).

**Direction and slope** carry the movement, and slope is among the tasks Cleveland & McGill said they could not separate from angle, in an ordering they called a tentative working hypothesis ([channels.md](../concepts/channels.md)). Slope means less here than on a [line chart](line-chart.md) anyway: its steepness is places-per-period, not units-per-period.

## What it is measurably good at

**Nothing. No study in this corpus tests a bump chart.**

The inheritance is thinner here than on most pages rather than merely absent. A [line chart](line-chart.md) can at least borrow the position result, because there are values on its axis. This form cannot borrow it in the usual sense, since what sits on position is the output of the transform.

## What it is measurably bad at

Nothing measured. Two untested exposures, recorded as exposures and not as findings:

**Whether readers over-read a crossing.** The definitional half is secure and is above. Whether people take a crossing for a large change is `absence of evidence`: nobody has looked, and it is not a prohibition.

**Tangle at many items.** Same shape of problem as the spaghetti chart, with no measured threshold. Schwabish's name for the guideline is "Avoid the Spaghetti Chart" ([schwabish.md](../sources/schwabish.md)). `authority-asserted`.

## What is contested

Nothing. Nobody has published a result about this form that could disagree with anything else.

## The failure mode it invites

**Presenting a reordering as a change.** The form's whole job is to make crossings visible, and a crossing is exactly as loud when the two items were a rounding error apart as when one collapsed. The remedy recorded here is not avoiding the form but putting the amount back somewhere the reader can reach it: end labels, a companion panel of the values, or a caption line saying how close the ranks were. `authority-asserted` as advice; the underlying fact about the transform is definitional.

**Letting the item set do the work.** A rank is relative to the population, so adding or dropping one item moves every rank below it while nothing about the remaining items has changed. Two bump charts built from different sets are not comparable, and the chart shows no sign of it. [ranking.md](ranking.md) states this once for the whole group.

**Cherry-picking the first and last period.** The middle is what distinguishes this form from a [slope chart](slope-chart.md), so a bump chart whose story is entirely in its endpoints was a slope chart that would have kept the values.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing. The rank transform puts the form out of reach of even the channel inheritance the other pages lean on.

**Defensible, with the label said out loud:**

- "A bump chart, because the question is who overtook whom across six seasons and the amounts are not the message. Practitioner convention; nothing in this corpus tests the form."
- "Eight items rather than thirty, because the lines tangle. No measured threshold exists; the guideline is one practitioner's, stated for line charts generally."
- "The two teams in question are in color and the rest are gray. Widely recommended, never measured ([refutations.md](../refutations.md#gray-plus-one-accent-as-an-evidence-backed-rule))."
- "The values are printed at both ends, because the rank axis does not carry them. That follows from the transform, and whether it helps a reader is untested."

**Commonly repeated, and the evidence does not support it:**

- ~~"A bump chart shows the change clearly."~~ It shows the ordering and its changes. The change itself is the thing the rank transform deleted, and nobody has measured what a reader takes from one either way.
- ~~"Lines crossing means the two swapped in a meaningful way."~~ Definitionally it means they swapped. By how much is not on the chart, and cannot be recovered from it.
- ~~"It is a line chart, so the line-chart evidence carries over."~~ The line-chart evidence is about reading values off position. There are no values on this chart.

## See also

- [line-chart.md](line-chart.md) — the same geometry with the value on the axis, and where the evidence is
- [slope-chart.md](slope-chart.md) — two periods, crossings still carrying the reordering, values kept
- [ranking.md](ranking.md) — the group, and why a rank is relative to its set
- [change-over-time.md](change-over-time.md) — the other group this belongs to, and its free parameters
- [../concepts/channels.md](../concepts/channels.md) — including why the accuracy ordering does not speak to reading an order
