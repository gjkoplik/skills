---
type: chart-type
relationships: [part-to-whole, change-over-time, magnitude]
aliases: [100% stacked bar, Stacked bar chart, Stacked column]
---

# Stacked bar charts

A bar divided into segments, each segment's length encoding a part's share of the bar's total.

## When to reach for it, and when not

The form is defined for cases where the total matters as well as the composition, or where composition repeats across categories or time. It is the only part-to-whole form that keeps a position-along-a-common-scale reading, for the total and the bottom segment.

| The question | Alternative |
|---|---|
| How does one middle series move across categories? | Small multiples, or a line chart of that series. Middle segments float |
| Only composition matters, and there is one whole | [Pie or donut](pie-and-donut.md). Nothing is lost |
| There are many parts per bar | [Treemap](treemap.md), or aggregate the tail into "other" |
| Precise values per segment | Any chart with an axis per value. This is the form's measured weakness |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (category, part) with a magnitude |
| Transform | Cumulative sum within category to get segment boundaries. Optionally normalize to 100% |
| Geometry | Rectangle |
| Scale | Magnitude to length |
| Coordinates | Cartesian |
| Guides | One quantitative axis, category axis, legend |

A grouped bar chart differs in the transform slot alone: no cumulative sum, so each bar keeps its own baseline. A 100% stacked bar adds a normalization. Polar coordinates give a stacked polar-area chart, not a coxcomb, which is a plain [bar chart](bar-chart.md#structural-decomposition) in polar coordinates, with equal angles and the quantity in the radius.

## Channels

Segment length. The first segment starts at the axis and is read as position along a common scale. Every later segment floats and is read as length, a less accurately read channel ([channels.md](../concepts/channels.md)). Cleveland & McGill spell this out for the divided bar chart:

> "For each of the three, the totals of A and B can be compared by perceiving position along the scale. ... All other values must be compared by the elementary task of perceiving different bar lengths"

In a 100% stacked bar every bar ends at the same line, so the top segment also has a shared end line, and only the middle segments float. Normalizing removes the position reading of the total and keeps the bottom segment's.

## What is measured

Totals and the bottom segment are read well. Both are position along a common scale, the most accurately read channel measured, `evidence-backed`.

Every segment not on the baseline is read badly. [Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md) measured this substitution, `evidence-backed`:

> "the average errors for length judgments are 40%-250% larger than those for position judgments"

The experiment's five judgment types, built from grouped and divided bars, isolate it: types 1-3 are position readings and types 4-5 floating-segment lengths. [Heer & Bostock (2010)](../studies/heer-bostock-2010.md) replicated it, finding types 4 and 5 somewhat more accurate than the original but position still significantly ahead. The claim is measured on this form directly, not inherited.

Nothing contested in this corpus. No study here tests whether a stacked bar beats a grouped bar or small multiples for a given question.

## The failure mode it invites

**Tracking a middle series across categories.** Comparing the orange segment across five bars is a set of floating length judgments. `authority-asserted`, following from the measured channel split. The remedy is ordering, with the series in question on the baseline, which follows from the evidence and is not separately tested.

**100% stacking hides the totals.** Only composition is left.

## Justifying the choice

**Defensible, evidence-backed:**

- "I put the series in question on the baseline. Floating segments are read as length, which carries 40% to 250% more error than position, measured on exactly this chart form."
- "The total is read as position along a common scale here, which is why this is a stacked bar rather than a pie: the reader needs the total and its composition."
- "I did not normalize to 100%, because that removes the position reading of the totals, and the totals are part of the message."

**Defensible, with the label said out loud:**

- "Three or four segments is about the practical limit before the middle becomes unreadable. Convention, not a measured threshold."

**Commonly repeated, and the evidence does not support it:**

- ~~"Readers can compare the orange segments across these bars."~~ Not well. It is this form's measured weakness.

## See also

- [../studies/cleveland-mcgill-1984.md](../studies/cleveland-mcgill-1984.md): the divided-bar stimuli and the 40-250% figure
- [pie-and-donut.md](pie-and-donut.md): the same job in polar coordinates
- [../concepts/channels.md](../concepts/channels.md)
