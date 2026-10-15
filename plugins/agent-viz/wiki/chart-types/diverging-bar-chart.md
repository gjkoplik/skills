---
type: chart-type
relationships: [deviation]
aliases: [Diverging bar chart, Diverging stacked bar]
---

# Diverging bar charts

One bar per category running from a shared reference line, its length encoding the size of the deviation and its side encoding the sign.

The **diverging stacked bar** shares the name: each row's ordered categories accumulate outward from a center, the standard treatment for Likert data.

## When to reach for it, and when not

The signed form is defined for items with a signed distance from a reference the reader accepts, where the side of the line is part of the message. The FT: "Typically the reference point is zero but it can also be a target or a long-term average" ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). The stacked form is defined for rows of ordered response categories, where the split between two opposed halves is compared across rows.

| The question | Alternative |
|---|---|
| How big is each of these? | [Bar chart](bar-chart.md) from zero. A deviation chart has thrown the level away |
| Which is biggest, and in what order? | A sorted bar chart |
| Everything is on one side of the line | A bar chart with the reference drawn as a rule |
| How did the gap move over time? | A line chart of the difference, with a rule at the reference ([change over time](change-over-time.md)) |
| Each row splits one total into two parts | [Spine chart](spine-chart.md), the paired form |
| How do the exact percentages compare? | A table. The outer segments of a diverging stack are the worst-read part |

## Structural decomposition

| Slot | Signed | Stacked |
|---|---|---|
| Data | One row per category, a value and a reference | One row per category, a magnitude per ordered response level |
| Transform | Subtract the reference. The plotted quantity is a difference, not a level | Cumulative sum outward in both directions from a center, optionally normalized per row |
| Geometry | Filled rectangle, one edge on the reference line | Rectangle |
| Scale | Signed difference to length, anchored at the reference, the zero of the transformed quantity | Segment magnitude to length |
| Coordinates | Cartesian | Cartesian |
| Guides | The reference line labeled with its value and what it is; an axis in difference units; a category axis | Reference line at the center, legend, and a stated rule for any neutral category |

The signed form is a [bar chart](bar-chart.md) with a subtraction, and inherits its zero baseline, because the zero of a difference *is* the reference line. A diverging bar starting anywhere else is truncated, the defect [Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) measured at a 91.0% inflation of size judgments.

The stacked form is a [stacked bar](stacked-bar.md) accumulating two ways, so only the segments touching the center share a line. On divided bars, [Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md) found "the average errors for length judgments are 40%-250% larger than those for position judgments." The step to this variant is structural.

The neutral category has no side. Splitting it, pushing it to one side, breaking it out, and dropping it are four charts of one dataset, and no source here rules between them.

## Channels

Same-side bars read as position along a common scale ([channels.md](../concepts/channels.md)), with the step from chart to channel conjecture. Bars pointing opposite ways share no baseline, and no study in this corpus measures that cross-line comparison, the one the chart usually invites. `absence of evidence`. The sign rides on direction, usually doubled in hue, which the accuracy ordering does not score ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)). Hue there does identity work, its strength.

## What it is measurably good at

No study in this corpus tests the form, in either variant. The case rests on same-side bar ends inheriting position from [bar-chart.md](bar-chart.md).

## What it is measurably bad at

Nothing measured on this form. The stacked form's off-center segments are floating lengths, 40% to 250% worse on divided bars. Truncation is measured and harmful ([Pandey et al. 2015](../studies/pandey-2015-deceptive-visualizations.md); [Correll et al. 2020](../studies/correll-2020-truncating-the-y-axis.md)). The signed form does not truncate. It redefines the quantity as a difference with proportional ink, the transform recommended as truncation's remedy ([urban-institute.md](../sources/urban-institute.md)). Its exposure is the untested choice of reference ([deviation.md](deviation.md)).

## What is contested

Nothing contested in this corpus. Filing differs: the FT calls it a Deviation chart, and Schwabish, who has no Deviation category, files Diverging Bar under Comparing Categories ([schwabish.md](../sources/schwabish.md), from the contents pages).

## The failure mode it invites

**Picking the reference that produces the picture.** Zero, the target and the long-run average can disagree about who is failing.

**Claiming accuracy across the line.** The form makes "how much worse is this one than that one" look like a length comparison, which is untested. `absence of evidence`.

**A vanishing neutral category.** Silently splitting or dropping the midpoint shifts every row's balance, and the chart does not show it.

**Reading the deviation as a level.** The base is off the chart, so +9 could be a doubling or a rounding error.

## Justifying the choice

**Defensible, evidence-backed:**

- "I plotted the difference from the target rather than truncating the axis under a plain bar. Truncation inflated size judgments 91% in a controlled test, and this keeps the ink proportional to the quantity actually drawn."
- "Bars run from the reference line, so within each side their ends read as position along a common scale." Inherited from the bar chart.
- "The response categories accumulate outward from the center, so only the two innermost segments sit on a shared line. The outer ones are read as floating lengths, which measured 40% to 250% worse on divided bars, and that is why the exact figures are in the table below the chart."

**Defensible, with the label said out loud:**

- "The reference is the 2015-2019 average, and the subtitle says so." Stating it is convention, untested.
- "Above and below differ in color as well as in direction." Redundant coding, [inventory](../inventory.md) topic 69, `authority-asserted`.
- "The neutral responses are drawn as their own centered block rather than split." One of four untested options.

**Commonly repeated, and the evidence does not support it:**

- ~~"A diverging bar shows deviations accurately."~~ It shows the sign by construction. Reading accuracy is unmeasured.
- ~~"A diverging stacked bar is the standard for Likert data, so it is the right choice."~~ No study in this corpus compares it against grouped bars, small multiples or a single net score. `absence of evidence`.
- ~~"The reference point is just the axis, it carries no argument."~~ Change it and bars change side while the data stands still.

## See also

- [bar-chart.md](bar-chart.md): this chart minus the subtraction, and its evidence
- [stacked-bar.md](stacked-bar.md): the stacked variant's baseline problem, measured
- [spine-chart.md](spine-chart.md): the paired form, two components splitting a total
- [deviation.md](deviation.md): the group, and the argument about the reference point
- [../concepts/channels.md](../concepts/channels.md)
