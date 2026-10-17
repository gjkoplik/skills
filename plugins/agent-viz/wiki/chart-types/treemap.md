---
type: chart-type
relationships: [part-to-whole, magnitude]
aliases: [Treemap]
---

# Treemaps

A rectangle recursively subdivided so that each sub-rectangle's area is proportional to its value.

## When to reach for it, and when not

The form is defined for part-to-whole on a fixed canvas, with too many parts for another form or a hierarchy that is itself the point. It trades value-reading accuracy for showing hundreds of parts at once. That density is why the form exists. No study here measures it, and it is `authority-asserted`.

| The question | Alternative |
|---|---|
| Which is biggest, and in what order? | Sorted bar chart. Area does not support reliable ordering by eye |
| How does this compare to last quarter? | Anything else. Layout recomputes per dataset |
| There are eight parts and no hierarchy | [Pie](pie-and-donut.md) or a bar chart. The density goes unused |
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

The layout algorithm sits in the transform slot, so the same data can produce very different treemaps and the layout is an encoding decision.

## Channels

Rectangular area, read less accurately than position or length ([channels.md](../concepts/channels.md)), but about as accurately as circular area. [Heer & Bostock](../studies/heer-bostock-2010.md), experiment 1B: "The results confirm our hypothesis that, on average, the accuracy of rectangular area judgments matches that of circular area judgments."

With no common baseline and no axis, position carries no magnitude, aligned or not.

## What is measured

Value extraction is weak. Area reads worse than position and angle, `evidence-backed` via Heer & Bostock.

The rest of the treemap does not interfere with the judgment, `evidence-backed`. Judging bare center-aligned rectangles and the same rectangles inside a full treemap showed no significant difference, "suggesting that other elements in a treemap display do not interfere with judgment accuracy." They did not vary color intensity, so interference in a colored treemap is unmeasured.

Rectangles with aspect ratio 1 were the worst case for area comparison, in both the bare-rectangle and the treemap condition, `evidence-backed`:

> "Somewhat surprisingly, comparisons of rectangles with aspect ratio 1 exhibited the worst performance, a result robust across both the rectangle and treemap display conditions. This finding suggests that viewers actually benefit from the inability of a squarified treemap algorithm to perfectly optimize the rectangles to 1:1 aspect ratios."

Squarified algorithms exist to drive aspect ratios toward 1, so the worst case is the one they aim for. The authors' mechanism, side lengths as a proxy for area, is a hypothesis: "Additional experimentation is needed to form an accurate perceptual model." Aspect-ratio extremes went unprobed, so the result does not reach "avoid squarified layouts".

Nothing is contested. The algorithms' design rationale was never tested this way, which is `absence of evidence`, not a contest.

## The failure mode it invites

**Reading a treemap as a ranking.** Similar-sized rectangles are not reliably orderable by eye, and the layout puts large rectangles in a corner, which reads as extra importance. `authority-asserted`.

**Comparing across two treemaps.** Layout depends on the whole dataset, so categories move and change shape.

## Justifying the choice

**Defensible, evidence-backed:**

- "Rectangular area reads about as accurately as circular area, so nothing is lost by using rectangles rather than bubbles here."
- "The surrounding rectangles do not degrade the judgment: bare rectangles and full-treemap conditions showed no significant difference."

**Defensible, with the label said out loud:**

- "A treemap because there are two hundred parts in a hierarchy and no other part-to-whole form shows them at once. That is what the form is for; it is not a claim that readers extract values well from it."

**Commonly repeated, and the evidence does not support it:**

- ~~"Squarified layouts are better because near-1 aspect ratios are easier to compare."~~ Aspect ratio 1 measured worst, in both display conditions.
- ~~"You can see which of these two is bigger."~~ Not reliably, from area, for similar sizes.

## See also

- [../studies/heer-bostock-2010.md](../studies/heer-bostock-2010.md): the area, treemap and square results
- [../concepts/channels.md](../concepts/channels.md)
- [part-to-whole.md](part-to-whole.md): the group, and the trade this form makes
