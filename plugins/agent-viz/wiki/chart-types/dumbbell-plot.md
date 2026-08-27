---
type: chart-type
relationships: [ranking, change-over-time]
aliases: [Barbell chart, Connected dot plot, DNA chart, Dumbbell plot, Gap chart, Paired dot plot, Range plot]
---

# Dumbbell plots

One row per category, two dots on a single shared quantitative axis carrying that category's two values, joined by a segment whose length is the gap between them.

**Also called a dumbbell chart, a barbell chart, a DNA chart, a connected dot plot or a paired dot plot.** Where the two dots mark the ends of a span rather than two moments, the same drawing gets called a **range plot** or a **gap chart**. Those are the names in circulation; no source in this corpus defines any of them, and only one appears in a source here at all: [Datawrapper](../sources/datawrapper-academy.md) says "range plot" for exactly this form, in passing, while explaining why it needs no zero baseline, "Readers don't expect dot plots (or, for two values, range plots) to start at zero because there's no filled bar or column that would indicate that."

**One name collision, and this wiki cannot settle it.** "Range plot" is also used for an interval drawn around an estimate, which is a different claim entirely: an uncertainty interval says what is not known, and two dots on a dumbbell are two measurements. Nothing in this corpus defines the term, so treat it as ambiguous and say in the caption which one you drew.

