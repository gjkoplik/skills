---
type: index
---

# Magnitude

Size comparisons among items: how big each one is, and how it stands against the others.

## Before anything: does this need a chart?

Same escape hatch as [part-to-whole](part-to-whole.md), and it bites harder here, because a magnitude question is often a question about *one* number. The Urban Institute style guide, by [Jonathan Schwabish](../people/jonathan-schwabish.md) ([urban-institute.md](../sources/urban-institute.md)):

> "You may also find that simply including a single, large number (commonly known as 'big aggregate numbers') may be sufficient."

Where the sentence under the chart reads "sales were 4.2 million," and the other bars exist so the one bar has company, the sentence carries the content. `authority-asserted`; no experiment compares a big number against a bar.

## Is magnitude the right frame?

The FT defines this family and part-to-whole against each other ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)):

> "Show size comparisons. These can be relative (just being able to see larger/bigger) or absolute (need to see fine differences). Usually these show a 'counted' number (for example, barrels, dollars or people) rather than a calculated rate or per cent."

and, from the part-to-whole entry: "If the reader's interest is solely in the size of the components, consider a magnitude-type chart instead." `authority-asserted`, and a family description rather than a rule. Rates in a bar chart are fine; the note is about which family the question usually lands in.

Two tests:

**Is the comparison across items, or within one item?** Across items, the question is in this group. Within one item, over time or across its parts, the question is change over time or part-to-whole.

**Does the reader need the size, or the position in an order?** The size is a magnitude question. "Which three are on top" is a ranking question, and the FT's own line for ranking is that it applies "where an item's position in an ordered list is more important than its absolute or relative value."

The second test costs almost nothing to get wrong. In part-to-whole, the wrong group lands on a genuinely different chart. Here, magnitude and ranking mostly produce the same object: a bar chart, sorted. The consequential group errors are the other ones.

| The reader's actual question | Group |
|---|---|
| Does this add up, and to what? | [Part-to-whole](part-to-whole.md) |
| How is this value spread across observations? | Distribution. A histogram, or a univariate scatterplot |
| How did this move over time? | Change over time. A line chart |
| How far is each item above or below a reference? | [Deviation](deviation.md). A [diverging bar](diverging-bar-chart.md) off that reference |
| Do these two variables move together? | Correlation. A scatterplot |
| Where is this? | [Spatial](spatial.md) |
| How big are these, side by side? | **This group** |

## What this group costs

This group starts by costing nothing. Every other index in this wiki opens by naming what its forms give up. The canonical magnitude chart spends position along a common scale on the value being asked about, and that is the most accurately read channel there is, measured and replicated ([channels.md](../concepts/channels.md)). This group is the baseline the others are measured against rather than a trade.

The costs are real and they are elsewhere.

**The categorical axis grows with the data and cannot be shrunk.** Datawrapper documents that bar charts, dot plots, range plots and arrow plots cannot have their height set at all, because the row count determines it ([datawrapper-academy.md](../sources/datawrapper-academy.md)). A forty-item bar chart does not fit on a phone by being resized. Item count is a hard design constraint here in a way it is not for a treemap.

**A filled mark binds a zero baseline.** Scoped by mark, not by axis, below. Truncating it is measurably not free.

**The chart shows a summary and nothing behind it.** [Weissgerber et al. (2015)](../studies/weissgerber-2015-beyond-bar-line.md) put numbers on how far that goes in practice: 85.6% of 703 physiology articles included a bar graph, the median minimum group size in a figure was 4, and "many different data distributions can lead to the same bar or line graph." Evidence-backed as a prevalence finding and as an argument; nobody was tested on what they concluded.

**Nothing here asserts a whole.** Where "and that is all of it" is part of the claim, the question is part-to-whole, at the accuracy cost that group charges.

## Choosing a form

| Form | What carries the value | Defined for |
|---|---|---|
| [Bar chart](bar-chart.md) | The end of a filled bar, on a common scale | The default, and the best-evidenced form in this wiki. Few enough categories to label |
| [Lollipop chart](lollipop-chart.md) | A point at the value, with a stem for orientation | Many categories, where filled bars become a block of ink. Untested as a form |
| [Stacked bar](stacked-bar.md) | Segment length; the total reads as position | The total is the magnitude *and* its composition matters |
| [Treemap](treemap.md) | Rectangular area | Hundreds of items at once, and approximate sizes are good enough |
| [Radar chart](radar-chart.md) | Radial distance on each item's own axis | Several measures profiling one entity. Nothing in this corpus evaluates it |
| [Heatmap](heatmap.md) | Cell color, on a grid whose two axes carry keys rather than values | Two keys, one value per pair, and the pattern across the grid matters more than any cell. Unmeasured |
| [Gauge and bullet](gauge-and-bullet.md) | Angular position inside an arc, or a bar's length against a reference marker | One value against a target and a band of context. The style guides' alternative is the number itself |

