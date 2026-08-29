---
type: index
---

# Spatial

Data drawn at geographic positions, so that *where* a value sits is part of what the reader takes away.

## Is geography the question, or an available column?

This is the one FT relationship whose category definition is written as a restriction rather than as a description ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)):

> "Used only when precise locations or geographical patterns in data are more important to the reader than anything else."

*Used only when.* *More important to the reader than anything else.* Every other category in that taxonomy states what the family shows; this one states the condition under which it applies. `authority-asserted`.

The Urban Institute style guide, by [Jonathan Schwabish](../people/jonathan-schwabish.md), states the same test as a diagnosis (inventory topic 22): **"If the map only shows where people live, it is a population map."** `authority-asserted`, and now corroborated from an unrelated direction: Munzner's own course slides give "most attributes just show where people live" as the choropleth failure, and add "visual salience depends on region size, not true importance wrt attribute value" ([munzner-vad.md](../sources/munzner-vad.md), read from the 2021 slide deck rather than the book). Two sources with no relationship to each other reach the same diagnosis, and both remain `authority-asserted`. Almost everything worth counting is counted per person, so a map of totals is usually a picture of the population distribution with a thin coat of subject matter on it.

Two tests, and a form here needs both.

**Is the geography the finding, or the index?** Where the sentence the reader leaves with is "the south is higher" or "it clusters along the river," geography is the finding. Where it is "these five are highest" or "it doubled since 2019," geography is only how the values were looked up, and the map is a lookup table with a legend in the way.

**Would the pattern survive being written down as a list of regions?** A map earns its place when the answer is no, because the pattern is contiguity, gradient, or proximity to something else on the map. Where a sorted list of region names carries the same message, the map adds nothing the list does not already hold.

Where either test fails, the question belongs to another group:

| The reader's actual question | Group |
|---|---|
| Which regions are highest, and in what order? | Ranking. A sorted bar chart, region names as labels |
| How big is each of these? | [Magnitude](magnitude.md). A [bar chart](bar-chart.md) |
| How did this change? | [Change over time](change-over-time.md). A line chart, or map the change itself |
| Do two variables move together across regions? | [Correlation](correlation.md). A [scatterplot](scatterplot.md), one point per region |
| How are the regional values spread? | [Distribution](distribution.md). A histogram of the values, not of the map |
| How far is each region from a target? | Deviation. A diverging bar off that reference |
| Is there a geographic pattern a list of regions would not show? | **This group** |

## What this group costs

**The plane is already spoken for.** In every other group the two positional dimensions are free to carry the values, and position along a common scale is the most accurately read channel measured ([channels.md](../concepts/channels.md)). On a map, x and y are longitude and latitude. Whatever the figure came to show has to go onto what is left: fill color, mark area, or counted marks.

[Bertin](../people/jacques-bertin.md) rates the two planar dimensions above every retinal variable because the plane is the only one carrying every perceptual property he tracks. A map spends it before anything else has been drawn. `authority-asserted`; there are no experiments in Bertin.

**And the area on the page belongs to the base geography, not to the data.** A region's share of the reader's visual field is fixed by how much land it covers. Large empty regions dominate the image and small dense ones can vanish, and neither fact is about the variable. That much is definitional: it follows from what the mark is. **Whether it measurably biases the conclusions readers draw is not tested in this corpus.** The weighting is certain; the effect on judgment is unmeasured. It is the reason for the rates-not-totals rule below, and it is the reason the [cartogram](cartogram.md) exists.

**No study in this corpus tests any map.** Not a choropleth, not a cartogram, not a dot map. [Heer & Bostock (2010)](../studies/heer-bostock-2010.md) names cartograms as a motivation for its rectangle experiment and then measures abstract rectangles; there is no map anywhere in its stimulus set. So the FT taxonomy has a Spatial family and the evidence base behind this wiki has no experiment in it at all. Everything on the pages below is definitional, inherited at the channel level, or `authority-asserted` from the FT and Urban.

## Choosing a form

| Form | What carries the value | Defined for |
|---|---|---|
| [Choropleth](choropleth-map.md) | Fill color of a fixed region | The value is a **rate** that makes sense as a property of every point in the region, and the reader thinks in those region boundaries |
| [Cartogram](cartogram.md) | Area of a distorted region | The value is a **total**, and the mismatch between land area and where the quantity actually is *is* the message |
| [Dot density](dot-density-map.md) | Number of dots per unit area | The value is a **count** and the locations within each region are known |
| Proportional symbol map *(no page here)* | Area of a symbol on the map | The value is a **total**, at points or region centroids. FT: "Use for totals rather than rates" |
| [Flow map](flow-map.md) | Width of a line between two places | The value is a **movement** between places, and where those places sit is part of the message. FT: "For showing unambiguous movement across a map" |

