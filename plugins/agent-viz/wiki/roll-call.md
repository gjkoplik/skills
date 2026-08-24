# Per-source roll-call

The audit trail for [inventory.md](inventory.md). For each source, its own published outline is enumerated and every entry is mapped either to an inventory topic or to a stated exclusion.

The point is that an omission becomes a **visibly unmapped chapter** rather than an absence nobody can see. "Graded on breadth" with no artifact is a hope with a label on it; this is the artifact.

**What this proves and does not prove.** It proves the mapping was performed. It does **not** prove the one-line rule attached to each topic is well worded. A chapter mapped to a badly-named topic looks identical to one mapped well.

Numbers refer to inventory topic numbers. Retrieval: **2026-08-22**.

---

## Wilke, *Fundamentals of Data Visualization*

Full table of contents retrieved from clauswilke.com/dataviz/.

| Chapter | Topics |
|---|---|
| 1. Introduction (ugly/bad/wrong) | 91, 86 |
| 2. Visualizing data: mapping onto aesthetics | 2, 6, 7 |
| 3. Coordinate systems and axes | 12, 20 |
| 4. Color scales | 23, 29, 35 |
| 5. Directory of visualizations | 8, 5 |
| 6. Visualizing amounts | 5, 9 |
| 7. Distributions: histograms and density | 50, 52 |
| 8. Distributions: ECDFs and q-q plots | 56 |
| 9. Many distributions at once | 50, 62 |
| 10. Proportions | 54 |
| 11. Nested proportions | 54, 5 |
| 12. Associations among quantitative variables | 5, 58 |
| 13. Time series | 5, 14 |
| 14. Trends (smoothing, functional form, detrending) | 52, 53 |
| 15. Geospatial data | 21, 22 |
| 16. Uncertainty | 48, 49, 51 |
| 17. Proportional ink | 9, 12 |
| 18. Overlapping points | 58, 59, 60 |
| 19. Common pitfalls of color use | 26, 35, 23 |
| 20. Redundant coding | 69, 39 |
| 21. Multi-panel figures | 62, 63 |
| 22. Titles, captions, and tables | 37, 17, 43, 18 |
| 23. Balance the data and the context | 66, 67 |
| 24. Use larger axis labels | 16, 64 |
| 25. Avoid line drawings | 70 |
| 26. Don't go 3D | 68 |
| 27. Image file formats | 75, 76 |
| 28. Choosing visualization software | 77, 78, 79 |
| 29. Telling a story and making a point | 85, 86, 87, 88 |
| 30. Annotated bibliography | **excluded**: bibliography, not a quality topic |
| Preface / technical notes / references | **excluded**: front and back matter |

**Every substantive chapter maps. No unmapped chapters.**

## Munzner, *Visualization Analysis and Design*

Chapter list from cs.ubc.ca/~tmm/vadbook/.

| Chapter | Topics |
|---|---|
| 1. What's Vis, and Why Do It? | 1, 4 |
| 2. What: Data Abstraction | 2 |
| 3. Why: Task Abstraction | 1 |
| 4. Analysis: Four Levels for Validation | **excluded**: a research-methodology framework (domain / abstraction / idiom / algorithm validation with threat-of-mismatch reasoning). A figure bar inherits its spirit via 1 and 2 but cannot mechanize four-level validation for a one-off chart. Deliberate exclusion, not an omission. |
| 5. Marks and Channels | 6, 7 |
| 6. Rules of Thumb | 68 (no unjustified 3D), 84 (eyes beat memory, resolution over immersion), 82 (overview first), 83 (responsiveness), 27 (get it right in black and white), 92 (function first, form next) |
| 7. Arrange Tables | 5, 57 |
| 8. Arrange Spatial Data | 21, 22 |
| 9. Arrange Networks and Trees | 5, the graph-specific chapter. A general bar owes at minimum "node-link versus matrix is a size-dependent choice", folded into 5 and 61 rather than given its own row. |
| 10. Map Color and Other Channels | 23 through 36 |
| 11. Manipulate View | 82 |
| 12. Facet into Multiple Views | 62, 63 |
| 13. Reduce Items and Attributes | 61 |
| 14. Embed: Focus+Context | 82 |
| 15. Analysis Case Studies | **excluded**: worked examples, not prescriptions |

