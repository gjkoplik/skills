---
type: source
status: primary-read
retrieved: 2026-08-23
---

# seaborn documentation

The tutorial documentation for seaborn, the statistical plotting layer over matplotlib. Two chapters matter here: *Choosing color palettes* and *Statistical estimation and error bars*.

**How this was read.** Both pages fetched and converted locally from the seaborn v0.13.2 docs, retrieved 2026-08-23. Quotes are verbatim.

**What it is good for.** The **error bars** chapter is the most useful thing in this wiki on uncertainty display, because it separates two things that get conflated everywhere else: an interval showing *spread of the data* and an interval showing *uncertainty about an estimate*. It is also the only library documentation reviewed here that argues against the plot it has just taught.

**What it does not settle.** It is scoped to what seaborn draws. Nothing on titles, annotation, layout, export, or accessibility beyond one sentence on colorblindness. The color chapter is a well-argued restatement of the standard perceptual position, not new ground; matplotlib's colormaps page is the better citation for the underlying claim.

---

## The error-bar taxonomy

seaborn's `errorbar=` parameter is a 2x2: what the interval shows (spread vs. uncertainty) crossed with how it was constructed (parametric vs. nonparametric). That gives four named options, and the docs are explicit that they answer different questions:

> "The error bars around an estimate of central tendency can show one of two general things: either the range of uncertainty about the estimate or the spread of the underlying data around it. These measures are related: given the same sample size, estimates will be more uncertain when data has a broader spread. But uncertainty will decrease as sample sizes grow, whereas spread will not."

| | Parametric | Nonparametric |
|---|---|---|
| Spread of data | `"sd"` (± k standard deviations) | `"pi"` (percentile interval, default 95%) |
| Uncertainty of estimate | `"se"` (± k standard errors) | `"ci"` (bootstrap CI, default 95%) |

The size parameter carries a trap, stated in the docs: "For parametric error bars, it is a scalar factor that is multiplied by the statistic defining the error... For nonparametric error bars, it is a percentile width." So `("se", 2)` means two standard errors, and `("pi", 50)` means the interquartile range. Same slot, different units. Generated code gets this wrong.

This is the direct backing for inventory topic 49 (error-bar semantics must be stated). A bar chart with an unlabeled interval is genuinely ambiguous between four different things, and seaborn's own defaults changed at v0.12, so "seaborn default" is not a stable answer either. The docs flag that: before v0.12 the only options were a bootstrap CI or a standard deviation, via a `ci` parameter.

## Impossible intervals, stated as a real failure

> "The standard deviation error bars will always be symmetrical around the estimate. This can be a problem when the data are skewed, especially if there are natural bounds (e.g., if the data represent a quantity that can only be positive). In some cases, standard deviation error bars may extend to 'impossible' values. The nonparametric approach does not have this problem, because it can account for asymmetrical spread and will never extend beyond the range of the data."

Inventory topic 51. This one is mechanizable at low cost: a check that the drawn interval bounds stay inside the variable's domain. It is also the kind of defect that is invisible in source review, because nothing in the call looks wrong.

## The "are error bars enough?" section

The chapter closes by arguing against itself:

> "You should always ask yourself whether it's best to use a plot that displays only a summary statistic and error bar. In many cases, it isn't."

and

> "If you are interested in questions about summaries (such as whether the mean value differs between groups or increases over time), aggregation reduces the complexity of the plot and makes those inferences easier. But in doing so, it obscures valuable information about the underlying data points, such as the shape of the distributions and the presence of outliers."

That is inventory topic 50. The second quote is scoped: seaborn is not saying aggregation is wrong, it is saying aggregation trades distributional information for inferential clarity. A quality bar that flattens this into "always show the distribution" is overclaiming.

Two smaller, practical points from the same chapter:

- Bootstrap intervals are stochastic. "Bootstrapping involves randomness, and the error bars will appear slightly different each time you run the code that creates them." `n_boot` and `seed` control it. This is inventory topic 77 (repeatability) arriving from an unexpected direction: an unseeded bootstrap makes a figure non-reproducible pixel-for-pixel even when the data and code are fixed.
- "seaborn functions cannot currently draw error bars from values that have been calculated externally." An interval from a model fit elsewhere has to be drawn in matplotlib. Agents routinely miss this and silently plot seaborn's own recomputed interval instead of the intended one.

## Color palettes: hue for categories, luminance for numbers

The chapter's structure is the argument. Two rules, each demonstrated with a paired counterexample figure.

**Hue distinguishes categories.**

> "So as a general rule, use hue variation to represent categories."

with the standard cap stated as a comprehension cost rather than a hard number:

> "If you have more than a handful of colors in your plot, it can become difficult to keep in mind what each one means, unless there are pre-existing associations between the categories and the colors used to represent them. This makes your plot harder to interpret: rather than focusing on the data, a viewer will have to continually refer to the legend to make sense of what is shown."

**Luminance represents numbers.**

> "On the other hand, hue variations are not well suited to representing numeric data."

The demonstration is a bivariate histogram drawn twice, once with a circular (hue-varying) colormap and once with a luminance ramp; the two peaks are visible only in the second. Same claim as matplotlib's CIELAB argument, made visually instead of numerically.

**Accessibility, in one sentence, doing two jobs:**

> "Varying both shape (or some other attribute) and color can help people with anomalous color vision understand your plots, and it can keep them (somewhat) interpretable if they are printed to black-and-white."

That is redundant coding (topic 69) and grayscale survival (topic 27) in a single line, and it is the whole of seaborn's accessibility content. seaborn is not an accessibility source; [chartability.md](chartability.md) is.

## Defaults

- The default palette is `deep`, a desaturated `tab10`. The docs concede the cost: the moderated hues "are also less distinct. As a result, they may be more difficult to discriminate in some contexts, which is something to keep in mind when making publication graphics." A default chosen for looks, with the tradeoff written down.
- There is a `colorblind` variant, alongside `muted`, `pastel`, `bright`, `dark`.
- When more colors are needed than the cycle holds, seaborn falls back to evenly spaced hues in **HSLuv** rather than HLS, because equal RGB luminance does not mean equal perceived intensity.
- Four in-house perceptually uniform sequential maps: `rocket` and `mako` for space-filling marks like heatmaps, `flare` and `crest` for lines and points. The stated reason is that rocket and mako approach white at one extreme, so "it will be difficult to discriminate important values against a white or gray background." A rare piece of documentation that picks a colormap by *mark type* rather than by data type.
- Discrete sampling of a continuous map does **not** use the extremes, which is why a discrete legend and a colorbar in the same figure set can look mismatched.

## One uncited sentence

> "And aesthetics do matter: the more that people want to look at your figures, the greater the chance that they will learn something from them."

This is the emotive-quality claim (inventory topic 89), and seaborn asserts it without a citation. It is plausible and it is not evidence. The nearest actual experimental record is the chartjunk literature in [refutations.md](../refutations.md), which is contested in both directions.

## Where this source is used

Inventory topics 23, 24, 26, 28, 32, 49, 50, 51, 69. The mapping in [roll-call.md](../roll-call.md) holds up against this reading.

## Links

- [Choosing color palettes](https://seaborn.pydata.org/tutorial/color_palettes.html)
- [Statistical estimation and error bars](https://seaborn.pydata.org/tutorial/error_bars.html)
- Related: [matplotlib.md](matplotlib.md) for the perceptual argument in its stronger form