**Rates versus totals.** The FT states both halves: the basic choropleth "should always be rates rather than totals and use a sensible base geography", the proportional symbol map is for "totals rather than rates". `authority-asserted` as published.

The reasoning behind it is structural, and it says when the rule generalizes. **On a choropleth the mark is the region, and its area takes no input from the data.** On a proportional symbol map the mark is a symbol whose area is set by the value, and geography only decides where it sits. A total is extensive: double the territory and the count tends to double, so it needs a mark that can grow. A rate is intensive: it is a property of every point inside the region rather than of the region's extent, so it survives being painted uniformly across an area the data did not choose. A total painted across a fixed polygon makes two claims at once, that the count is spread evenly through the region and that its importance is proportional to the region's land area, and neither is in the data. **That reasoning is definitional. What is not established is whether readers actually draw wrong conclusions from it**, which no study here tests.

Three constraints that come from the sources rather than from taste:

- **The projection is named, and equal-area wherever area is the message** (inventory topic 21). Urban: "US maps for print publication should use the Albers Equal Area projection." `authority-asserted`. On a choropleth area is not supposed to be the message, and it weights the reader's impression anyway, so an equal-area projection is necessary and nowhere near sufficient.
- **The colormap class matches the data type, and the diverging midpoint is set rather than inherited** (topics 23 and 32). Urban: "The center of the diverging palette should always be labeled to avoid confusing the reader." A diverging ramp whose midpoint landed wherever the data's mean fell asserts a threshold nobody chose.
- **The palette is checked against color-vision deficiency rather than by eye** (topic 26). Datawrapper ships a checker that "warns you if the colors in your chart/map would not be distinguishable by those with any of the three main types of color vision deficiency" ([datawrapper-academy.md](../sources/datawrapper-academy.md)).

Schwabish's *Better Data Visualizations* files Choropleth, Cartogram, Proportional Symbol and Dot Density together under **Geospatial**, which lines up with the FT's Spatial more cleanly than any other pair of their categories. Memberships are verified from the book's contents pages; his prose is unread, so this says where he files these forms and nothing about what he argues ([schwabish.md](../sources/schwabish.md)).

## Justifying the choice

**Defensible, evidence-backed:**

- "The exact values are in the table and the map is there for the geographic pattern. Whatever a map puts the value on, fill color or mark area, is read less accurately than position, measured and replicated." That is inherited from [channels.md](../concepts/channels.md), and the step from this figure to that channel is conjecture, as it is for every chart type.

Nothing else belongs in this bucket. No study in this corpus tests a map.

**Defensible, with the label said out loud:**

- "A map, because the pattern is contiguous and a ranked list would hide it. The FT's own definition is 'Used only when precise locations or geographical patterns in data are more important to the reader than anything else', and that condition holds here." Practitioner rule, not a measured one.
- "Rates rather than totals on the choropleth, and the denominator is in the subtitle." The FT's rule; the reasoning behind it is structural and the reader effect is untested.
- "Albers Equal Area, named in the caption." Urban's rule for US print maps. `authority-asserted`.

**Commonly repeated, and the evidence does not support it:**

- ~~"A choropleth shows the geographic distribution of the quantity."~~ It shows the distribution of the *rate*, weighted by land area. With a count on it the dark regions are usually the populous ones, which is the population map Urban warns about.
- ~~"An equal-area projection fixes the area problem."~~ It fixes the projection's contribution to it. It does nothing about the fact that Wyoming occupies far more of the page than New Jersey while holding far fewer people.
- ~~"The ranking of channels proves readers misread maps."~~ The ranking was measured on stripped proportional-judgment tasks with no map in the stimulus set. Anything a map takes from it is inheritance.

## The failure mode this group invites

**Drawing the population map.** It is the single most common outcome in this family and it is invisible from the inside, because the map looks informative and the data is real. The check stated in topic 22: the variable is swapped for raw population and redrawn. If the two pictures look much the same, the first one was population.

**The map that is really a table.** Where the reader's job is to find their own region and read its value off a legend, the task is a lookup through a color scale.

## Types in this index

- [choropleth-map.md](choropleth-map.md)
- [cartogram.md](cartogram.md)
- [dot-density-map.md](dot-density-map.md)
- [flow-map.md](flow-map.md), the one form here that draws a movement rather than a state, and the only page in this index that also belongs to [flow.md](flow.md)

Proportional symbol maps, hex and tile grid maps and heat maps over geography all belong to this group and none has a page here, because no study in this corpus tests any of them and the practitioner material available is a single line each.

## See also

- [../concepts/channels.md](../concepts/channels.md) — the channel a map leaves for the data, and what "color is the worst channel" actually means
- [../sources/ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md) — the "used only when" definition and the per-type glosses
- [../inventory.md](../inventory.md) — topics 21 (projection), 22 (is a map the right idiom), 23 (colormap class) and 32 (diverging midpoint)
- [README.md](README.md) — the page template and the inheritance rule
