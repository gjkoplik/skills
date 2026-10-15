---
type: person
status: primary-read
status_partial: true
retrieved: 2026-09-05
---

# Jeffrey Heer

**What they are known for.** Replicating the field's foundational result, then building much of the tooling charts are drawn with. Protovis, D3, Vega and Vega-Lite came out of labs he ran or co-ran. Both come from one habit: turn a design question into something a paid crowd can answer, or into a grammar whose defaults have to be written down.

**How this was read.** Four papers from `idl.cs.washington.edu`, extracted locally with `pdftotext`, plus this wiki's existing primary reading of Heer & Bostock (2010). Affiliations are as printed (Stanford, then University of Washington), with no claim about his current one. `status_partial`: the publication list is long, the four papers were chosen for what they bear on, and Vega-Lite and D3 are read only through their papers and shipped documentation.

**What they are good for.** *Has anyone re-run this?* He is the corpus's most reliable source of replications and of the crowdsourcing method that made them affordable. *What does a chart library decide when the spec is silent?* A declarative grammar must write its defaults down, and he co-authored several, so house style becomes checkable.

**What they do not settle.** Almost none of his perception work leaves proportional judgment: read a value off a mark, report a number. The systems work describes a design position rather than evidencing it, and a default shipped in a popular library is still `authority-asserted`. Nothing on narrative or accessibility, and no recorded position on chart-type taste.

---

## What their work established

### The replication, and the method that made it cheap

[Heer & Bostock (2010)](../studies/heer-bostock-2010.md) re-ran Cleveland & McGill's position-length experiment on Mechanical Turk at $0.05 a judgment and added experiments the original could not afford. It is why the Cleveland-McGill ordering can be called replicated.

- Position beats length, angle and area, and angle beats area, on a different population, hardware and decade.
- Rectangular area comparison is worst when both rectangles are **squares**, the opposite of what squarified treemap layouts optimize for.
- **Length did not beat angle**, though theory predicted it. That keeps rank 3 a tie on [concepts/channels.md](../concepts/channels.md).

