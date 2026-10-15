---
type: source
status: primary-read
status_partial: true
retrieved: 2026-08-27
---

# FT Visual Vocabulary

A poster and companion repository from the Financial Times Visual Journalism Team. It files chart types under **nine data relationships**, so chart choice starts from what is being shown rather than from a menu of shapes. The listing has **67 entries under 59 distinct names**, eight names being filed under two relationships each.

**What it is good for.** The answer to "what family of chart does this question call for", with a one-line gloss per type.

**What it does not settle.** Color, typography, accessibility, annotation and layout, which the README says it does not cover. It is **copyright, all rights reserved** by The Financial Times Limited, so it can be cited but not copied. The glosses are quoted with attribution. The poster and the README's related-reading apparatus are not reproduced.

**How this was read.** `primary-read` for the README, end to end. The PDF poster was not opened, so nothing about its layout or design is vouched for. The `visual-vocabulary` README in `Financial-Times/chart-doctor` was first fetched and converted locally for the category definitions and a sample of glosses. The raw markdown was then fetched with `curl -sL` from `raw.githubusercontent.com` on the default branch, saved, and identified from its opening lines before quoting. The listing was machine-lifted from that file by walking its `###` category and `####` type headings and taking the first prose line under each; every type heading yielded a gloss. Quotes keep the source's typos ("value pf multiple variables", "count/magnitde"). One repair: the category definitions run words together where the poster's line breaks were pasted in ("can bebroken down", "issolely"), and those spaces are restored. No gloss needed it.

---

## The nine relationships

Each carries a definition and an FT example. The definitions, verbatim:

**Deviation.** "Emphasise variations (+/-) from a fixed reference point. Typically the reference point is zero but it can also be a target or a long-term average. Can also be used to show sentiment (positive/neutral/negative)."

**Correlation.** "Show the relationship between two or more variables. Be mindful that, unless you tell them otherwise, many readers will assume the relationships you show them to be causal (i.e. one causes the other)."

**Ranking.** "Use where an item's position in an ordered list is more important than its absolute or relative value. Don't be afraid to highlight the points of interest."

**Distribution.** "Show values in a dataset and how often they occur. The shape (or 'skew') of a distribution can be a memorable way of highlighting the lack of uniformity or equality in the data."

**Change over Time.** "Give emphasis to changing trends. These can be short (intra-day) movements or extended series traversing decades or centuries. Choosing the correct time period is important to provide suitable context for the reader."

**Part-to-whole.** "Show how a single entity can be broken down into its component elements. If the reader's interest is solely in the size of the components, consider a magnitude-type chart instead."

**Magnitude.** "Show size comparisons. These can be relative (just being able to see larger/bigger) or absolute (need to see fine differences). Usually these show a 'counted' number (for example, barrels, dollars or people) rather than a calculated rate or per cent."

**Spatial.** "Used only when precise locations or geographical patterns in data are more important to the reader than anything else."

**Flow.** "Show the reader volumes or intensity of movement between two or more states or conditions. These might be logical sequences or geographical locations."

Correlation's warning is about what the audience will infer, not about what was drawn. Part-to-whole and Magnitude are defined against each other, so the same data can sit in two families and the question decides. Spatial's "used only when" is inventory topic 22 built into the taxonomy.

## The complete listing

Every type the Visual Vocabulary names, under its category, with its one-line gloss verbatim. Per-category counts are the FT's.

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

Eight of the 59 names sit under two relationships each, which is the taxonomy applying its own rule that the reader's question decides. Where the two glosses differ, both are in the listing above.

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

Both of the FT's zero statements sit in **Magnitude**:

- **Column** (Magnitude): "The standard way to compare the size of things. Must always start at 0 on the axis"
- **Lollipop chart** (Magnitude): "Lollipop charts draw more attention to the data value than standard bar/column – does not HAVE to start at zero (but preferable)."

No other gloss uses the word zero. **Column** under Change over Time says only "Columns work well for showing change over time - but usually best with only one series of data at a time." **Ordered bar** and **Ordered column** under Ranking say nothing about a baseline. The same mark carries the rule in one category and not in the other two.

That gives inventory topic 9 two readings:

1. **By mark, within a category.** A filled column must start at zero; a lollipop does not have to. The capitals on "HAVE" are the FT's and sit on the negation. The README does not capitalize "always"; the poster may, and is unread. Datawrapper's dot-plot remedy and Observable Plot's radius-only enforcement reason the same way: the constraint follows from whether length or area encodes the value, not from the axis being quantitative. Three sources reach that reading independently.
2. **By question, across categories.** The rule is stated where the task is "compare the size of things" and dropped where the task is trend or rank. No other source here makes that stronger claim.

