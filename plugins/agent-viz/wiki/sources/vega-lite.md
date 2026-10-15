---
type: source
status: primary-read
author: jeffrey-heer
retrieved: 2026-08-23
---

# Vega-Lite scale documentation

The scale reference for Vega-Lite, a declarative grammar of interactive graphics. It is a parameter table, and the most explicit statement anywhere of a design position shipped as a default.

**What it is good for.** What a chart grammar decides when the spec says nothing. A declarative grammar has to write its defaults down.

**What it does not settle.** The rest of a large specification: the encoding-channel opinion set, mark set and config system, a sampling gap [roll-call.md](../roll-call.md) also flags. Nothing on color beyond scheme names, annotation, accessibility or narrative.

**How this was read.** The scale docs page was fetched and converted locally. Quotes are verbatim from it.

**Authorship.** The `author` field names Jeffrey Heer, a coauthor of the Vega-Lite paper (Satyanarayan, Moritz, Wongsuphasawat & Heer, 2017). The documentation page itself is unsigned. The field is recorded because the wiki's claims of independence between sources depend on it; [../people/jeffrey-heer.md](../people/jeffrey-heer.md) says what the overlap does and does not reach.

---

## The `zero: true` default

On the scale property:

> "**zero**: If true, ensures that a zero baseline value is included in the scale domain.
>
> Default value: true for x and y channels if the quantitative field is not binned and no custom domain is provided; false otherwise.
>
> Note: Log, time, and utc scales do not support zero."

In the project-wide scale **config**:

> "**zero**: Default `scale.zero` for continuous scales except for (1) x/y-scales of non-ranged bar or area charts and (2) size scales.
>
> Default value: true"

So Vega-Lite includes zero in a quantitative positional domain **by default, for every mark type**. No style guide in this wiki commits that far: Wilke's proportional-ink rule and the Urban Institute's absolutes bind on bars and areas only, and [urban-institute.md](urban-institute.md) says scatterplots and line charts "do not necessarily need to start at zero".

The carve-outs:

- **Binned fields are exempt.** A histogram of ages does not stretch to zero for a bin at 40.
- **A custom domain wins**, silently.
- **Log, time and utc do not support it.** `log(0)` is undefined, and a zero baseline on a time axis is meaningless. Inventory topic 12, enforced by the type system.

The config exception for "non-ranged bar or area charts" exists because the mark-level default already forces zero for those marks.

## What Vega-Lite decides when the spec says nothing else

The scale-type table is "data abstraction determines encoding" (inventory topics 2 and 7) as a lookup:

| | Nominal / Ordinal | Quantitative | Bin-Quantitative | Temporal |
|---|---|---|---|---|
| X, Y | Band / Point | Linear | Linear | Time |
| Size, Opacity | Point | Linear | Linear | Time |
| Color | Ordinal | Linear | Bin-Ordinal | Linear |
| Shape | Ordinal | N/A | N/A | N/A |

**Shape is N/A for quantitative and binned data**: the grammar will not encode a number as a shape. For positional nominal fields, "'band' scale is the default scale type for bar, image, rect, and rule marks while 'point' is the default scales for all other marks", so the mark picks the scale.

Default color schemes are typed too:

> "Nominal fields use the 'categorical' pre-defined named range (the 'tableau10' scheme by default).
>
> Ordinal fields use the 'ordinal' pre-defined named color range (the 'blues' color scheme by default).
>
> Quantitative and temporal fields use the pre-defined named color range 'heatmap' (the 'viridis' scheme by default) for rect marks and 'ramp' (the 'blues' scheme by default) for other marks."

Seaborn reaches the same split independently with `rocket`/`mako` versus `flare`/`crest` ([seaborn.md](seaborn.md)). [Observable Plot](observable-plot.md) makes the opposite bet for its continuous default, the high-contrast turbo.

## Smaller defaults

- **`nice`** extends a computed domain "so that it starts and ends on nice round values... for a domain of [0.201479…, 0.996679…], a nice domain might be [0.2, 1.0]." The axis range then never exactly matches the data range, which bears on any truncation-ratio check.
- **`clamp`** pins out-of-domain values to the domain edge with nothing marking them as clipped (inventory topic 56). Observable Plot warns about this; Vega-Lite does not.
- **`round`** defaults to `false`.
- **`reverse`** defaults to `false`, with a separate `xReverse` config "useful for right-to-left charts", so an inverted axis is opt-in and named (inventory topic 11).
- **`useUnaggregatedDomain`** defaults to `false`, works only for aggregations inside the raw data range (`mean`, `median`, `q1`, `q3`, `min`, `max`), and is "ignored" for `count` and `sum`.
- **Invalid data** gets a scale-level policy: `"zero-or-min"` or an explicit value, described as covering "nulls and NaNs on a continuous scale". The closest any source here comes to inventory topic 55 (missing data shown as missing). It requires naming what a null renders as, not disclosing it.

## Defaults versus evidence

Zero baselines, scale-type matching, no shapes for numbers, opt-in inverted axes and a null policy are defaulted or enforced here, so quantitative-honesty rules are not inherently judgment calls. In matplotlib each is the caller's problem.

Defaults are not evidence. `zero: true` is a design position held by its authors, and the inventory classes proportional ink as authority-asserted with tooling corroboration. In the axis-break entry of [refutations.md](../refutations.md), the authors of the best truncation study refuse the maximalist reading: "we resist the interpretation... that all charts with quantitative axes should include 0." Vega-Lite ships a stricter rule than the paper most often cited for it will endorse.

## Where this source is used

Inventory topics 2, 7, 9, 12, 56. [roll-call.md](../roll-call.md) notes that Vega-Lite was sampled through the scale page only.

## Links

- [Vega-Lite: Scale](https://vega.github.io/vega-lite/docs/scale.html)
- [Vega-Lite documentation home](https://vega.github.io/vega-lite/)
- Related: [observable-plot.md](observable-plot.md): the same questions answered differently
