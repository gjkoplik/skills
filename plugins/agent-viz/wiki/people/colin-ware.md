---
type: person
status: primary-read
status_partial: true
retrieved: 2026-08-23
---

# Colin Ware

**What they are known for.** *Information Visualization: Perception for Design*, the standard reference on the perceptual basis of visualization, by a researcher trained in both computer science and the psychology of perception. His own experiments run from map color sequences in 1988 to colormap resolving power in 2019, plus node-link readability studies.

**How this was read.** `primary-read` for his own experiments, `secondary-only` for the book. Four of his papers were extracted locally with `pdftotext`. The book was not opened; its chapter list is from the publisher's product page. Each work carries its own label in [the table](#works-and-where-they-sit-in-this-wiki).

**What they are good for.** *Why does this work*, rather than *what should I do*: the point where a convention becomes a claim about the visual system. He comes from vision science, not statistics or design practice, and has run node-link experiments.

**What they do not settle.** Chart-type choice, narrative structure, production, reproducibility, audiences, organizations. The book is a textbook synthesizing other people's experiments, so "Ware showed that" cites a secondary source unless the claim is one of his own results below.

---

## What their work established

### Color sequences, 1988

The 2023 rainbow essay rests on this paper. It splits map reading into **metric** tasks (read a quantity off a key) and **form** tasks (see the shape of the surface). Its theory predicts a spectrum scale wins the first and a gray scale the second, because form perception runs through the luminance channel. With ten color-normal subjects and five sequences, the results "only partially confirm the form hypothesis." The third closing rule of thumb is the logic of viridis and turbo, and the content behind "Ware defends rainbows":

> "To create a color sequence that has good properties for revealing both shape and metric quantities, use a sequence that increases monotonically in luminance, while cycling through a range of hues. The hues provide accurate readings from a key, while the luminance conveys the form of the surface."

### Colormap resolving power, 2019

560 Mechanical Turk participants, nine colormaps, three feature sizes, 270 averaged feature-detection thresholds. Unmodified CIELAB overweights the chromatic channels. Luminance alone does better and still fails:

> "We also tested against the hypothesis that L\* by itself could account for the data equally well and found that it could not, although this did better than unmodified CIELAB."

A CIELAB variant with the green-red and yellow-blue terms weighted down to about 0.1 fits the combined data at r² = 0.94. The authors' implication:

> "colormap uniformity is not a simple concept, since the relative weights of chromatic variation and luminance variation change as a function of the spatial frequency of features"

[ware-2023-rainbow-colormaps.md](../studies/ware-2023-rainbow-colormaps.md) carries this paper secondhand, in the essay's words, as showing that "feature detection depends mostly on luminance," and *mostly* is right. Luminance alone was tested and rejected, and the chromatic share depends on feature size.

### Graph aesthetics, 2002

With Purchase, Colpoys and McGill. 43 subjects were timed finding shortest paths of length 3 to 5 in 137 spring-layout drawings. Stepwise regression over eight layout properties gave R² = 0.784. 100 degrees of path bendiness cost 1.7 seconds, and each crossing on the path cost 0.65 seconds:

> "the cognitive cost of a single crossing is approximately the same as 38 degrees of continuity. The practical consequence is that it may be worth allowing for an occasional crossing in a graph layout if it reduces the bendiness of paths."

> "we find that her measurement of the total number of edge crossings in the graph drawing is not a significant indicator of response time. For shortest path tasks, we have shown here that it is the number of edges that cross the shortest path itself that is important, rather than the total number of edges crossings in the drawing."

The authors' stated limit: "More studies are required to determine the robustness of our findings for other than spring layout graphs and for different graph sizes." Subjects were second- and third-year computing students at one university, on shortest-path tasks only. The paper discusses an unexplained negative regression intercept.

### Motion as a highlighting channel, 2004

With Robert Bobrow. Touching a node makes it and its topological neighborhood oscillate. Three experiments on the same 13 subjects favor motion over static highlighting on both speed and errors. The abstract says "we argue from perceptual principles," and at that sample size the paper is a demonstration with supporting measurements, not a settled effect size.

