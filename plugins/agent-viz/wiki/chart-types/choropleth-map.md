---
type: chart-type
relationships: [spatial]
aliases: [Choropleth map]
---

# Choropleth maps

A base geography drawn as filled polygons, with each region's fill color encoding one value for that whole region.

## When to reach for it, and when not

**The form applies where** the reader already thinks in those regions (the states, counties or countries are the units the decision is made in), the value is a rate or another intensive quantity that makes sense as a property of every point inside the region, and the pattern to be read is geographic rather than ordinal.

The FT's gloss carries two rules, not one: a basic choropleth "should always be rates rather than totals and use a sensible base geography" ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). The second half is the quieter one. The base geography decides what the units of the analysis are, and administrative boundaries were drawn for administration, not for the variable being mapped.

**Questions the form does not answer:**

| The question | Alternative |
|---|---|
| Which regions are highest, and in what order? | Sorted bar chart. Fill lightness does not support ordering by eye the way position does |
| How big is the total in each region? | A proportional symbol map (no page here). FT: "Use for totals rather than rates". Or a [cartogram](cartogram.md) |
| Where *within* the region are the things? | [Dot density](dot-density-map.md), where sub-region locations genuinely exist |
| What is the value for my region? | A table. A reader hunting one region is doing a lookup through a color scale |
| How much did it change? | The change itself, mapped. Two choropleths side by side are two color scales for the reader to reconcile |
| The regions vary enormously in size | [Cartogram](cartogram.md), or a tile grid map. Here, land area sets the visual weight |
| The value is a count | [Dot density](dot-density-map.md), a proportional symbol map, or a denominator applied to make it a rate |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per region, keyed to a boundary in a geographic file, carrying one value |
| Transform | Usually two: normalize a count to a rate by some denominator, and bin the continuous values into classes (or deliberately not) |
| Geometry | Filled polygon, its outline given by the base geography rather than by the data |
| Scale | Value to fill color, on a sequential or diverging ramp |
| Coordinates | A named map projection |
| Guides | A color legend or colorbar with units, and the projection named. No axis exists |

Two of those rows carry the whole character of the form.

**The geometry slot takes no input from the data.** The shape, position and size of every mark are fixed before any value arrives. That is what separates this from every other filled-area chart in the wiki, where the mark's extent is the encoding.

**The transform slot holds the two decisions that change the picture most**, the denominator and the binning, and neither is visible in the drawing. The palette gets all the attention and moves the image less than either of them.

## Channels

**Color lightness, usually with saturation riding along.** The 1984 Cleveland & McGill table puts shading and color saturation together in its bottom rank, below area and below volume. The section of [channels.md](../concepts/channels.md) on what "color is the worst channel" actually means sets out how far that fact goes.

The distinction is the whole design decision. An ordered lightness ramp is **low-accuracy** for magnitude. Color hue is not low-accuracy for magnitude, it is **unsuited** to it, because it has no unambiguous ordering from small to large. Those are different defects with different remedies. A sequential ramp read imprecisely is a working choropleth. A categorical palette on an ordered variable is a chart that cannot be read as a magnitude at all, which is why inventory topic 23 forbids crossing colormap class with data type.

[Bertin](../people/jacques-bertin.md) arrives at the same place from a different direction. In his levels of organization, `valeur` (lightness) is an **ordered** variable but not a quantitative one: only size is quantitative, and white cannot serve as a unit for measuring gray. So a choropleth supports "more here than there" and does not support "twice as much there as here". `authority-asserted`; there are no experiments in Bertin.

Position is on the map, and the map is not the value. This form has no secondary channel for the variable.

## What it is measurably good at

**Nothing. No study in this corpus tests a choropleth**, or any other map. See [spatial.md](spatial.md), where that is stated once for the whole group.

What the form does is not in dispute and is also not measured: it puts each value where its thing is, so a reader who does not know the region names can still see a regional pattern. That is the entire offer.

## What it is measurably bad at

Nothing measured on this form. Two exposures worth naming, one inherited and one definitional.

**Value extraction rides on the least accurate family of channels anyone has ranked**, inherited from [channels.md](../concepts/channels.md) with the usual caveat that the step from this chart to that channel is conjecture. Practically: nobody reads a number off a choropleth. Where the numbers matter, they sit in a table.

**The area on the page is the base geography, not the data.** This is the form's central defect and it is definitional, following from the fact that the mark's extent is fixed before the values arrive. A region's share of the reader's visual field is set by how much land it covers, so large sparse regions dominate the image and small dense ones can disappear. Neither fact has anything to do with the variable. **Whether that measurably biases the conclusions readers draw is not tested in this corpus.** The two claims have to stay apart: the weighting is certain, the effect on judgment is unmeasured.

