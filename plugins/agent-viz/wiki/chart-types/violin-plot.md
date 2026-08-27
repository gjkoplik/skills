---
type: chart-type
relationships: [distribution]
aliases: [Violin plot]
---

# Violin plots

A kernel density estimate of one variable, mirrored about the group's axis position and filled, so each group becomes a symmetric shape whose width is the estimated density at that value.

## When to reach for it, and when not

**Reach for it when** several groups have to be compared on one axis, there are enough observations per group for a density estimate to be about the data rather than about the bandwidth, and the shape within a group is part of the question: a second mode, a heavy tail, a pile-up at a bound.

**Reach for it also when the subject is a mean and its error**, which is the one use anybody has tested. [Correll & Gleicher (2014)](../studies/correll-gleicher-2014-error-bars-harmful.md) proposed the violin as one of two example encodings satisfying a property they state directly: "We can mitigate these problems by choosing encodings that are visually symmetric and visually continuous."

**Do not reach for it when:**

| The question | Use instead |
|---|---|
| n is small per group | Plot the observations. A density over six points is a picture of the bandwidth |
| What is the median, exactly? | [Box plot](boxplot.md), or a table. The density's peak is not the median |
| Is this group significantly different? | The width is the spread of the sample, not an interval about an estimate, unless you drew one and said so |
| One group, and the shape is the point | [Histogram](histogram.md). The mirroring buys nothing when there is nothing to compare against |
| How many observations are in each group? | The violin does not say, and area normalization can actively hide it |
| Many groups, compactly, with no knob to defend | [Box plot](boxplot.md) |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per observation, one continuous variable, usually one grouping variable |
| Transform | Kernel density estimate with a chosen kernel and bandwidth, evaluated on a grid, then normalized: per group to equal area, or across groups to encode count |
| Geometry | Filled polygon, the density mirrored about the group's position. Often a box plot or quantile marks inside |
| Scale | Value to position along a common scale; density to half-width, so the visible extent is twice the density |
| Coordinates | Cartesian, one axis categorical |
| Guides | The value axis; the bandwidth and the normalization rule; n per group. The density itself usually has no axis at all |

Three consequences follow from that transform, all definitional and none of them empirical:

- **The estimate places density where no observation lies**, including past the most extreme one, unless the kernel is truncated at a bound. A bounded quantity can be drawn with mass outside its own domain.
- **Bandwidth decides modality.** Wide enough and two modes merge; narrow enough and noise separates into modes. The picture reports a choice as well as the data.
- **The normalization decides what width means.** Equal-area-per-group makes a group of eight as wide as a group of eight hundred.

## Channels

Value on position along a common scale; density on width, which is an area reading once the shape is filled and mirrored. Those accuracy claims are inherited from [channels.md](../concepts/channels.md), where position is measured as read more accurately than area, and they are not restated here as native findings.

**No study in this source set has decomposed a violin into its cues.** [Skau & Kosara (2016)](../studies/skau-kosara-2016.md) did exactly that for the pie and found the received channel account wrong, which is a reason to hold the mapping above loosely rather than a reason to doubt it specifically.

The mirroring is worth naming as an open question rather than a defect: it doubles the ink for one density and it is the thing that makes the shape symmetric, which is the property Correll & Gleicher's result actually turns on. Whether readers use both halves is untested.

## What it is measurably good at

**Inferential judgments about a mean and its error, compared with a bar and error bars.** Correll & Gleicher, 240 participants across three crowdsourced experiments:

- The bar's "false metaphor of containment" made outcomes inside the bar look likelier than outcomes the same distance above the mean, a significant interaction at F(2,2) = 21.3, p < 0.0001. Not significant for the violin.
- Adherence to the expected strategy was highest with the violin, 89.2% of trials, against 83.2% for bars.
- Confidence was higher with the two encodings carrying distribution detail (violin M = 5.06, gradient M = 5.12) than with bars and box plots (both M = 4.86).
- Unfamiliarity cost this audience nothing. Mechanical Turk workers, not statisticians, did better with the unusual mark than with the standard one.

**Scope, stated because the result is easy to over-quote.** That experiment drew violins as encodings of a mean and its error, not as displays of a raw sample. The tasks were low-stakes prediction with no real consequences, and the authors say so: "One area not well-covered by our experimental tasks was decision-making." They also decline to say the alternatives are practically important: "the practical effect of these differences is difficult to determine."

## What it is measurably bad at

**Nothing has been measured.** No study in this source set tests a violin against a box plot, against a histogram, or against plotting the observations, on any task.

