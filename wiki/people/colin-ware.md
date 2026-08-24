# Colin Ware

**What they are known for.** Ware wrote *Information Visualization: Perception for Design*, the standard reference on the perceptual basis of everything this wiki argues about, and he holds advanced degrees in both computer science and the psychology of perception. His own experimental work runs from color sequences for maps in 1988 through colormap resolving power in 2019, plus a line of studies on what makes a node-link diagram readable.

**Status: `primary-read` for his own experiments, `secondary-only` for the book.** Splitting the label is not hedging. Four of his papers were downloaded and extracted locally with `pdftotext` and are quoted or characterized from those extractions. The book was not opened, and the chapter list below comes from the publisher's own product page. Every work carries its own label in [the table](#works-and-where-they-sit-in-this-wiki). Retrieval date: **2026-08-23**.

**What they are good for.** Come back here with *why does this work*, not *what should I do*. Ware is the canon's mechanism source: the level at which a rule stops being a convention and becomes a claim about the visual system. He is also the only figure in this set whose center of gravity is vision science rather than statistics or design practice, and the only one who has run experiments on **node-link diagrams specifically**.

**What they do not settle.** Chart-type choice, narrative structure, production, reproducibility, audiences, organizations. And structurally: most of what "Ware says" points at is his synthesis of other people's experiments. The book is a textbook. Citing it for an empirical claim is citing a secondary source unless the claim is one of his own results, and his own results are listed below so you can tell the difference.

---

## What their work actually established

### The book is a synthesis, and that is what it is for

*Information Visualization: Perception for Design* is a survey of the vision-science literature reorganized for people who have to draw something. Its 4th edition runs twelve chapters, from optics and lightness through color, salience, pattern, space, objects, interaction and visual thinking, and closes with a Guidelines appendix. When someone writes "Ware showed that," check whether the underlying study is his. His own experimental record is listed below; anything outside it is a citation of his reading of the vision-science literature, which is a different warrant and usually a much older result.

### Color sequences, 1988

The paper the 2023 rainbow essay points at as its real evidence. It splits map reading into two tasks that want opposite things: **metric** information (read a quantity off a key) and **form** information (see the shape of the surface). Its theory predicts a spectrum scale wins the first and loses the second, and a gray scale the reverse, because form perception runs through the luminance channel. Ten color-normal subjects, five color sequences, and the author's own verdict on his hypothesis is mixed: the results "only partially confirm the form hypothesis."

The three rules of thumb it ends on are worth quoting because the third one is the modern colormap, written in 1988:

> "To create a color sequence that has good properties for revealing both shape and metric quantities, use a sequence that increases monotonically in luminance, while cycling through a range of hues. The hues provide accurate readings from a key, while the luminance conveys the form of the surface."

That is viridis and turbo, thirty years early, and it is the actual content behind "Ware defends rainbows."

### Colormap resolving power, 2019

560 Mechanical Turk participants, nine colormaps, three feature sizes, 270 averaged feature-detection thresholds. The paper tested two models and rejected both. Unmodified CIELAB overweights the chromatic channels. A luminance-only model does better and still fails:

> "We also tested against the hypothesis that L\* by itself could account for the data equally well and found that it could not, although this did better than unmodified CIELAB."

The constructive result is a CIELAB variant with the green-red and yellow-blue terms weighted down to about 0.1, fitting the combined data at r² = 0.94. Their own statement of the implication:

> "colormap uniformity is not a simple concept, since the relative weights of chromatic variation and luminance variation change as a function of the spatial frequency of features"

**This sharpens a line the wiki currently carries secondhand.** [ware-2023-rainbow-colormaps.md](../studies/ware-2023-rainbow-colormaps.md) lists the 2019 paper as showing that "feature detection depends mostly on luminance," which is the essay's own compression of it. *Mostly* is right, *solely* was tested and rejected, and how much the chromatic channels contribute depends on how large the features are. If you are picking a colormap for fine structure, that is the whole decision.

### Graph aesthetics, 2002

