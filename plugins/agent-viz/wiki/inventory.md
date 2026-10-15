# The inventory: what a general figure bar owes

Derived from the general visualization canon by an agent working blind to any existing quality bar, so that a later diff against a real one would mean something. Topic numbers are stable and have gaps.

Each entry gives the one line a bar would say, a **mechanizable-or-judgment** verdict, a citation and an evidence class. Evidence-backed means a study, experiment or published standard. Authority-asserted means a design book or style guide says so. The two are not interchangeable.

The inventory has not been verified topic by topic, and sources reached only in secondary form are flagged inline. Later passes refuted or corrected several claims built on it; [refutations.md](refutations.md) records them.

---

## A. Framing: does this figure exist for a reason

**1. Task/purpose abstraction.** The question the reader should be able to answer is stated before a form is chosen. *Judgment*: the mapping from a stated goal to an abstract task is not recoverable from the artifact. Munzner, *Visualization Analysis and Design*, ch. 3 "Why: Task Abstraction". Authority-asserted.

**2. Data abstraction.** The dataset type (table / network / field / geometry) and each attribute's type are named before marks are picked. *Judgment* on the semantic call. *Partly mechanizable*: dtype introspection plus a cardinality heuristic catches numeric-coded categoricals in seconds. Munzner ch. 2. Authority-asserted.

**3. Audience and consumption context.** Who reads the figure, and where (notebook cell, docs page, slide, print, phone). The bar for a scratch diagnostic is not the bar for a docs figure. *Judgment*. Few, *Data Visualization Effectiveness Profile*: "The effectiveness of a data visualization can only be fully determined in light of its creator's intentions and its audience's needs." Authority-asserted. **Secondary source only.**

**4. Should this be a chart at all.** A sentence or a table sometimes carries the point better than a chart. *Judgment*. Urban Institute style guide: "If you find explanatory sentences do a better job of distilling the information you want to convey, consider going without a chart." Authority-asserted.

**5. Chart-type selection by data relationship.** The mark follows from the relationship being shown (deviation, correlation, ranking, distribution, change-over-time, part-to-whole, magnitude, spatial, flow) rather than from habit. *Judgment*. FT Visual Vocabulary. Authority-asserted.

**6. Channel-effectiveness ranking.** The most important attribute goes on the most accurately read channel: position, then length, then angle and area, then color and texture. *Judgment* to decide "most important". The ranking itself is evidence-backed via the Cleveland-McGill lineage. Munzner ch. 5.

**7. Expressiveness.** The encoding carries all of, and only, what is in the data. *Partly mechanizable*: a grep for a sequential or diverging colormap applied to a categorical column. Munzner: "the visual encoding should express all of, and only, the information in the dataset attributes." Authority-asserted.

**8. Directory-of-visualization coverage.** Coverage runs across amounts, distributions, proportions, x-y relationships, geospatial data *and* uncertainty, not one family. *Mechanizable as a self-audit*. Wilke, *Fundamentals of Data Visualization*, ch. 5. Authority-asserted.

## B. Scales, axes, and quantitative honesty

**9. Proportional ink / zero baseline.** Bars, areas and filled shapes start at zero on a linear scale; line and dot plots need not. *Mechanizable*: `ax.get_ylim()[0] == 0` when a bar or fill artist is present. Wilke ch. 17: "The sizes of shaded areas in a visualization need to be proportional to the data values they represent." Corroborated by Urban's "Data Visualization Absolutes" and by tooling default (Vega-Lite `zero: true` for quantitative x/y, the weaker by-axis reading). Authority-asserted.

  The stronger form is scoped by mark, not by axis. Observable Plot forces zero only on radius and opacity, where area encodes the value. The FT Visual Vocabulary scopes it per chart type ("Column... Must always start at 0" against "Lollipop... does not HAVE to start at zero"), and both its zero statements sit in its Magnitude category, so its rule is by mark *within* the size-comparison task ([sources/ft-visual-vocabulary.md](sources/ft-visual-vocabulary.md)). Schwabish scopes it to bars and columns. The independence of these sources is unaudited: Schwabish is behind the Urban Institute guide ([sources/urban-institute.md](sources/urban-institute.md)), so he and Urban are one source.

