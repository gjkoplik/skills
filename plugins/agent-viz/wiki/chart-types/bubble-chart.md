---
type: chart-type
relationships: [correlation]
aliases: [Bubble chart]
---

# Bubble chart

A scatterplot with a third quantitative variable encoded on the area of each point.

## When to reach for it, and when not

The form is defined for a [scatterplot](scatterplot.md) whose marks carry a third quantity that only needs to be read roughly, because area is the least accurately read of the measured channels. Population behind a per-capita scatter is the archetype, telling the reader which points to take seriously without ever being read as a number.

| The question | Alternative |
|---|---|
| How big is the third variable, exactly? | Position. A bar chart, or a second panel with it on an axis |
| The third variable is categorical | Color or shape. Size encodes an unordered category badly and implies an ordering that is not there |
| Which of these two bubbles is bigger? | A sorted bar or dot plot. Area is measured as worse than angle, and both as much worse than position |
| The points already overplot | Bubbles make overplotting worse by construction, since each mark grows. A binned density plot, or the third variable dropped |
| Nothing quantitative is riding on size | A plain [scatterplot](scatterplot.md). Size that encodes nothing is decoration that reads as an encoding |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per observation, carrying three quantitative values for the same unit |
| Transform | None on x and y. The size variable is mapped through a square root, since area rather than radius has to be proportional to the value |
| Geometry | Circle, or any filled shape of controlled area |
| Scale | Two positional scales, plus one area scale that must be anchored at zero for area to be proportional at all |
| Coordinates | Cartesian |
| Guides | Two axes, plus a size legend showing at least two reference bubbles with their values |

The transform and scale rows are arithmetic, not evidence. Mapped to radius, a doubled value gets four times the ink. And this is the one place in its group where zero is not optional, since proportionality means nothing unless zero area is zero.

## Channels

x and y are position along a common scale, and the third variable is circular area. [Heer & Bostock (2010)](../studies/heer-bostock-2010.md) found area worse than angle, both significantly worse than position, and circular and rectangular area comparably accurate ([channels.md](../concepts/channels.md)). Their area stimulus was drawn as a bubble chart, which shortens the usual step from chart to channel. The task was still proportional judgment on a stripped stimulus, so the result is inherited, not native.

## What it is measurably good at

Nothing measured belongs to the bubble form. Its offer is structural: three variables on one mark, without faceting or a second panel.

## What it is measurably bad at

**Value extraction on the size variable.** Area is the least accurate channel [Heer & Bostock](../studies/heer-bostock-2010.md) tested, below angle and well below position. So the size variable is context, not content.

**Exaggerated area.** [Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) ran a bubble-chart condition, area-as-quantity, in a between-subjects Mechanical Turk experiment. Mean response on a five-point "how much bigger" scale went from 1.71 in the control to 2.71 when distorted, a 58.5% increase (Mann-Whitney U = 1121, Z = 3.08, p = 0.0007, r = 0.34).

- The true values were printed on every chart, so the effect is not a failure to read numbers, and it counts *against* labeling as the remedy.
- Bubble/area produced the smallest of the three exaggeration effects, but chart type and distortion are confounded one-to-one, never varied independently. "Bubbles distort less than truncated bars" is not in this result.
- One scenario, one trial per participant, 40 control and 40 deceptive after exclusions, measuring a shift on a rating scale.

## What is contested

No study here disagrees with another about bubble charts, which is `absence of evidence`, not agreement.

Open, and it decides the design: whether readers judge these marks by area or partly by diameter. [Heer & Bostock](../studies/heer-bostock-2010.md) offer a side-length proxy as a hypothesis for their rectangle result and say "additional experimentation is needed to form an accurate perceptual model." Nobody has decomposed bubbles that way. Area scaling is the default because it makes the encoding proportional, not because readers are shown to use area.

## The failure mode it invites

**Scaling by radius or diameter.** The commonest bug in this form, inflating large values quadratically without looking wrong. `authority-asserted` as advice, though the arithmetic is not in question.

**A missing or one-bubble size legend.** Without a reference the area scale is unreadable, and the reader falls back on relative size, the judgment the evidence rates worst. `authority-asserted`.

**Size carrying the message.** If the third variable is the finding, it is on the wrong channel.

## Justifying the choice

**Defensible, evidence-backed:**

- "Population is on size because it only needs to be read as rough context. Area is measured as less accurate than angle and much less accurate than position, so nothing precise is riding on it."
- "Size is scaled by area, not radius, and anchored at zero. Otherwise the encoding is not proportional to the value at all."
- "The comparison the reader has to make exactly is on an axis rather than on bubble size."

**Defensible, with the label said out loud:**

- "The size legend shows three reference values. That is convention; no study here measures what a size legend is worth."
- "I capped the largest bubble to limit overplotting, which distorts the area scale at the top. A tradeoff I made deliberately, not a rule."

**Not defensible:**

- ~~"Bubble charts are less misleading than truncated bar charts."~~ The bubble effect was smaller, but confounded with chart type, so the comparison is not in the data.
- ~~"Labeling the values fixes the distortion."~~ The values were printed on every chart.
- ~~"Area works fine because readers only need the ranking."~~ Area lost on proportional judgment, and ordinal comparison of areas is unmeasured here.

## See also

- [scatterplot.md](scatterplot.md): the chart this one adds a channel to
- [treemap.md](treemap.md): the other area-encoding page, with the circular-versus-rectangular result
- [correlation.md](correlation.md): the group argument, including the zero-baseline exception this form sits outside of
