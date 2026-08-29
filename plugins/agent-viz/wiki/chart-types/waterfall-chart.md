---
type: chart-type
relationships: [flow]
aliases: [Waterfall chart]
---

# Waterfall charts

A running total drawn as a sequence of floating bars, each bar's length encoding one step's signed contribution and each bar's ends sitting at the running total before and after that step.

## When to reach for it, and when not

The form is defined for the case where one total moves to another through an ordered sequence of increases and decreases, and both the individual steps and the end point are part of the message.

Questions the form does not answer:

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
| Transform | Cumulative sum, giving each bar a start and an end. **The step order is an input, not a computation** |
| Geometry | Rectangle per step, plus connectors between consecutive bars. Opening and closing totals drawn as bars from the axis |
| Scale | Signed magnitude to bar length; running total to the position of both bar ends |
| Coordinates | Cartesian |
| Guides | One quantitative axis including zero, a category axis of steps, color for sign, usually direct labels |

**This is a [stacked bar](stacked-bar.md) taken apart along an axis of steps.** Same cumulative-sum transform, same rectangles at the same offsets; the segments have been given their own category positions and connectors instead of sharing one bar. That is the whole difference, and the evidence here is inherited from that form rather than native.

## What it costs, and it is definitional

**Almost every bar floats.** Only the opening total and any explicitly drawn subtotals or closing total start at the axis, so only those are read as position along a common scale. Every step in between is a length with no common baseline. That statement is about what the chart *is*, and it is secure.

What it does not license is a conclusion about readers. The floating-segment penalty is measured at the channel level, on divided bars, in [Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md): "the average errors for length judgments are 40%-250% larger than those for position judgments" ([stacked-bar.md](stacked-bar.md)). **That was not measured on a waterfall**, and separating the segments into their own columns changes the stimulus in ways nobody has tested. It stands as an exposure, not as a result about this chart.

One reading does survive on the good channel: **each bar's upper and lower edge sits at a running total on the shared axis**, so the level at every point in the sequence is a position reading. The waterfall puts the trajectory on position and the increments on floating length, which is the same split [stacked-bar.md](stacked-bar.md) has.

## The connectors assert a sequence, and the sequence is a choice

The horizontal connectors say these steps happened in this order. Frequently the order is an accounting convention the analyst picked, not a fact about the world: revenue before costs, fixed before variable, one segment before another. Reordering the steps moves every intermediate bar and changes the shape of the descent completely, and nothing in the figure records that a choice was made.

This is [change-over-time](change-over-time.md)'s free-parameter problem in a group where it is less expected, because a waterfall looks like arithmetic rather than like a trend. Whether readers infer chronology or causation from the connectors is untested. That the picture depends on the order is definitional.

## Channels

**Position along a common scale** for the running total at each bar's ends, **length with no common baseline** for the step sizes themselves, and **hue** for the sign of the step, which is hue used for identity rather than for magnitude and is what hue is good at ([channels.md](../concepts/channels.md)).

Inherited, with the standing caveat that the mapping from this chart to those channels is conjecture rather than measurement.

## What it is measurably good at

**Nothing. No study in this corpus tests a waterfall chart.**

The closest measured stimulus is the divided bar chart behind the Cleveland & McGill judgment types, and the relationship is one of construction rather than of evidence: a waterfall is that chart with the segments pulled apart. Nobody has run the comparison.

## What it is measurably bad at

Nothing measured. The inherited exposure is the floating bars, above, and it is real.

## What is contested

Nothing empirical. There is no record here to disagree with itself.

The record disagrees only about filing: the FT puts it under both Part-to-whole and Flow, [Schwabish](../sources/schwabish.md) under Comparing Categories, and [Datawrapper](../sources/datawrapper-academy.md) gives "Dual-axis & Waterfall Charts" a top-level slot in its Academy navigation with a walkthrough article. That last is thin, and thin is all it is: it establishes that a major tool vendor ships the type, and nothing about how it reads.

## The failure mode it invites

**A sequence presented as a finding.** The order is an input, the connectors make it look given, and the reader has no way to see the alternative orderings. `authority-asserted`, and it follows from the structure.

**Steps that are themselves nets.** A bar labeled "pricing" that is a net of increases and decreases hides a decomposition inside a chart whose entire purpose is decomposition. The remedy is more steps, and more steps is where the floating-length reading gets worse.

**Comparing two waterfalls.** Different step sets and different orderings put every intermediate bar at a different offset, so nothing survives the comparison except the opening and closing totals. Same reason two pies do not compare ([part-to-whole.md](part-to-whole.md)).

## Justifying the choice

**Defensible, evidence-backed:**

Nothing is native to this form. The inheritable sentence is a channel claim:

- "Each step is labeled, because only the opening and closing bars touch the axis and everything between them is a floating length judgment" ([channels.md](../concepts/channels.md), [stacked-bar.md](stacked-bar.md)).

**Defensible, with the label said out loud:**

- "The reader needs both the steps and the end point, which is why this is not a sorted bar chart of the contributions." Structural, untested.
- "The steps are in reporting order, not chronological order, and the subtitle says so."
- "Increases and decreases are colored by sign, which is hue carrying identity rather than magnitude."

**Commonly repeated, and the evidence does not support it:**

- ~~"A waterfall shows what drove the change."~~ It shows one ordered decomposition of a difference. Which factors appear, and in what order, is the analyst's model of the change rather than the chart's finding.
- ~~"The connectors show how one step led to the next."~~ They show the arithmetic of a running total in the order it was supplied.
- ~~"Pulling the segments apart makes them easier to read than a stacked bar."~~ Plausible, and nobody has tested it. Both forms leave every intermediate quantity floating.

## See also

- [flow.md](flow.md) — the group, and its two tests, one of which this form barely passes
- [stacked-bar.md](stacked-bar.md) — the same cumulative-sum transform, and where the floating-segment evidence actually is
- [part-to-whole.md](part-to-whole.md) — the group this form's decomposition also belongs to
- [change-over-time.md](change-over-time.md) — the free-parameter problem, in the group where it is expected
- [../concepts/channels.md](../concepts/channels.md)
