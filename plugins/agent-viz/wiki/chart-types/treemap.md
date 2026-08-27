---
type: chart-type
relationships: [part-to-whole, magnitude]
aliases: [Treemap]
---

# Treemaps

A rectangle recursively subdivided so that each sub-rectangle's area is proportional to its value. The standard answer for part-to-whole with hierarchy or with many parts.

## When to reach for it, and when not

**Reach for it when** there are too many parts to label in any other part-to-whole form, or when the parts nest in a hierarchy and the hierarchy is part of the point, and the canvas is fixed. It is the form that trades value-reading accuracy for showing hundreds of parts at once.

**Do not reach for it when:**

| The question | Use instead |
|---|---|
| Which is biggest, and in what order? | Sorted bar chart. Area does not support reliable ordering by eye |
| How does this compare to last quarter? | Anything else. Layout recomputes per dataset, so nothing is positionally stable |
| There are eight parts and no hierarchy | [Pie](pie-and-donut.md) or a bar chart. The treemap's density is not being used |
| How big is this part, precisely? | Bar chart. Position instead of area |

## Structural decomposition

| Slot | |
|---|---|
| Data | One row per leaf, with a magnitude and a path through a hierarchy |
| Transform | Roll up to internal nodes, then run a layout (slice-and-dice, squarified, Voronoi) |
| Geometry | Rectangle |
| Scale | Magnitude to area |
| Coordinates | Cartesian, recursively subdivided |
| Guides | Labels in place. No axis exists |

The **layout algorithm sits in the transform slot**, which is why treemaps with the same data can look entirely different and why layout choice is a data-encoding decision rather than a styling one.

## Channels

Rectangular area, which is read less accurately than position or length ([channels.md](../concepts/channels.md)).

Two things follow immediately, and both are measured rather than assumed:

**Rectangular area is about as accurate as circular area.** Heer & Bostock, experiment 1B: "The results confirm our hypothesis that, on average, the accuracy of rectangular area judgments matches that of circular area judgments." So a treemap is not paying an extra penalty for using rectangles rather than bubbles.

**Position contributes nothing.** Rectangles float in a subdivided plane with no common baseline and no axis. The treemap gives up both position readings entirely, along a common scale and along nonaligned scales, which is the price of packing hundreds of parts into a fixed canvas.

## What it is measurably good at

**Not interfering with itself.** Heer & Bostock found no significant difference between judging bare center-aligned rectangles and judging the same rectangles inside a full treemap, "suggesting that other elements in a treemap display do not interfere with judgment accuracy." The surrounding clutter is free, which is not obvious and is worth knowing.

The authors flag one untested extension: they did not vary color intensity, so interference from a colored treemap is unmeasured.

**Density.** A treemap shows hundreds of parts in a fixed area with every part visible. No study here measures this and it is the entire reason the form exists. `authority-asserted`.

## What it is measurably bad at

**Value extraction**, on area, which is read worse than position and worse than angle. Evidence-backed via Heer & Bostock.

**Squares specifically.**

> "Somewhat surprisingly, comparisons of rectangles with aspect ratio 1 exhibited the worst performance, a result robust across both the rectangle and treemap display conditions. This finding suggests that viewers actually benefit from the inability of a squarified treemap algorithm to perfectly optimize the rectangles to 1:1 aspect ratios."

Squarified treemap algorithms exist to drive aspect ratios toward 1. On this evidence, the closer they get to that goal, the worse the comparison accuracy. The proposed mechanism, that viewers compare side lengths as a proxy for area and that this proxy is maximally ambiguous between squares, is offered by the authors as consistent rather than demonstrated: "Additional experimentation is needed to form an accurate perceptual model."

**Treat the effect as measured and the explanation as a hypothesis.** And note the practical implication is not "avoid squarified layouts," since aspect-ratio extremes have their own problems that this experiment's range does not probe.

## What is contested

**Nothing directly**, but the aspect-ratio result sits awkwardly against the layout literature's stated goal without anyone having resolved it. That is closer to `absence of evidence` than to a contest: one experiment found squares worst, and the layout algorithms were designed on a different rationale that was never tested this way.

## The failure mode it invites

**Reading a treemap as a ranking.** Adjacent rectangles of similar size are not reliably orderable by eye from area alone, and the layout puts large rectangles in a corner, which reads as importance beyond what the areas encode. If the reader's question is "which is biggest," a sorted bar chart answers it with position. `authority-asserted`.

**Comparing across two treemaps.** Layout is a function of the whole dataset, so the same category lands in a different place and shape in each. Nothing survives the comparison.

## Justifying the choice

**Defensible, evidence-backed:**

- "Rectangular area reads about as accurately as circular area, so nothing is lost by using rectangles rather than bubbles here."
- "The surrounding rectangles do not degrade the judgment: bare rectangles and full-treemap conditions showed no significant difference."

**Defensible, with the label said out loud:**

- "A treemap because there are two hundred parts in a hierarchy and no other part-to-whole form shows them at once. That is what the form is for; it is not a claim that readers extract values well from it."

**Not defensible:**

- ~~"Squarified layouts are better because near-1 aspect ratios are easier to compare."~~ Measured, aspect ratio 1 was the **worst** case, robust across both display conditions. Treat the effect as real and the side-length-proxy explanation as the authors' hypothesis rather than an established mechanism.
- ~~"You can see which of these two is bigger."~~ Not reliably, from area, for similar sizes.

## See also

- [../studies/heer-bostock-2010.md](../studies/heer-bostock-2010.md) — rectangular area, the treemap condition, and the square result
- [../concepts/channels.md](../concepts/channels.md)
- [part-to-whole.md](part-to-whole.md) — the category, and the trade this form makes
