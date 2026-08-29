---
type: source
status: primary-read
status_partial: true
retrieved: 2026-08-27
---

# FT Visual Vocabulary

A poster and companion repository from the Financial Times Visual Journalism Team that organizes chart types under **nine data relationships**, so that chart choice starts from what is being shown rather than from a menu of shapes. The listing runs to **67 entries under 59 distinct names**, eight names being filed under two relationships each.

**How this was read.** `primary-read`, with one scope note, and read twice.

- **2026-08-23.** The `visual-vocabulary` README in the `Financial-Times/chart-doctor` repository was fetched and converted locally. That pass recorded all nine category definitions and a sample of the per-chart glosses.
- **2026-08-27.** The raw markdown was fetched again with `curl -sL` from `raw.githubusercontent.com` on the repository's default branch, saved locally, and its identity confirmed from the opening lines before anything was quoted. The full listing below was extracted from that saved file by walking its `###` category headings and `####` type headings and taking the first prose line under each, so every gloss here is machine-lifted from the source text rather than retyped. 67 type headings were found and 67 glosses recovered, with none missing.

Quotes are verbatim, including the source's own typos, which are frequent enough to be worth expecting: "value pf multiple variables", "the arrngement of the variables", "count/magnitde", "earthquakes by contintent", "in a table,they work best". **One repair was made and only one.** The nine category definitions in the raw markdown have words run together where the poster's line breaks were pasted in ("can bebroken down", "issolely", "chartinstead", "locations orgeographical"). Those spaces are restored in the definitions below. No gloss needed the repair.

**The PDF poster itself has still not been opened**, so any claim about the poster's layout or visual design is not vouched here. That is now the only unread part of this source: the README is covered end to end.

**What it is good for.** The taxonomy, and now the complete type listing under it. It is the answer to "what family of chart does this question call for", and it is the only source in this corpus organized that way. The per-chart glosses are one line each and are unusually sharp.

**What it does not settle.** Nearly everything else. No color guidance, no typography, no accessibility, no annotation, no layout. It says so itself. It is also **copyright, all rights reserved** by The Financial Times Limited, unlike the openly licensed material elsewhere in this wiki, so it can be cited but not copied. The glosses below are quoted with attribution, which is citation. The poster is not reproduced and neither is the README's related-reading apparatus, which is the bulk of the document by length.

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

**Correlation carries a warning about the reader's inference,** not about the chart. That is a different kind of rule from anything else in this corpus: it is about what the audience will conclude regardless of what was drawn.

**Part-to-whole and Magnitude are defined against each other.** "If the reader's interest is solely in the size of the components, consider a magnitude-type chart instead." The taxonomy is explicit that the same data can sit in two families and the *question* decides. This is the whole argument for organizing by relationship rather than by data shape.

**Spatial says "used only when",** which is inventory topic 22 embedded in the taxonomy itself.

## The complete listing

Every type the Visual Vocabulary names, under its category, with its one-line gloss verbatim. Counts per category are the FT's, not this wiki's.

### Deviation (4 types)

| Type | Gloss |
|---|---|
| **Diverging bar** | "A simple standard bar chart that can handle both negative and positive magnitude values." |
| **Diverging stacked bar** | "Perfect for presenting survey results which involve sentiment (eg disagree/neutral/agree)." |
| **Spine chart** | "Splits a single value into 2 contrasting components (eg Male/Female)" |
| **Surplus/deficit filled line** | "The shaded area of these charts allows a balance to be shown – either against a baseline or between two series." |

### Correlation (5 types)

| Type | Gloss |
|---|---|
| **Scatterplot** | "The standard way to show the relationship between two continuous variables, each of which has its own axis." |
| **Line + Column** | "A good way of showing the relationship between an amount (columns) and a rate (line)" |
| **Connected scatterplot** | "Usually used to show how the relationship between two variables has changed over time." |
| **Bubble** | "Like a scatterplot, but adds additional detail by sizing the circles according to a third variable" |
| **XY heatmap** | "A good way of showing the patterns between 2 categories of data, less good at showing fine differences in amounts." |

### Ranking (6 types)

| Type | Gloss |
|---|---|
| **Ordered bar** | "Standard bar charts display the ranks of values much more easily when sorted into order" |
| **Ordered column** | "See above." |
| **Ordered proportional symbol** | "Use when there are big variations between values and/or seeing fine differences between data is not so important." |
| **Dot strip plot** | "Dots placed in order on a strip are a space-efficient method of laying out ranks across multiple categories." |
| **Slope** | "Perfect for showing how ranks have changed over time or vary between categories." |
| **Lollipop chart** | "Lollipops draw more attention to the data value than standard bar/column and can also show rank and value effectively." |

### Distribution (8 types)