**Caveat.** Chapter 6's rule *names* are confirmed across two independent slide decks (UBC and HKUST). Verbatim one-line statements from the book itself were not obtained.

## Knaflic, *Storytelling with Data*

| Chapter | Topics |
|---|---|
| 1. The importance of context | 1, 3 |
| 2. Choosing an effective visual | 5, 6, 4 |
| 3. Clutter is your enemy! | 67, 66, 65 |
| 4. Focus your audience's attention (preattentive attributes) | 29, 41, 37 |
| 5. Think like a designer | 47, 71, 89, 79 |
| 6. Dissecting model visuals | **excluded**: worked examples |
| 7. Lessons in storytelling | 85, 86, 87 |
| 8. Pulling it all together | **excluded**: single end-to-end case study |
| 9. Case studies | **excluded**: worked examples |
| 10. Final thoughts | **excluded**: closing matter |

**Caveat, and it matters.** The chapter list came from search aggregation plus a publisher-derived snippet; storytellingwithdata.com publishes no chapter list. Chapter *titles* are corroborated across two independent aggregations. Any gloss on chapter 5's contents is **from background familiarity, not a retrieved quote, and is unvouched.**

This is the weakest link in the roll-call, and it is load-bearing: Knaflic is the source a practitioner is most likely to name when they say a bar is missing something basic.

## Few, *Data Visualization Effectiveness Profile*

| Criterion | Topics |
|---|---|
| Usefulness (informative) | 1, 3 |
| Completeness (informative) | 42, 45, 46 |
| Perceptibility (informative) | 6, 16, 33 |
| Truthfulness (informative) | 9-11, 91 |
| Intuitiveness (informative) | 5, 31 |
| Aesthetics (emotive) | 89 |
| Engagement (emotive) | 89 |

**Caveat.** The PDF at perceptualedge.com returned as unreadable/password-protected binary. The criteria list and the informative/emotive split came from search aggregation of that PDF. **Everything mapped to Few is unvouched at the primary level and should be re-verified before anyone builds on it.**

## Cairo, five qualities

| Quality | Topics |
|---|---|
| Truthful | 91, 9-11, 50, 55 |
| Functional | 6, 92 |
| Beautiful | 89 |
| Insightful | 37, 41 |
| Enlightening | **excluded**: Cairo defines it as the composite of the other four, not an independent check |

**Caveat.** Secondary summary, not Cairo's own text. *How Charts Lie* was not reached at all and would likely sharpen topics 10, 11 and 21.

## matplotlib, *Choosing Colormaps*

Retrieved in full.

| Section | Topics |
|---|---|
| Overview (perceptual uniformity, CIELAB lightness) | 24 |
| Classes of colormaps | 23 |
| Sequential; Sequential2 (plateaus, kinks, banding) | 24, 25 |
| Discouraged aliases | **excluded**: backward-compatibility naming note |
| Diverging (symmetric L\*, dark-mode maps) | 32, 81 |
| Cyclic | 23 |
| Qualitative / Miscellaneous | 23, 25, 28 |
| Lightness-of-colormaps plotting | 24 |
| Grayscale conversion | 27 |
| Color vision deficiencies | 26 |
| References | **excluded**: bibliography |

The page's own section navigation additionally enumerates matplotlib's documented figure concerns: placing colorbars (34), axis scales (12), axis ticks (15), legends (39, 40), constrained layout (65), style sheets and rcParams (79), annotations (41), fonts (47), animations (82). All mapped.

## seaborn

| Page / section | Topics |
|---|---|
| Choosing color palettes: qualitative | 23, 28 |
| ... sequential / luminance | 23, 24 |
| ... diverging | 23, 32 |
| ... perceptual uniformity (rocket/mako/flare/crest) | 24 |
| ... colorblind accessibility, vary shape as well as color | 26, 69 |
| Error bars: spread vs uncertainty | 49 |
| ... parametric vs nonparametric | 49, 51 |
| ... "impossible values" warning | 51 |
| ... summary-statistic caution | 50 |
| API-version note | **excluded**: release history |

## Vega-Lite, Scale docs

