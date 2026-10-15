---
type: source
status: primary-read
status_partial: true
retrieved: 2026-08-23
---

# Observable Plot scale documentation

The *Scales* chapter of Observable Plot, a JavaScript charting library built on D3 by Mike Bostock and collaborators, and the closest thing in JavaScript to a modern grammar-of-graphics default set.

**What it is good for.** A reasoned disagreement with two rules this wiki otherwise treats as settled, the rainbow ban and the zero baseline. For turbo, Plot names the cost.

**What it does not settle.** One chapter of one library. The marks, transforms and legends chapters were not read. Nothing on annotation, layout, accessibility or narrative.

**How this was read.** The scales page (`observablehq.com/plot/features/scales`) was fetched and converted locally. Quotes are verbatim from it.

---

## Turbo as the default continuous scheme

> "The default color scheme, turbo, was chosen primarily to ensure high-contrast visibility. Color schemes such as blues make low-value marks difficult to see against a white background, for better or for worse."

Elsewhere, unhedged: "The default quantitative color scale type is linear, and the default scheme is turbo."

The usual case against rainbows is perceptual ordering: not monotone in lightness, banding at the kinks, collapse in grayscale. [matplotlib.md](matplotlib.md) names turbo among maps that "would make it impossible for a viewer to interpret the information in a plot once it is printed in grayscale". Plot disputes none of that. It optimizes whether a low-value mark is visible against white, and "for better or for worse" concedes the trade. Its default radius is three pixels at the first quartile, and a sequential blues ramp puts such dots one step from invisible. The turbo default follows from the mark-size default.

[refutations.md](../refutations.md) therefore treats the rainbow ban as `contested` at the edges: rainbows fail on ordering and grayscale, and small-mark visibility is a stated reason to use one anyway. Habit is not.

## Zero is opt-in, which is the opposite of Vega-Lite

> "If you don't specify a quantitative scale's domain, it is the extent (minimum and maximum) of associated channel values, except for the r (radius) scale where it goes from zero to the maximum."

and, in the options list:

> "**zero** - if true, extend the domain to include zero if needed"

[Vega-Lite](vega-lite.md) defaults `zero` to true for quantitative x and y. Plot uses the data extent and makes zero a flag, available as a top-level shorthand across all scales. Its exceptions:

> "For the radius and opacity scales, the default domain is [0, max] to ensure a meaningful value encoding."

Plot forces zero on the radius and opacity channels and not on position, arguably a more defensible reading of Wilke's proportional-ink rule than Vega-Lite's blanket positional default.

> "for radius, the default range is designed to produce dots of 'reasonable' size assuming a sqrt scale type for accurate area representation: zero maps to zero, the first quartile maps to a radius of three pixels, and other values are extrapolated."

Square-root radius keeps area proportional to value, which is inventory topics 6 (channel effectiveness) and 9 (proportional ink) as a silent default.

## Other defaults with reasoning attached

- **Clamping comes with a warning**, unlike Vega-Lite's: "Clamping is useful for focusing on a subset of the data while ensuring that extreme values remain visible, but use caution: **clamped values may need an annotation to avoid misinterpretation.**" A better citation for inventory topic 56 than anything currently in the roll-call.
- **Diverging scales pivot at zero and default to `RdBu`.** "Diverging color scales are intended to show positive and negative values, or more generally values above or below some pivot value... The pivot defaults to zero, but you can change it with the pivot option, which should ideally be a value near the middle of the domain." Inventory topic 32. Red-blue rests on the cold/hot association, as in seaborn's `vlag`/`icefire`.
- **The categorical default is `observable10`,** a house palette: "The categorical scale type is also supported; it is equivalent to ordinal except as a color scale, where it provides a different default color scheme." Ordered categories get an ordered scheme and unordered ones distinct hues: inventory topic 23, enforced by the type name.
- **Rounding is on for band and point scales, off for quantitative:** "Use caution with high-cardinality ordinal domains... as rounding can lead to 'wasted' space or even zero-width bands."
- **Log scales cannot cross zero,** as in Vega-Lite, and the base "only affects the axis ticks and not the scale's behavior".
- **Type inference reads one value.** "Plot assumes that your data is consistently typed, so inference is based solely on the first non-null, non-undefined value." A string in row one silently makes a numeric column ordinal, which surfaces later as an unexplained band scale.

## Changing the channel instead of the palette

> "If you wish to encode a quantitative value without hue, consider using opacity rather than color (e.g., use Plot.dot's strokeOpacity instead of stroke)."

A rare library suggestion to switch channel rather than palette, under inventory topic 6.

## Where this source is used

Inventory topics 2, 9, 12, 31, 32, 39, and **25 as the counter-position**. [roll-call.md](../roll-call.md) records turbo as the dissent from the rainbow ban.

## Links

- [Observable Plot: Scales](https://observablehq.com/plot/features/scales)
- [Observable Plot](https://observablehq.com/plot/)
- Related: [vega-lite.md](vega-lite.md), [matplotlib.md](matplotlib.md)
