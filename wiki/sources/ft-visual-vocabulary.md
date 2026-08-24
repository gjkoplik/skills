# FT Visual Vocabulary

**What it is.** A poster and companion repository from the Financial Times Visual Journalism Team that organizes about seventy chart types under **nine data relationships**, so that chart choice starts from what you are showing rather than from a menu of shapes.

**Status.** `primary-read`, with one scope note. The `visual-vocabulary` README in the `Financial-Times/chart-doctor` repository was fetched and converted locally, retrieved 2026-08-23. That README states it carries "The full content of the poster, along with links to related material", and it does contain every category, every chart type, and every one-line gloss. **The PDF poster itself was not opened**, so any claim about the poster's layout or visual design is not vouched here.

**What it is good for.** The taxonomy. It is the answer to "what family of chart does this question call for", and it is the only source in this corpus organized that way. The per-chart glosses are one line each and are unusually sharp.

**What it does not settle.** Nearly everything else. No color guidance, no typography, no accessibility, no annotation, no layout. It says so itself. It is also **copyright, all rights reserved** by The Financial Times Limited, unlike the openly licensed material elsewhere in this wiki, so it can be cited but not copied.

---

## The nine relationships

Each carries a definition and example FT uses. These are the categories, with the definitions verbatim where they do work:

**Deviation.** "Emphasise variations (+/-) from a fixed reference point. Typically the reference point is zero but it can also be a target or a long-term average. Can also be used to show sentiment (positive/neutral/negative)."

**Correlation.** "Show the relationship between two or more variables. Be mindful that, unless you tell them otherwise, many readers will assume the relationships you show them to be causal (i.e. one causes the other)."

**Ranking.** "Use where an item's position in an ordered list is more important than its absolute or relative value. Don't be afraid to highlight the points of interest."

**Distribution.** "Show values in a dataset and how often they occur. The shape (or 'skew') of a distribution can be a memorable way of highlighting the lack of uniformity or equality in the data."

**Change over Time.** "Give emphasis to changing trends. These can be short (intra-day) movements or extended series traversing decades or centuries. Choosing the correct time period is important to provide suitable context for the reader."

**Part-to-whole.** "Show how a single entity can be broken down into its component elements. If the reader's interest is solely in the size of the components, consider a magnitude-type chart instead."

**Magnitude.** "Show size comparisons. These can be relative (just being able to see larger/bigger) or absolute (need to see fine differences). Usually these show a 'counted' number (for example, barrels, dollars or people) rather than a calculated rate or per cent."

**Spatial.** "Used only when precise locations or geographical patterns in data are more important to the reader than anything else."

**Flow.** "Show the reader volumes or intensity of movement between two or more states or conditions. These might be logical sequences or geographical locations."

Two of those definitions are doing more than categorizing.

**Correlation carries a warning about the reader's inference,** not about the chart. That is a different kind of rule from anything else in this corpus: it is about what the audience will conclude regardless of what you drew.

**Part-to-whole and Magnitude are defined against each other.** "If the reader's interest is solely in the size of the components, consider a magnitude-type chart instead." The taxonomy is explicit that the same data can sit in two families and the *question* decides. This is the whole argument for organizing by relationship rather than by data shape.

**Spatial says "used only when",** which is inventory topic 22 embedded in the taxonomy itself.

## The stated scope, which is the honest part

> "This is not an attempt to teach everyone how to make charts, but how to recognise the opportunities to use them effectively alongside words."

That sentence is why the Visual Vocabulary is worth a page and why it should not be cited for much. It is a recognition aid for a newsroom-wide chart-literacy training session, not a quality bar. Inventory topics 5 and 4 draw on it; nothing else should.

The lineage is credited: "inspired by the Graphic Continuum by Jon Schwabish and Severino Ribecca."

## The one-line glosses are the underrated part

A sample, chosen because each one encodes a real constraint in about ten words:

