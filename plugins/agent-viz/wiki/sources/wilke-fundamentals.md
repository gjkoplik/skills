---
type: source
status: primary-read
author: claus-wilke
retrieved: 2026-08-27
---

# Wilke, *Fundamentals of Data Visualization*

Claus O. Wilke, *Fundamentals of Data Visualization* (O'Reilly, 2019), 30 chapters in three parts. The complete text is free at [clauswilke.com/dataviz](https://clauswilke.com/dataviz/). It is the broadest single source in the canon: it covers chart-type choice, figure-design principles, and the production end (file formats, software, reproducibility) that nothing else in the set touches.

**How this was read.** Two passes, both at primary. The design-principles chapters were pulled 2026-08-23. **Chapters 5 through 16, the catalog of forms, were pulled in full on 2026-08-27**: each chapter page fetched with `curl` and a browser user-agent, stripped to text locally, and read end to end. Every quote below was re-extracted from that HTML, not taken from a fetch summary. One caveat that belongs here: the free web version is described on its own welcome page as "the complete author manuscript before final copy-editing and other quality control," licensed CC BY-NC-ND 4.0. Wording in the printed O'Reilly edition may differ slightly, and at least one sentence quoted below carries an uncorrected typo.

**What it is good for.** The questions it answers: *which chart form does this data relationship want*, and *what is wrong with an existing figure*. Chapters 5 through 16 are a directory of visualizations organized by relationship (amounts, distributions, proportions, x-y, geospatial, uncertainty). Chapters 17 through 26 are the design-principles half, and they are the part a figure bar actually reuses. Part III is the only place in the canon that treats image formats, plotting-software choice, reproducibility and separation of content from design as first-class quality topics.

**What it does not settle.** Wilke runs no experiments, and most of the book is authority-asserted, which the inventory labels correctly. **One correction from the full read: "cites few" undersells chapter 16**, which carries real citations (Kay et al. 2016 for quantile dotplots, Hullman et al. 2015 and Kale et al. 2018 for hypothetical outcome plots) and chapter 13 cites Haroz et al. 2016 against the connected scatterplot. Those are the places where his chart advice has a study behind it rather than a preference. Accessibility is limited to color-vision deficiency: no alt text, no screen readers, no contrast ratios. There is nothing on interaction, nothing on latency, and nothing on the statistical-reporting questions Cairo covers. The data-ink discussion is a corrective to Tufte, not evidence about him; see [tufte.md](tufte.md) and [refutations.md](../refutations.md).

---

## Structure

Three parts, 30 chapters.

- **Part I, From data to visualization** (chs. 2 to 16). Aesthetics and scales; coordinate systems and axes; color scales; a directory of visualizations; then one chapter each on amounts, histograms and densities, ECDFs and q-q plots, many distributions at once, proportions, nested proportions, associations, time series, trends, geospatial data, and uncertainty.
- **Part II, Principles of figure design** (chs. 17 to 26). Proportional ink; overlapping points; common pitfalls of color use; redundant coding; multi-panel figures; titles, captions and tables; balance the data and the context; use larger axis labels; avoid line drawings; don't go 3D.
- **Part III, Miscellaneous topics** (chs. 27 to 30). Image file formats; choosing visualization software (with subsections on reproducibility and repeatability, exploration versus presentation, and separation of content and design); telling a story and making a point; annotated bibliography.

The full chapter-to-topic mapping is in [roll-call.md](../roll-call.md), which records that every substantive chapter maps and none are unmapped.

## The catalog of forms, chapter by chapter

Chapters 5 through 16 file forms by data relationship, and chapter 5 is the catalog's own index: "It is meant both to serve as a table of contents, in case you are looking for a particular visualization whose name you may not know, and as a source of inspiration".

**This is the one catalog in the corpus that is readable in full.** [schwabish.md](schwabish.md) vouches memberships from contents pages with the prose unread, so it can say where a type sits and nothing more. Here both halves are available: the filing below, and the argument in the quotes further down. Read on 2026-08-27 from the local extraction described above.

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

Chapter 18 belongs to this list in practice even though it sits in the design-principles half: it is where partial transparency, jittering, 2D histograms, hex bins and contour lines live, and chapter 5.4 sends the reader there for overplotted scatterplots.

## Names it defines that nothing else in this corpus does

[../chart-types/aliases.md](../chart-types/aliases.md) marks a large share of the names it resolves as in circulation with no source in this wiki defining them. This chapter set closes a batch of those **at primary**, which is a stronger warrant than any other catalog here can give, because a contents line records that a name exists while these are definitions in running text.

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

Three names this catalog does **not** carry: streamgraph, sunburst and spine chart. Wilke's nested-pie section describes the sunburst construction without using the word.

## Where it disagrees with the other catalogs about filing

Same discipline as [schwabish.md](schwabish.md): a filing is a retrieval aid, not a fact about a chart, and three schemes disagreeing is the evidence for that.

**Slopegraph is paired data, not time.** Wilke files it in chapter 12.4, among associations between quantitative variables, as the small-n alternative to a paired scatterplot. Schwabish files Slope under Time, and the FT under Change over Time. **Wilke's is a third placement**, and his reason is specific: a slopegraph handles "a small number of observations" where "we are primarily interested in the identity of each individual case", and it extends to three or more columns.

**Heatmap is an amount.** Chapter 6.3 files it with bars and dots, as the option for when a position scale would be too busy. That agrees with Schwabish's Comparing Categories and with the magnitude half of this tier's [heatmap.md](../chart-types/heatmap.md); it does not match the FT's split of the name across Correlation and Spatial.

**Mosaic plot and treemap are both proportions**, filed together in chapter 11. Schwabish files Marimekko and Mosaic under Comparing Categories and Treemap under Part-to-Whole, so his own scheme separates two forms Wilke treats as neighbors.

**Bubble chart is an x-y relationship**, chapter 12.1, which agrees with the FT and with this tier and disagrees with Schwabish's Comparing Categories.

**Ridgeline plots are filed under distributions** and then explicitly given a second reading: "Ridgeline plots tend to work particularly well if want to show trends in distributions over time." That corroborates both memberships on [../chart-types/ridgeline-plot.md](../chart-types/ridgeline-plot.md) from one sentence.

## What it says about the forms, which is the part the other catalogs cannot supply

All of the following is `authority-asserted` unless a study is named in the sentence.

**Pie charts.** He refuses both of the usual verdicts:

> Many authors categorically reject pie charts and argue in favor of side-by-side or stacked bars. Others defend the use of pie charts in some applications. My own opinion is that none of these visualizations is consistently superior over any other.

with a scoped rule attached: "In general, pie charts work well when the goal is to emphasize simple fractions, such as one-half, one-third, or one-quarter. They also work well when we have very small datasets." Chapter 10 also carries a pros-and-cons table across pie, stacked bars and side-by-side bars, on six criteria.

**Stacked bars.** Stronger against them than most of this corpus:

> This is a general problem of stacked-bar plots, and the main reason why I normally do not recommend this type of visualization.

with the mechanism named (the internal bars shift baseline across the sequence) and the exception stated: "the problem of shifting internal bars disappears if there are only two bars in each stack".

**Bars versus dots**, which is the zero-baseline rule stated by mark rather than by axis:

> One important limitation of bars is that they need to start at zero, so that the bar length is proportional to the amount shown. For some datasets, this can be impractical or may obscure key features. In this case, we can indicate amounts by placing dots at the appropriate locations along the x or y axis.

That puts him with Observable Plot, the FT and Schwabish on the by-mark form of [../inventory.md](../inventory.md) topic 9.

**Violins over boxplots**, with a specific failure named: "In particular, violin plots will accurately represent bimodal data whereas a boxplot will not." Bounded by a caution he states as a rule: "Before using violins to visualize distributions, verify that you have sufficiently many data points in each group to justify showing the point densities as smooth lines."

**Connected scatterplots**, and this one is `evidence-backed` because he cites the study:

> Research reports that readers are more likely to confuse order and direction in a connected scatter plot than in line graphs and less likely to report correlation (Haroz, Kosara, and Franconeri 2016). On the flip side, connected scatter plots seem to result in higher engagement, and thus such plots may be a effective tools to draw readers into a story (Haroz, Kosara, and Franconeri 2016).

(The typo is his, in the free manuscript.) No study page exists here for Haroz et al. 2016 and it is a direct decomposition of a chart type, so it is the highest-value uncited paper this read surfaced.

**Choropleths**, which is the part [../chart-types/choropleth-map.md](../chart-types/choropleth-map.md) names as an open hole. He does not give a classification *method*, but he does give a bin count and the condition on the quantity:

> Choropleths work best when the coloring represents a density (i.e., some quantity divided by surface area, as in Figures 15.11 and 15.12).

> Therefore, it is often appropriate to bin the data values into discrete groups that are represented with distinct colors. On the order of four to six bins is a good choice. The binning sacrifices some information, but on the flip side the binned colors can be uniquely recognized.

He also names two conditions under which a non-density quantity is acceptable: the colored areas are all about the same size and shape, or they are small relative to the map and the quantity varies on a larger scale than they do. **That is a partial fill for the hole, and it is not the same question as which break algorithm to use**, which he never raises. See [cairo-truthful-art.md](cairo-truthful-art.md) for where that question is filed and why it is still unread.

**One claim in chapter 16 carries no citation.** He writes "Research in human perception shows that we are much better at perceiving, counting, and judging the relative frequencies of discrete objects" and cites nothing for it, in a chapter that otherwise cites carefully. It is authority-asserted despite the wording.

## The three-way labeling scheme

Chapter 1 defines the vocabulary the rest of the book grades with:

- **ugly**: "A figure that has aesthetic problems but otherwise is clear and informative."
- **bad**: "A figure that has problems related to perception; it may be unclear, confusing, overly complicated, or deceiving."
- **wrong**: "A figure that has problems related to mathematics; it is objectively incorrect."

(Wilke's own layout separates each term from its definition with a dash. The definitions themselves are verbatim.)

He is explicit that these are not equally objective: "In general, the 'ugly' rating is more subjective than the 'bad' or 'wrong' rating." A review that cannot say which of the three it is looking at will treat a taste call and an arithmetic error as the same finding.

## Quotes verified verbatim

On titles (ch. 22.1), both halves of the inventory's topic 37 citation, and they come from the same paragraph:

> It does not begin with "This figure shows how corruption is related to human development." The first part of the caption is always the title, not a description of the contents of the figure.

> A title does not have to be a complete sentence, though short sentences making a clear assertion can serve as titles. For example, for Figure 22.1, a title such as "The most developed countries are the least corrupt" would have worked fine.

On axis labels (ch. 24), stated as the book's single most important lesson:

> If you take away only one single lesson from this book, make it this one: Pay attention to your axis labels, axis tick labels, and other assorted plot annotations. Chances are they are too small.

On axis titles (ch. 22.2):

> As a general principle, I think it is a bad practice to make your readers guess what you mean.

On data and context (ch. 23.4), the sentence that scopes the whole chapter:

> Both overloading a figure with non-data ink and excessively erasing non-data ink can result in poor figure design.

On narrative (ch. 29):

> Never jump straight to a highly complex figure; first show an easily digestible subset.

> Simple and clear is better than complex and confusing.

## Where its advice is contested

Only in one place, and it is not really Wilke's advice being contested. Chapter 23 quotes Tufte's data-ink ratio and then argues against reading it maximally. The empirical record on data-ink and chartjunk is genuinely mixed in both directions and lives in [refutations.md](../refutations.md). Wilke's "within reason" framing survives that record better than Tufte's original does, but it is still an assertion, not a finding.

Two smaller places where the claim has a boundary: chapter 14 treats bin width and smoothing bandwidth as analysis choices without giving a rule, and chapter 17's proportional-ink principle is stated as a principle rather than measured. Both are fine; neither is evidence.

## Inventory topics it grounds

Per [roll-call.md](../roll-call.md), not recomputed here: 2, 5, 6, 7, 8, 9, 12, 14, 16, 17, 18, 20, 21, 22, 23, 26, 29, 35, 37, 39, 43, 48, 49, 50, 51, 52, 53, 54, 56, 58, 59, 60, 62, 63, 64, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 85, 86, 87, 88, 91.

That is more topics than any other source in the set, which is why "the canon" in this project is really Wilke plus corrections.

## What the project got wrong about it

One attribution nit, recorded here and on the Tufte page: inventory topic 67 cites `Wilke ch. 23: "Maximize the data-ink ratio, within reason."` The sentence is Tufte's, quoted by Wilke, and the italics on *within reason* are Wilke's own added emphasis. The correct citation is "Tufte, quoted in Wilke ch. 23." See [tufte.md](tufte.md).

Two things this page itself had understated before chapters 5 through 16 were read in full:

- **"Cites few" was wrong for the uncertainty chapter.** Corrected above. Chapter 16 is study-backed in a way no other chart-choice writing in this corpus is.
- **The catalog half was treated as a chapter list.** It is a per-form catalog with a definition and an argument for each form, and it was the only full-text one available the whole time. Everything in [../chart-types/aliases.md](../chart-types/aliases.md) marked "in circulation, no source here defines it" is checkable against the names section above before it is written up as undefined.

## Links

- [inventory.md](../inventory.md), the topics this source grounds
- [roll-call.md](../roll-call.md), the chapter-by-chapter mapping
- [refutations.md](../refutations.md), data-ink, chartjunk, aspect ratio
- [tufte.md](tufte.md), the source of the data-ink material in ch. 23
- [checks/matplotlib.md](../checks/matplotlib.md), runnable versions of the mechanizable rules
- [../chart-types/aliases.md](../chart-types/aliases.md), the name-resolution index this book's chapters 5 to 16 can vouch for
- [schwabish.md](schwabish.md), the other chart-type catalog here, and the one whose prose is unread
