---
type: index
---

# Spatial

Data drawn at geographic positions, so that *where* a value sits is part of what the reader takes away.

## Is geography the question, or an available column?

The FT writes this category's definition as a restriction ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)):

> "Used only when precise locations or geographical patterns in data are more important to the reader than anything else."

Most categories in that taxonomy state what the family shows. This one, like Ranking, states when it applies. `authority-asserted`.

The Urban Institute style guide, by [Jonathan Schwabish](../people/jonathan-schwabish.md), states the same test as a diagnosis (inventory topic 22): "If the map only shows where people live, it is a population map." Munzner's course slides, an unrelated source, give "most attributes just show where people live" as the choropleth failure and add "visual salience depends on region size, not true importance wrt attribute value" ([munzner-vad.md](../sources/munzner-vad.md), read from the 2021 slide deck rather than the book). Both are `authority-asserted`. Almost everything worth counting is counted per person, so a map of totals is usually a map of population.

Two tests, and a form here needs both.

**Is the geography the finding, or the index?** Where the reader leaves with "the south is higher" or "it clusters along the river," geography is the finding. Where it is "these five are highest" or "it doubled since 2019," geography is only how the values were looked up, and the map is a lookup table with a legend in the way.

**Would the pattern survive being written down as a list of regions?** A map earns its place when it would not, because the pattern is contiguity, gradient, or proximity to something else on the map.

Where either test fails:

| The reader's question | Group |
|---|---|
| Which regions are highest, and in what order? | Ranking. A sorted bar chart, region names as labels |
| How big is each of these? | [Magnitude](magnitude.md). A [bar chart](bar-chart.md) |
| How did this change? | [Change over time](change-over-time.md). A line chart, or map the change itself |
| Do two variables move together across regions? | [Correlation](correlation.md). A [scatterplot](scatterplot.md), one point per region |
| How are the regional values spread? | [Distribution](distribution.md). A histogram of the values, not of the map |
| How far is each region from a target? | Deviation. A diverging bar off that reference |
| Is there a geographic pattern a list of regions would not show? | **This group** |

## What this group costs

**The plane.** Elsewhere the two positional dimensions carry the values, and position along a common scale is the most accurately read channel measured ([channels.md](../concepts/channels.md)). On a map, x and y are longitude and latitude, and the data goes onto what is left: fill color, mark area, or counted marks. [Bertin](../people/jacques-bertin.md) rates the planar dimensions above every retinal variable because only the plane carries every perceptual property he tracks. A map spends it first. `authority-asserted`, and there are no experiments in Bertin.

**Area on the page.** A region's share of the image is fixed by its land area, not by the data. Large empty regions dominate and small dense ones can vanish. That is definitional, and whether it biases readers' conclusions is untested here. It motivates the rates-not-totals rule below and the [cartogram](cartogram.md).

No study in this corpus tests any map. [Heer & Bostock (2010)](../studies/heer-bostock-2010.md) names cartograms as a motivation for its rectangle experiment, then measures abstract rectangles with no map in the stimulus set. Everything on the pages below is definitional, inherited at the channel level, or `authority-asserted` from the FT and Urban.

## Choosing a form

| Form | What carries the value | Defined for |
|---|---|---|
| [Choropleth](choropleth-map.md) | Fill color of a fixed region | The value is a **rate** that makes sense as a property of every point in the region, and the reader thinks in those region boundaries |
| [Cartogram](cartogram.md) | Area of a distorted region | The value is a **total**, and the mismatch between land area and where the quantity is *is* the message |
| [Dot density](dot-density-map.md) | Number of dots per unit area | The value is a **count** and the locations within each region are known |
| Proportional symbol map *(no page here)* | Area of a symbol on the map | The value is a **total**, at points or region centroids. FT: "Use for totals rather than rates" |
| [Flow map](flow-map.md) | Width of a line between two places | The value is a **movement** between places, and where those places sit is part of the message. FT: "For showing unambiguous movement across a map" |

**Rates versus totals.** The FT says the basic choropleth "should always be rates rather than totals and use a sensible base geography", and the proportional symbol map is for "totals rather than rates". `authority-asserted` as published.

