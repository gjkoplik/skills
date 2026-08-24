# matplotlib documentation

**What it is.** The official documentation for matplotlib, the default plotting library for Python. The pages that matter here are *Choosing Colormaps in Matplotlib*, plus the narrative guides for colorbar placement, axis scales, axis ticks, legends, and style sheets / rcParams.

**Status.** `primary-read`. Six pages were fetched and converted to text locally (matplotlib 3.11.1 docs, retrieved 2026-08-23): `colors/colormaps`, `axes/colorbar_placement`, `axes/axes_scales`, `axes/axes_ticks`, `axes/legend_guide`, and `customizing`. Every quote below is verbatim from those files.

**What it is good for.** The single best free source on **why one colormap is worse than another**, stated in perceptual terms rather than taste. Also the reference for what matplotlib does *by default* when you don't say, which is what an agent driving the API is actually up against.

**What it does not settle.** Almost nothing outside color. The scales, ticks, and legend guides are API reference, not advice: they show you how to set a log scale, not when. The colormaps page is prescriptive; the rest of matplotlib's narrative documentation is deliberately not. Do not cite matplotlib for anything about titles, annotation, uncertainty, chart-type choice, or narrative. It has no position on those.

---

## The colormaps page carries the load

Three claims from that page do most of the work in [inventory.md](../inventory.md) topics 23 to 27.

**Lightness beats hue for quantitative data.** This is the load-bearing sentence:

> "Researchers have found that the human brain perceives changes in the lightness parameter as changes in the data much better than, for example, changes in hue. Therefore, colormaps which have monotonically increasing lightness through the colormap will be better interpreted by the viewer."

It is a measured perceptual result, not a style preference, and it is why the perceptual-uniformity rule sits in a different evidence class from most of the color advice in this wiki. The page frames the whole analysis in CIELAB, using `L*` as the axis of comparison, and it ships the code that plots `L*` for every registered colormap. That is unusual: the argument is reproducible from the doc page itself.

**Four classes, matched to data type.** Verbatim:

> "Sequential: change in lightness and often saturation of color incrementally, often using a single hue; should be used for representing information that has ordering."
>
> "Diverging: change in lightness and possibly saturation of two different colors that meet in the middle at an unsaturated color; should be used when the information being plotted has a critical middle value, such as topography or when the data deviates around zero."
>
> "Cyclic: ... should be used for values that wrap around at the endpoints, such as phase angle, wind direction, or time of day."
>
> "Qualitative: often are miscellaneous colors; should be used to represent information which does not have ordering or relationships."

This is checkable in code, because matplotlib registers the category alongside the name. A sequential ramp on an unordered categorical column is a lookup failure, not a judgment call.

**Grayscale survival, argued rather than asserted.** The page devotes a section to what happens on a black-and-white printer, and names names:

> "Many of the Qualitative and Miscellaneous colormaps, such as Accent, hsv, jet and turbo, change from darker to lighter and back to darker grey throughout the colormap. This would make it impossible for a viewer to interpret the information in a plot once it is printed in grayscale."

And on color vision deficiency, one blunt line:

> "The most common form of color vision deficiency involves differentiating between red and green. Thus, avoiding colormaps with both red and green will avoid many problems in general."

## The turbo tension

matplotlib files `turbo` under **Miscellaneous**, notes it "was created to display depth and disparity data," and then names it in the grayscale section as one of the maps that make a printed plot uninterpretable. It also cites the Google AI blog post that introduced turbo.

Observable Plot ships turbo as its **default** continuous color scheme. That is not a small disagreement between two doc pages; it is two projects reading the same evidence and shipping opposite defaults. See [observable-plot.md](observable-plot.md) for Plot's stated reasoning, and [refutations.md](../refutations.md), which treats the rainbow ban as contested at the edges partly because of it.

Worth noting that matplotlib's objection to turbo is narrower than the usual rainbow objection. It is not "turbo bands" or "turbo reverses"; the specific charge is that its lightness goes dark-light-dark, so grayscale collapses it. Plot's counter-argument is about visibility against white, which is a different axis entirely. Both can be right.

## Defaults matplotlib ships, and what they encode

The customizing page lists the bundled style sheets. As of 3.11:

```
['Solarize_Light2', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight',
 'ggplot', 'grayscale', 'petroff10', 'petroff6', 'petroff8', 'seaborn-v0_8', ...,
 'tableau-colorblind10']
```

Two of those entries are quiet accessibility positions. `tableau-colorblind10` and the three `petroff*` cycles exist so that "use a colorblind-safe cycle" is a one-line change rather than a research project. The qualitative colormap list now also includes `okabe_ito`, the standard colorblind-safe eight-color set. matplotlib does not editorialize about any of this in prose; it just makes the accessible option reachable by name.

The Diverging section adds `berlin`, `managua`, and `vanimo`, described as "dark-mode diverging colormaps, with minimum lightness at the center, and maximum at the extremes," taken from Crameri's scientific colour maps v8.0.1. That is a shipped answer to "what background does this figure assume", which most guides never address.

There is also a small **Discouraged** table, retiring `gist_gray`, `gist_yarg`, and `binary` in favor of `gray` / `gray_r`. Cheap to mechanize as a denylist.

## Style sheets: config beats prose, in the library itself

The customizing page states the precedence plainly: runtime `rcParams` beat style sheets, style sheets beat `matplotlibrc`. It then goes further than most libraries and documents **distributing** a style inside a Python package, so `plt.style.use("mypackage.presentation")` works after a `pip install`.

This is the same move the newsroom style guides make, arrived at independently. The BBC wrote `bbplot` because a written guide did not survive being retyped; the Urban Institute ships `urbnthemes`; matplotlib ships a packaging mechanism for exactly that. See [bbc-cookbook.md](bbc-cookbook.md) and [urban-institute.md](urban-institute.md). Inventory topic 79 ("house style lives in a theme or rcParams, not per-figure kwargs") is one of the few topics where every source in this wiki agrees, and all three arrived by the same route: prose did not hold.

## Colorbars, scales, ticks, legends

These four pages are worth reading once so you know what exists, and are not worth citing as authority.

- **Colorbars.** The useful practical content is that colorbars steal space from the parent Axes, that this desynchronizes panel widths in a shared-x layout, and that `layout='constrained'` is the fix. A `fig.colorbar(pcm, ax=axs[:, col])` call attaches one colorbar to a column of panels, which is the mechanism for *not* silently rescaling color between panels. The page does not tell you to label the colorbar or to pin `vmin`/`vmax`; that judgment is elsewhere.
- **Axis scales.** Enumerates the registered scales: `asinh`, `function`, `functionlog`, `linear`, `log`, `logit`, `symlog`. No guidance on when a log axis is appropriate or how to label it as log. For that, see the log-scale entry in [refutations.md](../refutations.md), which is the only place in this wiki with evidence attached.
- **Axis ticks.** Locators and formatters. The one durable idea is that hand-set ticks "work well for specific final plots, but do not adapt as the user interacts with the Axes", which is the argument for a formatter over a literal label list in anything interactive.
- **Legends.** Entirely mechanical. Note one trap that bites generated code: "Artists with an empty string as label or with a label starting with an underscore, `_`, will be ignored." A silently missing legend entry usually traces to that rule, not to a bug.

## Where this source is used

Inventory topics 23, 24, 25, 26, 27, 28, 32, 34, 79, 81. See [roll-call.md](../roll-call.md) for the section-by-section mapping, which this reading confirms is accurate.

The runnable versions of the color rules, including a dependency-free CVD simulation and a WCAG contrast function, are in [checks/matplotlib.md](../checks/matplotlib.md).

## Links

- [Choosing Colormaps in Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html)
- [Placing colorbars](https://matplotlib.org/stable/users/explain/axes/colorbar_placement.html)
- [Axis scales](https://matplotlib.org/stable/users/explain/axes/axes_scales.html)
- [Axis ticks](https://matplotlib.org/stable/users/explain/axes/axes_ticks.html)
- [Legend guide](https://matplotlib.org/stable/users/explain/axes/legend_guide.html)
- [Customizing Matplotlib with style sheets and rcParams](https://matplotlib.org/stable/users/explain/customizing.html)
- Related: [seaborn.md](seaborn.md), [observable-plot.md](observable-plot.md), [vega-lite.md](vega-lite.md)
