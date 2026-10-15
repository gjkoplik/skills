---
type: chart-type
relationships: [part-to-whole]
aliases: [Donut chart, Pie chart]
---

# Pie and donut charts

A circle divided into wedges, each wedge's share of the total encoded by its arc length, its area and the angle at the center. The donut is the same chart with the center removed, which removes the angle.

## When to reach for it, and when not

The form is defined for a total the reader cares about, where "these parts are all of it" is part of the assertion and the parts are few enough to label. Roughly five is the conventional ceiling, `authority-asserted`, not measured.

The **donut** frees the center for a total, a label or an icon at no cost, since the missing angle carried the least.

| The question | Alternative |
|---|---|
| Which of these is biggest? | Sorted bar chart. Position instead of arc length |
| How big is this one part? | Bar chart |
| How does composition differ between two groups? | Grouped or small-multiple bars. Two pies cannot be compared |
| How did composition change over time? | [Stacked bar](stacked-bar.md), or a line chart of shares |
| There are fifteen parts | [Treemap](treemap.md), or a bar chart without the whole-constraint |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per part, with a non-negative magnitude |
| Transform | Normalize to shares summing to 1, then cumulative sum to get wedge boundaries |
| Geometry | Filled wedge (annular sector for a donut) |
| Scale | Share maps linearly to swept angle, and so to arc length and to area simultaneously |
| Coordinates | Polar |
| Guides | Labels or a legend. No axis exists |

The scale puts one number on three channels at once, so the chart cannot be reasoned about the way single-channel charts can.

## Channels

Received wisdom, from Cleveland & McGill onward, says angle. Measured on this chart directly, rather than inherited from a ranking of channels ([channels.md](../concepts/channels.md)), the channels are arc length and area, with angle a minor and unreliable contributor.

[Skau & Kosara (2016)](../studies/skau-kosara-2016.md) built six variants isolating each cue. The two angle-only variants had the *highest* error and widest spread, and arc-only and area-only came close to the full pie:

> "Error was smaller for the baseline charts, area chart, and the arc chart than the two angle-only charts. This was not what we hypothesized, and contradicts common wisdom that angles are critical to pie and donut chart perception."

Eells (1926) pointed the same way by asking readers: 51% reported reading arc length, 25% area, 23% angle, 1% chord length.

Cleveland & McGill, the usual citation for angle, wrote:

> "we conjecture that the primary elementary visual task for extracting the numerical information is perception of angle, but the areas and arc lengths of the pie slices are variable and probably are also involved in judging the data."

They called it a conjecture and named the other two cues.

## What it is measurably good at

A donut reads as accurately as a pie. Skau & Kosara found the donut's log error "slightly lower ... but well within the 95% confidence interval." Their second study varied the inner radius from filled pie to thin outline and found the same.

Showing that the parts form a whole is the form's purpose. No study in this set measures it, and it is `authority-asserted` across the practitioner literature.

## What it is measurably bad at

**Value extraction, against a bar chart.** In the position-angle experiment of [Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md), "In only 3 of the 40 cases was the pie chart more accurate on average than the bar chart." Overall error was a factor of about 1.96 against position. [Heer & Bostock (2010)](../studies/heer-bostock-2010.md) replicated it. It is the one fully evidence-backed criticism, and it is about reading values, not about showing a whole.

**Larger shares.** Error grows with segment size for every encoding except angle-only (Skau & Kosara, study 1).

## What is contested

**The mechanism.**

- "Pies are read by angle" is **refuted** by direct decomposition.
- "Length beats angle" is **unsupported**, and the two Cleveland & McGill papers have to be kept apart to see it. The 1984 *JASA* table puts length, direction and angle at the *same* rank, with the note that "there is not enough information to separate the ties," and its two experiments are not comparable to each other, so it contains no test of the pair. The 1985 *Science* table does separate them, length above angle, but calls the whole ordering "a tentative working hypothesis" whose aspects "are partly conjectural in that we have no controlled experimentation to support them." Both tables are on [william-cleveland.md](../people/william-cleveland.md). [Heer & Bostock](../studies/heer-bostock-2010.md) then ran the head-to-head under a common task format: "the results do not support this."

So bars beat pies, measured, and the reason usually given for it is not established.

**The many-slices case.** Universally asserted to be where pies fail, and plausible, but untested here. Skau & Kosara used two segments. `absence of evidence`.

## The failure mode it invites

**Comparing across pies.** A slice in one pie against a slice in another is a comparison of arc lengths at different rotational offsets with no common baseline. The form gives no support for it and every cue that it should work. `authority-asserted`.

**Ordering by something other than size, or starting somewhere other than the top.** It removes what makes wedge boundaries comparable across charts. `authority-asserted`.

## Justifying the choice

**Defensible, evidence-backed:**

- "A bar chart reads values more accurately, measured and replicated. I used a pie anyway because the reader needs to see the parts exhaust the total, and reading exact values is not the task."
- "I used a donut rather than a pie to put the total in the center. Donut and pie measure as virtually identical in accuracy, so the center is free."

**Defensible, with the label said out loud:**

- "Five slices is about the limit. That is practitioner convention, not a measured result. No study here tests the many-slice case."

**Not defensible:**

- ~~"Pies are bad because they encode angle and angle is a weak channel."~~ Both halves fail. [Skau & Kosara](../studies/skau-kosara-2016.md) found angle the *least* used cue, and on length against angle [Heer & Bostock](../studies/heer-bostock-2010.md) report "the results do not support this."
- ~~"Donuts are worse than pies because the missing center destroys the angle."~~ It does remove the angle, and accuracy does not change.
