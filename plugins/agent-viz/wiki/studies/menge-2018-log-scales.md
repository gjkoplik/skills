---
type: study
status: secondary-only
status_partial: true
retrieved: 2026-08-23
---

# Menge et al. 2018: Logarithmic scales in ecological data presentation may cause misinterpretation

Duncan N. L. Menge, Anna C. MacPherson, Thomas A. Bytnerowicz, Andrew W. Quebbeman, Naomi B. Schwartz, Benton N. Taylor, Amelia A. Wolf. *Nature Ecology & Evolution* 2 (2018), 1393-1402. DOI [10.1038/s41559-018-0610-7](https://doi.org/10.1038/s41559-018-0610-7).

A literature audit of how often ecology papers use log axes, plus a randomized survey of Ecological Society of America members asking them to read graphs that were shown either on linear-linear or on log-log axes. The comprehension gap is large.

**How this was read.** Coverage here is not uniform.

What was read directly: the **publisher's own abstract** on nature.com, which carries every headline number quoted below verbatim, and **all four supplementary PDFs**, which are free to download from the article page and are labeled "In the format provided by the authors and unedited." Those supplements contain Supplementary Tables 1 through 6, the supplementary figure legends, and the complete survey instrument and flow.

What was **not** read: the main text. *Nature Ecology & Evolution* is not open access, the article is not in PMC, no preprint or author PDF exists, and the SharedIt read-only link is a JavaScript viewer. Bot-check walls blocked the remaining mirrors.

So the numbers are confirmed against the publisher record rather than a third-party summary, but the Methods, Results and Discussion prose is unread, and **the paper's own stated limitations could not be quoted**. That is why the status stays `secondary-only`.

This is a **strengthening** of the caveat in [refutations.md](../refutations.md), which recorded the Menge percentages as reached "in secondary form only." They now check out against the authors' own abstract.

## What it is good for

Killing the claim that **log scales are fine for expert audiences**. The population here is professional ecologists, 69% of them holding PhDs, and log-log comprehension still collapses.

## What it does not settle

Anything about visualization design per se. This is a comprehension survey with hand-built stimuli about rabbit and chipmunk populations, not a study of chart design choices, and it does not compare log axes against any alternative other than linear.

---

## The finding

From the abstract, quoted:

> "Analysing the extent of log scales in the literature, we show that 22% of papers published in the journal *Ecology* in 2015 included at least one log-scaled axis, of which 21% were log-log displays. We conducted a survey that asked members of the Ecological Society of America (988 responses, and 623 completed surveys) to interpret graphs that were randomly displayed with linear-linear or log-log axes. Many more respondents interpreted graphs correctly when the graphs had linear-linear axes than when they had log-log axes: 93% versus 56% for our all-around metric, although some of the individual item comparisons were even more skewed (for example, 86% versus 9% and 88% versus 12%). These results suggest that misconceptions about log-scaled data are rampant."

The recommendation, also from the abstract:

> "We recommend that ecology curricula include explicit instruction on how to interpret log-scaled axes and equations, and we also recommend that authors take the potential for misconceptions into account when deciding how to visualize data."

**Note the wording of that second recommendation.** It is "take the potential for misconceptions into account," not "do not use log scales."

## Method, from the supplements

The survey was not a simple two-arm design. There were **three display conditions**, not two: linear scale, log scale with untransformed axis values, and log scale with log-transformed axis values. Each was presented both as a **graph** and as an **equation-plus-table** analog, so the design crosses display form with scale treatment.

Four attributes were probed per dataset: whether each population increases or decreases with distance; which increases relatively more; positive versus zero versus negative; and accelerating versus decelerating. Three hypothetical datasets were used, with equations and parameter values given in Supplementary Table 2.

The survey flow (Supplementary PDF 4) randomizes which items each respondent sees, which variant of each item, the order of answer options, and the order in which the four selected items appear. So **each respondent answered a randomized subset, not the full battery**. Per-item sample sizes in Supplementary Table 1 range from about 137 to 468, well below 623.

"Wouldn't notice" was an available response and is tabulated separately. It was near zero for graphs (0 to 1% typically) and substantial for equations (up to 42%), which is itself informative: people know when an equation is beyond them and do not know when a log graph is.

## Sample size and population

- **988 responses, 623 completed surveys.** Members of the Ecological Society of America.
- Demographics (Supplementary Table 4): 55% male, 45% female; ages 20 to 84, mean 43; 89% white; **69% hold a PhD**, 20% a master's, 11% a bachelor's; 35% professors, 18% PhD students, 11% government research scientists, 8% academic research scientists, 10% postdocs.
- Self-reported comfort with logarithms (Supplementary Table 5): 73% comfortable to some degree (8% extremely, 39% moderately, 26% slightly), 9% neutral, 18% uncomfortable. **89% had log-transformed data for analysis themselves.**
- Stated preference: 21% linear, 0.5% log, 67% "usually linear," 3% "usually log," 9% no opinion.

## The result that most people miss

Supplementary Table 3 splits percent correct by demographic. For graphs, the linear / log-untransformed / log-transformed triple is:

| Split | Linear | Log, untransformed | Log, transformed |
|---|---|---|---|
| Male / Female | 94 / 92 | 55 / 56 | 54 / 53 |
| PhD / no PhD | 94 / 91 | 56 / 56 | 55 / 51 |
| Professor / other | 94 / 93 | 55 / 56 | 55 / 53 |
| Over 43 / under 43 | 93 / 94 | 54 / 56 | 54 / 53 |

**The gap does not close for anyone.** Holding a PhD buys 3 points on linear graphs and 0 points on log-untransformed graphs. That is the finding that makes this paper worth citing, and it is in a supplementary table rather than the abstract.

Supplementary Figure 7 regresses correctness against self-reported comfort with logarithms and reports the coefficients: for graphs, 0.58 ± 0.53 (linear), 0.93 ± 0.61 (log untransformed), -0.06 ± 0.66 (log transformed), with t values 1.1, 1.5 and -0.08. **Self-reported comfort with logs does not predict getting log graphs right.**

## Limits, and the fact that the authors' own could not be read

**The main text was unreachable, so no author-stated limitation is quoted here.** Anything on this page describing a limit is an observation from the abstract, the supplements, or the survey instrument, not the authors' own framing. If this page ever needs to carry the authors' stated caveats, someone has to read the paper.

Observable limits from what was reached:

- **The "all-around metric" is never defined in the material reached.** The 93%-versus-56% headline depends on that definition, which is in the main text.
- **Per-item n is much smaller than 623.** The randomized flow means each item was seen by roughly 140 to 470 people.
- The stimuli are hypothetical rabbit and chipmunk populations, drawn from parameterized equations. This is not real ecological data and not a real reading task.
- The sample is self-selected among ESA members who chose to open a survey, and 365 of 988 respondents did not finish.
- The abstract's own verb is hedged twice: log scales "**may** cause misinterpretation," and the results "**suggest** that misconceptions about log-scaled data are rampant."

## What this result does not license

- **Not "never use log scales."** The authors' own recommendation is instruction plus author awareness. They do not tell ecologists to stop.
- **Not a general claim about all audiences.** The population is ecologists. It generalizes *downward* comfortably (if PhD ecologists who routinely log-transform data get 56%, a lay audience will not do better) but the specific numbers belong to this population.
- **Not "log-log versus linear-linear" as the only comparison.** There are three conditions. The middle one, log axes with untransformed values, is the one most charts actually use, and it scored about the same as fully log-transformed.
- **Not a claim about labeled, gridded, or annotated log axes.** The stimuli were what they were. No remediation was tested.
- **Do not quote 93%/56% as if each rested on 623 respondents.** It is an aggregate over randomized item subsets.
- **Do not quote author limitations from this page.** There are none here to quote.

## Links

- Publisher page and abstract: [nature.com/articles/s41559-018-0610-7](https://www.nature.com/articles/s41559-018-0610-7)
- Supplementary PDFs (free): linked as MOESM1 through MOESM6 from the publisher page. MOESM1 and MOESM3 are the supplementary tables and figure legends, MOESM4 is the full survey instrument.
- Author page: [columbia.edu/~dm2972/pubs.html](https://www.columbia.edu/~dm2972/pubs.html), which also links a SharedIt read-only version
- [refutations.md](../refutations.md), "Log scales are fine for expert audiences"
- [inventory.md](../inventory.md), topic 12 (log and other nonlinear scales)
- Related: [Romano et al. 2020](romano-2020-log-scales-covid.md), the general-public counterpart, which cites this paper
