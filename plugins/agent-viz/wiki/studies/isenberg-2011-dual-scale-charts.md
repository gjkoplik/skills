---
type: study
status: primary-read
retrieved: 2026-08-23
---

# Isenberg, Bezerianos, Dragicevic & Fekete 2011: A Study on Dual-Scale Data Charts

Petra Isenberg, Anastasia Bezerianos, Pierre Dragicevic, Jean-Daniel Fekete. IEEE TVCG (Proceedings of InfoVis) 2011, vol. 17 no. 12. DOI [10.1109/TVCG.2011.160](https://doi.org/10.1109/TVCG.2011.160).

An experiment comparing four ways to show **two magnifications of the same series** in one chart (cut-out, broken, lens, superimposed) against a regular chart, on Cleveland's position, length and slope tasks.

**What it is good for.** Choosing a focus-plus-context design. A caution against the superimposed design, which lost on accuracy, time and ranking. The paper's statement that evidence on dual-scale charts was missing.

**What it does not settle.** Dual-*variable* twin axes, which it did not test ([below](#dual-scale-is-not-dual-variable)).

**How this was read.** Extracted locally with `pdftotext` from the author copy at [petra.isenberg.cc](https://petra.isenberg.cc/publications/papers/Isenberg_2011_ASO.pdf). PDF metadata marks it as the author camera-ready ("Submission for InfoVis 2011", created September 2011, IEEE acceptance block dated 1 August 2011), so it could differ from the typeset version in copyediting. The HAL and LRI mirrors were behind bot-check walls. This paper is the origin of one of the [retrieval hazards](../../CONTRIBUTING.md#retrieval-hazards): a web-fetch summarizer returned, **in quotation marks**, "Superimposed charts performed best overall and are recommended for most tasks." The abstract says the opposite.

## The finding

> "Our study suggests that cut-out charts which include collocated full context and focus are the best alternative, and that superimposed charts in which focus and context overlap on top of each other should be avoided."

Cut-out ranked first in the questionnaire for every task and location. Superimposed ranked last every time, and last overall for 14 of 15 participants, who called it "very confusing and demanding too much concentration or reflection to decipher the non-monotonic and discontinuous nature of the two scales." On the 7-point confidence scale, "for S all participants reported not to be confident about their answers."

On the position task, chart affected error, F(4,56) = 25, p < .0001. Mean absolute error was -0.2 for regular, -0.07 for cut-out, 0.26 for lens, 0.95 for broken and 2.1 for superimposed.

The recommendation also admits the broken chart:

> "Due to the ease of implementation of the broken chart we recommend to use this chart as an alternative to the cut-out chart if one has to save display space or cannot easily generate a cut-out chart."

## Dual-scale is not dual-variable

"Although the term dual-scale has been often used to specifically refer to superimposed charts, in this article we use it to refer to any chart showing two main scales." Every stimulus is two magnifications of **one** series. The superimposed condition resembles a twin-axis chart ("Superimposed charts are commonly used when two data sets have only one axis in common."), but limitation (3) says what was run:

> "There are many different ways to use superimposed charts, e. g., to compare data which uses different units of measure or which is significantly different in scale. We tested the second case and also designed the chart so that there was no overlap in the units on the top and bottom axis. The results could be different for other design alternatives but we hypothesize that this would not be the case."

The different-units case, which is what people mean by a twin-axis chart, was not tested. The paper also records the evidence gap:

> "Several experts discuss problems with the Dual-Scale chart in Fig. 1(b) and recommend careful design or to avoid using it altogether. Yet, empirical evidence on the effectiveness of the Dual-Scale compared to other charts is missing."

So the paper most often cited for a twin-axis ban reports that no such evidence exists.

## Method

Within-subjects: five charts, three tasks, each in focus, context and across-scale locations, at breakpoint magnifications u_b = 2, 5, 10. Six trials per cell gave **720 trials per participant**, Latin-square ordered, in 90 to 120 minutes. Participants judged a stimulus as a percentage (0 to 100%) of a reference object, in **data space** rather than drawing space, so tick spacing mattered. Measures were error and time to first keypress. Gridlines were equally spaced on all charts, following Zanella et al.'s finding that a grid is the most useful cue for a visual distortion.

## Sample size and population

**Fifteen participants** (10 male, 5 female) from the authors' research institute, ages 24 to 39, median 26. Eight students and seven non-students in "predominantly technical occupations." Nine saw such charts at least weekly, six monthly or less. Unpaid. Between-person generality is not established.

## Limits the authors state themselves

Six, quoted in condensed form:

> "(1) We believe that the good performance of the regular chart is a direct consequence of our experiment design. We specifically tested modulus values which were visible in the focus for all breakpoint conditions... For tasks in which the focus information would be invisible or very small, the regular chart would not fare as well and we expect the cut-out chart and possibly others to outperform it."

> "(2) We made specific choices in chart design which influenced our results. In contrast to our experiment, common implementations of the cut-out chart include two different scales for the top and bottom y-axis, which could negatively influence the performance of this chart for tasks involving slope judgements."

> "(3) There are many different ways to use superimposed charts, e. g., to compare data which uses different units of measure or which is significantly different in scale. We tested the second case..."

> "(4) We tested a specific gridline and tickmark spacing, set to be the same for all charts and scales... The influence of such indicators as well as the presence of data labels will have to be investigated further when gridline spacing differs."

> "(5) Our experiment explicitly compared non-interactive charts that are often seen in print. Our results may differ in interactive charts, where users can adjust the location and magnification of the focus area."

> "(6) Finally, this experiment focused on low-level perceptual tasks which compared isolated visual variables... Further experiments are necessary to confirm the influence of two scales for tasks on fully drawn Dual-Scale bar-, line-, area-, or other charts."

The slope task reduced to length by design:

> "we had designed each slope to connect two data points offset by 1 data unit. This meant that participants only had to compare the slope's y-offset which subsequently boiled down to a length comparison in the undistorted y-space."

## What this result does not license

- **Not a ban on two-variable twin axes.** Different chart, untested per limitation (3).
- **Not "superimposed charts are bad in general."** One design, one magnification regime, no unit overlap, n=15, isolated perceptual tasks.
- **Not a claim about interactive charts.** Limitation (5).
- **Not a claim about slope perception under scale change.** Limitation (6), and the slope task was a length judgment.
- **Not a transferable "cut-out wins" rule.** Limitation (1) ties the regular chart's showing to the modulus always being visible in the focus. Limitation (2) notes real cut-out charts usually have two y-scales.

[refutations.md](../refutations.md) records a caution instead: the apparent correlation between twin-axis series is a free parameter of the scaling. Its alternatives are stacked panels sharing an x-axis, or a statement of what each scale was pinned to. A published defense of the form ("Dual Y Axes Charts Defended") further undercuts a flat ban.

## Links

- Author copy: [petra.isenberg.cc/publications/papers/Isenberg_2011_ASO.pdf](https://petra.isenberg.cc/publications/papers/Isenberg_2011_ASO.pdf)
- HAL record: [hal.science/inria-00638535](https://hal.science/inria-00638535)
- PubMed: [22034368](https://pubmed.ncbi.nlm.nih.gov/22034368/)
- [refutations.md](../refutations.md), "A flat ban on dual axes" and "Tooling hazards"
- [inventory.md](../inventory.md), topic 13 (dual axes)