| Type | Gloss |
|---|---|
| **Histogram** | "The standard way to show a statistical distribution - keep the gaps between columns small to highlight the ‘shape’ of the data" |
| **Boxplot** | "Summarise multiple distributions by showing the median (centre) and range of the data" |
| **Violin plot** | "Similar to a box plot but more effective with complex distributions (data that cannot be summarised with simple average)." |
| **Population pyramid** | "A standard way for showing the age and sex breakdown of a population distribution; effectively, back to back histograms." |
| **Dot strip plot** | "Good for showing individual values in a distribution, can be a problem when too many dots have the same value." |
| **Dot plot** | "A simple way of showing the change or range (min/max) of data across multiple categories." |
| **Barcode plot** | "Like dot strip plots, good for displaying all the data in a table,they work best when highlighting individual values." |
| **Cumulative curve** | "A good way of showing how unequal a distribution is: y axis is always cumulative frequency, x axis is always a measure." |

### Change over Time (12 types)

| Type | Gloss |
|---|---|
| **Line** | "The standard way to show a changing time series. If data are irregular, consider markers to represent data points" |
| **Column** | "Columns work well for showing change over time - but usually best with only one series of data at a time." |
| **Line + column** | "A good way of showing the relationship over time between an amount (columns) and a rate (line)" |
| **Stock price** | "Usually focused on day-to-day activity, these charts show opening/closing and hi/low points of each day" |
| **Slope** | "Good for showing changing data as long as the data can be simplified into 2 or 3 points without missing a key part of story" |
| **Area chart** | "Use with care – these are good at showing changes to total, but seeing change in components can be very difficult" |
| **Fan chart (projection)** | "Use to show the uncertainty in future projections - usually this grows the further forward to projection" |
| **Connected scatterplot** | "A good way of showing changing data for two variables whenever there is a relatively clear pattern of progression." |
| **Calendar heatmap** | "A great way of showing temporal patterns (daily, weekly, monthly) – at the expense of showing precision in quantity." |
| **Priestley timeline** | "Great when date and duration are key elements of the story in the data." |
| **Circle timeline** | "Good for showing discrete values of varying size across multiple categories (eg earthquakes by contintent)." |
| **Seismogram** | "Another alternative to the circle timeline for showing series where there are big variations in the data." |

### Part-to-whole (10 types)

| Type | Gloss |
|---|---|
| **Stacked column** | "A simple way of showing part-to-whole relationships but can be difficult to read with more than a few components." |
| **Proportional stacked bar** | "A good way of showing the size and proportion of data at the same time – as long as the data are not too complicated." |
| **Pie** | "A common way of showing part-to-whole data – but be aware that it’s difficult to accurately compare the size of the segments." |
| **Donut** | "Similar to a pie chart – but the centre can be a good way of making space to include more information about the data (eg. total)" |
| **Treemap** | "Use for hierarchical part-to-whole relationships; can be difficult to read when there are many small segments." |
| **Voronoi** | "A way of turning points into areas – any point within each area is closer to the central point than any other centroid." |
| **Arc** | "A hemicycle, often used for visualising political results in parliaments." |
| **Gridplot** | "Good for showing % information, they work best when used on whole numbers and work well in multiple layout form." |
| **Venn** | "Generally only used for schematic representation" |
| **Waterfall** | "Can be useful for showing part-to-whole relationships where some of the components are negative." |

### Magnitude (10 types)

| Type | Gloss |
|---|---|
| **Column** | "The standard way to compare the size of things. Must always start at 0 on the axis" |
| **Bar** | "See above. Good when the data are not time series and labels have long category names." |
| **Paired column** | "As per standard column but allows for multiple series. Can become tricky to read with more than 2 series." |
| **Paired bar** | "See above." |
| **Proportional stacked bar** | "A good way of showing the size and proportion of data at the same time – as long as the data are not too complicated." |
| **Proportional symbol** | "Use when there are big variations between values and/or seeing fine differences between data is not so important." |
| **Isotype (pictogram)** | "Excellent solution in some instances – use only with whole numbers (do not slice off an arm to represent a decimal)." |
| **Lollipop chart** | "Lollipop charts draw more attention to the data value than standard bar/column – does not HAVE to start at zero (but preferable)." |
| **Radar chart** | "A space-efficient way of showing value pf multiple variables– but make sure they are organised in a way that makes sense to reader." |
| **Parallel coordinates** | "An alternative to radar charts – again, the arrngement of the variables is important. Usually benefits from highlighting values." |

### Spatial (8 types)