### Visual queries

His later work frames a display as supporting a **visual query**, a pattern the viewer must find for a specific cognitive step. His 2012 keynote slides list what that buys: "How big a problem can be addressed / Visual search requirements / Visual working memory load issues."

## Where his name is used as authority for more than he showed

1. **The rainbow, in both directions.** "Ware says rainbows are fine" and "Ware says rainbows are harmful" both cite opinion. The 2023 Viewpoints article contains no experiment, as [its page](../studies/ware-2023-rainbow-colormaps.md) documents. His 1988 and 2019 measurements say neither; both say luminance does more of the work than people assume.
2. **Preattentive processing.** Rules of the form "the viewer finds the accented item in a fixed short time regardless of how many other items are on screen" get cited to his chapter 5. The experiments are the visual-search tradition he summarizes, where set-size independence holds only for a narrow class of feature searches. [refutations.md](../refutations.md), "Gray plus one accent," records no controlled test of the rule as applied.
3. **Edge crossings.** Ware 2002 gets cited for "minimize crossings." It found total crossings in the drawing not significant, crossings on the traced path significant, and continuity outranking both once path length was factored out.

## What they would object to in a figure

*Reconstruction from his stated priorities, not a response to any actual figure.*

He would ask whether the pattern answering the figure's visual query is resolvable at the size drawn. He has measured hue-only distinctions failing at small feature sizes. He would object to a specific rainbow on luminance grounds rather than ban rainbows, trade a crossing for a straighter path, and count what the reader must hold in visual working memory across panels.

## Works, and where they sit in this wiki