**10. Axis truncation as a deception vector.** A truncated axis is disclosed on the figure. *Mechanizable*: data range against axis range. Pandey et al., CHI 2015: distorted charts produced responses "between 58.5% and 129.5% bigger than the control condition" (n=330). **Evidence-backed.**

**11. Inverted or unconventional axis direction.** Inversion reverses the conclusion, not just the effort, and carries a loud label. *Mechanizable*: `ax.yaxis_inverted()`. Pandey et al. 2015 names it among the most common distortions. **Evidence-backed.**

**12. Log and other nonlinear scales.** A log axis is labeled as log; bars on a log scale start at 1, not 0. *Mechanizable*. Wilke ch. 17. Authority-asserted.

**13. Dual axes.** Two y-axes invite a false correlation. *Mechanizable*: detection of `twinx()` / `twiny()`. Urban: "Charts that have two axes should be avoided", but its current text names two exceptions (unit translations like Fahrenheit/Celsius, and Pareto charts), and Datawrapper now ships a dual-axis chart type. Authority-asserted, and the authorities have softened. No experiment supports a flat ban ([refutations](refutations.md)).

**14. Aspect ratio.** The ratio decides which slope differences are readable, and a library default is not set for the slope comparison at hand. *Mechanizable in principle, contested in practice*. Talbot, Gerth & Hanrahan. Two of their papers are often conflated: arc-length banking (InfoVis 2011) and the slope-ratio model (InfoVis 2012). **Evidence-backed**, with Cleveland's own caveat that banking "needs to be tempered with judgment". **Secondary source for the Cleveland quote.** See [studies/talbot-2012-slope-ratio.md](studies/talbot-2012-slope-ratio.md).

**15. Axis tick density and formatting.** Few enough ticks to read, formatted in the reader's units. *Mechanizable*. BBC cookbook sections on thousands separators and percent symbols. Authority-asserted.

**16. Axis and tick label size.** Axis text is commonly too small at the size the figure is viewed. *Mechanizable*. Wilke ch. 24: "Chances are they are too small." BBC's house theme fixes `axis.text` at 18, `plot.title` at 28. Authority-asserted.

**17. Axis titles and units.** Every axis carries a title with units unless the ticks are self-explanatory. *Mechanizable*. Wilke ch. 22: "it is a bad practice to make your readers guess what you mean." Authority-asserted.

**18. Number formatting, rounding, significant digits.** The precision shown is the precision the data supports and no more. *Mechanizable*: a regex over rendered text for excess decimals. Datawrapper Academy. Authority-asserted.

**19. Locale and number conventions.** Decimal marks, separators and date formats follow the reader, not the machine. *Mechanizable*. Datawrapper Academy. Authority-asserted.

**20. Coordinate system choice.** A non-Cartesian system must be justified by the data's structure and labeled as such. *Judgment*. Wilke ch. 3. Authority-asserted.

**21. Map projection.** The projection is chosen on purpose and named; equal-area wherever area is the message. *Mechanizable*. Urban: "US maps for print publication should use the Albers Equal Area projection." Authority-asserted.

**22. Is a map even the right idiom.** If the map only shows where people live, it is a population map. *Judgment*. Urban, Maps. Authority-asserted.

## C. Color

**23. Colormap class matched to data type.** Sequential for ordered, diverging for a meaningful midpoint, cyclic for wraparound, qualitative for unordered. Never crossed. *Mechanizable*: the named colormap's registered category against the column's inferred type. matplotlib, *Choosing Colormaps*. Authority-asserted.

**24. Perceptual uniformity.** A perceptually uniform ramp makes equal data steps look equal. *Mechanizable*: allowlist. matplotlib: "the human brain perceives changes in the lightness parameter as changes in the data much better than, for example, changes in hue." **Evidence-backed** (the CIELAB claim is a measured perceptual result).

**25. Rainbow / jet / turbo.** On quantitative data they band, they reverse, and they fail in grayscale. *Mechanizable*: denylist. matplotlib on the grayscale failure. Authority-asserted with an evidence-backed lightness argument. **Contested at the edges**: Observable Plot ships turbo as its default continuous scheme "chosen primarily to ensure high-contrast visibility". See refutations.

**26. Color-vision deficiency.** The assumed reader is red-green colorblind, and the palette is checked rather than eyeballed. *Mechanizable*: a CVD simulation with pairwise separation checked. matplotlib: "avoiding colormaps with both red and green will avoid many problems in general." Wilke ch. 19. Authority-asserted.

