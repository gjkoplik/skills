---
type: chart-type
relationships: [part-to-whole]
aliases: [Donut chart, Pie chart]
---

# Pie and donut charts

A circle divided into wedges, each wedge's share of the total encoded by its arc length, its area, and the angle at the center. The donut is the same chart with the center removed, which removes the angle.

## When to reach for it, and when not

**Reach for it when** the total is a real quantity the reader cares about, "these parts are all of it" is part of what you are asserting, and there are few enough parts to label. Roughly five is the conventional ceiling and it is `authority-asserted`, not measured.

Use the **donut** whenever you want the center for a total, a label, or an icon. It costs nothing: the missing angle is the cue that was carrying the least.

**Do not reach for it when:**

| The question | Use instead |
|---|---|
| Which of these is biggest? | Sorted bar chart. Position instead of arc length |
| How big is this one part? | Bar chart |
| How does composition differ between two groups? | Grouped or small-multiple bars. Two pies cannot be compared |
| How did composition change over time? | [Stacked bar](stacked-bar.md), or a line chart of shares |
| There are fifteen parts | [Treemap](treemap.md), or a bar chart and drop the whole-constraint |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per part, with a non-negative magnitude |
| Transform | Normalize to shares summing to 1, then cumulative sum to get wedge boundaries |
| Geometry | Filled wedge (annular sector for a donut) |
| Scale | Share maps linearly to swept angle, and so to arc length and to area simultaneously |
| Coordinates | Polar |
| Guides | Labels or a legend. No axis exists |

The triple encoding puts **one number on three channels at once**, which is why the chart cannot be reasoned about the way single-channel charts can.

## Channels

Received wisdom, from Cleveland & McGill onward, says angle. **Measured, it is not angle.**

[Skau & Kosara (2016)](../studies/skau-kosara-2016.md) built six chart variants isolating each cue and found the two angle-only conditions produced the *highest* error and the widest spread, while arc-only and area-only conditions performed close to the full pie:

> "Error was smaller for the baseline charts, area chart, and the arc chart than the two angle-only charts. This was not what we hypothesized, and contradicts common wisdom that angles are critical to pie and donut chart perception."

Eells (1926) had pointed the same way ninety years earlier by simply asking: 51% of participants reported reading arc length, 25% area, 23% angle, 1% chord length.

**So the channels are arc length and area, with angle a minor and unreliable contributor.** That is measured on this chart directly, rather than inherited from a ranking of channels in the abstract ([channels.md](../concepts/channels.md)), which is why it can be stated flatly.

Note what Cleveland & McGill actually wrote, since they are usually cited as the source of the angle claim:

> "we conjecture that the primary elementary visual task for extracting the numerical information is perception of angle, but the areas and arc lengths of the pie slices are variable and probably are also involved in judging the data."

They flagged it as a conjecture and named the other two cues. The hardening into "pies encode angle" happened downstream.

## What it is measurably good at

**Being read about as accurately as a donut, and vice versa.** Skau & Kosara: the donut's log error was "slightly lower ... but well within the 95% confidence interval." Their second study varied the inner radius from filled pie to thin outline and found the same.

**Communicating that the parts form a whole.** No study in this set measures this. It is the form's actual purpose and it is `authority-asserted` across the entire practitioner literature.

## What it is measurably bad at

**Value extraction, compared with a bar chart.** [Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md), position-angle experiment: "In only 3 of the 40 cases was the pie chart more accurate on average than the bar chart." Overall error factor about 1.96 against position. Replicated by [Heer & Bostock (2010)](../studies/heer-bostock-2010.md).

This is the one criticism that is fully evidence-backed. It is also narrower than it sounds: it is about reading a number off a slice, not about the chart failing at its job.

**Larger shares.** Error grows with segment size for every encoding except angle-only (Skau & Kosara, study 1). A slice near half the circle is read less accurately than a small one.

## What is contested

**The mechanism.** Every element of the standard argument is in trouble:

- "Pies are read by angle" is **refuted** by direct decomposition.
- "Length beats angle" is **unsupported**, and the two Cleveland & McGill papers have to be kept apart to see it. The 1984 *JASA* table puts length, direction and angle at the *same* rank, with the note that "there is not enough information to separate the ties," and its two experiments are not comparable to each other, so it contains no test of the pair. The 1985 *Science* table does separate them, length above angle, but calls the whole ordering "a tentative working hypothesis" whose aspects "are partly conjectural in that we have no controlled experimentation to support them" (see [william-cleveland.md](../people/william-cleveland.md) for both tables). [Heer & Bostock](../studies/heer-bostock-2010.md) then ran the head-to-head under a common task format: "the results do not support this."

So bars beat pies, measured. The reason universally given for it is not established. State the finding, drop the mechanism.

**The many-slices case.** Universally asserted to be where pies fail, and not tested by any study here. Skau & Kosara deliberately used two segments. This is `absence of evidence`, not evidence of absence: the criticism is plausible, widely held, and unmeasured in this source set.

## The failure mode it invites

**Comparing across pies.** Two pie charts side by side invite reading a slice in one against a slice in the other, which requires comparing arc lengths at different rotational offsets with no common baseline. The form gives no support for this and every visual cue that it should work. `authority-asserted`.

**Ordering by something other than size, or starting somewhere other than the top.** Removes the one thing that makes wedge boundaries comparable across charts. `authority-asserted`.

## Justifying the choice

**Defensible, evidence-backed:**

- "A bar chart reads values more accurately, measured and replicated. I used a pie anyway because the reader needs to see the parts exhaust the total, and reading exact values is not the task."
- "I used a donut rather than a pie to put the total in the center. Donut and pie measure as virtually identical in accuracy, so the center is free."

**Defensible, with the label said out loud:**

- "Five slices is about the limit. That is practitioner convention, not a measured result. No study here tests the many-slice case."

**Not defensible, and it is the most repeated claim about this chart:**

- ~~"Pies are bad because they encode angle and angle is a weak channel."~~ Both halves fail. [Skau & Kosara](../studies/skau-kosara-2016.md) isolated the cues and found angle the *least* used. [Heer & Bostock](../studies/heer-bostock-2010.md) tested length against angle directly and "the results do not support this."
- ~~"Donuts are worse than pies because the missing center destroys the angle."~~ It does, and it does not matter.

The conclusion that bars beat pies for value extraction survives. The mechanism everyone gives for it does not. State the finding, drop the explanation.