**The taxonomies in this corpus do not name the form separately.** Schwabish files **Paired Bar** and **Dot Plot** under Comparing Categories and has no dumbbell entry ([schwabish.md](../sources/schwabish.md), memberships verified from the book's contents pages; his prose is unread and nothing here reports what he argues). The FT glosses quoted in this wiki do not include one either. Structurally it is a paired dot plot with the pair connected, and that is as far as the record here goes.

## When to reach for it, and when not

**Reach for it when** each category carries exactly two values of the same quantity (two periods, two groups, two conditions) and **both the levels and the gap are part of the message**. If only one of the two is the message there is a better chart in each direction: levels alone are a [bar chart](bar-chart.md) or a [lollipop chart](lollipop-chart.md), and the gap alone is a sorted bar chart of the differences.

Where the two values are two dates this is also a change-over-time chart, and where one of them is a reference rather than a measurement it sits next to [deviation](deviation.md). It is indexed under [ranking](ranking.md) because the usual reason to draw thirty of these rows is to sort them.

**Do not reach for it when:**

| The question | Use instead |
|---|---|
| Only the size of the gap matters, not where each item sits | A sorted bar chart of the differences, which puts the quantity you care about back on position from a shared zero. See below |
| Which items changed places between the two periods? | [Slope chart](slope-chart.md). Crossings are drawn there and are not drawable here |
| What happened between the two dates? | [Line chart](line-chart.md). Two points assert nothing about the path |
| Where does each item sit in the order across six periods? | [Bump chart](bump-chart.md) |
| One value per category | [Bar chart](bar-chart.md), or a [lollipop chart](lollipop-chart.md) once there are enough categories that filled bars become a block of ink |
| The second mark is an interval around an estimate, not a second measurement | Not this form. Draw it as uncertainty and label it as uncertainty; expert readers misread error bars badly ([belia-2005-ci-misconceptions.md](../studies/belia-2005-ci-misconceptions.md)) |
| What are the exact values? | A table, or direct labels on both dots |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per category, carrying two values of the same quantity |
| Transform | None. The gap is drawn rather than computed. The sort is an input |
| Geometry | Two points per row, plus a segment joining them |
| Scale | Both values to position on **one quantitative axis shared by every row** |
| Coordinates | Cartesian, with one categorical position per row |
| Guides | The quantitative axis, category labels, and something saying which dot is which: a legend, direct labels, or an arrowhead on the segment |

**It is a [lollipop chart](lollipop-chart.md) with a second dot, and the stem spanning the gap instead of running back to the baseline.** Lollipop's page names the same substitution from its side. The stem changes job in the swap: there it is a guide, here it is the mark carrying the quantity of interest.

**It is not a [slope chart](slope-chart.md), and they are not interchangeable.** A slope chart puts the two periods at two x positions and draws each category as a segment between them, so all the categories share both columns and crossings show the reorderings. A dumbbell gives each category its own row and lays its two values side by side on one shared axis, so nothing crosses and a reordering is invisible. The dumbbell keeps categories separable and labelable at counts where a slope chart becomes a tangle; the slope chart shows who overtook whom, which the dumbbell cannot show at all.

## Channels

**Both endpoints are position along a common scale**, inherited from [channels.md](../concepts/channels.md) with the standard caveat that the mapping from mark to channel is conjecture in the source literature.

**The gap is not.** The connecting segment is a **length with no common baseline**, because every row's segment starts wherever that category's first value happens to sit. So the form puts the levels on the best-measured channel and puts the quantity that usually motivated the chart on a worse one. That is definitional. The same split is on [waterfall-chart.md](waterfall-chart.md) and [stacked-bar.md](stacked-bar.md): levels on position, increments on floating length.

**What that does not license is a conclusion about readers.** Whether anyone misjudges the gaps on this form is unmeasured in this corpus. The floating-length penalty was measured on divided bars rather than on dumbbells ([channels.md](../concepts/channels.md)), so inherit it as an exposure and not as a result about this chart. `absence of evidence`.

Where one or two rows are picked out by color, that is hue used for identity, which is the job [channels.md](../concepts/channels.md) says hue is actually good at and which no accuracy ordering scores.

## If the gap is the whole message, plot the gap

This follows from the section above rather than from a study. A sorted bar chart of the differences puts the gap on position along a common scale from a shared zero, and sorts on the quantity of interest instead of on a proxy for it.

The cost is real: it throws the levels away. Two categories with a gap of four might be at 104 and 4004, and the difference chart cannot tell them apart, which is [deviation.md](deviation.md)'s standing trade. Reach for the dumbbell when you are unwilling to make it, not by default.

Datawrapper lists plotting the differences between the bars as one of its three replacements for a truncated axis, and [slope-chart.md](slope-chart.md) carries the same row ([datawrapper-academy.md](../sources/datawrapper-academy.md)). `authority-asserted` on both.

## What it is measurably good at

**Nothing. No study in this corpus tests a dumbbell plot.**

Two nearby results, neither transferring and both pointing away from the form. [Correll & Gleicher (2014)](../studies/correll-gleicher-2014-error-bars-harmful.md) note in passing that "comparing ratios can be done quickly and more accurately with bar charts as compared to dot plots", which is a different task on a different form and an aside in a paper about something else. [Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) measured what truncating an axis does to size judgments on **filled bars**, and nobody has pointed that question at a pair of dots.

## What it is measurably bad at

Nothing measured. Two exposures worth naming, both structural.

**The gaps float**, per the channels section, so reading one row's gap against another's is the floating-length judgment rather than the position judgment the endpoints get.

**Row count is a hard design constraint.** Datawrapper documents that dot plots, range plots and arrow plots cannot have their height set at all, because the row count determines it ([datawrapper-academy.md](../sources/datawrapper-academy.md)). Forty categories do not fit on a phone by being resized, as for a bar chart ([magnitude.md](magnitude.md)).

## What is contested

**Nothing native. There is no record here to disagree with itself.**

The inherited contest is the zero baseline and it is `authority-asserted` on both sides. Datawrapper releases it for dot and range plots because there is no filled bar, the FT scopes the rule by mark, the Urban Institute releases marks that "do not use length or height as the primary encoding" ([urban-institute.md](../sources/urban-institute.md)), and [Vega-Lite](../sources/vega-lite.md) forces zero on every quantitative positional scale whatever the mark. [lollipop-chart.md](lollipop-chart.md) carries the argument in full.

It binds a little differently here. There is no stem running back to the axis for a reader to take for a bar, which is the lollipop's exposure. But the segment is a length, and its ink is proportional to the gap, so proportional ink has something to bite on even though the origin it is proportional from is not zero.

## The failure mode it invites

**Comparing gaps across rows as though they were bars.** The segment looks like a bar and invites being read like one, and it is not one: it starts somewhere different in every row. `authority-asserted`, and it follows from the structure rather than from a study.

**Shipping without saying which dot is which.** Nothing about a dot at 40 and a dot at 60 says which is 2010 and which is 2024, or which is the treatment group. A legend, direct labels on the top row, or an arrowhead fixes it, and the chart is unreadable without one of them.

**Three sorts, and the reader sees none of them.** Sorting by the first value, by the second value or by the gap gives three different charts of the same data. [ranking.md](ranking.md) states the general version; this form has one more knob than most of that group, so the caption has more to say.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing on this page qualifies. The one inherited sentence available covers the endpoints, "each dot is position along a common scale, the most accurately read channel measured", with the step from this chart to that channel being conjecture as it is for every chart type. It says nothing about the gap, which is usually the reason the chart exists.

**Defensible, with the label said out loud:**

- "Both the levels and the change matter, so both are on the chart. The levels are on position and the gap is on an unanchored length, and that is the trade this form makes."
- "Thirty categories over two periods, so one row each rather than a slope chart. A legibility judgment about label collisions, with no study here on either form."
- "The axis does not start at zero, because nothing on the chart is a filled bar. A newsroom taxonomy, a chart tool and a style guide scope the rule that way, none of them tested it, and one plotting library disagrees outright."
- "Sorted by gap rather than by the later value, and the caption says so."

**Commonly repeated, and the evidence does not support it:**

- ~~"A dumbbell shows the change more accurately than two bars."~~ Nobody has measured this form. What is secure is the opposite in shape: it puts the levels on the good channel and the change on the worse one.
- ~~"The longer segment is the bigger change, so readers can rank the changes off the chart."~~ The first half is definitional. Whether people rank floating lengths reliably is untested here, and the one measurement of that penalty was made on a different stimulus. If ranking the changes is the job, plot the differences.
- ~~"It is a slope chart with the periods side by side."~~ It is not. A slope chart draws the reordering and this form cannot.

## See also

- [lollipop-chart.md](lollipop-chart.md) — one dot with a stem to the baseline, and the zero-baseline argument in full
- [slope-chart.md](slope-chart.md) — the other two-value form, and what it shows that this one cannot
- [ranking.md](ranking.md) — the group, and the free parameters it hands you
- [dot-strip-plot.md](dot-strip-plot.md) — many items on one shared axis, one value each
- [../concepts/channels.md](../concepts/channels.md) — the evidence tier this page inherits, including why the gap is on the worse channel
