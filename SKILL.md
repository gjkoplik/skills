---
name: agent-viz
description: A quality bar for any chart, plot, or figure a person will look at. Splits into a floor that binds on every figure (quantitative honesty, statistical honesty, accessibility) and a ceiling that scales with the figure's job (narrative titles, emphasis palette, annotation), so a deliberately minimal figure is judged correct rather than unfinished. Carries runnable checks, not just principles, and tells you to translate the field's jargon into plain language rather than talking past someone who is not a visualization expert. Load before writing the first line of plotting code, and before reviewing someone else's figure: a research plot, a performance comparison, a diagnostic, a dashboard panel, a docs example, or anything headed for a blog post or a paper.
---

# agent-viz: a quality bar for figures

Read this **before** the first line of plotting code, not after the figure exists. Most of what follows is cheaper to satisfy while drawing than to retrofit.

**The rules here are ecosystem-neutral.** They are about what a figure claims, not about which library drew it. Where a check is spelled out concretely it is written against matplotlib, because that is where it was built and tested, and matplotlib is the **reference implementation rather than the intended scope**. The equivalent in ggplot2, Vega-Lite, plotly or D3 is usually a different call against the same idea. If a rule below reads as Python-specific, that is a defect in the phrasing, not a limit on the rule.

## Talk to the person like they are not a visualization expert, because they almost certainly are not

This matters more than any single rule below. Almost nobody is in the weeds on visualization. Everybody makes figures anyway, and they should still get the benefit of this.

**Never use a term of art without translating it, the first time, every conversation.** The rules below are written in the field's shorthand because that is how the sources write it. That shorthand is for you, not for the person you are helping. Some of it is genuinely obscure even to people who know the underlying ideas well.

Translate at least these:

- **CVD** is color vision deficiency, which most people call colorblindness. The common form makes red and green hard to tell apart. Say that, do not say "CVD".
- **WCAG** is the web accessibility standard. Say "the accessibility standard for contrast" and give the number.
- **SD, SE, 95% CI** are three different things an error bar can mean, and most people including researchers mix them up. If you need the distinction, explain it in one sentence rather than assuming it.
- **Perceptually uniform** means equal steps in the data look like equal steps to the eye. **Sequential, diverging, qualitative** describe what kind of thing a color scale is for. **Data-ink** is Tufte's term for the pixels actually carrying information.
- **Small multiples** means several small charts side by side instead of one crowded one.

**Say what is wrong and what to do about it, in their words.** "Your bar chart's y-axis starts at 95 instead of 0, which makes a small difference look like a big one" beats "proportional ink violation." Lead with the consequence to the reader of their figure.

**Do not cite this skill or its wiki at them** unless they ask why. They want a better figure, not a reading list.

**One thing worth being direct about:** if a figure is misleading, say so plainly and early. Softening that is not kindness, because they are about to show it to someone.

## Decide what kind of figure this is, first

**If it is not obvious, ask. One question, in plain language, before you start drawing.**

Something like: *"Is this figure making a point to a reader, or showing how the code works?"* Or, if the context suggests it: *"Is this for you to look at once, or is someone else going to see it?"*

That one answer decides which half of this skill applies, and getting it wrong in either direction is expensive. Treat a throwaway diagnostic like a paper figure and you waste their time on polish they did not want. Treat a figure headed for a blog post like a scratch plot and you ship something that undersells their work.

**Do not interrogate them.** One question, then get on with it. If the context already answers it, do not ask at all: a figure in a docs notebook demonstrating a parameter is instructional, and a figure captioned with a finding is storytelling.



The rules below are not one undifferentiated list, and applying them uniformly produces bad review.

**The floor binds on every figure regardless of role.** Quantitative honesty, statistical honesty, accessibility. Break one and the figure is *wrong*, or is unreadable to some of the people looking at it. A teaching figure that misleads teaches the wrong thing, and a reader with a color-vision deficiency is a real reader.

**The ceiling scales with the figure's job.** Narrative titles, emphasis palettes, direct labeling, alignment craft, annotation. This is how a figure *argues*. A figure whose job is to show how three lines of API work does not need to argue, and spending polish there costs the reader the thing they came for.

So:

- **A storytelling figure** (a finding, a blog post, a paper figure, a README hero) owes the floor and the ceiling.
- **An instructional figure** (a demo of what a parameter does, where the *code* is as much the artifact as the picture) owes the floor, and its real quality bar is minimal, clean, copy-able source. A plain literal title, default colors, and no custom legend are **correct** there, not unfinished. Do not review such a figure as a defect list.
- **A diagnostic figure** you will look at once owes the floor only, and barely that: it needs to not mislead *you*.

The one place minimalism does not win: **minimal code buys API comprehension, never a misleading axis.** A truncated baseline or an undisclosed error bar is worse in a two-cell demo than in a paper, because the reader is there to learn the idiom and will copy it.

