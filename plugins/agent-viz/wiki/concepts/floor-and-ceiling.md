---
type: concept
---

# The floor and the ceiling

**What it is.** A way of scoping a figure quality bar so that it can be large without being wrong. Some rules bind on every figure. Others scale with what the figure is for. Conflating them makes a good bar produce bad review.

**Status.** Synthesis, arrived at by this project rather than taken from a source. No published equivalent was found, which is not the same as none existing.

**What it is good for.** Deciding whether a specific figure's plainness is a defect or a correct choice.

**What it does not settle.** Where exactly the line sits for any given rule. The split is a structure, not an algorithm, and a few rules sit genuinely near the boundary.

---

## The problem it solves

A quality bar grows. Every gap someone notices becomes another rule, and the rules are individually reasonable. Then someone applies the whole list to a figure whose entire job is to show what a function parameter does, and produces forty findings against a two-line demo.

That review is wrong, and it is wrong in a way that discredits the bar. The author knows their figure is fine. What they conclude is that the bar has no judgment, and they stop reading it.

The failure is not that the bar has too many rules. It is that the bar has no way to say which of its rules are conditional.

## The split

**The floor binds on every figure regardless of role.** Quantitative honesty, statistical honesty, accessibility.

Break one and the figure is *wrong*, or it is unreadable to some of the people looking at it. Neither of those is excused by the figure being quick, internal, or pedagogical. A teaching figure that misleads teaches the wrong thing, and a reader with a color-vision deficiency is a real reader whether the figure is a paper hero or a docs aside.

**The ceiling scales with the figure's job.** Narrative titles, emphasis palettes, direct labeling, annotation, alignment craft.

This is the machinery by which a figure *argues*. A figure that is not making an argument does not need it, and spending effort there is not neutral: on an instructional figure, every line of styling is a line the reader has to skip to find the API call they came for.

## Roles

- **Storytelling.** A finding, a paper figure, a blog post, a README hero. Owes the floor and the ceiling.
- **Instructional.** A demo of what a parameter or method does, where the *code* is as much the artifact as the picture. Owes the floor. Its real quality bar is minimal, clean, copy-able source. A plain literal title, library-default colors and no custom legend are **correct** here.
- **Diagnostic.** Something you will look at once. Owes the floor, and barely that: it needs to not mislead *you*.

## The asymmetry that keeps this honest

Minimalism wins a lot of arguments in the instructional case. It never wins this one:

**Minimal code buys API comprehension. It never buys a misleading axis.**

A truncated baseline, an unlabeled log scale, a silently clipped colorbar or an undisclosed error bar is as wrong in a two-cell demo as in a paper figure, and worse in one respect. The reader is there to learn the idiom, and they will copy it.

## The other constraint people miss

A figure can be subject to constraints that operate at the level of the **document set** rather than the figure. The clearest example: deliberately orthogonalizing colors across a gallery so neighboring entries stay visually distinguishable. A palette that looks arbitrary in isolation can be correct in context, and a reviewer looking at one figure cannot see the constraint.

The pushback that still applies: **orthogonalize inside the floor, not out of it.** Differentiating by reaching for a rainbow ramp on ordered data, or a red-against-green pairing, buys distinctiveness with a floor violation. There is room to differentiate among perceptually safe options.

## Where the boundary is genuinely arguable

Stated rather than hidden:

- **Alt text.** Accessibility, so floor by the logic above. But the notebook and pipeline tooling frequently does not support it, which makes it a floor rule that a whole medium cannot satisfy. Current resolution: floor where the medium supports it.
- **"Every mark on the canvas is explained."** Reads like clarity, which is ceiling. But an unexplained encoded value is closer to a correctness problem than a polish problem, so it sits on the floor here.
- **Axis titles with units.** Arguably clarity. Treated as floor, because a unitless quantitative axis is not merely unpolished, it is ambiguous about what was measured.

If you disagree with any of these placements, the structure survives the disagreement. That is the point of separating the structure from the assignments.

## See also

- [evidence-class.md](evidence-class.md): the other axis a rule should carry
- [../inventory.md](../inventory.md): the topics being scoped
- [../refutations.md](../refutations.md): why several ceiling rules cannot be stated as flatly as they usually are
