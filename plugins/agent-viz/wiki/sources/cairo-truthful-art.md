---
type: source
status: secondary-only
status_partial: true
author: alberto-cairo
retrieved: 2026-08-27
---

# Cairo, *The Truthful Art*

Alberto Cairo, *The Truthful Art: Data, Charts, and Maps for Communication* (New Riders, 2016). Twelve chapters in four parts. About half the book is statistics for communicators (distributions, variance, correlation, regression, standard error, confidence intervals, significance), written for people who make charts rather than people who run models.

**What it is good for.** Whether a chart over-reads its data. Cairo is the only source in the canon with real pages on conjecture and hypothesis, study quality, sample variation, standard error, confidence intervals, disclosing uncertainty, and significance versus effect size versus power. By its contents he also covers how time-series charts mislead, index construction, and choropleth classification, though those chapters were not read.

**What it does not settle.** The five qualities at the primary level (below). Chartcraft is thinner than in Wilke or the newsroom style guides: no production, accessibility or software, and less color.

**How this was read.** `secondary-only` for the argument, `primary-read` for the structure. Peachpit's sample PDF of the book (`peachpit.com/content/images/9780321934079/samplepages/9780321934079.pdf`) was downloaded with `curl` and text-extracted locally with `pypdf`. It holds the front matter with the full section-level contents, the preface, chapter 4 in full, and the complete index. Chapter 2, "The Five Qualities of Great Visualizations", is not in the sample and was not read. A second pass mined the sample's contents and index for chapter 10 (choropleth classification) and chapter 11 (uncertainty), but neither chapter was reached, so only their titles and placement are vouched.

A complete PDF of chapter 10 served from an official EU course-materials path (`data.europa.eu/sites/default/files/course/`) carries a Pearson `ptg` watermark and a Safari footer, "From the Library of Alberto Cairo", on every page. It is a DRM-stripped ebook, not a licensed excerpt. It was deleted unread, and nothing here comes from it.

Cairo's 2014 blog post "The challenges of classification in choropleth maps", reached through a Wayback snapshot because the original URL now 404s, is four sentences on a New York Times map: "Building classes for choropleth maps is always tricky business. By grouping values together as intervals, you always put yourself at the risk of hiding important nuances in the data. There are reliable guidelines you can follow, but the process always requires a good dose of common sense." On that map, "I'm not sure that using equal intervals is the best choice here".

*How Charts Lie* (2019) is `not-reached`. No retrieval was attempted and nothing in the wiki rests on it. [roll-call.md](../roll-call.md) names it as a gap.

---

## Structure

Four parts, twelve chapters, from the book's own contents page.

- **Part I, Foundations.** 1. What We Talk About When We Talk About Visualization (27). 2. The Five Qualities of Great Visualizations (41).
- **Part II, Truthful.** 3. The Truth Continuum (69). 4. Of Conjectures and Uncertainty (99).
- **Part III, Functional.** 5. Basic Principles of Visualization (121). 6. Exploring Data with Simple Charts (151). 7. Visualizing Distributions (167). 8. Revealing Change (199). 9. Seeing Relationships (233). 10. Mapping Data (263). 11. Uncertainty and Significance (299).
- **Part IV, Practice.** 12. On Creativity and Innovation (329), plus an epilogue.

The publisher's web listing calls chapter 11 "Confidence and Significance". The printed contents page, the better source, says "Uncertainty and Significance".

## The five qualities, confirmed at the name level

Chapter 2's section list, with the book's own page numbers:

| Quality | Page |
|---|---|
| Truthful | 45 |
| Functional | 50 |
| Beautiful | 53 |
| Insightful | 59 |
| Enlightening | 60 |

Two claims the wiki carries remain unverified.

1. Inventory topic 91 quotes Cairo: *"striving to be truthful is paramount among these five."* That sentence was not found in anything reached, and the word "paramount" does not occur anywhere in the 46-page sample. The claim is plausible (Part II is titled "Truthful" and the book is called *The Truthful Art*) but secondary.
2. [roll-call.md](../roll-call.md) excludes "Enlightening" on the grounds that Cairo defines it as the composite of the other four. That gloss came from a secondary summary. The contents page gives Enlightening its own section at page 60, between Insightful and the chapter's "To Learn More", which fits either reading.

## Quotes verified verbatim (chapter 4 only)

The chapter's thesis:

> Here's a dirty little secret about data: it's always noisy and uncertain.

On why:

> Data always vary randomly because the object of our inquiries, nature itself, is also random. We can analyze and predict events in nature with an increasing amount of precision and accuracy, thanks to improvements in our techniques and instruments, but a certain amount of random variation, which gives rise to uncertainty, is inevitable.

On reading past an abstract, a methods point most chart books never make:

> reporting on a study after reading just its abstract is dangerous

On noise versus signal, he weighs himself daily for six weeks, and the downward trend "only becomes visible when I display more than five or six days in a row. If I zoom in too much to the chart and just pay attention to two or three days, I'd be fooled into thinking that the noise in the data means something."

## Where its advice is contested

Nothing in this wiki contests Cairo, largely because so little of him was reached.

- **Truncation, inverted axes and map projection** (inventory topics 10, 11, 21) are what *How Charts Lie* would sharpen, and it was not opened. The evidence on truncation remedies does not favor the axis-break glyph ([refutations.md](../refutations.md)).
- **Log scales** (chapter 8's "From Ratios to Logs") have stronger evidence than any design book states: log-log comprehension fails even for expert audiences ([refutations.md](../refutations.md)).

## Inventory topics it grounds

Per [roll-call.md](../roll-call.md), not recomputed here: 6, 9, 10, 11, 37, 41, 50, 55, 89, 91, 92. All were mapped through the five qualities. Chapters 3, 4, 7, 8, 9, 10 and 11 hold more, particularly on uncertainty and misleading time series.

## What the project got wrong about it

Nothing wrong, one thing thin. The roll-call mapped Cairo through a secondary summary of the five qualities, the book's least distinctive part, rather than through the statistical chapters. That is why he grounds far fewer topics than Wilke.

## Links

- [inventory.md](../inventory.md): the topics this source grounds
- [roll-call.md](../roll-call.md): the mapping, and the "not consulted" list that names *How Charts Lie*
- [refutations.md](../refutations.md): truncation remedies, log scales, and the statistical-reporting canon that was missing from the original source set
- [few-effectiveness-profile.md](few-effectiveness-profile.md): the other criteria-list source, and the only one whose primary is free
