---
type: chart-type
relationships: [change-over-time, part-to-whole, distribution]
aliases: [Facets, Faceted chart, Lattice plot, Panel chart, Small multiples, Trellis display, Trellis plot]
---

# Small multiples

One chart repeated once per level of a categorical variable, as a grid of panels at shared scales, so groups are compared across panels instead of untangled from one overlay.

The term is Tufte's, his chapter 8 ([tufte.md](../sources/tufte.md), `secondary-only`), and the practice is older: Nightingale's 1858 plate is two panels on one area scale ([edward-tufte.md](../people/edward-tufte.md)). Becker, Cleveland and Shyu called it trellis display ([william-cleveland.md](../people/william-cleveland.md)), Munzner's slides list "small multiples" and "trellis plots" under Facet into Multiple Views ([munzner-vad.md](../sources/munzner-vad.md)), and ggplot2 calls it faceting ([bbc-cookbook.md](../sources/bbc-cookbook.md)). Schwabish files it as a guideline: "Small Multiples (or, as I call it in the book, Avoid the Spaghetti Chart)" ([schwabish.md](../sources/schwabish.md)).

## When to reach for it, and when not

The device is defined for a chart that already works for one group, a categorical variable with more levels than one overlay can keep apart, and a question about how the groups differ in shape, trend or composition. It is a composition device, not a mark: each panel does what its chart does, and the device adds a split, a scale decision and a reading order. It is indexed under [change over time](change-over-time.md) as the usual remedy for spaghetti ([line-chart.md](line-chart.md)), [part-to-whole](part-to-whole.md) because two pies cannot be compared ([pie-and-donut.md](pie-and-donut.md)), and [distribution](distribution.md) because overlaid shapes hide each other.

| The question | Alternative |
|---|---|
| One series is the subject, the rest context | One [line chart](line-chart.md), the rest gray and the subject in an accent. Urban's recommendation, untested |
| What is the exact gap between two groups at each point? | Both in one panel, or a chart of the difference. Panels put the two values on separate axes |
| Which group is largest? | A sorted bar chart ([ranking](ranking.md)). One-number panels are a bar chart cut apart |
| Thirty ordered groups, and only the shape moves | [Ridgeline plot](ridgeline-plot.md), which overlaps the panels to fit them |
| Two variables in different units over the same time | Two stacked panels sharing an x-axis ([correlation.md](correlation.md)), the same device split over variables |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per observation, plus one categorical variable to split on (wrapped into a grid) or two (rows and columns) |
| Transform | The split: rows partitioned by level, then the panel chart's own transform once per panel |
| Geometry | The panel chart's mark, repeated |
| Scale | Shared across panels by default, or free per panel, on each positional axis and on color. The shared-or-free choice lives here |
| Coordinates | The panel chart's, tiled. Panel position is layout, not data, unless a variable places the panels, as in Wilke's per-region panels laid out geographically ([wilke-fundamentals.md](../sources/wilke-fundamentals.md), chapter 15) |
| Guides | One axis per shared row or column, a label naming each panel's level, and a note when scales are free |

Panel order is a free parameter, as a bar chart's sort is.

## Channels

Inside a panel, the panel chart's channels apply. Across panels, two values sit on identical scales that are aligned only within a shared row (vertical axis) or column (horizontal). Elsewhere the comparison is position along nonaligned scales, the rank below a common scale in [channels.md](../concepts/channels.md). An overlay makes the opposite trade: one common scale, with series told apart by hue. The step from mark to channel is conjecture in the source literature, and the ranking measures reading a value, not comparing trends or shapes ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)).

Free scales change what position means from panel to panel, so a cross-panel comparison has to go through the tick labels.

## What is measured

No study in this corpus tests the device. Two nearby results do not transfer. [Cleveland & McGill (1984)](../studies/cleveland-mcgill-1984.md) measured nonaligned position as a judgment between two marks, not as reading a grid. [Isenberg et al. (2011)](../studies/isenberg-2011-dual-scale-charts.md) found a superimposed design lost to a collocated cut-out on accuracy, time and ranking, but each stimulus was two magnifications of one series, not groups split into panels. The trellis paper was not reached.

## The failure mode it invites

**Free scales nobody labeled.** Each panel autoscales and the grid still reads as one scale. The BBC cookbook: "It's always best to use the same y axis scale across small multiples, to avoid misleading, but sometimes you may need to set these independently for each multiple, which we can do by adding the argument `scales = "free"`." Its fixed-scale example shows the opposite cost: "Oceania, with its relatively small population, has disappeared completely" ([bbc-cookbook.md](../sources/bbc-cookbook.md)). [inventory.md](../inventory.md) topic 62 (Urban, the BBC, Wilke chapter 21, Munzner chapter 12) asks for shared axis and color scales and labeled free ones. `authority-asserted`. Color drifts the same way ([choropleth-map.md](choropleth-map.md)), and [checks/matplotlib.md](../checks/matplotlib.md) tests that comparable panels share one color limit.

**Panels in dataframe order.** The grid takes whatever order the grouping produced, and readers take neighbors as related. The BBC notes that "By default, R will display your data in alphabetical order", there about bars. Bertin's reorderable matrix makes the sort the analysis ([jacques-bertin.md](../people/jacques-bertin.md)). Topic 63, from Wilke chapter 21, asks for a title or letter on every panel and a reading order. `authority-asserted`.

**Too many panels to read.** Every added level shrinks every panel, and on a phone the whole grid "might only be 380px or 400px wide" ([datawrapper-academy.md](../sources/datawrapper-academy.md)). No source here gives a panel ceiling. `absence of evidence`.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing on this page qualifies. Inside each panel, the panel chart's inherited channel claims still hold.

**Defensible, with the label said out loud:**

- "Nine series became nine panels on one shared y-axis. Every major source here recommends it, Schwabish calls it 'Avoid the Spaghetti Chart', and no study here compares it with the overlay."
- "The small groups vanished under a shared scale, so these panels use free scales and the subtitle says so."
- "Panels are ordered by the latest value, not alphabetically, and the caption says so."

**Commonly repeated, and the evidence does not support it:**

- ~~"Small multiples beat overlaid lines."~~ The plugin's [quality bar](../../SKILL.md) states "Small multiples beat overlaid spaghetti, at identical scales" as a rule, and its warrant is topic 62, `authority-asserted`.
- ~~"Tufte showed that small multiples work."~~ Tufte ran no experiments ([edward-tufte.md](../people/edward-tufte.md)). That nothing in the record argues against them is `absence of evidence`, not support.
- ~~"Each panel has its own axis, so free scales cannot mislead."~~ Whether readers check tick labels before comparing heights is untested.

## See also

- [line-chart.md](line-chart.md): spaghetti, and the gray-plus-accent alternative
- [ridgeline-plot.md](ridgeline-plot.md): small multiples of densities, overlapped
- [../concepts/channels.md](../concepts/channels.md): common against nonaligned scales
