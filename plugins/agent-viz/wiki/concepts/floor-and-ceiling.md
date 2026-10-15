---
type: concept
---

# The floor and the ceiling

**What it is.** A way of scoping a figure quality bar so it can be large without being wrong. Some rules bind on every figure, and others scale with what the figure is for. Conflating the two makes a good bar produce bad review.

**Status.** Synthesis by this project. No published equivalent was found, which is not the same as none existing.

**What it is good for.** Deciding whether a figure's plainness is a defect or a correct choice.

**What it does not settle.** Where the line sits for a given rule. The split is a structure, not an algorithm.

---

## The problem it solves

A quality bar grows one reasonable rule at a time. Applied whole to a two-line demo of a function parameter, it produces forty findings. The author knows the figure is fine, concludes the bar has no judgment, and stops reading. The bar has no way to mark a rule conditional.

## The split

**The floor** binds on every figure: quantitative honesty, statistical honesty, accessibility. Breaking one makes the figure wrong, or unreadable to some readers, and being quick, internal or pedagogical is no excuse. A misleading teaching figure teaches the wrong thing.

**The ceiling** scales with the figure's job: narrative titles, emphasis palettes, direct labeling, annotation, alignment craft. It is how a figure argues. On an instructional figure, styling is what the reader skips to find the API call.

## Roles

- **Storytelling.** A finding, a paper figure, a blog post, a README hero. Owes the floor and the ceiling.
- **Instructional.** A demo of a parameter or method, where the code matters as much as the picture. Owes the floor. Its quality bar is minimal, copyable source, so a plain literal title, library-default colors and no custom legend are correct.
- **Diagnostic.** A figure looked at once. Owes the floor, and barely that: it must not mislead its own author.

## The asymmetry

Minimal code buys API comprehension. It never buys a misleading axis. A truncated baseline, an unlabeled log scale, a silently clipped colorbar or an undisclosed error bar is as wrong in a two-cell demo as in a paper figure, and worse, because the reader came to learn the idiom and will copy it.

## Document-set constraints

Some constraints bind the **document set**. Colors orthogonalized across a gallery keep neighbors distinguishable, so a palette that looks arbitrary to a reviewer of one figure can be correct in context. That differentiation still happens inside the floor. A rainbow ramp on ordered data or a red-against-green pairing buys distinctiveness with a floor violation.

## Where the boundary is arguable

- **Alt text.** Accessibility, so floor, but notebook and pipeline tooling often cannot carry it. It is floor where the medium supports it.
- **"Every mark on the canvas is explained."** Reads like ceiling clarity, but an unexplained encoded value is closer to a correctness problem, so it is floor.
- **Axis titles with units.** Treated as floor, because a unitless quantitative axis is ambiguous about what was measured.

Disagreement about a placement leaves the structure intact.

## See also

- [evidence-class.md](evidence-class.md): the other axis a rule should carry
- [../inventory.md](../inventory.md): the topics being scoped
- [../refutations.md](../refutations.md): why several ceiling rules carry hedges
