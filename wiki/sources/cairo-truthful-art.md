# Cairo, *The Truthful Art*

**What it is.** Alberto Cairo, *The Truthful Art: Data, Charts, and Maps for Communication* (New Riders, 2016). Twelve chapters in four parts. Roughly half the book is statistics for communicators (distributions, variance, correlation, regression, standard error, confidence intervals, significance) written for people who make charts rather than for people who run models.

**Status: `secondary-only` for the argument, `primary-read` for the structure.** Retrieved 2026-08-23: Peachpit's **46-page sample PDF of the book itself** (`peachpit.com/content/images/9780321934079/samplepages/9780321934079.pdf`), downloaded with `curl` and text-extracted locally with `pypdf`. It contains the front matter (including the full section-level contents), the preface, **chapter 4 in full**, and the complete index.

**Chapter 2, "The Five Qualities of Great Visualizations", is not in the sample and was not read.** The five names and their page numbers are confirmed from the book's own contents page. Cairo's argument about them is not.

*How Charts Lie* (2019): **`not-reached`**, and this project never reached it. Nothing in the wiki rests on it. It was looked for only as a named gap in [roll-call.md](../roll-call.md); no retrieval was attempted in this pass.

**What it is good for.** Come back here with: *am I over-reading this data*. Cairo is the only source in the canon that spends real pages on conjecture and hypothesis, study quality, sample variation, standard error, confidence intervals, disclosing uncertainty, and significance versus effect size versus power. He is also the source for how time-series charts mislead, for index construction, and for choropleth classification.

**What it does not settle.** The five qualities themselves, at the primary level (see below). Chartcraft detail is thinner than Wilke or the newsroom style guides: no production, no accessibility, no software, and color gets a fraction of the space Wilke gives it.

---

## Structure

Four parts, twelve chapters, from the book's own contents page.

- **Part I, Foundations.** 1. What We Talk About When We Talk About Visualization (27). 2. The Five Qualities of Great Visualizations (41).
- **Part II, Truthful.** 3. The Truth Continuum (69). 4. Of Conjectures and Uncertainty (99).
- **Part III, Functional.** 5. Basic Principles of Visualization (121). 6. Exploring Data with Simple Charts (151). 7. Visualizing Distributions (167). 8. Revealing Change (199). 9. Seeing Relationships (233). 10. Mapping Data (263). 11. Uncertainty and Significance (299).
- **Part IV, Practice.** 12. On Creativity and Innovation (329), plus an epilogue.

Note that the printed chapter 11 is titled **"Uncertainty and Significance"**, where the publisher's web listing calls it "Confidence and Significance". The contents page inside the book is the better source.

## The five qualities, confirmed at the name level

Chapter 2's section list, with the book's own page numbers:

| Quality | Page |
|---|---|
| Truthful | 45 |
| Functional | 50 |
| Beautiful | 53 |
| Insightful | 59 |
| Enlightening | 60 |

The names and the ordering are now primary. The content of each section is not.

**Two claims the project carries that are still unverified.**

1. Inventory topic 91 quotes Cairo: *"striving to be truthful is paramount among these five."* That sentence was not found in anything reached. The word "paramount" does not occur anywhere in the 46-page sample. The claim is plausible (Part II is titled "Truthful" and the book is called *The Truthful Art*) and it is still **secondary**.
2. [roll-call.md](../roll-call.md) excludes "Enlightening" on the grounds that Cairo defines it as the composite of the other four. That gloss came from a secondary summary. The contents page gives Enlightening its own section at page 60, between Insightful and the chapter's "To Learn More", which is consistent with either reading. **Open question**, and it would take four pages of chapter 2 to close.

## Quotes verified verbatim (chapter 4 only)

The chapter's thesis, stated flatly:

> Here's a dirty little secret about data: it's always noisy and uncertain.

On why, which is the part that distinguishes Cairo from the design books:

> Data always vary randomly because the object of our inquiries, nature itself, is also random. We can analyze and predict events in nature with an increasing amount of precision and accuracy, thanks to improvements in our techniques and instruments, but a certain amount of random variation, which gives rise to uncertainty, is inevitable.

On reading past an abstract, which is a methods point most chart books never make:

> reporting on a study after reading just its abstract is dangerous

And a worked illustration of noise-versus-signal that a figure bar can use directly: he weighs himself daily for six weeks, and the downward trend "only becomes visible when I display more than five or six days in a row. If I zoom in too much to the chart and just pay attention to two or three days, I'd be fooled into thinking that the noise in the data means something."

## Where its advice is contested

Cairo is not contested inside this wiki, mostly because so little of him was reached. Two adjacent notes:

- **Truncation, inverted axes and map projection** (inventory topics 10, 11, 21) are the topics *How Charts Lie* would sharpen, and it was never opened. The empirical picture on truncation remedies is in [refutations.md](../refutations.md), and it is not encouraging for the axis-break glyph.
- **Log scales** (chapter 8's "From Ratios to Logs") is a place where the evidence is stronger than any design book states it: log-log comprehension fails even for expert audiences. See [refutations.md](../refutations.md).

## Inventory topics it grounds

Per [roll-call.md](../roll-call.md), do not recompute: 6, 9, 10, 11, 37, 41, 50, 55, 89, 91, 92.

All of those were mapped through the five qualities, which is a thin basis for a 400-page book. Chapters 3, 4, 7, 8, 9, 10 and 11 have far more in them than the mapping shows, particularly on uncertainty and on how time-series charts mislead. A second pass over the actual chapters would likely add topics rather than move them.

## What the project got wrong about it

Nothing wrong, one thing thin. The roll-call mapped Cairo through a **secondary summary of the five qualities** rather than through his chapters, which is why he grounds eleven topics while Wilke grounds fifty. The five-qualities frame is the book's least distinctive part; the statistical chapters are the reason to read it.

## Links

- [inventory.md](../inventory.md), the topics this source grounds
- [roll-call.md](../roll-call.md), the mapping and the "not consulted" list that names *How Charts Lie*
- [refutations.md](../refutations.md), truncation remedies, log scales, and the statistical-reporting canon that was missing from the original source set
- [few-effectiveness-profile.md](few-effectiveness-profile.md), the other criteria-list source, and the only one whose primary is free
