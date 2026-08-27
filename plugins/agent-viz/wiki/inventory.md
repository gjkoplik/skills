# The inventory: what a general figure bar owes

Derived 2026-08-22 from the general visualization canon by an agent working **blind to any existing quality bar**, so that a later diff against a real one would mean something. 92 topics.

Every entry carries: the one line a bar would say, a **mechanizable-or-judgment** verdict, and its evidence class. **Evidence-backed** means a study, experiment or published standard. **Authority-asserted** means a design book or style guide asserting it. Both are usable; conflating them is the error.

Retrieval date for every citation: **2026-08-22**.

> Provenance note. This is the raw derived inventory. It has **not** been individually verified topic by topic; three of its sources were reachable only in secondary form and are flagged inline. Later verification passes refuted or corrected several claims built on top of this list, and those corrections live in [refutations.md](refutations.md). Read that file before quoting anything here as settled.

---

## A. Framing: does this figure exist for a reason

**1. Task/purpose abstraction.** State what question the reader should be able to answer before choosing a form. *Judgment*: the mapping from a stated goal to an abstract task is not recoverable from the artifact. Munzner, *Visualization Analysis and Design*, ch. 3 "Why: Task Abstraction". Authority-asserted.

**2. Data abstraction.** Name the dataset type (table / network / field / geometry) and each attribute's type before picking marks. *Judgment* on the semantic call; *partly mechanizable*: dtype introspection plus a cardinality heuristic catches numeric-coded categoricals in seconds. Munzner ch. 2. Authority-asserted.

**3. Audience and consumption context.** Name who reads this and where (notebook cell, docs page, slide, print, phone). The bar for a scratch diagnostic is not the bar for a docs figure. *Judgment*. Few, *Data Visualization Effectiveness Profile*: "The effectiveness of a data visualization can only be fully determined in light of its creator's intentions and its audience's needs." Authority-asserted. **Secondary source only.**

**4. Should this be a chart at all.** If a sentence or a table carries the point better, don't draw a chart. *Judgment*. Urban Institute style guide: "If you find explanatory sentences do a better job of distilling the information you want to convey, consider going without a chart." Authority-asserted.

**5. Chart-type selection by data relationship.** Pick the mark from the relationship you are showing (deviation, correlation, ranking, distribution, change-over-time, part-to-whole, magnitude, spatial, flow), not from habit. *Judgment*. FT Visual Vocabulary. Authority-asserted.

**6. Channel-effectiveness ranking.** Put the most important attribute on the most accurately-read channel: position, then length, then angle and area, then color and texture. *Judgment* to decide "most important"; the ranking itself is evidence-backed via the Cleveland-McGill lineage. Munzner ch. 5.

**7. Expressiveness.** Encode all of, and only, what is in the data. *Partly mechanizable*: grep for a sequential or diverging colormap applied to a categorical column. Munzner: "the visual encoding should express all of, and only, the information in the dataset attributes." Authority-asserted.

**8. Directory-of-visualization coverage.** A general bar must say something about amounts, distributions, proportions, x-y relationships, geospatial data *and* uncertainty, not one family. *Mechanizable as a self-audit*. Wilke, *Fundamentals of Data Visualization*, ch. 5. Authority-asserted.

## B. Scales, axes, and quantitative honesty