The most directly relevant Ware result to anything network-shaped, and it is not in this wiki. 43 subjects timed on finding the shortest path between two marked nodes in 137 spring-layout drawings, with path lengths of 3 to 5. Stepwise regression over eight measured layout properties, R² = 0.784.

The finding is a **price list**:

> "the cognitive cost of a single crossing is approximately the same as 38 degrees of continuity. The practical consequence is that it may be worth allowing for an occasional crossing in a graph layout if it reduces the bendiness of paths."

Concretely: 100 degrees of path bendiness costs 1.7 seconds, each crossing on the path costs 0.65 seconds. And it partly overturns the aesthetic the graph-drawing field had been optimizing:

> "we find that her measurement of the total number of edge crossings in the graph drawing is not a significant indicator of response time. For shortest path tasks, we have shown here that it is the number of edges that cross the shortest path itself that is important, rather than the total number of edges crossings in the drawing."

**Limits the authors state.** "More studies are required to determine the robustness of our findings for other than spring layout graphs and for different graph sizes." The subjects were second- and third-year computing students at one university. The task is shortest-path only, at lengths 3 to 5. Their own most-difficult-to-explain result is a negative regression intercept, which they discuss rather than bury.

### Motion as a highlighting channel, 2004

With Robert Bobrow. Touching a node makes it and its topological neighborhood oscillate. Three experiments, all with **the same 13 subjects**, all favoring motion over static highlighting on both speed and errors. The abstract's own framing is "we argue from perceptual principles," and the sample is small enough that it should be read as a demonstration with supporting measurements rather than a settled effect size.

### Where his name is used as authority for more than he showed

1. **The rainbow, in both directions.** "Ware says rainbows are fine" and "Ware says rainbows are harmful" are both citations of opinion pieces. The 2023 Viewpoints article contains no experiment, which [its own page](../studies/ware-2023-rainbow-colormaps.md) documents at length. What he actually measured is above: 1988 for the metric-versus-form split, 2019 for resolving power. Neither says "rainbows are fine." Both say luminance is doing more of the work than people think.
2. **Preattentive processing.** Emphasis rules of the form "the viewer finds the accented item in a fixed short time regardless of how many other items are on screen" get pointed at Ware's book, because his chapter 5 is where a designer meets that literature. The experiments are not his, the timing figures come from the visual-search tradition he is summarizing, and set-size independence holds for a narrow class of feature searches rather than for whatever you happened to make orange. This is a warrant problem rather than a factual one, and it is the same shape as the Cleveland and Munzner cases. See [refutations.md](../refutations.md), "Gray plus one accent," for what happened when this wiki went looking for a controlled test of the rule people actually apply.
3. **Edge crossings.** People cite the graph-drawing tradition, and increasingly Ware 2002, for "minimize crossings." Ware 2002 found the opposite emphasis: *total* crossings in the drawing were not significant, crossings *on the path being traced* were, and continuity outranked both once path length was factored out.

### The visual-query framing, which is his and which people skip

