---
type: chart-type
relationships: [change-over-time]
aliases: [Bar sparkline, Datawords, Inline chart, Micro chart, Sparkline, Win/loss sparkline, Word-sized graphic]
---

# Sparklines

A [line chart](line-chart.md) with the guides slot emptied and the whole graphic sized to sit inside a line of text, so the only thing on offer is the shape of the series.

Also called a **word-sized graphic**, an **inline chart** or a **micro chart**. [Tufte](../people/edward-tufte.md), who coined "sparkline", calls them "datawords" in his own text. The name covers a family rather than one form: a **bar sparkline** and a **win/loss sparkline** fill the same slot in a sentence with a different mark, and **no source in this wiki defines either variant**, so they are recorded here as names in circulation. The only sparkline material read from Tufte in this corpus is the line form.

**Where the Tufte material comes from, exactly.** [sources/tufte.md](../sources/tufte.md) covers *The Visual Display of Quantitative Information* only, is `secondary-only`, and carries nothing about sparklines; the term comes from *Beautiful Evidence* (2006), which nobody here has opened. What this corpus does have is an excerpt of that book's sparklines chapter, posted by Tufte on his own site, fetched and read locally, and recorded on [people/edward-tufte.md](../people/edward-tufte.md). That page notes it is the only thing in this wiki read from Tufte directly. Everything attributed to him below comes from that excerpt. `authority-asserted`, as everything of his is: he ran no experiments.

## When to reach for it, and when not

The form is defined for the case where the reading is "rising, falling, spiky, flat, above the band, below the band", and either the graphic belongs inside a sentence or many series have to be scanned in parallel in a table. Tufte's demonstration is a clinical glucose series inside running text, and a financial table stacking hundreds of series so they compare down the column.

**Removing the axes is the design, not an economy.** That has one consequence and it decides every use of the form: **every reading is relative and no value can be extracted from the mark.** Definitional. Tufte's own construction answers it by printing the most recent value as a number beside the line.

Questions the form does not answer:

| The question | Alternative |
|---|---|
| What is the value? | The printed number. That is what Tufte does, next to the line |
| How much did it change? | Any chart with an axis, or two numbers and a subtraction |
| Is this series higher than that one? | A [line chart](line-chart.md) on shared, drawn axes. Two sparklines share nothing unless the scale was deliberately shared, and nothing on them records whether it was |
| There are three or four points | A number, a sentence, or a table. There is no shape yet |
| Someone has to defend a conclusion drawn from it | A full chart. There is no axis to check the conclusion against |
| One share or one figure is the whole message | A single large number. The argument is on [part-to-whole.md](part-to-whole.md) and it applies to any group |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per (time, value), for one series |
| Transform | None. The y range is set per graphic unless it is deliberately shared across a set, which is a decision the drawing does not record |
| Geometry | Path, optionally with the endpoint or the min and max marked. The bar and win/loss variants swap this slot for a different mark |
| Scale | Time to position on x, value to position on y, over a range that is **not shown** |
| Coordinates | Cartesian, sized to the surrounding type. Tufte gives 14 letterspaces as a working width |
| Guides | **None.** Optionally a gray band behind the line for a normal range, and a number printed beside it |

**This is [line-chart.md](line-chart.md) with the guides slot emptied**, and that is the entire difference. [slope-chart.md](slope-chart.md) is the other page in this group built by emptying the same slot, and it fills the gap with direct labels; this form does not fill it at all.

## Channels

**Position along a common scale, within the one graphic, on a scale the reader cannot see.** The channel is inherited from [channels.md](../concepts/channels.md) with the standing caveat that the mapping from chart to channel is conjecture. What the missing guides do to it: the position reading holds inside a single sparkline, comparing one point of the series to another, and **it does not survive between two sparklines unless the scale was deliberately shared, and nothing on either graphic records whether it was.** Definitional.

**The gray band changes the task.** Drawing a normal range behind the line converts the reading from magnitude to a categorical above/inside/below judgment, which is what Tufte's clinical example is built to deliver. That is a different question, and it is the one thing this form can be made to answer without an axis.

**The ranking does not bear on the main reading anyway.** Shape, spikes and turning points are not value extraction, and the source authors scope themselves out of exactly those tasks ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)).

## What it is measurably good at

