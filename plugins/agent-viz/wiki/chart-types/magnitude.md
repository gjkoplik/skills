---
type: index
---

# Magnitude

Size comparisons among items: how big each one is, and how it stands against the others.

## Before anything: does this need a chart?

[Part-to-whole](part-to-whole.md) asks the same question, and it matters more here, since a magnitude question is often about one number. The Urban Institute style guide, by [Jonathan Schwabish](../people/jonathan-schwabish.md) ([urban-institute.md](../sources/urban-institute.md)):

> "You may also find that simply including a single, large number (commonly known as 'big aggregate numbers') may be sufficient."

Where the sentence under the chart reads "sales were 4.2 million," and the other bars only keep that bar company, the sentence carries the content. `authority-asserted`. No experiment compares a big number against a bar.

## Is magnitude the right frame?

The FT defines this family and part-to-whole against each other ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)):

> "Show size comparisons. These can be relative (just being able to see larger/bigger) or absolute (need to see fine differences). Usually these show a 'counted' number (for example, barrels, dollars or people) rather than a calculated rate or per cent."

and, from the part-to-whole entry: "If the reader's interest is solely in the size of the components, consider a magnitude-type chart instead." `authority-asserted`, and a family description rather than a rule. Rates in a bar chart are fine.

**Is the comparison across items, or within one item?** Across items is this group. Within one item, it is change over time or part-to-whole.

**Does the reader need the size, or the position in an order?** The size is magnitude. "Which three are on top" is ranking, which the FT says applies "where an item's position in an ordered list is more important than its absolute or relative value." Getting this one wrong costs little, since both groups mostly produce the same sorted bar chart. The consequential errors are the others:

| The reader's actual question | Group |
|---|---|
| Does this add up, and to what? | [Part-to-whole](part-to-whole.md) |
| How is this value spread across observations? | [Distribution](distribution.md). A histogram, or a univariate scatterplot |
| How did this move over time? | [Change over time](change-over-time.md). A line chart |
| How far is each item above or below a reference? | [Deviation](deviation.md). A [diverging bar](diverging-bar-chart.md) off that reference |
| Do these two variables move together? | [Correlation](correlation.md). A scatterplot |
| Where is this? | [Spatial](spatial.md) |
| How big are these, side by side? | **This group** |

## What this group costs

The canonical chart puts the value on position along a common scale, the most accurately read channel, measured and replicated ([channels.md](../concepts/channels.md)). This group is the baseline the others are measured against. Its costs sit elsewhere.

**Item count.** Datawrapper documents that bar charts, dot plots, range plots and arrow plots cannot have their height set, because the row count determines it ([datawrapper-academy.md](../sources/datawrapper-academy.md)). A forty-item bar chart does not fit on a phone by resizing, which is not true of a treemap.

**Zero baseline.** A filled mark binds one, scoped by mark rather than axis (below).

**No whole.** Where "and that is all of it" is part of the claim, the question is part-to-whole, at that group's accuracy cost.

## Choosing a form

| Form | What carries the value | Defined for |
|---|---|---|
| [Bar chart](bar-chart.md) | The end of a filled bar, on a common scale | The default, and the best-evidenced form here. Few enough categories to label |
| [Lollipop chart](lollipop-chart.md) | A point at the value, with a stem for orientation | Many categories, where filled bars become a block of ink. Untested as a form |
| [Stacked bar](stacked-bar.md) | Segment length. The total reads as position | The total is the magnitude *and* its composition matters |
| [Treemap](treemap.md) | Rectangular area | Hundreds of items at once, where approximate sizes are good enough |
| [Radar chart](radar-chart.md) | Radial distance on each item's own axis | Several measures profiling one entity. Nothing in this corpus evaluates it |
| [Heatmap](heatmap.md) | Cell color, on a grid whose two axes carry keys rather than values | Two keys, one value per pair, and the pattern across the grid matters more than any cell. Unmeasured |
| [Gauge and bullet](gauge-and-bullet.md) | Angular position inside an arc, or a bar's length against a reference marker | One value against a target and a band of context. The style guides' alternative is the number itself |

Isotype and pictogram charts, proportional symbols and grouped bars have no page, for want of any study to hang one on.