| Type | Gloss |
|---|---|
| **Basic choropleth (rate/ratio)** | "The standard approach for putting data on a map – should always be rates rather than totals and use a sensible base geography" |
| **Proportional symbol (count/magnitde)** | "Use for totals rather than rates – be wary that small differences in data will be hard to see." |
| **Flow map** | "For showing unambiguous movement across a map." |
| **Contour map** | "For showing areas of equal value on a map. Can use deviation colour schemes for showing +/- values" |
| **Equalised cartogram** | "Converting each unit on a map to a regular and equally-sized shape – good for representing voting regions with equal value." |
| **Scaled cartogram (value)** | "Stretching and shrinking a map so that each area is sized according to a particular value." |
| **Dot density** | "Used to show the location of individual events/locations – make sure to annotate any patterns the reader should see." |
| **Heat map** | "Grid-based data values mapped with an intensity colour scale. As choropleth map – but not snapped to an admin/political unit." |

### Flow (4 types)

| Type | Gloss |
|---|---|
| **Sankey (aka river plot)** | "Shows changes in flows from one condition to at least one other; good for tracing the eventual outcome of a complex process." |
| **Waterfall** | "Designed to show the sequencing of data through a flow process, typically budgets. Can include +/- components." |
| **Chord** | "A complex but powerful diagram which can illustrate 2-way flows (and net winner) in a matrix." |
| **Network** | "Used for showing the strength and inter-connectedness of relationships of varying types." |


## Eight names, filed twice

The FT files eight of its 59 names under two relationships each, which is the taxonomy applying its own rule that the reader's question decides. Where the two glosses differ, both are given above and the difference is the point.

| Name | Filed under | Do the two glosses differ? |
|---|---|---|
| Column | Change over Time, Magnitude | Yes, and the zero rule sits in only one of them. See below |
| Lollipop chart | Ranking, Magnitude | Yes. Only the Magnitude entry mentions zero |
| Slope | Ranking, Change over Time | Yes. Rank change in one, simplification to 2 or 3 points in the other |
| Dot strip plot | Ranking, Distribution | Yes. Space efficiency across categories in one, individual values and overplotting in the other |
| Connected scatterplot | Correlation, Change over Time | Yes, but both glosses are about change over time |
| Line + Column | Correlation, Change over Time | Nearly identical, the Change over Time one adding "over time" |
| Proportional stacked bar | Part-to-whole, Magnitude | No, the same sentence appears in both |
| Waterfall | Part-to-whole, Flow | Yes. Negative components in one, sequencing through a process in the other |

## The zero baseline is attached to Magnitude, not to columns

This is the finding the earlier partial reading got half right. The FT states the zero rule twice and both statements sit in **Magnitude**:

- **Column** (Magnitude): "The standard way to compare the size of things. Must always start at 0 on the axis"
- **Lollipop chart** (Magnitude): "Lollipop charts draw more attention to the data value than standard bar/column – does not HAVE to start at zero (but preferable)."

Nowhere else in the listing does the word zero appear in a gloss. The **Column** entry under Change over Time says only "Columns work well for showing change over time - but usually best with only one series of data at a time." **Ordered bar** and **Ordered column** under Ranking say nothing about a baseline. The same mark, drawn the same way, carries the rule in one category and not in the other two.

So the FT is doing two things at once, and both matter for inventory topic 9:

1. **By mark, within a category.** Filled column must start at zero, lollipop does not have to. The capitals on "HAVE" are the FT's own, and they sit on the negation rather than on the rule. (The earlier partial reading of this source claimed the README also capitalizes "always" on the column. It does not; the raw markdown reads "Must always start at 0 on the axis" with no emphasis of any kind. The poster may set it differently, and the poster is unread.) Same reasoning as Datawrapper's dot-plot remedy and Observable Plot's radius-only enforcement: the constraint follows from whether length or area encodes the value, not from the axis being quantitative. Three sources reaching that independently is the strongest form the topic takes.
2. **By question, across categories.** The rule is stated where the reader's task is "compare the size of things" and dropped where the task is trend or rank. That is a stronger claim than the by-mark reading alone and it is not one this wiki has recorded from anywhere else.

Read together, the FT's position is that the zero baseline belongs to the size-comparison task rather than to the bar. It is authority-asserted, not evidence-backed, and the FT immediately links out to both sides of the argument (below).

## Names the taxonomy does not carry

Recording absences matters as much as the listing, because a name missing here cannot be cited to the FT at all.

- **Marimekko and mosaic.** Neither word is a heading. The FT's entry for the form is **Proportional stacked bar**, under both Part-to-whole and Magnitude, and the only further reading attached to either copy is a Chart Doctor piece, "How to apply Marimekko to data". So the FT does file the form, twice, under a name this wiki does not use for it.
- **Waffle and unit chart.** The FT's name is **Gridplot**, under Part-to-whole. **Isotype (pictogram)** is a separate entry filed under **Magnitude**. The FT therefore splits the two constructions across two relationships rather than treating them as one form.
- **Adjacency matrix, hive plot, bump chart, sunburst, streamgraph, alluvial diagram, arc diagram.** None appear. The FT's **Arc** entry is unrelated to an arc diagram: it is "A hemicycle, often used for visualising political results in parliaments", filed under Part-to-whole.
- **Uncertainty** as a relationship. See the Todo gap below.