**27. Grayscale / monochrome survival.** The figure must read when printed black and white. *Mechanizable*: conversion to L\* with category separation checked. matplotlib; Munzner's rule of thumb "Get It Right in Black and White". Authority-asserted.

**28. Number of categorical colors.** Roughly five to seven at most; past that, the idiom changes. *Mechanizable*: a count of legend entries. seaborn: "if you have more than a handful of colors in your plot, it can become difficult to keep in mind what each one means." Urban's standard is fewer than seven categories in any graph. Authority-asserted.

**29. Gray as context, saturated color as emphasis.** *Partly mechanizable*: a count of non-gray series. Datawrapper; Urban; Wilke ch. 4 "Color as a tool to highlight". Authority-asserted. No controlled study tests one-accent against two-saturated emphasis. See refutations.

**30. Consistent color mapping across a figure set.** Once a group is blue, it is blue in every figure. *Mechanizable*: a diff of the category-to-hex map across a document. Urban; Datawrapper. Authority-asserted.

**31. Semantically intuitive color.** The color the reader already associates with the thing, unless there is a reason not to. *Judgment*. Datawrapper; Observable Plot on blue/red for cold/hot. Authority-asserted.

**32. Diverging-scale midpoint.** Set to a meaningful value and labeled. *Mechanizable*: `TwoSlopeNorm` / `vcenter` is explicit. Urban, Map Colors. Authority-asserted.

**33. Text and background contrast.** *Mechanizable*: WCAG relative-luminance ratio, ~30 minutes to implement, seconds to run. Urban cites WCAG 2.0 AA at 4.5:1 for normal text. **Evidence-backed** (a published standard). WCAG AA is 3:1 for graphical objects and 4.5:1 for text, and Chartability adopts those figures. Datawrapper's house floor is softer: 2.5 for big text, 4 for small.

  The 4.5:1 text floor is SC 1.4.3, from WCAG 2.0. The 3:1 graphical-object floor is SC 1.4.11 Non-text Contrast, absent from WCAG 2.0 (which stops at 1.4.9). It entered in 2.1 and is unchanged in WCAG 2.2, the current Recommendation of 12 December 2024. So the mark floor is not part of the WCAG 2.0 AA that Urban's guide names.

**34. Colorbar / continuous-legend design.** A continuous encoding needs a colorbar with units, sensible ticks, explicit `vmin`/`vmax`, and must not silently rescale between panels. *Mechanizable*. matplotlib documents colorbars and normalization as first-class. Authority-asserted.

**35. Color that encodes nothing.** Decorative color is either dropped or made redundant with something already encoded. *Judgment*, partly mechanizable. Wilke ch. 19. Authority-asserted.

## D. Text, labels, and annotation

**37. Title states the takeaway.** An assertion, not a description of the axes. *Mechanizable as a smell test*: a regex for "Plot of", "Chart showing", "X vs Y". The positive form is judgment. Wilke ch. 22: "The most developed countries are the least corrupt" beats "This figure shows how corruption is related to human development." Authority-asserted.

**38. Text case convention.** One convention, held across the set. *Mechanizable*. Urban: "Titles use headline/title case, and subtitles use sentence case." Authority-asserted.

**39. Direct labeling over legends.** Series are labeled on the data where there is room. *Mechanizable*: `ax.legend()` flagged when series count is small and space exists. Urban; Wilke ch. 20. The exception is mobile: Datawrapper switches to legends on small screens. Authority-asserted.

**40. Legend order matches data order.** Not alphabetical, not insertion order. *Mechanizable*: legend handle order against terminal y-values. BBC cookbook. Authority-asserted.

**41. Annotate the specific point being made.** The point is annotated on the figure rather than left to the caption. *Mechanizable as a presence check*; content is judgment. Urban: "Annotation is one of the most important ways to improve your data communication efforts." Authority-asserted.

**42. Every visual mark is explained.** *Judgment* on completeness. *Mechanizable floor*: every mapped channel has a legend, colorbar or direct label. Datawrapper: "Every visual mark that represents a value or variable should be explained." Authority-asserted.