Isotype and pictogram charts, proportional symbols and grouped bars have no page here, for want of any study to hang one on.

Three constraints that follow from the record rather than from taste:

- **Sorting is by value, or by a stated logic.** The BBC cookbook treats alphabetical order as a bug rather than a choice: it is "what R will display by default," fixed by wrapping `reorder()` ([bbc-cookbook.md](../sources/bbc-cookbook.md)). Urban makes the same point from the other side, that ordering is an editorial act whether or not anyone notices it. `authority-asserted`.
- **The zero baseline is scoped by mark, not by axis.** A filled bar encodes the value with its length from the baseline, so moving the baseline rescales the encoding. A dot or a line does not. Urban states both halves: bar axes "should always start at zero," and "other charts types that do not use length or height as the primary encoding -- including, for example, scatterplots and line charts -- do not necessarily need to start at zero." The FT applies it per mark too, "Must always start at 0" for the column against "does not HAVE to start at zero (but preferable)" for the lollipop. Observable Plot forces zero only where area encodes the value. [Vega-Lite](../sources/vega-lite.md) is the outlier, defaulting `zero: true` on every quantitative positional scale regardless of mark, which is the by-axis reading and the weaker one. `authority-asserted`, with the harm from getting it wrong evidence-backed (below).
- **A magnitude on area or on color, where position is available.** Both are read less accurately than position for magnitude, measured ([channels.md](../concepts/channels.md)). The [treemap](treemap.md) buys something specific with the area trade and the [heatmap](heatmap.md) buys a whole cross-tabulation with the color trade; a bubble chart of eight values, or a single-key heatmap, buys nothing.

## Justifying the choice

**Defensible, evidence-backed:**

- "This is a bar chart because the reader has to read values off it. Position along a common scale is the most accurately read channel, measured and replicated."
- "I did not truncate the value axis. In a controlled test, truncating a bar axis moved readers' judgments 91% against the same data drawn honestly."
- "These are individual observations rather than bars of the mean, because at n = 5 the bar and the error bar are compatible with distributions that support opposite conclusions."

**Defensible, with the label said out loud:**

- "Bars are sorted by value rather than alphabetically. That is practitioner consensus, not a measured result, and the alternative is the order the dataframe happened to be in."
- "The zero baseline binds here because the mark is filled. Every style guide in this corpus scopes it that way, and none of them ran an experiment on the rule itself. One plotting library disagrees and forces zero on all positional scales."

**Commonly repeated and not supported:**

- ~~"Every quantitative axis should start at zero."~~ The scoping is by mark. [Correll, Bertini & Franconeri (2020)](../studies/correll-2020-truncating-the-y-axis.md) explicitly refuse the maximalist version: "we resist the interpretation... that all charts with quantitative axes should include 0... We reject the unequivocal dichotomy of 'honest' and 'dishonest' charts."
- ~~"An axis-break glyph makes truncation honest."~~ The two designs tested did not measurably reduce the exaggeration. See [refutations.md](../refutations.md#axis-break-glyphs-as-the-truncation-remedy), including why "placebo" overstates it.

## The failure mode this group invites

**Being the default.** The bar chart is what gets drawn when nobody decided anything, which means this group absorbs questions that belong to distribution, to uncertainty, and to change over time. Weissgerber's 85.6% is that failure measured in one field: bar graphs of the mean, over continuous data, at sample sizes of four.

**A bar height that is a statistic rather than a count is hiding something.** A bar of a mean, a median, a rate or a model coefficient is a summary standing in for a distribution, and the form gives the reader no way to tell which one they are looking at.

## Types in this index

- [bar-chart.md](bar-chart.md)
- [gauge-and-bullet.md](gauge-and-bullet.md), two forms for one value against a reference, filed together by Schwabish
- [heatmap.md](heatmap.md), which is also read as correlation and as spatial, and which one scheme files under comparison while another splits it in two
- [lollipop-chart.md](lollipop-chart.md)
- [radar-chart.md](radar-chart.md)
- [stacked-bar.md](stacked-bar.md), which is also part-to-whole and change over time
- [treemap.md](treemap.md), which is also part-to-whole
- [cartogram.md](cartogram.md), which encodes a total as area like a treemap does, and is indexed primarily under [spatial.md](spatial.md)
- [waffle-chart.md](waffle-chart.md), where the reading is a count of cells rather than a judgment of size, and which is indexed primarily under [part-to-whole.md](part-to-whole.md)
- [marimekko-chart.md](marimekko-chart.md), which is here for its bar widths and is indexed primarily under [part-to-whole.md](part-to-whole.md)

## See also

- [../concepts/channels.md](../concepts/channels.md) — the evidence these pages inherit, and the conjecture in the inheritance
- [README.md](README.md) — the page template and the inheritance rule
- [part-to-whole.md](part-to-whole.md) — the group this one is defined against