**9. Proportional ink / zero baseline.** Bars, areas and filled shapes start at zero on a linear scale; line and dot plots need not. *Mechanizable*: assert `ax.get_ylim()[0] == 0` when a bar or fill artist is present. Wilke ch. 17: "The sizes of shaded areas in a visualization need to be proportional to the data values they represent." Corroborated by tooling default (Vega-Lite `zero: true` for quantitative x/y) and Urban's "Data Visualization Absolutes". The FT scopes it more tightly than any of them: **both of its zero statements sit in its Magnitude category and no gloss outside that category mentions a baseline at all**, so the rule is by mark *within* the size-comparison task rather than across every quantitative axis (full listing on [sources/ft-visual-vocabulary.md](sources/ft-visual-vocabulary.md), read complete 2026-08-25). Authority-asserted.

  **The stronger form, and the one to use: scope it by mark, not by axis.** Three independent sources converge. Observable Plot forces a zero baseline only on radius and opacity, the channels where area actually encodes the value. The FT Visual Vocabulary does it per chart type ("Column... Must always start at 0" against "Lollipop... does not HAVE to start at zero"). Vega-Lite defaults `zero: true` for quantitative x and y, which is the by-axis reading and the weaker one. Schwabish scopes it to bars and columns specifically. A library, a taxonomy, a newsroom and a practitioner converging on the by-mark version is the best warrant this topic has. *(Added 2026-08-23.)*

  **Correction, 2026-08-25: this entry previously called Schwabish "a fourth independent source", and the count needs an audit.** Schwabish is behind the Urban Institute style guide (see [sources/urban-institute.md](sources/urban-institute.md)), so if Urban is one of the sources being counted here, he is not additional to it. The convergence is real; the arithmetic is not verified, and the members of "three independent sources" are not named in this entry. **Independence is a claim that needs support, and the absence of a byline is not support for it.**

**10. Axis truncation as a deception vector.** If you truncate, say so on the figure. *Mechanizable*: compare data range to axis range. Pandey et al., CHI 2015: distorted charts produced responses "between 58.5% and 129.5% bigger than the control condition" (n=330). **Evidence-backed.**

**11. Inverted or unconventional axis direction.** Never invert without a loud label; inversion reverses the conclusion, not just the effort. *Mechanizable*: `ax.yaxis_inverted()`. Pandey et al. 2015 names it among the most common distortions. **Evidence-backed.**

**12. Log and other nonlinear scales.** Label a log axis as log; bars on a log scale start at 1, not 0. *Mechanizable*. Wilke ch. 17. Authority-asserted.

**13. Dual axes.** Don't. Two y-axes invite a false correlation. *Mechanizable*: detect `twinx()` / `twiny()`. Urban: "Charts that have two axes should be avoided", **but its current text names two exceptions** (unit translations like Fahrenheit/Celsius, and Pareto charts), and **Datawrapper now ships a dual-axis chart type**. Authority-asserted, and the authorities have softened. **See [refutations](refutations.md): no experiment supports a flat ban, and the sources usually cited for one no longer state it flatly.** *(Corrected 2026-08-23 from the current primaries.)*

**14. Aspect ratio.** The ratio decides which slope differences are readable; do not accept the library default for a slope-comparison figure. *Mechanizable in principle, contested in practice*. Talbot, Gerth & Hanrahan. Two adjacent papers, often conflated: arc-length banking (InfoVis 2011) and the slope-ratio model (InfoVis 2012). **Evidence-backed**, with Cleveland's own caveat that banking "needs to be tempered with judgment". **Secondary source for the Cleveland quote.** *Citation corrected 2026-08-23; an earlier version credited this to "Talbot, Gehrke & Heer", which is wrong.* See [studies/talbot-2012-slope-ratio.md](studies/talbot-2012-slope-ratio.md).

**15. Axis tick density and formatting.** Few enough ticks to read, formatted in the reader's units. *Mechanizable*. BBC cookbook sections on thousands separators and percent symbols. Authority-asserted.

**16. Axis and tick label size.** Your axis text is almost certainly too small; check at the size it will be viewed. *Mechanizable*. Wilke ch. 24: "Chances are they are too small." BBC's house theme fixes `axis.text` at 18, `plot.title` at 28. Authority-asserted.

**17. Axis titles and units.** Every axis carries a title with units unless the ticks are self-explanatory. *Mechanizable*. Wilke ch. 22: "it is a bad practice to make your readers guess what you mean." Authority-asserted.

