---
type: person
status: primary-read
status_partial: true
retrieved: 2026-09-05
---

# Jeffrey Heer

**What they are known for.** Heer is the person who put the field's foundational result back on a bench and got the same answer, and then built most of the tooling everyone else's charts are drawn with. [Heer & Bostock (2010)](../studies/heer-bostock-2010.md) is the reason the Cleveland-McGill ordering can be called replicated at all. Protovis, D3, Vega and Vega-Lite came out of labs he ran or co-ran. Both halves of that come from the same habit: turn a design question into something a crowd of strangers can be paid to answer, or into a grammar whose defaults have to be written down.

**How this was read.** Four of his papers were downloaded from `idl.cs.washington.edu` and extracted locally with `pdftotext`, plus this wiki's existing primary reading of Heer & Bostock (2010). Retrieval date **2026-09-05**. Affiliations below are as printed on each paper (Stanford, then University of Washington); no claim is made about where he works now. `status_partial` because the publication list is long, the four papers read here were chosen for what they bear on, and the Vega-Lite and D3 systems are read through their papers and shipped documentation rather than through their full literature.

**What they are good for.** Two questions. *Has anyone actually re-run this?* He is the corpus's most reliable source of replications and of the crowdsourcing method that made them affordable. And *what does a chart library decide when the spec is silent?* A declarative grammar has to write its defaults down, and he has co-authored several, which turns house style into something checkable.

**What they do not settle.** Almost none of his perception work leaves proportional judgment: read a value off a mark, report a number. The systems work is descriptive of a design position rather than evidence for it, and a default that ships in a popular library is still `authority-asserted`, however many charts it draws. Nothing on narrative, nothing on accessibility, and no position on chart-type taste that this corpus records.

---

## What their work actually established

### The replication, and the method that made it cheap

**Heer & Bostock (2010), the replication.** Cleveland & McGill's position-length experiment re-run on Mechanical Turk at $0.05 a judgment, plus new experiments the original could not afford. Full treatment at [studies/heer-bostock-2010.md](../studies/heer-bostock-2010.md). Two things it settled and one it did not:

- Position beats length, angle and area; angle beats area. Measured on a different population, on different hardware, in a different decade.
- Rectangular area comparison is worst when both rectangles are **squares**, which is the opposite of what squarified treemap layouts optimize for.
- **Length did not beat angle**, which theory predicted. That failure is what keeps rank 3 a tie on [concepts/channels.md](../concepts/channels.md).