The FT ties the zero baseline to the size-comparison task rather than to the bar. Authority-asserted, not evidence-backed.

## Names the taxonomy does not carry

A name missing here cannot be cited to the FT.

- **Marimekko and mosaic.** Not headings. The FT files the form as **Proportional stacked bar**, under Part-to-whole and Magnitude, and the only further reading on either copy is a Chart Doctor piece, "How to apply Marimekko to data".
- **Waffle and unit chart.** The FT's name is **Gridplot**, under Part-to-whole. **Isotype (pictogram)** is a separate entry under **Magnitude**, so the two constructions sit in different relationships.
- **Adjacency matrix, hive plot, bump chart, sunburst, streamgraph, alluvial diagram, arc diagram.** Absent. The FT's **Arc** is "A hemicycle, often used for visualising political results in parliaments", unrelated to an arc diagram.
- **Uncertainty** as a relationship. See below.

## Stated scope

> "This is not an attempt to teach everyone how to make charts, but how to recognise the opportunities to use them effectively alongside words."

It is a recognition aid for newsroom chart-literacy training, not a quality bar. Inventory topics 4 and 5 rest on it, and several others cite it in passing. The lineage is credited: "inspired by the Graphic Continuum by Jon Schwabish and Severino Ribecca."

## Further reading: both sides, no ruling

Most of the README is a per-type related-reading list, labeled "_This is a work in progress._" Under **Line** in Change over Time it links ONS "Does the axis have to start at zero? (Part 1 – line charts)", Quartz "It's OK not to start your y-axis at zero", Vox "Shut up about the y-axis", and Emily Schuch "How to Make a Line Chart that Doesn't Lie". **Column** in the same category links the ONS Part 2 piece on bar charts. **Column** under Magnitude, which states the rule, links nothing.

**Line + Column** in Correlation links two dual-axis cautions and HBR on spurious correlations; **Connected scatterplot** repeats one caution beside Kosara's paper. **Pie** links nine items, among them three Kosara pieces, an ONS series, Spence's history, "In defense of pie charts" and Few's "Save the Pies for Dessert". Where the BBC and Urban guides settle these arguments, the FT links to them, which matches a record that is contested on zero baselines, dual axes and chartjunk ([refutations.md](../refutations.md)).

## No uncertainty family

The README ends with five unfinished sections:

```
Todo:
### Uncertainty
### Animation
### Interactivity
### Map projections
### Colour
```

Uncertainty, Animation and Interactivity carry two or three reading links and no types. Map projections and Colour are empty. A fan chart sits under Change over Time ("Use to show the uncertainty in future projections - usually this grows the further forward to projection"), and box plot and violin under Distribution, but no relationship covers "this value is not known precisely".

Inventory topic 8 requires a general bar to cover **uncertainty** alongside amounts, distributions, proportions, x-y relationships and geospatial data. The most widely circulated chart-selection taxonomy has no slot for it, which is some evidence that the under-coverage belongs to the field rather than to one guide. The statistical-reporting canon fills the gap; [refutations.md](../refutations.md) records that it was not in this project's original source set.

## Practical notes

- FT-style D3 templates live in `ft-interactive/visual-vocabulary`, the same config-over-prose pattern as `bbplot` and `urbnthemes` ([bbc-cookbook.md](bbc-cookbook.md), [urban-institute.md](urban-institute.md)).
- The poster exists in English, Japanese, traditional Chinese, and simplified Chinese.
- **Ordered column** (Ranking), **Bar** and **Paired bar** (Magnitude) are defined by cross-reference: "See above."
- **Licensing:** "Copyright © The Financial Times Limited, all rights reserved." Citable and linkable; the poster is not reproducible.

## Where this source is used

Inventory topics 4, 5, 21, 22, 50, 54, 79. [roll-call.md](../roll-call.md) maps all nine categories to topic 5 collectively.

## Links

- [Financial-Times/chart-doctor: visual-vocabulary](https://github.com/Financial-Times/chart-doctor/tree/main/visual-vocabulary)
- [Visual Vocabulary poster (PDF)](https://github.com/ft-interactive/chart-doctor/blob/master/visual-vocabulary/Visual-vocabulary.pdf)
- [Interactive web version](http://ft-interactive.github.io/visual-vocabulary/)
- [Graphic Continuum](https://policyviz.com/2014/09/09/graphic-continuum/): the acknowledged inspiration
