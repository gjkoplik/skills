---
type: source
status: primary-read
retrieved: 2026-08-23
---

# matplotlib documentation

The official documentation for matplotlib, Python's default plotting library.

**What it is good for.** The best free source on why one colormap is worse than another, argued in perceptual terms, and the reference for matplotlib's defaults.

**What it does not settle.** Almost anything outside color. The scales, ticks and legend guides say how to set a log scale, not when. Nothing on titles, annotation, uncertainty, chart-type choice or narrative.

**How this was read.** Six pages of the matplotlib 3.11.1 docs were fetched and converted to text locally: `colors/colormaps`, `axes/colorbar_placement`, `axes/axes_scales`, `axes/axes_ticks`, `axes/legend_guide`, and `customizing`. Quotes are verbatim from those files.

---

## The colormaps page

This page carries [inventory.md](../inventory.md) topics 23 to 27.

**Lightness beats hue for quantitative data.**

> "Researchers have found that the human brain perceives changes in the lightness parameter as changes in the data much better than, for example, changes in hue. Therefore, colormaps which have monotonically increasing lightness through the colormap will be better interpreted by the viewer."

A measured perceptual result, not a style preference, so the perceptual-uniformity rule sits in a different evidence class from most color advice here. The page compares maps on CIELAB `L*` and ships the code that plots it for every registered colormap.

**Four classes, matched to data type.**

> "Sequential: change in lightness and often saturation of color incrementally, often using a single hue; should be used for representing information that has ordering."
>
> "Diverging: change in lightness and possibly saturation of two different colors that meet in the middle at an unsaturated color; should be used when the information being plotted has a critical middle value, such as topography or when the data deviates around zero."
>
> "Cyclic: ... should be used for values that wrap around at the endpoints, such as phase angle, wind direction, or time of day."
>
> "Qualitative: often are miscellaneous colors; should be used to represent information which does not have ordering or relationships."

Each map's class is registered with its name, so a sequential ramp on an unordered column is a lookup failure code can catch.

**Grayscale survival.**

> "Many of the Qualitative and Miscellaneous colormaps, such as Accent, hsv, jet and turbo, change from darker to lighter and back to darker grey throughout the colormap. This would make it impossible for a viewer to interpret the information in a plot once it is printed in grayscale."

**Color vision deficiency.**

> "The most common form of color vision deficiency involves differentiating between red and green. Thus, avoiding colormaps with both red and green will avoid many problems in general."

## The turbo tension

matplotlib files `turbo` under Miscellaneous, notes it "was created to display depth and disparity data," cites the Google AI blog post that introduced it, and lists it among the maps that fail in grayscale. Observable Plot ships turbo as its default continuous scheme ([observable-plot.md](observable-plot.md)), which is partly why [refutations.md](../refutations.md) treats the rainbow ban as contested at the edges. matplotlib's charge is narrow: turbo's lightness goes dark-light-dark, so grayscale collapses it. Plot argues visibility against white, a different axis. Both can hold.

## Defaults matplotlib ships, and what they encode

The bundled style sheets, as of 3.11:

```
['Solarize_Light2', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight',
 'ggplot', 'grayscale', 'petroff10', 'petroff6', 'petroff8', 'seaborn-v0_8', ...,
 'tableau-colorblind10']
```

`tableau-colorblind10` and the three `petroff*` cycles make a colorblind-safe cycle a one-line change, and the qualitative colormaps include `okabe_ito`, the standard colorblind-safe eight-color set. The diverging `berlin`, `managua` and `vanimo` are "dark-mode diverging colormaps, with minimum lightness at the center, and maximum at the extremes," from Crameri's "Scientific colour maps" v8.0.1, a shipped answer to "what background does this figure assume". A **Discouraged** table retires `gist_gray`, `gist_yarg` and `binary` for `gray` / `gray_r`, enforceable as a denylist.

## Style sheets: config beats prose

Runtime `rcParams` beat style sheets, which beat `matplotlibrc`. A style can be distributed in a Python package, so `plt.style.use("mypackage.presentation")` works after a `pip install`. The BBC wrote `bbplot` because a written guide did not survive retyping, and the Urban Institute ships `urbnthemes` ([bbc-cookbook.md](bbc-cookbook.md), [urban-institute.md](urban-institute.md)). No source here disputes inventory topic 79 ("house style lives in a theme or rcParams, not per-figure kwargs"), and all three reached it because prose did not hold.

## Colorbars, scales, ticks, legends

API inventory, not authority.

- **Colorbars.** A colorbar steals space from its parent Axes, desynchronizing panel widths in a shared-x layout, which `layout='constrained'` fixes. `fig.colorbar(pcm, ax=axs[:, col])` gives a column of panels one colorbar, so color does not silently rescale between them. Nothing on labeling it or pinning `vmin`/`vmax`.
- **Axis scales.** `asinh`, `function`, `functionlog`, `linear`, `log`, `logit`, `symlog`, with no guidance on when log fits or how to label it. The evidence is in the log-scale entry of [refutations.md](../refutations.md).
- **Axis ticks.** Hand-set ticks "work well for specific final plots, but do not adapt as the user interacts with the Axes", an argument for formatters over literal label lists in interactive figures.
- **Legends.** "Artists with an empty string as label or with a label starting with an underscore, `_`, will be ignored." A legend entry missing from generated code usually traces to that rule.

## Where this source is used

Inventory topics 23, 24, 25, 26, 27, 28, 32, 34, 79, 81, mapped in [roll-call.md](../roll-call.md). Runnable color checks, including a dependency-free CVD simulation and a WCAG contrast function, are in [checks/matplotlib.md](../checks/matplotlib.md).

## Links

- [Choosing Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html)
- [Placing colorbars](https://matplotlib.org/stable/users/explain/axes/colorbar_placement.html)
- [Axis scales](https://matplotlib.org/stable/users/explain/axes/axes_scales.html)
- [Axis ticks](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html)
- [Legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html)
- [Customizing Matplotlib with style sheets and rcParams](https://matplotlib.org/stable/users/explain/customizing.html)
- Related: [seaborn.md](seaborn.md), [observable-plot.md](observable-plot.md), [vega-lite.md](vega-lite.md)