**18. Number formatting, rounding, significant digits.** Show the precision the data supports and no more. *Mechanizable*: regex rendered text for excess decimals. Datawrapper Academy. Authority-asserted.

**19. Locale and number conventions.** Decimal marks, separators and date formats follow the reader, not the machine. *Mechanizable*. Datawrapper Academy. Authority-asserted.

**20. Coordinate system choice.** A non-Cartesian system must be justified by the data's structure and labeled as such. *Judgment*. Wilke ch. 3. Authority-asserted.

**21. Map projection.** Choose deliberately and name it; equal-area wherever area is the message. *Mechanizable*. Urban: "US maps for print publication should use the Albers Equal Area projection." Authority-asserted.

**22. Is a map even the right idiom.** If the map only shows where people live, it is a population map. *Judgment*. Urban, Maps. Authority-asserted.

## C. Color

**23. Colormap class matched to data type.** Sequential for ordered, diverging for a meaningful midpoint, cyclic for wraparound, qualitative for unordered. Never crossed. *Mechanizable*: look up the named colormap's registered category against the column's inferred type. matplotlib, *Choosing Colormaps*. Authority-asserted.

**24. Perceptual uniformity.** Prefer a perceptually uniform ramp so equal data steps look equal. *Mechanizable*: allowlist. matplotlib: "the human brain perceives changes in the lightness parameter as changes in the data much better than, for example, changes in hue." **Evidence-backed** (the CIELAB claim is a measured perceptual result).

**25. Rainbow / jet / turbo.** Don't use them for quantitative data; they band, they reverse, they die in grayscale. *Mechanizable*: denylist. matplotlib on the grayscale failure. Authority-asserted with an evidence-backed lightness argument. **Contested at the edges**: Observable Plot ships turbo as its default continuous scheme "chosen primarily to ensure high-contrast visibility". See refutations.

**26. Color-vision deficiency.** Assume a red-green colorblind reader; check the palette, don't eyeball it. *Mechanizable*: run through a CVD simulation and assert pairwise separation. matplotlib: "avoiding colormaps with both red and green will avoid many problems in general." Wilke ch. 19. Authority-asserted.

**27. Grayscale / monochrome survival.** The figure must read when printed black and white. *Mechanizable*: convert to L\* and assert category separation. matplotlib; Munzner's rule of thumb "Get It Right in Black and White". Authority-asserted.

**28. Number of categorical colors.** Cap at roughly five to seven; past that, change idiom. *Mechanizable*: count legend entries. seaborn: "if you have more than a handful of colors in your plot, it can become difficult to keep in mind what each one means." Urban: "Keep the number of categories in any graph to fewer than seven." Authority-asserted.

**29. Gray as context, saturated color as emphasis.** *Partly mechanizable*: count non-gray series. Datawrapper; Urban; Wilke ch. 4 "Color as a tool to highlight". Authority-asserted. **No controlled study tests one-accent against two-saturated emphasis.** See refutations.

**30. Consistent color mapping across a figure set.** Once a group is blue, it is blue in every figure. *Mechanizable*: diff the category-to-hex map across a document. Urban; Datawrapper. Authority-asserted.

**31. Semantically intuitive color.** Use the color the reader already associates with the thing, unless there is a reason not to. *Judgment*. Datawrapper; Observable Plot on blue/red for cold/hot. Authority-asserted.

**32. Diverging-scale midpoint.** Must be set to a meaningful value and labeled. *Mechanizable*: assert `TwoSlopeNorm` / `vcenter` is explicit. Urban, Map Colors. Authority-asserted.

**33. Text and background contrast.** *Mechanizable*: WCAG relative-luminance ratio, ~30 minutes to implement, seconds to run. Urban cites WCAG 2.0 AA at 4.5:1 for normal text. **Evidence-backed** (a published standard). Note Datawrapper states a softer chart-specific floor (2.5 big / 4 small); the two disagree and a bar should pick one.

  **Resolved: use the WCAG numbers.** Datawrapper publishes 2.5 for big text and 4 for small; WCAG AA is 3:1 for graphical objects and 4.5:1 for text; Chartability adopts the WCAG figures. Two of three agree, and the one they agree with is an actual published standard rather than a house guideline. *(Resolved 2026-08-23.)*

