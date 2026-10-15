---
type: chart-type
relationships: [ranking, change-over-time]
aliases: [Barbell chart, Connected dot plot, DNA chart, Dumbbell plot, Gap chart, Paired dot plot, Range plot]
---

# Dumbbell plots

One row per category, two dots on a single shared quantitative axis carrying that category's two values, joined by a segment whose length is the gap between them.

It is also called a dumbbell chart, barbell chart, DNA chart, connected dot plot or paired dot plot, and a range plot or gap chart when the dots mark the ends of a span. No source here defines these names. [Datawrapper](../sources/datawrapper-academy.md) says "range plot" for exactly this form, in passing, while explaining why it needs no zero baseline, "Readers don't expect dot plots (or, for two values, range plots) to start at zero because there's no filled bar or column that would indicate that." "Range plot" also names an uncertainty interval around an estimate, a collision the corpus does not resolve. Neither Schwabish nor the FT glosses quoted here give the form an entry. Schwabish files Paired Bar and Dot Plot under Comparing Categories ([schwabish.md](../sources/schwabish.md); contents pages only, prose unread).

## When to reach for it, and when not

The form is defined for categories carrying exactly two values of the same quantity (two periods, groups or conditions), where both the levels and the gap are the message. With two dates it is also a change-over-time chart. When one value is a reference rather than a measurement, it sits next to [deviation](deviation.md). It is indexed under [ranking](ranking.md) because the rows are usually sorted.

| The question | Alternative |
|---|---|
| Only the size of the gap matters, not where each item sits | A sorted bar chart of the differences: the gap on position from a shared zero, the levels dropped ([deviation](deviation.md)'s trade) |
| Which items changed places between the two periods? | [Slope chart](slope-chart.md). Crossings are drawn there and cannot be drawn here |
| What happened between the two dates? | [Line chart](line-chart.md). Two points assert nothing about the path |
| Where does each item sit in the order across six periods? | [Bump chart](bump-chart.md) |
| One value per category | [Bar chart](bar-chart.md), or a [lollipop chart](lollipop-chart.md) once filled bars become a block of ink |
| The second mark is an interval around an estimate, not a second measurement | Not this form. Uncertainty drawn and labeled as uncertainty. Expert readers misread error bars badly ([belia-2005-ci-misconceptions.md](../studies/belia-2005-ci-misconceptions.md)) |
| What are the exact values? | A table, or direct labels on both dots |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per category, carrying two values of the same quantity |
| Transform | None. The gap is drawn, not computed. The sort is an input |
| Geometry | Two points per row, plus a segment joining them |
| Scale | Both values to position on one quantitative axis shared by every row |
| Coordinates | Cartesian, with one categorical position per row |
| Guides | The quantitative axis, category labels, and something saying which dot is which: a legend, direct labels, or an arrowhead on the segment |

It is a [lollipop chart](lollipop-chart.md) with a second dot, where the stem spans the gap and carries the quantity of interest instead of running to the baseline. Unlike a [slope chart](slope-chart.md), it gives each category its own row, so nothing crosses. Reorderings are invisible, but labels stay separable at counts where a slope chart tangles.

## Channels

Both endpoints are position along a common scale, the most accurately read channel in [channels.md](../concepts/channels.md). The gap is a length with no common baseline, because each row's segment starts wherever that row's first value sits. So the levels sit on the best-measured channel and the quantity that usually motivated the chart sits on a worse one. [Waterfall](waterfall-chart.md) and [stacked bar](stacked-bar.md) charts make the same split.

Whether readers misjudge the gaps on this form is unmeasured. The floating-length penalty was measured on divided bars, not dumbbells. `absence of evidence`. The step from mark to channel is conjecture in the source literature, as it is for every chart type.

Rows picked out by color use hue for identity, a job hue does well and no accuracy ordering scores.

## What it is measurably good at

No study in this corpus tests the form. Two nearby results do not transfer. [Correll & Gleicher (2014)](../studies/correll-gleicher-2014-error-bars-harmful.md) note in an aside that "comparing ratios can be done quickly and more accurately with bar charts as compared to dot plots", a different task on a different form. [Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) measured axis truncation on filled bars, not on a pair of dots.

## What it is measurably bad at

Nothing measured. Besides the floating gaps, row count sets the height. Datawrapper documents that dot plots, range plots and arrow plots cannot have their height set ([datawrapper-academy.md](../sources/datawrapper-academy.md)), so, as with a bar chart, forty categories do not fit on a phone by resizing ([magnitude.md](magnitude.md)).

## What is contested

Nothing contested in this corpus. The inherited contest is the zero baseline, `authority-asserted` on both sides. Datawrapper releases it for dot and range plots and lists plotting the differences as one of three replacements for a truncated axis, a row [slope-chart.md](slope-chart.md) also carries. The FT scopes the rule by mark. The Urban Institute releases marks that "do not use length or height as the primary encoding" ([urban-institute.md](../sources/urban-institute.md)). [Vega-Lite](../sources/vega-lite.md) forces zero on every quantitative positional scale regardless of mark.

With no stem back to the axis, the lollipop's bar-like exposure is absent. The segment's ink is still proportional to the gap, so proportional ink applies from a nonzero origin.

## The failure mode it invites

**Gaps compared across rows as though they were bars.** Each segment starts somewhere different. `authority-asserted`, from the structure rather than a study.

**No key to which dot is which.** Dots at 40 and 60 do not say which year, 2010 or 2024, each marks. Without a legend, direct labels on the top row, or an arrowhead, the chart is unreadable.

**An unstated sort.** First value, second value and gap give three different charts of the same data. That is one more sort key than most of [its group](ranking.md), so the caption says more.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing on this page qualifies. The inherited sentence, "each dot is position along a common scale, the most accurately read channel measured", covers the endpoints and not the gap.

**Defensible, with the label said out loud:**

- "Both the levels and the change matter, so both are on the chart. The levels are on position and the gap is on an unanchored length, and that is the trade this form makes."
- "Thirty categories over two periods, so one row each rather than a slope chart. A legibility judgment about label collisions, with no study here on either form."
- "The axis does not start at zero, because nothing on the chart is a filled bar. A newsroom taxonomy, a chart tool and a style guide scope the rule that way, none of them tested it, and one plotting library disagrees outright."
- "Sorted by gap rather than by the later value, and the caption says so."

**Commonly repeated, and the evidence does not support it:**

- ~~"A dumbbell shows the change more accurately than two bars."~~ Unmeasured, and the form puts the change on the worse of its two channels.
- ~~"The longer segment is the bigger change, so readers can rank the changes off the chart."~~ The first half is definitional. Ranking floating lengths is untested here, and the one measurement of that penalty used a different stimulus.
- ~~"It is a slope chart with the periods side by side."~~ A slope chart draws the reordering. This form cannot.

## See also

- [lollipop-chart.md](lollipop-chart.md): one dot with a stem, and the zero-baseline argument
- [slope-chart.md](slope-chart.md): the other two-value form, which shows reorderings
- [ranking.md](ranking.md): the group and its free parameters
- [dot-strip-plot.md](dot-strip-plot.md): many items on one axis, one value each
- [../concepts/channels.md](../concepts/channels.md): the inherited channel evidence
