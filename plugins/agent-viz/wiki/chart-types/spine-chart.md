---
type: chart-type
relationships: [deviation]
aliases: [Population pyramid, Spine chart]
---

# Spine charts

One row per category, each row's total split into two contrasting components that run in opposite directions from a shared central line.

That definition is this page's stipulation. No source here defines the term, including the glosses quoted on [ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md), and the field uses it inconsistently.

The population pyramid, with age bands as rows and men and women as components, has a primary definition. [Wilke](../sources/wilke-fundamentals.md) builds it as an age pyramid: "we can also make two separate histograms, rotate them by 90 degrees, and have the bars in one histogram point into the opposite direction of the other." As two mirrored histograms it is also a distribution chart, which is where [Schwabish](../sources/schwabish.md) files Pyramid.

## When to reach for it, and when not

The form is defined for rows that are each one total split in two, where the split is the message and the two parts are opposed in kind rather than ordered.

| The question | Alternative |
|---|---|
| How big is each row's total? | [Stacked bar](stacked-bar.md) or [bar chart](bar-chart.md). This form makes the total hard to read |
| One signed number per row, above or below a reference | [Diverging bar chart](diverging-bar-chart.md) |
| Three or more components per row | [Stacked bar](stacked-bar.md), or the diverging stacked bar on [diverging-bar-chart.md](diverging-bar-chart.md) |
| How does one component compare across rows? | A sorted [bar chart](bar-chart.md) of that component alone |
| Do the parts exhaust the total, and is that the claim? | [Part-to-whole](part-to-whole.md). This form asserts no whole |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per category, with exactly two component magnitudes |
| Transform | None, or normalize each row to shares. No cumulative sum |
| Geometry | Two filled rectangles per row, meeting at the center line |
| Scale | Component magnitude to length, both anchored at the center, one running each way |
| Coordinates | Cartesian, usually with the category axis vertical |
| Guides | The center line, labels or a legend naming the components, and one axis with unsigned values on both sides |

It is a two-segment [stacked bar](stacked-bar.md) hinged at the segment boundary. Both components now sit on a shared line, so neither floats. The row total stops being a position reading and becomes two opposite lengths added across the center by eye. The second component's baseline is bought with the total. Normalizing to shares makes ratios comparable across rows and removes the totals, as on a stacked bar.

## Channels

Length from a shared center line, twice per row. Within one side that is position along a common scale ([channels.md](../concepts/channels.md)), with the step from chart to channel conjecture rather than measurement.

The comparison the chart is built for, A against B in one row, crosses the line. Two lengths running opposite ways from one origin are not two bars off a common baseline, and nothing here measures that judgment. `absence of evidence`.

Side, doubled in hue, marks which component is which. The accuracy ordering scores neither ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)).

## What is measured

No study in this corpus tests the form.

## The failure mode it invites

**Reading the outer edges as a total.** The row's overall span is its total, but it is a floating length with no shared baseline, so it is the least legible quantity here.

**Normalizing silently.** Shares and counts produce similar pictures and answer different questions, and only a labeled axis says which.

Both follow from the structure and are untested on readers. `absence of evidence`.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing beyond the same-side position reading every bar chart has ([bar-chart.md](bar-chart.md), [channels.md](../concepts/channels.md)).

**Defensible, with the label said out loud:**

- "Both components run off one center line, so neither is the floating segment a stacked bar would have made it." That follows from the geometry. What a reader gets from it is untested.
- "Rows are counts rather than shares, and the axis says so, because the size of each band is part of the point."
- "Two components only. Anything more goes back to a stacked form." Convention, with no measured threshold.

**Commonly repeated, and the evidence does not support it:**

- ~~"A spine chart shows the balance between the two groups accurately."~~ It shows which side is longer, by construction. The gap is a cross-center comparison nobody here has measured.
- ~~"It is just a bar chart mirrored, so the bar chart evidence applies."~~ It applies to each side, not to the comparison the form exists for.

## See also

- [diverging-bar-chart.md](diverging-bar-chart.md): one signed number per row
- [stacked-bar.md](stacked-bar.md): the form this one hinges, and the measured baseline result
- [deviation.md](deviation.md): the group
- [../concepts/channels.md](../concepts/channels.md)
