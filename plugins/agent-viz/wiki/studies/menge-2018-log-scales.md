---
type: study
status: secondary-only
status_partial: true
retrieved: 2026-08-23
---

# Menge et al. 2018: Logarithmic scales in ecological data presentation may cause misinterpretation

Duncan N. L. Menge, Anna C. MacPherson, Thomas A. Bytnerowicz, Andrew W. Quebbeman, Naomi B. Schwartz, Benton N. Taylor, Amelia A. Wolf. *Nature Ecology & Evolution* 2 (2018), 1393-1402. DOI [10.1038/s41559-018-0610-7](https://doi.org/10.1038/s41559-018-0610-7).

A literature audit of how often ecology papers use log axes, plus a randomized survey of Ecological Society of America members reading graphs shown on either linear-linear or log-log axes. The comprehension gap is large.

**What it is good for.** Refuting the claim that log scales are fine for expert audiences. The respondents are professional ecologists, 69% of them with PhDs, and log-log comprehension still collapses.

**What it does not settle.** Visualization design as such. This is a comprehension survey with hand-built stimuli about rabbit and chipmunk populations, and it compares log axes only against linear ones.

**How this was read.** Read directly: the publisher's abstract on nature.com, which carries every headline number below verbatim, and all four supplementary PDFs, free from the article page and labeled "In the format provided by the authors and unedited." They hold Supplementary Tables 1 through 6, the figure legends, and the full survey instrument and flow. Not read: the main text. It is not open access or in PMC, no preprint or author PDF exists, the SharedIt link is a JavaScript viewer, and bot-check walls blocked the other mirrors. The numbers match the publisher record, but the Methods, Results and Discussion are unread, so the status is `secondary-only`.

## The finding

From the abstract:

> "Analysing the extent of log scales in the literature, we show that 22% of papers published in the journal *Ecology* in 2015 included at least one log-scaled axis, of which 21% were log-log displays. We conducted a survey that asked members of the Ecological Society of America (988 responses, and 623 completed surveys) to interpret graphs that were randomly displayed with linear-linear or log-log axes. Many more respondents interpreted graphs correctly when the graphs had linear-linear axes than when they had log-log axes: 93% versus 56% for our all-around metric, although some of the individual item comparisons were even more skewed (for example, 86% versus 9% and 88% versus 12%). These results suggest that misconceptions about log-scaled data are rampant."

The recommendation, also from the abstract:

> "We recommend that ecology curricula include explicit instruction on how to interpret log-scaled axes and equations, and we also recommend that authors take the potential for misconceptions into account when deciding how to visualize data."

The advice to authors is "take the potential for misconceptions into account," not "do not use log scales."

## Method, from the supplements

Three display conditions, not two: linear, log with untransformed axis values, and log with log-transformed axis values. Each appeared as a graph and as an equation-plus-table analog. Four attributes were probed per dataset: increase or decrease with distance, which increases relatively more, positive versus zero versus negative, and accelerating versus decelerating. Three hypothetical datasets, with equations and parameters in Supplementary Table 2.

The survey flow (Supplementary PDF 4) randomizes which items each respondent sees, their variants, the order of answer options and the order of the four selected items. Per-item sample sizes in Supplementary Table 1 run from about 137 to 468, well below 623.

"Wouldn't notice" was tabulated separately. It was near zero for graphs (typically 0 to 1%) and up to 42% for equations. Respondents knew when an equation was beyond them and did not know it for a log graph.

## Sample size and population

- **988 responses, 623 completed surveys**, from members of the Ecological Society of America.
- Demographics (Supplementary Table 4): 55% male, 45% female; ages 20 to 84, mean 43; 89% white; **69% hold a PhD**, 20% a master's, 11% a bachelor's; 35% professors, 18% PhD students, 11% government research scientists, 8% academic research scientists, 10% postdocs.
- Comfort with logarithms (Supplementary Table 5): 73% comfortable to some degree (8% extremely, 39% moderately, 26% slightly), 9% neutral, 18% uncomfortable. **89% had log-transformed data for analysis themselves.**
- Stated preference: 21% linear, 0.5% log, 67% "usually linear," 3% "usually log," 9% no opinion.

## Correctness by demographic

Supplementary Table 3, percent correct on graphs:

| Split | Linear | Log, untransformed | Log, transformed |
|---|---|---|---|
| Male / Female | 94 / 92 | 55 / 56 | 54 / 53 |
| PhD / no PhD | 94 / 91 | 56 / 56 | 55 / 51 |
| Professor / other | 94 / 93 | 55 / 56 | 55 / 53 |
| Over 43 / under 43 | 93 / 94 | 54 / 56 | 54 / 53 |

The gap does not close for any group. A PhD adds 3 points on linear graphs and 0 on log-untransformed graphs. This is in a supplementary table, not the abstract.

Supplementary Figure 7 regresses correctness on self-reported comfort with logarithms. For graphs the coefficients are 0.58 ± 0.53 (linear), 0.93 ± 0.61 (log untransformed) and -0.06 ± 0.66 (log transformed), with t values 1.1, 1.5 and -0.08. Self-reported comfort does not predict getting log graphs right.

## Limits

No author-stated limitation is quoted, because the main text was not read. Observed from the abstract, supplements and instrument:

- The "all-around metric" behind 93% versus 56% is not defined in the material reached.
- Per-item n is roughly 140 to 470.
- The stimuli are hypothetical rabbit and chipmunk populations from parameterized equations, not real ecological data or a real reading task.
- The sample is self-selected ESA members who opened a survey, and 365 of 988 respondents did not finish.
- The abstract hedges twice: log scales "**may** cause misinterpretation," and the results "**suggest** that misconceptions about log-scaled data are rampant."

## What this result does not license

- **Not "never use log scales."** The authors recommend instruction plus author awareness. They do not tell ecologists to stop.
- **Not a claim about all audiences.** The result plausibly generalizes downward (if PhD ecologists who routinely log-transform data get 56%, a lay audience will not do better), but the numbers belong to ecologists.
- **Not log-log versus linear-linear as the only comparison.** The middle condition, log axes with untransformed values, is the one most charts use, and it scored about the same as fully log-transformed.
- **Not a claim about labeled, gridded or annotated log axes.** No remediation was tested.
- **Not 93%/56% as two figures each resting on 623 respondents.** They aggregate randomized item subsets.

## Links

- Publisher page and abstract: [nature.com/articles/s41559-018-0610-7](https://www.nature.com/articles/s41559-018-0610-7)
- Supplementary PDFs (free): MOESM1 through MOESM6 on the publisher page. MOESM1 and MOESM3 are the supplementary tables and figure legends, MOESM4 is the full survey instrument.
- Author page: [columbia.edu/~dm2972/pubs.html](https://www.columbia.edu/~dm2972/pubs.html), which also links a SharedIt read-only version
- [refutations.md](../refutations.md), "Log scales are fine for expert audiences"
- [inventory.md](../inventory.md), topic 12 (log and other nonlinear scales)
- [Romano et al. 2020](romano-2020-log-scales-covid.md), the general-public counterpart, which cites this paper
