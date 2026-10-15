---
type: source
status: primary-read
retrieved: 2026-08-23
---

# seaborn documentation

The tutorial documentation for seaborn, the statistical plotting layer over matplotlib: *Choosing color palettes* and *Statistical estimation and error bars*.

**What it is good for.** Uncertainty display. The error-bars chapter separates an interval showing the spread of the data from one showing uncertainty about an estimate, which most sources conflate, and then argues against the plot it has just taught.

**What it does not settle.** Titles, annotation, layout, export, and accessibility past one sentence. For the perceptual color claim, [matplotlib.md](matplotlib.md) is the better citation.

**How this was read.** Both pages were fetched and converted locally from the seaborn v0.13.2 docs. Quotes are verbatim.

---

## The error-bar taxonomy

The `errorbar=` parameter is a 2x2: what the interval shows (spread or uncertainty) crossed with how it is built (parametric or nonparametric).

> "The error bars around an estimate of central tendency can show one of two general things: either the range of uncertainty about the estimate or the spread of the underlying data around it. These measures are related: given the same sample size, estimates will be more uncertain when data has a broader spread. But uncertainty will decrease as sample sizes grow, whereas spread will not."

| | Parametric | Nonparametric |
|---|---|---|
| Spread of data | `"sd"` (± k standard deviations) | `"pi"` (percentile interval, default 95%) |
| Uncertainty of estimate | `"se"` (± k standard errors) | `"ci"` (bootstrap CI, default 95%) |

The size parameter changes units with the method: "For parametric error bars, it is a scalar factor that is multiplied by the statistic defining the error... For nonparametric error bars, it is a percentile width." So `("se", 2)` means two standard errors, and `("pi", 50)` means the interquartile range. Generated code gets this wrong.

An unlabeled interval could be any of the four, which backs inventory topic 49 (error-bar semantics must be stated). Before v0.12 the only options were a bootstrap CI or a standard deviation, via a `ci` parameter.

## Impossible intervals

> "The standard deviation error bars will always be symmetrical around the estimate. This can be a problem when the data are skewed, especially if there are natural bounds (e.g., if the data represent a quantity that can only be positive). In some cases, standard deviation error bars may extend to 'impossible' values. The nonparametric approach does not have this problem, because it can account for asymmetrical spread and will never extend beyond the range of the data."

Inventory topic 51. A check that drawn bounds stay inside the variable's domain catches it. Source review does not, since nothing in the call looks wrong.

## The "are error bars enough?" section


> "You should always ask yourself whether it's best to use a plot that displays only a summary statistic and error bar. In many cases, it isn't."

> "If you are interested in questions about summaries (such as whether the mean value differs between groups or increases over time), aggregation reduces the complexity of the plot and makes those inferences easier. But in doing so, it obscures valuable information about the underlying data points, such as the shape of the distributions and the presence of outliers."

Inventory topic 50. The second quote describes a trade, distributional information for inferential clarity, so "always show the distribution" overclaims it.

- "Bootstrapping involves randomness, and the error bars will appear slightly different each time you run the code that creates them." `n_boot` and `seed` control it. Unseeded, a figure is not reproducible pixel-for-pixel even with fixed data and code (inventory topic 77).
- "seaborn functions cannot currently draw error bars from values that have been calculated externally." Agents routinely plot seaborn's recomputed interval instead of one fit elsewhere, which has to be drawn in matplotlib.

## Color palettes: hue for categories, luminance for numbers

**Hue distinguishes categories.**

> "So as a general rule, use hue variation to represent categories."

The cap is a comprehension cost, not a number:

> "If you have more than a handful of colors in your plot, it can become difficult to keep in mind what each one means, unless there are pre-existing associations between the categories and the colors used to represent them. This makes your plot harder to interpret: rather than focusing on the data, a viewer will have to continually refer to the legend to make sense of what is shown."

**Luminance represents numbers.**

> "On the other hand, hue variations are not well suited to representing numeric data."

A bivariate histogram drawn with a circular hue map and with a luminance ramp shows its two peaks only in the second, matplotlib's CIELAB argument made visually.

**Accessibility**, in one sentence:

> "Varying both shape (or some other attribute) and color can help people with anomalous color vision understand your plots, and it can keep them (somewhat) interpretable if they are printed to black-and-white."

Redundant coding (topic 69) and grayscale survival (topic 27), and all of seaborn's accessibility content. [chartability.md](chartability.md) covers accessibility.

## Defaults

- The default `deep` is a desaturated `tab10`, and the moderated hues "are also less distinct. As a result, they may be more difficult to discriminate in some contexts, which is something to keep in mind when making publication graphics."
- A `colorblind` variant ships alongside `muted`, `pastel`, `bright` and `dark`.
- Past the cycle's length, it uses evenly spaced hues in **HSLuv** rather than HLS, because equal RGB luminance is not equal perceived intensity.
- Its perceptually uniform sequential maps are chosen by mark type: `rocket` and `mako` for space-filling marks like heatmaps, `flare` and `crest` for lines and points. Rocket and mako approach white at one end, so on lines and points "it will be difficult to discriminate important values against a white or gray background."
- Discrete samples of a continuous map skip the extremes, so a discrete legend and a colorbar in one figure set can look mismatched.

## One uncited sentence

> "And aesthetics do matter: the more that people want to look at your figures, the greater the chance that they will learn something from them."

The emotive-quality claim (inventory topic 89), uncited. The nearest experimental record, the chartjunk literature in [refutations.md](../refutations.md), is contested in both directions.

## Where this source is used

Inventory topics 23, 24, 26, 28, 32, 49, 50, 51, 69, mapped in [roll-call.md](../roll-call.md).

## Links

- [Choosing color palettes](https://seaborn.pydata.org/tutorial/color_palettes.html)
- [Statistical estimation and error bars](https://seaborn.pydata.org/tutorial/error_bars.html)
- Related: [matplotlib.md](matplotlib.md), the perceptual argument in its stronger form