## Floor: quantitative honesty

- **Zero baseline when area encodes the value.** Bars, area fills, filled regions and bubbles start at zero on a linear scale. Line and dot plots, which encode by position, do not have to. On a log scale bars start at 1.
- **Truncation inflates perceived effect, and axis-break glyphs do not undo it.** The exaggeration persists across chart types and even when readers correctly read the numbers off the axis, and the tested break-glyph remedies did not measurably reduce it. Choose the range to match the effect you mean to communicate, and say what the range is.
- **Never invert an axis silently.** Inversion reverses the conclusion rather than exaggerating it, and readers do not notice. One attribute read catches it.
- **Label a log axis as log**, in untransformed units with visible decade ticks. Do not assume an expert audience rescues it; domain experts misread log-log badly compared to linear-linear.
- **Two y-axes is a judgment call, not a banned construct.** No experiment establishes a flat ban. But the correlation a reader sees is a free parameter of your scaling choice, so prefer two stacked panels sharing an x-axis, and if you keep the twin axis, say what each scale was pinned to.
- **Choose the aspect ratio deliberately.** It decides which slope differences are readable. There is no defensible automatic rule; "bank to 45 degrees" is not the error-minimizing ratio in general. Accepting the library default silently is itself a choice, and a real caveat on any claim about steepness.
- **Every quantitative axis carries a title with units.** Prefer `quantity / unit` (`Time / s`) so tick numbers stay pure numbers.
- **Never let a raw float reach a label.** `f"threshold {0.1 + 0.2}"` renders `0.30000000000000004`. Format explicitly, to the significant digits the measurement supports: a median of five timings supports two significant figures, not five.
- **A colorbar needs explicit limits, a label with units, and `extend` whenever real data falls outside those limits.** Without it, the plotting library clips silently (matplotlib, ggplot2 and Vega-Lite all do) and a value past the cap renders identically to the cap, so the figure cannot report the thing it was drawn to report. Comparable panels share one colorbar; a diverging map has its midpoint pinned to the meaningful zero and labeled.

## Floor: statistical honesty

Usually the weakest area of a general viz bar, because the canonical sources for it are in statistical reporting rather than visualization design.

- **An error bar without a stated meaning is not a measurement.** Name it: SD, SE, 95% CI, bootstrap percentile, or observed min-max. Readers, including expert readers, systematically misread which one they are seeing.
- **Two whiskers in one figure must not mean two different things.** If one series shows quartiles and another shows full spread, they cannot share a style.
- **State n**, and state the denominator for any rate or percentage. If two panels come from one script, both disclose it.
- **Show uncertainty, and pick the encoding for the task.** At small n, plotting every point is a strong default. Bar-plus-error-bar is legitimate when the error term is named; the failure mode is an undisclosed statistic, not the bar.
- **A symmetric interval on a bounded quantity eventually crosses the bound.** A whisker reaching a negative duration means the interval is the wrong shape, not that the axis is. Build asymmetric error from the observed quantiles when the quantity is bounded.
- **Bin width, bandwidth and rasterization resolution are analysis choices.** State the value and check the conclusion survives a different one.
- **A line through a scatter is a model.** Name it, and stop it at the data's edge.
- **Parts of a whole must reach the whole, and the whole must be named.**
- **Silence and zero look identical on a chart.** Draw a gap, a hatch, or a labeled "no data" band. Never let a dropped row, an interpolation, or a defaulted lookup turn missing data into an observation or missing uncertainty into displayed precision.
- **If the axis limits exclude points, say how many.**
- **Categorical order is an encoding.** Sort by value, by a natural sequence, or by an order you can name, never by whatever order the dataframe happened to be in. An inherent sequence outranks sorting by size. This is the characteristic failure of *programmatic* plotting specifically, and it is invisible to anyone reviewing the design rather than the pipeline.

## Floor: accessibility

- **Contrast:** 4.5:1 for normal text, 3:1 for graphical objects.
- **Never encode in red-versus-green alone.** It is the most common color-vision-deficiency confusion and it smuggles in a good-versus-bad reading the data may not support. Pair with shape, line style or position. An established semantic convention can outrank perceptual optimization; say so in the caption when it does.
- **Simulate color vision deficiency rather than eyeballing it.** It takes about fifteen lines of numpy and no extra dependency. See [checks](wiki/checks/matplotlib.md).
- **Grayscale survival.** Color distinction must hold in grayscale. Cheapest proxy for a luminance failure, and print still exists.
- **Alt text and a long description** for any figure published outside a notebook. The short one identifies it; the long one carries the scales, values and trends a sighted reader gets for free.
- **The underlying numbers are reachable.** A linked table is what a screen-reader user, or anyone who wants to check you, actually needs.

