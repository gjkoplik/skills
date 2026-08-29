---
type: chart-type
relationships: [spatial, magnitude]
aliases: [Cartogram, Dorling cartogram, Hex grid map, Tile grid map]
---

# Cartograms

A map whose regions are resized, or replaced by simpler shapes, so that each region's **area** encodes a value and the geography is deliberately distorted to make room for it.

**The family is filed together and does not reason together.** In a value-by-area cartogram (contiguous, non-contiguous, Dorling circles) area *is* the encoding. In a tile or hex grid map every region gets an identical cell, which removes land area as a distortion and removes area as an encoding at the same time, handing the value back to fill color. **A tile grid map is a [choropleth](choropleth-map.md) on a schematic base geography, not a value-by-area cartogram.** Everything below is about the value-by-area kind unless it says otherwise.

## When to reach for it, and when not

**The form applies where** the value is a total, the base geography's land areas are badly out of proportion to where that total actually sits, and that mismatch is part of the assertion. The sentence it makes is "the map you are picturing is the wrong shape for this quantity."

**Questions the form does not answer:**

| The question | Alternative |
|---|---|
| Which is biggest, and in what order? | Sorted bar chart. Area does not support reliable ordering by eye |
| The value is a rate | [Choropleth](choropleth-map.md). Rates do not add up over area, so sizing a region by one asserts nothing |
| The reader has to find their own region | [Choropleth](choropleth-map.md), or a table. Recognizability is exactly what the form spends |
| The audience does not already know this map well | Almost anything else. The distortion only reads as distortion against a map the reader carries in their head |
| What are the exact values? | A table, or a sorted bar chart |
| How did it change between two years? | Not two cartograms. Layout is recomputed per dataset, so nothing is positionally stable |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per region, with a boundary and a magnitude, normally a total |
| Transform | An area-equalizing layout algorithm that resizes and relocates regions subject to some mix of contiguity, shape and topology constraints |
| Geometry | Distorted polygon, circle (Dorling), or a uniform tile |
| Scale | Magnitude to area, which must be anchored at zero for the encoding to be proportional at all |
| Coordinates | A named projection, with a distortion applied on top of it |
| Guides | An area legend with at least two reference sizes, region labels (shape no longer identifies anything), and often an inset of the true geography |

**The layout algorithm sits in the transform slot**, exactly as it does for a [treemap](treemap.md). Two cartograms of the same data under different algorithms can look entirely different, so the algorithm is a data-encoding decision rather than a styling one.

**Zero is not optional here**, for the same arithmetic reason as on a [bubble chart](bubble-chart.md): proportionality to a value means nothing if zero area does not mean zero.

## Channels

**Area**, plus geographic position that has been degraded on purpose.

Inherited from [channels.md](../concepts/channels.md) with a link rather than a restatement: area is read less accurately than angle and much less accurately than position ([Heer & Bostock 2010](../studies/heer-bostock-2010.md)), and circular and rectangular area judgments come out comparably accurate. Nothing in that transfers to the *shapes* a contiguous cartogram produces, which are neither circles nor rectangles.

**What Heer & Bostock actually did, since this is the study people reach for.** Experiment 1B "extended circular area judgment to rectangles, motivated by treemaps and cartograms." It ran a 3x2x6 factorial, 108 trials, on pairs of marked rectangles shown bare and again inside a full treemap, at 380x380 pixels, with aspect ratios taken from a squarified treemap layout. It found rectangular area about as accurate as circular area, and aspect ratio 1 the worst case. **There was no cartogram in the stimulus set, no map, no distorted polygon and no recognizability task.** Cartograms appear in that paper as a stated motivation and nowhere else. The transferable claim is at the channel level only, and it is an inheritance rather than a finding about this form.

## What it is measurably good at

**Nothing. No study in this corpus tests a cartogram.**

## What it is measurably bad at

Nothing measured on this form. The inherited exposure is the area channel, above. The native cost is definitional and it is the trade the whole form is built on:

**A cartogram fixes the choropleth's area problem by distorting the geography, and pays for it in recognizability.** Both halves follow from what the mark is. The area of every mark now comes from the data, so the reader's visual field is weighted by the variable rather than by land, which is the defect that sends totals off a [choropleth](choropleth-map.md) in the first place. And the shapes, adjacencies and relative sizes a reader uses to locate themselves on a map are precisely what the algorithm moved.

**Whether readers lose more from the distortion than they gain from the honest weighting is not tested here, by anyone.** That is the question that would decide when to use the form, and this corpus cannot answer it. `absence of evidence`.

## What is contested

**Nothing. There is no record here to disagree with itself.**

## The failure mode it invites

**Assuming the reader knows the map.** The distortion carries information only against a mental image the reader already holds. Drawn for an audience without that image, a cartogram is an unlabeled abstract shape diagram, and the whole payment bought nothing. `authority-asserted`, and it follows from the construction.

**Sizing a rate.** Area is additive over regions and a rate is not, so a region sized by its unemployment rate is asserting a quantity that does not exist. This is the mirror image of the choropleth's totals error, and it comes from the same place: whether the mark's extent tracks an extensive or an intensive quantity.

**Scaling by a linear dimension instead of by area.** The standard area-encoding bug, worked through on [bubble-chart.md](bubble-chart.md). It inflates large values quadratically and it will not look wrong.

**Comparing two cartograms.** The layout is a function of the whole dataset, so a region lands in a different place and shape in each. Same structural problem as two [treemaps](treemap.md).

**Calling a tile grid map a cartogram** and then claiming the area honesty it does not have. Equal cells remove the land-area weighting by removing area from the encoding entirely; the value goes back onto fill color and every caution on the [choropleth](choropleth-map.md) page applies again.

## Justifying the choice

**Defensible, evidence-backed:**

Nothing native. The one inherited sentence is a caution rather than a justification: "area is read less accurately than angle and much less accurately than position, measured, so the reader is not expected to take numbers off this figure" ([channels.md](../concepts/channels.md)).

**Defensible, with the label said out loud:**

- "A cartogram because the choropleth of this total was a map of land area with a color layer on it. That reasoning is structural rather than measured, and no study here tests whether readers do better on the cartogram."
- "Region areas are proportional to the count and anchored at zero, so the visual weight in this figure comes from the variable." Definitional, and it is the entire claim the form supports.
- "An inset shows the true geography, and every region is labeled." Practitioner convention, no measured value.
- "The layout algorithm is named in the caption, because a different one gives a different picture."

**Commonly repeated, and the evidence does not support it:**

- ~~"Heer & Bostock validated cartograms."~~ They named cartograms as a motivation for studying rectangles and then measured rectangles. There is no map in that paper.
- ~~"A cartogram is more accurate than a choropleth."~~ Nobody has measured either one. What can be said is structural: the visual weight now comes from the variable instead of from land area. Accuracy is a different claim with nothing behind it.
- ~~"Distortion is fine, people adjust."~~ Untested, in either direction. What the record supports is that the form trades a certain defect for an uncertain one.

## See also

- [spatial.md](spatial.md) — the group, and the area argument stated once for all three forms
- [choropleth-map.md](choropleth-map.md) — the form this one is a reaction to
- [treemap.md](treemap.md) — the other page where the layout algorithm lives in the transform slot
- [bubble-chart.md](bubble-chart.md) — area scaling, zero anchoring, and the size-legend problem
- [../studies/heer-bostock-2010.md](../studies/heer-bostock-2010.md) — the rectangle experiment, and what it did not measure