The structural reasoning says when the rule generalizes. On a choropleth the mark is the region, and its area takes no input from the data. On a proportional symbol map the value sets the symbol's area. A total is extensive (double the territory and the count tends to double), so it needs a mark that can grow. A rate is intensive, a property of every point in the region, so it survives being painted uniformly across an area the data did not choose. A total painted on a fixed polygon claims that the count is spread evenly through the region and that its importance scales with land area, and the data says neither. That is definitional, and the effect on readers is untested.

Three constraints come from the sources:

- **The projection is named, and equal-area wherever area is the message** (inventory topic 21). Urban: "US maps for print publication should use the Albers Equal Area projection." `authority-asserted`. Area weights a choropleth reader's impression anyway, so equal-area is necessary and far from sufficient.
- **The colormap class matches the data type, and the diverging midpoint is set rather than inherited** (topics 23 and 32). Urban: "The center of the diverging palette should always be labeled to avoid confusing the reader." A midpoint that landed on the data's mean asserts a threshold nobody chose.
- **The palette is checked against color-vision deficiency, not by eye** (topic 26). Datawrapper ships a checker that "warns you if the colors in your chart/map would not be distinguishable by those with any of the three main types of color vision deficiency" ([datawrapper-academy.md](../sources/datawrapper-academy.md)).

Schwabish's *Better Data Visualizations* files Choropleth, Cartogram, Proportional Symbol and Dot Density under Geospatial, the closest match between any of his categories and the FT's ([schwabish.md](../sources/schwabish.md); contents pages only, prose unread).

## Justifying the choice

**Defensible, evidence-backed:**

- "The exact values are in the table and the map is there for the geographic pattern. Whatever a map puts the value on, fill color or mark area, is read less accurately than position, measured and replicated." Inherited from [channels.md](../concepts/channels.md). The step from this figure to that channel is conjecture, as it is for every chart type.

Nothing else belongs in this bucket.

**Defensible, with the label said out loud:**

- "A map, because the pattern is contiguous and a ranked list would hide it. The FT's own definition is 'Used only when precise locations or geographical patterns in data are more important to the reader than anything else', and that condition holds here." Practitioner rule, not a measured one.
- "Rates rather than totals on the choropleth, and the denominator is in the subtitle." The FT's rule, with structural reasoning and an untested reader effect.
- "Albers Equal Area, named in the caption." Urban's rule for US print maps. `authority-asserted`.

**Commonly repeated, and the evidence does not support it:**

- ~~"A choropleth shows the geographic distribution of the quantity."~~ It shows the distribution of the *rate*, weighted by land area. With a count on it, the dark regions are usually the populous ones.
- ~~"An equal-area projection fixes the area problem."~~ Only the projection's share. Wyoming still takes far more of the page than New Jersey while holding far fewer people.
- ~~"The ranking of channels proves readers misread maps."~~ The ranking was measured on stripped proportional-judgment tasks with no map in the stimulus set. A map only inherits it.

## The failure mode this group invites

**Drawing the population map.** It is the most common outcome in this family, and it looks informative because the data is real. The check in topic 22 swaps the variable for raw population and redraws. If the two pictures look much the same, the first one was population.

**The map that is really a table.** Where the reader's job is to find their own region and read its value off a legend, the task is a lookup through a color scale.

## Types in this index

- [choropleth-map.md](choropleth-map.md)
- [cartogram.md](cartogram.md)
- [dot-density-map.md](dot-density-map.md)
- [flow-map.md](flow-map.md): draws a movement rather than a state, and is also indexed under [flow.md](flow.md)

Proportional symbol maps, hex and tile grid maps and heat maps over geography belong here and have no page. No study in this corpus tests them, and the practitioner material is a single line each.

## See also

- [../concepts/channels.md](../concepts/channels.md): the channel a map leaves for the data, and what "color is the worst channel" means
- [../sources/ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md): the "used only when" definition and the per-type glosses
- [../inventory.md](../inventory.md): topics 21 (projection), 22 (is a map the right idiom), 23 (colormap class) and 32 (diverging midpoint)
- [README.md](README.md): the page template and the inheritance rule