**34. Colorbar / continuous-legend design.** A continuous encoding needs a colorbar with units, sensible ticks, explicit `vmin`/`vmax`, and must not silently rescale between panels. *Mechanizable*. matplotlib documents colorbars and normalization as first-class. Authority-asserted.

**35. Color that encodes nothing.** If color is decorative, drop it or make it redundant with something already encoded. *Judgment*, partly mechanizable. Wilke ch. 19. Authority-asserted.

**37. Title states the takeaway.** An assertion, not a description of the axes. *Mechanizable as a smell test*: regex for "Plot of", "Chart showing", "X vs Y". The positive form is judgment. Wilke ch. 22: "The most developed countries are the least corrupt" beats "This figure shows how corruption is related to human development." Authority-asserted.

**38. Text case convention.** Fix one and hold it. *Mechanizable*. Urban: "Titles use headline/title case, and subtitles use sentence case." Authority-asserted.

**39. Direct labeling over legends.** Label the series on the data where you can. *Mechanizable*: flag `ax.legend()` when series count is small and space exists. Urban; Wilke ch. 20. Note the mobile exception: Datawrapper switches to legends on small screens. Authority-asserted.

**40. Legend order matches data order.** Not alphabetical, not insertion order. *Mechanizable*: compare legend handle order to terminal y-values. BBC cookbook. Authority-asserted.

**41. Annotate the specific point being made.** Don't leave it to the caption. *Mechanizable as a presence check*; content is judgment. Urban: "Annotation is one of the most important ways to improve your data communication efforts." Authority-asserted.

**42. Every visual mark is explained.** *Judgment* on completeness; *mechanizable floor*: every mapped channel has a legend, colorbar or direct label. Datawrapper: "Every visual mark that represents a value or variable should be explained." Authority-asserted.

**43. Caption vs title placement.** Figure captions below, table captions above. *Mechanizable*. Wilke ch. 22. Authority-asserted.

**44. Source line / data provenance.** Every figure a reader sees names where the data came from. *Mechanizable*. Datawrapper; Urban ("All tables must have a source line"); BBC's `finalise_plot()` exists to attach it. Authority-asserted.

**45. Notes: definitions, abbreviations, exclusions.** Define every abbreviation, disclose what was dropped. *Mechanizable*. Urban, Tables. Authority-asserted.

**46. Sample size / denominator disclosure.** State n; state the denominator for any rate. *Judgment* on materiality. **Weakly sourced in the viz canon** (the deriving pass could not land a direct quote). See [refutations.md](refutations.md), where the statistical-reporting canon supplies it properly.

**47. Typography: family, weight, hierarchy.** Fix one family and a size ladder across the set. *Mechanizable*: rcParams assertion. Urban uses Lato; BBC hardcodes Helvetica. Authority-asserted.

## E. Statistical honesty

**48. Uncertainty is displayed, not omitted.** A bare point estimate asserts precision you may not have. *Judgment* on representation; *mechanizable floor*: flag an estimator plotted with no interval artist. Wilke ch. 16. Authority-asserted.

**49. Error-bar semantics must be stated.** SD, SE, 95% CI or bootstrap percentile, on the figure. *Mechanizable*: assert the kind appears in legend or caption. seaborn on spread-versus-uncertainty; Correll & Gleicher, IEEE TVCG 2014: "the encoding of mean and error significantly changes how viewers make decisions about uncertain data." **Evidence-backed.**

