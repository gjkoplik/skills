---
type: chart-type
relationships: [deviation]
aliases: [Diverging bar chart, Diverging stacked bar]
---

# Diverging bar charts

One bar per category running from a shared reference line, its length encoding the size of the deviation and the side it falls on encoding the sign.

**Two charts share the name and they are not the same object.** The first is the one above: one signed number per category, bars pointing both ways off a single line. The second is the **diverging stacked bar**, where each row's ordered categories accumulate outward from a center, the standard treatment for Likert data. They differ in one decomposition slot and they cost different things to read, so both are laid out separately below.

## When to reach for it, and when not

**The form applies where** every item has a meaningful signed distance from one reference the reader already accepts, and which side of the line an item lands on is part of the message. The reference is typically zero, and the FT names the two others explicitly: "Typically the reference point is zero but it can also be a target or a long-term average" ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)).

The **diverging stacked** variant applies where each row is a set of ordered response categories and the split between two opposed halves is what the reader is comparing across rows.

**Questions the form does not answer:**

| The question | Alternative |
|---|---|
| How big is each of these? | [Bar chart](bar-chart.md) from zero. A deviation chart has thrown the level away |
| Which is biggest, and in what order? | A sorted bar chart. Ranking |
| Everything is on one side of the line | A bar chart with the reference drawn as a rule. There is no sign to show |
| How did the gap move over time? | A line chart of the difference, with a rule at the reference. [Change over time](change-over-time.md) |
| Each row splits one total into two parts | [Spine chart](spine-chart.md), which is the paired form and not this one |
| How do the exact percentages compare? | A table. The outer segments of a diverging stack are the worst-read part of the chart |

## Structural decomposition

The signed form:

| Slot | |
|---|---|
| Data | One row per category, with a value and a reference |
| Transform | Subtract the reference. The plotted quantity is a difference, not a level |
| Geometry | Filled rectangle, one edge on the reference line |
| Scale | Signed difference to length, anchored at the reference, which is the zero of the transformed quantity |
| Coordinates | Cartesian |
| Guides | The reference line, labeled with its value and with what it is; one quantitative axis in difference units; a category axis |

**This is a [bar chart](bar-chart.md) with a subtraction added to the transform slot.** Nothing else changes, which is why this page inherits rather than restates: everything on the bar chart page carries over, including the zero baseline, because the zero of a difference *is* the reference line. A diverging bar that starts somewhere other than its reference is a truncated bar chart, and that is the defect [Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) measured at a 91.0% inflation of size judgments.

The diverging stacked form differs in two slots:

| Slot | |
|---|---|
| Data | One row per category, with a magnitude for each of several ordered response levels |
| Transform | Cumulative sum **outward in both directions from a center**, optionally normalized per row first |
| Geometry | Rectangle, as above |
| Scale | Segment magnitude to length |
| Coordinates | Cartesian |
| Guides | Reference line at the center, legend, and a stated rule for what was done with any neutral category |

**That is a [stacked bar](stacked-bar.md) with two accumulation directions instead of one**, and it inherits the cost named there: only the segments touching the center start at a shared line, and every segment outside them floats at a different offset per row. [Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md) measured that substitution directly on divided bars, "the average errors for length judgments are 40%-250% larger than those for position judgments." The measurement is on the divided bar; the step to this variant is structural, since splitting the accumulation into two directions changes how many segments sit on the shared line and not what happens to the ones that do not.

**Where the neutral category goes is a decision the form forces.** A midpoint response has no side. Splitting it across the center, pushing it entirely to one side, breaking it out into a separate column, and dropping it are four different charts of one dataset. No source in this corpus rules between them, and the chart itself does not show which was done.

## Channels

**Length from a shared reference line**, which for items on the same side of it is a reading of position along a common scale, inherited from [channels.md](../concepts/channels.md) with the usual caveat that the mapping from chart to channel is conjecture rather than measurement.

**Comparing across the line is a different judgment and an untested one.** Two bars pointing in opposite directions from a common origin are not two bars from a common baseline, and no study in this corpus measures that comparison. `absence of evidence`. It is also the comparison this chart is usually drawn to invite.

**The sign rides on direction**, doubled in hue almost always. Neither of those is a magnitude channel; the accuracy ordering scores nothing of the kind ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)). Hue used to mark which side an item is on is hue doing identity work, which is what it is good at.

## What it is measurably good at

**Nothing. No study in this corpus tests a diverging bar chart, in either form.**