| Item | Topics |
|---|---|
| `zero` default true for quantitative unbinned x/y | 9 |
| `zero` unsupported for log/time/utc | 12 |
| `scale.zero` config exceptions (ranged bar/area, size) | 9 |
| Default scale type by field type | 2, 7 |
| Remaining scale properties (domain, range, padding, interpolate, nice…) | **excluded**: parameter reference, except `clamp` which touches 56 |

**Sampling caveat.** Vega-Lite has a documented encoding-channel opinion set reached only via the scale page.

## Observable Plot, Scales

| Item | Topics |
|---|---|
| Quantitative scale types (linear, pow, sqrt, log, symlog) | 12 |
| Temporal | 2 |
| Ordinal (point / band / categorical) | 2 |
| Radius and opacity default domain `[0, max]` | 9 |
| Default color scheme turbo, "chosen primarily to ensure high-contrast visibility" | **25, as the counter-position** |
| Diverging schemes with semantic color | 31, 32 |
| Legends | 39 |

## BBC Visual and Data Journalism cookbook

All headings retrieved from bbc.github.io/rcookbook/.

| Heading group | Topics |
|---|---|
| Create BBC style graphics / load libraries / install bbplot | **excluded**: installation mechanics |
| How `bbc_style()` works (font, size, color, axis lines, axis text, margins) | 79, 47, 16, 66 |
| `finalise_plot()` (source line, branding, sizing, export) | 44, 64, 75 |
| Make a line / multiple line / bar / stacked bar / grouped bar / dumbbell / histogram | 5 |
| Legend changes (remove, position, reverse order, rearrange, symbols, spacing) | 39, 40, 42 |
| Axis changes (flip coords, gridlines, manual text, thousand separators, percent, limits, titles, ticks) | 66, 15, 17, 18, 56 |
| Annotations (annotation, alignment, data labels, left-aligned bar labels, lines, curved lines, arrows) | 41, 39 |
| Small multiples (facets, free scales) | 62 |
| Other (margins, export margins, reorder bars by size, reorder manually, conditional color) | 65, 57, 29 |

**Every heading maps.**

## Urban Institute Data Visualization Style Guide

| Section | Topics |
|---|---|
| Chart typography and sizing | 47 |
| Excel macro / R theme / Word templates / tool guidance | 79; the procurement policy itself **excluded** as org-specific |
| Chart parts (title/subtitle case) | 38, 43 |
| ... On the web (text in a single PNG) | 73 |
| ... In print | 73, 44 |
| Using color (palette, categorical/sequential/diverging/binary, eight-color hierarchy) | 23, 28, 30 |
| ... Text and contrast, WCAG 2.0 AA | 33 |
| Best practices: what is the right chart | 4, 5 |
| ... Creating effective charts | 86, 30, 62, 29, 37, 41, 39 |
| ... Absolutes: nonzero baselines | 9 |
| ... Absolutes: dual axis | 13 |
| ... Absolutes: pie slices < 5 | 28, 54 |
| ... Absolutes: categories < 7 | 28 |
| Accessibility: alt text | 71 |
| ... color contrast | 33 |
| ... no merged cells in tables | 55 |
| ... built-in Word styles | **excluded**: document authoring |
| ... plain language | 37 |
| ... group ordering | 57 |
| Chart examples (bar, dot, line, sparkline, slope, area, Gantt, pie, treemap, unit, scatter, bubble, connected scatter, heatmap, beeswarm, box-whisker, fan, histogram, strip) | 5 collectively; specifics → 9, 39, 28, 13, 41, 53, 23, 57, 49, 48, 58 |
| Maps: should you use a map | 22 |
| ... projections | 21 |
| ... kinds of maps | 5 |
| ... map colors | 23, 32 |
| Tables | 18, 43, 44, 45 |
| Tables for the web | 80 |

**Every section maps.**

## Datawrapper Academy

