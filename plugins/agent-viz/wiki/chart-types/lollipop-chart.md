---
type: chart-type
relationships: [magnitude, ranking]
aliases: [Lollipop chart]
---

# Lollipop charts

A dot at the value with a thin stem running back to the baseline. A [bar chart](bar-chart.md) with the fill taken out, and that is the whole of the difference.

## When to reach for it, and when not

The form is defined for the case where there are enough categories that filled bars turn the plot into a block of ink, and the reader's job is to find and compare a few values inside a long sorted list. The FT's one-line gloss ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)):

> "Lollipop charts draw more attention to the data value than standard bar/column -- **does not HAVE to start at zero (but preferable)**"

`authority-asserted`, both halves. Nothing in this corpus tests either one.

Questions the form does not answer:

| The question | Alternative |
|---|---|
| How many times bigger is this than that? | [Bar chart](bar-chart.md). Ratio comparison is one task where the filled bar has measured support |
| There are six categories | [Bar chart](bar-chart.md). The ink saving is the reason to be here, and at six bars there is none |
| Does this add up, and to what? | [Part-to-whole](part-to-whole.md). Neither form asserts a total, and this one asserts it less |
| Two values per category, and the gap is the point | [Dumbbell plot](dumbbell-plot.md). There the stem spans the gap rather than the baseline |
| What does the distribution look like? | A histogram or a univariate scatterplot. The stem implies a magnitude from zero |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per category, with a magnitude |
| Transform | None, usually |
| Geometry | A point at the value, plus a rule from the baseline to the point |
| Scale | Magnitude to position |
| Coordinates | Cartesian |
| Guides | One quantitative axis, a category axis, labels |

**It differs from a bar chart in the geometry slot alone.** That is the entire structural claim: the decomposition offers no reason to expect a different reading, and no study has looked.

## Channels

**Position along a common scale**, same as the bar chart, read at the dot rather than at the bar's end. Inherited from [channels.md](../concepts/channels.md) with the usual caveat that the mapping from mark to channel is conjecture in the source literature.

Two structural notes that follow from the geometry and assert nothing empirical. The **stem is a guide, not an encoding**: it exists so the eye can get from the category axis to the dot, which is why removing it gives a dot plot rather than a broken lollipop. And **there is no filled area**, which is the basis of the FT's and Datawrapper's release of the zero baseline for this form.

## What it is measurably good at

**Nothing has been measured on this form.** No study in this corpus uses a lollipop chart as a stimulus, tests it against a bar chart, or decomposes it into channels. `absence of evidence`.

What can be said without measurement is the structural point above: the value sits on the same channel a bar's end sits on. That is an inheritance, not a finding, and it does not license "as accurate as a bar chart."

## What it is measurably bad at

**Also unmeasured.** Two nearby results bear on it, and both need their distance stated.

**Ratio comparison, from a study of dot plots rather than lollipops.** [Correll & Gleicher (2014)](../studies/correll-gleicher-2014-error-bars-harmful.md), in passing: "comparing ratios can be done quickly and more accurately with bar charts as compared to dot plots." A lollipop is not a dot plot, since it keeps a stem to the baseline, so this is suggestive about the direction and is not a test of this form.

**The terminator mechanism cuts against the dot.** [Skau, Harrison & Kosara (2015)](../studies/skau-2015-embellished-bars.md) found that a bar with a strong horizontal cap matched the plain baseline while every embellishment that rounded or pointed the top raised error, and proposed that readers "rely on strong lines at the ends of bars to mentally extend the bar end to the value axis." A lollipop replaces the terminator with a circle. **They did not test a lollipop**, and the mechanism is their hypothesis rather than their result, so this is an extrapolation from a conjecture rather than evidence.

The most cited reason to prefer a lollipop is ink, and the one mechanism in the literature that would predict a cost has never been pointed at it.

## What is contested

**The zero baseline, and the disagreement is among authorities with no experiment on either side.**

The FT releases it for this form, and the capitals in its own text sit on the negation: the lollipop "does not HAVE to start at zero (but preferable)", against a plain "Must always start at 0 on the axis" for the filled column ([ft-visual-vocabulary.md](../sources/ft-visual-vocabulary.md)). Both statements sit in its Magnitude category, and no gloss outside that category mentions a baseline at all, so the FT scopes the rule by mark *within* the size-comparison task rather than across every quantitative axis. Datawrapper gives the reasoning explicitly: "Readers don't expect dot plots (or, for two values, range plots) to start at zero because there's no filled bar or column that would indicate that" ([datawrapper-academy.md](../sources/datawrapper-academy.md)). Urban releases marks that "do not use length or height as the primary encoding" ([urban-institute.md](../sources/urban-institute.md)). [Vega-Lite](../sources/vega-lite.md) goes the other way and forces zero on every quantitative positional scale regardless of mark.

What is measured is one step away: [Pandey et al. (2015)](../studies/pandey-2015-deceptive-visualizations.md) found truncating a **bar** axis moved size judgments 91%. Whether a stem behaves like a bar for that purpose is exactly the untested question. The by-mark scoping is `authority-asserted`, and the truncation result was not run on this form.

## The failure mode it invites

**Relaxing the baseline on a chart the reader parses as bars.** The stem runs from the axis to the dot, which is the same visual gesture a bar makes, so the argument for releasing zero ("no filled area, so no proportional-ink claim") is stronger on paper than it may be in a reader's eye. `absence of evidence` rather than a prohibition: nobody has checked, and the FT hedges in the same direction with "but preferable."

**Using it at small category counts to look less ordinary.** The ink saving is the whole case for the form. At six categories a bar chart is more familiar and better evidenced. `authority-asserted`.

## Justifying the choice

**Defensible, evidence-backed:**

- Nothing on this page qualifies. The one evidence-backed sentence available is inherited and belongs to the channel rather than to the form: "the value is on position along a common scale, which is the most accurately read channel." That is true of a [bar chart](bar-chart.md) too, and it does not distinguish the two.

**Defensible, with the label said out loud:**

- "Forty categories in filled bars is a wall of ink, so the fill comes out. That is a legibility judgment, not a measured improvement."
- "The axis does not start at zero, because the mark is not filled. A taxonomy, a chart tool and a style guide all scope the rule that way, none of them tested it, and one plotting library disagrees outright."
- "This draws attention to the value point rather than the bar's mass. Asserted by the FT in one line, and unmeasured."

**Commonly repeated and not supported:**

- ~~"A lollipop is as accurate as a bar chart, with less ink."~~ It is on the same channel; nobody has measured the form. The one mechanism anyone has proposed for how a bar gets read predicts the dot should be a little worse, and that prediction has never been tested either.
- ~~"Dot-based charts are safe to truncate, and it has been shown."~~ The scoping is a practitioner default. What was shown is that truncating a *filled bar* moves readers a long way.

## See also

- [bar-chart.md](bar-chart.md) — the same chart with the fill in, and the evidence
- [magnitude.md](magnitude.md) — the group, and the zero-baseline scoping stated once
- [../concepts/evidence-class.md](../concepts/evidence-class.md#what-is-exempt-and-why-the-exemption-matters) — why the decomposition above carries no label and the claims do
