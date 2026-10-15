---
type: chart-type
relationships: [ranking, change-over-time]
aliases: [Bump chart]
---

# Bump charts

One line per item across several periods, with the vertical axis carrying position in the ordering rather than the value, so the crossings are the reorderings.

## When to reach for it, and when not

The form is defined for several periods, few enough items to label at the ends, and the question of who overtook whom. It is filed under [ranking](ranking.md) and [change-over-time](change-over-time.md), and the rank axis is both its offer and its cost.

| The question | Alternative |
|---|---|
| How much did each one change? | [Line chart](line-chart.md). The rank axis has thrown the amount away |
| There are exactly two periods | [Slope chart](slope-chart.md). Same crossings, and it keeps the values |
| How big is each item now? | [Magnitude](magnitude.md): a sorted [bar chart](bar-chart.md) |
| Is one item's trend accelerating or plateauing? | [Line chart](line-chart.md), which keeps the value |
| Which items are close together and which are far apart? | The values, drawn |
| There are fifty items | Aggregation, faceting, or a drawn subset |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per item per period, with a value |
| Transform | **Rank within each period.** The only slot doing work, and the value does not survive it |
| Geometry | One line per item across the periods, usually with a marker at each period |
| Scale | Rank to position on a common vertical scale, usually inverted so first place is on top |
| Coordinates | Cartesian, with x taking one position per period |
| Guides | A rank axis or per-period rank labels, direct item labels at one or both ends, and highlighting for the items to follow |

It is a [line chart](line-chart.md) with a rank transform in front, and two definitional consequences follow. Line spacing reflects the item count, not the data, so a crossing can be a reordering of any size, including a rounding error, and distant lines may differ by a hair. And the vertical range is fixed from first place to last, so there is nothing to truncate. The aspect ratio and the choice of periods stay free.

## Channels

Rank sits on position along a common scale ([channels.md](../concepts/channels.md)), a mapping that is conjecture. The accuracy ordering measures reading a *value* off a mark, and here the value has become an ordinal, which nobody has measured anyone reading ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)).

Movement is on direction and slope. Cleveland & McGill could not separate slope from angle, in an ordering they called a tentative working hypothesis ([channels.md](../concepts/channels.md)). Slope here is places per period, not units per period as on a [line chart](line-chart.md).

## What it is measurably good at

No study in this corpus tests the form, and unlike a [line chart](line-chart.md) it cannot borrow the position result, since its axis holds ranks.

## What it is measurably bad at

Nothing measured. Whether readers take a crossing for a large change is untested. `absence of evidence`.

Lines tangle at many items, with no measured threshold. Schwabish's guideline is "Avoid the Spaghetti Chart" ([schwabish.md](../sources/schwabish.md)). `authority-asserted`.

## What is contested

Nothing contested in this corpus.

## The failure mode it invites

**Presenting a reordering as a change.** The recorded remedy puts the amount back within reach: end labels, a companion panel of values, or a caption saying how close the ranks were. `authority-asserted`.

**Letting the item set do the work.** Adding or dropping one item moves every rank below it, so charts built from different sets are not comparable ([ranking.md](ranking.md)).

**Cherry-picking the first and last period.** A bump chart whose story is all in its endpoints should have been a [slope chart](slope-chart.md), which keeps the values.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing, not even the usual channel inheritance, which the rank transform breaks.

**Defensible, with the label said out loud:**

- "A bump chart, because the question is who overtook whom across six seasons and the amounts are not the message. Practitioner convention; nothing in this corpus tests the form."
- "Eight items rather than thirty, because the lines tangle. No measured threshold exists; the guideline is one practitioner's, stated for line charts generally."
- "The two teams in question are in color and the rest are gray. Widely recommended, never measured ([refutations.md](../refutations.md#gray-plus-one-accent-as-an-evidence-backed-rule))."
- "The values are printed at both ends, because the rank axis does not carry them. That follows from the transform, and whether it helps a reader is untested."

**Commonly repeated, and the evidence does not support it:**

- ~~"A bump chart shows the change clearly."~~ It shows the ordering. The size of the change is what the transform deleted.
- ~~"Lines crossing means the two swapped in a meaningful way."~~ They swapped. By how much cannot be recovered from the chart.
- ~~"It is a line chart, so the line-chart evidence carries over."~~ That evidence is about reading values off position, and this chart has none.

## See also

- [line-chart.md](line-chart.md): the same geometry with values, and the evidence
- [slope-chart.md](slope-chart.md): two periods, with values kept
- [ranking.md](ranking.md): the group, and why a rank is relative to its set
- [change-over-time.md](change-over-time.md): the other group's free parameters
- [../concepts/channels.md](../concepts/channels.md): why the accuracy ordering does not speak to reading an order