**43. Caption vs title placement.** Figure captions below, table captions above. *Mechanizable*. Wilke ch. 22. Authority-asserted.

**44. Source line / data provenance.** Every figure a reader sees names where the data came from. *Mechanizable*. Datawrapper; Urban ("All tables must have a source line"); BBC's `finalise_plot()` exists to attach it. Authority-asserted.

**45. Notes: definitions, abbreviations, exclusions.** Every abbreviation is defined and everything dropped is disclosed. *Mechanizable*. Urban, Tables. Authority-asserted.

**46. Sample size / denominator disclosure.** n is stated, and so is the denominator for any rate. *Judgment* on materiality. Weakly sourced in the viz canon; [refutations.md](refutations.md) sources it from statistical reporting.

**47. Typography: family, weight, hierarchy.** One family and one size ladder across the set. *Mechanizable*: rcParams assertion. Urban uses Lato; BBC hardcodes Helvetica. Authority-asserted.

## E. Statistical honesty

**48. Uncertainty is displayed, not omitted.** A bare point estimate asserts precision the data may not support. *Judgment* on representation. *Mechanizable floor*: an estimator plotted with no interval artist is flagged. Wilke ch. 16. Authority-asserted.

**49. Error-bar semantics must be stated.** SD, SE, 95% CI or bootstrap percentile, on the figure. *Mechanizable*: the kind appears in legend or caption. seaborn on spread versus uncertainty; Correll & Gleicher, IEEE TVCG 2014: "the encoding of mean and error significantly changes how viewers make decisions about uncertain data." **Evidence-backed.**

**50. Show the distribution, not only the summary.** *Partly mechanizable*: bar-of-mean plus errorbar is flagged. seaborn: "You should always ask yourself whether it's best to use a plot that displays only a summary statistic and error bar. In many cases, it isn't." Matejka & Fitzmaurice's Datasaurus is the illustration. **Evidence-backed for the seaborn claim; the Datasaurus is a construction, not an experiment.**

**51. Asymmetric / impossible intervals.** Symmetric bars on skewed data extend past physically possible values. *Mechanizable*: bounds stay inside the variable's domain. seaborn. Authority-asserted.

**52. Binning and smoothing sensitivity.** Bin width and bandwidth are analysis choices, and a conclusion drawn under one may not survive another. *Mechanizable*: set explicitly rather than left to a default. Wilke ch. 7 and 14. Authority-asserted.

**53. Trend lines and fits labeled as models.** A fitted line is a model, not data. *Mechanizable*. Urban: "Best fit or regression lines should be used sparingly." Wilke ch. 14. Authority-asserted.

**54. Part-to-whole integrity.** Parts sum to the whole and the whole is stated. *Mechanizable*: segments sum within tolerance. Urban: "Pie charts should always add up to 100 percent." Authority-asserted.

**55. Missing data is shown as missing.** Gaps and dropped rows are disclosed, not interpolated across. *Mechanizable*: input row count against plotted point count. Weakly sourced in the viz canon; refutations cites a TVCG study.

**56. Outliers: clipped, shown or annotated, never silently dropped.** Where the limits exclude points, how many is stated. *Mechanizable*: a count of points outside the limits. Wilke ch. 8. Weakly sourced; see refutations.

**57. Sorting / ordering of categorical axes.** Sorted by value or by a stated logic, never left in arbitrary dataframe order. *Mechanizable*: monotone in the value, or an explicit `order=`. BBC; Urban on sorting logically. Authority-asserted.

## F. Density, overplotting, scale

**58. Overplotting and occlusion.** Overlapping marks are handled explicitly: alpha, jitter, 2D binning, contours. *Mechanizable heuristic*: point count over plot area with `alpha=1`. Wilke ch. 18. Authority-asserted.

**59. Jitter distorts.** Enough jitter to reveal, not enough to lie, and seeded. *Mechanizable*. Wilke ch. 18: "if we jitter too much, we end up placing points in locations that are not representative of the underlying dataset." Authority-asserted.

**60. Density idioms at scale.** Past the point where individual marks are readable, the idiom changes rather than the alpha. *Judgment* on the switch point. Wilke ch. 18. Authority-asserted.

**61. Reduce items and attributes.** Filtering, aggregating and sampling are legitimate design moves, and they are disclosed. *Judgment*. Munzner ch. 13. Authority-asserted.