Ware's later work recasts a display's job as supporting a **visual query**: a specific pattern the viewer must find, in service of a specific cognitive step. From his 2012 keynote slides (his words, on slides, not the book's sentences), what this buys you is "How big a problem can be addressed / Visual search requirements / Visual working memory load issues." A design frame with a budget in it, which almost nothing else in the canon has.

---

## What they would object to in your figure

*Reconstruction from his stated priorities. He has not seen your figure.*

He would ask what visual query the figure exists to support, and then whether the pattern that answers it is available to the visual system at the size you drew it. Not whether it is present in the data, and not whether a careful reader could work it out. He is a spatial-frequency person: a distinction carried entirely in hue, at small feature sizes, on an uncalibrated screen, is one he would predict people cannot resolve, and he has measured that. He would care much less than Few or Cleveland whether the chart type is respectable and much more whether the encoding survives the eye. He would push back on a blanket rainbow ban and then object to your specific rainbow on luminance grounds. On a network diagram he would ask which paths the reader has to trace, and then trade you a crossing for a straighter path without hesitating. And he would want to know how many things you are asking the reader to hold in visual working memory while comparing panels, because his answer to that is a small number.

---

## Works, and where they sit in this wiki

| Work | Status | Where it sits |
|---|---|---|
| *Information Visualization: Perception for Design*, 4th ed. (Morgan Kaufmann, 19 Dec 2019, ISBN 9780128128756) | `secondary-only`. Chapter list from [shop.elsevier.com](https://shop.elsevier.com/books/information-visualization/ware/978-0-12-812875-6), the publisher's own. The book was not opened. | **No page. No row in [roll-call.md](../roll-call.md). Absent from [inventory.md](../inventory.md).** |
| Ware (1988), "Color Sequences for Univariate Maps: Theory, Experiments, and Principles," *IEEE CG&A* 8(5), 41-49 | `primary-read`. Author-hosted preprint at [vislab-ccom.unh.edu/pdfs/ColorSequences.pdf](https://vislab-ccom.unh.edu/pdfs/ColorSequences.pdf), extracted locally. | No page. Named as the real evidence in [ware-2023-rainbow-colormaps.md](../studies/ware-2023-rainbow-colormaps.md). Bears on [inventory.md](../inventory.md) topics 23, 24, 25. |
| Ware, Purchase, Colpoys & McGill (2002), "Cognitive Measurements of Graph Aesthetics," *Information Visualization* 1(2), 103-110 | `primary-read`. [vislab-ccom.unh.edu/pdfs/GraphAesthetics.pdf](https://vislab-ccom.unh.edu/pdfs/GraphAesthetics.pdf), extracted locally. | **No page, and it belongs in the network tier.** See [chart-types/node-link.md](../chart-types/node-link.md), [chart-types/network-topology.md](../chart-types/network-topology.md). |
| Ware & Bobrow (2004), "Motion to Support Rapid Interactive Queries on Node-Link Diagrams," *ACM TAP* 1(1) | `primary-read`. [vislab-ccom.unh.edu/pdfs/MotionQueries.pdf](https://vislab-ccom.unh.edu/pdfs/MotionQueries.pdf), extracted locally. | No page. Relevant to interaction and to the node-link side of [ghoniem-2004.md](../studies/ghoniem-2004.md) / [okoe-2018.md](../studies/okoe-2018.md). |
| Ware, Turton, Bujack, Samsel, Shrivastava & Rogers (2019), "Measuring and Modeling the Feature Detection Threshold Functions of Colormaps," *IEEE TVCG* 25(9), 2777-2790 | `primary-read`. IEEE PDF, extracted locally. | No page. Referenced secondhand in [ware-2023-rainbow-colormaps.md](../studies/ware-2023-rainbow-colormaps.md). |
| Ware, Stone & Szafir (2023), *Rainbow Colormaps Are Not All Bad* | `primary-read` | [studies/ware-2023-rainbow-colormaps.md](../studies/ware-2023-rainbow-colormaps.md) |
| Ware & Franck (1996), "Evaluating Stereo and Motion Cues for Visualizing Information Nets in Three Dimensions," *ACM TOG* 15(2) | Reachable, not read. [vislab-ccom.unh.edu/pdfs/TOGGraph_Net.pdf](https://vislab-ccom.unh.edu/pdfs/TOGGraph_Net.pdf) | No page. The nearest empirical treatment in this source set of when 3D helps a network view, against which Munzner's "No Unjustified 3D" is an unsourced rule of thumb. |
| Ware & Beatty (1988), "Using Color Dimensions to Display Data Dimensions," *Human Factors* 30(2) | `not-reached`. Closed access; no repository copy on Unpaywall or OpenAlex, publisher returns 403, absent from the UNH lab archive. | No page. |
| *Visual Thinking for Design* (2008) / *Visual Thinking for Information Design*, 2nd ed. (2021) | `secondary-only`. The visual-query material above is from his 2012 VISIGRAPP keynote deck, extracted locally. | No page. |

**Retrieval note worth stealing.** `ccom.unh.edu/vislab/PDFs/<anything>.pdf` returns **HTTP 200 with 4.7 KB of HTML**, a soft 404 that passes a naive status-code check. The live host is `vislab-ccom.unh.edu/pdfs/` with a lowercase directory name and an open index listing 66 papers.

The 4th edition's chapters, verbatim from the publisher: 1. Foundations for an Applied Science of Data Visualization. 2. The Environment, Optics, Resolution, and the Display. 3. Lightness, Brightness, Contrast, and Constancy. 4. Color. 5. Visual Salience and Finding Information. 6. Static and Moving Patterns. 7. Space Perception. 8. Visual Objects and Data Objects. 9. Images, Narrative, and Gestures for Explanation. 10. Interacting with Visualizations. 11. Visual Thinking Processes. 12. Designing for Perception. Then a list of the book's named **Visual Thinking Algorithms** (Visual Queries, Pathfinding on a Map or Diagram, Reasoning with a Hybrid of a Visual Display and Mental Imagery, Design Sketching, Brushing, Small Pattern Comparisons in a Large Information Space, Degree-of-Relevance Highlighting, Generalized Fisheye Views, Multidimensional Dynamic Queries with Scatter Plot, Visual Monitoring Strategies), then appendices A (Changing Primaries), B (CIE Color Measurement System) and C (**Guidelines**). The publisher's page flags chapter 12 as new and does not say which chapters the algorithms sit in.

## What the repo lost by missing the book

Stated plainly, because it is why this page exists.

**It is the second uncounted source, and it has one fewer excuse than the first.** The README names Tufte as "the structural gap," on the grounds that he has no row in the roll-call, so the roll-call's coverage guarantee cannot see him. Ware is in exactly that position, and Tufte at least enters the inventory by quotation through Wilke. Ware does not enter it at all. Grep the wiki for his name and you get one study page, for an essay containing no experiment.

**Chapter 5 is the missing warrant under a rule the wiki already flagged as unwarranted.** [refutations.md](../refutations.md) records "gray plus one accent" as having no controlled study, noting that the preattentive and visual-search literature supports pop-out generally without testing this rule. That negative result is correct and it is thin, because the search never went through the source that organizes that literature for design use. Preattentive attention currently enters [inventory.md](../inventory.md) through topics 29, 37 and 41, sourced to Knaflic, Datawrapper, Urban and Wilke. Four practitioner sources and no perception source, for a claim about perception.

**Chapters 3 and 4 are the mechanism under color rules the wiki takes on assertion.** Topic 24 (perceptual uniformity) is evidence-backed on matplotlib's docs. Topic 33 (text contrast) is evidence-backed on WCAG. Topic 27 (grayscale survival) is authority-asserted on Munzner's rule-of-thumb name, which her own slides attribute to Maureen Stone. Every one is a lightness-and-contrast claim, and the canon's lightness-and-contrast reference was consulted for none of them.

**The Guidelines appendix is a free audit nobody ran.** [inventory.md](../inventory.md) was derived blind from the canon on purpose, so a later diff would mean something. The book ships its own consolidated guideline list, derived by a perception researcher from the perception literature. Diffing 92 topics against that appendix is the highest-value unexecuted task in this wiki: whatever Ware has that the inventory lacks is a hole, and whatever the inventory has that Ware lacks is a rule with no perceptual basis. Both directions are worth knowing.

**And the network tier is missing a leg it could already be standing on.** [chart-types/network-topology.md](../chart-types/network-topology.md) rests on Ghoniem 2004 and Okoe 2018, both node-link-versus-matrix comparisons. Neither says anything about what makes an individual node-link drawing readable. Ware 2002 does, it is open access, and it produces an exchange rate between two layout properties that graph-drawing algorithms optimize. The wiki's rule that no controlled study has ever tested a chart type has a partial exception sitting on a university web server, and it went unread until this page.

## See also

- [studies/ware-2023-rainbow-colormaps.md](../studies/ware-2023-rainbow-colormaps.md), the one Ware page that exists, and why it is not evidence
- [concepts/channels.md](../concepts/channels.md), the wiki's claim that channels are the only level the literature speaks at, which Ware's book is the standing counterexample to
- [sources/munzner-vad.md](../sources/munzner-vad.md), the other framework book, `secondary-only` for the same reason and handled by the same publisher-TOC method
- [william-cleveland.md](william-cleveland.md), the other half of the perception lineage, approached from statistics rather than vision science
