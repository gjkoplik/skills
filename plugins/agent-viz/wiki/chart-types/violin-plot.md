---
type: chart-type
relationships: [distribution, uncertainty]
aliases: [Violin plot]
---

# Violin plots

A kernel density estimate of one variable, mirrored about the group's axis position and filled, so each group becomes a symmetric shape whose width is the estimated density at that value.

## When to reach for it, and when not

The form is defined for several groups on one axis, each large enough that the density describes the data rather than the bandwidth, where within-group shape matters: a second mode, a heavy tail, a pile-up at a bound. The one tested use is a mean and its error. [Correll & Gleicher (2014)](../studies/correll-gleicher-2014-error-bars-harmful.md) proposed the violin as one of two encodings with the property they ask for: "We can mitigate these problems by choosing encodings that are visually symmetric and visually continuous."

| The question | Alternative |
|---|---|
| n is small per group | The observations. A density over six points pictures the bandwidth |
| What is the median, exactly? | [Box plot](boxplot.md) or a table. The peak is not the median |
| Is this group significantly different? | A labeled interval. The width is sample spread |
| One group, shape is the point | [Histogram](histogram.md). Mirroring needs something to compare against |
| How many observations per group? | Not shown, and area normalization can hide it |
| Many groups, compactly, no knob to defend | [Box plot](boxplot.md) |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per observation, one continuous variable, usually a grouping variable |
| Transform | Kernel density estimate (kernel, bandwidth, grid), normalized per group to equal area or across groups to encode count |
| Geometry | Filled polygon mirrored about the group's position, often with a box plot or quantiles inside |
| Scale | Value to position, density to half-width |
| Coordinates | Cartesian, one axis categorical |
| Guides | The value axis, the bandwidth and normalization rule, n per group. The density usually has no axis |

Three consequences are definitional. The estimate puts density where no observation lies, even outside a bounded domain unless the kernel is truncated. Bandwidth decides modality. Equal-area normalization draws a group of eight as wide as a group of eight hundred.

## Channels

Value is position along a common scale and density is width, an area reading once filled, both inherited from [channels.md](../concepts/channels.md). No study has decomposed a violin into cues, and [Skau & Kosara (2016)](../studies/skau-kosara-2016.md) found the received account wrong for the pie. Mirroring doubles the ink but creates the symmetry Correll & Gleicher's result turns on. Whether readers use both halves is untested. `absence of evidence`.

## What is measured

Inferential judgments about a mean and its error, against a bar with error bars, are measured. Correll & Gleicher ran 240 participants through three crowdsourced experiments. `evidence-backed`.

- The bar's "false metaphor of containment" made outcomes inside the bar look likelier than outcomes the same distance above the mean, a significant interaction at F(2,2) = 21.3, p < 0.0001. Not significant for the violin.
- Adherence to the expected strategy was highest with the violin, 89.2% of trials, against 83.2% for bars.
- Mean confidence was 5.06 with the violin and 5.12 with the gradient, against 4.86 for both bars and box plots. No pairwise test of the violin against the box plot or the bar is reported.
- Mechanical Turk workers showed no within-the-bar bias with the unfamiliar mark, and the authors report that unfamiliarity cost a general audience nothing.

The violins encoded a mean and error, not a raw sample, on low-stakes tasks. The authors: "One area not well-covered by our experimental tasks was decision-making." And: "the practical effect of these differences is difficult to determine."

No study in this corpus tests a violin against a box plot, a histogram or the plotted observations, on any task.

Which symmetric encoding to use is `contested`. Correll & Gleicher decline to rank their two: "Our data do not support the use of one over the other for decisions tasks, however paper authors, reviewers, and colleagues have stated differing preferences between the two on aesthetic and theoretical grounds."

Bimodality detection against a histogram, the value of the mirrored half, and how bandwidth moves a conclusion are all untested. `absence of evidence` ([evidence-class.md](../concepts/evidence-class.md)). Bandwidth as an undetermined analysis choice comes from [wilke-fundamentals.md](../sources/wilke-fundamentals.md) chapter 14 and [inventory.md](../inventory.md) topic 52, both `authority-asserted`.

## The failure mode it invites

**A confident shape over almost no data.** The curve looks as smooth at n = 6 as at n = 600. It is the [box plot](boxplot.md)'s missing-n problem plus a smoothing parameter, and the group sizes [Weissgerber et al.](../studies/weissgerber-2015-beyond-bar-line.md) found in published science, median minimum 4, are in that range.

**Bandwidth tuned until modes appear.** The knob is invisible. [inventory.md](../inventory.md) topic 52's mitigation is an explicit bandwidth, with the claim checked against a wider and a narrower one. `authority-asserted`.

**Widths compared across separately normalized groups.** Equal area is a common default, and the drawing does not say it ran.

**Density past a bound.** Durations, counts or proportions can show mass below zero or above one. [seaborn](../sources/seaborn.md) says symmetric error bars "may extend to 'impossible' values". The transfer to kernel estimates is by construction.

## Justifying the choice

**Defensible, evidence-backed:**

- "I encoded the mean and its error as a violin rather than a bar with error bars. The bar made outcomes inside it look likelier than equidistant outcomes above it, and the violin did not show that bias; adherence to the expected strategy was also higher." `evidence-backed`.
- "The audience is not technical, and unfamiliarity is not a reason to keep the bar. A general crowdsourced audience showed no containment bias with the unfamiliar symmetric encoding, and the authors report that unfamiliarity cost them nothing."

**Defensible, with the label said out loud:**

- "Violin rather than gradient plot. The study that recommends both explicitly declines to rank them, so this is preference, not evidence."
- "Bandwidth is stated and the second mode survives a wider and a narrower choice. There is no measured rule for bandwidth." `authority-asserted`.
- "Violin rather than box plot because the second mode is the finding. Nobody has measured whether readers actually pick modality off a violin more reliably; the box plot's inability to express it, on the other hand, is definitional." `absence of evidence`.
- "Widths are comparable across groups because the areas are scaled by count rather than normalized per group."

**Commonly repeated, and the evidence does not support it:**

- ~~"A violin shows the data."~~ It shows a smoothed estimate, and at small n it shows the bandwidth.
- ~~"Violin plots are more accurate than box plots."~~ The one study with both compared each against bars, using a modified uncertainty box plot, not Tukey's. Their mean confidence ratings were 5.06 and 4.86, with no pairwise test reported. Nobody has ranked them on accuracy.
- ~~"The violin is the modern replacement for the box plot."~~ Never compared. The evidence covers a symmetric continuous encoding against a bar with error bars.
- ~~"Symmetry is decoration."~~ The paper states it as the design requirement its result turns on.

## See also

- [distribution.md](distribution.md): the group, and the sample-size gate
- [boxplot.md](boxplot.md): the same strip with no tuning parameter and no shape
- [../studies/correll-gleicher-2014-error-bars-harmful.md](../studies/correll-gleicher-2014-error-bars-harmful.md): the one experiment with a violin