## G. Composition and layout

**62. Small multiples with shared scales.** Panels compared side by side share axis ranges and color scales; free scales must be labeled. *Mechanizable*: per-axes limits compared across a grid. Urban; BBC; Wilke ch. 21; Munzner ch. 12. Authority-asserted.

**63. Panel labeling and reading order.** *Mechanizable*: every subplot has a title or letter. Wilke ch. 21. Authority-asserted.

**64. Figure size targeted at the display size.** `figsize` targets where the figure will appear, and the figure is viewed at that size. *Mechanizable*. Wilke ch. 24: "Always look at scaled-down versions of your figures." Authority-asserted.

**65. Margins, whitespace, clipped text.** Nothing cut off; long labels don't collide. *Mechanizable*: on render, no artist bbox exceeds the figure bbox. BBC. Authority-asserted.

**66. Gridline discipline.** Gridlines run perpendicular to the variable of interest, light and minimal, or absent. *Mechanizable*. Wilke ch. 23; BBC's theme blanks the x grid and lightens the y. Authority-asserted.

**67. Data-ink discipline, and its contested status.** Ink that is not carrying data is cut, *within reason*. Maximal minimalism is not settled. *Partly mechanizable*: a count of decorative artists. Tufte, quoted and italicized by Wilke in ch. 23: "Maximize the data-ink ratio, *within reason*." Against it, Bateman et al., CHI 2010: embellished-chart accuracy "no worse than for plain charts", recall after two to three weeks "significantly better". The authority claim and the experiment sit on opposite sides of this topic.

**68. 3D avoidance.** No 3D unless the data is three-dimensional. *Mechanizable*: a grep for `projection='3d'`. Wilke ch. 26; Munzner's "No Unjustified 3D"; Urban. Authority-asserted.

**69. Redundant coding.** Important distinctions are double-encoded so no single channel carries one alone. *Mechanizable*: two channels distinguish series when count > 2. Wilke ch. 20; seaborn. Authority-asserted.

**70. Line drawings.** Filled marks are preferred to outline-only figures. *Judgment*. Wilke ch. 25. Authority-asserted.

## H. Accessibility

**71. Alt text and long description.** A short alt text to identify, a longer description of what the data shows. *Mechanizable* as a presence check; content is judgment. W3C WAI, *Complex Images*: the two-part pattern. **Evidence-backed** (a published standard). Urban: "Alternative text should present the content and function, not necessarily a description, of an image."

**72. Underlying data reachable.** The reader has a path to the numbers. *Mechanizable*. Datawrapper: "a reader with a visual impairment has the possibility to download the data." Authority-asserted.

**73. Text baked into raster.** Chart text is real text where the medium allows. *Mechanizable*: export format. Urban resolves this *against* live text and compensates with alt text, so the sources disagree. Authority-asserted.

**74. Screen-reader-legible structure.** What a screen reader announces of the figure. *Judgment* plus tooling. Datawrapper reports experimenting with defaults. Authority-asserted.

## I. Medium, production, reproducibility

**75. Vector vs raster.** Vector for line art; never JPEG for a chart. *Mechanizable*: extension against mark count. Wilke ch. 27: "you should avoid it [jpeg] for images containing line drawings or text." Authority-asserted.

**76. Resolution / DPI.** Export resolution matches what the destination needs, and it cannot be recovered later. *Mechanizable*. Wilke ch. 27. Authority-asserted.

**77. Reproducibility of the figure.** Reproducible if data and transformations are specified; repeatable if it regenerates pixel-for-pixel, seed included. *Mechanizable*: two runs, then a byte diff. Wilke ch. 28. Authority-asserted.

**78. No manual post-hoc editing in a pipeline.** *Mechanizable*: policy grep. Wilke ch. 28. Authority-asserted.

**79. Separation of content and design.** House style lives in a theme or rcParams, not per-figure kwargs. *Mechanizable*. Wilke ch. 28; BBC ships this as `bbc_style()`. Authority-asserted.

**80. Responsive / small-screen rendering.** A figure that will be seen on a phone is checked at phone width. *Mechanizable*: a render at 380px with the label checks re-run. Datawrapper: "On mobile screens, your chart might only be 380px or 400px wide." Authority-asserted.

