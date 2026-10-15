---
type: chart-type
relationships: [flow]
aliases: [Waterfall chart]
---

# Waterfall charts

A running total drawn as a sequence of floating bars, each bar's length encoding one step's signed contribution and each bar's ends sitting at the running total before and after that step.

## When to reach for it, and when not

The form is defined for one total moving to another through an ordered sequence of increases and decreases, where both the steps and the end point are the message.

| The question | Alternative |
|---|---|
| How does this total break down, with no sequence in it? | [Stacked bar](stacked-bar.md) or [treemap](treemap.md), and see [part-to-whole.md](part-to-whole.md) |
| Which contribution is biggest? | A sorted [bar chart](bar-chart.md) of the contributions. Ranking, not flow |
| How did the total move across many periods? | [Line chart](line-chart.md), and see [change-over-time.md](change-over-time.md) |
| Where did the quantity go, across states? | [Sankey diagram](sankey-diagram.md). A waterfall has one running total, not a set of destinations |
| How far is each item from a reference? | [Deviation](deviation.md). A [diverging bar chart](diverging-bar-chart.md) |
| What are the exact contributions? | A table, or direct labels. There is no common baseline to read most bars against |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per step, with a signed magnitude, plus an opening total and usually a closing one |
| Transform | Cumulative sum, giving each bar a start and an end. The step order is an input, not a computation |
| Geometry | Rectangle per step, plus connectors between consecutive bars. Opening and closing totals drawn as bars from the axis |
| Scale | Signed magnitude to bar length; running total to the position of both bar ends |
| Coordinates | Cartesian |
| Guides | One quantitative axis including zero, a category axis of steps, color for sign, usually direct labels |

It is a [stacked bar](stacked-bar.md) taken apart along an axis of steps, each segment given its own category position and connectors. Its evidence is inherited from that form.

## Channels

The running total at each bar's ends is position along a common scale, and each step is a length with no common baseline. Hue marks the sign, which is identity, not magnitude ([channels.md](../concepts/channels.md)). Only the opening total and any drawn subtotals or closing total touch the axis, so almost every bar floats. [stacked-bar.md](stacked-bar.md) makes the same split, with the trajectory on position and the increments on floating length.

Whether readers misjudge the steps is unmeasured. The floating-segment penalty, "the average errors for length judgments are 40%-250% larger than those for position judgments," was measured on divided bars ([Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md)), not on segments pulled into their own columns.

## What it is measurably good at

No study in this corpus tests a waterfall chart, or compares it with the divided bar it is built from.

## What it is measurably bad at

Nothing measured. The floating bars are an inherited exposure.

## What is contested

Nothing empirical. Only the filing differs. The FT puts it under both Part-to-whole and Flow, [Schwabish](../sources/schwabish.md) under Comparing Categories, and [Datawrapper](../sources/datawrapper-academy.md) gives "Dual-axis & Waterfall Charts" a top-level slot in its Academy with a walkthrough article. That shows a major vendor ships the type, not how it reads.

## The failure mode it invites

**A sequence presented as a finding.** The connectors assert an order that is often an accounting convention, such as revenue before costs, rather than a fact. Reordering reshapes the descent, and the figure does not record the choice. This is [change-over-time](change-over-time.md)'s free-parameter problem, disguised as arithmetic. `authority-asserted`, from the structure. Whether readers infer chronology or causation from the connectors is untested.

**Steps that are themselves nets.** A "pricing" bar that nets increases against decreases hides a decomposition. More steps fix that and add floating lengths.

**Comparing two waterfalls.** Different steps and orderings put every intermediate bar at a different offset, so only the opening and closing totals compare, as with two pies ([part-to-whole.md](part-to-whole.md)).

## Justifying the choice

**Defensible, evidence-backed:**

Nothing native. One channel claim is inheritable:

- "Each step is labeled, because only the opening and closing bars touch the axis and everything between them is a floating length judgment" ([channels.md](../concepts/channels.md), [stacked-bar.md](stacked-bar.md)).

**Defensible, with the label said out loud:**

- "The reader needs both the steps and the end point, which is why this is not a sorted bar chart of the contributions." Structural, untested.
- "The steps are in reporting order, not chronological order, and the subtitle says so."
- "Increases and decreases are colored by sign, which is hue carrying identity rather than magnitude."

**Commonly repeated, and the evidence does not support it:**

- ~~"A waterfall shows what drove the change."~~ It shows one ordered decomposition of a difference, and the factors and their order are the analyst's model.
- ~~"The connectors show how one step led to the next."~~ They show a running total's arithmetic in the order supplied.
- ~~"Pulling the segments apart makes them easier to read than a stacked bar."~~ Untested. Both leave every intermediate quantity floating.

## See also

- [flow.md](flow.md): the group, and its two tests, one of which this form barely passes
- [stacked-bar.md](stacked-bar.md): the same cumulative-sum transform, and the floating-segment evidence
- [part-to-whole.md](part-to-whole.md): the other group this decomposition belongs to
- [change-over-time.md](change-over-time.md): the free-parameter problem, where it is expected
- [../concepts/channels.md](../concepts/channels.md)