Nearly every post-2010 study in this wiki runs on the platform this paper and [Kosara & Ziemkiewicz's contemporaneous BELIV paper](robert-kosara.md) validated: his reproduced a lab result with a crowd, theirs catalogued how such studies go wrong.

### Treemaps: Kong, Heer & Agrawala (2010)

> "We find no evidence that luminance affects area judgments, but observe that aspect ratio does have an effect. Specifically, we find that the accuracy of area comparisons suffers when the compared rectangles have extreme aspect ratios or when both are squares. Contrary to common assumptions, the optimal distribution of rectangle aspect ratios within a treemap should include non-squares, but should avoid extreme aspect ratios."

The crossover against the length-encoded alternative, which [chart-types/treemap.md](../chart-types/treemap.md) does not yet carry:

> "The transition point we found was at 4096 leaves, where treemaps were almost 3 seconds faster. At 8000 leaves, treemaps were almost 5 seconds faster. If a data set has thousands of elements, treemaps are more effective."

### Horizon graphs: Heer, Kong & Agrawala (2009)

*Sizing the Horizon* compared line charts with mirrored and layered variants across heights, scoring value-comparison error against a within-5-values target.

- **Mirroring is free.** Flipping negatives above the axis in a different color "neither slowed estimation time nor hurt estimation accuracy," at half the height.
- **Layering costs until the chart gets small.** Bands increased time and error at constant height, but two-band mirrored charts were more accurate below 24 pixels. Four or more bands were worse on both measures, and subjects called them tiring.
- **The optimal size is small.** For line charts and one-band mirror charts, 24 pixels minimized estimation time without costing accuracy.

Only value comparison was measured, and the authors note that "graphical perception of time series typically involves observing rates of change in addition to comparing values."

### Task and data: Kim & Heer (2018)

Twelve encodings of trivariate data (one categorical, two quantitative), four task types, and 24 data distributions varying cardinality, records per category and entropy. It is the closest empirical test in the corpus of the argument [Bertini, Correll & Franconeri](michael-correll.md) make on paper, that a ranking from two-value ratio judgment may not transfer to other tasks. The average holds:

> "Though APT's rankings were largely derived in the context of individual value comparison tasks [Mac86,CM84], they align well with our empirical rankings averaged across task types."

Individual conditions do not:

> "colored scatterplots (with positionally-coded quantities and color-coded categories) perform well for comparing individual points, but perform poorly for summary tasks as the number of categories increases."

The authors blame most of the movement on overplotting and visual congestion, not the channels. Effects they cannot explain, such as asymmetries when x and y are swapped, are listed under "Unexplained Observations."

### Vega-Lite and its defaults

Vega-Lite (Satyanarayan, Moritz, Wongsuphasawat & Heer, 2017) assumes specs will be underspecified:

> "Concise specification is achieved in part through ambiguity: users may omit details such as scale transforms (e.g., linear or log) or color palettes, which are then filled in using a rule-based system of smart defaults."

A library that fills in defaults has to publish them, and a published default states a design position more exactly than a style guide. Hence [sources/vega-lite.md](../sources/vega-lite.md), which turns on `zero: true`.

The paper's Figure 1, five examples chosen to show the grammar off, includes a "dual-axis layered bar and line chart." Received wisdom bans that form ([refutations.md](../refutations.md), dual-axis entry).

---

## What they would object to in a figure

*Reconstruction from his stated priorities, not a response to any figure.*

The task, since his 2018 paper found it changes the encoding ranking. The size, since he measured the optimal time-series height as smaller than most people draw. Whether the design was tested or inherited, with "we could crowdsource that" as a live answer. On a squarified treemap, that it optimizes toward the aspect ratio his experiments found worst. Whether the defaults are written down, more than which ones they are.

---

## Works, and where they sit in this wiki

| Work | Status | Where it sits |
|---|---|---|
| Heer & Bostock (2010), "Crowdsourcing Graphical Perception," CHI | `primary-read` | [studies/heer-bostock-2010.md](../studies/heer-bostock-2010.md), [concepts/channels.md](../concepts/channels.md) |
| Kong, Heer & Agrawala (2010), "Perceptual Guidelines for Creating Rectangular Treemaps," *TVCG* | `primary-read`, [PDF](https://idl.cs.washington.edu/files/2010-Treemaps-InfoVis.pdf) | No page. Has the crossover [chart-types/treemap.md](../chart-types/treemap.md) lacks. |
| Heer, Kong & Agrawala (2009), "Sizing the Horizon," CHI | `primary-read`, [PDF](https://idl.cs.washington.edu/files/2009-TimeSeries-CHI.pdf) | No page. The evidence for the horizon graph, a missing type in [../README.md](../README.md). |
| Kim & Heer (2018), "Assessing Effects of Task and Data Distribution on the Effectiveness of Visual Encodings," EuroVis | `primary-read`, [PDF](https://idl.cs.washington.edu/files/2018-TaskDataEffectiveness-EuroVis.pdf) | No page. The empirical counterpart to the scope critique [concepts/channels.md](../concepts/channels.md) states from a position paper. |
| Satyanarayan, Moritz, Wongsuphasawat & Heer (2017), "Vega-Lite: A Grammar of Interactive Graphics," *TVCG* | `primary-read`, [PDF](https://idl.cs.washington.edu/files/2017-VegaLite-InfoVis.pdf) | Behind [sources/vega-lite.md](../sources/vega-lite.md), which covers the documentation, not the paper. |
| Bostock, Ogievetsky & Heer (2011), "D3: Data-Driven Documents," and Bostock & Heer (2009), "Protovis" | `not-reached` | No page. Listed for the lineage, below. |
| Kay & Heer (2016), "Beyond Weber's Law," and the rest | Unread. [idl.uw.edu/papers](https://idl.uw.edu/papers/) | Re-analyzes correlation-perception rankings, bearing on [chart-types/scatterplot.md](../chart-types/scatterplot.md). |

## Independence of the sources he touches

[sources/vega-lite.md](../sources/vega-lite.md) documents a grammar he co-authored, and [sources/observable-plot.md](../sources/observable-plot.md) a library by Mike Bostock, his co-author on the 2010 replication and on D3. Separate organizations make this weaker than the [jonathan-schwabish.md](jonathan-schwabish.md) case, where one person is behind both artifacts, but both are grammar-of-graphics descendants from overlapping people. [inventory.md](../inventory.md) topic 9 counts Vega-Lite and Observable Plot among the sources on the zero baseline, unaudited against this overlap.

## See also

- [studies/heer-bostock-2010.md](../studies/heer-bostock-2010.md): the replication the channel evidence rests on
- [concepts/channels.md](../concepts/channels.md): the length-against-angle tie
- [william-cleveland.md](william-cleveland.md): the work being replicated
- [robert-kosara.md](robert-kosara.md): the other re-tester, same method, same year
- [michael-correll.md](michael-correll.md): the scope critique Kim & Heer tested
