---
type: chart-type
relationships: [uncertainty]
aliases: [Gradient plot]
---

# Gradient plots

A mean on a shared quantitative axis with a symmetric band of color around it whose opacity changes continuously, so the error is drawn without a hard edge.

"Gradient plot" is [Correll & Gleicher's (2014)](../studies/correll-gleicher-2014-error-bars-harmful.md) name: "Gradient plots and violin plots are example solutions." [Wilke](../sources/wilke-fundamentals.md) chapter 16 catalogs "graded error bars" and "confidence strips", and nothing here says whether either is the same construction. "Fuzzy error bar" is defined by no source here.

## When to reach for it, and when not

The form is defined for a mean and its error, where the reader judges how likely an outcome is or whether two means differ, and the exact bounds do not have to be read off. Correll & Gleicher tested it as a replacement for the bar with error bars, with Mechanical Turk workers.

| The question | Alternative |
|---|---|
| Is zero inside the 95% CI? What are the bounds? | [Interval plot](interval-plot.md). The gradient has no edge to read |
| What shape is the sample? | [Distribution](distribution.md) |
| n is 3 or 4 per group | The observations: a [dot strip plot](dot-strip-plot.md) or [beeswarm](beeswarm-plot.md) |
| Gradient or violin? | [Violin plot](violin-plot.md), equally. The one study that tested both declines to rank them |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per observation with a grouping variable, or a precomputed mean and margin of error per group |
| Transform | A mean and an error per group, then opacity as a function of distance from the mean |
| Geometry | A filled band centered on the mean, shaded by a gradient |
| Scale | Mean to position on a shared quantitative axis. Distance from the mean to opacity |
| Coordinates | Cartesian, one axis categorical |
| Guides | The value axis, and a statement of which interval the gradient encodes and at what level, with n |

The tested gradient was opaque inside the margin of error rather than shaped to the probability density, with one color ramp. The authors list both as unexplored design parameters.

## Channels

The mean is position along a common scale, the most accurately read channel in [channels.md](../concepts/channels.md). The error is opacity, which sits with shading and saturation at the bottom of Cleveland & McGill's table. The reader's task here is a likelihood judgment, not reading a number off the mark, and the ranking does not cover that ([the scope limit](../concepts/channels.md#what-the-ranking-is-not-about)). The step from mark to channel is conjecture in the source literature. What Correll & Gleicher's result turns on is two properties of the mark, symmetry and continuity.

## What is measured

Inferential judgments about a mean and its error, against a bar with error bars. Correll & Gleicher, 240 crowdsourced participants:

- With bars, outcomes inside the bar were rated likelier than outcomes the same distance above the mean, F(2,2) = 21.3, p < 0.0001. The gradient did not show this.
- Adherence to the expected strategy was 88.5% of trials with the gradient, against 83.2% with bars.
- Confidence was highest with the gradient, M = 5.12, against 5.06 for the violin and 4.86 for bars and box plots.

`evidence-backed`, on low-stakes predictions. The authors: "One area not well-covered by our experimental tasks was decision-making." And: "the practical effect of these differences is difficult to determine."

Against the violin, the record does not decide. "Our data do not support the use of one over the other for decisions tasks, however paper authors, reviewers, and colleagues have stated differing preferences between the two on aesthetic and theoretical grounds." No study here tests the gradient against a dot with whiskers or against the plotted observations.

## The failure mode it invites

**An unstated mapping.** What full opacity means (the edge of a 95% CI, one SE, the margin of error) is in the guides only, the same exposure as on [interval-plot.md](interval-plot.md).

**A ramp that biases the reading.** The authors name Cleveland & McGill's color-caused optical illusion as a way other gradient designs might bias judgments. Untested. `absence of evidence`.

## Justifying the choice

**Defensible, evidence-backed:**

- "A gradient rather than a bar with error bars. The bar made outcomes inside it look likelier than equidistant ones above it, and the gradient did not."
- "The audience is general, and the form's unfamiliarity is not a reason to avoid it. Crowdsourced readers followed the expected strategy more often with the gradient than with the bar."

**Defensible, with the label said out loud:**

- "Gradient rather than violin. The study that tested both declines to rank them, so this is preference."
- "The ramp and the opacity rule are mine. The tested version used one ramp, and the authors say others might bias judgments."

**Commonly repeated, and not supported:**

- ~~"The gradient shows the probability distribution."~~ The tested gradient was opaque inside the margin of error rather than shaped to the density.
- ~~"Gradient plots are the best uncertainty encoding."~~ The authors: "Our experiments suggest that some encoding other than bar charts with error bars should be used, but are less specific in recommending the best replacement."
- ~~"Gradients lead to better decisions."~~ No real decisions were tested.

## See also

- [uncertainty.md](uncertainty.md): the group
- [violin-plot.md](violin-plot.md): the other symmetric continuous form tested
- [interval-plot.md](interval-plot.md): the hard-edged form, and the bar with error bars it was tested against
