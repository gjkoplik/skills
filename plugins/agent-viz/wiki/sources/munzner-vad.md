---
type: source
status: secondary-only
status_partial: true
author: tamara-munzner
retrieved: 2026-08-27
---

# Munzner, *Visualization Analysis and Design*

Tamara Munzner, *Visualization Analysis and Design* (A K Peters / CRC Press, 2014). A framework book, not a chart cookbook. It decomposes every design into *what* data there is, *why* the user is looking, and *how* the encoding and interaction are built. Companion site at [cs.ubc.ca/~tmm/vadbook](https://www.cs.ubc.ca/~tmm/vadbook/).

**What it is good for.** *What is this figure for, what is the data made of, and is the most important attribute on the most accurate channel.* It is the one canon source that seriously covers **networks and trees** (node-link versus matrix as a size-dependent choice), **interaction** as an encoding decision rather than a feature, and **reduction** (filter, aggregate) as a legitimate design move.

**What it does not settle.** Titles, captions, annotation, source lines, number formatting, locale, narrative. Accessibility beyond "get it right in black and white". Production and reproducibility. Chapter 4's four-levels validation framework is research methodology, excluded from the inventory on purpose.

**How this was read.** The book is not free and was not read. Chapter and section names come from the publisher's section-level table of contents (routledge.com product page, fetched with `curl` and stripped locally), the book's own outline. The rest comes from the companion site and two of Munzner's slide decks, both from that site and text-extracted locally with `pypdf`: the 689-slide `vadallslides-2021.pdf` (68 MB), covering the whole book, and the 2021 deck `VAD-2021.pdf` (541 slides, 53 MB, identity-checked against its title slide), which supplies the idiom listing. Every quote below is from the slides: the author's words on the same material, a stronger secondary than a review, but not the book's sentences. In `VAD-2021.pdf` the spatial-data section is captioned "Spatial Data (Ch 9)" although the book's chapter 9 is Arrange Networks and Trees and its spatial chapter is 8; the surrounding content is the spatial chapter, so this is a slide typo. And two slides embed page images from a **draft galley** of the book, watermarked "Permission needed" and numbered against a chapter scheme the published book does not use. They are the only book prose reached and are not quoted.

## Structure

Fifteen chapters, from the publisher's listing:

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

## The idioms, chapter by chapter, from the author's slides

Munzner files a chart type, an "idiom", by **what the encoding arranges**: a table, spatial data, or a network. Each entry is a slide titled `Idiom: <name>` in `VAD-2021.pdf`, in deck order. The listing vouches for what she teaches under each chapter heading, not for the book's prose.

| Chapter | Idioms named |
|---|---|
| **7. Arrange Tables** | scatterplot, bar chart, stacked bar chart, streamgraph, dot / line chart, indexed line chart, Gantt chart, slopegraph, heatmap, cluster heatmap, radial bar chart, star plot, radar plot, pie chart, **coxcomb chart**, normalized stacked bar chart, glyphmaps, **SPLOM**, parallel coordinates, dense software overviews |
| **8. Arrange Spatial Data** | choropleth map, symbol map, contiguous cartogram, grid cartogram, dot density map, topographic map, isosurfaces, direct volume rendering, similarity-clustered streamlines, ellipsoid tensor glyphs |
| **9. Arrange Networks and Trees** | force-directed placement, circular layouts and **arc diagrams**, adjacency matrix view, NodeTrix, radial node-link tree, **treemap**, implicit tree layouts (**sunburst**, **icicle plot**), GrouseFlocks, sfdp, **hierarchical edge bundling** |
| **11 and 12. Manipulate and Facet** | re-encode, change parameters, reorder, change alignment, animated transitions, scrollytelling, linked highlighting, overview-detail views, tooltips, small multiples, reorderable lists, **trellis plots** |
| **13. Reduce Items and Attributes** | cross filtering, **histogram**, scented widgets, **boxplot**, continuous scatterplot, hierarchical parallel coordinates, dimensionality reduction |
| **14. Embed: Focus+Context** | DOITrees Revisited, fisheye lens |

Chapters 1 to 6 and 10 have no idiom slides. Four filings differ structurally from the two chart catalogs in this corpus:

- **Treemap and sunburst are tree layouts**, because they encode containment. [schwabish.md](schwabish.md) and this tier file both under Part-to-Whole. One drawing answers both a composition and a hierarchy question, which is why [../chart-types/README.md](../chart-types/README.md) stores types flat.
- **Histogram and boxplot are reduction idioms** (chapter 13), where every other scheme here calls them distribution charts. Munzner treats them as what gets drawn after the decision to aggregate, a claim about workflow rather than the chart.
- **Streamgraph, Gantt, slopegraph, pie, radar and parallel coordinates are all table arrangements.** Schwabish spreads them across Time, Relationship and Comparing Categories, and the FT across Change over Time, Magnitude and Correlation. Munzner splits by dataset type, so they share one bucket.
- **Arc diagrams are a restricted node-link layout**: "lay out nodes around circle or along line". This deck sources the name for this tier's network index.

The deck is the corpus's only source for: coxcomb chart, star plot, SPLOM, icicle plot, cluster heatmap, glyphmap, trellis plot, contiguous cartogram, grid cartogram, symbol map (aliases "proportional symbol maps" and "graduated symbol maps" on the same slide), hierarchical edge bundling, indexed line chart. Slide titles are a weaker warrant than the book definitions in [wilke-fundamentals.md](wilke-fundamentals.md), and a stronger one than a catalog contents line, since most carry a data-and-encoding breakdown.

## Choropleths

[../chart-types/choropleth-map.md](../chart-types/choropleth-map.md) records classification as an open hole. The deck's recommendations slide states the surrounding conditions:

> only use when central task is understanding spatial relationships
> show only one variable at a time
> normalize when appropriate
> be careful when choosing colors & bins
> best case: regions are roughly equal sized

Failures: "visual salience depends on region size, not true importance wrt attribute value", and "most attributes just show where people live", a spurious-correlation argument for normalizing. Symbol maps are "often a good alternative to choropleth maps". Dot density maps get the same caution: "show population density (correlated with attribute), not effect of interest".

"Be careful when choosing colors & bins" is as far as the deck goes on classification; it names no break algorithm. Slides, so `authority-asserted`, and unvouched as to what chapter 8 argues.

## Chapter 6, the rules of thumb, from the publisher's section list

Eight rules:

- No Unjustified 3D
- **No Unjustified 2D**
- Eyes Beat Memory
- Resolution over Immersion
- Overview First, Zoom and Filter, Details on Demand
- Responsiveness Is Required
- Get It Right in Black and White
- Function First, Form Next

(plus "Why and When to Follow Rules of Thumb?" and "The Big Picture" as framing sections)

[roll-call.md](../roll-call.md) maps seven and omits **No Unjustified 2D** (no spatial layout for network data when a text list reads better), the rule most relevant to graph visualization. Its caveat that the rule names were "confirmed across two independent slide decks (UBC and HKUST)" is superseded by this section list.

## What the slides say

Channel choice:

> expressiveness: match channel type to data type
> effectiveness: some channels are better than others

Magnitude channels, in the slides' order: position on common scale, position on unaligned scale, length (1D size), tilt/angle, area (2D size), depth (3D position), color luminance, color saturation, curvature, volume (3D size). Identity channels: spatial region, color hue, motion, shape.

On 3D:

> 3D legitimate for true 3D spatial data. 3D needs very careful justification for abstract data. Enthusiasm in 1990s, but now skepticism. Be especially careful with 3D for point clouds or networks.

Mechanisms: occlusion hides information, perspective distortion "interferes with all size channel encodings", and tilted text is far less legible.

On function first:

> dangerous to start with aesthetics. Usually impossible to add function retroactively.

On responsiveness, the chapter's one quantitative rule:

> 0.1 seconds: perceptual processing. Subsecond response for mouseover highlighting.
> 1 second: immediate response. Fast response after mouseclick, button press.
> 10 seconds: brief tasks. Bounded response after dialog box.

"Get It Right in Black and White" is Maureen Stone's phrase, not Munzner's. The slides cite Stone's 2010 post of that title.

Node-link versus matrix, where two studies in this corpus disagree, gets a scoped conclusion:

> node-link best for small networks
> matrix best for large networks

with "if tasks don't involve path tracing!" attached, citing [Ghoniem et al.](../studies/ghoniem-2004.md). The adjacency-matrix slide gives a scalability figure of 1K nodes and 1M edges. The slides relay these; they did not measure them.

## Not confirmed

Inventory topic 7 attributes this to Munzner:

> "the visual encoding should express all of, and only, the information in the dataset attributes"

It appears nowhere in the 689-slide deck, which says "match channel type to data type". It may be in the book, and is unvouched until someone opens chapter 5.

## Where its advice is contested

Neither point is a refutation.

- **The channel-effectiveness ranking** has an experimental lineage from Cleveland and McGill onward, and the inventory labels it evidence-backed. Its ordering is better supported than any gap between adjacent channels.
- **Aspect ratio** does not appear in Munzner's table of contents or slides, and the banking-to-45-degrees result it would have rested on is scope-limited ([refutations.md](../refutations.md)).

The rules of thumb are authority-asserted. "No Unjustified 3D" has perceptual arguments in the slides and no controlled study attached in this reading.

## Inventory topics it grounds

Per [roll-call.md](../roll-call.md): 1, 2, 4, 5, 6, 7, 21, 22, 23 through 36, 57, 61, 62, 63, 68, 82, 83, 84, 92. Chapters 4 (not mechanizable for a one-off chart) and 15 (worked examples) are stated exclusions.

## Links

- [inventory.md](../inventory.md): the topics this source grounds
- [roll-call.md](../roll-call.md): the chapter-by-chapter mapping
- [refutations.md](../refutations.md): aspect ratio
- [wilke-fundamentals.md](wilke-fundamentals.md): the complementary source; Wilke covers what Munzner skips (text, annotation, production) and vice versa
- [schwabish.md](schwabish.md): the other catalog whose memberships are recorded but whose prose is unread
- [../chart-types/aliases.md](../chart-types/aliases.md): where the idiom names above resolve