| Work | Status | Where it sits |
|---|---|---|
| *Information Visualization: Perception for Design*, 4th ed. (Morgan Kaufmann, 19 Dec 2019, ISBN 9780128128756) | `secondary-only`. Chapter list from the publisher, [shop.elsevier.com](https://shop.elsevier.com/books/information-visualization/ware/978-0-12-812875-6). | No page. No row in [roll-call.md](../roll-call.md). Absent from [inventory.md](../inventory.md). |
| Ware (1988), "Color Sequences for Univariate Maps: Theory, Experiments, and Principles," *IEEE CG&A* 8(5), 41-49 | `primary-read`. Author preprint, [vislab-ccom.unh.edu/pdfs/ColorSequences.pdf](https://vislab-ccom.unh.edu/pdfs/ColorSequences.pdf). | No page. Named as the evidence in [ware-2023-rainbow-colormaps.md](../studies/ware-2023-rainbow-colormaps.md). Bears on [inventory.md](../inventory.md) topics 23, 24, 25. |
| Ware, Purchase, Colpoys & McGill (2002), "Cognitive Measurements of Graph Aesthetics," *Information Visualization* 1(2), 103-110 | `primary-read`. [vislab-ccom.unh.edu/pdfs/GraphAesthetics.pdf](https://vislab-ccom.unh.edu/pdfs/GraphAesthetics.pdf). | No page. Bears on [chart-types/node-link.md](../chart-types/node-link.md) and [chart-types/network-topology.md](../chart-types/network-topology.md). |
| Ware & Bobrow (2004), "Motion to Support Rapid Interactive Queries on Node-Link Diagrams," *ACM TAP* 1(1) | `primary-read`. [vislab-ccom.unh.edu/pdfs/MotionQueries.pdf](https://vislab-ccom.unh.edu/pdfs/MotionQueries.pdf). | No page. The node-link side of [ghoniem-2004.md](../studies/ghoniem-2004.md) and [okoe-2018.md](../studies/okoe-2018.md). |
| Ware, Turton, Bujack, Samsel, Shrivastava & Rogers (2019), "Measuring and Modeling the Feature Detection Threshold Functions of Colormaps," *IEEE TVCG* 25(9), 2777-2790 | `primary-read`. IEEE PDF. | No page. Cited secondhand in [ware-2023-rainbow-colormaps.md](../studies/ware-2023-rainbow-colormaps.md). |
| Ware, Stone & Szafir (2023), *Rainbow Colormaps Are Not All Bad* | `primary-read` | [studies/ware-2023-rainbow-colormaps.md](../studies/ware-2023-rainbow-colormaps.md) |
| Ware & Franck (1996), "Evaluating Stereo and Motion Cues for Visualizing Information Nets in Three Dimensions," *ACM TOG* 15(2) | Reachable, not read. [vislab-ccom.unh.edu/pdfs/TOGGraph_Net.pdf](https://vislab-ccom.unh.edu/pdfs/TOGGraph_Net.pdf) | No page. The nearest empirical test here of when 3D helps a network view, against Munzner's unsourced "No Unjustified 3D." |
| Ware & Beatty (1988), "Using Color Dimensions to Display Data Dimensions," *Human Factors* 30(2) | `not-reached`. Closed access; no repository copy on Unpaywall or OpenAlex, publisher returns 403, absent from the UNH lab archive. | No page. |
| *Visual Thinking for Design* (2008) / *Visual Thinking for Information Design*, 2nd ed. (2021) | `secondary-only`. The visual-query material is from his 2012 VISIGRAPP keynote deck, extracted locally. | No page. |

All `primary-read` PDFs were extracted locally. The UNH lab archive is an open index of 66 papers at `vislab-ccom.unh.edu/pdfs/`.

The 4th edition's chapters, verbatim from the publisher: 1. Foundations for an Applied Science of Data Visualization. 2. The Environment, Optics, Resolution, and the Display. 3. Lightness, Brightness, Contrast, and Constancy. 4. Color. 5. Visual Salience and Finding Information. 6. Static and Moving Patterns. 7. Space Perception. 8. Visual Objects and Data Objects. 9. Images, Narrative, and Gestures for Explanation. 10. Interacting with Visualizations. 11. Visual Thinking Processes. 12. Designing for Perception (new in this edition). Then ten named **Visual Thinking Algorithms**, placed in no stated chapter, and appendices A (Changing Primaries), B (CIE Color Measurement System) and C (Guidelines).

## Where the book bears on the inventory

With no roll-call row, Ware is invisible to the roll-call's coverage guarantee, the gap the README names for Tufte.

- **Chapter 5** organizes the visual-search literature behind pop-out, and the search behind "gray plus one accent" in [refutations.md](../refutations.md) did not go through it. Preattentive attention enters [inventory.md](../inventory.md) through topic 29, sourced to Datawrapper, Urban and Wilke: practitioners, with no perception source.
- **Chapters 3 and 4** are the lightness-and-contrast mechanism under topic 24 (perceptual uniformity, evidence-backed on matplotlib's docs), topic 33 (text contrast, evidence-backed on WCAG) and topic 27 (grayscale survival, authority-asserted on Munzner's rule-of-thumb name, which her own slides attribute to Maureen Stone). The book was consulted for none of them.
- **Appendix C** is a perception-derived guideline list not yet diffed against [inventory.md](../inventory.md). A topic only Ware has would be a hole. A topic only the inventory has would be a rule with no perceptual basis.
- **Ware 2002** says what makes a single node-link drawing readable, which Ghoniem 2004 and Okoe 2018, the node-link-versus-matrix studies under [chart-types/network-topology.md](../chart-types/network-topology.md), do not. It is open access.

## See also

- [studies/ware-2023-rainbow-colormaps.md](../studies/ware-2023-rainbow-colormaps.md): his rainbow essay, and why it is not evidence
- [concepts/channels.md](../concepts/channels.md): claims channels are the only level the literature speaks at; Ware's book is the counterexample
- [sources/munzner-vad.md](../sources/munzner-vad.md): the other framework book, also `secondary-only` via the publisher's contents
- [william-cleveland.md](william-cleveland.md): the other half of the perception lineage, from statistics rather than vision science