The method matters as much as the result. Nearly every post-2010 study in this wiki runs on the platform this paper and [Kosara & Ziemkiewicz's contemporaneous BELIV paper](robert-kosara.md) validated between them: his showed a crowdsourced perception study could reproduce a lab result, theirs catalogued how such a study goes wrong.

### The treemap follow-up, which this wiki does not yet carry

**Kong, Heer & Agrawala (2010), *Perceptual Guidelines for Creating Rectangular Treemaps*.** The extension of the 2010 rectangle result into the form it was motivated by. Three findings, all measured:

> "We find no evidence that luminance affects area judgments, but observe that aspect ratio does have an effect. Specifically, we find that the accuracy of area comparisons suffers when the compared rectangles have extreme aspect ratios or when both are squares. Contrary to common assumptions, the optimal distribution of rectangle aspect ratios within a treemap should include non-squares, but should avoid extreme aspect ratios."

and a transition point against the length-encoded alternative:

> "The transition point we found was at 4096 leaves, where treemaps were almost 3 seconds faster. At 8000 leaves, treemaps were almost 5 seconds faster. If a data set has thousands of elements, treemaps are more effective."

[chart-types/treemap.md](../chart-types/treemap.md) currently carries the square-worst result from Heer & Bostock and nothing about where the treemap-against-bar-chart crossover sits. This paper measures that crossover, and it is the number a chooser standing in front of a hierarchy actually wants.

### The horizon graph, which is a form this wiki has no page for

**Heer, Kong & Agrawala (2009), *Sizing the Horizon*.** Line charts against mirrored and layered variants across a range of chart heights, value-comparison task, error measured against a within-5-values target. Three results:

- **Mirroring is free.** Flipping negative values above the axis and coloring them differently "neither slowed estimation time nor hurt estimation accuracy," while halving the height.
- **Layering costs, until the chart gets small.** Bands reliably increased both time and error at constant height, but two-band mirrored charts were more accurate below 24 pixels. Four or more bands were worse on both measures and subjects called them tiring.
- **There is an optimal size, and it is smaller than the default.** For line charts and one-band mirror charts, a height of 24 pixels minimized estimation time without costing accuracy, so shrinking the chart was free even without a space constraint.

The authors state the limit themselves: only value comparison was measured, and "graphical perception of time series typically involves observing rates of change in addition to comparing values."

### The scope critique, tested rather than argued

**Kim & Heer (2018), *Assessing Effects of Task and Data Distribution on the Effectiveness of Visual Encodings*.** Twelve encodings of trivariate data (one categorical, two quantitative), four task types, 24 data distributions varying cardinality, records per category and entropy. It is the closest thing in this corpus to an empirical test of the argument [Bertini, Correll & Franconeri](michael-correll.md) make on paper, that a ranking derived from two-value ratio judgment should not be assumed to transfer to other tasks.

It comes out both ways, and the paper says so:

> "Though APT's rankings were largely derived in the context of individual value comparison tasks [Mac86,CM84], they align well with our empirical rankings averaged across task types."

The average holds. The individual conditions do not: "colored scatterplots (with positionally-coded quantities and color-coded categories) perform well for comparing individual points, but perform poorly for summary tasks as the number of categories increases." Most of the movement they attribute to overplotting and visual congestion rather than to the channels themselves. They also report a set of effects they cannot explain, including asymmetries between encodings that differ only in swapping x and y, and say so under a heading called "Unexplained Observations."

### The grammars, and what they commit to

**Vega-Lite (Satyanarayan, Moritz, Wongsuphasawat & Heer, 2017)** is a high-level grammar whose whole design premise is that the spec will be underspecified and the system will fill in the rest: "Concise specification is achieved in part through ambiguity: users may omit details such as scale transforms (e.g., linear or log) or color palettes, which are then filled in using a rule-based system of smart defaults."

That is why [sources/vega-lite.md](../sources/vega-lite.md) is in this corpus at all. A library that fills in defaults has to publish them, and the published default is a design position stated more precisely than any style guide states it, `zero: true` being the case that page turns on.

One detail worth recording against [refutations.md](../refutations.md)'s dual-axis entry: the paper's own Figure 1, five examples chosen to show the grammar off, includes a "dual-axis layered bar and line chart." The form the received wisdom bans appears in the showcase figure of a grammar paper.

---

## What they would object to in a figure

*Reconstruction from his stated priorities, not a response to any actual figure.*

He would ask what the reader is being asked to do with it, because his 2018 paper measured that the answer changes the encoding ranking. He would ask how big it is, having measured that the optimal height for a time series is smaller than most people draw. He would want to know whether the design choice was tested or inherited, and would treat "we could crowdsource that" as a live answer rather than a deferral. Shown a squarified treemap he would say the layout algorithm optimizes toward the aspect ratio his own experiments found worst. And he would be more interested in whether the figure's defaults are written down anywhere than in whether they are the ones he would pick.

---

## Works, and where they sit in this wiki

| Work | Status | Where it sits |
|---|---|---|
| Heer & Bostock (2010), "Crowdsourcing Graphical Perception," CHI | `primary-read` | [studies/heer-bostock-2010.md](../studies/heer-bostock-2010.md), [concepts/channels.md](../concepts/channels.md) |
| Kong, Heer & Agrawala (2010), "Perceptual Guidelines for Creating Rectangular Treemaps," *TVCG* | `primary-read`. [idl.cs.washington.edu](https://idl.cs.washington.edu/files/2010-Treemaps-InfoVis.pdf), extracted locally with `pdftotext`. | **No page**, and it carries the treemap-against-bar-chart transition point [chart-types/treemap.md](../chart-types/treemap.md) does not have. |
| Heer, Kong & Agrawala (2009), "Sizing the Horizon," CHI | `primary-read`. [idl.cs.washington.edu](https://idl.cs.washington.edu/files/2009-TimeSeries-CHI.pdf), extracted locally with `pdftotext`. | **No page**, and the horizon graph is named as a missing type in [../README.md](../README.md). This is the study that would let that page carry evidence rather than a decomposition. |
| Kim & Heer (2018), "Assessing Effects of Task and Data Distribution on the Effectiveness of Visual Encodings," EuroVis | `primary-read`. [idl.cs.washington.edu](https://idl.cs.washington.edu/files/2018-TaskDataEffectiveness-EuroVis.pdf), extracted locally with `pdftotext`. | **No page**, and it is the empirical counterpart to the scope critique [concepts/channels.md](../concepts/channels.md) currently states from a position paper only. |
| Satyanarayan, Moritz, Wongsuphasawat & Heer (2017), "Vega-Lite: A Grammar of Interactive Graphics," *TVCG* | `primary-read`. [idl.cs.washington.edu](https://idl.cs.washington.edu/files/2017-VegaLite-InfoVis.pdf), extracted locally with `pdftotext`. | The system behind [sources/vega-lite.md](../sources/vega-lite.md), which covers the shipped scale documentation rather than the paper. |
| Bostock, Ogievetsky & Heer (2011), "D3: Data-Driven Documents," and Bostock & Heer (2009), "Protovis" | `not-reached`. | No page. Named here because the lineage matters for counting voices, below. |
| Kay & Heer (2016), "Beyond Weber's Law," and the rest of the publication list | Unread. Index at [idl.uw.edu/papers](https://idl.uw.edu/papers/). | Kay & Heer is a re-analysis of correlation-perception rankings and would bear on [chart-types/scatterplot.md](../chart-types/scatterplot.md). |

## The independence problem this page creates

**Two source pages in this wiki descend from work he co-authored**, and the corpus has already been caught counting one person as two voices ([jonathan-schwabish.md](jonathan-schwabish.md)). [sources/vega-lite.md](../sources/vega-lite.md) documents a grammar he co-authored. [sources/observable-plot.md](../sources/observable-plot.md) documents a library built by Mike Bostock, his co-author on the 2010 replication and on D3.

They are separate organizations and separate products, so this is weaker than the Schwabish case, which is one person behind both artifacts. It is not nothing either: both are grammar-of-graphics descendants from an overlapping set of people. [inventory.md](../inventory.md) topic 35 counts Vega-Lite and Observable Plot among converging sources for the by-mark reading of the zero baseline, and that count has not been audited against this. **Recorded, not resolved.**

## See also

- [studies/heer-bostock-2010.md](../studies/heer-bostock-2010.md), the replication this wiki's channel evidence rests on
- [concepts/channels.md](../concepts/channels.md), and the length-against-angle joint his experiment failed to close
- [william-cleveland.md](william-cleveland.md), the work being replicated
- [robert-kosara.md](robert-kosara.md), the other re-tester, arriving at the same crowdsourcing method in the same year
- [michael-correll.md](michael-correll.md), the scope critique Kim & Heer put on a bench