- **Column** (Magnitude): "The standard way to compare the size of things. **Must always start at 0 on the axis**"
- **Lollipop chart** (Magnitude): "Lollipop charts draw more attention to the data value than standard bar/column -- **does not HAVE to start at zero (but preferable)**"
- **Isotype (pictogram)**: "use only with whole numbers (do not slice off an arm to represent a decimal)"
- **Histogram**: "keep the gaps between columns small to highlight the 'shape' of the data"
- **Stacked column**: "A simple way of showing part-to-whole relationships but can be difficult to read with more than a few components."
- **Area chart**: "Use with care -- these are good at showing changes to total, but seeing change in components can be very difficult"
- **Basic choropleth**: "should always be rates rather than totals and use a sensible base geography"
- **Proportional symbol (map)**: "Use for totals rather than rates"
- **Dot density**: "make sure to annotate any patterns the reader should see"
- **Radar chart**: "make sure they are organised in a way that makes sense to reader"
- **Venn**: "Generally only used for schematic representation"

Note the column/lollipop pair. The FT applies the zero baseline **by mark**, capitalizes "always" for the filled column and "HAVE" for the negation on the lollipop. Same reasoning as Datawrapper's dot-plot remedy and Observable Plot's radius-only enforcement: the constraint follows from whether length or area encodes the value, not from the axis being quantitative. Three sources reaching that independently is the strongest form inventory topic 9 takes.

## The FT ships the argument, not a ruling

Under **Line** and **Column** in Change over Time, the further-reading links include, in the same list:

- ONS, "Does the axis have to start at zero? (Part 1 -- line charts)" and "(Part 2 -- bar charts)"
- Quartz, "It's OK not to start your y-axis at zero"
- Vox, "Shut up about the y-axis. It shouldn't always start at zero"
- Emily Schuch, "How to Make a Line Chart that Doesn't Lie"

Under **Line + Column** and **Connected scatterplot**, it links two separate pieces cautioning about dual axes plus HBR on spurious correlations. Under **Pie**, it links eight items including Kosara's pie-chart studies, Spence's history, "In defense of pie charts", and Few's "Save the Pies for Dessert" -- both sides, at length.

A style guide that links to the argument instead of settling it is doing something different from the BBC's or Urban's. Whether that is a virtue depends on the reader: it is excellent for someone building a rulebook and useless for someone who wanted a rule. For the topics where this wiki finds the evidence genuinely contested (zero baselines, dual axes, chartjunk; see [refutations.md](../refutations.md)), the FT's refusal to rule looks like the better call in retrospect.

## The gap: uncertainty is a TODO

At the bottom of the README, after all nine categories, sit four unfinished sections:

```
Todo:
### Uncertainty
### Animation
### Interactivity
### Map projections
### Colour
```

**The FT taxonomy has no uncertainty family.** A fan chart appears under Change over Time ("Use to show the uncertainty in future projections") and a box plot and violin under Distribution, but there is no relationship category for "this value is not known precisely", and the section that would create one is a stub.

That is worth recording, because inventory topic 8 (directory-of-visualization coverage) explicitly requires a general bar to say something about **uncertainty** alongside amounts, distributions, proportions, x-y relationships and geospatial data. The most widely circulated chart-selection taxonomy in the field does not have a slot for it. That is some evidence that the topic's under-coverage is a property of the field rather than of any one guide. The statistical-reporting canon fills the gap, and [refutations.md](../refutations.md) records that it was not in this project's original source set either.

## Practical notes

- There are D3 templates in FT style in a separate repository, `ft-interactive/visual-vocabulary`. Same config-beats-prose pattern as `bbplot` and `urbnthemes` (see [bbc-cookbook.md](bbc-cookbook.md), [urban-institute.md](urban-institute.md)), in a different language.
- The poster exists in English, Japanese, traditional Chinese, and simplified Chinese.
- The README labels its own related-reading section "_This is a work in progress._"
- **Licensing:** "Copyright © The Financial Times Limited, all rights reserved." Cite and link. Do not reproduce the poster.

## Where this source is used

Inventory topics 4, 5, 21, 22, 50, 54, 79. See [roll-call.md](../roll-call.md), which maps all nine categories to topic 5 collectively.

## Links

- [Financial-Times/chart-doctor: visual-vocabulary](https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary)
- [Visual Vocabulary poster (PDF)](https://github.com/ft-interactive/chart-doctor/blob/master/visual-vocabulary/Visual-vocabulary.pdf)
- [Interactive web version](http://ft-interactive.github.io/visual-vocabulary/)
- [Graphic Continuum](https://policyviz.com/2014/09/09/graphic-continuum/), the acknowledged inspiration
