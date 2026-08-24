# Wilke, *Fundamentals of Data Visualization*

**What it is.** Claus O. Wilke, *Fundamentals of Data Visualization* (O'Reilly, 2019), 30 chapters in three parts. The complete text is free at [clauswilke.com/dataviz](https://clauswilke.com/dataviz/). It is the broadest single source in the canon: it covers chart-type choice, figure-design principles, and the production end (file formats, software, reproducibility) that nothing else in the set touches.

**Status: `primary-read`.** Retrieved 2026-08-23. The chapter pages were pulled with `curl` and stripped to text locally; every quote below was re-extracted from that HTML, not taken from a fetch summary. One caveat that belongs in the status line: the free web version is described on its own welcome page as "the complete author manuscript before final copy-editing and other quality control," licensed CC BY-NC-ND 4.0. Wording in the printed O'Reilly edition may differ slightly.

**What it is good for.** Come back here with: *which chart form does this data relationship want*, and *what is wrong with the figure I already have*. Chapters 5 through 16 are a directory of visualizations organized by relationship (amounts, distributions, proportions, x-y, geospatial, uncertainty). Chapters 17 through 26 are the design-principles half, and they are the part a figure bar actually reuses. Part III is the only place in the canon that treats image formats, plotting-software choice, reproducibility and separation of content from design as first-class quality topics.

**What it does not settle.** Wilke runs no experiments and cites few; nearly everything here is authority-asserted, which the inventory labels correctly. Accessibility is limited to color-vision deficiency: no alt text, no screen readers, no contrast ratios. There is nothing on interaction, nothing on latency, and nothing on the statistical-reporting questions Cairo covers. The data-ink discussion is a corrective to Tufte, not evidence about him; see [tufte.md](tufte.md) and [refutations.md](../refutations.md).

---

## Structure

Three parts, 30 chapters.

- **Part I, From data to visualization** (chs. 2 to 16). Aesthetics and scales; coordinate systems and axes; color scales; a directory of visualizations; then one chapter each on amounts, histograms and densities, ECDFs and q-q plots, many distributions at once, proportions, nested proportions, associations, time series, trends, geospatial data, and uncertainty.
- **Part II, Principles of figure design** (chs. 17 to 26). Proportional ink; overlapping points; common pitfalls of color use; redundant coding; multi-panel figures; titles, captions and tables; balance the data and the context; use larger axis labels; avoid line drawings; don't go 3D.
- **Part III, Miscellaneous topics** (chs. 27 to 30). Image file formats; choosing visualization software (with subsections on reproducibility and repeatability, exploration versus presentation, and separation of content and design); telling a story and making a point; annotated bibliography.

The full chapter-to-topic mapping is in [roll-call.md](../roll-call.md), which records that every substantive chapter maps and none are unmapped.

## The three-way labeling scheme, which is worth stealing

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

Two smaller places where a reader should notice the boundary of the claim: chapter 14 treats bin width and smoothing bandwidth as analysis choices without giving a rule, and chapter 17's proportional-ink principle is stated as a principle rather than measured. Both are fine; neither is evidence.

## Inventory topics it grounds

Per [roll-call.md](../roll-call.md), do not recompute: 2, 5, 6, 7, 8, 9, 12, 14, 16, 17, 18, 20, 21, 22, 23, 26, 29, 35, 37, 39, 43, 48, 49, 50, 51, 52, 53, 54, 56, 58, 59, 60, 62, 63, 64, 66, 67, 68, 69, 70, 75, 76, 77, 78, 79, 85, 86, 87, 88, 91.

That is more topics than any other source in the set, which is why "the canon" in this project is really Wilke plus corrections.

## What the project got wrong about it

Nothing substantive. One attribution nit, recorded here and on the Tufte page: inventory topic 67 cites `Wilke ch. 23: "Maximize the data-ink ratio, within reason."` The sentence is Tufte's, quoted by Wilke, and the italics on *within reason* are Wilke's own added emphasis. The correct citation is "Tufte, quoted in Wilke ch. 23." See [tufte.md](tufte.md).

## Links

- [inventory.md](../inventory.md), the topics this source grounds
- [roll-call.md](../roll-call.md), the chapter-by-chapter mapping
- [refutations.md](../refutations.md), data-ink, chartjunk, aspect ratio
- [tufte.md](tufte.md), the source of the data-ink material in ch. 23
- [checks/matplotlib.md](../checks/matplotlib.md), runnable versions of the mechanizable rules