## The stated scope, which is the honest part

> "This is not an attempt to teach everyone how to make charts, but how to recognise the opportunities to use them effectively alongside words."

That sentence is why the Visual Vocabulary is worth a page and what bounds the claims it can carry. It is a recognition aid for a newsroom-wide chart-literacy training session, not a quality bar. Inventory topics 5 and 4 draw on it, and nothing else in the inventory does.

The lineage is credited: "inspired by the Graphic Continuum by Jon Schwabish and Severino Ribecca."

## The FT ships the argument, not a ruling

Most of the README by length is a per-type related-reading list, described in its own words as a work in progress. It is not summarized here beyond what the argument needs, and none of it is reproduced.

Under **Line** in Change over Time the further reading includes, in one list, ONS "Does the axis have to start at zero? (Part 1 – line charts)", Quartz "It's OK not to start your y-axis at zero", Vox "Shut up about the y-axis", and Emily Schuch "How to Make a Line Chart that Doesn't Lie". Under **Column** in the same category it links the ONS Part 2 piece on bar charts. The **Column** entry under Magnitude, the one that states the rule, links nothing at all.

Under **Line + Column** in Correlation it links two separate pieces cautioning about dual axes plus HBR on spurious correlations; the **Connected scatterplot** entry repeats one of the dual-axis cautions alongside Kosara's paper. Under **Pie** it links nine items, including three of Kosara's pie-chart pieces, both parts of an ONS series, Spence's history, "In defense of pie charts" and Few's "Save the Pies for Dessert". Both sides, at length.

A style guide that links to the argument instead of settling it is doing something different from the BBC's or Urban's. Whether that is a virtue depends on the reader: it is excellent for someone building a rulebook and useless for someone who wanted a rule. For the topics where this wiki finds the evidence genuinely contested (zero baselines, dual axes, chartjunk; see [refutations.md](../refutations.md)), the FT's refusal to rule looks like the better call in retrospect.

## The gap: uncertainty is a TODO

At the bottom of the README, after all nine categories, sit five unfinished sections:

```
Todo:
### Uncertainty
### Animation
### Interactivity
### Map projections
### Colour
```

Uncertainty, Animation and Interactivity each carry two or three reading links and no types. Map projections and Colour are empty headings.

**The FT taxonomy has no uncertainty family.** A fan chart appears under Change over Time ("Use to show the uncertainty in future projections - usually this grows the further forward to projection") and a box plot and violin under Distribution, but there is no relationship category for "this value is not known precisely", and the section that would create one is a stub.

That matters, because inventory topic 8 (directory-of-visualization coverage) explicitly requires a general bar to say something about **uncertainty** alongside amounts, distributions, proportions, x-y relationships and geospatial data. The most widely circulated chart-selection taxonomy in the field does not have a slot for it. That is some evidence that the topic's under-coverage is a property of the field rather than of any one guide. The statistical-reporting canon fills the gap, and [refutations.md](../refutations.md) records that it was not in this project's original source set either.

## Practical notes

- There are D3 templates in FT style in a separate repository, `ft-interactive/visual-vocabulary`. Same config-beats-prose pattern as `bbplot` and `urbnthemes` (see [bbc-cookbook.md](bbc-cookbook.md), [urban-institute.md](urban-institute.md)), in a different language.
- The poster exists in English, Japanese, traditional Chinese, and simplified Chinese.
- The README labels its own related-reading section "_This is a work in progress._"
- Three entries are defined only by cross-reference and carry no gloss of their own: **Ordered column** under Ranking, and **Bar** and **Paired bar** under Magnitude, all of which say "See above."
- **Licensing:** "Copyright © The Financial Times Limited, all rights reserved." The material is citable and linkable; the poster is not reproducible.

## Where this source is used

Inventory topics 4, 5, 21, 22, 50, 54, 79. See [roll-call.md](../roll-call.md), which maps all nine categories to topic 5 collectively.

## Links

- [Financial-Times/chart-doctor: visual-vocabulary](https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary)
- [Visual Vocabulary poster (PDF)](https://github.com/ft-interactive/chart-doctor/blob/master/visual-vocabulary/Visual-vocabulary.pdf)
- [Interactive web version](http://ft-interactive.github.io/visual-vocabulary/)
- [Graphic Continuum](https://policyviz.com/2014/09/09/graphic-continuum/), the acknowledged inspiration