**50. Show the distribution, not only the summary.** *Partly mechanizable*: flag bar-of-mean plus errorbar. seaborn: "You should always ask yourself whether it's best to use a plot that displays only a summary statistic and error bar. In many cases, it isn't." Matejka & Fitzmaurice's Datasaurus is the illustration. **Evidence-backed for the seaborn claim; the Datasaurus is a construction, not an experiment.**

**51. Asymmetric / impossible intervals.** Symmetric bars on skewed data extend past physically possible values. *Mechanizable*: assert bounds stay inside the variable's domain. seaborn. Authority-asserted.

**52. Binning and smoothing sensitivity.** Bin width and bandwidth are analysis choices; state them and check the conclusion survives a different one. *Mechanizable*: assert explicit rather than defaulted. Wilke ch. 7 and 14. Authority-asserted.

**53. Trend lines and fits labeled as models.** A fitted line is a model, not data. *Mechanizable*. Urban: "Best fit or regression lines should be used sparingly." Wilke ch. 14. Authority-asserted.

**54. Part-to-whole integrity.** Parts sum to the whole and the whole is stated. *Mechanizable*: assert segments sum within tolerance. Urban: "Pie charts should always add up to 100 percent." Authority-asserted.

**55. Missing data is shown as missing.** Gaps and dropped rows are disclosed, not interpolated across. *Mechanizable*: compare input row count to plotted point count. **Weakly sourced in the viz canon**; see refutations, where a TVCG study supplies it.

**56. Outliers: clipped, shown or annotated, never silently dropped.** If the limits exclude points, say how many. *Mechanizable*: count points outside the limits. Wilke ch. 8. **Weakly sourced**; see refutations.

**57. Sorting / ordering of categorical axes.** Sort by value or by a stated logic; never leave arbitrary dataframe order. *Mechanizable*: assert monotone in the value or an explicit `order=`. BBC; Urban on sorting logically. Authority-asserted.

## F. Density, overplotting, scale

**58. Overplotting and occlusion.** When marks overlap, do something explicit: alpha, jitter, 2D binning, contours. *Mechanizable heuristic*: point count over plot area with `alpha=1`. Wilke ch. 18. Authority-asserted.

**59. Jitter distorts.** Jitter enough to reveal, not enough to lie, and seed it. *Mechanizable*. Wilke ch. 18: "if we jitter too much, we end up placing points in locations that are not representative of the underlying dataset." Authority-asserted.

**60. Density idioms at scale.** Past the point where individual marks are readable, switch idiom rather than piling on alpha. *Judgment* on the switch point. Wilke ch. 18. Authority-asserted.

**61. Reduce items and attributes.** Filtering, aggregating and sampling are legitimate design moves, but disclose them. *Judgment*. Munzner ch. 13. Authority-asserted.

## G. Composition and layout

**62. Small multiples with shared scales.** Panels compared side by side share axis ranges and color scales; free scales must be labeled. *Mechanizable*: compare per-axes limits across a grid. Urban; BBC; Wilke ch. 21; Munzner ch. 12. Authority-asserted.

**63. Panel labeling and reading order.** *Mechanizable*: assert every subplot has a title or letter. Wilke ch. 21. Authority-asserted.

**64. Figure size targeted at the display size.** Set `figsize` for where it will appear, then look at it there. *Mechanizable*. Wilke ch. 24: "Always look at scaled-down versions of your figures." Authority-asserted.

**65. Margins, whitespace, clipped text.** Nothing cut off; long labels don't collide. *Mechanizable*: render and assert no artist bbox exceeds the figure bbox. BBC. Authority-asserted.

**66. Gridline discipline.** Gridlines run perpendicular to the variable of interest, light and minimal, or absent. *Mechanizable*. Wilke ch. 23; BBC's theme blanks the x grid and lightens the y. Authority-asserted.