**Nothing. No study in this corpus tests a sparkline.**

## What it is measurably bad at

Nothing measured on this form. Two inherited results bear on it.

**Removing axis furniture has been measured once, and the result is element-conditional.** [Gillan & Richman (1994)](../studies/gillan-richman-1994-data-ink.md) found that removing the y-axis line and the x axis generally *increased* response time, meaning removal hurt, while removing tick marks helped, and that each element's effect depended on graph type, task, and which other elements were present. Three caveats: that study page is `secondary-only`, the stimuli were ordinary graphs rather than word-sized ones, and a sparkline removes the guides deliberately in exchange for fitting in a sentence, which is a trade Gillan & Richman never tested. **It does not settle this form, and it is the only place the corpus touches the design decision the form is built on.**

**The aspect ratio is set by the typography rather than by the analyst.** [Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) moved reader judgments by 129.5% on a line chart by changing the aspect ratio and nothing else, with the true values printed on the chart. On a sparkline the height is whatever the line of text allows. That is inherited exposure, stated at group level in [change-over-time.md](change-over-time.md), and the observation here is only that the parameter is decided by the page layout.

## What is contested

**Nothing about this form. There is no record here to disagree with itself.**

One adjacent fact bears on the form's origin. A sparkline is the data-ink argument taken to its limit, and that argument is the most contested thing in this corpus ([refutations.md](../refutations.md)). The one Tufte minimization anybody has measured, his midgap box plot, came out worse than the original it minimized ([edward-tufte.md](../people/edward-tufte.md)). Neither of those is about sparklines and neither is evidence against them. What they bear on is the data-ink argument the form is commonly justified by, not the form itself.

## The failure mode it invites

**Reading a value off it.** There is no axis, so there is no value, and the graphic gives the reader no sign that the reading they just made is unsupported. Tufte's own construction prints the value beside the line.

**Comparing two sparklines that do not share a scale.** Stacked in a column they look built for comparison. Independently scaled, a flat series and a violent one can produce the same picture. The drawing does not record which it is.

**Using one where a number would do.** A word-sized graphic of a four-point series is decoration in the shape of evidence.

All three follow from the structure. None has been tested on readers.

## Justifying the choice

**Defensible, evidence-backed:**

Nothing. No study here touches this form.

**Defensible, with the label said out loud:**

- "The most recent value is printed beside the line, tied to it by one accent color." Tufte's own construction, read from his excerpt, and asserted rather than tested.
- "The normal range is a gray band behind the line, so the reading is above, inside or below rather than a number." Same source, same status, and it is the design that makes an axis-free graphic answer a real question.
- "All forty sparklines in this table share one vertical scale, and the caption says so." Follows from the structure. Untested, and the alternative is a comparison the reader cannot know is invalid.
- "About fourteen letterspaces wide, so it sits in the line of text rather than interrupting it." Tufte's working width, `authority-asserted`.
- "Its purpose is to be approximately right at a glance rather than exactly wrong at length." That is his defense of the resolution trade, in his own frame: "General idea = max[data], min[design]."

**Commonly repeated, and the evidence does not support it:**

- ~~"Sparklines let readers see the value at a glance."~~ There is no axis. There is no value. There is a shape.
- ~~"Stripping the axes makes it cleaner, so it reads better."~~ The one measurement in this corpus on removing axis elements found the effect element-conditional, and found that removing the axis lines *hurt*.
- ~~"A sparkline is just a small line chart."~~ It is a line chart with the guides removed, and the guides were the part that made values readable. That is the trade the form makes; it is not the same chart.
- ~~"Tufte showed that sparklines work."~~ He proposed them, demonstrated them, and ran no experiments. Nobody in this corpus has tested them since.

## See also

- [line-chart.md](line-chart.md) — the same chart with its guides, and where the evidence in this group lives
- [slope-chart.md](slope-chart.md) — the other form here built by emptying the guides slot, and what it puts back
- [change-over-time.md](change-over-time.md) — the group, and the free parameters it leaves open
- [../people/edward-tufte.md](../people/edward-tufte.md) — the sparklines excerpt, the only Tufte material in this wiki read from Tufte
- [../sources/tufte.md](../sources/tufte.md) — the 1983 book, which is not where sparklines come from
- [tables.md](tables.md) — where a column of sparklines actually lives