What it can inherit is one link deep: the bar ends read as position along a common scale for same-side comparisons ([bar-chart.md](bar-chart.md)), and that is the best-measured channel there is. The inheritance is the whole of the case.

## What it is measurably bad at

Nothing measured on this form. Two inherited exposures, named separately because they are usually collapsed into each other:

**Floating segments, in the stacked variant.** Inherited from [stacked-bar.md](stacked-bar.md) and measured on the divided bar: 40% to 250% more error than position. It applies to every segment not touching the center.

**The baseline is a free parameter, and it is one level up from truncation.** Truncation, which moves the origin while the axis stays in raw units, is measured and harmful ([Pandey et al. 2015](../studies/pandey-2015-deceptive-visualizations.md); [Correll et al. 2020](../studies/correll-2020-truncating-the-y-axis.md)). This chart does not do that: it redefines the quantity as a difference, and the ink stays proportional to the difference, which is why that transform is recommended as the *remedy* for a truncation temptation ([urban-institute.md](../sources/urban-institute.md)). The exposure it has instead is the choice of reference, which nobody has tested. The argument is on [deviation.md](deviation.md) and it is the reason that index exists.

## What is contested

Nothing. There is no record here to disagree with itself.

The nearest thing to a disagreement is filing rather than evidence: the FT calls this a Deviation chart and Schwabish files Diverging Bar under Comparing Categories, his scheme having no Deviation category at all ([schwabish.md](../sources/schwabish.md), memberships verified from the contents pages). Two taxonomies, no experiment on either side.

## The failure mode it invites

**Picking the reference that produces the picture.** Zero, the target and the long-run average are three different charts of one dataset and they can disagree about who is failing. Follows from the structure, and what it does to readers is unmeasured. See [deviation.md](deviation.md).

**Inviting the cross-line comparison and then claiming accuracy for it.** The form makes "how much worse is this one than that one" look like a length comparison the reader can do. On the same side of the line it inherits the position reading. Across it, nobody knows. `absence of evidence`.

**Letting the neutral category disappear.** In the stacked variant, silently splitting or dropping the midpoint changes the apparent balance of every row and leaves no trace on the chart. Structural, and unaddressed by any source here.

**Reading the deviation as a level.** The base is off the chart entirely, so +9 could be a doubling or a rounding error, and the form offers no cue that the question exists.

## Justifying the choice

**Defensible, evidence-backed:**

- "I plotted the difference from the target rather than truncating the axis under a plain bar. Truncation inflated size judgments 91% in a controlled test, and this keeps the ink proportional to the quantity actually drawn."
- "Bars run from the reference line, so within each side their ends read as position along a common scale." Inherited from the bar chart, and the step from chart to channel is conjecture there too.
- "The response categories accumulate outward from the center, so only the two innermost segments sit on a shared line. The outer ones are read as floating lengths, which measured 40% to 250% worse on divided bars, and that is why the exact figures are in the table below the chart."

**Defensible, with the label said out loud:**

- "The reference is the 2015-2019 average, and the subtitle says so." That the reader could not otherwise recover the choice follows from the structure; that saying it helps is convention with nothing measured behind it.
- "Above and below differ in color as well as in direction." Redundant coding, [inventory](../inventory.md) topic 69, `authority-asserted`.
- "The neutral responses are drawn as their own centered block rather than split." A defensible choice among four, none of them tested.

**Commonly repeated, and the evidence does not support it:**

- ~~"A diverging bar shows deviations accurately."~~ It shows the sign by construction and it inherits a good channel within each side. Nobody has measured what a reader takes off one, and the cross-line comparison it advertises is untested.
- ~~"A diverging stacked bar is the standard for Likert data, so it is the right choice."~~ Ubiquity is not evidence. No study in this corpus compares it against grouped bars, against small multiples, or against plotting a single net score. `absence of evidence`.
- ~~"The reference point is just the axis, it carries no argument."~~ Change it and bars change side while the data stands still.

## See also

- [bar-chart.md](bar-chart.md) — this chart minus the subtraction, and where its evidence comes from
- [stacked-bar.md](stacked-bar.md) — the stacked variant's baseline problem, measured
- [spine-chart.md](spine-chart.md) — the paired form, where two components split a total rather than one value taking a sign
- [deviation.md](deviation.md) — the group, and the argument about the reference point
- [../concepts/channels.md](../concepts/channels.md)
