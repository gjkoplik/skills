# Isenberg, Bezerianos, Dragicevic & Fekete 2011: A Study on Dual-Scale Data Charts

Petra Isenberg, Anastasia Bezerianos, Pierre Dragicevic, Jean-Daniel Fekete. IEEE TVCG (Proceedings of InfoVis) 2011, vol. 17 no. 12. DOI [10.1109/TVCG.2011.160](https://doi.org/10.1109/TVCG.2011.160).

## What it is

A design-space analysis plus a controlled experiment comparing four ways of packing **two magnifications of the same series** into one chart: cut-out, broken, lens, and superimposed, benchmarked against a regular single-scale chart. Tasks are Cleveland's elementary graphical perception tasks: position, length, slope.

## Status

**`primary-read`.** Extracted locally with `pdftotext` from the author copy at [petra.isenberg.cc](https://petra.isenberg.cc/publications/papers/Isenberg_2011_ASO.pdf). PDF metadata identifies it as the author camera-ready ("Submission for InfoVis 2011", created September 2011, carrying the IEEE accepted-1-August-2011 block), so it has no published page numbering and could in principle differ from the IEEE typeset version in copyediting. Retrieval date: **2026-08-23**.

The HAL and LRI mirrors are currently behind bot-check walls. Do not substitute a fetch summary for this paper: see the extraction warning below.

## What it is good for

- Choosing among **focus-plus-context chart designs** when one series has to be shown at two resolutions.
- A grounded caution against the **superimposed** design specifically, which lost on accuracy, on time, and on subjective ranking.
- The paper's own statement that **empirical evidence on dual-scale charts was missing**, which is still the cleanest citation for the evidence gap.

## What it does not settle

**Dual-*variable* twin axes.** That is the whole point of this page. See the category error section.

---

## The finding

From the abstract:

> "Our study suggests that cut-out charts which include collocated full context and focus are the best alternative, and that superimposed charts in which focus and context overlap on top of each other should be avoided."

Cut-out was ranked first for every task and task-by-location combination in the post-study questionnaire; superimposed was ranked last every time, and last overall by all but one of the fifteen participants. Participants described superimposed as "very confusing and demanding too much concentration or reflection to decipher the non-monotonic and discontinuous nature of the two scales." On the 7-point confidence scale, "for S all participants reported not to be confident about their answers."

Representative numbers, from the position task: a significant effect of chart on error, F(4,56) = 25, p < .0001. Mean absolute error was -0.2 for regular, -0.07 for cut-out, 0.26 for lens, 0.95 for broken, and 2.1 for superimposed.

The practical recommendation the authors land on is more nuanced than "use cut-out":

> "Due to the ease of implementation of the broken chart we recommend to use this chart as an alternative to the cut-out chart if one has to save display space or cannot easily generate a cut-out chart."

## The category error this page exists to stop

**Dual-scale is not dual-variable.** The paper defines its own term: "Although the term dual-scale has been often used to specifically refer to superimposed charts, in this article we use it to refer to any chart showing two main scales." Every stimulus is two magnifications of **one** series, a focus region and a context region.

The superimposed condition is the near neighbor of the twin-axis chart, and the paper acknowledges the family resemblance: "Superimposed charts are commonly used when two data sets have only one axis in common." But the stimulus that was actually run is the focus-plus-context variant, and limitation (3) says exactly which case was tested and which was not:

> "There are many different ways to use superimposed charts, e. g., to compare data which uses different units of measure or which is significantly different in scale. We tested the second case and also designed the chart so that there was no overlap in the units on the top and bottom axis. The results could be different for other design alternatives but we hypothesize that this would not be the case."

The different-units case, which is what people mean by a twin-axis chart, is the case they did not test. The hypothesis in the last sentence is a hypothesis, offered as such.

**The paper also states the evidence gap itself:**

> "Several experts discuss problems with the Dual-Scale chart in Fig. 1(b) and recommend careful design or to avoid using it altogether. Yet, empirical evidence on the effectiveness of the Dual-Scale compared to other charts is missing."

So the paper most often cited *for* a twin-axis ban is the paper reporting that no such evidence exists.

## Method

Within-subjects repeated measures, run in the authors' research institute.

Five chart conditions: Regular (single scale), Cut-out, Broken, Lens, Superimposed. Three tasks (position, length, slope), each in focus, context, and across-scale locations, at three breakpoint magnifications (u_b = 2, 5, 10). Six trials per task-by-chart-by-location-by-breakpoint cell, giving **720 trials per participant**. Order randomized by Latin square. Session length 90 to 120 minutes.

Magnitude estimation with a modulus: a reference object was shown on the chart and the participant judged the stimulus object as a percentage of it, always between 0 and 100%, judged in **data space** rather than drawing space, so gridline and tick spacing had to be taken into account. Dependent variables were magnitude of error and time. Timing started when the chart appeared and stopped at the first keypress, so typing time is excluded.

Gridlines were present on all charts and set to the same spacing everywhere, following Zanella et al.'s finding that a grid is the most useful cue for a visual distortion.

## Sample size and population

**Fifteen participants** (10 male, 5 female), recruited from the authors' research institute. Ages 24 to 39, median 26. All reported normal or corrected-to-normal vision. Eight students, seven non-students in "predominantly technical occupations." Nine reported at least weekly exposure to charts of this kind; six reported monthly or less. Unpaid.

A lab-recruited, technically skilled convenience sample of fifteen. The trial count per participant is high, so within-subject power is reasonable, but between-person generality is not established.

## Limits the authors state themselves

The paper lists six, quoted in condensed form:

> "(1) We believe that the good performance of the regular chart is a direct consequence of our experiment design. We specifically tested modulus values which were visible in the focus for all breakpoint conditions... For tasks in which the focus information would be invisible or very small, the regular chart would not fare as well and we expect the cut-out chart and possibly others to outperform it."

> "(2) We made specific choices in chart design which influenced our results. In contrast to our experiment, common implementations of the cut-out chart include two different scales for the top and bottom y-axis, which could negatively influence the performance of this chart for tasks involving slope judgements."

> "(3) There are many different ways to use superimposed charts, e. g., to compare data which uses different units of measure or which is significantly different in scale. We tested the second case..."

> "(4) We tested a specific gridline and tickmark spacing, set to be the same for all charts and scales... The influence of such indicators as well as the presence of data labels will have to be investigated further when gridline spacing differs."

> "(5) Our experiment explicitly compared non-interactive charts that are often seen in print. Our results may differ in interactive charts, where users can adjust the location and magnification of the focus area."

> "(6) Finally, this experiment focused on low-level perceptual tasks which compared isolated visual variables... Further experiments are necessary to confirm the influence of two scales for tasks on fully drawn Dual-Scale bar-, line-, area-, or other charts."

They also flag that their slope task collapsed into a length comparison by design: "we had designed each slope to connect two data points offset by 1 data unit. This meant that participants only had to compare the slope's y-offset which subsequently boiled down to a length comparison in the undistorted y-space."

## What this result does not license

- **Not a ban on two-variable twin axes.** Wrong chart. The authors say the different-units case is untested, in limitation (3).
- **Not "superimposed charts are bad in general."** One design, one magnification regime, no unit overlap between the two axes, at n=15, on isolated perceptual tasks.
- **Not a claim about interactive charts.** Limitation (5).
- **Not a claim about slope perception under scale change.** Limitation (6) plus the authors' own note that the slope task reduced to a length judgment.
- **Not a transferable "cut-out wins" rule.** Limitation (1) says the regular chart's strong showing is an artifact of always keeping the modulus visible in the focus, and limitation (2) says a real-world cut-out chart usually uses two y-scales, unlike the tested one.

For the flat-dual-axis-ban question specifically, the honest formulation is the one in [refutations.md](../refutations.md): a caution with its reason. The apparent correlation between two series on twin axes is a free parameter of the scaling choice, so prefer two stacked panels sharing an x-axis, and if the twin axis stays, say what each scale was pinned to. There is also a published defence of the form in the literature ("Dual Y Axes Charts Defended"), which further undercuts a flat ban.

## Extraction warning

This paper is the origin of one of the two [retrieval hazards](../../CONTRIBUTING.md#retrieval-hazards) on record here. Asked to summarize it, a web-fetch summarization returned, **in quotation marks**, "Superimposed charts performed best overall and are recommended for most tasks." The abstract says the exact opposite. Re-extract the PDF locally.

## Links

- Author copy: [petra.isenberg.cc/publications/papers/Isenberg_2011_ASO.pdf](https://petra.isenberg.cc/publications/papers/Isenberg_2011_ASO.pdf)
- HAL record: [hal.science/inria-00638535](https://hal.science/inria-00638535) (bot-check walled at time of retrieval)
- PubMed: [22034368](https://pubmed.ncbi.nlm.nih.gov/22034368/)
- [refutations.md](../refutations.md), "A flat ban on dual axes" and "Tooling hazards"
- [inventory.md](../inventory.md), topic 13 (dual axes)