**67. Data-ink discipline, and its contested status.** Cut ink that is not carrying data, *within reason*. Do not treat maximal minimalism as settled. *Partly mechanizable*: count decorative artists. **Tufte**, quoted and italicized by Wilke in ch. 23: "Maximize the data-ink ratio, *within reason*." (*Attribution corrected 2026-08-23; an earlier version credited the sentence to Wilke.*) Against it, Bateman et al., CHI 2010: embellished-chart accuracy "no worse than for plain charts", recall after two to three weeks "significantly better". **This is the canonical case where a bar must not present an authority claim as an empirical one.**

**68. 3D avoidance.** No 3D unless the data is genuinely three-dimensional. *Mechanizable*: grep for `projection='3d'`. Wilke ch. 26; Munzner's "No Unjustified 3D"; Urban. Authority-asserted.

**69. Redundant coding.** Double-encode important distinctions so no single channel is load-bearing. *Mechanizable*: assert two channels distinguish series when count > 2. Wilke ch. 20; seaborn. Authority-asserted.

**70. Line drawings.** Avoid outline-only figures where filled marks read better. *Judgment*. Wilke ch. 25. Authority-asserted.

## H. Accessibility

**71. Alt text and long description.** A short alt text to identify, a longer description of what the data shows. *Mechanizable* as a presence check; content is judgment. W3C WAI, *Complex Images*: the two-part pattern. **Evidence-backed** (a published standard). Urban: "Alternative text should present the content and function, not necessarily a description, of an image."

**72. Underlying data reachable.** Give the reader a path to the numbers. *Mechanizable*. Datawrapper: "a reader with a visual impairment has the possibility to download the data." Authority-asserted.

**73. Text baked into raster.** Chart text should be real text where the medium allows. *Mechanizable*: check export format. Urban resolves this *against* live text and compensates with alt text, which is **a real disagreement a bar should resolve explicitly.** Authority-asserted.

**74. Screen-reader-legible structure.** Know what a screen reader announces. *Judgment* plus tooling. Datawrapper reports experimenting with defaults. Authority-asserted.

## I. Medium, production, reproducibility

**75. Vector vs raster.** Vector for line art; never JPEG a chart. *Mechanizable*: check extension against mark count. Wilke ch. 27: "you should avoid it [jpeg] for images containing line drawings or text." Authority-asserted.

**76. Resolution / DPI.** Export at what the destination needs; you cannot recover it later. *Mechanizable*. Wilke ch. 27. Authority-asserted.

**77. Reproducibility of the figure.** Reproducible if data and transformations are specified; repeatable if it regenerates pixel-for-pixel, seed included. *Mechanizable*: run twice, diff the bytes. Wilke ch. 28. Authority-asserted.

**78. No manual post-hoc editing in a pipeline.** *Mechanizable*: policy grep. Wilke ch. 28. Authority-asserted.

**79. Separation of content and design.** House style lives in a theme or rcParams, not per-figure kwargs. *Mechanizable*. Wilke ch. 28; BBC ships exactly this as `bbc_style()`. Authority-asserted.

**80. Responsive / small-screen rendering.** If it will be seen on a phone, check it at phone width. *Mechanizable*: render at 380px and re-run label checks. Datawrapper: "On mobile screens, your chart might only be 380px or 400px wide." Authority-asserted.

**81. Background / dark-mode assumption.** State the background the figure assumes. *Mechanizable*: assert explicit `facecolor`. matplotlib documents dark-mode diverging colormaps. Authority-asserted.

## J. Interaction

**82. Interaction idioms.** Say what the interaction is *for*; it is an encoding decision, not a feature. *Judgment*. Munzner ch. 11, 13, 14; "Overview First, Zoom and Filter, Details on Demand". Authority-asserted.

**83. Latency budget.** An interactive figure that does not respond is not interactive. *Mechanizable*: measure time-to-first-paint. Munzner's "Responsiveness Is Required". Authority-asserted.

**84. Eyes beat memory.** Prefer showing side by side over making the reader remember or navigate. *Judgment*. Munzner ch. 6. Authority-asserted.

## K. Narrative and the figure-set level