Two things follow from the construction rather than from an experiment: at small n the shape is the bandwidth, and the smoothed estimate can put visible mass outside the data's range.

## What is contested

**Which symmetric encoding to use.** The authors who established that a symmetric continuous encoding beats a bar with error bars refuse to rank their own two candidates: "Our data do not support the use of one over the other for decisions tasks, however paper authors, reviewers, and colleagues have stated differing preferences between the two on aesthetic and theoretical grounds." Choosing the violin over the gradient plot is preference, and it should be stated as preference.

Everything else here is `absence of evidence` rather than contested, which [evidence-class.md](../concepts/evidence-class.md) keeps deliberately distinct from refuted. Nobody has measured whether readers detect bimodality more reliably from a violin than from a histogram, whether the mirrored half helps, or how bandwidth choice moves a reader's conclusion. The general treatment of bandwidth as an undetermined analysis choice comes from [wilke-fundamentals.md](../sources/wilke-fundamentals.md) chapter 14 and [inventory.md](../inventory.md) topic 52, both `authority-asserted`.

## The failure mode it invites

**A confident shape over almost no data.** The estimate always produces a smooth curve, and the curve looks equally authoritative at n = 6 and n = 600. This is the [box plot](boxplot.md)'s missing-n problem with a smoothing parameter added on top, and the sample sizes [Weissgerber et al.](../studies/weissgerber-2015-beyond-bar-line.md) measured in published science, median minimum group size 4, are squarely in the range where it bites.

**Tuning the bandwidth until the modes appear.** The knob is invisible in the output and the reader cannot check it. The mitigation is the one [inventory.md](../inventory.md) topic 52 states: choose it explicitly and confirm the claim survives a wider and a narrower choice. `authority-asserted`.

**Comparing widths across groups that were normalized separately.** Equal-area normalization is a common default and it makes width incomparable in count between groups. Definitional, and easy to miss because the drawing gives no sign of which normalization ran.

**Density spilling past a bound.** A distribution of durations, counts or proportions can be drawn with visible mass below zero or above one. The mechanism is the same one seaborn names for symmetric error bars on bounded quantities, where an interval "may extend to 'impossible' values" ([seaborn.md](../sources/seaborn.md)); that quote is about error bars, and the transfer to a kernel estimate is by construction, not by measurement.

## Justifying the choice

**Defensible, evidence-backed:**

- "I encoded the mean and its error as a violin rather than a bar with error bars. The bar made outcomes inside it look likelier than equidistant outcomes above it, measured, and the violin did not show that bias; adherence to the expected strategy was also higher."
- "The audience is not technical, and unfamiliarity is not a reason to keep the bar. A general crowdsourced audience did better with the unfamiliar symmetric encoding than with the familiar one."

**Defensible, with the label said out loud:**

- "Violin rather than gradient plot. The study that recommends both explicitly declines to rank them, so this is preference, not evidence."
- "Bandwidth is stated and the second mode survives a wider and a narrower choice. There is no measured rule for bandwidth."
- "Violin rather than box plot because the second mode is the finding. Nobody has measured whether readers actually pick modality off a violin more reliably; the box plot's inability to express it, on the other hand, is definitional."
- "Widths are comparable across groups because the areas are scaled by count rather than normalized per group."

**Commonly repeated, and not supported:**

- ~~"A violin shows the data."~~ It shows a smoothed estimate with a tunable parameter. At small n it shows the parameter. Plotting the observations, which is what "shows the data" describes, is a different chart.
- ~~"Violin plots are more accurate than box plots."~~ Not established. The one study that drew both compared each against bars, and its box plot was a modified uncertainty encoding rather than a Tukey box plot. On confidence the violin separated from the box plot; on accuracy nobody has ranked them.
- ~~"The violin is the modern replacement for the box plot."~~ The comparison has not been run. What the evidence supports is narrower and more specific: a symmetric continuous encoding beat a bar with error bars on inferential tasks.
- ~~"Symmetry is decoration."~~ It is the property the measured result turns on, and the paper states it as the design requirement rather than as an aesthetic.

## See also

- [distribution.md](distribution.md) — the group, and the sample-size gate that decides most of this
- [boxplot.md](boxplot.md) — the same strip with no tuning parameter and no shape
- [../studies/correll-gleicher-2014-error-bars-harmful.md](../studies/correll-gleicher-2014-error-bars-harmful.md) — the only experiment here that put a violin under test, and what it was testing