**The rates rule follows from that, and this is why it generalizes.** The mark asserts one value across a whole territory. A rate can bear that, because a rate is a property of points inside the region rather than of its extent. A total cannot: painting it across a fixed polygon claims both that the count is spread evenly through the region and that its importance scales with land area. Definitional reasoning, and it is the same reasoning that sends totals to a proportional symbol map, where the mark's area is set by the value and geography only decides where the mark sits.

## What is contested

**Nothing. There is no record here to disagree with itself.**

The most consequential open decision is **classification**: how many bins, where the breaks fall, or whether to leave the scale continuous. Every break moves regions between colors, and a different break set can create or erase a pattern without any number changing. Cairo's *The Truthful Art* is the one source in this wiki named as covering choropleth classification, and it is [`secondary-only`](../sources/cairo-truthful-art.md) for its argument, so nothing about what it recommends is vouched here. `absence of evidence`, and a real hole rather than a settled question.

## The failure mode it invites

**The population map.** Urban, inventory topic 22: "If the map only shows where people live, it is a population map." Munzner's slides state it as the form's named failure, "most attributes just show where people live", and prescribe "normalize when appropriate" ([munzner-vad.md](../sources/munzner-vad.md)). Two unrelated sources, both `authority-asserted`. It is the default outcome for any count, and it survives normalization badly too, since many rates are correlated with density. The check is cheap: the same map redrawn with population as the variable, compared against the original.

**A diverging ramp with an accidental midpoint.** A diverging scale asserts that a particular value is the neutral one. A midpoint left wherever the library put it asserts a threshold nobody chose. Topic 32, and Urban's rule: "The center of the diverging palette should always be labeled to avoid confusing the reader." `authority-asserted`.

**Two choropleths on two color scales.** Same trap as comparing two treemaps or two pies: nothing survives the comparison, and every visual cue says it should. The remedies are one scale fixed across panels, or the difference mapped directly.

**Taking the default binning.** The transform slot is where the picture is decided, and the default was not chosen for the distribution at hand. `authority-asserted`, and unusually cheap to check by redrawing with a different break set.

## Justifying the choice

**Defensible, evidence-backed:**

- "The rate is on fill color and the exact values are in the table beneath. Color is read less accurately than position, measured, so nothing precise rides on the map." Inherited from [channels.md](../concepts/channels.md); the step from this chart to that channel is conjecture.

Nothing else is native to the form. No study here tests it.

**Defensible, with the label said out loud:**

- "Rates, not totals, and the denominator is stated. That is the FT's rule for this chart and the reasoning is structural; no experiment here tests reader behavior on it."
- "A sequential ramp, because the variable is ordered and has no meaningful midpoint." Colormap class matched to data type, topic 23, `authority-asserted` from matplotlib's own documentation.
- "Albers Equal Area, named in the caption." Urban's rule for US print maps, topic 21.
- "The palette was run through a color-vision-deficiency check rather than eyeballed." Datawrapper ships that check; topic 26.
- "Five classes with stated breaks, not a continuous ramp." A judgment call with nothing behind it in this corpus.

**Commonly repeated, and the evidence does not support it:**

- ~~"A choropleth shows where the quantity is."~~ It shows where the *rate* is, weighted by land area. Where the quantity is takes a [cartogram](cartogram.md), a [dot density map](dot-density-map.md) or a proportional symbol map, all of which put the amount on the mark's extent.
- ~~"Color is the worst channel, so choropleths are the worst chart."~~ Two errors stacked. The claim is about magnitude only, and it separates ordered lightness (imprecise) from hue (unsuited), which is the distinction that decides whether the palette works at all. And no study in this corpus has tested a choropleth against anything.
- ~~"An equal-area projection makes the areas honest."~~ It removes the projection's contribution. The base geography's own mismatch between land area and where the quantity lives is untouched, and it is usually the larger effect.

## See also

- [spatial.md](spatial.md) — the group, and why nothing in it is evidence-backed
- [cartogram.md](cartogram.md) — the form that trades recognizability for fixing the area problem
- [dot-density-map.md](dot-density-map.md) — the form that handles counts, and what it costs to place the dots
- [../concepts/channels.md](../concepts/channels.md) — ordered lightness versus hue, and why the difference is not a matter of degree
- [../people/jacques-bertin.md](../people/jacques-bertin.md) — lightness as an ordered but not quantitative variable
