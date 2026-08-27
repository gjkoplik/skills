---
type: source
status: secondary-only
status_partial: true
author: tamara-munzner
retrieved: 2026-08-27
---

# Munzner, *Visualization Analysis and Design*

Tamara Munzner, *Visualization Analysis and Design* (A K Peters / CRC Press, 2014, 428 pp). A framework book rather than a chart cookbook: it decomposes every design into *what* data you have, *why* the user is looking, and *how* the encoding and interaction are built. Companion site at [cs.ubc.ca/~tmm/vadbook](https://www.cs.ubc.ca/~tmm/vadbook/).

**How this was read.** The book is not free and was not read. Retrieved 2026-08-23:

1. the publisher's **section-level** table of contents (routledge.com product page, fetched with `curl` and stripped locally), which is the book's own outline rather than a third-party reconstruction;
2. **Munzner's own 689-slide deck** covering the entire book (`vadallslides-2021.pdf`, 68 MB, from her companion site), downloaded and text-extracted locally with `pypdf`;
3. the companion site itself.

Every quote below is **from the slides, not the book**. They are the author's own words on the same material, which is a stronger secondary than a review or a summary, and it is still not the book's sentences. Do not present them as quotations from *Visualization Analysis and Design*.

This is an upgrade on the previous state, which had chapter names from two third-party decks and no rule text at all.

**Second pass, 2026-08-27**, aimed at one question: can the *idioms* (Munzner's word for chart types) be recovered chapter by chapter, the way [schwabish.md](schwabish.md) recovered them from a contents page? **Partly.** The publisher's table of contents is section-level and stops above the idioms, so it names "Connection: Link Marks" and "Matrix Views" but no chart. The **2021 slide deck** (`VAD-2021.pdf`, 541 slides, 53 MB, from the companion site, extracted locally with `pypdf` and identity-checked against its title slide) does name them, one per slide, in the book's chapter order. The listing below is from that deck. **It vouches for what the author teaches under each chapter heading. It does not vouch for a word of the book's prose.**

Two provenance details from that extraction. The deck's spatial-data section is captioned "Spatial Data (Ch 9)" although the book's chapter 9 is Arrange Networks and Trees and its spatial chapter is 8; the surrounding content is the spatial chapter, so this is a slide typo. And two slides embed page images from a **draft galley** of the book, watermarked "Permission needed" and numbered against a chapter scheme the published book does not use. They are the only book prose reached in this project and they are not quoted here, because a draft with different chapter numbers is not the book.

**What it is good for.** Come back here with: *what is this figure for, what is the data actually made of, and is the most important attribute on the most accurate channel*. Munzner is also the only canon source with serious coverage of **networks and trees** (node-link versus matrix as a size-dependent choice), **interaction** as an encoding decision rather than a feature, and **reduction** (filter, aggregate) as a legitimate design move.

**What it does not settle.** Nothing on titles, captions, annotation, source lines, number formatting, locale, or narrative. No accessibility beyond "get it right in black and white". No production or reproducibility. The four-levels validation framework in chapter 4 is research methodology and is deliberately excluded from the inventory, not overlooked.

---

## Structure

Fifteen chapters. From the publisher's own listing:

1. What's Vis, and Why Do It?
2. What: Data Abstraction
3. Why: Task Abstraction
4. Analysis: Four Levels for Validation
5. Marks and Channels
6. Rules of Thumb
7. Arrange Tables
8. Arrange Spatial Data
9. Arrange Networks and Trees
10. Map Color and Other Channels
11. Manipulate View
12. Facet into Multiple Views
13. Reduce Items and Attributes
14. Embed: Focus+Context
15. Analysis Case Studies

## The idioms, chapter by chapter, from the author's own slides

Munzner does not organize by data relationship; she organizes by **what the encoding arranges**. A chart type is an "idiom", and where it sits is decided by whether it arranges a table, spatial data, or a network. Every entry below is a slide titled `Idiom: <name>` in the 2021 deck, in the order it appears.

| Chapter | Idioms named |
|---|---|
| **7. Arrange Tables** | scatterplot, bar chart, stacked bar chart, streamgraph, dot / line chart, indexed line chart, Gantt chart, slopegraph, heatmap, cluster heatmap, radial bar chart, star plot, radar plot, pie chart, **coxcomb chart**, normalized stacked bar chart, glyphmaps, **SPLOM**, parallel coordinates, dense software overviews |
| **8. Arrange Spatial Data** | choropleth map, symbol map, contiguous cartogram, grid cartogram, dot density map, topographic map, isosurfaces, direct volume rendering, similarity-clustered streamlines, ellipsoid tensor glyphs |
| **9. Arrange Networks and Trees** | force-directed placement, circular layouts and **arc diagrams**, adjacency matrix view, NodeTrix, radial node-link tree, **treemap**, implicit tree layouts (**sunburst**, **icicle plot**), GrouseFlocks, sfdp, **hierarchical edge bundling** |
| **11 and 12. Manipulate and Facet** | re-encode, change parameters, reorder, change alignment, animated transitions, scrollytelling, linked highlighting, overview-detail views, tooltips, small multiples, reorderable lists, **trellis plots** |
| **13. Reduce Items and Attributes** | cross filtering, **histogram**, scented widgets, **boxplot**, continuous scatterplot, hierarchical parallel coordinates, dimensionality reduction |
| **14. Embed: Focus+Context** | DOITrees Revisited, fisheye lens |

Chapters 1 to 6 and 10 carry no idiom slides; they are the framework and the channel material.

**Four filings here disagree with the two chart catalogs in this corpus, and the disagreements are structural rather than arbitrary.**

- **Treemap and sunburst are tree layouts**, filed under networks and trees, because what they encode is containment. [schwabish.md](schwabish.md) files both under Part-to-Whole, and so does this tier. Neither is wrong: the same drawing answers a composition question and a hierarchy question, which is precisely why [../chart-types/README.md](../chart-types/README.md) stores types flat.
- **Histogram and boxplot are reduction idioms**, filed in chapter 13 with filtering and aggregation rather than with distributions. Every other scheme here files them as distribution charts. Munzner's reading is that they are what you draw *after* deciding to aggregate, which is a claim about the workflow rather than about the chart.
- **Streamgraph, Gantt, slopegraph, pie, radar and parallel coordinates are all table arrangements.** Schwabish spreads the same six across Time, Relationship and Comparing Categories; the FT spreads them across Change over Time, Magnitude and Correlation. Munzner has no bucket for them to disagree about, because her top-level split is by dataset type.
- **Arc diagrams are a node-link layout**, a restricted one: "lay out nodes around circle or along line". This tier's network index names arc diagrams with no source behind the name, and this is one.

**Names this deck vouches that nothing else in the corpus does:** coxcomb chart, star plot, SPLOM, icicle plot, cluster heatmap, glyphmap, trellis plot, contiguous cartogram, grid cartogram, symbol map (with "proportional symbol maps" and "graduated symbol maps" given as aliases on the same slide), hierarchical edge bundling, indexed line chart. It is a weaker warrant than [wilke-fundamentals.md](wilke-fundamentals.md) gives, because these are slide titles rather than definitions in a book, and it is a stronger one than a catalog contents line, because most carry a data-and-encoding breakdown on the same slide.

## Choropleths, which is the one place this fills a hole downstream

[../chart-types/choropleth-map.md](../chart-types/choropleth-map.md) records classification as an open hole. The deck does not close it, and it does state the surrounding conditions compactly. From the recommendations slide:

> only use when central task is understanding spatial relationships
> show only one variable at a time
> normalize when appropriate
> be careful when choosing colors & bins
> best case: regions are roughly equal sized

with the failure named rather than asserted: "visual salience depends on region size, not true importance wrt attribute value", and "most attributes just show where people live", which is a spurious-correlation argument for normalizing. The same section files **symbol maps** as "often a good alternative to choropleth maps", and gives dot density maps the same normalization caution: "show population density (correlated with attribute), not effect of interest".

"Be careful when choosing colors & bins" is as far as the deck goes on classification. It names no break algorithm. Slides, not the book, so `authority-asserted` and unvouched as to what chapter 8 argues.

## Chapter 6, the rules of thumb, from the publisher's section list

This is the chapter a figure bar borrows from. The section-level TOC names **eight** rules, listed here as extracted, plus two framing sections:

- No Unjustified 3D
- **No Unjustified 2D**
- Eyes Beat Memory
- Resolution over Immersion
- Overview First, Zoom and Filter, Details on Demand
- Responsiveness Is Required
- Get It Right in Black and White
- Function First, Form Next

(plus "Why and When to Follow Rules of Thumb?" and "The Big Picture" as the framing sections)

[roll-call.md](../roll-call.md) maps **seven** of the eight and omits **No Unjustified 2D**, which is about not forcing network data into a spatial layout when a text list would read better. It is the rule most directly relevant to graph visualization, so the omission matters more than its size suggests. *Corrected 2026-08-27: this page and roll-call previously both said the chapter has nine rules, while the list extracted here has eight and roll-call maps seven. If anyone re-reads the TOC and finds a ninth, that is a correction to record rather than a number to restore.*

## What the slides actually say

On channel choice, the compact statement of both principles:

> expressiveness: match channel type to data type
> effectiveness: some channels are better than others

The effectiveness ranking as the slides present it, magnitude channels in order: position on common scale, position on unaligned scale, length (1D size), tilt/angle, area (2D size), depth (3D position), color luminance, color saturation, curvature, volume (3D size). Identity channels: spatial region, color hue, motion, shape.

On 3D:

> 3D legitimate for true 3D spatial data. 3D needs very careful justification for abstract data. Enthusiasm in 1990s, but now skepticism. Be especially careful with 3D for point clouds or networks.

with the mechanism named rather than asserted: occlusion hides information, perspective distortion "interferes with all size channel encodings", and tilted text is far less legible.

On function first:

> dangerous to start with aesthetics. Usually impossible to add function retroactively.

On responsiveness, which is the only quantitative rule in the chapter:

> 0.1 seconds: perceptual processing. Subsecond response for mouseover highlighting.
> 1 second: immediate response. Fast response after mouseclick, button press.
> 10 seconds: brief tasks. Bounded response after dialog box.

A provenance detail the wiki did not have: **"Get It Right in Black and White" is Maureen Stone's phrase**, not Munzner's. Her slides cite Stone's 2010 post of that title directly.

On node-link versus matrix, which is the one type-level comparison in this corpus that two studies already disagree about, the deck states the conclusion as scoped rather than flat:

> node-link best for small networks
> matrix best for large networks

with "if tasks don't involve path tracing!" attached, and it cites [Ghoniem et al.](../studies/ghoniem-2004.md) for it. Her adjacency-matrix slide also carries a scalability figure, 1K nodes and 1M edges. Both belong to the slides, so they are the author relaying an experiment rather than the experiment, and the experiment already has its own page here.

## Not confirmed

Inventory topic 7 carries this, attributed to Munzner:

> "the visual encoding should express all of, and only, the information in the dataset attributes"

That sentence does not appear anywhere in the 689-slide deck. The slides state expressiveness as "match channel type to data type". The quoted sentence may well be in the book, which was not read. Treat it as unvouched until someone opens chapter 5.

## Where its advice is contested

Two places, neither of them a refutation:

- **The channel-effectiveness ranking** is the one part of Munzner with a real experimental lineage behind it (Cleveland and McGill onward), and the inventory labels it evidence-backed for that reason. The ranking's *ordering* is better supported than any single gap between adjacent channels.
- **Aspect ratio** does not appear in Munzner at all, and the banking-to-45-degrees result it would have rested on is scope-limited. See [refutations.md](../refutations.md).

The rules of thumb themselves are authority-asserted. "No Unjustified 3D" has supporting perceptual arguments in the slides; it does not have a controlled study attached in this project's reading.

## Inventory topics it grounds

Per [roll-call.md](../roll-call.md), do not recompute: 1, 2, 4, 5, 6, 7, 21, 22, 23 through 36 (which already includes 27), 57, 61, 62, 63, 68, 82, 83, 84, 92.

Chapter 4 is a stated exclusion (research-methodology framework, not mechanizable for a one-off chart). Chapter 15 is a stated exclusion (worked examples).

## What the project got wrong about it

- The rules-of-thumb list in the roll-call is missing **No Unjustified 2D**. Fixed above, from the publisher's own section list.
- The roll-call's caveat said rule names were "confirmed across two independent slide decks (UBC and HKUST)". The publisher's section-level TOC is a better source for the same fact and now supersedes it.
- Topic 7's quote is unvouched (above).
- This page previously implied that the publisher's detailed contents was the deepest listing available. It is not the deepest listing of **idioms**, which the slides carry and the contents page does not reach. That is why the section above exists.

## Links

- [inventory.md](../inventory.md), the topics this source grounds
- [roll-call.md](../roll-call.md), the chapter-by-chapter mapping
- [refutations.md](../refutations.md), aspect ratio, dual axes
- [wilke-fundamentals.md](wilke-fundamentals.md), the complementary source; Wilke covers what Munzner skips (text, annotation, production) and vice versa
- [schwabish.md](schwabish.md), the other catalog whose memberships are recorded but whose prose is unread
- [../chart-types/aliases.md](../chart-types/aliases.md), where the idiom names above resolve
