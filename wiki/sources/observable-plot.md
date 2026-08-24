# Observable Plot scale documentation

**What it is.** The *Scales* chapter of Observable Plot, a JavaScript charting library built on D3 by Mike Bostock and collaborators. Plot is the closest thing in the JavaScript world to a modern grammar-of-graphics default set.

**Status.** `primary-read`. The scales page (`observablehq.com/plot/features/scales`) was fetched and converted locally, retrieved 2026-08-23. Quotes are verbatim from that page.

**What it is good for.** Reading a **considered disagreement** with two rules this wiki otherwise treats as settled: the rainbow ban, and the zero baseline. Plot is not sloppy about either. It states its reasoning, and in the turbo case it says out loud that the choice has a cost.

**What it does not settle.** One chapter of one library. Plot's marks, transforms, and legends chapters were not read. Nothing here on annotation, layout, accessibility, or narrative.

---

## Turbo as the default continuous scheme

This is the sentence that makes the page worth a wiki entry:

> "The default color scheme, turbo, was chosen primarily to ensure high-contrast visibility. Color schemes such as blues make low-value marks difficult to see against a white background, for better or for worse."

Restated earlier in the chapter without hedging: "The default quantitative color scale type is linear, and the default scheme is turbo."

Three things to take from it.

**The reasoning is orthogonal to the usual objection.** The standard anti-rainbow case is about perceptual ordering: a rainbow ramp is not monotone in lightness, so equal data steps do not look equal, it bands at the kinks, and it collapses in grayscale. matplotlib makes exactly that case and names turbo among the maps that "would make it impossible for a viewer to interpret the information in a plot once it is printed in grayscale" (see [matplotlib.md](matplotlib.md)). Plot does not dispute any of it. It optimizes a different quantity: **whether a low-value mark is visible at all** against white. On a scatterplot of small dots, a sequential blues ramp puts your smallest values one step from invisible.

**"For better or for worse" is the authors conceding the trade.** That clause is doing real work. It is not a claim that turbo is perceptually superior; it is a claim that visibility is the binding constraint for Plot's typical output, which is small marks on a white page in a notebook.

**Plot's default marks are small.** The radius default (below) is three pixels at the first quartile. A three-pixel dot in light blue on white is a defect. Read that way, the turbo default is downstream of the mark-size default, not an independent color opinion.

This is why [refutations.md](../refutations.md) treats the rainbow ban as **contested at the edges**. The right phrasing for a quality bar is not "never rainbow" but something closer to: rainbow schemes fail on perceptual ordering and on grayscale, and if you pick one anyway, say what you bought with it. Small-mark visibility is a real reason. Habit is not.

## Zero is opt-in, which is the opposite of Vega-Lite

> "If you don't specify a quantitative scale's domain, it is the extent (minimum and maximum) of associated channel values, except for the r (radius) scale where it goes from zero to the maximum."

and, in the options list:

> "**zero** - if true, extend the domain to include zero if needed"

Two grammars of graphics, built by overlapping communities, ship opposite defaults on the single most-repeated rule in visualization. Vega-Lite defaults `zero` to true for quantitative x and y; Plot defaults to the data extent and makes zero a flag. See [vega-lite.md](vega-lite.md).

Neither is careless, and the difference is not really about honesty. Plot's exceptions show where it *does* enforce proportionality:

> "For the radius and opacity scales, the default domain is [0, max] to ensure a meaningful value encoding."

So Plot forces zero exactly where **area encodes the value** and lets it go where position does. That is proportional ink applied narrowly and correctly, and it is arguably the more defensible reading of Wilke's rule than Vega-Lite's blanket application to all positional quantitative scales. Plot also supports `zero` as a top-level shorthand across all scales, so the strict behavior is one word away.

The radius range is worked out to the same standard:

> "for radius, the default range is designed to produce dots of 'reasonable' size assuming a sqrt scale type for accurate area representation: zero maps to zero, the first quartile maps to a radius of three pixels, and other values are extrapolated."

Square-root scaling for radius, so area is proportional to value. This is inventory topic 6 (channel effectiveness) and topic 9 (proportional ink) shipped as a default nobody has to know about.

## Other defaults with reasoning attached

- **Clamping comes with a warning**, which Vega-Lite's does not: "Clamping is useful for focusing on a subset of the data while ensuring that extreme values remain visible, but use caution: **clamped values may need an annotation to avoid misinterpretation.**" That is inventory topic 56 stated properly by a library, in one line, and it is the better citation for that topic than anything currently in the roll-call.
- **Diverging scales pivot at zero and default to `RdBu`.** "Diverging color scales are intended to show positive and negative values, or more generally values above or below some pivot value... The pivot defaults to zero, but you can change it with the pivot option, which should ideally be a value near the middle of the domain." Note that Plot makes the midpoint explicit and typed, which is inventory topic 32. Note also that red-blue is the semantic default here and in seaborn's `vlag`/`icefire`, on the cold/hot association.
- **Categorical default is `observable10`,** a house palette, distinct from `ordinal`. The type distinction matters: "The categorical scale type is also supported; it is equivalent to ordinal except as a color scale, where it provides a different default color scheme." Ordered categories get an ordered scheme; unordered ones get distinct hues. Inventory topic 23, enforced by the type name.
- **Rounding is on for band and point scales, off for quantitative,** with a stated failure mode: "Use caution with high-cardinality ordinal domains... as rounding can lead to 'wasted' space or even zero-width bands."
- **Log scales cannot cross zero,** same as Vega-Lite, and the base "only affects the axis ticks and not the scale's behavior".
- **Type inference reads one value.** "Plot assumes that your data is consistently typed, so inference is based solely on the first non-null, non-undefined value." A numeric column with a string in row one silently becomes ordinal. Worth knowing before debugging a mysterious band scale.

## An aside worth keeping

> "If you wish to encode a quantitative value without hue, consider using opacity rather than color (e.g., use Plot.dot's strokeOpacity instead of stroke)."

A rare piece of library documentation that suggests changing the *channel* rather than tuning the palette. Fits inventory topic 6 better than most of the color-focused advice does.

## Where this source is used

Inventory topics 2, 9, 12, 31, 32, 39, and **25 as the counter-position**. See [roll-call.md](../roll-call.md), which already records turbo as the dissent rather than folding it into the rainbow ban, and [refutations.md](../refutations.md) for the resulting scope limit on that rule.

## Links

- [Observable Plot: Scales](https://observablehq.com/plot/features/scales)
- [Observable Plot](https://observablehq.com/plot/)
- Related: [vega-lite.md](vega-lite.md), [matplotlib.md](matplotlib.md)