**Do not re-derive the accessibility list.** [Chartability](https://chartability.fizz.studio/) publishes 50 heuristics under CC-BY-SA with a 14-test shortlist runnable in 20 to 40 minutes, and invites adoption. The bullets above are roughly three of its fifty.

## Ceiling: how a figure argues

Scales with role. Skip deliberately on an instructional or diagnostic figure.

- **Clarity is the communicator's responsibility.** Title, labels and on-figure annotation alone answer "what am I looking at?"
- **Annotate the insight in the title.** "Engineering connects to Sales 3x more than Sales connects internally" beats "Network of departments."
- **Write the title for the artifact's audience, not for the room.** When the person you are talking to differs from whoever eventually reads the figure, the eventual reader wins. The tell is insider framing.
- **Color focuses attention; it does not decorate.** Default to a muted hue for the bulk and one saturated accent for what the eye should land on. Two saturated colors compete and neither reads as the answer. Note this is a **default, not a measured result**: no controlled study tests one-accent against two-saturated emphasis.
- **Label directly when you can.** Every glance to a side legend is overhead. When the legend would carry two or three entries, consider putting those words in the title, colored to match what they label. Color tokens must match the encoding exactly, or the title lies. **And use it only when the color reinforces a distinction the reader can already see another way**, such as position or ordering. If color in the title is the *only* thing separating two series, you have moved the legend into the sentence without making the figure any more readable.
- **Cap categorical hues at five to seven.** Past that, switch to small multiples, direct labeling, or aggregation.
- **Hold one color mapping across a figure set.** Once a group is blue, it is blue in every figure in the document.
- **Small multiples beat overlaid spaghetti**, at identical scales. Free scales must be labeled as such.
- **Use grouping, alignment and white space deliberately.** Proximity and similarity group elements whether you intended it or not, so check what your layout implicitly claims is related.
- **Every mark on the canvas is explained.** A highlight marker needs a name in the title or an annotation; an unexplained colored dot is noise.
- **Text case:** pick a convention and hold it across the set.

## Encoding choices that are usually right

- **Encode magnitude in position and length.** The most precise pre-attentive channels. Prefer axis position over area or color.
- **Scale marker size by area, not radius.** Doubling a radius quadruples the ink.
- **Match palette type to data type.** Sequential for ordered, diverging around a meaningful midpoint, cyclic for wraparound, qualitative for unordered. A sequential ramp on an unordered category invents an ordering the data does not have.
- **Default to a perceptually uniform ramp** (viridis, cividis, magma) on ordered data, and avoid rainbow and jet: non-monotonic luminance fabricates banding and collapses in grayscale. State it as a strong default rather than a law; the ban is contested at the edges, and at least one major library ships turbo as its default continuous scheme.
- **Double-encode what matters.** When more than two series must be told apart, vary two channels so no single one is load-bearing.
- **Tame density with structure, not just transparency.** A 1000-point blob at low alpha is still a blob. Filter, bin, or facet before relying on alpha.
- **Maximize data-ink, within reason.** Drop 3D, shadows, gradients, heavy frames. But the effect is element-conditional, not monotone: removing axis lines measurably *hurts* reading speed, and the chartjunk literature is contested in both directions. Strip decoration, keep orientation.

## Production and reproducibility

Under-served by bars written for newsrooms, and unusually mechanizable.

- **Vector for line art, raster only when the mark count demands it. Never JPEG a chart.**
- **Set size and DPI for the destination**, then look at the figure at that size.
- **A figure is reproducible when the data and every transformation are specified, and repeatable when it regenerates byte-identically.** Seed anything stochastic, jitter included.
- **No manual post-hoc editing inside a reproducible pipeline.** If a figure needed hand-fixing, fix the code.
- **House style belongs in a theme, not per-call kwargs.** A style file is a default a figure cannot forget; a rule in a document is a default a figure can.

## Before shipping

Run these. Most are one line, and [checks](wiki/checks/matplotlib.md) has the runnable form of every one.

- Simulate color vision deficiency, or at minimum confirm no two encoded series differ *only* in hue.
- Check contrast numerically rather than by eye.
- Check the axis range against the data range, and check whether either axis is inverted.
- Sweep the rendered text for raw floats.
- Check tick and annotation labels for collisions **at the size the figure will be viewed**, especially annotations placed relative to data values, which move when the data does.
- Read the figure back cold: do the title, labels and annotations alone answer "what am I looking at, and what am I supposed to take away?"
- Confirm grayscale survival.

## On confidence

Where a rule here is backed by an experiment, it is stated flatly. Where it is a design convention the evidence contests, it is stated as a default with its exception named. **Do not upgrade a convention into a finding when quoting this file.**

Several widely repeated rules did not survive contact with their primary sources, including bank-to-45-degrees, the axis-break remedy, a flat dual-axis ban, and "log scales are fine for experts". The corrections, with quotes, are in [refutations](wiki/refutations.md). The full 92-topic derivation and its per-source audit trail are in [inventory](wiki/inventory.md) and [roll-call](wiki/roll-call.md).