| Article / section | Topics |
|---|---|
| Choosing colors: same color for same variables | 30 |
| ... explain color encoding | 42 |
| ... grey as context | 29 |
| ... contrast requirements | 33 |
| ... color positioning / high contrast for small marks | 33, 29 |
| ... intuitive colors | 31 |
| ... lightness for gradients | 23, 24 |
| ... palette type matching | 23 |
| ... lightness over hue alone | 24, 26 |
| ... diverging palettes | 32 |
| ... colorblind accessibility | 26 |
| Accessibility: alternative descriptions | 71 |
| ... colorblind checker | 26 |
| ... data download | 72 |
| ... screen-reader defaults | 74 |
| Annotate tab (title, description, notes, byline, source, alt description) | 37, 41, 44, 45, 71 |
| Number formats / divide and round | 18 |
| Setting the number locale | 19 |
| Changing visualization size (responsive, mobile 380-400px, label switching, breakpoints) | 80, 39, 62 |
| Locator maps for mobile | 80 |
| "What to consider when creating X" series | 5 |
| Embedding mechanics | **excluded**: platform-specific delivery |

## FT Visual Vocabulary

| Category | Topics |
|---|---|
| Deviation / Correlation / Ranking / Distribution / Change over Time / Part-to-Whole / Magnitude / Spatial / Flow | 5 (all nine); Part-to-Whole → 54, Spatial → 21/22, Distribution → 50 |
| D3 templates in FT style | 79 |
| "not an attempt to teach everyone how to make charts, but how to recognise the opportunities" | 4 |

## W3C WAI, *Complex Images*

| Item | Topics |
|---|---|
| Two-part alternative: short plus long description | 71 |
| Long description conveys scales, values, relationships, trends | 71, 72 |

---

## Corrections found when each source got its own page (2026-08-23)

The per-source pages were written by agents that opened the sources. They found four things wrong with this roll-call, which is the roll-call working as intended.

- **Tufte has no row here at all**, and his name appears nowhere in `inventory.md` or `refutations.md` except secondhand through Wilke ch. 23. He is the canon's most-cited author on this subject and he entered the 92 topics only by quotation. **The roll-call's guarantee does not cover a source that was never enumerated**: an omission shows up as an unmapped chapter only if the chapters were listed. See [sources/tufte.md](sources/tufte.md), which now lists nine chapters for whoever has a copy.
- **Munzner ch. 6 has nine rules of thumb, not the eight mapped above.** The missing one is **No Unjustified 2D**, which is the one most relevant to network layouts. Also, "Get It Right in Black and White" is Maureen Stone's phrase, cited by Munzner to her 2010 post rather than coined by her.
- **The Few mappings are partly extrapolation.** Topics 6 and 3 check out. The mappings to 16, 33, 42, 45 and 46 do not: Few's *Completeness* is about **comparison context** ("comparisons to targets, measures of the norm, and historical values"), not legends, notes and sample size, and **no inventory topic covers it**. His *Truthfulness* is accuracy **and validity**, and **validity has no topic at all**. Two real gaps, found only because his primary turned out to be readable after all.
- **Two quotes could not be located in the available material.** Topic 7's Munzner quote ("express all of, and only...") appears nowhere in her 689-slide deck, and topic 91's Cairo quote ("paramount among these five") appears nowhere in the 46-page sample, where the word "paramount" does not occur. Both are flagged on their source pages rather than removed, since neither the book nor the full text was reached.

**One recorded limitation reversed.** Few's profile, described above as an unreadable, password-protected binary, is neither. It was read in full, and the mappings drawn from it are corrected in the section above.

## Sources deliberately not consulted

Named so the next pass knows where to look rather than re-deriving the same list:

- **Cairo, *How Charts Lie***. Would sharpen truncation, inverted axes and map distortion (10, 11, 21).
- **Chartability** (Elavsky, Bennett & Moritz, EuroVis 2022). 50 accessibility heuristics under POUR+CAF, CC-BY-SA, with a 14-test shortlist. Discovered *after* the accessibility topics were derived. **Importing beats deriving here**: the inventory's four accessibility topics are roughly three of its fifty.
- **The statistical-reporting canon.** Cumming/Fidler/Vaux, Weissgerber, Belia, Song & Szafir. Not in the original source set at all, which is exactly why topics 46, 55 and 56 came out weakly sourced. See [refutations.md](refutations.md).
- **Draco** (Moritz et al., TVCG 2019). Formalizes encoding-choice knowledge as constraints with weights learned from experiment. Covers mark and channel selection only; does not touch titles, annotation or narrative.
