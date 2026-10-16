---
type: source
status: primary-read
author: claus-wilke
retrieved: 2026-08-27
---

# Wilke, *Fundamentals of Data Visualization*

Claus O. Wilke, *Fundamentals of Data Visualization* (O'Reilly, 2019), 30 chapters in three parts, free in full at [clauswilke.com/dataviz](https://clauswilke.com/dataviz/). The broadest single source in the canon, and the only one that treats production (image formats, software choice, reproducibility, separation of content from design) as a quality topic.

**What it is good for.** Which chart form a data relationship wants (the catalog, chapters 5 to 16), and what is wrong with an existing figure (the design principles, chapters 17 to 26, which a figure bar reuses).

**What it does not settle.** Wilke runs no experiments, and most of the book is `authority-asserted`. The exceptions cite studies: chapter 16 cites Kay et al. 2016 (quantile dotplots), Hullman et al. 2015 and Kale et al. 2018 (hypothetical outcome plots), and chapter 13 cites Haroz et al. 2016 against the connected scatterplot. Accessibility stops at color-vision deficiency (no alt text, screen readers or contrast ratios). Nothing on interaction, latency, or Cairo's statistical-reporting questions. The data-ink discussion is a corrective to Tufte, not evidence about him ([tufte.md](tufte.md), [refutations.md](../refutations.md)).

**How this was read.** Two passes at primary, the design-principles chapters and then chapters 5 to 16 in full. Each chapter page was fetched with `curl` and a browser user-agent, stripped to text locally and read end to end. Every quote was re-extracted from that HTML. The free web version is "the complete author manuscript before final copy-editing and other quality control," licensed CC BY-NC-ND 4.0, per its welcome page. The printed edition's wording may differ, and one quoted sentence carries an uncorrected typo.

---

## Structure

Three parts, 30 chapters.

- **Part I, From data to visualization** (chs. 2 to 16). Aesthetics and scales; coordinate systems and axes; color scales; then the catalog below.
- **Part II, Principles of figure design** (chs. 17 to 26). Proportional ink; overlapping points; common pitfalls of color use; redundant coding; multi-panel figures; titles, captions and tables; balance the data and the context; use larger axis labels; avoid line drawings; don't go 3D.
- **Part III, Miscellaneous topics** (chs. 27 to 30). Image file formats; choosing visualization software (with subsections on reproducibility and repeatability, exploration versus presentation, and separation of content and design); telling a story and making a point; annotated bibliography.

## The catalog of forms, chapter by chapter

Chapter 5 is the catalog's own index: "It is meant both to serve as a table of contents, in case you are looking for a particular visualization whose name you may not know, and as a source of inspiration". Unlike [schwabish.md](schwabish.md), both the filing and the argument for each form were read.

| Chapter | Forms named, in the book's order |
|---|---|
| **5. Directory of visualizations** | The index. Six sections: Amounts, Distributions, Proportions, x-y relationships, Geospatial data, Uncertainty |
| **6. Visualizing amounts** | Bar plot (vertical and horizontal), grouped bars, stacked bars, dot plot, heatmap |
| **7. Histograms and density plots** | Histogram, density plot (kernel density estimate), stacked histogram, overlapping histograms, overlapping density plots, **age pyramid** |
| **8. ECDFs and q-q plots** | Empirical cumulative distribution function (ascending and descending), descending log-log ecdf, quantile-quantile plot |
| **9. Many distributions at once** | Mean with error bars (labeled "bad"), boxplot, violin plot, **strip chart**, jittered strip chart, **sina plot**, **ridgeline plot**, ridgeline plot of histograms |
| **10. Proportions** | Pie chart, stacked bars, side-by-side bars, stacked densities, partial densities as parts of the total |
| **11. Nested proportions** | **Mosaic plot**, treemap, nested pies (inner and outer circle), a single pie subdivided with a nested color scale, **parallel sets** |
| **12. Associations** | Scatterplot, bubble chart, all-against-all scatterplot matrix, **correlogram** (colored tiles, and circles sized by absolute value), principal components analysis, paired-data scatterplot on an x = y line, **slopegraph** |
| **13. Time series** | Line graph (with dots, without dots, with the area filled), multiple line graphs, dose-response curve, **connected scatterplot** (also given as **phase portrait**) |
| **14. Trends** | Moving average, LOESS, splines (cubic, B-, thin-plate, Gaussian process), GAM, fits to a defined functional form, log-linear / log-log / linear-log axes, detrending, STL time-series decomposition |
| **15. Geospatial data** | Map projections (orthographic, Mercator, transverse and web Mercator, interrupted Goode homolosine, Albers), layers, **choropleth map**, **cartogram**, **cartogram heatmap**, per-region panels laid out geographically |
| **16. Uncertainty** | Frequency framing and discrete outcome visualization, **quantile dotplot**, error bars (graded and simple, with and without caps), **confidence strips**, confidence distributions, bars with error bars, scatterplot with x and y error bars, ridgeline plot of posteriors, **half eyes** and **eye plots**, confidence band, graded confidence band, alternative-fit draws, **hypothetical outcome plot** |

Chapter 18, in the design half, also belongs here (partial transparency, jittering, 2D histograms, hex bins, contour lines). Chapter 5.4 sends overplotted scatterplots there.

## Names it defines that nothing else in this corpus does

Definitions in running text, read at primary. Names that [../chart-types/aliases.md](../chart-types/aliases.md) marks "in circulation, no source here defines it" can be checked here.

- **Correlogram.** "Visualizations of correlation coefficients are called correlograms."
- **Sina plot**, with a citation: "This method, called a sina plot (Sidiropoulos et al. 2018), can be thought of as a hybrid between a violin plot and jittered points".
- **Strip chart**, and jittering: "we can try to circumvent these issues by simply plotting all the individual data points directly, as dots... Such a figure is called a strip chart."
- **Age pyramid**: "we can also make two separate histograms, rotate them by 90 degrees, and have the bars in one histogram point into the opposite direction of the other... the resulting plot is usually called an age pyramid."
- **Mosaic plot**, and the condition that scopes it: "unlike in a stacked bar plot, in a mosaic plot both the heights and the widths of individual shaded areas vary", and "This is a critical condition for a mosaic plot: Every categorical variable shown must cover all the observations in the dataset."
- **Parallel sets**: "we show how the total dataset breaks down by each individual categorical variable, and then we draw shaded bands that show how the subgroups relate to each other."
- **Empirical cumulative distribution function** and **quantile-quantile plot**, both constructed step by step in chapter 8.
- **Cartogram heatmap**: "each state is represented by a colored square", arranged by approximate relative position.
- **Quantile dotplot**, citing Kay et al. 2016, and **hypothetical outcome plot**, citing Hullman et al. 2015.
- **Half eyes and eye plots**: "Ridgeline plots with error bars underneath are called half eyes, and violin plots with error bars are called eye plots."
- **Phase portrait**, as an alias: "Physicists and engineers often call this a phase portrait, because in their disciplines it is commonly used to represent movement in phase space."

Streamgraph, sunburst and spine chart are absent. The nested-pie section describes a sunburst without the word.

## Where it disagrees with the other catalogs about filing

A filing is a retrieval aid, not a fact about a chart ([schwabish.md](schwabish.md)).

- **Slopegraph is paired data, not time** (chapter 12.4), the small-n alternative to a paired scatterplot. Schwabish files Slope under Time, the FT under both Ranking and Change over Time. Wilke's reason: it handles "a small number of observations" where "we are primarily interested in the identity of each individual case", and it extends to three or more columns.
- **Heatmap is an amount** (chapter 6.3), for when a position scale would be too busy. That agrees with Schwabish and the magnitude half of [heatmap.md](../chart-types/heatmap.md), not with the FT's split across Correlation and Spatial.
- **Mosaic plot and treemap are both proportions** (chapter 11). Schwabish puts Marimekko and Mosaic under Comparing Categories and Treemap under Part-to-Whole.
- **Bubble chart is an x-y relationship** (chapter 12.1), with the FT and this tier, against Schwabish's Comparing Categories.
- **Ridgeline plots** are distributions, with a second reading: "Ridgeline plots tend to work particularly well if want to show trends in distributions over time." That supports both memberships on [../chart-types/ridgeline-plot.md](../chart-types/ridgeline-plot.md).

## What it says about the forms

All of the following is `authority-asserted` unless a study is named in the sentence.

**Pie charts.** He rejects both usual verdicts:

> Many authors categorically reject pie charts and argue in favor of side-by-side or stacked bars. Others defend the use of pie charts in some applications. My own opinion is that none of these visualizations is consistently superior over any other.

"In general, pie charts work well when the goal is to emphasize simple fractions, such as one-half, one-third, or one-quarter. They also work well when we have very small datasets." Chapter 10 tabulates pie, stacked bars and side-by-side bars against six criteria.

**Stacked bars.** Stronger against them than most of this corpus:

> This is a general problem of stacked-bar plots, and the main reason why I normally do not recommend this type of visualization.

The mechanism is that internal bars shift baseline across the sequence. The exception: "the problem of shifting internal bars disappears if there are only two bars in each stack".

**Bars versus dots.** The zero-baseline rule, stated by mark rather than by axis:

> One important limitation of bars is that they need to start at zero, so that the bar length is proportional to the amount shown. For some datasets, this can be impractical or may obscure key features. In this case, we can indicate amounts by placing dots at the appropriate locations along the x or y axis.

That is the by-mark form of [../inventory.md](../inventory.md) topic 9, with Observable Plot, the FT and Schwabish.

**Violins over boxplots.** "In particular, violin plots will accurately represent bimodal data whereas a boxplot will not." Bounded by: "Before using violins to visualize distributions, verify that you have sufficiently many data points in each group to justify showing the point densities as smooth lines."

**Connected scatterplots.** `evidence-backed`, because he cites the study:

> Research reports that readers are more likely to confuse order and direction in a connected scatter plot than in line graphs and less likely to report correlation (Haroz, Kosara, and Franconeri 2016). On the flip side, connected scatter plots seem to result in higher engagement, and thus such plots may be a effective tools to draw readers into a story (Haroz, Kosara, and Franconeri 2016).

The typo is in the free manuscript. Haroz et al. 2016 decomposes a chart type directly and has no study page here, so its findings reach this wiki only through this summary.

**Choropleths.** [../chart-types/choropleth-map.md](../chart-types/choropleth-map.md) names classification as an open gap. Wilke gives no method, but a bin count and a condition on the quantity:

> Choropleths work best when the coloring represents a density (i.e., some quantity divided by surface area, as in Figures 15.11 and 15.12).

> Therefore, it is often appropriate to bin the data values into discrete groups that are represented with distinct colors. On the order of four to six bins is a good choice. The binning sacrifices some information, but on the flip side the binned colors can be uniquely recognized.

A non-density quantity is acceptable when the areas are about the same size and shape, or small relative to the map with the quantity varying on a larger scale. Which break algorithm to use he never raises. That question sits, unread, at [cairo-truthful-art.md](cairo-truthful-art.md).

**Discrete outcomes.** Chapter 16 says "Research in human perception shows that we are much better at perceiving, counting, and judging the relative frequencies of discrete objects" and cites nothing. It is `authority-asserted` despite the wording.

## The three-way labeling scheme

Chapter 1 defines the grades the rest of the book uses:

- **ugly**: "A figure that has aesthetic problems but otherwise is clear and informative."
- **bad**: "A figure that has problems related to perception; it may be unclear, confusing, overly complicated, or deceiving."
- **wrong**: "A figure that has problems related to mathematics; it is objectively incorrect."

His layout separates term and definition with a dash. The definitions are verbatim. The three are not equally objective: "In general, the 'ugly' rating is more subjective than the 'bad' or 'wrong' rating." A review that does not name the grade treats a taste call and an arithmetic error alike.

## Titles, labels and narrative

Titles (ch. 22.1), one paragraph that supplies both halves of inventory topic 37:

> It does not begin with "This figure shows how corruption is related to human development." The first part of the caption is always the title, not a description of the contents of the figure.

> A title does not have to be a complete sentence, though short sentences making a clear assertion can serve as titles. For example, for Figure 22.1, a title such as "The most developed countries are the least corrupt" would have worked fine.

Axis labels (ch. 24):

> If you take away only one single lesson from this book, make it this one: Pay attention to your axis labels, axis tick labels, and other assorted plot annotations. Chances are they are too small.

Axis titles (ch. 22.2):

> As a general principle, I think it is a bad practice to make your readers guess what you mean.

Data and context (ch. 23.4), the sentence that scopes the chapter:

> Both overloading a figure with non-data ink and excessively erasing non-data ink can result in poor figure design.

Narrative (ch. 29):

> Never jump straight to a highly complex figure; first show an easily digestible subset.

> Simple and clear is better than complex and confusing.

## Where its advice is contested

Chapter 23 argues against a maximal reading of Tufte's data-ink ratio. The record on data-ink and chartjunk is mixed in both directions ([refutations.md](../refutations.md)), and Wilke's "within reason" survives it better than Tufte's original. It is still an assertion.

The sentence "Maximize the data-ink ratio, within reason." is Tufte's. Wilke quotes it and adds the italics on *within reason*. The correct citation is "Tufte, quoted in Wilke ch. 23." See [tufte.md](tufte.md).

Chapter 14 treats bin width and bandwidth as analysis choices with no rule. Chapter 17's proportional-ink principle is stated, not measured.

## Inventory topics it grounds

Per [roll-call.md](../roll-call.md): 2, 5, 6, 7, 8, 9, 12, 14, 16, 17, 18, 20, 21, 22, 23, 26, 29, 35, 37, 39, 43, 48, 49, 50, 51, 52, 53, 54, 56, 58, 59, 60, 62, 63, 64, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 85, 86, 87, 88, 91.

## Links

- [inventory.md](../inventory.md): the topics this source grounds
- [roll-call.md](../roll-call.md): the chapter-by-chapter mapping
- [refutations.md](../refutations.md): data-ink, chartjunk, aspect ratio
- [tufte.md](tufte.md): the source of the data-ink material in ch. 23
- [checks/matplotlib.md](../checks/matplotlib.md): runnable versions of the mechanizable rules
- [../chart-types/aliases.md](../chart-types/aliases.md): the name-resolution index that chapters 5 to 16 can vouch for
- [schwabish.md](schwabish.md): the other chart-type catalog here, with its prose unread