**85. Sequence / build-up.** Don't open with the complicated figure. *Judgment*. Wilke ch. 29: "Never jump straight to a highly complex figure; first show an easily digestible subset." Authority-asserted.

**86. Simplify for the audience.** *Judgment*. Wilke ch. 29: "Simple and clear is better than complex and confusing." Authority-asserted.

**87. Consistent but not repetitive across a set.** Hold visual language constant; vary the idiom when the analysis changes. *Judgment*. Wilke ch. 29. Authority-asserted.

**88. Memorability.** Distinctiveness aids recall, but not at the cost of clarity. *Judgment*. Wilke ch. 29; empirically supported on recall by Bateman et al. 2010. Mixed.

**89. Emotive quality.** A figure nobody looks at communicates nothing. *Judgment*. Few's profile splits criteria into informative and emotive, with Aesthetics and Engagement in the latter. Authority-asserted. **Secondary source only.**

**91. Truthfulness as the dominant constraint.** When beauty and truth conflict, truth wins. *Judgment*. Cairo's five qualities: "striving to be truthful is paramount among these five." Authority-asserted. **Secondary source only.**

**92. Function first, form next.** Get the encoding right before styling it. *Judgment*. Munzner ch. 6. Authority-asserted.

---

## Where a short bar most often falls short

Ranked by confidence that the topic is both owed and absent from a typical bar:

1. **Colorbar design (34)** and **uncertainty (48-51)**. Note uncertainty is *four* topics, not one: display at all, semantics disclosure, distribution-over-summary, and impossible bounds. A bar that adds "show uncertainty" and stops has closed a quarter of it.
2. **Grayscale survival (27).** Munzner makes it a named rule and matplotlib devotes a section to it, and it is nearly always absent because everyone assumes screens.
3. **Reproducibility, seeding, no-manual-editing (77, 78, 59).** A figure bar living in a software repo has an obligation a newsroom bar does not, and it is the most mechanizable thing on the list: regenerate, diff bytes.
4. **Aspect ratio (14).** Three research papers, near-zero presence in practitioner bars.
5. **Number formatting and locale (18, 19).** The single most common visible defect in machine-generated figures, and almost never in a bar because it feels beneath design.
6. **Export format and DPI (75, 76).** JPEG-a-chart is real and cheap to catch.
7. **Sorting and ordering (57).** Arbitrary dataframe order is the characteristic failure of *programmatic* plotting specifically, and it is invisible to anyone reviewing the design rather than the pipeline.
8. **Missing data and clipped outliers (55, 56).** The deriving pass could not fully ground these, which is itself the tell: the viz canon treats them thinly even though a plotting library's users hit them constantly.
9. **Panel-set consistency (30, 62, 87).** Bars tend to say things about *a* figure, not about a *set*.
10. **Text-baked-into-raster (73).** Genuinely contested; a bar that ignores the conflict produces inconsistent review.
11. **The data-ink contested status (67).** Not a missing topic but a *mislabeled* one.

## Known gaps in this inventory

Stated by the deriving pass against its own work:

- **Few's *Data Visualization Effectiveness Profile*** would not render; the seven criteria and the informative/emotive split came from search aggregation. Topics 3, 89 are unvouched at the primary level.
- **Knaflic's chapter list** came from aggregation, not a publisher list. Chapter titles are corroborated across two independent aggregations; any gloss on their contents is not.
- **Cairo's five qualities** came from a secondary summary. *How Charts Lie* was not reached at all and would likely sharpen 10, 11 and 21.
- **Munzner ch. 6** rule *names* are confirmed across two independent slide decks; verbatim statements were not obtained.
- The plotting ecosystems were sampled at their most opinionated pages rather than exhaustively. Vega-Lite in particular has an encoding-channel opinion set touched only via the scale docs.
- **The roll-call proves the mapping, not the wording.** A chapter mapped to a badly-named topic looks identical to one mapped well. See [roll-call.md](roll-call.md).