**81. Background / dark-mode assumption.** The background the figure assumes is stated. *Mechanizable*: an explicit `facecolor`. matplotlib documents dark-mode diverging colormaps. Authority-asserted.

## J. Interaction

**82. Interaction idioms.** The interaction has a stated purpose; it is an encoding decision, not a feature. *Judgment*. Munzner ch. 11, 13, 14; "Overview First, Zoom and Filter, Details on Demand". Authority-asserted.

**83. Latency budget.** An interactive figure that does not respond is not interactive. *Mechanizable*: time-to-first-paint. Munzner's "Responsiveness Is Required". Authority-asserted.

**84. Eyes beat memory.** Side-by-side display over making the reader remember or navigate. *Judgment*. Munzner ch. 6. Authority-asserted.

## K. Narrative and the figure-set level

**85. Sequence / build-up.** The complicated figure does not come first. *Judgment*. Wilke ch. 29: "Never jump straight to a highly complex figure; first show an easily digestible subset." Authority-asserted.

**86. Simplify for the audience.** *Judgment*. Wilke ch. 29: "Simple and clear is better than complex and confusing." Authority-asserted.

**87. Consistent but not repetitive across a set.** Visual language holds constant; the idiom varies when the analysis changes. *Judgment*. Wilke ch. 29. Authority-asserted.

**88. Memorability.** Distinctiveness aids recall, but not at the cost of clarity. *Judgment*. Wilke ch. 29; empirically supported on recall by Bateman et al. 2010. Mixed.

**89. Emotive quality.** A figure nobody looks at communicates nothing. *Judgment*. Few's profile splits criteria into informative and emotive, with Aesthetics and Engagement in the latter. Authority-asserted. **Secondary source only.**

**91. Truthfulness as the dominant constraint.** When beauty and truth conflict, truth wins. *Judgment*. Cairo's five qualities: "striving to be truthful is paramount among these five." Authority-asserted. **Secondary source only.**

**92. Function first, form next.** The encoding is settled before the styling. *Judgment*. Munzner ch. 6. Authority-asserted.

---

## Where a short bar most often falls short

Ranked by confidence that the topic is both owed and absent from a typical bar:

1. **Colorbar design (34)** and **uncertainty (48-51)**. Uncertainty is four topics: display, semantics, distribution over summary, impossible bounds. "Show uncertainty" alone covers a quarter of it.
2. **Grayscale survival (27).** A named Munzner rule and a matplotlib section, nearly always absent because screens are assumed.
3. **Reproducibility, seeding, no manual editing (77, 78, 59).** Owed by a bar in a software repo, not a newsroom one. The check is regeneration, then a byte diff.
4. **Aspect ratio (14).** Three research papers, near-zero presence in practitioner bars.
5. **Number formatting and locale (18, 19).** The most common visible defect in machine-generated figures, and rarely in a bar.
6. **Export format and DPI (75, 76).** A chart saved as JPEG is common and cheap to catch.
7. **Sorting and ordering (57).** Arbitrary dataframe order is the characteristic failure of *programmatic* plotting, invisible to a design-only review.
8. **Missing data and clipped outliers (55, 56).** Thinly treated in the viz canon, though plotting-library users hit them constantly.
9. **Panel-set consistency (30, 62, 87).** Bars tend to address *a* figure, not a *set*.
10. **Text baked into raster (73).** Contested, so a bar that ignores the conflict produces inconsistent review.
11. **Data-ink status (67).** Not missing but mislabeled.

## Known gaps in this inventory

- **Few's *Data Visualization Effectiveness Profile*** would not render. Its seven criteria and informative/emotive split came from search aggregation, so topics 3 and 89 are unconfirmed at the primary.
- **Knaflic's chapter titles** came from two independent aggregations, not a publisher list. Any gloss on their contents is uncorroborated.
- **Cairo's five qualities** came from a secondary summary. *How Charts Lie* was not reached and would likely sharpen 10, 11 and 21.
- **Munzner ch. 6** rule names are confirmed across two independent slide decks, but not verbatim.
- The plotting ecosystems were sampled at their most opinionated pages. Vega-Lite's encoding-channel opinions were touched only via the scale docs.
- [roll-call.md](roll-call.md) proves the mapping, not the wording: a chapter mapped to a badly named topic looks identical to one mapped well.
