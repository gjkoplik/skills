---
type: chart-type
relationships: [correlation]
aliases: [Bubble chart]
---

# Bubble chart

A scatterplot with a third quantitative variable encoded on the area of each point.

## When to reach for it, and when not

**Reach for it when** you already want a [scatterplot](scatterplot.md), a third quantity genuinely belongs on the same marks, and rough is good enough for it. The third variable should be the one whose exact values matter least, because it is going onto the least accurately read of the channels anyone has measured. Population behind a per-capita scatter is the archetype: it tells the reader which points to take seriously without ever needing to be read as a number.

**Do not reach for it when:**

| The question | Use instead |
|---|---|
| How big is the third variable, exactly? | Put it on position. A bar chart, or a second panel with it on an axis |
| The third variable is categorical | Color or shape. Size encodes an unordered category badly and implies an ordering that is not there |
| Which of these two bubbles is bigger? | A sorted bar or dot plot. Area is measured as worse than angle, and both as much worse than position |
| The points already overplot | Bubbles make overplotting worse by construction, since each mark grows. A binned density plot, or drop the third variable |
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

Two of those rows are arithmetic rather than advice, and carry no evidence label. **If the value is mapped to radius, area grows as its square**, so a doubled value gets four times the ink. And **an area encoding is the one place in this group where zero is not optional**: proportionality to a value has no meaning if zero area does not mean zero.

## Channels

x and y are position along a common scale. The third variable is on **circular area**.

Inherited from [channels.md](../concepts/channels.md), with the link rather than a restatement: [Heer & Bostock (2010)](../studies/heer-bostock-2010.md) found area worse than angle and both significantly worse than position, and found circular and rectangular area comparably accurate. Two details make the inheritance unusually direct here. Their area stimulus was drawn as a bubble chart, so the usual conjectural step from chart to channel is shorter than for most types. And the task was still proportional judgment on a stripped stimulus, not a bubble chart doing a job in the world, so it is an inheritance and not a native finding.

## What it is measurably good at

**Nothing that has been measured belongs to the bubble form specifically.** The positional part of the chart inherits the position result; the size part inherits the area result, which is a cost rather than a benefit.

What survives without measurement, because it follows from the construction: three variables on one mark, with no faceting and no second panel. That is the entire offer.

## What it is measurably bad at

**Value extraction on the size variable.** Area is the least accurate of the channels tested in [Heer & Bostock](../studies/heer-bostock-2010.md), below angle and well below position. Inherited, and the strongest reason to treat the size variable as context rather than as content.

**Moving a reader's judgment when the area encoding exaggerates.** [Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) included a bubble-chart condition, labeled area-as-quantity, in a between-subjects Mechanical Turk experiment. Mean response on a five-point "how much bigger" scale went from 1.71 in the control to 2.71 in the distorted condition, a 58.5% increase, Mann-Whitney U = 1121, Z = 3.08, p = 0.0007, r = 0.34. Check the scope before citing it:

- **The true values were printed on every chart.** The effect is not a failure to read numbers, which also means this is evidence *against* labeling as the remedy rather than for it.
- **It cannot be used to rank distortions.** Bubble/area produced the smallest of the three exaggeration effects, but chart type and distortion are confounded one-to-one and the paper never varies the distortion within a chart type. "Bubbles distort less than truncated bars" is not in this result.
- **One scenario, one trial per participant**, 40 control and 40 deceptive after exclusions. The construct measured is a shift in a rating-scale response.

## What is contested

**Nothing in this source set.** No study here disagrees with another about bubble charts, which is `absence of evidence` and not agreement.

The open question worth naming, since it decides the design: whether readers judge these marks by area or partly by diameter. [Heer & Bostock](../studies/heer-bostock-2010.md) offer a side-length proxy as a hypothesis for their rectangle result and say plainly that "additional experimentation is needed to form an accurate perceptual model." Nobody has run the equivalent decomposition on bubbles. Scaling by area is the defensible default because it is the one that makes the encoding proportional, not because a study has shown readers use it.

## The failure mode it invites

**Scaling by radius or by diameter.** It is the most common bug in this form, it inflates large values quadratically, and it will not look wrong. `authority-asserted` as advice; the arithmetic itself is not in question.

**A size legend that is missing or shows one bubble.** With no reference the area scale is unreadable, and the reader falls back on relative size, which is the judgment the evidence says is worst. `authority-asserted`.

**Letting size carry the message.** If the third variable is the finding, it is on the wrong channel. The form is for context riding along with a relationship, not for a third headline.

## Justifying the choice

**Defensible, evidence-backed:**

- "Population is on size because it only needs to be read as rough context. Area is measured as less accurate than angle and much less accurate than position, so nothing precise is riding on it."
- "Size is scaled by area, not radius, and anchored at zero. Otherwise the encoding is not proportional to the value at all."
- "The comparison the reader has to make exactly is on an axis rather than on bubble size."

**Defensible, with the label said out loud:**

- "The size legend shows three reference values. That is convention; no study here measures what a size legend is worth."
- "I capped the largest bubble to limit overplotting, which distorts the area scale at the top. A tradeoff I made deliberately, not a rule."

**Not defensible:**

- ~~"Bubble charts are less misleading than truncated bar charts."~~ Pandey et al. measured a smaller effect for the bubble condition, but chart type and distortion are confounded one-to-one in that design and the authors never vary distortion within a chart type. The comparison is not in the data.
- ~~"Labeling the values fixes the distortion."~~ The values were printed on every chart in that experiment and the effect appeared anyway.
- ~~"Area works fine because readers only need the ranking."~~ Area lost to angle and to position on exactly the proportional-judgment task, and ordinal comparison of areas has not been measured separately here.

## See also

- [scatterplot.md](scatterplot.md) — the chart this one adds a channel to
- [treemap.md](treemap.md) — the other area-encoding page, and where the circular-versus-rectangular result is worked through
- [correlation.md](correlation.md) — the group argument, including the zero-baseline exception this form sits outside of
