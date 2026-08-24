# Vega-Lite scale documentation

**What it is.** The scale reference for Vega-Lite, a declarative grammar of interactive graphics. It is a parameter table, and it is also the most explicit statement anywhere of a design position shipped as a default.

**Status.** `primary-read`. The scale docs page was fetched and converted locally, retrieved 2026-08-23. Quotes below are verbatim from that page.

**What it is good for.** Reading what a chart grammar decides *for* you when you don't say. Vega-Lite is unusually honest about this, because a declarative grammar has to write its defaults down or nobody can predict what a spec renders.

**What it does not settle.** This is one page of a large specification. Vega-Lite has an encoding-channel opinion set, a mark set, and a config system that are not covered here at all; [roll-call.md](../roll-call.md) flags the same sampling gap. Nothing on color choice beyond default scheme names, nothing on annotation, accessibility, or narrative.

---

## `zero: true` is the interesting part

The zero-baseline debate is usually conducted as advice. Vega-Lite conducts it as code, and the default is spelled out twice.

On the scale property:

> "**zero**: If true, ensures that a zero baseline value is included in the scale domain.
>
> Default value: true for x and y channels if the quantitative field is not binned and no custom domain is provided; false otherwise.
>
> Note: Log, time, and utc scales do not support zero."

And in the scale **config**, the project-wide setting:

> "**zero**: Default `scale.zero` for continuous scales except for (1) x/y-scales of non-ranged bar or area charts and (2) size scales.
>
> Default value: true"

Read those together and the position is precise. Vega-Lite includes zero in a quantitative positional domain **by default, for every mark type**, not just for bars. That is a stronger commitment than any of the style guides in this wiki make. Wilke's proportional-ink rule and the Urban Institute's absolutes both bind on bars and areas only, and both explicitly release line and dot plots (see [urban-institute.md](urban-institute.md), which says scatterplots and line charts "do not necessarily need to start at zero").

The three carve-outs are also informative about how the position was reasoned:

- **Binned fields are exempt.** A histogram of ages should not stretch to zero to accommodate a bin at 40.
- **A custom domain wins.** Saying `domain` is treated as saying you meant it, so `zero` steps aside rather than fighting you. No warning, no conflict.
- **Log, time, and utc do not support it at all.** Not "ignored", not "defaults to false": unsupported. `log(0)` is undefined, and a zero baseline on a time axis is meaningless. This is inventory topic 12 enforced by the type system instead of by a rule.

The config exception for "non-ranged bar or area charts" reads backwards on first pass. It means the mark-level default already forces zero for those marks, so the config knob does not need to.

## What Vega-Lite decides when you say nothing else

The scale-type table is the compact version of "data abstraction determines encoding" (inventory topics 2 and 7), shipped as a lookup:

| | Nominal / Ordinal | Quantitative | Bin-Quantitative | Temporal |
|---|---|---|---|---|
| X, Y | Band / Point | Linear | Linear | Time |
| Size, Opacity | Point | Linear | Linear | Time |
| Color | Ordinal | Linear | Bin-Ordinal | Linear |
| Shape | Ordinal | N/A | N/A | N/A |

Two details in that table are arguments, not conveniences. **Shape is N/A for quantitative and binned data**, so the grammar simply will not let you encode a number as a shape. And for positional nominal fields, "'band' scale is the default scale type for bar, image, rect, and rule marks while 'point' is the default scales for all other marks", which is the mark deciding the scale rather than the field.

Default color schemes are similarly typed:

> "Nominal fields use the 'categorical' pre-defined named range (the 'tableau10' scheme by default).
>
> Ordinal fields use the 'ordinal' pre-defined named color range (the 'blues' color scheme by default).
>
> Quantitative and temporal fields use the pre-defined named color range 'heatmap' (the 'viridis' scheme by default) for rect marks and 'ramp' (the 'blues' scheme by default) for other marks."

`viridis` for filled rect marks, `blues` for everything else. That is the same mark-type reasoning seaborn gives for `rocket`/`mako` versus `flare`/`crest` (see [seaborn.md](seaborn.md)), reached independently. And it is the opposite bet from Observable Plot, which uses one high-contrast scheme everywhere; see [observable-plot.md](observable-plot.md).

## Smaller defaults with opinions inside

- **`nice`** extends a computed domain "so that it starts and ends on nice round values... for a domain of [0.201479…, 0.996679…], a nice domain might be [0.2, 1.0]." Rounding the axis, not the data. Harmless, and it means an axis range never exactly matches the data range, which any truncation-ratio check needs to know.
- **`clamp`** pins out-of-domain values to the domain edge. This is the one place the scale docs touch inventory topic 56 (clipped outliers). Clamping is silent: the point is drawn at the boundary and nothing marks it as clipped. Compare Observable Plot, which does warn about exactly this, and note that the Vega-Lite page does not.
- **`round`** defaults to `false` for output values, snapping to the pixel grid only when asked.
- **`reverse`** defaults to `false`, and there is a separate `xReverse` config "useful for right-to-left charts". An inverted axis is opt-in and named, which is the right shape for inventory topic 11.
- **`useUnaggregatedDomain`** defaults to `false` and only works for aggregations that stay inside the raw data range (`mean`, `median`, `q1`, `q3`, `min`, `max`), and is "ignored" for `count` and `sum`. A guard against a scale that pretends to show raw spread while displaying sums.
- **Invalid data** gets a scale-level policy: `"zero-or-min"` or an explicit value, described as covering "nulls and NaNs on a continuous scale". This is the closest any source in this wiki comes to inventory topic 55 (missing data shown as missing), and it is a mechanism, not advice. Vega-Lite makes you name what a null renders as; it does not tell you to disclose it.

## Why this page matters to a figure bar

Vega-Lite is the counterexample to the claim that quantitative-honesty rules are inherently judgment calls. Zero baselines, scale-type-to-data-type matching, no-shapes-for-numbers, inverted axes as opt-in, and a null policy are all here as enforced or defaulted behavior. In matplotlib every one of them is the caller's problem.

That is worth saying carefully, though. Defaults are not evidence. Vega-Lite's `zero: true` is a **design position held by its authors**, and the inventory correctly classes the proportional-ink topic as authority-asserted with tooling corroboration rather than as evidence-backed. The experimental record on truncation is messier than the default implies; see the axis-break entry in [refutations.md](../refutations.md), where the authors of the best truncation study explicitly refuse the maximalist reading: "we resist the interpretation... that all charts with quantitative axes should include 0."

So: Vega-Lite ships the stricter rule, and the paper most often cited for the rule declines to endorse it that strongly. Both facts belong in any bar that repeats the rule.

## Where this source is used

Inventory topics 2, 7, 9, 12, 56. See [roll-call.md](../roll-call.md), including its standing caveat that Vega-Lite was sampled through the scale page only.

## Links

- [Vega-Lite: Scale](https://vega.github.io/vega-lite/docs/scale.html)
- [Vega-Lite documentation home](https://vega.github.io/vega-lite/)
- Related: [observable-plot.md](observable-plot.md) for the same questions answered differently