- **Sorting** is by value, or by a stated logic. The BBC cookbook treats alphabetical order as a bug: it is "what R will display by default," fixed by wrapping `reorder()` ([bbc-cookbook.md](../sources/bbc-cookbook.md)). Urban treats ordering as an editorial act, noticed or not. `authority-asserted`.
- **The zero baseline** is scoped by mark, not by axis. A filled bar encodes the value as length from the baseline, so moving the baseline rescales the encoding. A dot or a line does not. Urban states both halves: bar axes "should always start at zero," and "other charts types that do not use length or height as the primary encoding -- including, for example, scatterplots and line charts -- do not necessarily need to start at zero." The FT also rules per mark, "Must always start at 0" for the column against "does not HAVE to start at zero (but preferable)" for the lollipop. Observable Plot forces zero only where area encodes the value. [Vega-Lite](../sources/vega-lite.md) is the outlier, defaulting `zero: true` on every quantitative positional scale regardless of mark, the by-axis reading and the weaker one. `authority-asserted`, with the harm from getting it wrong evidence-backed.
- **Area and color** read magnitude less accurately than position, measured ([channels.md](../concepts/channels.md)). A [treemap](treemap.md) buys something with the area trade and a [heatmap](heatmap.md) buys a cross-tabulation with color. A bubble chart of eight values, or a single-key heatmap, buys nothing.

## Justifying the choice

**Defensible, evidence-backed:**

- "This is a bar chart because the reader has to read values off it. Position along a common scale is the most accurately read channel, measured and replicated."
- "I did not truncate the value axis. In a controlled test, truncating a bar axis moved readers' judgments 91% against the same data drawn honestly."
- "These are individual observations rather than bars of the mean, because at n = 5 the bar and the error bar are compatible with distributions that support opposite conclusions."

**Defensible, with the label said out loud:**

- "Bars are sorted by value rather than alphabetically. That is practitioner consensus, not a measured result, and the alternative is the order the dataframe happened to be in."
- "The zero baseline binds here because the mark is filled. Every style guide in this corpus scopes it that way, and none of them ran an experiment on the rule itself. One plotting library disagrees and forces zero on all positional scales."

**Commonly repeated, and the evidence does not support it:**

- ~~"Every quantitative axis should start at zero."~~ The scoping is by mark. [Correll, Bertini & Franconeri (2020)](../studies/correll-2020-truncating-the-y-axis.md) refuse the maximalist version: "we resist the interpretation... that all charts with quantitative axes should include 0... We reject the unequivocal dichotomy of 'honest' and 'dishonest' charts."
- ~~"An axis-break glyph makes truncation honest."~~ The two designs tested did not measurably reduce the exaggeration. [refutations.md](../refutations.md#axis-break-glyphs-as-the-truncation-remedy) covers why "placebo" overstates it.

## The failure mode this group invites

**Being the default.** The bar chart is what gets drawn when nobody decided anything, so this group absorbs questions that belong to distribution, uncertainty and change over time. [Weissgerber et al. (2015)](../studies/weissgerber-2015-beyond-bar-line.md) measured it in one field, bar graphs of the mean over continuous data. Of 703 physiology articles, 85.6% included a bar graph, the median minimum group size in a figure was 4, and "many different data distributions can lead to the same bar or line graph." Evidence-backed as a prevalence finding and as an argument. No one was tested on what they concluded.

**A bar height that is a statistic rather than a count.** A bar of a mean, a median, a rate or a model coefficient is a summary standing in for a distribution, and the form gives the reader no way to tell which one they are looking at.

## Types in this index

- [bar-chart.md](bar-chart.md)
- [gauge-and-bullet.md](gauge-and-bullet.md): two forms for one value against a reference, filed together by Schwabish
- [heatmap.md](heatmap.md): also correlation and spatial. One scheme files it under comparison, another splits it in two
- [lollipop-chart.md](lollipop-chart.md)
- [radar-chart.md](radar-chart.md)
- [stacked-bar.md](stacked-bar.md): also part-to-whole and change over time
- [treemap.md](treemap.md): also part-to-whole
- [cartogram.md](cartogram.md): a total as area, like a treemap. Primarily [spatial.md](spatial.md)
- [waffle-chart.md](waffle-chart.md): a count of cells rather than a judgment of size. Primarily [part-to-whole.md](part-to-whole.md)
- [marimekko-chart.md](marimekko-chart.md): here for its bar widths. Primarily part-to-whole

## See also

- [../concepts/channels.md](../concepts/channels.md): the evidence these pages inherit, and the conjecture in the inheritance
- [README.md](README.md): the page template and the inheritance rule
- [part-to-whole.md](part-to-whole.md): the group this one is defined against
